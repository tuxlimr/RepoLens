# Project structure: pwxcoo/chinese-xinhua

**Analysed commit:** `fe6d6c2e8baa82187f4c96bbe042e43f96c05666`

**Commit reference:** [fe6d6c2e8baa82187f4c96bbe042e43f96c05666](https://github.com/pwxcoo/chinese-xinhua/commit/fe6d6c2e8baa82187f4c96bbe042e43f96c05666)

**Tree at this commit:** [pwxcoo/chinese-xinhua@fe6d6c2e8baa](https://github.com/pwxcoo/chinese-xinhua/tree/fe6d6c2e8baa82187f4c96bbe042e43f96c05666)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pwxcoo/chinese-xinhua |
| Description | :orange_book: 中华新华字典数据库。包括歇后语，成语，词语，汉字。 |
| Stars | 11770 |
| Forks | 2718 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `fe6d6c2e8baa82187f4c96bbe042e43f96c05666` |
| Retrieved at | 2026-11-14T19:10:29.092343+00:00 |
| Files in this snapshot | 10 |

## Directory tree

```text
scripts/  (7 files)
  README.md
  addAbbreviation.py
  chengyu.py
  ci.py
  clean.ipynb
  word.py
  xiehouyu.py
.gitignore
LICENSE
README.md
```

## Entry points

- [scripts/chengyu.py:48](https://github.com/pwxcoo/chinese-xinhua/blob/fe6d6c2e8baa82187f4c96bbe042e43f96c05666/scripts/chengyu.py#L48)
- [scripts/ci.py:59](https://github.com/pwxcoo/chinese-xinhua/blob/fe6d6c2e8baa82187f4c96bbe042e43f96c05666/scripts/ci.py#L59)
- [scripts/word.py:52](https://github.com/pwxcoo/chinese-xinhua/blob/fe6d6c2e8baa82187f4c96bbe042e43f96c05666/scripts/word.py#L52)
- [scripts/xiehouyu.py:30](https://github.com/pwxcoo/chinese-xinhua/blob/fe6d6c2e8baa82187f4c96bbe042e43f96c05666/scripts/xiehouyu.py#L30)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: downloader. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: abbreviation. |

## Important files

No manifest, config, CI, or container files were observed in the analysed set.

## Top-level layout

- `scripts` — 7 analysed file(s)
- `(root files)` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `fe6d6c2e8baa82187f4c96bbe042e43f96c05666` is the revision these paths and observations refer to.
