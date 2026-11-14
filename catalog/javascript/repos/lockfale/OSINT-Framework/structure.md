# Project structure: lockfale/OSINT-Framework

**Analysed commit:** `08720d5b594cb7513d7ec81f8e70c400375a85fc`

**Commit reference:** [08720d5b594cb7513d7ec81f8e70c400375a85fc](https://github.com/lockfale/OSINT-Framework/commit/08720d5b594cb7513d7ec81f8e70c400375a85fc)

**Tree at this commit:** [lockfale/OSINT-Framework@08720d5b594c](https://github.com/lockfale/OSINT-Framework/tree/08720d5b594cb7513d7ec81f8e70c400375a85fc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lockfale/OSINT-Framework |
| Description | OSINT Framework |
| Stars | 12453 |
| Forks | 2100 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `08720d5b594cb7513d7ec81f8e70c400375a85fc` |
| Retrieved at | 2026-11-14T19:12:05.688895+00:00 |
| Files in this snapshot | 19 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
public/  (4 files)
  css/  (2 files)
    arf.css
    panel.css
  js/  (1 files)
    arf.js
  index.html
src/  (1 files)
  worker.js
tools/  (5 files)
  link-recheck/  (2 files)
    package.json
    recheck.mjs
  extract_urls.py
  link_checker.py
  remove_dead_links.py
.gitignore
LICENSE
README.md
THE-127-domain-enrichment-batch1.md
enrichment-batch4-domains.json
merge_enrichments.py
package.json
wrangler.jsonc
```

## Entry points

- [merge_enrichments.py:40](https://github.com/lockfale/OSINT-Framework/blob/08720d5b594cb7513d7ec81f8e70c400375a85fc/merge_enrichments.py#L40)
- [tools/extract_urls.py:57](https://github.com/lockfale/OSINT-Framework/blob/08720d5b594cb7513d7ec81f8e70c400375a85fc/tools/extract_urls.py#L57)
- [tools/link_checker.py:176](https://github.com/lockfale/OSINT-Framework/blob/08720d5b594cb7513d7ec81f8e70c400375a85fc/tools/link_checker.py#L176)
- [tools/remove_dead_links.py:88](https://github.com/lockfale/OSINT-Framework/blob/08720d5b594cb7513d7ec81f8e70c400375a85fc/tools/remove_dead_links.py#L88)
- [public/index.html](https://github.com/lockfale/OSINT-Framework/blob/08720d5b594cb7513d7ec81f8e70c400375a85fc/public/index.html)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 4 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: LinkResult. Observed top-level functions: check_url, extract_urls, get_dead_urls, is_templ… |
| public package | library | Observed | Groups 1 file(s) under public package (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 1 file(s) under tools package (observed from repository paths and static analysis). |
| worker.js package | library | Observed | Groups 1 file(s) under worker.js package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/ci.yml` (ci)
- `enrichment-batch4-domains.json` (config)
- `package.json` (manifest)
- `tools/link-recheck/package.json` (manifest)

## Top-level layout

- `(root files)` — 8 analysed file(s)
- `tools` — 5 analysed file(s)
- `public` — 4 analysed file(s)
- `.github` — 1 analysed file(s)
- `src` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `08720d5b594cb7513d7ec81f8e70c400375a85fc` is the revision these paths and observations refer to.
