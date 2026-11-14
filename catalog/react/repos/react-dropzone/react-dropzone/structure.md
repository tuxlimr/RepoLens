# Project structure: react-dropzone/react-dropzone

**Analysed commit:** `512bcf2bf28498d13e05aef70c3e9147d752612a`

**Commit reference:** [512bcf2bf28498d13e05aef70c3e9147d752612a](https://github.com/react-dropzone/react-dropzone/commit/512bcf2bf28498d13e05aef70c3e9147d752612a)

**Tree at this commit:** [react-dropzone/react-dropzone@512bcf2bf284](https://github.com/react-dropzone/react-dropzone/tree/512bcf2bf28498d13e05aef70c3e9147d752612a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | react-dropzone/react-dropzone |
| Description | Simple HTML5 drag-drop zone with React.js. |
| Stars | 11023 |
| Forks | 799 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `512bcf2bf28498d13e05aef70c3e9147d752612a` |
| Retrieved at | 2026-11-14T19:13:27.808664+00:00 |
| Files in this snapshot | 68 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (4 files)
    dependabot-auto-merge.yml
    docs-monitor.yml
    release.yml
    test.yml
  dependabot.yml
  stale.yml
docs/  (20 files)
  components/  (2 files)
    dropzone.css
    examples.tsx
  pages/  (18 files)
    examples/  (15 files)
      … 15 files under this directory
    guide/  (2 files)
      … 2 files under this directory
    index.mdx
e2e/  (1 files)
  docs-smoke.e2e.ts
public/  (3 files)
  dropzone-lockup-dark.svg
  dropzone-lockup.svg
  favicon.svg
src/  (5 files)
  __snapshots__/  (1 files)
    index.spec.tsx.snap
  utils/  (2 files)
    index.spec.ts
    index.ts
  index.spec.tsx
  index.tsx
type-tests/  (10 files)
  accept.tsx
  all.tsx
  basic.tsx
  events.tsx
  file-dialog.tsx
  file-removal.tsx
  hook.tsx
  plugin.tsx
  refs.tsx
  validator.tsx
.codeclimate.yml
.editorconfig
.gitignore
.gitpod.yml
.nvmrc
.oxfmtrc.json
.oxlintrc.json
.pre-commit-config.yaml
.releaserc.json
AGENTS.md
CLAUDE.md
LICENSE
README.md
netlify.toml
package.json
playwright.config.ts
test-setup.js
tsconfig.build.json
tsconfig.json
tsconfig.type-tests.json
tsdown.config.ts
vitest.config.ts
vocs.config.ts
```

## Entry points

- [src/index.tsx](https://github.com/react-dropzone/react-dropzone/blob/512bcf2bf28498d13e05aef70c3e9147d752612a/src/index.tsx)
- [src/utils/index.ts](https://github.com/react-dropzone/react-dropzone/blob/512bcf2bf28498d13e05aef70c3e9147d752612a/src/utils/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 1 file(s) under e2e package (observed from repository paths and static analysis). |
| index.spec.tsx package | library | Observed | Groups 1 file(s) under index.spec.tsx package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| type-tests package | library | Observed | Groups 10 file(s) under type-tests package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 2 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.codeclimate.yml` (config)
- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/dependabot-auto-merge.yml` (ci)
- `.github/workflows/docs-monitor.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.gitpod.yml` (config)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `.pre-commit-config.yaml` (config)
- `.releaserc.json` (config)
- `netlify.toml` (config)
- `package.json` (manifest)
- `tsconfig.build.json` (config)
- `tsconfig.json` (config)
- `tsconfig.type-tests.json` (config)

## Top-level layout

- `(root files)` — 23 analysed file(s)
- `docs` — 20 analysed file(s)
- `type-tests` — 10 analysed file(s)
- `.github` — 6 analysed file(s)
- `src` — 5 analysed file(s)
- `public` — 3 analysed file(s)
- `e2e` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `512bcf2bf28498d13e05aef70c3e9147d752612a` is the revision these paths and observations refer to.
