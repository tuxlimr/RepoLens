# Project structure: selierlin/Share-SSR-V2ray

**Analysed commit:** `ac204b135344b1a2449bacadcd881698f0ac2c93`

**Commit reference:** [ac204b135344b1a2449bacadcd881698f0ac2c93](https://github.com/selierlin/Share-SSR-V2ray/commit/ac204b135344b1a2449bacadcd881698f0ac2c93)

**Tree at this commit:** [selierlin/Share-SSR-V2ray@ac204b135344](https://github.com/selierlin/Share-SSR-V2ray/tree/ac204b135344b1a2449bacadcd881698f0ac2c93)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | selierlin/Share-SSR-V2ray |
| Description | 机场推荐、Clash / V2ray 客户端配置与代理工具指南 |
| Stars | 12718 |
| Forks | 1178 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `ac204b135344b1a2449bacadcd881698f0ac2c93` |
| Retrieved at | 2026-11-14T19:10:02.632082+00:00 |
| Files in this snapshot | 31 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    pages.yml
Clash/  (4 files)
  Clash_Android.md
  Clash_Linux.md
  Clash_Mac.md
  Clash_Windows.md
Other/  (4 files)
  7-1-firefox-setup-guide-cn.md
  7-2-chrome-setup-guide-cn.md
  8-proxifier-settings.md
  9-dns-setup-guide-cn.md
SS/  (5 files)
  2-windows-setup-guide-cn.md
  3-macos-setup-guide-cn.md
  4-ios-setup-guide-cn.md
  5-android-setup-guide-cn.md
  6-linux-setup-guide-cn.md
SSR/  (6 files)
  11-windows-setup-guide-cn.md
  12-macos-setup-guide-cn.md
  13-ios-setup-guide-cn.md
  14-android-setup-guide-cn.md
  15-linux-setup-guide-cn.md
  README.md
V2ray/  (2 files)
  V2rayN_Windows.md
  V2ray_Android.md
files/  (2 files)
  config/  (2 files)
    OmegaOptions-1080.bak
    OmegaOptions-1086.bak
scripts/  (1 files)
  build_site.py
site/  (1 files)
  style.css
.gitignore
1-share-ssr-v2ray.md
LICENSE
README.md
tools.md
```

## Entry points

- [scripts/build_site.py:448](https://github.com/selierlin/Share-SSR-V2ray/blob/ac204b135344b1a2449bacadcd881698f0ac2c93/scripts/build_site.py#L448)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Guide, Service. Observed top-level functions: build_guides, clean_cell, copy_guide_assets,… |

## Important files

- `.github/workflows/pages.yml` (ci)

## Top-level layout

- `SSR` — 6 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `SS` — 5 analysed file(s)
- `Clash` — 4 analysed file(s)
- `Other` — 4 analysed file(s)
- `V2ray` — 2 analysed file(s)
- `files` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)
- `site` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ac204b135344b1a2449bacadcd881698f0ac2c93` is the revision these paths and observations refer to.
