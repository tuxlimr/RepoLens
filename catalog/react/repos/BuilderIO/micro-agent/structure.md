# Project structure: BuilderIO/micro-agent

**Analysed commit:** `f33523ce9f9c52a698d13a2883eb2ba7fb4fb462`

**Commit reference:** [f33523ce9f9c52a698d13a2883eb2ba7fb4fb462](https://github.com/BuilderIO/micro-agent/commit/f33523ce9f9c52a698d13a2883eb2ba7fb4fb462)

**Tree at this commit:** [BuilderIO/micro-agent@f33523ce9f9c](https://github.com/BuilderIO/micro-agent/tree/f33523ce9f9c52a698d13a2883eb2ba7fb4fb462)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | BuilderIO/micro-agent |
| Description | An AI agent that writes (actually useful) code for you |
| Stars | 4335 |
| Forks | 382 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `f33523ce9f9c52a698d13a2883eb2ba7fb4fb462` |
| Retrieved at | 2026-11-14T19:14:49.118016+00:00 |
| Files in this snapshot | 82 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    buildOnPR.yml
.husky/  (2 files)
  commit-msg
  pre-commit
.vscode/  (1 files)
  settings.json
src/  (51 files)
  commands/  (2 files)
    config.ts
    update.ts
  helpers/  (36 files)
    apply-unified-diff.test.ts
    apply-unified-diff.ts
    base64.ts
    config.test.ts
    config.ts
    constants.ts
    dependency-files.test.ts
    dependency-files.ts
    error.ts
    exit-on-cancel.ts
    file-exists.ts
    find-package-json.ts
    find-visual-file.ts
    generate-ascii-tree.test.ts
    generate-ascii-tree.ts
    generate.ts
    get-screenshot.ts
    get-test-command.ts
    interactive-mode.ts
    invalid-project-warning.ts
    iterate-on-test-command.ts
    iterate-on-test.ts
    llm.test.ts
    llm.ts
    … 12 more files
  tests/  (12 files)
    angular-parser/  (4 files)
      … 4 files under this directory
    integration/  (4 files)
      … 4 files under this directory
    ternary/  (4 files)
      … 4 files under this directory
  cli.ts
test/  (13 files)
  fixtures/  (1 files)
    add.json
  nextjs-app/  (12 files)
    app/  (3 files)
      … 3 files under this directory
    public/  (2 files)
      … 2 files under this directory
    .gitignore
    README.md
    next.config.mjs
    package.json
    postcss.config.mjs
    tailwind.config.ts
    tsconfig.json
.commitlintrc.json
.eslintrc.cjs
.gitignore
.nvmrc
.prettierignore
.prettierrc
.prettierrc.json
.versionrc.json
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
package.json
tsconfig.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cli.ts package | library | Observed | Groups 1 file(s) under cli.ts package (observed from repository paths and static analysis). |
| commands package | library | Observed | Groups 2 file(s) under commands package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 36 file(s) under helpers package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 25 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.commitlintrc.json` (config)
- `.github/workflows/buildOnPR.yml` (ci)
- `.prettierrc.json` (config)
- `.versionrc.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 51 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `test` — 13 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f33523ce9f9c52a698d13a2883eb2ba7fb4fb462` is the revision these paths and observations refer to.
