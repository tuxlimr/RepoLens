# Project structure: tgbot-collection/YYeTsBot

**Analysed commit:** `de73b9c1aa9aad7affdf4228f6d1d0198195921d`

**Commit reference:** [de73b9c1aa9aad7affdf4228f6d1d0198195921d](https://github.com/tgbot-collection/YYeTsBot/commit/de73b9c1aa9aad7affdf4228f6d1d0198195921d)

**Tree at this commit:** [tgbot-collection/YYeTsBot@de73b9c1aa9a](https://github.com/tgbot-collection/YYeTsBot/tree/de73b9c1aa9aad7affdf4228f6d1d0198195921d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tgbot-collection/YYeTsBot |
| Description | 🎬 人人影视 机器人和网站，包含人人影视全部资源以及众多网友的网盘分享 |
| Stars | 16316 |
| Forks | 1836 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `de73b9c1aa9aad7affdf4228f6d1d0198195921d` |
| Retrieved at | 2026-11-14T19:08:52.029904+00:00 |
| Files in this snapshot | 111 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (1 files)
    docker.yaml
  FUNDING.yml
  dependabot.yml
conf/  (2 files)
  yyets.dmesg.app.conf
  yyets.env
yyets/  (35 files)
  BagAndDrag/  (9 files)
    zimuxia/  (2 files)
      … 2 files under this directory
    README.md
    bag.py
    cfkv.py
    convert_db.py
    create_db.py
    drag.py
    sample.json
  healthcheck/  (2 files)
    check.py
    restart_service.py
  management/  (2 files)
    format.json
    ui.py
  worker/  (21 files)
    public/  (16 files)
      … 16 files under this directory
    workers-site/  (2 files)
      … 2 files under this directory
    .cargo-ok
    README.md
    wrangler.toml
  __init__.py
yyetsbot/  (4 files)
  config.py
  fansub.py
  utils.py
  yyetsbot.py
yyetsweb/  (56 files)
  cmd/  (4 files)
    add_dl.py
    db.py
    douban_fix.py
    grafana_test_data.py
  common/  (5 files)
    __init__.py
    comments_check.py
    dump_db.py
    sync.py
    utils.py
  databases/  (9 files)
    __init__.py
    base.py
    comment.py
    douban.py
    grafana.py
    oauth.py
    other.py
    resources.py
    user.py
  handlers/  (9 files)
    __init__.py
    base.py
    comment.py
    douban.py
    grafana.py
    oauth.py
    other.py
    resources.py
    user.py
  templates/  (22 files)
    css/  (9 files)
      … 9 files under this directory
    js/  (4 files)
      … 4 files under this directory
    404.html
    ads.txt
    email_template.html
    googlee927c64a054a7beb.html
    help.html
    index.html
    resource.html
    robots.txt
    search.html
  tests/  (1 files)
    router_test.py
  README.md
  YYeTs-grafana.json
  go.mod
  go.sum
  server.go
  server.py
.dockerignore
.gitattributes
.gitignore
Dockerfile
LICENSE
Makefile
README.md
docker-compose.yml
requirements.txt
setup.py
tea.yaml
```

## Entry points

- [yyets/BagAndDrag/bag.py:104](https://github.com/tgbot-collection/YYeTsBot/blob/de73b9c1aa9aad7affdf4228f6d1d0198195921d/yyets/BagAndDrag/bag.py#L104)
- [yyets/BagAndDrag/cfkv.py:84](https://github.com/tgbot-collection/YYeTsBot/blob/de73b9c1aa9aad7affdf4228f6d1d0198195921d/yyets/BagAndDrag/cfkv.py#L84)
- [yyets/BagAndDrag/convert_db.py:98](https://github.com/tgbot-collection/YYeTsBot/blob/de73b9c1aa9aad7affdf4228f6d1d0198195921d/yyets/BagAndDrag/convert_db.py#L98)
- [yyets/BagAndDrag/drag.py:59](https://github.com/tgbot-collection/YYeTsBot/blob/de73b9c1aa9aad7affdf4228f6d1d0198195921d/yyets/BagAndDrag/drag.py#L59)
- [yyets/BagAndDrag/zimuxia/convert_db.py:61](https://github.com/tgbot-collection/YYeTsBot/blob/de73b9c1aa9aad7affdf4228f6d1d0198195921d/yyets/BagAndDrag/zimuxia/convert_db.py#L61)
- [yyets/BagAndDrag/zimuxia/zimuxia.py:55](https://github.com/tgbot-collection/YYeTsBot/blob/de73b9c1aa9aad7affdf4228f6d1d0198195921d/yyets/BagAndDrag/zimuxia/zimuxia.py#L55)
- [yyets/__init__.py:60](https://github.com/tgbot-collection/YYeTsBot/blob/de73b9c1aa9aad7affdf4228f6d1d0198195921d/yyets/__init__.py#L60)
- [yyets/healthcheck/check.py:79](https://github.com/tgbot-collection/YYeTsBot/blob/de73b9c1aa9aad7affdf4228f6d1d0198195921d/yyets/healthcheck/check.py#L79)
- [yyetsbot/fansub.py:448](https://github.com/tgbot-collection/YYeTsBot/blob/de73b9c1aa9aad7affdf4228f6d1d0198195921d/yyetsbot/fansub.py#L448)
- [yyetsbot/yyetsbot.py:407](https://github.com/tgbot-collection/YYeTsBot/blob/de73b9c1aa9aad7affdf4228f6d1d0198195921d/yyetsbot/yyetsbot.py#L407)
- [yyetsweb/cmd/add_dl.py:101](https://github.com/tgbot-collection/YYeTsBot/blob/de73b9c1aa9aad7affdf4228f6d1d0198195921d/yyetsweb/cmd/add_dl.py#L101)
- [yyetsweb/common/comments_check.py:199](https://github.com/tgbot-collection/YYeTsBot/blob/de73b9c1aa9aad7affdf4228f6d1d0198195921d/yyetsweb/common/comments_check.py#L199)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 9 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: AdsenseStatusHandler, AnnouncementHandler, BaseHandler, BlacklistHandler, CaptchaHandler, CategoryHandle… |
| Configuration and deployment | config | Observed | Groups 17 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: UploadCommand. |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Mongo. |
| Application entry point | entrypoint | Observed | Groups 16 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AliyunChecker, BD2020, BaiduChecker, BaseFansub, BaseSync, Cloudflare. Observed top-level… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestIndex, YYeTsTest. |
| yyets package | library | Observed | Groups 6 file(s) under yyets package (observed from repository paths and static analysis). Observed top-level functions: get_value. |
| yyetsbot package | library | Observed | Groups 1 file(s) under yyetsbot package (observed from repository paths and static analysis). Observed top-level functions: get_error_dump, redis_announcement, reset_request, save_error_dump, show_usage, today_request. |
| yyetsweb package | library | Observed | Groups 16 file(s) under yyetsweb package (observed from repository paths and static analysis). Observed top-level classes: Announcement, Blacklist, Captcha, Category, Comment, CommentChild. Observed top-level functions:… |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/docker.yaml` (ci)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `requirements.txt` (manifest)
- `setup.py` (manifest)
- `tea.yaml` (config)
- `yyets/BagAndDrag/sample.json` (config)
- `yyets/management/format.json` (config)
- `yyets/worker/public/css/data.json` (config)
- `yyets/worker/public/css/index.json` (config)
- `yyets/worker/workers-site/package.json` (manifest)
- `yyets/worker/wrangler.toml` (config)
- `yyetsweb/YYeTs-grafana.json` (config)
- `yyetsweb/go.mod` (manifest)
- `yyetsweb/templates/css/data.json` (config)
- `yyetsweb/templates/css/index.json` (config)
- `yyetsweb/templates/js/sample.json` (config)

## Top-level layout

- `yyetsweb` — 56 analysed file(s)
- `yyets` — 35 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `yyetsbot` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `conf` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (5 x generated/minified file excluded; 1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `de73b9c1aa9aad7affdf4228f6d1d0198195921d` is the revision these paths and observations refer to.
