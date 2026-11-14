# Project structure: code-hike/codehike

**Analysed commit:** `cd81d8af1c503b699cbf0458d504e4578bcb9c74`

**Commit reference:** [cd81d8af1c503b699cbf0458d504e4578bcb9c74](https://github.com/code-hike/codehike/commit/cd81d8af1c503b699cbf0458d504e4578bcb9c74)

**Tree at this commit:** [code-hike/codehike@cd81d8af1c50](https://github.com/code-hike/codehike/tree/cd81d8af1c503b699cbf0458d504e4578bcb9c74)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | code-hike/codehike |
| Description | Build rich content websites with Markdown and React |
| Stars | 5399 |
| Forks | 168 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | next |
| Analysed commit | `cd81d8af1c503b699cbf0458d504e4578bcb9c74` |
| Retrieved at | 2026-11-14T19:14:21.279201+00:00 |
| Files in this snapshot | 409 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (14 files)
  scripts/  (9 files)
    git-utils.mjs
    md-utils.mjs
    params.mjs
    pr-merged.mjs
    pr-updated.mjs
    prepare-release.mjs
    readme.md
    release.mjs
    website-pr.mjs
  workflows/  (5 files)
    pr-build.yml
    pr-comment.yml
    pr-merged.yml
    push-to-next.yml
    release-pr-merged.yml
.vscode/  (1 files)
  settings.json
apps/  (257 files)
  web/  (257 files)
    app/  (41 files)
      … 41 files under this directory
    components/  (36 files)
      … 36 files under this directory
    content/  (82 files)
      … 82 files under this directory
    demos/  (79 files)
      … 79 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    public/  (2 files)
      … 2 files under this directory
    ui/  (7 files)
      … 7 files under this directory
    .gitignore
    components.json
    mdx-components.tsx
    next.config.mjs
    package.json
    postcss.config.js
    tailwind.config.ts
    theme.mjs
    tsconfig.json
packages/  (127 files)
  codehike/  (123 files)
    src/  (29 files)
      … 29 files under this directory
    tests/  (90 files)
      … 90 files under this directory
    CHANGELOG.md
    package.json
    readme.md
    tsconfig.json
  recma/  (2 files)
    index.js
    package.json
  remark/  (2 files)
    index.js
    package.json
.gitignore
.prettierrc
CHANGELOG.md
license
package.json
pnpm-workspace.yaml
readme.md
turbo.json
```

## Entry points

- [packages/recma/index.js](https://github.com/code-hike/codehike/blob/cd81d8af1c503b699cbf0458d504e4578bcb9c74/packages/recma/index.js)
- [packages/remark/index.js](https://github.com/code-hike/codehike/blob/cd81d8af1c503b699cbf0458d504e4578bcb9c74/packages/remark/index.js)
- [apps/web/app/page.tsx](https://github.com/code-hike/codehike/blob/cd81d8af1c503b699cbf0458d504e4578bcb9c74/apps/web/app/page.tsx)
- [packages/codehike/src/index.ts](https://github.com/code-hike/codehike/blob/cd81d8af1c503b699cbf0458d504e4578bcb9c74/packages/codehike/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 3 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 130 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 31 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 94 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/workflows/pr-build.yml` (ci)
- `.github/workflows/pr-comment.yml` (ci)
- `.github/workflows/pr-merged.yml` (ci)
- `.github/workflows/push-to-next.yml` (ci)
- `.github/workflows/release-pr-merged.yml` (ci)
- `.vscode/settings.json` (config)
- `apps/web/app/landing/sponsors.json` (config)
- `apps/web/components.json` (config)
- `apps/web/content/docs/meta.json` (config)
- `apps/web/package.json` (manifest)
- `apps/web/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/codehike/package.json` (manifest)
- `packages/codehike/tsconfig.json` (config)
- `packages/recma/package.json` (manifest)
- `packages/remark/package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `turbo.json` (config)

## Top-level layout

- `apps` — 257 analysed file(s)
- `packages` — 127 analysed file(s)
- `.github` — 14 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `cd81d8af1c503b699cbf0458d504e4578bcb9c74` is the revision these paths and observations refer to.
