# Project structure: BuilderIO/figma-html

**Analysed commit:** `2b244343ba3fcc1a2de50fa652e13833e78e36f9`

**Commit reference:** [2b244343ba3fcc1a2de50fa652e13833e78e36f9](https://github.com/BuilderIO/figma-html/commit/2b244343ba3fcc1a2de50fa652e13833e78e36f9)

**Tree at this commit:** [BuilderIO/figma-html@2b244343ba3f](https://github.com/BuilderIO/figma-html/tree/2b244343ba3fcc1a2de50fa652e13833e78e36f9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | BuilderIO/figma-html |
| Description | Convert any website to editable Figma designs |
| Stars | 3715 |
| Forks | 365 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `2b244343ba3fcc1a2de50fa652e13833e78e36f9` |
| Retrieved at | 2026-11-14T19:15:07.674655+00:00 |
| Files in this snapshot | 27 |

## Directory tree

```text
.github/  (1 files)
  ISSUE_TEMPLATE/  (1 files)
    bug_report.md
chrome-extension/  (15 files)
  info/  (2 files)
    manifest.json
    popup.html
  src/  (5 files)
    constants/  (1 files)
      … 1 files under this directory
    popup/  (2 files)
      … 2 files under this directory
    background.ts
    inject.ts
  .gitignore
  README.md
  package.json
  tsconfig.json
  tslint.json
  webpack.common.js
  webpack.dev.js
  webpack.prod.js
shared/  (2 files)
  typings.d.ts
  typings.ts
.gitignore
.nvmrc
CODEOWNERS
DEVELOP.md
LICENSE.md
README.md
package.json
tsconfig.json
webpack.config.js
```

## Entry points

- [chrome-extension/src/popup/index.tsx](https://github.com/BuilderIO/figma-html/blob/2b244343ba3fcc1a2de50fa652e13833e78e36f9/chrome-extension/src/popup/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| chrome-extension package | library | Observed | Groups 8 file(s) under chrome-extension package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 2 file(s) under shared package (observed from repository paths and static analysis). |

## Important files

- `chrome-extension/info/manifest.json` (config)
- `chrome-extension/package.json` (manifest)
- `chrome-extension/tsconfig.json` (config)
- `chrome-extension/tslint.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `chrome-extension` — 15 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `shared` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2b244343ba3fcc1a2de50fa652e13833e78e36f9` is the revision these paths and observations refer to.
