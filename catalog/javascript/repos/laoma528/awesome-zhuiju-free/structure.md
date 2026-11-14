# Project structure: laoma528/awesome-zhuiju-free

**Analysed commit:** `bacc0f32b72313b31f4cfc18d0a8b3c7ffb76904`

**Commit reference:** [bacc0f32b72313b31f4cfc18d0a8b3c7ffb76904](https://github.com/laoma528/awesome-zhuiju-free/commit/bacc0f32b72313b31f4cfc18d0a8b3c7ffb76904)

**Tree at this commit:** [laoma528/awesome-zhuiju-free@bacc0f32b723](https://github.com/laoma528/awesome-zhuiju-free/tree/bacc0f32b72313b31f4cfc18d0a8b3c7ffb76904)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | laoma528/awesome-zhuiju-free |
| Description | 免费无广告的追剧资源指南，人工精选资源、每天检测资源有效性。收录在线影视、影视APP、网盘搜索、磁力BT、字幕、TVBox / 影视仓空壳软件/配置地址、IPTV直播源、会员拼团、影视相关开源项目。开源，社区共同维护。 |
| Stars | 15620 |
| Forks | 1127 |
| Licence | CC-BY-4.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `bacc0f32b72313b31f4cfc18d0a8b3c7ffb76904` |
| Retrieved at | 2026-11-14T19:11:36.550584+00:00 |
| Files in this snapshot | 51 |

## Directory tree

```text
.githooks/  (1 files)
  pre-push
.github/  (10 files)
  ISSUE_TEMPLATE/  (3 files)
    broken-link.yml
    resource.yml
    rights-holder-request.yml
  workflows/  (6 files)
    check-availability.yml
    issue-to-resource-pr.yml
    public-files.yml
    update-open-source-stats.yml
    validate-data.yml
    weekly-release.yml
  pull_request_template.md
blog/  (17 files)
  articles/  (15 files)
    2026-07-12-awesome-zhuiju-free-guide.md
    2026-07-12-selene-tv-guide.md
    2026-07-12-tvbox-yingshicang-interface-guide.md
    2026-07-12-yingshicang-config-addresses.md
    2026-08-01-fongmi-download.md
    2026-08-01-ok-yingshi-download.md
    2026-08-01-peekpro-download.md
    2026-08-01-webhometv-download.md
    2026-08-01-yingshicang-download.md
    2026-08-29-about-awesome-zhuiju-free.md
    2026-08-29-friend-links.md
    2026-08-29-submit-resource.md
    2026-09-13-ios-yingshi-app.md
    2026-10-17-iptv-live-sources.md
    2026-11-01-android-yingshi-app.md
  README.md
  _template.md
docs/  (1 files)
  PUBLIC-FILES.md
reports/  (4 files)
  README.md
  availability.json
  notices.json
  verifications.json
resources/  (4 files)
  README.md
  android-yingshi-app-downloads.json
  resources.json
  schema.json
scripts/  (7 files)
  check-availability.mjs
  check-public-files.mjs
  generate-weekly-release.mjs
  publish-typecho.py
  sync-readme.mjs
  update-open-source-stats.mjs
  validate-data.mjs
.gitattributes
.gitignore
CLAUDE.md
CONTRIBUTING.md
LICENSE
MAINTAINERS.md
README.md
```

## Entry points

- [scripts/publish-typecho.py:569](https://github.com/laoma528/awesome-zhuiju-free/blob/bacc0f32b72313b31f4cfc18d0a8b3c7ffb76904/scripts/publish-typecho.py#L569)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: TimeoutSafeTransport. Observed top-level functions: add_common_document_arguments, add_get… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/broken-link.yml` (config)
- `.github/ISSUE_TEMPLATE/resource.yml` (config)
- `.github/ISSUE_TEMPLATE/rights-holder-request.yml` (config)
- `.github/workflows/check-availability.yml` (ci)
- `.github/workflows/issue-to-resource-pr.yml` (ci)
- `.github/workflows/public-files.yml` (ci)
- `.github/workflows/update-open-source-stats.yml` (ci)
- `.github/workflows/validate-data.yml` (ci)
- `.github/workflows/weekly-release.yml` (ci)
- `reports/availability.json` (config)
- `reports/notices.json` (config)
- `reports/verifications.json` (config)
- `resources/android-yingshi-app-downloads.json` (config)
- `resources/resources.json` (config)
- `resources/schema.json` (config)

## Top-level layout

- `blog` — 17 analysed file(s)
- `.github` — 10 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `scripts` — 7 analysed file(s)
- `reports` — 4 analysed file(s)
- `resources` — 4 analysed file(s)
- `.githooks` — 1 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `bacc0f32b72313b31f4cfc18d0a8b3c7ffb76904` is the revision these paths and observations refer to.
