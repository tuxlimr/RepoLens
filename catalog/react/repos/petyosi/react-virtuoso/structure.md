# Project structure: petyosi/react-virtuoso

**Analysed commit:** `cb6c1941d340b2d66ffeea830620cbaf7db3c3c5`

**Commit reference:** [cb6c1941d340b2d66ffeea830620cbaf7db3c3c5](https://github.com/petyosi/react-virtuoso/commit/cb6c1941d340b2d66ffeea830620cbaf7db3c3c5)

**Tree at this commit:** [petyosi/react-virtuoso@cb6c1941d340](https://github.com/petyosi/react-virtuoso/tree/cb6c1941d340b2d66ffeea830620cbaf7db3c3c5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | petyosi/react-virtuoso |
| Description | The most powerful virtual list component for React |
| Stars | 6491 |
| Forks | 368 |
| Licence | Not detected |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `cb6c1941d340b2d66ffeea830620cbaf7db3c3c5` |
| Retrieved at | 2026-11-14T19:14:05.046307+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.agents/  (1 files)
  plugins/  (1 files)
    marketplace.json
.changeset/  (2 files)
  README.md
  config.json
.claude-plugin/  (1 files)
  marketplace.json
.codex/  (7 files)
  environments/  (1 files)
    environment.toml
  skills/  (5 files)
    docs-guidance/  (5 files)
      … 5 files under this directory
  config.toml
.github/  (8 files)
  ISSUE_TEMPLATE/  (2 files)
    1.bug.md
    config.yml
  workflows/  (4 files)
    main.yml
    pr-checks.yml
    sync-skills.yml
    virtuoso.dev.yml
  FUNDING.yml
  dependabot.yml
apps/  (90 files)
  virtuoso.dev/  (90 files)
    .claude/  (1 files)
      … 1 files under this directory
    docs/  (1 files)
      … 1 files under this directory
    public/  (1 files)
      … 1 files under this directory
    registry/  (9 files)
      … 9 files under this directory
    src/  (66 files)
      … 66 files under this directory
    .example.env
    .gitignore
    .oxlintrc.json
    CHANGELOG.md
    README.md
    astro.config.mjs
    components.json
    package.json
    prettier.config.mjs
    registry.json
    tsconfig.json
    tsconfig.message-list.json
examples/  (10 files)
  .ladle/  (1 files)
    config.mjs
  react-virtuoso/  (5 files)
    hello.stories.tsx
    mui-list.stories.tsx
    mui-table.stories.tsx
    tanstack-table.stories.tsx
    window-scroll-top-items.stories.tsx
  .oxlintrc.json
  CHANGELOG.md
  package.json
  tsconfig.json
packages/  (666 files)
  data-table/  (241 files)
    .ladle/  (2 files)
      … 2 files under this directory
    docs/  (46 files)
      … 46 files under this directory
    src/  (159 files)
      … 159 files under this directory
    tests/  (25 files)
      … 25 files under this directory
    .oxlintrc.json
    CHANGELOG.md
    CLAUDE.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    vite.config.ts
    vitest.config.ts
  gurx/  (27 files)
    src/  (16 files)
      … 16 files under this directory
    .gitignore
    .oxlintrc.json
    CHANGELOG.json
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
    vitest.config.ts
  masonry/  (28 files)
    src/  (18 files)
      … 18 files under this directory
    .oxlintrc.json
    CHANGELOG.json
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
    vitest.workspace.ts
  message-list/  (28 files)
    docs/  (27 files)
      … 27 files under this directory
    README.md
  react-virtuoso/  (257 files)
    .ladle/  (1 files)
      … 1 files under this directory
    docs/  (31 files)
      … 31 files under this directory
    e2e/  (28 files)
      … 28 files under this directory
    examples/  (96 files)
      … 96 files under this directory
    src/  (60 files)
      … 60 files under this directory
    test/  (33 files)
      … 33 files under this directory
    .oxlintrc.json
    CHANGELOG.md
    LICENSE
    README.md
    package.json
    playwright.config.ts
    tsconfig.json
    vite.config.ts
  reactive-engine-core/  (62 files)
    .claude/  (1 files)
      … 1 files under this directory
    docs/  (6 files)
      … 6 files under this directory
    src/  (48 files)
      … 48 files under this directory
    .oxlintrc.json
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    vite.config.ts
    vitest.config.ts
  reactive-engine-examples/  (23 files)
    basic/  (18 files)
      … 18 files under this directory
    todo-app/  (3 files)
      … 3 files under this directory
    CHANGELOG.md
    package.json
.gitignore
.markdownlint.json
.markdownlintignore
.node-version
.oxfmtrc.json
.oxlintrc.json
AGENTS.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
README.md
knip.json
lefthook.json
package.json
```

## Entry points

- [packages/data-table/src/index.ts](https://github.com/petyosi/react-virtuoso/blob/cb6c1941d340b2d66ffeea830620cbaf7db3c3c5/packages/data-table/src/index.ts)
- [packages/gurx/src/index.ts](https://github.com/petyosi/react-virtuoso/blob/cb6c1941d340b2d66ffeea830620cbaf7db3c3c5/packages/gurx/src/index.ts)
- [packages/masonry/src/index.ts](https://github.com/petyosi/react-virtuoso/blob/cb6c1941d340b2d66ffeea830620cbaf7db3c3c5/packages/masonry/src/index.ts)
- [packages/react-virtuoso/src/index.tsx](https://github.com/petyosi/react-virtuoso/blob/cb6c1941d340b2d66ffeea830620cbaf7db3c3c5/packages/react-virtuoso/src/index.tsx)
- [packages/reactive-engine-core/src/index.ts](https://github.com/petyosi/react-virtuoso/blob/cb6c1941d340b2d66ffeea830620cbaf7db3c3c5/packages/reactive-engine-core/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apps package | library | Observed | Groups 54 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 32 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 367 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 8 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 133 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.agents/plugins/marketplace.json` (config)
- `.changeset/config.json` (config)
- `.claude-plugin/marketplace.json` (config)
- `.codex/config.toml` (config)
- `.codex/environments/environment.toml` (config)
- `.codex/skills/docs-guidance/agents/openai.yaml` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/pr-checks.yml` (ci)
- `.github/workflows/sync-skills.yml` (ci)
- `.github/workflows/virtuoso.dev.yml` (ci)
- `.markdownlint.json` (config)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `apps/virtuoso.dev/.claude/settings.local.json` (config)
- `apps/virtuoso.dev/.oxlintrc.json` (config)
- `apps/virtuoso.dev/components.json` (config)
- `apps/virtuoso.dev/package.json` (manifest)
- `apps/virtuoso.dev/registry.json` (config)
- `apps/virtuoso.dev/tsconfig.json` (config)
- `apps/virtuoso.dev/tsconfig.message-list.json` (config)
- `examples/.oxlintrc.json` (config)
- `examples/package.json` (manifest)
- `examples/tsconfig.json` (config)
- `knip.json` (config)
- `lefthook.json` (config)
- `package.json` (manifest)
- `packages/data-table/.oxlintrc.json` (config)
- `packages/data-table/package.json` (manifest)
- `packages/data-table/tsconfig.json` (config)
- `packages/gurx/.oxlintrc.json` (config)
- `packages/gurx/CHANGELOG.json` (config)
- `packages/gurx/package.json` (manifest)
- `packages/gurx/tsconfig.json` (config)
- `packages/gurx/tsconfig.node.json` (config)
- `packages/masonry/.oxlintrc.json` (config)
- `packages/masonry/CHANGELOG.json` (config)
- `packages/masonry/package.json` (manifest)
- `packages/masonry/tsconfig.json` (config)
- `packages/masonry/tsconfig.node.json` (config)
- `packages/react-virtuoso/.oxlintrc.json` (config)
- `packages/react-virtuoso/package.json` (manifest)
- `packages/react-virtuoso/tsconfig.json` (config)
- `packages/reactive-engine-core/.claude/settings.local.json` (config)
- `packages/reactive-engine-core/.oxlintrc.json` (config)
- `packages/reactive-engine-core/package.json` (manifest)
- `packages/reactive-engine-core/tsconfig.json` (config)
- `packages/reactive-engine-examples/package.json` (manifest)
- `packages/reactive-engine-examples/todo-app/db.json` (config)

## Top-level layout

- `packages` — 666 analysed file(s)
- `apps` — 90 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `examples` — 10 analysed file(s)
- `.github` — 8 analysed file(s)
- `.codex` — 7 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.agents` — 1 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `cb6c1941d340b2d66ffeea830620cbaf7db3c3c5` is the revision these paths and observations refer to.
