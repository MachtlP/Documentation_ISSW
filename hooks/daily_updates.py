"""
Inject §1 Daily Updates on the home page.

Sources (newest first):
1) Curated files in docs/daily-updates/YYYY-MM-DD.md  (preferred for that day)
2) Git commits on that calendar day (auto), for days without a curated file

Runs on every mkdocs build / serve — including GitHub Pages deploys after push.
"""

from __future__ import annotations

import re
import subprocess
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

MARKER = "<!-- AUTO_DAILY_UPDATES -->"
DATE_FILE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})\.md$")
MAX_DAYS = 30


def repo_root(docs_dir: Path) -> Path:
    return docs_dir.parent


def load_curated(updates_dir: Path) -> dict[date, str]:
    curated: dict[date, str] = {}
    if not updates_dir.is_dir():
        return curated
    for path in sorted(updates_dir.glob("*.md"), reverse=True):
        m = DATE_FILE_RE.match(path.name)
        if not m:
            continue
        day = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        body = path.read_text(encoding="utf-8").strip()
        if body:
            curated[day] = body
    return curated


def git_commits_by_day(root: Path, since: date) -> dict[date, list[tuple[str, str]]]:
    """Return {date: [(short_sha, subject), ...]} newest commits first per day."""
    since_s = since.isoformat()
    try:
        out = subprocess.check_output(
            [
                "git",
                "-C",
                str(root),
                "log",
                f"--since={since_s} 00:00:00",
                "--date=short",
                "--pretty=format:%h%x09%ad%x09%s",
            ],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return {}

    by_day: dict[date, list[tuple[str, str]]] = defaultdict(list)
    for line in out.splitlines():
        parts = line.split("\t", 2)
        if len(parts) != 3:
            continue
        sha, day_s, subject = parts
        try:
            day = datetime.strptime(day_s.strip(), "%Y-%m-%d").date()
        except ValueError:
            continue
        by_day[day].append((sha.strip(), subject.strip()))
    return dict(by_day)


def escape_html(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def md_body_to_html(body: str) -> str:
    """Minimal markdown → HTML for daily-update bodies (paragraphs + lists + `code`)."""
    lines = body.splitlines()
    html: list[str] = []
    in_list = False

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            html.append("</ul>")
            in_list = False

    def inline(s: str) -> str:
        # Protect markdown links before HTML-escaping
        links: list[tuple[str, str]] = []

        def stash_link(m: re.Match[str]) -> str:
            links.append((m.group(1), m.group(2)))
            return f"\x00LINK{len(links) - 1}\x00"

        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", stash_link, s)
        s = escape_html(s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        for i, (label, href) in enumerate(links):
            label_html = escape_html(label)
            label_html = re.sub(r"`([^`]+)`", r"<code>\1</code>", label_html)
            label_html = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", label_html)
            href_html = escape_html(href)
            s = s.replace(
                f"\x00LINK{i}\x00",
                f'<a href="{href_html}">{label_html}</a>',
            )
        return s

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            close_list()
            continue
        if line.lstrip().startswith("- "):
            if not in_list:
                html.append("<ul>")
                in_list = True
            html.append(f"<li>{inline(line.lstrip()[2:].strip())}</li>")
            continue
        close_list()
        html.append(f"<p>{inline(line)}</p>")
    close_list()
    return "\n".join(html)


def format_day_block(day: date, body_md: str, source: str) -> str:
    day_label = day.strftime("%d %b %Y")
    source_note = (
        "Curated summary"
        if source == "curated"
        else "Auto from git commits (this push / rebuild)"
    )
    body_html = md_body_to_html(body_md)
    return "\n".join(
        [
            f"### {day_label}",
            "",
            f'<p class="section-updated">{source_note}</p>',
            "",
            '<div class="daily-update-box">',
            '<div class="daily-update-box__body">',
            body_html,
            "</div>",
            "</div>",
            "",
        ]
    )


def commits_to_markdown(commits: list[tuple[str, str]]) -> str:
    lines = []
    for sha, subject in commits:
        lines.append(f"- `{sha}` — {subject}")
    return "\n".join(lines)

def build_section(docs_dir: Path) -> str:
    updates_dir = docs_dir / "daily-updates"
    curated = load_curated(updates_dir)
    today = date.today()
    since = today - timedelta(days=MAX_DAYS)
    commits = git_commits_by_day(repo_root(docs_dir), since)

    days = sorted(set(curated) | set(commits), reverse=True)
    days = [d for d in days if d >= since][:MAX_DAYS]

    lines = [
        "",
        "## 1. Daily Updates",
        "",
        '<p class="section-updated">Auto-updated on each site rebuild / git push</p>',
        "",
        "_Curated notes in `docs/daily-updates/YYYY-MM-DD.md` override that day’s auto commit list._",
        "",
    ]

    if not days:
        lines.append("_No daily updates yet. Push commits or add a file under `docs/daily-updates/`._")
        lines.append("")
        return "\n".join(lines)

    for day in days:
        if day in curated:
            lines.append(format_day_block(day, curated[day], "curated"))
        elif day in commits and commits[day]:
            lines.append(
                format_day_block(day, commits_to_markdown(commits[day]), "git")
            )

    return "\n".join(lines)


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "index.md":
        return markdown

    block = build_section(Path(config["docs_dir"]))
    if MARKER in markdown:
        return markdown.replace(MARKER, block)
    return markdown.rstrip() + "\n" + block
