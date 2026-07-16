"""
Inject local-only credentials into pages that contain:

    <!-- PRIVATE_CREDENTIALS -->

Reads `private/credentials.md` from the project root when present.
On machines / CI without that file, or when MKDOCS_PUBLIC=1, inserts a safe
public placeholder (so `mkdocs gh-deploy` never publishes passwords).
"""

from __future__ import annotations

import os
from pathlib import Path

MARKER = "<!-- PRIVATE_CREDENTIALS -->"

PUBLIC_PLACEHOLDER = """\
<div class="quote-box">
<div class="quote-box__body">
<p><em>Login details are stored in the local-only file <code>private/credentials.md</code> (gitignored) and are not published. Copy <code>private/credentials.example.md</code> → <code>private/credentials.md</code> on your machine to see them when you build locally.</em></p>
</div>
</div>
"""

LOCAL_WRAPPER_START = '<div class="note-box">\n<p class="note-box__title">Local credentials (not published)</p>\n<div class="note-box__body">\n\n'
LOCAL_WRAPPER_END = "\n\n</div>\n</div>\n"


def _public_build() -> bool:
    flag = os.environ.get("MKDOCS_PUBLIC", "").strip().lower()
    if flag in {"1", "true", "yes"}:
        return True
    if os.environ.get("CI", "").strip().lower() in {"1", "true"}:
        return True
    return False


def on_page_markdown(markdown, page, config, files):
    if MARKER not in markdown:
        return markdown

    project_root = Path(config["docs_dir"]).parent
    creds = project_root / "private" / "credentials.md"

    if (not _public_build()) and creds.is_file():
        body = creds.read_text(encoding="utf-8").strip()
        lines = body.splitlines()
        if lines and lines[0].startswith("# "):
            body = "\n".join(lines[1:]).strip()
        replacement = LOCAL_WRAPPER_START + body + LOCAL_WRAPPER_END
    else:
        replacement = PUBLIC_PLACEHOLDER

    return markdown.replace(MARKER, replacement)
