# Project structure: ant-design/x

**Analysed commit:** `da08db16714b608d7f5db248c2b2fcc30a756660`

**Commit reference:** [da08db16714b608d7f5db248c2b2fcc30a756660](https://github.com/ant-design/x/commit/da08db16714b608d7f5db248c2b2fcc30a756660)

**Tree at this commit:** [ant-design/x@da08db16714b](https://github.com/ant-design/x/tree/da08db16714b608d7f5db248c2b2fcc30a756660)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ant-design/x |
| Description | Craft AI-driven interface effortlessly🤖 |
| Stars | 4847 |
| Forks | 1175 |
| Licence | Not detected |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `da08db16714b608d7f5db248c2b2fcc30a756660` |
| Retrieved at | 2026-11-14T19:14:34.851015+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.github/  (17 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    feature_request.yml
  workflows/  (11 files)
    main.yml
    markdown-benchmark.yml
    pr-auto-merge.yml
    pr-contributor-welcome.yml
    preview-build.yml
    preview-deploy.yml
    preview-start.yml
    release-dingtalk.yml
    release-x.yml
    site-deploy.yml
    size-limit.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  PULL_REQUEST_TEMPLATE_CN.md
  dependabot.yml
.husky/  (2 files)
  commit-msg
  pre-commit
packages/  (769 files)
  x/  (543 files)
    .dumi/  (165 files)
      … 165 files under this directory
    alias/  (1 files)
      … 1 files under this directory
    components/  (366 files)
      … 366 files under this directory
    .dumirc.ts
    .fatherrc.ts
    .jest.js
    .lintstagedrc.json
    .surgeignore
    BUG_VERSIONS.json
    CNAME
    LICENSE
    README-zh_CN.md
    README.md
    bunfig.toml
  x-card/  (31 files)
    scripts/  (1 files)
      … 1 files under this directory
    src/  (22 files)
      … 22 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    .fatherrc.ts
    .jest.js
    .lintstagedrc.json
    README.md
    package.json
    tsconfig.json
  x-markdown/  (70 files)
    scripts/  (2 files)
      … 2 files under this directory
    src/  (50 files)
      … 50 files under this directory
    tests/  (5 files)
      … 5 files under this directory
    typings/  (3 files)
      … 3 files under this directory
    .fatherrc.ts
    .jest.js
    BUG_VERSIONS.json
    LICENSE
    README-zh_CN.md
    README.md
    jest-puppeteer.config.js
    mako.config.json
    package.json
    tsconfig.json
  x-sdk/  (49 files)
    scripts/  (1 files)
      … 1 files under this directory
    src/  (29 files)
      … 29 files under this directory
    tests/  (7 files)
      … 7 files under this directory
    typings/  (3 files)
      … 3 files under this directory
    .fatherrc.ts
    .jest.js
    BUG_VERSIONS.json
    LICENSE
    README-zh_CN.md
    README.md
    mako.config.json
    package.json
    tsconfig.json
  x-skill/  (76 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    scripts/  (6 files)
      … 6 files under this directory
    skills/  (27 files)
      … 27 files under this directory
    skills-zh/  (27 files)
      … 27 files under this directory
    src/  (6 files)
      … 6 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    .fatherrc.ts
    .gitignore
    .skill.json
    LICENSE
    README-zh_CN.md
    README.md
    package.json
    tsconfig.json
.editorconfig
.gitignore
.lintstagedrc.json
.prettierrc
CHANGELOG.en-US.md
CHANGELOG.zh-CN.md
CNAME
README-zh_CN.md
README.md
biome.json
package.json
```

## Entry points

- [packages/x-card/src/index.ts](https://github.com/ant-design/x/blob/da08db16714b608d7f5db248c2b2fcc30a756660/packages/x-card/src/index.ts)
- [packages/x-markdown/src/index.ts](https://github.com/ant-design/x/blob/da08db16714b608d7f5db248c2b2fcc30a756660/packages/x-markdown/src/index.ts)
- [packages/x-sdk/src/index.ts](https://github.com/ant-design/x/blob/da08db16714b608d7f5db248c2b2fcc30a756660/packages/x-sdk/src/index.ts)
- [packages/x-skill/src/index.ts](https://github.com/ant-design/x/blob/da08db16714b608d7f5db248c2b2fcc30a756660/packages/x-skill/src/index.ts)
- [packages/x/components/index.ts](https://github.com/ant-design/x/blob/da08db16714b608d7f5db248c2b2fcc30a756660/packages/x/components/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 25 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 529 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 4 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/markdown-benchmark.yml` (ci)
- `.github/workflows/pr-auto-merge.yml` (ci)
- `.github/workflows/pr-contributor-welcome.yml` (ci)
- `.github/workflows/preview-build.yml` (ci)
- `.github/workflows/preview-deploy.yml` (ci)
- `.github/workflows/preview-start.yml` (ci)
- `.github/workflows/release-dingtalk.yml` (ci)
- `.github/workflows/release-x.yml` (ci)
- `.github/workflows/site-deploy.yml` (ci)
- `.github/workflows/size-limit.yml` (ci)
- `.lintstagedrc.json` (config)
- `biome.json` (config)
- `package.json` (manifest)
- `packages/x-card/.lintstagedrc.json` (config)
- `packages/x-card/package.json` (manifest)
- `packages/x-card/tsconfig.json` (config)
- `packages/x-markdown/BUG_VERSIONS.json` (config)
- `packages/x-markdown/mako.config.json` (config)
- `packages/x-markdown/package.json` (manifest)
- `packages/x-markdown/src/plugins/version/plugin-meta.json` (config)
- `packages/x-markdown/tsconfig.json` (config)
- `packages/x-sdk/BUG_VERSIONS.json` (config)
- `packages/x-sdk/mako.config.json` (config)
- `packages/x-sdk/package.json` (manifest)
- `packages/x-sdk/tsconfig.json` (config)
- `packages/x-skill/.claude-plugin/marketplace.json` (config)
- `packages/x-skill/.skill.json` (config)
- `packages/x-skill/package.json` (manifest)
- `packages/x-skill/src/skill-meta.json` (config)
- `packages/x-skill/tsconfig.json` (config)
- `packages/x/.dumi/theme/locales/en-US.json` (config)
- `packages/x/.dumi/theme/locales/zh-CN.json` (config)
- `packages/x/.dumi/tsconfig.json` (config)
- `packages/x/.lintstagedrc.json` (config)
- `packages/x/BUG_VERSIONS.json` (config)
- `packages/x/bunfig.toml` (config)

## Top-level layout

- `packages` — 769 analysed file(s)
- `.github` — 17 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `da08db16714b608d7f5db248c2b2fcc30a756660` is the revision these paths and observations refer to.
