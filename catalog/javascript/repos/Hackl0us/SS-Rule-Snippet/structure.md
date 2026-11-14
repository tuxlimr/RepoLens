# Project structure: Hackl0us/SS-Rule-Snippet

**Analysed commit:** `6fb5c342fbe3c63a3baa4f0e8bb32046631809f6`

**Commit reference:** [6fb5c342fbe3c63a3baa4f0e8bb32046631809f6](https://github.com/Hackl0us/SS-Rule-Snippet/commit/6fb5c342fbe3c63a3baa4f0e8bb32046631809f6)

**Tree at this commit:** [Hackl0us/SS-Rule-Snippet@6fb5c342fbe3](https://github.com/Hackl0us/SS-Rule-Snippet/tree/6fb5c342fbe3c63a3baa4f0e8bb32046631809f6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Hackl0us/SS-Rule-Snippet |
| Description | 搜集、整理、维护 Surge / Quantumult (X) / Shadowrocket / Surfboard / clash (Premium) 实用规则。 |
| Stars | 11197 |
| Forks | 1757 |
| Licence | AGPL-3.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `6fb5c342fbe3c63a3baa4f0e8bb32046631809f6` |
| Retrieved at | 2026-11-14T19:12:24.626874+00:00 |
| Files in this snapshot | 105 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    purge_cdn_cache.yaml
LAZY_RULES/  (6 files)
  Clash_Premium.yaml
  Quantumult.conf
  QuantumultX.conf
  Shadowrocket.conf
  Surge.conf
  clash.yaml
Module/  (1 files)
  Surge/  (1 files)
    Gboard_zhHans_patch.sgmodule
Rulesets/  (50 files)
  Clash/  (11 files)
    App/  (4 files)
      … 4 files under this directory
    Basic/  (7 files)
      … 7 files under this directory
  Quantumult/  (12 files)
    App/  (4 files)
      … 4 files under this directory
    Basic/  (7 files)
      … 7 files under this directory
    rewrite.list
  Surge/  (27 files)
    App/  (14 files)
      … 14 files under this directory
    Basic/  (6 files)
      … 6 files under this directory
    Custom/  (7 files)
      … 7 files under this directory
Scripts/  (5 files)
  Surge/  (4 files)
    weather_aqi_us/  (4 files)
      … 4 files under this directory
  hackl0us.boxjs.json
归档/  (3 files)
  Surfboard.conf
  Surge 2.conf
  Surge Legacy Global.conf
规则片段集/  (35 files)
  App 规则集/  (15 files)
    工具/  (3 files)
      … 3 files under this directory
    流媒体/  (5 files)
      … 5 files under this directory
    社交分享/  (7 files)
      … 7 files under this directory
  功能性规则集/  (5 files)
    Proxyee Down 代理.txt
    TikTok 解锁.txt
    修复Siri高延迟或不可用.txt
    手机端使用知乎网页版.txt
    维基百科(Wikipedia)排版优化.txt
  基础规则集/  (6 files)
    AppleNews解锁.txt
    Apple服务优化.txt
    国内直连.txt
    国外代理.txt
    常见广告域名.txt
    最终规则.txt
  自选规则集/  (9 files)
    GFW 黑名单/  (2 files)
      … 2 files under this directory
    国内网站广告追踪屏蔽.txt
    学术网站-代理.txt
    学术网站-直连.txt
    屏蔽视频广告.txt
    常见国外网站列表.txt
    广告域名列表.txt
    成人网站.txt
.gitignore
Changelog.md
LICENSE
README.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/purge_cdn_cache.yaml` (ci)
- `LAZY_RULES/Clash_Premium.yaml` (config)
- `LAZY_RULES/clash.yaml` (config)
- `Rulesets/Clash/App/social/Telegram.yaml` (config)
- `Rulesets/Clash/App/social/WhatsApp.yaml` (config)
- `Rulesets/Clash/App/stream/DisneyPlus.yaml` (config)
- `Rulesets/Clash/App/stream/Netflix.yaml` (config)
- `Rulesets/Clash/Basic/Apple-News.yaml` (config)
- `Rulesets/Clash/Basic/Apple-direct.yaml` (config)
- `Rulesets/Clash/Basic/Apple-proxy.yaml` (config)
- `Rulesets/Clash/Basic/CN.yaml` (config)
- `Rulesets/Clash/Basic/LAN.yaml` (config)
- `Rulesets/Clash/Basic/common-ad-keyword.yaml` (config)
- `Rulesets/Clash/Basic/foreign.yaml` (config)
- `Scripts/hackl0us.boxjs.json` (config)

## Top-level layout

- `Rulesets` — 50 analysed file(s)
- `规则片段集` — 35 analysed file(s)
- `LAZY_RULES` — 6 analysed file(s)
- `Scripts` — 5 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `归档` — 3 analysed file(s)
- `.github` — 1 analysed file(s)
- `Module` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6fb5c342fbe3c63a3baa4f0e8bb32046631809f6` is the revision these paths and observations refer to.
