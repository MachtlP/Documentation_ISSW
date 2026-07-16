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

## Publish to GitHub Pages (`*.github.io`)

This repo has a GitHub Action that builds with `MKDOCS_PUBLIC=1` (no passwords) and deploys to Pages on every push to `main`.

**One-time setup in GitHub**

1. Open the repo → **Settings** → **Pages**
2. Under **Build and deployment**, set **Source** to **GitHub Actions**
3. Push to `main` (or run the workflow manually under **Actions**)

Site URL (after the first successful deploy):

https://machtlp.github.io/Documentation_ISSW/

**Note:** Your repo is **private**. GitHub Pages on a private repo needs GitHub Pro/Team (or make the repo public). The Action still builds either way.

**Manual deploy alternative (from your Mac):**

```bash
MKDOCS_PUBLIC=1 mkdocs gh-deploy
```
