# Project structure: nomcopter/react-mosaic

**Analysed commit:** `a189cd943d6d602672bc111163157697b8befd41`

**Commit reference:** [a189cd943d6d602672bc111163157697b8befd41](https://github.com/nomcopter/react-mosaic/commit/a189cd943d6d602672bc111163157697b8befd41)

**Tree at this commit:** [nomcopter/react-mosaic@a189cd943d6d](https://github.com/nomcopter/react-mosaic/tree/a189cd943d6d602672bc111163157697b8befd41)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nomcopter/react-mosaic |
| Description | A React tiling window manager |
| Stars | 4803 |
| Forks | 244 |
| Licence | Other |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `a189cd943d6d602672bc111163157697b8befd41` |
| Retrieved at | 2026-11-14T19:14:35.511067+00:00 |
| Files in this snapshot | 174 |

## Directory tree

```text
.claude/  (18 files)
  agents/  (3 files)
    component-reviewer.md
    feature-planner.md
    mosaic-tree-expert.md
  commands/  (11 files)
    add-feature.md
    analyze-tree.md
    build.md
    explain-concept.md
    fix-issue.md
    lint.md
    refactor.md
    review-component.md
    test.md
    type-check.md
    update-deps.md
  context/  (2 files)
    architecture.md
    development.md
  README.md
  settings.json
.cursor/  (2 files)
  mcp.json
  setting.json
.github/  (18 files)
  agents/  (1 files)
    ci-monitor-subagent.agent.md
  prompts/  (1 files)
    monitor-ci.prompt.md
  skills/  (7 files)
    link-workspace-packages/  (1 files)
      … 1 files under this directory
    monitor-ci/  (1 files)
      … 1 files under this directory
    nx-generate/  (1 files)
      … 1 files under this directory
    nx-plugins/  (1 files)
      … 1 files under this directory
    nx-run-tasks/  (1 files)
      … 1 files under this directory
    nx-workspace/  (2 files)
      … 2 files under this directory
  workflows/  (6 files)
    claude.yml
    deployment.yml
    pr-validation.yml
    preview-deploy.yml
    publish.yaml
    validate-commits.yml
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
.verdaccio/  (1 files)
  config.yml
.vscode/  (2 files)
  mcp.json
  settings.json
apps/  (34 files)
  website/  (34 files)
    docs/  (13 files)
      … 13 files under this directory
    src/  (13 files)
      … 13 files under this directory
    static/  (1 files)
      … 1 files under this directory
    .gitignore
    babel.config.js
    docusaurus.config.ts
    package.json
    project.json
    sidebars.ts
    tsconfig.json
libs/  (75 files)
  react-mosaic-component/  (75 files)
    src/  (67 files)
      … 67 files under this directory
    .babelrc
    eslint.config.mjs
    package.json
    project.json
    tsconfig.json
    tsconfig.lib.json
    tsconfig.spec.json
    vite.config.ts
skills/  (1 files)
  react-mosaic/  (1 files)
    SKILL.md
tools/  (1 files)
  package-tests/  (1 files)
    package-exports.test.mjs
.claudeignore
.commitlintrc.json
.editorconfig
.gitignore
.mcp.json
.node-version
.npmignore
.prettierignore
.prettierrc.yml
AGENTS.md
CLAUDE.md
CONTRIBUTING.md
LICENSE
README.md
eslint.config.mjs
lefthook.yml
nx.json
package.json
tsconfig.base.json
tsconfig.json
tsup.config.ts
vitest.config.ts
```

## Entry points

- [libs/react-mosaic-component/src/index.ts](https://github.com/nomcopter/react-mosaic/blob/a189cd943d6d602672bc111163157697b8befd41/libs/react-mosaic-component/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apps package | library | Observed | Groups 12 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| libs package | library | Observed | Groups 64 file(s) under libs package (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 1 file(s) under tools package (observed from repository paths and static analysis). |

## Important files

- `.claude/settings.json` (config)
- `.commitlintrc.json` (config)
- `.cursor/mcp.json` (config)
- `.cursor/setting.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/claude.yml` (ci)
- `.github/workflows/deployment.yml` (ci)
- `.github/workflows/pr-validation.yml` (ci)
- `.github/workflows/preview-deploy.yml` (ci)
- `.github/workflows/publish.yaml` (ci)
- `.github/workflows/validate-commits.yml` (ci)
- `.mcp.json` (config)
- `.prettierrc.yml` (config)
- `.verdaccio/config.yml` (config)
- `.vscode/mcp.json` (config)
- `.vscode/settings.json` (config)
- `apps/website/package.json` (manifest)
- `apps/website/project.json` (config)
- `apps/website/tsconfig.json` (config)
- `lefthook.yml` (config)
- `libs/react-mosaic-component/package.json` (manifest)
- `libs/react-mosaic-component/project.json` (config)
- `libs/react-mosaic-component/tsconfig.json` (config)
- `libs/react-mosaic-component/tsconfig.lib.json` (config)
- `libs/react-mosaic-component/tsconfig.spec.json` (config)
- `nx.json` (config)
- `package.json` (manifest)
- `tsconfig.base.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `libs` — 75 analysed file(s)
- `apps` — 34 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `.claude` — 18 analysed file(s)
- `.github` — 18 analysed file(s)
- `.cursor` — 2 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.verdaccio` — 1 analysed file(s)
- `skills` — 1 analysed file(s)
- `tools` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a189cd943d6d602672bc111163157697b8befd41` is the revision these paths and observations refer to.
