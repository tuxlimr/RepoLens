# Project structure: Bowen7/regex-vis

**Analysed commit:** `a6d920601ca44ab2d4e9cd02306510ab6d5e4b38`

**Commit reference:** [a6d920601ca44ab2d4e9cd02306510ab6d5e4b38](https://github.com/Bowen7/regex-vis/commit/a6d920601ca44ab2d4e9cd02306510ab6d5e4b38)

**Tree at this commit:** [Bowen7/regex-vis@a6d920601ca4](https://github.com/Bowen7/regex-vis/tree/a6d920601ca44ab2d4e9cd02306510ab6d5e4b38)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Bowen7/regex-vis |
| Description | 🎨 Regex visualizer & editor |
| Stars | 4451 |
| Forks | 333 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `a6d920601ca44ab2d4e9cd02306510ab6d5e4b38` |
| Retrieved at | 2026-11-14T19:14:45.175633+00:00 |
| Files in this snapshot | 171 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (1 files)
    test.yml
  CONTRIBUTING.md
  FUNDING.yml
public/  (8 files)
  locales/  (5 files)
    cn/  (1 files)
      … 1 files under this directory
    fr/  (1 files)
      … 1 files under this directory
    jp/  (1 files)
      … 1 files under this directory
    ru/  (1 files)
      … 1 files under this directory
    tr/  (1 files)
      … 1 files under this directory
  logo.svg
  manifest.json
  robots.txt
src/  (139 files)
  atom/  (21 files)
    __tests__/  (9 files)
      … 9 files under this directory
    atoms.ts
    content.ts
    flags.ts
    group.ts
    index.ts
    insert.ts
    look-around.tsx
    quantifier.ts
    remove.ts
    select.ts
    undo.ts
    utils.ts
  components/  (29 files)
    button-dropdown/  (1 files)
      … 1 files under this directory
    button-group/  (1 files)
      … 1 files under this directory
    cell/  (1 files)
      … 1 files under this directory
    header/  (1 files)
      … 1 files under this directory
    language-select/  (1 files)
      … 1 files under this directory
    legend-item/  (1 files)
      … 1 files under this directory
    logo/  (1 files)
      … 1 files under this directory
    mode-toggle/  (1 files)
      … 1 files under this directory
    range-input/  (1 files)
      … 1 files under this directory
    show-more/  (1 files)
      … 1 files under this directory
    test-item/  (1 files)
      … 1 files under this directory
    theme-provider/  (1 files)
      … 1 files under this directory
    ui/  (16 files)
      … 16 files under this directory
    validation/  (1 files)
      … 1 files under this directory
  constants/  (1 files)
    index.ts
  modules/  (39 files)
    editor/  (18 files)
      … 18 files under this directory
    graph/  (17 files)
      … 17 files under this directory
    home/  (2 files)
      … 2 files under this directory
    playground/  (1 files)
      … 1 files under this directory
    samples/  (1 files)
      … 1 files under this directory
  parser/  (32 files)
    __tests__/  (8 files)
      … 8 files under this directory
    modifiers/  (10 files)
      … 10 files under this directory
    ast.ts
    backslash.ts
    character-class.ts
    dict.ts
    gen-with-selected.ts
    gen.ts
    index.ts
    lexer.ts
    parse.ts
    parser.ts
    patterns.ts
    token.ts
    utils.ts
    visit.ts
  utils/  (9 files)
    helpers/  (1 files)
      … 1 files under this directory
    hooks/  (7 files)
      … 7 files under this directory
    links/  (1 files)
      … 1 files under this directory
  App.tsx
  global.css
  i18n.ts
  index.tsx
  logo.svg
  routes.tsx
  utils.ts
  vite-envd.ts
tests/  (6 files)
  __mocks__/  (4 files)
    analytics.js
    css.js
    react-i18next.js
    svgrMock.js
  index.test.tsx
  setup.ts
.gitignore
.prettierrc
Dockerfile
LICENSE
README.md
components.json
docker-compose.yml
eslint.config.mjs
index.html
package.json
postcss.config.js
tailwind.config.ts
tsconfig.json
vercel.json
vite.config.ts
```

## Entry points

- [src/App.tsx](https://github.com/Bowen7/regex-vis/blob/a6d920601ca44ab2d4e9cd02306510ab6d5e4b38/src/App.tsx)
- [src/atom/index.ts](https://github.com/Bowen7/regex-vis/blob/a6d920601ca44ab2d4e9cd02306510ab6d5e4b38/src/atom/index.ts)
- [src/components/button-dropdown/index.tsx](https://github.com/Bowen7/regex-vis/blob/a6d920601ca44ab2d4e9cd02306510ab6d5e4b38/src/components/button-dropdown/index.tsx)
- [src/components/button-group/index.tsx](https://github.com/Bowen7/regex-vis/blob/a6d920601ca44ab2d4e9cd02306510ab6d5e4b38/src/components/button-group/index.tsx)
- [src/components/cell/index.tsx](https://github.com/Bowen7/regex-vis/blob/a6d920601ca44ab2d4e9cd02306510ab6d5e4b38/src/components/cell/index.tsx)
- [src/components/header/index.tsx](https://github.com/Bowen7/regex-vis/blob/a6d920601ca44ab2d4e9cd02306510ab6d5e4b38/src/components/header/index.tsx)
- [src/components/language-select/index.tsx](https://github.com/Bowen7/regex-vis/blob/a6d920601ca44ab2d4e9cd02306510ab6d5e4b38/src/components/language-select/index.tsx)
- [src/components/legend-item/index.tsx](https://github.com/Bowen7/regex-vis/blob/a6d920601ca44ab2d4e9cd02306510ab6d5e4b38/src/components/legend-item/index.tsx)
- [src/components/logo/index.tsx](https://github.com/Bowen7/regex-vis/blob/a6d920601ca44ab2d4e9cd02306510ab6d5e4b38/src/components/logo/index.tsx)
- [src/components/mode-toggle/index.tsx](https://github.com/Bowen7/regex-vis/blob/a6d920601ca44ab2d4e9cd02306510ab6d5e4b38/src/components/mode-toggle/index.tsx)
- [src/components/range-input/index.tsx](https://github.com/Bowen7/regex-vis/blob/a6d920601ca44ab2d4e9cd02306510ab6d5e4b38/src/components/range-input/index.tsx)
- [src/components/show-more/index.tsx](https://github.com/Bowen7/regex-vis/blob/a6d920601ca44ab2d4e9cd02306510ab6d5e4b38/src/components/show-more/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| App.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| atom package | library | Observed | Groups 21 file(s) under atom package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 29 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants package | library | Observed | Groups 1 file(s) under constants package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| i18n.ts package | library | Observed | Groups 1 file(s) under i18n.ts package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| modules package | library | Observed | Groups 39 file(s) under modules package (observed from repository paths and static analysis). |
| parser package | library | Observed | Groups 32 file(s) under parser package (observed from repository paths and static analysis). |
| routes.tsx package | library | Observed | Groups 1 file(s) under routes.tsx package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 9 file(s) under utils package (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |
| vite-envd.ts package | library | Observed | Groups 1 file(s) under vite-envd.ts package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/test.yml` (ci)
- `Dockerfile` (container)
- `components.json` (config)
- `docker-compose.yml` (container)
- `package.json` (manifest)
- `public/locales/cn/translation.json` (config)
- `public/locales/fr/translation.json` (config)
- `public/locales/jp/translation.json` (config)
- `public/locales/ru/translation.json` (config)
- `public/locales/tr/translation.json` (config)
- `public/manifest.json` (config)
- `tsconfig.json` (config)
- `vercel.json` (config)

## Top-level layout

- `src` — 139 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `public` — 8 analysed file(s)
- `tests` — 6 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a6d920601ca44ab2d4e9cd02306510ab6d5e4b38` is the revision these paths and observations refer to.
