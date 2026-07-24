#!/usr/bin/env python3
"""
Draft today's curated daily-update file from git commits.

Usage (optional, before push):
  python scripts/draft_daily_update.py
  # edit docs/daily-updates/YYYY-MM-DD.md, then commit + push

If you skip this, the Home page still auto-lists that day's commits on rebuild.
"""

from __future__ import annotations

import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "docs" / "daily-updates"


def main() -> int:
    today = date.today()
    out = OUT_DIR / f"{today.isoformat()}.md"
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if out.exists():
        print(f"Already exists: {out}")
        print("Edit that file for a curated narrative, or delete it to regenerate.")
        return 0

    since = today.isoformat()
    try:
        log = subprocess.check_output(
            [
                "git",
                "-C",
                str(ROOT),
                "log",
                f"--since={since} 00:00:00",
                "--pretty=format:- `%h` — %s",
            ],
            text=True,
        ).strip()
    except subprocess.CalledProcessError as e:
        print("git log failed:", e, file=sys.stderr)
        return 1

    if not log:
        log = "- _(no commits yet today — add bullets manually)_"

    body = (
        f"**Focus:** _(one-line theme)_\n\n"
        f"{log}\n"
    )
    out.write_text(body, encoding="utf-8")
    print(f"Wrote {out}")
    print("Edit the Focus line / bullets, then: git add docs/daily-updates && git commit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
