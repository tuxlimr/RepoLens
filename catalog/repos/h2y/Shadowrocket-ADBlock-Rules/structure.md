# Project structure: h2y/Shadowrocket-ADBlock-Rules

**Analysed commit:** `1b691dc27ac483cfc0574c7559c6f9db9293c6f7`

**Commit reference:** [1b691dc27ac483cfc0574c7559c6f9db9293c6f7](https://github.com/h2y/Shadowrocket-ADBlock-Rules/commit/1b691dc27ac483cfc0574c7559c6f9db9293c6f7)

**Tree at this commit:** [h2y/Shadowrocket-ADBlock-Rules@1b691dc27ac4](https://github.com/h2y/Shadowrocket-ADBlock-Rules/tree/1b691dc27ac483cfc0574c7559c6f9db9293c6f7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | h2y/Shadowrocket-ADBlock-Rules |
| Description | 提供多款 Shadowrocket 规则，带广告过滤功能。用于 iOS 未越狱设备选择性地自动翻墙。 |
| Stars | 16736 |
| Forks | 2333 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `1b691dc27ac483cfc0574c7559c6f9db9293c6f7` |
| Retrieved at | 2026-11-14T19:08:43.859391+00:00 |
| Files in this snapshot | 38 |

## Directory tree

```text
factory/  (29 files)
  resultant/  (4 files)
    gfw.list
    gfw_unhandle.log
    top500_direct.list
    top500_proxy.list
  template/  (13 files)
    sr_adb.txt
    sr_backcn.txt
    sr_backcn_ad.txt
    sr_cnip.txt
    sr_cnip_ad.txt
    sr_direct_banad.txt
    sr_foot.txt
    sr_head.txt
    sr_proxy_banad.txt
    sr_top500_banlist.txt
    sr_top500_banlist_ad.txt
    sr_top500_whitelist.txt
    sr_top500_whitelist_ad.txt
  README.md
  ad.py
  auto_build.sh
  build_confs.py
  chnroutes.py
  gfwlist.py
  index.sh.bat
  manual_direct.txt
  manual_gfwlist.txt
  manual_proxy.txt
  manual_reject.txt
  top500.py
figure/  (1 files)
  免费在线二维码生成器.url
.gitignore
LICENSE
readme.md
requirements.txt
sr_backcn.conf
sr_cnip.conf
sr_top500_banlist.conf
sr_top500_whitelist.conf
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| factory package | library | Observed | Groups 6 file(s) under factory package (observed from repository paths and static analysis). Observed top-level classes: DomainScaner, UrlScaner. Observed top-level functions: clear_format, fetchHTML, filtrate_rules, ge… |

## Important files

- `requirements.txt` (manifest)

## Top-level layout

- `factory` — 29 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `figure` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `1b691dc27ac483cfc0574c7559c6f9db9293c6f7` is the revision these paths and observations refer to.
