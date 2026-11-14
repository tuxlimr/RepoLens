# Project structure: epicweb-dev/react-fundamentals

**Analysed commit:** `bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1`

**Commit reference:** [bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1](https://github.com/epicweb-dev/react-fundamentals/commit/bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1)

**Tree at this commit:** [epicweb-dev/react-fundamentals@bef2dbf208bf](https://github.com/epicweb-dev/react-fundamentals/tree/bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | epicweb-dev/react-fundamentals |
| Description | Material for my React Fundamentals Workshop |
| Stars | 5310 |
| Forks | 3097 |
| Licence | Other |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1` |
| Retrieved at | 2026-11-14T19:14:22.419835+00:00 |
| Files in this snapshot | 274 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    validate.yml
.vscode/  (1 files)
  extensions.json
epicshop/  (9 files)
  .diffignore
  Dockerfile
  fly.yaml
  in-browser-tests.spec.js
  package.json
  playwright.config.js
  post-set-playground.js
  setup-custom.js
  update-deps.sh
exercises/  (250 files)
  01.js-hello-world/  (12 files)
    01.problem.hello/  (2 files)
      … 2 files under this directory
    01.solution.hello/  (3 files)
      … 3 files under this directory
    02.problem.root/  (2 files)
      … 2 files under this directory
    02.solution.root/  (3 files)
      … 3 files under this directory
    FINISHED.mdx
    README.mdx
  02.raw-react/  (17 files)
    01.problem.elements/  (2 files)
      … 2 files under this directory
    01.solution.elements/  (3 files)
      … 3 files under this directory
    02.problem.nesting/  (2 files)
      … 2 files under this directory
    02.solution.nesting/  (3 files)
      … 3 files under this directory
    03.problem.deep-nesting/  (2 files)
      … 2 files under this directory
    03.solution.deep-nesting/  (3 files)
      … 3 files under this directory
    FINISHED.mdx
    README.mdx
  03.using-jsx/  (31 files)
    01.problem.compiler/  (2 files)
      … 2 files under this directory
    01.solution.compiler/  (4 files)
      … 4 files under this directory
    02.problem.interpolation/  (2 files)
      … 2 files under this directory
    02.solution.interpolation/  (4 files)
      … 4 files under this directory
    03.problem.spread/  (2 files)
      … 2 files under this directory
    03.solution.spread/  (4 files)
      … 4 files under this directory
    04.problem.nesting/  (2 files)
      … 2 files under this directory
    04.solution.nesting/  (3 files)
      … 3 files under this directory
    05.problem.fragments/  (2 files)
      … 2 files under this directory
    05.solution.fragments/  (4 files)
      … 4 files under this directory
    FINISHED.mdx
    README.mdx
  04.components/  (25 files)
    01.problem.function/  (2 files)
      … 2 files under this directory
    01.solution.function/  (4 files)
      … 4 files under this directory
    02.problem.raw/  (2 files)
      … 2 files under this directory
    02.solution.raw/  (4 files)
      … 4 files under this directory
    03.problem.jsx/  (2 files)
      … 2 files under this directory
    03.solution.jsx/  (4 files)
      … 4 files under this directory
    04.problem.props/  (2 files)
      … 2 files under this directory
    04.solution.props/  (3 files)
      … 3 files under this directory
    FINISHED.mdx
    README.mdx
  05.typescript/  (32 files)
    01.problem.props/  (2 files)
      … 2 files under this directory
    01.solution.props/  (3 files)
      … 3 files under this directory
    02.problem.narrow/  (2 files)
      … 2 files under this directory
    02.solution.narrow/  (3 files)
      … 3 files under this directory
    03.problem.derive/  (2 files)
      … 2 files under this directory
    03.solution.derive/  (3 files)
      … 3 files under this directory
    04.problem.default-props/  (2 files)
      … 2 files under this directory
    04.solution.default-props/  (3 files)
      … 3 files under this directory
    05.problem.function-types/  (2 files)
      … 2 files under this directory
    05.solution.function-types/  (3 files)
      … 3 files under this directory
    06.problem.satisfies/  (2 files)
      … 2 files under this directory
    06.solution.satisfies/  (3 files)
      … 3 files under this directory
    FINISHED.mdx
    README.mdx
  06.styling/  (25 files)
    01.problem.style/  (3 files)
      … 3 files under this directory
    01.solution.style/  (4 files)
      … 4 files under this directory
    02.problem.component/  (3 files)
      … 3 files under this directory
    02.solution.component/  (5 files)
      … 5 files under this directory
    03.problem.size-prop/  (3 files)
      … 3 files under this directory
    03.solution.size-prop/  (5 files)
      … 5 files under this directory
    FINISHED.mdx
    README.mdx
  07.forms/  (40 files)
    01.problem.form/  (2 files)
      … 2 files under this directory
    01.solution.form/  (3 files)
      … 3 files under this directory
    02.problem.action/  (3 files)
      … 3 files under this directory
    02.solution.action/  (5 files)
      … 5 files under this directory
    03.problem.types/  (3 files)
      … 3 files under this directory
    03.solution.types/  (5 files)
      … 5 files under this directory
    04.problem.submit/  (3 files)
      … 3 files under this directory
    04.solution.submit/  (7 files)
      … 7 files under this directory
    05.problem.action/  (3 files)
      … 3 files under this directory
    05.solution.action/  (4 files)
      … 4 files under this directory
    FINISHED.mdx
    README.mdx
  08.inputs/  (32 files)
    01.problem.checkbox/  (2 files)
      … 2 files under this directory
    01.solution.checkbox/  (4 files)
      … 4 files under this directory
    02.problem.select/  (2 files)
      … 2 files under this directory
    02.solution.select/  (4 files)
      … 4 files under this directory
    03.problem.radio/  (2 files)
      … 2 files under this directory
    03.solution.radio/  (4 files)
      … 4 files under this directory
    04.problem.hidden/  (2 files)
      … 2 files under this directory
    04.solution.hidden/  (4 files)
      … 4 files under this directory
    05.problem.default-value/  (2 files)
      … 2 files under this directory
    05.solution.default-value/  (4 files)
      … 4 files under this directory
    FINISHED.mdx
    README.mdx
  09.errors/  (17 files)
    01.problem.composition/  (2 files)
      … 2 files under this directory
    01.solution.composition/  (3 files)
      … 3 files under this directory
    02.problem.show-boundary/  (2 files)
      … 2 files under this directory
    02.solution.show-boundary/  (3 files)
      … 3 files under this directory
    03.problem.reset/  (2 files)
      … 2 files under this directory
    03.solution.reset/  (3 files)
      … 3 files under this directory
    FINISHED.mdx
    README.mdx
  10.arrays/  (17 files)
    01.problem.key-prop/  (2 files)
      … 2 files under this directory
    01.solution.key-prop/  (3 files)
      … 3 files under this directory
    02.problem.focus-state/  (2 files)
      … 2 files under this directory
    02.solution.focus-state/  (3 files)
      … 3 files under this directory
    03.problem.key-reset/  (2 files)
      … 2 files under this directory
    03.solution.key-reset/  (3 files)
      … 3 files under this directory
    FINISHED.mdx
    README.mdx
  FINISHED.mdx
  README.mdx
public/  (5 files)
  og/  (1 files)
    logo.svg
  react-dom/  (1 files)
    client.js
  favicon.svg
  logo.svg
  react.js
shared/  (1 files)
  api-utils.ts
.gitignore
.prettierignore
LICENSE.md
README.md
eslint.config.js
package.json
tsconfig.json
```

## Entry points

- [exercises/05.typescript/01.problem.props/index.tsx](https://github.com/epicweb-dev/react-fundamentals/blob/bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1/exercises/05.typescript/01.problem.props/index.tsx)
- [exercises/05.typescript/01.solution.props/index.tsx](https://github.com/epicweb-dev/react-fundamentals/blob/bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1/exercises/05.typescript/01.solution.props/index.tsx)
- [exercises/05.typescript/02.problem.narrow/index.tsx](https://github.com/epicweb-dev/react-fundamentals/blob/bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1/exercises/05.typescript/02.problem.narrow/index.tsx)
- [exercises/05.typescript/02.solution.narrow/index.tsx](https://github.com/epicweb-dev/react-fundamentals/blob/bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1/exercises/05.typescript/02.solution.narrow/index.tsx)
- [exercises/05.typescript/03.problem.derive/index.tsx](https://github.com/epicweb-dev/react-fundamentals/blob/bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1/exercises/05.typescript/03.problem.derive/index.tsx)
- [exercises/05.typescript/03.solution.derive/index.tsx](https://github.com/epicweb-dev/react-fundamentals/blob/bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1/exercises/05.typescript/03.solution.derive/index.tsx)
- [exercises/05.typescript/04.problem.default-props/index.tsx](https://github.com/epicweb-dev/react-fundamentals/blob/bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1/exercises/05.typescript/04.problem.default-props/index.tsx)
- [exercises/05.typescript/04.solution.default-props/index.tsx](https://github.com/epicweb-dev/react-fundamentals/blob/bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1/exercises/05.typescript/04.solution.default-props/index.tsx)
- [exercises/05.typescript/05.problem.function-types/index.tsx](https://github.com/epicweb-dev/react-fundamentals/blob/bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1/exercises/05.typescript/05.problem.function-types/index.tsx)
- [exercises/05.typescript/05.solution.function-types/index.tsx](https://github.com/epicweb-dev/react-fundamentals/blob/bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1/exercises/05.typescript/05.solution.function-types/index.tsx)
- [exercises/05.typescript/06.problem.satisfies/index.tsx](https://github.com/epicweb-dev/react-fundamentals/blob/bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1/exercises/05.typescript/06.problem.satisfies/index.tsx)
- [exercises/05.typescript/06.solution.satisfies/index.tsx](https://github.com/epicweb-dev/react-fundamentals/blob/bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1/exercises/05.typescript/06.solution.satisfies/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| epicshop package | library | Observed | Groups 5 file(s) under epicshop package (observed from repository paths and static analysis). |
| exercises package | library | Observed | Groups 116 file(s) under exercises package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 2 file(s) under public package (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 1 file(s) under shared package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/validate.yml` (ci)
- `.vscode/extensions.json` (config)
- `epicshop/Dockerfile` (container)
- `epicshop/fly.yaml` (config)
- `epicshop/package.json` (manifest)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `exercises` — 250 analysed file(s)
- `epicshop` — 9 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `public` — 5 analysed file(s)
- `.github` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `shared` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `bef2dbf208bf057d40e8080855e1bbbd8fb9d4b1` is the revision these paths and observations refer to.
