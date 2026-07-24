"""
Collect all todo-box blocks from docs and inject a linked summary on the home page.
"""

from __future__ import annotations

import re
from pathlib import Path

try:
    from markdown.extensions.toc import slugify as md_slugify
except ImportError:  # pragma: no cover
    def md_slugify(value, separator):
        value = re.sub(r"[^\w\s-]", "", value).strip().lower()
        return re.sub(r"[{}\s]+".format(re.escape(separator)), separator, value)


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TODO_TITLE_RE = re.compile(
    r'<p\s+class="todo-box__title">\s*(.*?)\s*</p>',
    re.I | re.S,
)
LI_RE = re.compile(r"<li>\s*(.*?)\s*</li>", re.I | re.S)
BODY_RE = re.compile(
    r'<div\s+class="todo-box__body">\s*(.*?)\s*</div>',
    re.I | re.S,
)


def page_url(rel: str) -> str:
    """MkDocs default directory URLs."""
    if rel == "index.md":
        return "."
    if rel.endswith("/index.md"):
        return rel[: -len("/index.md")] + "/"
    if rel.endswith(".md"):
        return rel[:-3] + "/"
    return rel


def page_label(rel: str) -> str:
    if rel == "index.md":
        return "Home"
    if rel.endswith("/index.md"):
        return rel[: -len("/index.md")]
    if rel.endswith(".md"):
        return rel[:-3]
    return rel


# Friendly page names (nav titles)
PAGE_TITLES = {
    "index.md": "ISSW Project Overview",
    "avapro/v1.md": "AvaPro v1",
    "avapro/v2.md": "AvaPro v2",
    "avapro/index.md": "Avapro Point Location",
    "spatial-config.md": "Spatial Config",
    "hrdps.md": "HRDPS",
    "snowpack.md": "SNOWPACK",
    "info-ex.md": "Info Ex",
}


def page_title(rel: str) -> str:
    return PAGE_TITLES.get(rel, page_label(rel))


def extract_todo_block(lines: list[str], start: int) -> tuple[str, int]:
    """Return (block_html, index_after_block)."""
    depth = 0
    block: list[str] = []
    i = start
    while i < len(lines):
        line = lines[i]
        block.append(line)
        depth += line.count("<div") - line.count("</div>")
        i += 1
        if depth <= 0:
            break
    return "\n".join(block), i


def parse_items(html: str) -> list[str]:
    items = [re.sub(r"<[^>]+>", "", m).strip() for m in LI_RE.findall(html)]
    items = [x for x in items if x]
    if items:
        return items
    body_m = BODY_RE.search(html)
    if not body_m:
        return []
    text = re.sub(r"<[^>]+>", " ", body_m.group(1))
    text = re.sub(r"\s+", " ", text).strip()
    return [text] if text else []


def collect_todos(docs_dir: Path) -> list[dict]:
    todos: list[dict] = []
    for md in sorted(docs_dir.rglob("*.md")):
        rel = md.relative_to(docs_dir).as_posix()
        if rel == "index.md":
            continue
        lines = md.read_text(encoding="utf-8").splitlines()
        current_heading = page_label(rel)
        i = 0
        while i < len(lines):
            hm = HEADING_RE.match(lines[i])
            if hm:
                current_heading = hm.group(2).strip()
                i += 1
                continue
            if '<div class="todo-box">' in lines[i] or "<div class='todo-box'>" in lines[i]:
                html, i = extract_todo_block(lines, i)
                title_m = TODO_TITLE_RE.search(html)
                box_title = re.sub(r"<[^>]+>", "", title_m.group(1)).strip() if title_m else "ToDo"
                items = parse_items(html)
                if not items:
                    i += 1
                    continue
                anchor = md_slugify(current_heading, "-")
                todos.append(
                    {
                        "page": page_title(rel),
                        "page_slug": page_label(rel),
                        "section": current_heading,
                        "box_title": box_title,
                        "items": items,
                        "url": f"{page_url(rel)}#{anchor}",
                    }
                )
                continue
            i += 1
    return todos


def format_todos(todos: list[dict]) -> str:
    lines = [
        "",
        "## Next to do's",
        "",
        '<p class="section-updated">Auto-collected from all pages on each rebuild</p>',
        "",
    ]
    if not todos:
        lines.append("_No Next to do's boxes found yet._")
        lines.append("")
        return "\n".join(lines)

    for t in todos:
        heading = f"{t['page']} › {t['section']}"
        lines.append(f"### [{heading}]({t['url']})")
        lines.append("")
        for item in t["items"]:
            lines.append(f"- {item}")
        lines.append("")
    return "\n".join(lines)


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "index.md":
        return markdown

    docs_dir = Path(config["docs_dir"])
    block = format_todos(collect_todos(docs_dir))
    marker = "<!-- AUTO_TODOS -->"
    if marker in markdown:
        return markdown.replace(marker, block)
    return markdown.rstrip() + "\n" + block
