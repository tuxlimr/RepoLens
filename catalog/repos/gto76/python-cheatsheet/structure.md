# Project structure: gto76/python-cheatsheet

**Analysed commit:** `f2ace2d90ea2f153d7f47edc368586ce8f15d8d7`

**Commit reference:** [f2ace2d90ea2f153d7f47edc368586ce8f15d8d7](https://github.com/gto76/python-cheatsheet/commit/f2ace2d90ea2f153d7f47edc368586ce8f15d8d7)

**Tree at this commit:** [gto76/python-cheatsheet@f2ace2d90ea2](https://github.com/gto76/python-cheatsheet/tree/f2ace2d90ea2f153d7f47edc368586ce8f15d8d7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gto76/python-cheatsheet |
| Description | Comprehensive Python Cheatsheet |
| Stars | 38927 |
| Forks | 6682 |
| Licence | Not detected |
| Language | Python |
| Default branch | main |
| Analysed commit | `f2ace2d90ea2f153d7f47edc368586ce8f15d8d7` |
| Retrieved at | 2026-11-14T19:06:46.958567+00:00 |
| Files in this snapshot | 37 |

## Directory tree

```text
pdf/  (17 files)
  Acrobat/  (11 files)
    Chapter_1.xml
    bottom_line.xml
    chapter_2.xml
    chapter_3.xml
    chapter_4.xml
    chapter_5.xml
    chapter_6.xml
    chapter_7.xml
    chapter_8.xml
    even_pages.xml
    odd_pages.xml
  README.md
  create_index.py
  index_for_pdf.html
  index_for_pdf_print.html
  popup.html
  remove_links.py
web/  (18 files)
  OnlineWebFonts_COM_cb7eb796ae7de7195a34c485cacebad1/  (3 files)
    @font-face/  (1 files)
      … 1 files under this directory
    License.txt
    Online_Web_Fonts.url
  OnlineWebFonts_COM_d6ba633f6ea4cafe1a39ab736fe55e88/  (3 files)
    Menlo Bold/  (1 files)
      … 1 files under this directory
    License.txt
    Online_Web_Fonts.url
  continents.csv
  convert_table.py
  covid_cases.js
  faq.html
  script_2.js
  style.css
  style_dark.css
  style_dark1.css
  style_dark2.css
  style_dark3.css
  template.html
  update_plots.py
README.md
parse.js
```

## Entry points

- [pdf/create_index.py:50](https://github.com/gto76/python-cheatsheet/blob/f2ace2d90ea2f153d7f47edc368586ce8f15d8d7/pdf/create_index.py#L50)
- [pdf/remove_links.py:68](https://github.com/gto76/python-cheatsheet/blob/f2ace2d90ea2f153d7f47edc368586ce8f15d8d7/pdf/remove_links.py#L68)
- [web/convert_table.py:31](https://github.com/gto76/python-cheatsheet/blob/f2ace2d90ea2f153d7f47edc368586ce8f15d8d7/web/convert_table.py#L31)
- [web/update_plots.py:123](https://github.com/gto76/python-cheatsheet/blob/f2ace2d90ea2f153d7f47edc368586ce8f15d8d7/web/update_plots.py#L123)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: convert_table, main, print_hhh, read_file, update_confirmed_cases, update_covid_deaths. |
| web package | library | Observed | Groups 2 file(s) under web package (observed from repository paths and static analysis). |

## Important files

No manifest, config, CI, or container files were observed in the analysed set.

## Top-level layout

- `web` — 18 analysed file(s)
- `pdf` — 17 analysed file(s)
- `(root files)` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (5 x generated/minified file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f2ace2d90ea2f153d7f47edc368586ce8f15d8d7` is the revision these paths and observations refer to.
