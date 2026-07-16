# ISSW Project Documentation

MkDocs site for ISSW project notes (Avapro, Spatial config, HRDPS, InfoEx).

## Local preview

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install mkdocs
mkdocs serve
```

Open http://127.0.0.1:8000/

## Private credentials

Login details live in `private/credentials.md` (gitignored).

```bash
cp private/credentials.example.md private/credentials.md
# edit with your real values
```

Local `mkdocs serve` / `mkdocs build` injects them into pages that contain `<!-- PRIVATE_CREDENTIALS -->`.

For a public deploy (no secrets):

```bash
MKDOCS_PUBLIC=1 mkdocs build
# or
MKDOCS_PUBLIC=1 mkdocs gh-deploy
```

## Build static HTML for Finder

```bash
mkdocs build
open site/index.html
```
