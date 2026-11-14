# Project structure: wevm/wagmi

**Analysed commit:** `b148425e51be6b9bfc750568918f5dd0bf8f94ca`

**Commit reference:** [b148425e51be6b9bfc750568918f5dd0bf8f94ca](https://github.com/wevm/wagmi/commit/b148425e51be6b9bfc750568918f5dd0bf8f94ca)

**Tree at this commit:** [wevm/wagmi@b148425e51be](https://github.com/wevm/wagmi/tree/b148425e51be6b9bfc750568918f5dd0bf8f94ca)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | wevm/wagmi |
| Description | Reactive primitives for Ethereum apps |
| Stars | 6776 |
| Forks | 1467 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `b148425e51be6b9bfc750568918f5dd0bf8f94ca` |
| Retrieved at | 2026-11-14T19:14:02.115016+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.agents/  (2 files)
  skills/  (1 files)
    wagmi-development/  (1 files)
      … 1 files under this directory
  README.md
.changeset/  (4 files)
  README.md
  config.json
  quiet-foxes-inject.md
  wallet-initiated-connect-listener.md
.github/  (18 files)
  DISCUSSION_TEMPLATE/  (1 files)
    connector-request.yml
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    docs_issue.yml
  workflows/  (6 files)
    changesets.yml
    issue-labeled.yml
    lock-issue.yml
    pull-request.yml
    scorecard.yml
    verify.yml
  CODEOWNERS
  CONTRIBUTING.md
  README.md
  SECURITY.md
  dependabot.yml
  logo-dark.svg
  logo-light.svg
  pull_request_template.md
.vscode/  (3 files)
  extensions.json
  settings.json
  workspace.code-workspace
packages/  (768 files)
  cli/  (71 files)
    src/  (63 files)
      … 63 files under this directory
    test/  (3 files)
      … 3 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
  connectors/  (18 files)
    src/  (13 files)
      … 13 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
  core/  (421 files)
    src/  (415 files)
      … 415 files under this directory
    test/  (1 files)
      … 1 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
  create-wagmi/  (73 files)
    src/  (6 files)
      … 6 files under this directory
    templates/  (62 files)
      … 62 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.build.json
    tsconfig.json
  engine-tests/  (9 files)
    next/  (4 files)
      … 4 files under this directory
    vite/  (2 files)
      … 2 files under this directory
    package.json
    test.ts
    tsconfig.json
  react/  (176 files)
    src/  (174 files)
      … 174 files under this directory
    README.md
    package.json
.gitignore
FUNDING.json
LICENSE
biome.json
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 34 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 273 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 413 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/DISCUSSION_TEMPLATE/connector-request.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/docs_issue.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/changesets.yml` (ci)
- `.github/workflows/issue-labeled.yml` (ci)
- `.github/workflows/lock-issue.yml` (ci)
- `.github/workflows/pull-request.yml` (ci)
- `.github/workflows/scorecard.yml` (ci)
- `.github/workflows/verify.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `FUNDING.json` (config)
- `biome.json` (config)
- `package.json` (manifest)
- `packages/cli/package.json` (manifest)
- `packages/cli/src/plugins/__fixtures__/foundry/foundry.toml` (config)
- `packages/cli/src/plugins/__fixtures__/hardhat/package.json` (manifest)
- `packages/cli/tsconfig.build.json` (config)
- `packages/cli/tsconfig.json` (config)
- `packages/connectors/package.json` (manifest)
- `packages/connectors/tsconfig.build.json` (config)
- `packages/connectors/tsconfig.json` (config)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.build.json` (config)
- `packages/core/tsconfig.json` (config)
- `packages/create-wagmi/package.json` (manifest)
- `packages/create-wagmi/templates/next/package.json` (manifest)
- `packages/create-wagmi/templates/next/tsconfig.json` (config)
- `packages/create-wagmi/templates/nuxt/package.json` (manifest)
- `packages/create-wagmi/templates/nuxt/server/tsconfig.json` (config)
- `packages/create-wagmi/templates/nuxt/tsconfig.json` (config)
- `packages/create-wagmi/templates/vite-react/package.json` (manifest)
- `packages/create-wagmi/templates/vite-react/tsconfig.json` (config)
- `packages/create-wagmi/templates/vite-react/tsconfig.node.json` (config)
- `packages/create-wagmi/templates/vite-vanilla/package.json` (manifest)
- `packages/create-wagmi/templates/vite-vanilla/tsconfig.json` (config)
- `packages/create-wagmi/templates/vite-vue/package.json` (manifest)
- `packages/create-wagmi/templates/vite-vue/tsconfig.json` (config)
- `packages/create-wagmi/templates/vite-vue/tsconfig.node.json` (config)
- `packages/create-wagmi/tsconfig.build.json` (config)
- `packages/create-wagmi/tsconfig.json` (config)
- `packages/engine-tests/next/tsconfig.json` (config)
- `packages/engine-tests/package.json` (manifest)
- `packages/engine-tests/tsconfig.json` (config)
- `packages/react/package.json` (manifest)

## Top-level layout

- `packages` — 768 analysed file(s)
- `.github` — 18 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `.changeset` — 4 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `.agents` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b148425e51be6b9bfc750568918f5dd0bf8f94ca` is the revision these paths and observations refer to.
