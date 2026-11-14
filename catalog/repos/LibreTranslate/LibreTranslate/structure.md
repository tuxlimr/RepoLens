# Project structure: LibreTranslate/LibreTranslate

**Analysed commit:** `84cd56c061a7ba3955b49efdaee2ac54dcbca07f`

**Commit reference:** [84cd56c061a7ba3955b49efdaee2ac54dcbca07f](https://github.com/LibreTranslate/LibreTranslate/commit/84cd56c061a7ba3955b49efdaee2ac54dcbca07f)

**Tree at this commit:** [LibreTranslate/LibreTranslate@84cd56c061a7](https://github.com/LibreTranslate/LibreTranslate/tree/84cd56c061a7ba3955b49efdaee2ac54dcbca07f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | LibreTranslate/LibreTranslate |
| Description | Free and Open Source Machine Translation API. Self-hosted, offline capable and easy to setup. |
| Stars | 17706 |
| Forks | 1855 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `84cd56c061a7ba3955b49efdaee2ac54dcbca07f` |
| Retrieved at | 2026-11-14T19:08:30.410020+00:00 |
| Files in this snapshot | 207 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (4 files)
    issue-triage.yml
    publish-docker.yml
    publish-package.yml
    run-tests.yml
  FUNDING.yml
  issue-template.md
.well-known/  (1 files)
  funding-manifest-urls
db/  (1 files)
  .gitignore
docker/  (5 files)
  Dockerfile
  arm.Dockerfile
  cuda.Dockerfile
  root-with-sshd.Dockerfile
  user-with-api-key.Dockerfile
libretranslate/  (165 files)
  locales/  (130 files)
    ar/  (2 files)
      … 2 files under this directory
    az/  (2 files)
      … 2 files under this directory
    be/  (2 files)
      … 2 files under this directory
    bg/  (2 files)
      … 2 files under this directory
    bn/  (2 files)
      … 2 files under this directory
    ca/  (2 files)
      … 2 files under this directory
    ckb/  (1 files)
      … 1 files under this directory
    cs/  (2 files)
      … 2 files under this directory
    cv/  (1 files)
      … 1 files under this directory
    da/  (2 files)
      … 2 files under this directory
    de/  (2 files)
      … 2 files under this directory
    el/  (2 files)
      … 2 files under this directory
    eo/  (2 files)
      … 2 files under this directory
    es/  (2 files)
      … 2 files under this directory
    et/  (2 files)
      … 2 files under this directory
    eu/  (2 files)
      … 2 files under this directory
    ext/  (2 files)
      … 2 files under this directory
    fa/  (2 files)
      … 2 files under this directory
    fi/  (2 files)
      … 2 files under this directory
    fil/  (2 files)
      … 2 files under this directory
    fr/  (2 files)
      … 2 files under this directory
    ga/  (2 files)
      … 2 files under this directory
    gd/  (2 files)
      … 2 files under this directory
    gl/  (2 files)
      … 2 files under this directory
    got/  (1 files)
      … 1 files under this directory
    he/  (2 files)
      … 2 files under this directory
    hi/  (2 files)
      … 2 files under this directory
    hu/  (2 files)
      … 2 files under this directory
    ia/  (1 files)
      … 1 files under this directory
    id/  (2 files)
      … 2 files under this directory
    it/  (2 files)
      … 2 files under this directory
    ja/  (2 files)
      … 2 files under this directory
    ka/  (1 files)
      … 1 files under this directory
    kab/  (2 files)
      … 2 files under this directory
    kk/  (2 files)
      … 2 files under this directory
    ko/  (2 files)
      … 2 files under this directory
    lt/  (2 files)
      … 2 files under this directory
    lv/  (2 files)
      … 2 files under this directory
    mia/  (2 files)
      … 2 files under this directory
    ms/  (2 files)
      … 2 files under this directory
    nb/  (2 files)
      … 2 files under this directory
    nl/  (2 files)
      … 2 files under this directory
    nn/  (2 files)
      … 2 files under this directory
    oc/  (2 files)
      … 2 files under this directory
    pa/  (2 files)
      … 2 files under this directory
    pl/  (2 files)
      … 2 files under this directory
    pt/  (2 files)
      … 2 files under this directory
    pt_BR/  (2 files)
      … 2 files under this directory
    ro/  (2 files)
      … 2 files under this directory
    ru/  (2 files)
      … 2 files under this directory
    si/  (2 files)
      … 2 files under this directory
    sk/  (2 files)
      … 2 files under this directory
    sl/  (2 files)
      … 2 files under this directory
    sq/  (2 files)
      … 2 files under this directory
    sr/  (2 files)
      … 2 files under this directory
    sv/  (2 files)
      … 2 files under this directory
    ta/  (1 files)
      … 1 files under this directory
    th/  (2 files)
      … 2 files under this directory
    tl/  (2 files)
      … 2 files under this directory
    tr/  (2 files)
      … 2 files under this directory
    ug/  (2 files)
      … 2 files under this directory
    uk/  (2 files)
      … 2 files under this directory
    ur/  (2 files)
      … 2 files under this directory
    vi/  (2 files)
      … 2 files under this directory
    zgh/  (2 files)
      … 2 files under this directory
    zh/  (2 files)
      … 2 files under this directory
    zh_Hant/  (2 files)
      … 2 files under this directory
    .gitignore
    messages.pot
  static/  (4 files)
    css/  (2 files)
      … 2 files under this directory
    js/  (1 files)
      … 1 files under this directory
    icon.svg
  templates/  (2 files)
    app.js.template
    index.html
  tests/  (10 files)
    test_api/  (8 files)
      … 8 files under this directory
    __init__.py
    test_init.py
  __init__.py
  api_keys.py
  app.py
  cache.py
  default_values.py
  detect.py
  flood.py
  init.py
  language.py
  locales.py
  main.py
  manage.py
  no_limiter.py
  remove_translated_files.py
  scheduler.py
  secret.py
  security.py
  storage.py
  suggestions.py
scripts/  (8 files)
  compile_locales.py
  entrypoint.sh
  gunicorn_conf.py
  healthcheck.py
  install_models.py
  print_args_env.py
  suggestions-to-jsonl.py
  update_locales.py
.dockerignore
.editorconfig
.gitattributes
.gitignore
.pre-commit-config.yaml
AGENTS.md
CONTRIBUTING.md
LICENSE
README.md
TRADEMARK.md
VERSION
babel.cfg
docker-compose.cuda.yml
docker-compose.yml
k8s.yaml
main.py
manage.py
pyproject.toml
run.bat
run.sh
wsgi.py
```

## Entry points

- [libretranslate/app.py:1311](https://github.com/LibreTranslate/LibreTranslate/blob/84cd56c061a7ba3955b49efdaee2ac54dcbca07f/libretranslate/app.py#L1311)
- [libretranslate/main.py](https://github.com/LibreTranslate/LibreTranslate/blob/84cd56c061a7ba3955b49efdaee2ac54dcbca07f/libretranslate/main.py)
- [libretranslate/manage.py](https://github.com/LibreTranslate/LibreTranslate/blob/84cd56c061a7ba3955b49efdaee2ac54dcbca07f/libretranslate/manage.py)
- [main.py:3](https://github.com/LibreTranslate/LibreTranslate/blob/84cd56c061a7ba3955b49efdaee2ac54dcbca07f/main.py#L3)
- [manage.py:3](https://github.com/LibreTranslate/LibreTranslate/blob/84cd56c061a7ba3955b49efdaee2ac54dcbca07f/manage.py#L3)
- [scripts/compile_locales.py:8](https://github.com/LibreTranslate/LibreTranslate/blob/84cd56c061a7ba3955b49efdaee2ac54dcbca07f/scripts/compile_locales.py#L8)
- [scripts/install_models.py:10](https://github.com/LibreTranslate/LibreTranslate/blob/84cd56c061a7ba3955b49efdaee2ac54dcbca07f/scripts/install_models.py#L10)
- [scripts/suggestions-to-jsonl.py:7](https://github.com/LibreTranslate/LibreTranslate/blob/84cd56c061a7ba3955b49efdaee2ac54dcbca07f/scripts/suggestions-to-jsonl.py#L7)
- [scripts/update_locales.py:20](https://github.com/LibreTranslate/LibreTranslate/blob/84cd56c061a7ba3955b49efdaee2ac54dcbca07f/scripts/update_locales.py#L20)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 67 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 10 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed top-level functions: app, create_app, detect_translatable, fi… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| libretranslate package | library | Observed | Groups 17 file(s) under libretranslate package (observed from repository paths and static analysis). Observed top-level classes: Database, Detector, Language, Limiter, MemoryStorage, RedisStorage. Observed top-level fun… |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: child_exit, on_starting. |
| Tests | test | Observed | Groups 10 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: app, client, test_api_detect_language, test_api_detect_language_must_fail_bad_request_type, test_api_dete… |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/issue-triage.yml` (ci)
- `.github/workflows/publish-docker.yml` (ci)
- `.github/workflows/publish-package.yml` (ci)
- `.github/workflows/run-tests.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `babel.cfg` (config)
- `docker-compose.cuda.yml` (config)
- `docker-compose.yml` (container)
- `docker/Dockerfile` (container)
- `k8s.yaml` (config)
- `libretranslate/locales/ar/meta.json` (config)
- `libretranslate/locales/az/meta.json` (config)
- `libretranslate/locales/be/meta.json` (config)
- `libretranslate/locales/bg/meta.json` (config)
- `libretranslate/locales/bn/meta.json` (config)
- `libretranslate/locales/ca/meta.json` (config)
- `libretranslate/locales/cs/meta.json` (config)
- `libretranslate/locales/da/meta.json` (config)
- `libretranslate/locales/de/meta.json` (config)
- `libretranslate/locales/el/meta.json` (config)
- `libretranslate/locales/eo/meta.json` (config)
- `libretranslate/locales/es/meta.json` (config)
- `libretranslate/locales/et/meta.json` (config)
- `libretranslate/locales/eu/meta.json` (config)
- `libretranslate/locales/ext/meta.json` (config)
- `libretranslate/locales/fa/meta.json` (config)
- `libretranslate/locales/fi/meta.json` (config)
- `libretranslate/locales/fil/meta.json` (config)
- `libretranslate/locales/fr/meta.json` (config)
- `libretranslate/locales/ga/meta.json` (config)
- `libretranslate/locales/gd/meta.json` (config)
- `libretranslate/locales/gl/meta.json` (config)
- `libretranslate/locales/he/meta.json` (config)
- `libretranslate/locales/hi/meta.json` (config)
- `libretranslate/locales/hu/meta.json` (config)
- `libretranslate/locales/id/meta.json` (config)
- `libretranslate/locales/it/meta.json` (config)
- `libretranslate/locales/ja/meta.json` (config)
- `libretranslate/locales/kab/meta.json` (config)
- `libretranslate/locales/kk/meta.json` (config)
- `libretranslate/locales/ko/meta.json` (config)
- `libretranslate/locales/lt/meta.json` (config)
- `libretranslate/locales/lv/meta.json` (config)
- `libretranslate/locales/mia/meta.json` (config)
- `libretranslate/locales/ms/meta.json` (config)
- `libretranslate/locales/nb/meta.json` (config)
- `libretranslate/locales/nl/meta.json` (config)
- `libretranslate/locales/nn/meta.json` (config)
- `libretranslate/locales/oc/meta.json` (config)
- `libretranslate/locales/pa/meta.json` (config)
- `libretranslate/locales/pl/meta.json` (config)
- `libretranslate/locales/pt/meta.json` (config)
- `libretranslate/locales/pt_BR/meta.json` (config)
- `libretranslate/locales/ro/meta.json` (config)
- `libretranslate/locales/ru/meta.json` (config)
- `libretranslate/locales/si/meta.json` (config)
- `libretranslate/locales/sk/meta.json` (config)
- `libretranslate/locales/sl/meta.json` (config)
- `libretranslate/locales/sq/meta.json` (config)
- `libretranslate/locales/sr/meta.json` (config)
- `libretranslate/locales/sv/meta.json` (config)
- `libretranslate/locales/th/meta.json` (config)
- `libretranslate/locales/tl/meta.json` (config)
- `libretranslate/locales/tr/meta.json` (config)
- `libretranslate/locales/ug/meta.json` (config)
- `libretranslate/locales/uk/meta.json` (config)
- `libretranslate/locales/ur/meta.json` (config)
- `libretranslate/locales/vi/meta.json` (config)
- `libretranslate/locales/zgh/meta.json` (config)
- `libretranslate/locales/zh/meta.json` (config)
- `libretranslate/locales/zh_Hant/meta.json` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `libretranslate` — 165 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `scripts` — 8 analysed file(s)
- `.github` — 6 analysed file(s)
- `docker` — 5 analysed file(s)
- `.well-known` — 1 analysed file(s)
- `db` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x generated/minified file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `84cd56c061a7ba3955b49efdaee2ac54dcbca07f` is the revision these paths and observations refer to.
