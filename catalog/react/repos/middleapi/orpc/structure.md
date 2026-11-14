# Project structure: middleapi/orpc

**Analysed commit:** `ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc`

**Commit reference:** [ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc](https://github.com/middleapi/orpc/commit/ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc)

**Tree at this commit:** [middleapi/orpc@ab64ed68ffad](https://github.com/middleapi/orpc/tree/ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | middleapi/orpc |
| Description | Typesafe APIs Made Simple 🪄 |
| Stars | 5765 |
| Forks | 176 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc` |
| Retrieved at | 2026-11-14T19:14:14.280345+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.agents/  (35 files)
  skills/  (35 files)
    blume/  (1 files)
      … 1 files under this directory
    blume-migrate/  (32 files)
      … 32 files under this directory
    blume-update-docs/  (2 files)
      … 2 files under this directory
.claude/  (1 files)
  launch.json
.github/  (11 files)
  ISSUE_TEMPLATE/  (4 files)
    1-bug-report.yml
    2-feature-request.yml
    3-documentation.yml
    config.yml
  workflows/  (5 files)
    ci.yaml
    codspeed.yaml
    pullfrog.yml
    release.yaml
    sponsors-sync.yaml
  FUNDING.yml
  dependabot.yml
.vscode/  (2 files)
  extensions.json
  settings.json
.zed/  (1 files)
  settings.json
apps/  (212 files)
  content/  (212 files)
    blog/  (5 files)
      … 5 files under this directory
    components/  (7 files)
      … 7 files under this directory
    dev/  (1 files)
      … 1 files under this directory
    docs/  (145 files)
      … 145 files under this directory
    experts/  (1 files)
      … 1 files under this directory
    pages/  (25 files)
      … 25 files under this directory
    public/  (3 files)
      … 3 files under this directory
    search/  (2 files)
      … 2 files under this directory
    shared/  (3 files)
      … 3 files under this directory
    sponsors/  (12 files)
      … 12 files under this directory
    .gitignore
    blume.config.ts
    components.ts
    logo.svg
    package.json
    theme.css
    tsconfig.json
    wrangler.jsonc
benches/  (9 files)
  __shared__/  (1 files)
    payloads.ts
  effect-middleware.bench.ts
  json-schema-coercer.bench.ts
  openapi-link-handler.bench.ts
  openapi-serializer.bench.ts
  procedure-call.bench.ts
  rpc-link-handler.bench.ts
  rpc-serializer.bench.ts
  static-file-handler.bench.ts
packages/  (518 files)
  ai-sdk/  (12 files)
    src/  (8 files)
      … 8 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  arktype/  (8 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  bun/  (26 files)
    src/  (8 files)
      … 8 files under this directory
    tests/  (13 files)
      … 13 files under this directory
    .gitignore
    README.md
    bunfig.toml
    package.json
    tsconfig.json
  client/  (79 files)
    src/  (75 files)
      … 75 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  cloudflare/  (21 files)
    src/  (14 files)
      … 14 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
    vitest.config.ts
    wrangler.jsonc
  contract/  (52 files)
    src/  (48 files)
      … 48 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  effect/  (32 files)
    src/  (28 files)
      … 28 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  evlog/  (12 files)
    src/  (8 files)
      … 8 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  hibernation/  (9 files)
    src/  (6 files)
      … 6 files under this directory
    README.md
    package.json
    tsconfig.json
  json-schema/  (24 files)
    src/  (20 files)
      … 20 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  lock/  (18 files)
    src/  (14 files)
      … 14 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    README.md
    package.json
    tsconfig.json
  mcp/  (14 files)
    src/  (11 files)
      … 11 files under this directory
    README.md
    package.json
    tsconfig.json
  msw/  (12 files)
    src/  (9 files)
      … 9 files under this directory
    README.md
    package.json
    tsconfig.json
  nest/  (12 files)
    src/  (8 files)
      … 8 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  next/  (31 files)
    src/  (27 files)
      … 27 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  node/  (15 files)
    src/  (9 files)
      … 9 files under this directory
    tests/  (3 files)
      … 3 files under this directory
    README.md
    package.json
    tsconfig.json
  openapi/  (80 files)
    src/  (67 files)
      … 67 files under this directory
    tests/  (9 files)
      … 9 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  opentelemetry/  (10 files)
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  pinia-colada/  (37 files)
    src/  (28 files)
      … 28 files under this directory
    tests/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  pino/  (10 files)
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
    package.json
    tsconfig.json
  publisher/  (4 files)
    src/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    package.json
.env.example
.gitignore
AGENTS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
oxfmt.config.ts
oxlint.config.ts
package.json
```

## Entry points

- [packages/ai-sdk/src/index.ts](https://github.com/middleapi/orpc/blob/ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc/packages/ai-sdk/src/index.ts)
- [packages/arktype/src/index.ts](https://github.com/middleapi/orpc/blob/ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc/packages/arktype/src/index.ts)
- [packages/bun/src/index.ts](https://github.com/middleapi/orpc/blob/ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc/packages/bun/src/index.ts)
- [packages/client/src/index.ts](https://github.com/middleapi/orpc/blob/ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc/packages/client/src/index.ts)
- [packages/cloudflare/src/index.ts](https://github.com/middleapi/orpc/blob/ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc/packages/cloudflare/src/index.ts)
- [packages/contract/src/index.ts](https://github.com/middleapi/orpc/blob/ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc/packages/contract/src/index.ts)
- [packages/effect/src/index.ts](https://github.com/middleapi/orpc/blob/ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc/packages/effect/src/index.ts)
- [packages/evlog/src/index.ts](https://github.com/middleapi/orpc/blob/ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc/packages/evlog/src/index.ts)
- [packages/hibernation/src/index.ts](https://github.com/middleapi/orpc/blob/ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc/packages/hibernation/src/index.ts)
- [packages/json-schema/src/index.ts](https://github.com/middleapi/orpc/blob/ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc/packages/json-schema/src/index.ts)
- [packages/lock/src/index.ts](https://github.com/middleapi/orpc/blob/ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc/packages/lock/src/index.ts)
- [packages/mcp/src/index.ts](https://github.com/middleapi/orpc/blob/ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc/packages/mcp/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apps package | library | Observed | Groups 19 file(s) under apps package (observed from repository paths and static analysis). |
| benches package | library | Observed | Groups 9 file(s) under benches package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 45 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 113 file(s) under external integrations (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 293 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 32 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.claude/launch.json` (config)
- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/1-bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/2-feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/3-documentation.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yaml` (ci)
- `.github/workflows/codspeed.yaml` (ci)
- `.github/workflows/pullfrog.yml` (ci)
- `.github/workflows/release.yaml` (ci)
- `.github/workflows/sponsors-sync.yaml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `.zed/settings.json` (config)
- `apps/content/package.json` (manifest)
- `apps/content/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/ai-sdk/package.json` (manifest)
- `packages/ai-sdk/tsconfig.json` (config)
- `packages/arktype/package.json` (manifest)
- `packages/arktype/tsconfig.json` (config)
- `packages/bun/bunfig.toml` (config)
- `packages/bun/package.json` (manifest)
- `packages/bun/tsconfig.json` (config)
- `packages/client/package.json` (manifest)
- `packages/client/tsconfig.json` (config)
- `packages/cloudflare/package.json` (manifest)
- `packages/cloudflare/tsconfig.json` (config)
- `packages/contract/package.json` (manifest)
- `packages/contract/tsconfig.json` (config)
- `packages/effect/package.json` (manifest)
- `packages/effect/tsconfig.json` (config)
- `packages/evlog/package.json` (manifest)
- `packages/evlog/tsconfig.json` (config)
- `packages/hibernation/package.json` (manifest)
- `packages/hibernation/tsconfig.json` (config)
- `packages/json-schema/package.json` (manifest)
- `packages/json-schema/tsconfig.json` (config)
- `packages/lock/package.json` (manifest)
- `packages/lock/tsconfig.json` (config)
- `packages/mcp/package.json` (manifest)
- `packages/mcp/tsconfig.json` (config)
- `packages/msw/package.json` (manifest)
- `packages/msw/tsconfig.json` (config)
- `packages/nest/package.json` (manifest)
- `packages/nest/tsconfig.json` (config)
- `packages/next/package.json` (manifest)
- `packages/next/tsconfig.json` (config)
- `packages/node/package.json` (manifest)
- `packages/node/tsconfig.json` (config)
- `packages/openapi/package.json` (manifest)
- `packages/openapi/tsconfig.json` (config)
- `packages/opentelemetry/package.json` (manifest)
- `packages/opentelemetry/tsconfig.json` (config)
- `packages/pinia-colada/package.json` (manifest)
- `packages/pinia-colada/tsconfig.json` (config)
- `packages/pino/package.json` (manifest)
- `packages/pino/tsconfig.json` (config)
- `packages/publisher/package.json` (manifest)

## Top-level layout

- `packages` — 518 analysed file(s)
- `apps` — 212 analysed file(s)
- `.agents` — 35 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 11 analysed file(s)
- `benches` — 9 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.claude` — 1 analysed file(s)
- `.zed` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ab64ed68ffadeb2b7da6a7a5ae008e1a05205ffc` is the revision these paths and observations refer to.
