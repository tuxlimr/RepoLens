# Project structure: epicweb-dev/advanced-react-patterns

**Analysed commit:** `97a160158526e54f5829854b59b7281bfc777b91`

**Commit reference:** [97a160158526e54f5829854b59b7281bfc777b91](https://github.com/epicweb-dev/advanced-react-patterns/commit/97a160158526e54f5829854b59b7281bfc777b91)

**Tree at this commit:** [epicweb-dev/advanced-react-patterns@97a160158526](https://github.com/epicweb-dev/advanced-react-patterns/tree/97a160158526e54f5829854b59b7281bfc777b91)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | epicweb-dev/advanced-react-patterns |
| Description | This is the latest advanced react patterns workshop |
| Stars | 3517 |
| Forks | 1060 |
| Licence | Other |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `97a160158526e54f5829854b59b7281bfc777b91` |
| Retrieved at | 2026-11-14T19:15:16.460209+00:00 |
| Files in this snapshot | 216 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    validate.yml
.vscode/  (2 files)
  extensions.json
  settings.kcd.json
epicshop/  (12 files)
  .diffignore
  Dockerfile
  fix-watch.js
  fix.js
  fly.yaml
  in-browser-tests.spec.js
  package.json
  playwright.config.js
  post-set-playground.js
  setup-custom.js
  tsconfig.json
  update-deps.sh
exercises/  (183 files)
  01.composition/  (9 files)
    01.problem.compose/  (3 files)
      … 3 files under this directory
    01.solution.compose/  (4 files)
      … 4 files under this directory
    FINISHED.mdx
    README.mdx
  02.latest-ref/  (8 files)
    01.problem.ref/  (2 files)
      … 2 files under this directory
    01.solution.ref/  (4 files)
      … 4 files under this directory
    FINISHED.mdx
    README.mdx
  03.compound-components/  (25 files)
    01.problem.context/  (5 files)
      … 5 files under this directory
    01.solution.context/  (6 files)
      … 6 files under this directory
    02.problem.validation/  (5 files)
      … 5 files under this directory
    02.solution.validation/  (7 files)
      … 7 files under this directory
    FINISHED.mdx
    README.mdx
  04.slots/  (47 files)
    01.problem.context/  (7 files)
      … 7 files under this directory
    01.solution.context/  (8 files)
      … 8 files under this directory
    02.problem.generic/  (7 files)
      … 7 files under this directory
    02.solution.generic/  (8 files)
      … 8 files under this directory
    03.problem.prop/  (7 files)
      … 7 files under this directory
    03.solution.prop/  (8 files)
      … 8 files under this directory
    FINISHED.mdx
    README.mdx
  05.prop-getters/  (27 files)
    01.problem.collections/  (5 files)
      … 5 files under this directory
    01.solution.collections/  (7 files)
      … 7 files under this directory
    02.problem.getters/  (5 files)
      … 5 files under this directory
    02.solution.getters/  (8 files)
      … 8 files under this directory
    FINISHED.mdx
    README.mdx
  06.state-initializers/  (24 files)
    01.problem.initial/  (5 files)
      … 5 files under this directory
    01.solution.initial/  (6 files)
      … 6 files under this directory
    02.problem.stability/  (5 files)
      … 5 files under this directory
    02.solution.stability/  (6 files)
      … 6 files under this directory
    FINISHED.mdx
    README.mdx
  07.state-reducer/  (27 files)
    01.problem.reducer/  (5 files)
      … 5 files under this directory
    01.solution.reducer/  (7 files)
      … 7 files under this directory
    02.problem.default/  (5 files)
      … 5 files under this directory
    02.solution.default/  (8 files)
      … 8 files under this directory
    FINISHED.mdx
    README.mdx
  08.control-props/  (14 files)
    01.problem.control/  (5 files)
      … 5 files under this directory
    01.solution.control/  (7 files)
      … 7 files under this directory
    FINISHED.mdx
    README.mdx
  FINISHED.mdx
  README.mdx
public/  (5 files)
  og/  (1 files)
    logo.svg
  favicon.svg
  logo.svg
  manifest.json
  switch.styles.css
shared/  (5 files)
  sports.tsx
  switch.tsx
  toggle.test.tsx
  types.d.ts
  utils.tsx
.gitattributes
.gitignore
LICENSE.md
README.md
eslint.config.js
package.json
reset.d.ts
tsconfig.json
```

## Entry points

- [exercises/01.composition/01.problem.compose/index.tsx](https://github.com/epicweb-dev/advanced-react-patterns/blob/97a160158526e54f5829854b59b7281bfc777b91/exercises/01.composition/01.problem.compose/index.tsx)
- [exercises/01.composition/01.solution.compose/index.tsx](https://github.com/epicweb-dev/advanced-react-patterns/blob/97a160158526e54f5829854b59b7281bfc777b91/exercises/01.composition/01.solution.compose/index.tsx)
- [exercises/02.latest-ref/01.problem.ref/index.tsx](https://github.com/epicweb-dev/advanced-react-patterns/blob/97a160158526e54f5829854b59b7281bfc777b91/exercises/02.latest-ref/01.problem.ref/index.tsx)
- [exercises/02.latest-ref/01.solution.ref/index.tsx](https://github.com/epicweb-dev/advanced-react-patterns/blob/97a160158526e54f5829854b59b7281bfc777b91/exercises/02.latest-ref/01.solution.ref/index.tsx)
- [exercises/03.compound-components/01.problem.context/app.tsx](https://github.com/epicweb-dev/advanced-react-patterns/blob/97a160158526e54f5829854b59b7281bfc777b91/exercises/03.compound-components/01.problem.context/app.tsx)
- [exercises/03.compound-components/01.problem.context/index.tsx](https://github.com/epicweb-dev/advanced-react-patterns/blob/97a160158526e54f5829854b59b7281bfc777b91/exercises/03.compound-components/01.problem.context/index.tsx)
- [exercises/03.compound-components/01.solution.context/app.tsx](https://github.com/epicweb-dev/advanced-react-patterns/blob/97a160158526e54f5829854b59b7281bfc777b91/exercises/03.compound-components/01.solution.context/app.tsx)
- [exercises/03.compound-components/01.solution.context/index.tsx](https://github.com/epicweb-dev/advanced-react-patterns/blob/97a160158526e54f5829854b59b7281bfc777b91/exercises/03.compound-components/01.solution.context/index.tsx)
- [exercises/03.compound-components/02.problem.validation/app.tsx](https://github.com/epicweb-dev/advanced-react-patterns/blob/97a160158526e54f5829854b59b7281bfc777b91/exercises/03.compound-components/02.problem.validation/app.tsx)
- [exercises/03.compound-components/02.problem.validation/index.tsx](https://github.com/epicweb-dev/advanced-react-patterns/blob/97a160158526e54f5829854b59b7281bfc777b91/exercises/03.compound-components/02.problem.validation/index.tsx)
- [exercises/03.compound-components/02.solution.validation/app.tsx](https://github.com/epicweb-dev/advanced-react-patterns/blob/97a160158526e54f5829854b59b7281bfc777b91/exercises/03.compound-components/02.solution.validation/app.tsx)
- [exercises/03.compound-components/02.solution.validation/index.tsx](https://github.com/epicweb-dev/advanced-react-patterns/blob/97a160158526e54f5829854b59b7281bfc777b91/exercises/03.compound-components/02.solution.validation/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| epicshop package | library | Observed | Groups 7 file(s) under epicshop package (observed from repository paths and static analysis). |
| exercises package | library | Observed | Groups 111 file(s) under exercises package (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 5 file(s) under shared package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/validate.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.kcd.json` (config)
- `epicshop/Dockerfile` (container)
- `epicshop/fly.yaml` (config)
- `epicshop/package.json` (manifest)
- `epicshop/tsconfig.json` (config)
- `package.json` (manifest)
- `public/manifest.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `exercises` — 183 analysed file(s)
- `epicshop` — 12 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `public` — 5 analysed file(s)
- `shared` — 5 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `97a160158526e54f5829854b59b7281bfc777b91` is the revision these paths and observations refer to.
