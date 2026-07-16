"""
Auto-generate a Change log on the home page from:
1) <p class="section-updated">Last updated: ...</p> stamps under headings
2) markdown file modification times

Updates on every `mkdocs serve` / `mkdocs build` rebuild.
"""

from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

UPDATED_RE = re.compile(
    r'<p\s+class="section-updated">\s*Last updated:\s*([^<]+?)\s*</p>',
    re.I,
)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")

SKIP_TITLES = {
    "change log",
    "changelog",
    "issw project overview",
}

DATE_FORMATS = (
    "%d %b %Y",
    "%d %B %Y",
    "%Y-%m-%d",
    "%b %d %Y",
    "%B %d %Y",
)


def parse_date(text: str) -> datetime | None:
    text = text.strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue
    return None


def page_label(rel: str) -> str:
    if rel == "index.md":
        return "Home"
    if rel.endswith("/index.md"):
        return rel[: -len("/index.md")]
    if rel.endswith(".md"):
        return rel[:-3]
    return rel


def collect_section_entries(docs_dir: Path) -> list[dict]:
    entries: list[dict] = []
    for md in sorted(docs_dir.rglob("*.md")):
        rel = md.relative_to(docs_dir).as_posix()
        text = md.read_text(encoding="utf-8")
        lines = text.splitlines()
        for i, line in enumerate(lines):
            hm = HEADING_RE.match(line)
            if not hm:
                continue
            title = hm.group(2).strip()
            if title.lower() in SKIP_TITLES:
                continue
            date = None
            for j in range(i + 1, min(i + 6, len(lines))):
                if HEADING_RE.match(lines[j]):
                    break
                um = UPDATED_RE.search(lines[j])
                if um:
                    date = parse_date(um.group(1))
                    break
            if date is None:
                continue
            entries.append(
                {
                    "date": date,
                    "title": title,
                    "page": page_label(rel),
                    "kind": "section",
                }
            )
    return entries


def collect_file_entries(docs_dir: Path) -> list[dict]:
    entries: list[dict] = []
    for md in sorted(docs_dir.rglob("*.md")):
        rel = md.relative_to(docs_dir).as_posix()
        if rel == "index.md":
            continue
        mtime = datetime.fromtimestamp(md.stat().st_mtime)
        entries.append(
            {
                "date": mtime,
                "title": f"Page edited — {page_label(rel)}",
                "page": page_label(rel),
                "kind": "file",
            }
        )
    return entries


def format_changelog(entries: list[dict], limit: int = 50) -> str:
    lines = [
        "",
        "## Change log",
        "",
        '<p class="section-updated">Auto-updated on each site rebuild</p>',
        "",
        "_Built from section “Last updated” stamps and page file times._",
        "",
    ]
    if not entries:
        lines.append("_No changes recorded yet._")
        lines.append("")
        return "\n".join(lines)

    # Prefer one entry per (page, title, calendar day); keep newest kinds
    seen: set[tuple] = set()
    unique: list[dict] = []
    for e in sorted(entries, key=lambda x: x["date"], reverse=True):
        key = (e["page"], e["title"], e["date"].date(), e["kind"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(e)

    current_day = None
    count = 0
    for e in unique:
        if count >= limit:
            break
        # Skip file-level entries when a section stamp exists same day/page
        # (keep file entries; they're useful). Show time for file edits.
        day = e["date"].strftime("%d %b %Y")
        if day != current_day:
            current_day = day
            lines.append(f"### {day}")
            lines.append("")
        if e["kind"] == "file":
            time_s = e["date"].strftime("%H:%M")
            lines.append(f"- {e['title']} _{time_s}_")
        else:
            lines.append(f"- **{e['title']}** — `{e['page']}`")
        count += 1

    lines.append("")
    return "\n".join(lines)


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "index.md":
        return markdown

    docs_dir = Path(config["docs_dir"])
    entries = collect_section_entries(docs_dir) + collect_file_entries(docs_dir)
    block = format_changelog(entries)

    marker = "<!-- AUTO_CHANGELOG -->"
    if marker in markdown:
        return markdown.replace(marker, block)
    return markdown.rstrip() + "\n" + block
