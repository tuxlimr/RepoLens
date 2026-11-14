# Project structure: mouredev/python-web

**Analysed commit:** `f732469c2d3e0fae80ce893417c82220730f5bb0`

**Commit reference:** [f732469c2d3e0fae80ce893417c82220730f5bb0](https://github.com/mouredev/python-web/commit/f732469c2d3e0fae80ce893417c82220730f5bb0)

**Tree at this commit:** [mouredev/python-web@f732469c2d3e](https://github.com/mouredev/python-web/tree/f732469c2d3e0fae80ce893417c82220730f5bb0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mouredev/python-web |
| Description | Curso para aprender desarrollo frontend Web con Python puro desde cero. Elaborado durante las emisiones en directo desde Twitch de MoureDev. |
| Stars | 4809 |
| Forks | 249 |
| Licence | Apache-2.0 |
| Language | HTML |
| Default branch | main |
| Analysed commit | `f732469c2d3e0fae80ce893417c82220730f5bb0` |
| Retrieved at | 2026-11-14T19:14:35.869943+00:00 |
| Files in this snapshot | 129 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    static_build.yml
link_bio/  (126 files)
  assets/  (32 files)
    css/  (1 files)
      … 1 files under this directory
    icons/  (27 files)
      … 27 files under this directory
    js/  (1 files)
      … 1 files under this directory
    logo.svg
    logo_symbol.svg
    raiola_networks.svg
  link_bio/  (33 files)
    api/  (4 files)
      … 4 files under this directory
    components/  (10 files)
      … 10 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    model/  (2 files)
      … 2 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    state/  (1 files)
      … 1 files under this directory
    styles/  (3 files)
      … 3 files under this directory
    views/  (4 files)
      … 4 files under this directory
    __init__.py
    conf.py
    constants.py
    link_bio.py
    routes.py
    utils.py
  public/  (49 files)
    assets/  (11 files)
      … 11 files under this directory
    css/  (1 files)
      … 1 files under this directory
    cursos/  (1 files)
      … 1 files under this directory
    icons/  (27 files)
      … 27 files under this directory
    js/  (1 files)
      … 1 files under this directory
    404.html
    __spa-fallback.html
    cursos.html
    index.html
    logo.svg
    logo_symbol.svg
    raiola_networks.svg
    sitemap.xml
  reflex.lock/  (2 files)
    bun.lock
    package.json
  .dockerignore
  .gitignore
  AGENTS.md
  CLAUDE.md
  Dockerfile
  README.md
  local_build.sh
  remote_build.sh
  requirements.txt
  rxconfig.py
LICENSE
README.md
```

## Entry points

- [link_bio/link_bio/api/api.py:11](https://github.com/mouredev/python-web/blob/f732469c2d3e0fae80ce893417c82220730f5bb0/link_bio/link_bio/api/api.py#L11)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 7 file(s) under api layer (observed from repository paths and static analysis). Observed top-level classes: ConfigCatAPI, SupabaseAPI, TwitchAPI. Observed top-level functions: courses_links, experience, header, i… |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed routes: GET /repo, GET /live/{user}, GET /featured, GET /sch… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| link_bio package | library | Observed | Groups 41 file(s) under link_bio package (observed from repository paths and static analysis). Observed top-level classes: Color, Featured, Font, FontWeight, Live, PageState. Observed top-level functions: courses, featu… |

## Important files

- `.github/workflows/static_build.yml` (ci)
- `link_bio/.dockerignore` (container)
- `link_bio/Dockerfile` (container)
- `link_bio/reflex.lock/package.json` (manifest)
- `link_bio/requirements.txt` (manifest)

## Top-level layout

- `link_bio` — 126 analysed file(s)
- `(root files)` — 2 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f732469c2d3e0fae80ce893417c82220730f5bb0` is the revision these paths and observations refer to.
