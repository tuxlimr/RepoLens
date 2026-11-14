# Project structure: ritz078/transform

**Analysed commit:** `ff7557939be351706f4dc6f71cc375e3bc64c225`

**Commit reference:** [ff7557939be351706f4dc6f71cc375e3bc64c225](https://github.com/ritz078/transform/commit/ff7557939be351706f4dc6f71cc375e3bc64c225)

**Tree at this commit:** [ritz078/transform@ff7557939be3](https://github.com/ritz078/transform/tree/ff7557939be351706f4dc6f71cc375e3bc64c225)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ritz078/transform |
| Description | A polyglot web converter. |
| Stars | 9259 |
| Forks | 705 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `ff7557939be351706f4dc6f71cc375e3bc64c225` |
| Retrieved at | 2026-11-14T19:13:35.233804+00:00 |
| Files in this snapshot | 129 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
assets/  (3 files)
  svgs/  (3 files)
    Error404.tsx
    Error500.tsx
    Npm.tsx
components/  (9 files)
  ConversionPanel.tsx
  EditorPanel.tsx
  Form.tsx
  Meta.tsx
  Monaco.tsx
  Navigator.tsx
  NoSSR.tsx
  Searchbox.tsx
  SvgConverter.tsx
constants/  (4 files)
  babelTransforms.ts
  data.ts
  graphqlTransforms.ts
  svgoConfig.ts
hooks/  (5 files)
  useDarkMode.ts
  useData.ts
  useLocalStorage.ts
  useSessionStorage.ts
  useSettings.ts
pages/  (75 files)
  api/  (8 files)
    flow-to-javascript.ts
    flow-to-typescript.ts
    html-to-pug.ts
    json-schema-to-openapi-schema.ts
    typescript-to-flow.ts
    typescript-to-javascript.ts
    typescript-to-json-schema.ts
    typescript-to-zod.ts
  _app.tsx
  _document.tsx
  _error.tsx
  cadence-to-go.tsx
  css-to-js.tsx
  css-to-tailwind.tsx
  flow-to-javascript.tsx
  flow-to-typescript-declaration.tsx
  flow-to-typescript.tsx
  graphql-to-components.tsx
  graphql-to-flow.tsx
  graphql-to-fragment-matcher.tsx
  graphql-to-introspection-json.tsx
  graphql-to-java.tsx
  graphql-to-resolvers-signature.tsx
  graphql-to-schema-ast.tsx
  graphql-to-typescript-mongodb.tsx
  graphql-to-typescript.tsx
  html-to-jsx.tsx
  html-to-pug.tsx
  index.tsx
  js-object-to-json.tsx
  js-object-to-typescript.tsx
  json-schema-to-openapi-schema.tsx
  … 43 more files
patches/  (5 files)
  @khanacademy+flow-to-ts+0.5.2.patch
  htmltojsx+0.3.0.patch
  json-schema-to-typescript+10.1.4.patch
  json_typegen_wasm+0.7.0.patch
  relay-compiler+10.1.0.patch
public/  (1 files)
  static/  (1 files)
    site.webmanifest
styles/  (1 files)
  main.css
typings/  (2 files)
  npm/  (2 files)
    Readme.md
    evergreen-ui.d.ts
utils/  (5 files)
  prettier.ts
  prettify.ts
  request.ts
  routes.tsx
  workerWrapper.ts
workers/  (6 files)
  babel.worker.ts
  graphql.worker.ts
  postcss.worker.ts
  prettier.worker.ts
  svgo.worker.ts
  svgr.worker.ts
.all-contributorsrc
.gitignore
.prettierignore
.prettierrc
LICENSE
README.md
next-env.d.ts
next.config.js
package.json
tsconfig.json
typings.d.ts
vercel.json
```

## Entry points

- [pages/index.tsx](https://github.com/ritz078/transform/blob/ff7557939be351706f4dc6f71cc375e3bc64c225/pages/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 8 file(s) under api layer (observed from repository paths and static analysis). |
| assets package | library | Observed | Groups 3 file(s) under assets package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 9 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants package | library | Observed | Groups 4 file(s) under constants package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 5 file(s) under hooks package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 67 file(s) under pages package (observed from repository paths and static analysis). |
| typings package | library | Observed | Groups 1 file(s) under typings package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 5 file(s) under utils package (observed from repository paths and static analysis). |
| workers package | library | Observed | Groups 6 file(s) under workers package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `vercel.json` (config)

## Top-level layout

- `pages` — 75 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `components` — 9 analysed file(s)
- `workers` — 6 analysed file(s)
- `hooks` — 5 analysed file(s)
- `patches` — 5 analysed file(s)
- `utils` — 5 analysed file(s)
- `constants` — 4 analysed file(s)
- `assets` — 3 analysed file(s)
- `typings` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `public` — 1 analysed file(s)
- `styles` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ff7557939be351706f4dc6f71cc375e3bc64c225` is the revision these paths and observations refer to.
