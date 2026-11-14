# Project structure: vidstack/player

**Analysed commit:** `0133da67e4f84a5aaad59c63853b12c6cda0a6a9`

**Commit reference:** [0133da67e4f84a5aaad59c63853b12c6cda0a6a9](https://github.com/vidstack/player/commit/0133da67e4f84a5aaad59c63853b12c6cda0a6a9)

**Tree at this commit:** [vidstack/player@0133da67e4f8](https://github.com/vidstack/player/tree/0133da67e4f84a5aaad59c63853b12c6cda0a6a9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vidstack/player |
| Description | Deprecated in favour of Video.js 10; security fixes only until January 2028. UI components and hooks for building video and audio players on the web. |
| Stars | 3735 |
| Forks | 230 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `0133da67e4f84a5aaad59c63853b12c6cda0a6a9` |
| Retrieved at | 2026-11-14T19:15:09.505127+00:00 |
| Files in this snapshot | 597 |

## Directory tree

```text
.build/  (1 files)
  copy-pkg-files.js
.github/  (12 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    config.yml
  maintenance/  (5 files)
    close-backlog.sh
    issue.md
    pull-request.md
    security.md
    triage.mjs
  workflows/  (2 files)
    ci.yml
    maintenance-triage.yml
  CONTRIBUTING.md
  PULL_REQUEST_TEMPLATE.md
  REPRO.md
.scripts/  (5 files)
  copy.js
  release.js
  run-on-change.js
  sandbox.js
  test-node-esm.js
.vscode/  (1 files)
  settings.json
examples/  (1 files)
  README.md
packages/  (561 files)
  react/  (148 files)
    .templates/  (6 files)
      … 6 files under this directory
    npm/  (1 files)
      … 1 files under this directory
    src/  (132 files)
      … 132 files under this directory
    AGENTS.md
    LICENSE
    README.md
    analyze.config.ts
    package.json
    tsconfig.build.json
    tsconfig.json
    tsdown.config.ts
    vite.config.ts
  vidstack/  (413 files)
    .templates/  (3 files)
      … 3 files under this directory
    npm/  (12 files)
      … 12 files under this directory
    src/  (371 files)
      … 371 files under this directory
    styles/  (18 files)
      … 18 files under this directory
    AGENTS.md
    LICENSE
    README.md
    analyze.config.ts
    package.json
    tsconfig.build.json
    tsconfig.json
    tsdown.config.ts
    vite.config.ts
.editorconfig
.gitattributes
.gitignore
.nvmrc
.oxfmtrc.json
AGENTS.md
CHANGELOG.md
LICENSE
README.md
RELEASES.md
SECURITY.md
cliff.toml
package.json
pnpm-workspace.yaml
tsconfig.json
turbo.json
```

## Entry points

- [packages/react/src/index.ts](https://github.com/vidstack/player/blob/0133da67e4f84a5aaad59c63853b12c6cda0a6a9/packages/react/src/index.ts)
- [packages/vidstack/src/index.ts](https://github.com/vidstack/player/blob/0133da67e4f84a5aaad59c63853b12c6cda0a6a9/packages/vidstack/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 14 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 475 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 35 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/maintenance-triage.yml` (ci)
- `.oxfmtrc.json` (config)
- `.vscode/settings.json` (config)
- `cliff.toml` (config)
- `package.json` (manifest)
- `packages/react/package.json` (manifest)
- `packages/react/tsconfig.build.json` (config)
- `packages/react/tsconfig.json` (config)
- `packages/vidstack/package.json` (manifest)
- `packages/vidstack/tsconfig.build.json` (config)
- `packages/vidstack/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `turbo.json` (config)

## Top-level layout

- `packages` — 561 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 12 analysed file(s)
- `.scripts` — 5 analysed file(s)
- `.build` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `examples` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0133da67e4f84a5aaad59c63853b12c6cda0a6a9` is the revision these paths and observations refer to.
