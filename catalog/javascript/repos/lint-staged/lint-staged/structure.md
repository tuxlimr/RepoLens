# Project structure: lint-staged/lint-staged

**Analysed commit:** `49b5472587a6ad112bb32fe1ea3d4c324f2e2ecc`

**Commit reference:** [49b5472587a6ad112bb32fe1ea3d4c324f2e2ecc](https://github.com/lint-staged/lint-staged/commit/49b5472587a6ad112bb32fe1ea3d4c324f2e2ecc)

**Tree at this commit:** [lint-staged/lint-staged@49b5472587a6](https://github.com/lint-staged/lint-staged/tree/49b5472587a6ad112bb32fe1ea3d4c324f2e2ecc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lint-staged/lint-staged |
| Description | 🚫💩 — Run tasks like formatters and linters against files staged in Git |
| Stars | 14761 |
| Forks | 482 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `49b5472587a6ad112bb32fe1ea3d4c324f2e2ecc` |
| Retrieved at | 2026-11-14T19:11:42.915084+00:00 |
| Files in this snapshot | 181 |

## Directory tree

```text
.changeset/  (3 files)
  README.md
  config.json
  modern-doors-speak.md
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    01-bug.md
    02-feature.md
    config.yml
  workflows/  (4 files)
    npm.yml
    pull-requests.yml
    release.yml
    security.yml
  FUNDING.yml
.husky/  (3 files)
  commit-msg
  pre-commit
  pre-push
.vscode/  (2 files)
  extensions.json
  settings.json
bin/  (1 files)
  lint-staged.js
lib/  (43 files)
  assertGitVersion.js
  cli.js
  colors.js
  config.d.ts
  config.js
  configFiles.js
  debug.js
  execGit.js
  figures.js
  file.js
  generateTasks.js
  getAbortController.js
  getDiffCommand.js
  getFunctionTask.js
  getIntentToAddFiles.js
  getMaxArgLength.js
  getSpawnedTask.js
  getSpawnedTasks.js
  getStagedFiles.js
  gitWorkflow.js
  groupFilesByConfig.js
  index.d.ts
  index.js
  killSubprocesses.js
  … 19 more files
scripts/  (1 files)
  test-node-range.js
test/  (103 files)
  __utils__/  (2 files)
    createTempDir.js
    getRepoRootPath.js
  e2e/  (7 files)
    __utils__/  (1 files)
      … 1 files under this directory
    git-pre-commit.test.js
    internal-errors.test.js
    kill-tasks-on-failure.test.js
    no-stash.test.js
    special-characters.test.js
    stdin-config.test.js
  integration/  (40 files)
    __fixtures__/  (2 files)
      … 2 files under this directory
    __utils__/  (3 files)
      … 3 files under this directory
    allow-empty.test.js
    basic-functionality.test.js
    binary-files.test.js
    continue-on-error.test.js
    diff-options.test.js
    fail-on-changes.test.js
    fail-to-spawn.test.js
    file-resurrection.test.js
    files-outside-cwd.test.js
    function-tasks.test.js
    git-amend.test.js
    git-lock-file.test.js
    git-submodules.test.js
    git-worktree.test.js
    gitWorkFlow.test.js
    hide-all.test.js
    hide-unstaged.test.js
    include-all-files.test.js
    intent-to-add.test.js
    merge-conflict.test.js
    multiple-config-files.test.js
    no-hide-partially-staged.test.js
    no-initial-commit.test.js
    no-revert.test.js
    … 11 more files
  types/  (2 files)
    config.test.ts
    index.test.ts
  unit/  (52 files)
    __mocks__/  (11 files)
      … 11 files under this directory
    __utils__/  (3 files)
      … 3 files under this directory
    assertGitVersion.spec.js
    cli.spec.js
    colors.spec.js
    debug.spec.js
    execGit.spec.js
    file.spec.js
    generateTasks.spec.js
    getAbortController.spec.js
    getDiffCommand.spec.js
    getFunctionTask.spec.js
    getMaxArgLength.spec.js
    getSpawnedTask.2.spec.js
    getSpawnedTask.spec.js
    getSpawnedTask.unmocked.spec.js
    getSpawnedTasks.3.spec.js
    getSpawnedTasks.spec.js
    getStagedFiles.spec.js
    gitWorkFlow.test.js
    groupFilesByConfig.spec.js
    index.spec.js
    index2.spec.js
    index3.spec.js
    killSubprocesses.spec.js
    loadConfig.spec.js
    … 14 more files
.editorconfig
.gitattributes
.gitignore
.node-version
.oxfmtrc.json
.oxlintrc.json
AGENTS.md
CHANGELOG.md
CONTRIBUTING.md
LICENSE
MIGRATION.md
README.md
commitlint.config.js
lint-staged.config.js
package.json
tsconfig.json
vitest.config.js
```

## Entry points

- [bin/lint-staged.js](https://github.com/lint-staged/lint-staged/blob/49b5472587a6ad112bb32fe1ea3d4c324f2e2ecc/bin/lint-staged.js)
- [test/unit/__mocks__/my-lint-staged-config/index.cjs](https://github.com/lint-staged/lint-staged/blob/49b5472587a6ad112bb32fe1ea3d4c324f2e2ecc/test/unit/__mocks__/my-lint-staged-config/index.cjs)
- [lib/index.js](https://github.com/lint-staged/lint-staged/blob/49b5472587a6ad112bb32fe1ea3d4c324f2e2ecc/lib/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 43 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 103 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/npm.yml` (ci)
- `.github/workflows/pull-requests.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/security.yml` (ci)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `test` — 103 analysed file(s)
- `lib` — 43 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 8 analysed file(s)
- `.changeset` — 3 analysed file(s)
- `.husky` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `bin` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `49b5472587a6ad112bb32fe1ea3d4c324f2e2ecc` is the revision these paths and observations refer to.
