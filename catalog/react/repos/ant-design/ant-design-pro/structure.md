# Project structure: ant-design/ant-design-pro

**Analysed commit:** `42f2cb1d303380909ea04c73b5e60679d09c321a`

**Commit reference:** [42f2cb1d303380909ea04c73b5e60679d09c321a](https://github.com/ant-design/ant-design-pro/commit/42f2cb1d303380909ea04c73b5e60679d09c321a)

**Tree at this commit:** [ant-design/ant-design-pro@42f2cb1d3033](https://github.com/ant-design/ant-design-pro/tree/42f2cb1d303380909ea04c73b5e60679d09c321a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ant-design/ant-design-pro |
| Description | 👨🏻‍💻👩🏻‍💻 Use Ant Design like a Pro! |
| Stars | 38960 |
| Forks | 8245 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `42f2cb1d303380909ea04c73b5e60679d09c321a` |
| Retrieved at | 2026-11-14T19:13:00.803548+00:00 |
| Files in this snapshot | 326 |

## Directory tree

```text
.claude/  (2 files)
  skills/  (2 files)
    antd/  (1 files)
      … 1 files under this directory
    pro-upgrade/  (1 files)
      … 1 files under this directory
.github/  (15 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    question.md
  workflows/  (10 files)
    antd-cli.yml
    ci.yml
    coverage.yml
    deploy.yml
    e2e.yml
    emoji-helper.yml
    issue-labeled.yml
    preview-build.yml
    preview-deploy.yml
    react-doctor.yml
  FUNDING.yml
  dependabot.yml
.husky/  (2 files)
  commit-msg
  pre-commit
cloudflare-worker/  (20 files)
  src/  (17 files)
    data/  (5 files)
      … 5 files under this directory
    routes/  (10 files)
      … 10 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    index.ts
  package.json
  tsconfig.json
  wrangler.toml
config/  (7 files)
  config.ts
  defaultSettings.ts
  md-raw-loader.cjs
  oneapi.json
  proxy.ts
  routes.simple.ts
  routes.ts
docs/  (4 files)
  roadmap/  (2 files)
    v6.1.0-release-plan.md
    v6.1.0-upgrade-evaluation.md
  cheatsheet.en-US.md
  cheatsheet.zh-CN.md
e2e/  (1 files)
  login.spec.ts
mock/  (6 files)
  fakeList.ts
  listTableList.ts
  notices.ts
  route.ts
  user.ts
  utils.ts
public/  (4 files)
  scripts/  (1 files)
    loading.js
  CNAME
  logo.svg
  pro_icon.svg
scripts/  (2 files)
  i18n-remove.js
  simple.js
src/  (240 files)
  components/  (18 files)
    ArticleListContent/  (2 files)
      … 2 files under this directory
    AvatarList/  (2 files)
      … 2 files under this directory
    ErrorBoundary/  (1 files)
      … 1 files under this directory
    Footer/  (1 files)
      … 1 files under this directory
    HeaderDropdown/  (1 files)
      … 1 files under this directory
    OfflineBanner/  (1 files)
      … 1 files under this directory
    RightContent/  (5 files)
      … 5 files under this directory
    StandardFormRow/  (2 files)
      … 2 files under this directory
    TagSelect/  (2 files)
      … 2 files under this directory
    index.ts
  locales/  (64 files)
    bn-BD/  (7 files)
      … 7 files under this directory
    en-US/  (7 files)
      … 7 files under this directory
    fa-IR/  (7 files)
      … 7 files under this directory
    id-ID/  (7 files)
      … 7 files under this directory
    ja-JP/  (7 files)
      … 7 files under this directory
    pt-BR/  (7 files)
      … 7 files under this directory
    zh-CN/  (7 files)
      … 7 files under this directory
    zh-TW/  (7 files)
      … 7 files under this directory
    bn-BD.ts
    en-US.ts
    fa-IR.ts
    id-ID.ts
    ja-JP.ts
    pt-BR.ts
    zh-CN.ts
    zh-TW.ts
  pages/  (138 files)
    account/  (23 files)
      … 23 files under this directory
    chatbot/  (4 files)
      … 4 files under this directory
    dashboard/  (39 files)
      … 39 files under this directory
    exception/  (3 files)
      … 3 files under this directory
    form/  (13 files)
      … 13 files under this directory
    list/  (28 files)
      … 28 files under this directory
    profile/  (9 files)
      … 9 files under this directory
    result/  (4 files)
      … 4 files under this directory
    table-list/  (4 files)
      … 4 files under this directory
    user/  (7 files)
      … 7 files under this directory
    Admin.tsx
    Welcome-dark.css
    Welcome.css
    Welcome.tsx
  services/  (4 files)
    ant-design-pro/  (4 files)
      … 4 files under this directory
  utils/  (3 files)
    chinaDivision.test.ts
    chinaDivision.ts
    format.ts
  access.test.ts
  access.ts
  app.test.tsx
  app.tsx
  global.less
  global.style.ts
  global.tsx
  loading.tsx
  manifest.json
  requestErrorConfig.test.ts
  requestErrorConfig.ts
  service-worker.js
  typings.d.ts
tests/  (3 files)
  __mocks__/  (2 files)
    mermaid.ts
    raw.ts
  setupTests.ts
types/  (2 files)
  cache/  (1 files)
    mock/  (1 files)
      … 1 files under this directory
  index.d.ts
.commitlintrc.js
.editorconfig
.gitignore
.lintstagedrc
CLAUDE.md
CODE_OF_CONDUCT.md
LICENSE
README.md
README.zh-CN.md
biome.json
codecov.yml
doctor.config.json
package.json
playwright.config.ts
tailwind.config.js
tailwind.css
tsconfig.json
vitest.config.ts
```

## Entry points

- [cloudflare-worker/src/index.ts](https://github.com/ant-design/ant-design-pro/blob/42f2cb1d303380909ea04c73b5e60679d09c321a/cloudflare-worker/src/index.ts)
- [src/app.tsx](https://github.com/ant-design/ant-design-pro/blob/42f2cb1d303380909ea04c73b5e60679d09c321a/src/app.tsx)
- [src/components/ArticleListContent/index.tsx](https://github.com/ant-design/ant-design-pro/blob/42f2cb1d303380909ea04c73b5e60679d09c321a/src/components/ArticleListContent/index.tsx)
- [src/components/AvatarList/index.tsx](https://github.com/ant-design/ant-design-pro/blob/42f2cb1d303380909ea04c73b5e60679d09c321a/src/components/AvatarList/index.tsx)
- [src/components/ErrorBoundary/index.tsx](https://github.com/ant-design/ant-design-pro/blob/42f2cb1d303380909ea04c73b5e60679d09c321a/src/components/ErrorBoundary/index.tsx)
- [src/components/Footer/index.tsx](https://github.com/ant-design/ant-design-pro/blob/42f2cb1d303380909ea04c73b5e60679d09c321a/src/components/Footer/index.tsx)
- [src/components/HeaderDropdown/index.tsx](https://github.com/ant-design/ant-design-pro/blob/42f2cb1d303380909ea04c73b5e60679d09c321a/src/components/HeaderDropdown/index.tsx)
- [src/components/OfflineBanner/index.tsx](https://github.com/ant-design/ant-design-pro/blob/42f2cb1d303380909ea04c73b5e60679d09c321a/src/components/OfflineBanner/index.tsx)
- [src/components/RightContent/index.tsx](https://github.com/ant-design/ant-design-pro/blob/42f2cb1d303380909ea04c73b5e60679d09c321a/src/components/RightContent/index.tsx)
- [src/components/StandardFormRow/index.tsx](https://github.com/ant-design/ant-design-pro/blob/42f2cb1d303380909ea04c73b5e60679d09c321a/src/components/StandardFormRow/index.tsx)
- [src/components/TagSelect/index.tsx](https://github.com/ant-design/ant-design-pro/blob/42f2cb1d303380909ea04c73b5e60679d09c321a/src/components/TagSelect/index.tsx)
- [src/components/index.ts](https://github.com/ant-design/ant-design-pro/blob/42f2cb1d303380909ea04c73b5e60679d09c321a/src/components/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| access.test.ts package | library | Observed | Groups 1 file(s) under access.test.ts package (observed from repository paths and static analysis). |
| access.ts package | library | Observed | Groups 1 file(s) under access.ts package (observed from repository paths and static analysis). |
| API layer | api | Observed | Groups 10 file(s) under api layer (observed from repository paths and static analysis). |
| app.test.tsx package | library | Observed | Groups 1 file(s) under app.test.tsx package (observed from repository paths and static analysis). |
| app.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| cloudflare-worker package | library | Observed | Groups 2 file(s) under cloudflare-worker package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 18 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 28 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 1 file(s) under e2e package (observed from repository paths and static analysis). |
| global.style.ts package | library | Observed | Groups 1 file(s) under global.style.ts package (observed from repository paths and static analysis). |
| global.tsx package | library | Observed | Groups 1 file(s) under global.tsx package (observed from repository paths and static analysis). |
| loading.tsx package | library | Observed | Groups 1 file(s) under loading.tsx package (observed from repository paths and static analysis). |
| locales package | library | Observed | Groups 64 file(s) under locales package (observed from repository paths and static analysis). |
| mock package | library | Observed | Groups 6 file(s) under mock package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 124 file(s) under pages package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 1 file(s) under public package (observed from repository paths and static analysis). |
| requestErrorConfig.test.ts package | library | Observed | Groups 1 file(s) under requesterrorconfig.test.ts package (observed from repository paths and static analysis). |
| requestErrorConfig.ts package | library | Observed | Groups 1 file(s) under requesterrorconfig.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 4 file(s) under service / domain layer (observed from repository paths and static analysis). |
| service-worker.js package | library | Observed | Groups 1 file(s) under service-worker.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 2 file(s) under types package (observed from repository paths and static analysis). |
| typings.d.ts package | library | Observed | Groups 1 file(s) under typings.d.ts package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 3 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/antd-cli.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/coverage.yml` (ci)
- `.github/workflows/deploy.yml` (ci)
- `.github/workflows/e2e.yml` (ci)
- `.github/workflows/emoji-helper.yml` (ci)
- `.github/workflows/issue-labeled.yml` (ci)
- `.github/workflows/preview-build.yml` (ci)
- `.github/workflows/preview-deploy.yml` (ci)
- `.github/workflows/react-doctor.yml` (ci)
- `biome.json` (config)
- `cloudflare-worker/package.json` (manifest)
- `cloudflare-worker/tsconfig.json` (config)
- `cloudflare-worker/wrangler.toml` (config)
- `codecov.yml` (config)
- `config/oneapi.json` (config)
- `doctor.config.json` (config)
- `package.json` (manifest)
- `src/manifest.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 240 analysed file(s)
- `cloudflare-worker` — 20 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 15 analysed file(s)
- `config` — 7 analysed file(s)
- `mock` — 6 analysed file(s)
- `docs` — 4 analysed file(s)
- `public` — 4 analysed file(s)
- `tests` — 3 analysed file(s)
- `.claude` — 2 analysed file(s)
- `.husky` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `types` — 2 analysed file(s)
- `e2e` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `42f2cb1d303380909ea04c73b5e60679d09c321a` is the revision these paths and observations refer to.
