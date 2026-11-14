# Project structure: guofei9987/blind_watermark

**Analysed commit:** `322c90dc02d45644692095b34d3a6b735b6edbd8`

**Commit reference:** [322c90dc02d45644692095b34d3a6b735b6edbd8](https://github.com/guofei9987/blind_watermark/commit/322c90dc02d45644692095b34d3a6b735b6edbd8)

**Tree at this commit:** [guofei9987/blind_watermark@322c90dc02d4](https://github.com/guofei9987/blind_watermark/tree/322c90dc02d45644692095b34d3a6b735b6edbd8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | guofei9987/blind_watermark |
| Description | Blind&Invisible Watermark ，图片盲水印，提取水印无须原图！ |
| Stars | 14850 |
| Forks | 1449 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `322c90dc02d45644692095b34d3a6b735b6edbd8` |
| Retrieved at | 2026-11-14T19:09:12.212376+00:00 |
| Files in this snapshot | 38 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (1 files)
    tests.yml
  FUNDING.yml
blind_watermark/  (9 files)
  __init__.py
  att.py
  blind_watermark.py
  bwm_core.py
  cli_tools.py
  pool.py
  recover.py
  requirements.txt
  version.py
docs/  (15 files)
  en/  (3 files)
    README.md
    _coverpage.md
    _sidebar.md
  zh/  (3 files)
    README.md
    _coverpage.md
    _sidebar.md
  .nojekyll
  README.md
  _coverpage.md
  _navbar.md
  _sidebar.md
  index.html
  make_doc.py
  run_server.bat
  vue.css
examples/  (6 files)
  output/  (1 files)
    .keep
  example_bit.py
  example_img.py
  example_no_writing.py
  example_str.py
  example_str_multi.py
.travis.yml
LICENSE
README.md
README_cn.md
requirements.txt
setup.py
```

## Entry points

- [blind_watermark/cli_tools.py](https://github.com/guofei9987/blind_watermark/blob/322c90dc02d45644692095b34d3a6b735b6edbd8/blind_watermark/cli_tools.py)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| blind_watermark package | library | Observed | Groups 8 file(s) under blind_watermark package (observed from repository paths and static analysis). Observed top-level classes: AutoPool, CommonPool, MyValues, Notes, WaterMark, WaterMarkCore. Observed top-level functi… |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: read_file, read_requirements. |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/tests.yml` (ci)
- `.travis.yml` (ci)
- `blind_watermark/requirements.txt` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `docs` — 15 analysed file(s)
- `blind_watermark` — 9 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `examples` — 6 analysed file(s)
- `.github` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `322c90dc02d45644692095b34d3a6b735b6edbd8` is the revision these paths and observations refer to.
