# Project structure: hackerkid/Mind-Expanding-Books

**Analysed commit:** `2844c5ad5e1f4da8a637c74503763a2cb56f5550`

**Commit reference:** [2844c5ad5e1f4da8a637c74503763a2cb56f5550](https://github.com/hackerkid/Mind-Expanding-Books/commit/2844c5ad5e1f4da8a637c74503763a2cb56f5550)

**Tree at this commit:** [hackerkid/Mind-Expanding-Books@2844c5ad5e1f](https://github.com/hackerkid/Mind-Expanding-Books/tree/2844c5ad5e1f4da8a637c74503763a2cb56f5550)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | hackerkid/Mind-Expanding-Books |
| Description |  :books: Find your next book to read! |
| Stars | 14559 |
| Forks | 1178 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `2844c5ad5e1f4da8a637c74503763a2cb56f5550` |
| Retrieved at | 2026-11-14T19:11:44.817059+00:00 |
| Files in this snapshot | 51 |

## Directory tree

```text
.github/  (1 files)
  PULL_REQUEST_TEMPLATE.md
app/  (36 files)
  src/  (23 files)
    components/  (13 files)
      … 13 files under this directory
    context/  (2 files)
      … 2 files under this directory
    data/  (1 files)
      … 1 files under this directory
    pages/  (4 files)
      … 4 files under this directory
    styles/  (2 files)
      … 2 files under this directory
    templates/  (1 files)
      … 1 files under this directory
  .eslintrc.js
  .gitignore
  .prettierignore
  .prettierrc
  .prettierrc.json
  LICENSE
  README.md
  gatsby-browser.js
  gatsby-config.js
  gatsby-node.js
  gatsby-ssr.js
  package.json
  postcss.config.js
utils/  (11 files)
  .gitignore
  HOUSEKEEPING.md
  README.MD
  config-sample.py
  gooodreads.py
  housekeep.py
  pyvenv.cfg
  read_file.py
  requirements.txt
  update_json_files.py
  write_file.py
.gitignore
CONTRIBUTING.md
README.md
```

## Entry points

- [utils/housekeep.py:76](https://github.com/hackerkid/Mind-Expanding-Books/blob/2844c5ad5e1f4da8a637c74503763a2cb56f5550/utils/housekeep.py#L76)
- [utils/update_json_files.py:56](https://github.com/hackerkid/Mind-Expanding-Books/blob/2844c5ad5e1f4da8a637c74503763a2cb56f5550/utils/update_json_files.py#L56)
- [app/src/pages/index.js](https://github.com/hackerkid/Mind-Expanding-Books/blob/2844c5ad5e1f4da8a637c74503763a2cb56f5550/app/src/pages/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 25 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: book_has_all_fields, clean_category, format_library, main, sort, validate_bookcover. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 4 file(s) under utils package (observed from repository paths and static analysis). Observed top-level functions: get_details, get_goodread_info, load, parse_book_string, parse_book_string_new, read_file_content. |

## Important files

- `app/.prettierrc.json` (config)
- `app/package.json` (manifest)
- `app/src/data/categories.json` (config)
- `utils/pyvenv.cfg` (config)
- `utils/requirements.txt` (manifest)

## Top-level layout

- `app` — 36 analysed file(s)
- `utils` — 11 analysed file(s)
- `(root files)` — 3 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `2844c5ad5e1f4da8a637c74503763a2cb56f5550` is the revision these paths and observations refer to.
