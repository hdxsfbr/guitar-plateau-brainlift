# Task 4 build scripts (snapshot)

These are the scripts Grok Bot used on its own box to build `research/source-register.csv`, `research/evidence.csv` and `research/manual-sources/`. They are kept for transparency.
- Paths are hard-coded to the box (`/workspace/bl2/...`), and the full-text PDFs and abstract cache they read are not committed, so they will not run as-is.
- `vq.py` contains the quote-normalization and matching rules (yes / near / no).
- `searchlog.tsv` is the raw manual-search log that the `research/search-log.md` table was rendered from.
