# Project structure: AhmadHassan-BTed/Ledgerify

**Analysed commit:** `6e3c40379d762ef2a9b76d4ce48051e9cac04cbe`

**Commit reference:** [6e3c40379d762ef2a9b76d4ce48051e9cac04cbe](https://github.com/AhmadHassan-BTed/Ledgerify/commit/6e3c40379d762ef2a9b76d4ce48051e9cac04cbe)

**Tree at this commit:** [AhmadHassan-BTed/Ledgerify@6e3c40379d76](https://github.com/AhmadHassan-BTed/Ledgerify/tree/6e3c40379d762ef2a9b76d4ce48051e9cac04cbe)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | AhmadHassan-BTed/Ledgerify |
| Description | Shopify Excel Ledger intelligence platform with dark aesthetic, multi-sheet workbook analysis, 7 departmental dashboards, and live comparative benchmarking. |
| Stars | 4771 |
| Forks | 0 |
| Licence | Not detected |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `6e3c40379d762ef2a9b76d4ce48051e9cac04cbe` |
| Retrieved at | 2026-11-14T19:14:36.254580+00:00 |
| Files in this snapshot | 80 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    deploy.yml
public/  (1 files)
  logo.svg
scripts/  (3 files)
  analyze.js
  inspect.js
  inspect_sheets.js
src/  (63 files)
  components/  (32 files)
    charts/  (5 files)
      … 5 files under this directory
    layout/  (7 files)
      … 7 files under this directory
    ui/  (12 files)
      … 12 files under this directory
    views/  (8 files)
      … 8 files under this directory
  context/  (4 files)
    DataContext.tsx
    FilterContext.tsx
    ServiceContext.tsx
    ThemeContext.tsx
  core/  (16 files)
    di/  (1 files)
      … 1 files under this directory
    math/  (1 files)
      … 1 files under this directory
    parser/  (3 files)
      … 3 files under this directory
    services/  (9 files)
      … 9 files under this directory
    storage/  (2 files)
      … 2 files under this directory
  styles/  (4 files)
    themes/  (4 files)
      … 4 files under this directory
  types/  (3 files)
    analytics.ts
    filter.ts
    order.ts
  utils/  (1 files)
    datasetTitle.ts
  App.tsx
  index.css
  main.tsx
.gitignore
ARCHITECTURE.md
CHANGELOG.md
README.md
TODO.md
index.html
package.json
postcss.config.js
requirements.txt
tailwind.config.js
tsconfig.json
vite.config.ts
```

## Entry points

- [src/App.tsx](https://github.com/AhmadHassan-BTed/Ledgerify/blob/6e3c40379d762ef2a9b76d4ce48051e9cac04cbe/src/App.tsx)
- [src/main.tsx](https://github.com/AhmadHassan-BTed/Ledgerify/blob/6e3c40379d762ef2a9b76d4ce48051e9cac04cbe/src/main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 8 file(s) under api layer (observed from repository paths and static analysis). |
| App.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 24 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| context package | library | Observed | Groups 4 file(s) under context package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). |
| main.tsx package | library | Observed | Groups 1 file(s) under main.tsx package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 14 file(s) under service / domain layer (observed from repository paths and static analysis). |
| styles package | library | Observed | Groups 1 file(s) under styles package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 3 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/deploy.yml` (ci)
- `package.json` (manifest)
- `requirements.txt` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 63 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.github` — 1 analysed file(s)
- `public` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6e3c40379d762ef2a9b76d4ce48051e9cac04cbe` is the revision these paths and observations refer to.
