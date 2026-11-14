# Project structure: wojtekmaj/react-lifecycle-methods-diagram

**Analysed commit:** `e2ce0072a6c77e56c77b85be08debd1d560c157a`

**Commit reference:** [e2ce0072a6c77e56c77b85be08debd1d560c157a](https://github.com/wojtekmaj/react-lifecycle-methods-diagram/commit/e2ce0072a6c77e56c77b85be08debd1d560c157a)

**Tree at this commit:** [wojtekmaj/react-lifecycle-methods-diagram@e2ce0072a6c7](https://github.com/wojtekmaj/react-lifecycle-methods-diagram/tree/e2ce0072a6c77e56c77b85be08debd1d560c157a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | wojtekmaj/react-lifecycle-methods-diagram |
| Description | Interactive React Lifecycle Methods diagram. |
| Stars | 3930 |
| Forks | 327 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `e2ce0072a6c77e56c77b85be08debd1d560c157a` |
| Retrieved at | 2026-11-14T19:14:58.247670+00:00 |
| Files in this snapshot | 91 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    ci.yml
    deploy.yml
  FUNDING.yml
.husky/  (1 files)
  pre-commit
.vscode/  (2 files)
  extensions.json
  settings.json
.yarn/  (1 files)
  plugins/  (1 files)
    @yarnpkg/  (1 files)
      … 1 files under this directory
public/  (1 files)
  .htaccess
src/  (71 files)
  diagramElements/  (10 files)
    Arrow.module.css
    Arrow.tsx
    DocLink.tsx
    Initiator.module.css
    Initiator.tsx
    Method.module.css
    Method.tsx
    Section.module.css
    Section.tsx
    Subsection.tsx
  i18n/  (34 files)
    json/  (31 files)
      … 31 files under this directory
    README.md
    i18n.ts
    languages.json
  legendElements/  (2 files)
    Phase.module.css
    Phase.tsx
  shared/  (1 files)
    utils.ts
  versions/  (9 files)
    16.3/  (4 files)
      … 4 files under this directory
    16.4/  (4 files)
      … 4 files under this directory
    README.md
  Diagram.tsx
  DiagramWithLegend.module.css
  DiagramWithLegend.tsx
  Footer.module.css
  Footer.tsx
  GitHub.tsx
  Legend.module.css
  Legend.tsx
  Options.module.css
  Options.tsx
  Root.tsx
  global.css
  index.tsx
  reactVersions.ts
  types.ts
.browserslistrc
.gitattributes
.gitignore
.yarnrc.yml
LICENSE
README.md
biome.json
global.d.ts
index.html
package.json
tsconfig.json
vite.config.ts
```

## Entry points

- [src/index.tsx](https://github.com/wojtekmaj/react-lifecycle-methods-diagram/blob/e2ce0072a6c77e56c77b85be08debd1d560c157a/src/index.tsx)
- [src/versions/16.3/index.ts](https://github.com/wojtekmaj/react-lifecycle-methods-diagram/blob/e2ce0072a6c77e56c77b85be08debd1d560c157a/src/versions/16.3/index.ts)
- [src/versions/16.4/index.ts](https://github.com/wojtekmaj/react-lifecycle-methods-diagram/blob/e2ce0072a6c77e56c77b85be08debd1d560c157a/src/versions/16.4/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 35 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Diagram.tsx package | library | Observed | Groups 1 file(s) under diagram.tsx package (observed from repository paths and static analysis). |
| diagramElements package | library | Observed | Groups 6 file(s) under diagramelements package (observed from repository paths and static analysis). |
| DiagramWithLegend.tsx package | library | Observed | Groups 1 file(s) under diagramwithlegend.tsx package (observed from repository paths and static analysis). |
| Footer.tsx package | library | Observed | Groups 1 file(s) under footer.tsx package (observed from repository paths and static analysis). |
| GitHub.tsx package | library | Observed | Groups 1 file(s) under github.tsx package (observed from repository paths and static analysis). |
| i18n package | library | Observed | Groups 1 file(s) under i18n package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| Legend.tsx package | library | Observed | Groups 1 file(s) under legend.tsx package (observed from repository paths and static analysis). |
| legendElements package | library | Observed | Groups 1 file(s) under legendelements package (observed from repository paths and static analysis). |
| Options.tsx package | library | Observed | Groups 1 file(s) under options.tsx package (observed from repository paths and static analysis). |
| reactVersions.ts package | library | Observed | Groups 1 file(s) under reactversions.ts package (observed from repository paths and static analysis). |
| Root.tsx package | library | Observed | Groups 1 file(s) under root.tsx package (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 1 file(s) under shared package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| versions package | library | Observed | Groups 8 file(s) under versions package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deploy.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `.yarnrc.yml` (config)
- `biome.json` (config)
- `package.json` (manifest)
- `src/i18n/json/ar-AE.json` (config)
- `src/i18n/json/az-AZ.json` (config)
- `src/i18n/json/be-BY.json` (config)
- `src/i18n/json/bn-BD.json` (config)
- `src/i18n/json/de-DE.json` (config)
- `src/i18n/json/es-ES.json` (config)
- `src/i18n/json/fa-IR.json` (config)
- `src/i18n/json/fr-FR.json` (config)
- `src/i18n/json/hi-IN.json` (config)
- `src/i18n/json/hu-HU.json` (config)
- `src/i18n/json/hy-AM.json` (config)
- `src/i18n/json/id-ID.json` (config)
- `src/i18n/json/it-IT.json` (config)
- `src/i18n/json/ja-JP.json` (config)
- `src/i18n/json/kk-KZ.json` (config)
- `src/i18n/json/ko-KR.json` (config)
- `src/i18n/json/pl-PL.json` (config)
- `src/i18n/json/pt-BR.json` (config)
- `src/i18n/json/pt-PT.json` (config)
- `src/i18n/json/ro-RO.json` (config)
- `src/i18n/json/ru-RU.json` (config)
- `src/i18n/json/sq-AL.json` (config)
- `src/i18n/json/sv-SE.json` (config)
- `src/i18n/json/th-TH.json` (config)
- `src/i18n/json/tr-TR.json` (config)
- `src/i18n/json/uk-UA.json` (config)
- `src/i18n/json/ur.json` (config)
- `src/i18n/json/uz.json` (config)
- `src/i18n/json/vi-VN.json` (config)
- `src/i18n/json/zh-Hans.json` (config)
- `src/i18n/json/zh-Hant.json` (config)
- `src/i18n/languages.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 71 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `.yarn` — 1 analysed file(s)
- `public` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e2ce0072a6c77e56c77b85be08debd1d560c157a` is the revision these paths and observations refer to.
