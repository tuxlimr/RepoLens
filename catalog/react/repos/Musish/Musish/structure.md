# Project structure: Musish/Musish

**Analysed commit:** `9846878b0a0bb59a627d60784e092e636b933244`

**Commit reference:** [9846878b0a0bb59a627d60784e092e636b933244](https://github.com/Musish/Musish/commit/9846878b0a0bb59a627d60784e092e636b933244)

**Tree at this commit:** [Musish/Musish@9846878b0a0b](https://github.com/Musish/Musish/tree/9846878b0a0bb59a627d60784e092e636b933244)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Musish/Musish |
| Description | Apple Music...ish  |
| Stars | 3226 |
| Forks | 241 |
| Licence | AGPL-3.0 |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `9846878b0a0bb59a627d60784e092e636b933244` |
| Retrieved at | 2026-11-14T19:15:27.805899+00:00 |
| Files in this snapshot | 180 |

## Directory tree

```text
.circleci/  (3 files)
  config.yml
  deploy.sh
  generate_structure.sh
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  FUNDING.yml
src/  (164 files)
  app/  (154 files)
    assets/  (5 files)
      … 5 files under this directory
    components/  (122 files)
      … 122 files under this directory
    hoc/  (3 files)
      … 3 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    services/  (3 files)
      … 3 files under this directory
    types/  (4 files)
      … 4 files under this directory
    utils/  (14 files)
      … 14 files under this directory
    app.html
    index.tsx
  backend/  (10 files)
    browse/  (2 files)
      … 2 files under this directory
    genius/  (2 files)
      … 2 files under this directory
    landing/  (2 files)
      … 2 files under this directory
    appleMusicApi.js
    package.json
    serverless.yml
    utils.js
.babelrc
.env.example
.gitignore
.prettierrc
LICENSE
README.md
package.json
tsconfig.json
tslint.json
webpack.config.js
```

## Entry points

- [src/app/components/App.tsx](https://github.com/Musish/Musish/blob/9846878b0a0bb59a627d60784e092e636b933244/src/app/components/App.tsx)
- [src/app/index.tsx](https://github.com/Musish/Musish/blob/9846878b0a0bb59a627d60784e092e636b933244/src/app/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 20 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 69 file(s) under app package (observed from repository paths and static analysis). |
| backend package | library | Observed | Groups 6 file(s) under backend package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 19 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 3 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.circleci/deploy.sh` (ci)
- `.circleci/generate_structure.sh` (ci)
- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `package.json` (manifest)
- `src/app/components/Routes/Catalog/Browse/browse.json` (config)
- `src/app/utils/translations/languages/BrazilianPortuguese.json` (config)
- `src/app/utils/translations/languages/English.json` (config)
- `src/app/utils/translations/languages/French.json` (config)
- `src/app/utils/translations/languages/Greek.json` (config)
- `src/app/utils/translations/languages/Hungarian.json` (config)
- `src/app/utils/translations/languages/Italian.json` (config)
- `src/app/utils/translations/languages/Korean.json` (config)
- `src/app/utils/translations/languages/Polish.json` (config)
- `src/app/utils/translations/languages/Russian.json` (config)
- `src/app/utils/translations/languages/SChinese.json` (config)
- `src/app/utils/translations/languages/Turkish.json` (config)
- `src/backend/browse/filters.json` (config)
- `src/backend/package.json` (manifest)
- `src/backend/serverless.yml` (config)
- `tsconfig.json` (config)
- `tslint.json` (config)

## Top-level layout

- `src` — 164 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.circleci` — 3 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 17 file(s) were skipped during inventory (1 x lockfile excluded; 16 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9846878b0a0bb59a627d60784e092e636b933244` is the revision these paths and observations refer to.
