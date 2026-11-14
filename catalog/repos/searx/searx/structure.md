# Project structure: searx/searx

**Analysed commit:** `00abe3df3857f70875543e766223bc7bc0ccce93`

**Commit reference:** [00abe3df3857f70875543e766223bc7bc0ccce93](https://github.com/searx/searx/commit/00abe3df3857f70875543e766223bc7bc0ccce93)

**Tree at this commit:** [searx/searx@00abe3df3857](https://github.com/searx/searx/tree/00abe3df3857f70875543e766223bc7bc0ccce93)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | searx/searx |
| Description | Privacy-respecting metasearch engine |
| Stars | 13566 |
| Forks | 1685 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `00abe3df3857f70875543e766223bc7bc0ccce93` |
| Retrieved at | 2026-11-14T19:09:47.278873+00:00 |
| Files in this snapshot | 567 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (4 files)
    bug-report.md
    config.yml
    engine-request.md
    feature-request.md
  workflows/  (2 files)
    data-update.yml
    integration.yml
  dependabot.yml
dockerfiles/  (2 files)
  docker-entrypoint.sh
  uwsgi.ini
docs/  (62 files)
  _themes/  (2 files)
    searx/  (2 files)
      … 2 files under this directory
  admin/  (22 files)
    engines/  (1 files)
      … 1 files under this directory
    api.rst
    arch_public.dot
    architecture.rst
    buildhosts.rst
    command-engine.rst
    engines.rst
    filtron.rst
    index.rst
    indexer-engines.rst
    installation-apache.rst
    installation-docker.rst
    installation-nginx.rst
    installation-searx.rst
    installation-uwsgi.rst
    installation.rst
    morty.rst
    no-sql-engines.rst
    plugins.rst
    private-engines.rst
    settings.rst
    update-searx.rst
  blog/  (11 files)
    admin.rst
    command-line-engines.rst
    documentation-offline-engines.rst
    index.rst
    intro-offline.rst
    lxcdev-202006.rst
    private-engines.rst
    python3.rst
    search-database-engines.rst
    search-indexer-engines.rst
    sql-engines.rst
  build-templates/  (3 files)
    filtron.rst
    morty.rst
    searx.rst
  dev/  (12 files)
    contribution_guide.rst
    csv_table.txt
    engine_overview.rst
    hello.dot
    index.rst
    makefile.rst
    plugins.rst
    quickstart.rst
    reST.rst
    search_api.rst
    svg_image.svg
    translation.rst
  searx_extra/  (2 files)
    index.rst
    standalone_searx.py.rst
  user/  (3 files)
    index.rst
    own-instance.rst
    search_syntax.rst
  utils/  (5 files)
    filtron.sh.rst
    index.rst
    lxc.sh.rst
    morty.sh.rst
    searx.sh.rst
  conf.py
  index.rst
examples/  (1 files)
  basic_engine.py
searx/  (408 files)
  answerers/  (3 files)
    random/  (1 files)
      … 1 files under this directory
    statistics/  (1 files)
      … 1 files under this directory
    __init__.py
  data/  (4 files)
    __init__.py
    external_urls.json
    useragents.json
    wikidata_units.json
  engines/  (119 files)
    1337x.py
    __init__.py
    ahmia.py
    apkmirror.py
    archlinux.py
    arxiv.py
    bandcamp.py
    base.py
    bing.py
    bing_images.py
    bing_news.py
    bing_videos.py
    btdigg.py
    command.py
    core.py
    currency_convert.py
    dailymotion.py
    deezer.py
    deviantart.py
    dictzone.py
    digbt.py
    digg.py
    doku.py
    duckduckgo.py
    … 95 more files
  metrology/  (2 files)
    __init__.py
    error_recorder.py
  plugins/  (48 files)
    https_rules/  (36 files)
      … 36 files under this directory
    __init__.py
    ahmia_filter.py
    hash_plugin.py
    hostname_replace.py
    https_rewrite.py
    infinite_scroll.py
    oa_doi_rewrite.py
    search_on_category_select.py
    search_operators.py
    self_info.py
    tracker_url_remover.py
    vim_hotkeys.py
  search/  (12 files)
    checker/  (4 files)
      … 4 files under this directory
    processors/  (6 files)
      … 6 files under this directory
    __init__.py
    models.py
  shared/  (4 files)
    __init__.py
    shared_abstract.py
    shared_simple.py
    shared_uwsgi.py
  static/  (94 files)
    plugins/  (6 files)
      … 6 files under this directory
    themes/  (88 files)
      … 88 files under this directory
  templates/  (56 files)
    __common__/  (3 files)
      … 3 files under this directory
    oscar/  (31 files)
      … 31 files under this directory
    simple/  (22 files)
      … 22 files under this directory
  translations/  (46 files)
    ar/  (1 files)
      … 1 files under this directory
    bg/  (1 files)
      … 1 files under this directory
    bo/  (1 files)
      … 1 files under this directory
    ca/  (1 files)
      … 1 files under this directory
    cs/  (1 files)
      … 1 files under this directory
    cy/  (1 files)
      … 1 files under this directory
    da/  (1 files)
      … 1 files under this directory
    de/  (1 files)
      … 1 files under this directory
    el_GR/  (1 files)
      … 1 files under this directory
    en/  (1 files)
      … 1 files under this directory
    eo/  (1 files)
      … 1 files under this directory
    es/  (1 files)
      … 1 files under this directory
    et/  (1 files)
      … 1 files under this directory
    eu/  (1 files)
      … 1 files under this directory
    fa_IR/  (1 files)
      … 1 files under this directory
    fi/  (1 files)
      … 1 files under this directory
    fil/  (1 files)
      … 1 files under this directory
    fr/  (1 files)
      … 1 files under this directory
    gl/  (1 files)
      … 1 files under this directory
    he/  (1 files)
      … 1 files under this directory
    hr/  (1 files)
      … 1 files under this directory
    hu/  (1 files)
      … 1 files under this directory
    ia/  (1 files)
      … 1 files under this directory
    it/  (1 files)
      … 1 files under this directory
    ja/  (1 files)
      … 1 files under this directory
    lt/  (1 files)
      … 1 files under this directory
    nl/  (1 files)
      … 1 files under this directory
    nl_BE/  (1 files)
      … 1 files under this directory
    oc/  (1 files)
      … 1 files under this directory
    pl/  (1 files)
      … 1 files under this directory
    pt/  (1 files)
      … 1 files under this directory
    pt_BR/  (1 files)
      … 1 files under this directory
    ro/  (1 files)
      … 1 files under this directory
    ru/  (1 files)
      … 1 files under this directory
    sk/  (1 files)
      … 1 files under this directory
    sl/  (1 files)
      … 1 files under this directory
    sr/  (1 files)
      … 1 files under this directory
    sv/  (1 files)
      … 1 files under this directory
    ta/  (1 files)
      … 1 files under this directory
    te/  (1 files)
      … 1 files under this directory
    tr/  (1 files)
      … 1 files under this directory
    uk/  (1 files)
      … 1 files under this directory
    vi/  (1 files)
      … 1 files under this directory
    zh_CN/  (1 files)
      … 1 files under this directory
    zh_Hant_TW/  (1 files)
      … 1 files under this directory
    zh_TW/  (1 files)
      … 1 files under this directory
  __init__.py
  autocomplete.py
  exceptions.py
  external_bang.py
  external_urls.py
  languages.py
  poolrequests.py
  preferences.py
  query.py
  raise_for_httperror.py
  results.py
  settings.yml
  settings_loader.py
  settings_robot.yml
  testing.py
  utils.py
  version.py
  webadapter.py
  webapp.py
  webutils.py
searx_extra/  (14 files)
  update/  (11 files)
    __init__.py
    update_ahmia_blacklist.py
    update_currencies.py
    update_engine_descriptions.py
    update_external_bangs.py
    update_firefox_version.py
    update_languages.py
    update_osm_keys_tags.py
    update_pygments.py
    update_translations.sh
    update_wikidata_units.py
  __init__.py
  google_search.py
  standalone_searx.py
tests/  (27 files)
  robot/  (1 files)
    __init__.py
  unit/  (25 files)
    engines/  (2 files)
      … 2 files under this directory
    settings/  (7 files)
      … 7 files under this directory
    __init__.py
    test_answerers.py
    test_engines_init.py
    test_external_bangs.py
    test_plugins.py
    test_poolrequests.py
    test_preferences.py
    test_query.py
    test_results.py
    test_search.py
    test_settings_loader.py
    test_standalone_searx.py
    test_utils.py
    test_webadapter.py
    test_webapp.py
    test_webutils.py
  __init__.py
utils/  (23 files)
  templates/  (13 files)
    etc/  (11 files)
      … 11 files under this directory
    lib/  (2 files)
      … 2 files under this directory
  brand.env
  build_env.py
  filtron.sh
  lib.sh
  lxc-searx.env
  lxc.sh
  makefile.include
  makefile.lxc
  morty.sh
  searx.sh
.codecov.yml
.config.sh
.coveragerc
.dir-locals.el
.dockerignore
.gitattributes
.gitignore
.landscape.yaml
.pylintrc
AUTHORS.rst
CHANGELOG.rst
CONTRIBUTING.md
Dockerfile
LICENSE
Makefile
PULL_REQUEST_TEMPLATE.md
README.rst
babel.cfg
manage
requirements-dev.txt
requirements.txt
setup.py
tox.ini
```

## Entry points

- [searx/search/checker/__main__.py](https://github.com/searx/searx/blob/00abe3df3857f70875543e766223bc7bc0ccce93/searx/search/checker/__main__.py)
- [searx/testing.py:103](https://github.com/searx/searx/blob/00abe3df3857f70875543e766223bc7bc0ccce93/searx/testing.py#L103)
- [searx/webapp.py](https://github.com/searx/searx/blob/00abe3df3857f70875543e766223bc7bc0ccce93/searx/webapp.py)
- [searx_extra/standalone_searx.py:209](https://github.com/searx/searx/blob/00abe3df3857f70875543e766223bc7bc0ccce93/searx_extra/standalone_searx.py#L209)
- [searx_extra/update/update_currencies.py:149](https://github.com/searx/searx/blob/00abe3df3857f70875543e766223bc7bc0ccce93/searx_extra/update/update_currencies.py#L149)
- [searx_extra/update/update_engine_descriptions.py:201](https://github.com/searx/searx/blob/00abe3df3857f70875543e766223bc7bc0ccce93/searx_extra/update/update_engine_descriptions.py#L201)
- [searx_extra/update/update_external_bangs.py:149](https://github.com/searx/searx/blob/00abe3df3857f70875543e766223bc7bc0ccce93/searx_extra/update/update_external_bangs.py#L149)
- [searx_extra/update/update_languages.py:200](https://github.com/searx/searx/blob/00abe3df3857f70875543e766223bc7bc0ccce93/searx_extra/update/update_languages.py#L200)
- [searx_extra/update/update_osm_keys_tags.py:201](https://github.com/searx/searx/blob/00abe3df3857f70875543e766223bc7bc0ccce93/searx_extra/update/update_osm_keys_tags.py#L201)
- [searx_extra/update/update_pygments.py:137](https://github.com/searx/searx/blob/00abe3df3857f70875543e766223bc7bc0ccce93/searx_extra/update/update_pygments.py#L137)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 18 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: EngineRef, SearchQuery. Observed top-level functions: _load, ahmia_blacklist_loader. |
| dockerfiles package | library | Observed | Groups 1 file(s) under dockerfiles package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 10 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /, ROUTE /healthz, ROUTE /search, ROUTE /about,… |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level functions: replace_pua_chars, request, response. |
| searx package | library | Observed | Groups 188 file(s) under searx package (observed from repository paths and static analysis). Observed top-level classes: BangParser, Checker, CheckerTests, EngineProcessor, EnginesSetting, EnumStringSetting. Observed to… |
| searx_extra package | library | Observed | Groups 7 file(s) under searx_extra package (observed from repository paths and static analysis). Observed top-level functions: fetch_ahmia_blacklist, fetch_firefox_last_versions, fetch_firefox_versions, get_ahmia_blackl… |
| Tests | test | Observed | Groups 27 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH searx.poolrequests.get_global_proxies. Observed top-level classes: AnswererTest, HashPluginTest, PluginStoreTest… |
| utils package | library | Observed | Groups 6 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.codecov.yml` (config)
- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/data-update.yml` (ci)
- `.github/workflows/integration.yml` (ci)
- `.landscape.yaml` (config)
- `Dockerfile` (container)
- `babel.cfg` (config)
- `dockerfiles/uwsgi.ini` (config)
- `requirements-dev.txt` (manifest)
- `requirements.txt` (manifest)
- `searx/data/external_urls.json` (config)
- `searx/data/useragents.json` (config)
- `searx/data/wikidata_units.json` (config)
- `searx/settings.yml` (config)
- `searx/settings_robot.yml` (config)
- `searx/static/themes/oscar/package.json` (manifest)
- `searx/static/themes/simple/package.json` (manifest)
- `setup.py` (manifest)
- `tox.ini` (config)
- `utils/templates/etc/filtron/rules.json` (config)
- `utils/templates/etc/searx/use_default_settings.yml` (config)
- `utils/templates/etc/uwsgi/apps-archlinux/searx.ini` (config)
- `utils/templates/etc/uwsgi/apps-available/searx.ini` (config)

## Top-level layout

- `searx` — 408 analysed file(s)
- `docs` — 62 analysed file(s)
- `tests` — 27 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `utils` — 23 analysed file(s)
- `searx_extra` — 14 analysed file(s)
- `.github` — 7 analysed file(s)
- `dockerfiles` — 2 analysed file(s)
- `examples` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 8 file(s) were skipped during inventory (8 x generated/minified file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `00abe3df3857f70875543e766223bc7bc0ccce93` is the revision these paths and observations refer to.
