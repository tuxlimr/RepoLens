# Project structure: thebuilder/react-intersection-observer

**Analysed commit:** `591e167abb2300f2017c810f83ee0511f7fbbd50`

**Commit reference:** [591e167abb2300f2017c810f83ee0511f7fbbd50](https://github.com/thebuilder/react-intersection-observer/commit/591e167abb2300f2017c810f83ee0511f7fbbd50)

**Tree at this commit:** [thebuilder/react-intersection-observer@591e167abb23](https://github.com/thebuilder/react-intersection-observer/tree/591e167abb2300f2017c810f83ee0511f7fbbd50)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | thebuilder/react-intersection-observer |
| Description | React implementation of the Intersection Observer API to tell you when an element enters or leaves the viewport. |
| Stars | 5543 |
| Forks | 188 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `591e167abb2300f2017c810f83ee0511f7fbbd50` |
| Retrieved at | 2026-11-14T19:14:18.150162+00:00 |
| Files in this snapshot | 87 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (3 files)
    pkg-pr.yml
    release.yml
    test.yml
apps/  (48 files)
  docs/  (32 files)
    components/  (2 files)
      … 2 files under this directory
    docs/  (12 files)
      … 12 files under this directory
    islands/  (2 files)
      … 2 files under this directory
    pages/  (4 files)
      … 4 files under this directory
    public/  (4 files)
      … 4 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    sources/  (1 files)
      … 1 files under this directory
    .gitignore
    blume.config.ts
    components.ts
    evals.yaml
    package.json
    theme.css
  storybook/  (16 files)
    .storybook/  (5 files)
      … 5 files under this directory
    stories/  (6 files)
      … 6 files under this directory
    package.json
    postcss.config.js
    styles.css
    tailwind.config.js
    tsconfig.json
packages/  (22 files)
  react-intersection-observer/  (22 files)
    compat/  (1 files)
      … 1 files under this directory
    fixtures/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    src/  (14 files)
      … 14 files under this directory
    package.json
    tsconfig.json
    tsup.config.ts
    vitest.config.ts
.fallowrc.json
.gitattributes
.gitignore
.npmignore
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
biome.json
package.json
pnpm-workspace.yaml
turbo.json
```

## Entry points

- [apps/storybook/.storybook/main.ts](https://github.com/thebuilder/react-intersection-observer/blob/591e167abb2300f2017c810f83ee0511f7fbbd50/apps/storybook/.storybook/main.ts)
- [packages/react-intersection-observer/src/index.tsx](https://github.com/thebuilder/react-intersection-observer/blob/591e167abb2300f2017c810f83ee0511f7fbbd50/packages/react-intersection-observer/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apps package | library | Observed | Groups 11 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 10 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 19 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.fallowrc.json` (config)
- `.github/workflows/pkg-pr.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `apps/docs/evals.yaml` (config)
- `apps/docs/package.json` (manifest)
- `apps/storybook/package.json` (manifest)
- `apps/storybook/tsconfig.json` (config)
- `biome.json` (config)
- `package.json` (manifest)
- `packages/react-intersection-observer/package.json` (manifest)
- `packages/react-intersection-observer/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `turbo.json` (config)

## Top-level layout

- `apps` — 48 analysed file(s)
- `packages` — 22 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `591e167abb2300f2017c810f83ee0511f7fbbd50` is the revision these paths and observations refer to.
