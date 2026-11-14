# Project structure: beetbox/beets

**Analysed commit:** `029ac6f37d0bc5ce478fb95e5b27547f74ac6100`

**Commit reference:** [029ac6f37d0bc5ce478fb95e5b27547f74ac6100](https://github.com/beetbox/beets/commit/029ac6f37d0bc5ce478fb95e5b27547f74ac6100)

**Tree at this commit:** [beetbox/beets@029ac6f37d0b](https://github.com/beetbox/beets/tree/029ac6f37d0bc5ce478fb95e5b27547f74ac6100)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | beetbox/beets |
| Description | music library manager and MusicBrainz tagger |
| Stars | 15940 |
| Forks | 2194 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `029ac6f37d0bc5ce478fb95e5b27547f74ac6100` |
| Retrieved at | 2026-11-14T19:08:57.957064+00:00 |
| Files in this snapshot | 498 |

## Directory tree

```text
.github/  (16 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.md
    config.yml
    feature-request.md
  problem-matchers/  (2 files)
    sphinx-build.json
    sphinx-lint.json
  workflows/  (6 files)
    changelog_reminder.yaml
    ci.yaml
    integration_test.yaml
    label-issues.yaml
    lint.yaml
    make_release.yaml
  CODEOWNERS
  copilot-instructions.md
  labeler.yaml
  pull_request_template.md
  stale.yml
beets/  (74 files)
  autotag/  (5 files)
    __init__.py
    distance.py
    hooks.py
    match.py
    source.py
  dbcore/  (7 files)
    __init__.py
    db.py
    pathutils.py
    query.py
    queryparse.py
    sort.py
    types.py
  importer/  (6 files)
    __init__.py
    actions.py
    session.py
    stages.py
    state.py
    tasks.py
  library/  (7 files)
    __init__.py
    exceptions.py
    fields.py
    library.py
    migrations.py
    models.py
    queries.py
  test/  (4 files)
    __init__.py
    _common.py
    fixtures.py
    helper.py
  ui/  (18 files)
    commands/  (17 files)
      … 17 files under this directory
    __init__.py
  util/  (16 files)
    __init__.py
    artresizer.py
    color.py
    config.py
    deprecation.py
    diff.py
    extension.py
    functemplate.py
    hidden.py
    id_extractors.py
    layout.py
    lyrics.py
    m3u.py
    pathformats.py
    pipeline.py
    units.py
  __init__.py
  __main__.py
  config_default.yaml
  context.py
  events.py
  exceptions.py
  logging.py
  mediafile.py
  metadata_plugins.py
  plugins.py
  py.typed
beetsplug/  (105 files)
  _utils/  (6 files)
    __init__.py
    art.py
    musicbrainz.py
    playcount.py
    requests.py
    vfs.py
  bpd/  (2 files)
    __init__.py
    gstplayer.py
  discogs/  (3 files)
    __init__.py
    states.py
    types.py
  lastgenre/  (6 files)
    __init__.py
    aliases.yaml
    client.py
    genres-tree.yaml
    genres.txt
    utils.py
  metasync/  (3 files)
    __init__.py
    amarok.py
    itunes.py
  tidal/  (4 files)
    __init__.py
    api.py
    api_types.py
    session.py
  web/  (6 files)
    static/  (4 files)
      … 4 files under this directory
    templates/  (1 files)
      … 1 files under this directory
    __init__.py
  _typing.py
  absubmit.py
  acousticbrainz.py
  advancedrewrite.py
  albumtypes.py
  aura.py
  autobpm.py
  badfiles.py
  bareasc.py
  beatport.py
  bench.py
  bpm.py
  bpsync.py
  bucket.py
  chroma.py
  convert.py
  deezer.py
  duplicates.py
  edit.py
  embedart.py
  embyupdate.py
  export.py
  fetchart.py
  filefilter.py
  … 51 more files
docs/  (126 files)
  _static/  (1 files)
    beets.css
  _templates/  (4 files)
    autosummary/  (4 files)
      … 4 files under this directory
  api/  (4 files)
    database.rst
    index.rst
    plugin_utilities.rst
    plugins.rst
  dev/  (17 files)
    plugins/  (12 files)
      … 12 files under this directory
    cli.rst
    importer.rst
    index.rst
    library.rst
    paths.rst
  extensions/  (1 files)
    conf.py
  guides/  (5 files)
    advanced.rst
    index.rst
    installation.rst
    main.rst
    tagger.rst
  plugins/  (80 files)
    absubmit.rst
    acousticbrainz.rst
    advancedrewrite.rst
    albumtypes.rst
    aura.rst
    autobpm.rst
    badfiles.rst
    bareasc.rst
    beatport.rst
    bpd.rst
    bpm.rst
    bpsync.rst
    bucket.rst
    chroma.rst
    convert.rst
    deezer.rst
    discogs.rst
    duplicates.rst
    edit.rst
    embedart.rst
    embyupdate.rst
    export.rst
    fetchart.rst
    filefilter.rst
    … 56 more files
  reference/  (5 files)
    cli.rst
    config.rst
    index.rst
    pathformat.rst
    query.rst
  .gitignore
  Makefile
  code_of_conduct.rst
  conf.py
  contributing.rst
  faq.rst
  index.rst
  modd.conf
  team.rst
extra/  (3 files)
  _beet
  ascii_logo.txt
  release.py
test/  (160 files)
  autotag/  (4 files)
    __init__.py
    test_distance.py
    test_hooks.py
    test_match.py
  dbcore/  (7 files)
    __init__.py
    test_datequery.py
    test_db.py
    test_query.py
    test_queryparse.py
    test_sort.py
    test_types.py
  extra/  (2 files)
    __init__.py
    test_release.py
  library/  (2 files)
    __init__.py
    test_migrations.py
  plugins/  (81 files)
    factories/  (3 files)
      … 3 files under this directory
    utils/  (5 files)
      … 5 files under this directory
    __init__.py
    conftest.py
    lyrics_pages.py
    test_acousticbrainz.py
    test_advancedrewrite.py
    test_albumtypes.py
    test_art.py
    test_aura.py
    test_autobpm.py
    test_badfiles.py
    test_bareasc.py
    test_beatport.py
    test_bpd.py
    test_bucket.py
    test_chroma.py
    test_convert.py
    test_deezer.py
    test_discogs.py
    test_duplicates.py
    test_edit.py
    test_embedart.py
    test_embyupdate.py
    test_export.py
    test_fetchart.py
    … 49 more files
  rsrc/  (26 files)
    acousticbrainz/  (1 files)
      … 1 files under this directory
    beetsplug/  (1 files)
      … 1 files under this directory
    lyrics/  (6 files)
      … 6 files under this directory
    mbpseudo/  (2 files)
      … 2 files under this directory
    spotify/  (7 files)
      … 7 files under this directory
    convert_stub.py
    itunes_library_unix.xml
    itunes_library_windows.xml
    no_ext_not_music
    playlist.m3u
    playlist.m3u8
    playlist_non_ext.m3u
    playlist_windows.m3u8
    test_completion.sh
  ui/  (15 files)
    commands/  (11 files)
      … 11 files under this directory
    __init__.py
    test_ui.py
    test_ui_importer.py
    test_ui_init.py
  util/  (14 files)
    test_art_resize.py
    test_color.py
    test_config.py
    test_diff.py
    test_extension.py
    test_functemplate.py
    test_hidden.py
    test_id_extractors.py
    test_layout.py
    test_lyrics.py
    test_m3ufile.py
    test_pathformats.py
    test_pipeline.py
    test_units.py
  __init__.py
  conftest.py
  test_files.py
  test_importer.py
  test_library.py
  test_logging.py
  test_metadata_plugins.py
  test_plugins.py
  test_util.py
.git-blame-ignore-revs
.gitignore
.pre-commit-config.yaml
.readthedocs.yaml
AI_POLICY.md
CODE_OF_CONDUCT.rst
CONTRIBUTING.rst
LICENSE
README.rst
README_kr.rst
SECURITY.md
codecov.yml
pyproject.toml
setup.cfg
```

## Entry points

- [beets/__main__.py:9](https://github.com/beetbox/beets/blob/029ac6f37d0bc5ce478fb95e5b27547f74ac6100/beets/__main__.py#L9)
- [beets/ui/__init__.py](https://github.com/beetbox/beets/blob/029ac6f37d0bc5ce478fb95e5b27547f74ac6100/beets/ui/__init__.py)
- [beets/util/functemplate.py:601](https://github.com/beetbox/beets/blob/029ac6f37d0bc5ce478fb95e5b27547f74ac6100/beets/util/functemplate.py#L601)
- [beetsplug/aura.py:879](https://github.com/beetbox/beets/blob/029ac6f37d0bc5ce478fb95e5b27547f74ac6100/beetsplug/aura.py#L879)
- [beetsplug/bpd/__init__.py:1026](https://github.com/beetbox/beets/blob/029ac6f37d0bc5ce478fb95e5b27547f74ac6100/beetsplug/bpd/__init__.py#L1026)
- [beetsplug/bpd/gstplayer.py:304](https://github.com/beetbox/beets/blob/029ac6f37d0bc5ce478fb95e5b27547f74ac6100/beetsplug/bpd/gstplayer.py#L304)
- [beetsplug/web/__init__.py:292](https://github.com/beetbox/beets/blob/029ac6f37d0bc5ce478fb95e5b27547f74ac6100/beetsplug/web/__init__.py#L292)
- [extra/release.py:263](https://github.com/beetbox/beets/blob/029ac6f37d0bc5ce478fb95e5b27547f74ac6100/extra/release.py#L263)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| beets package | library | Observed | Groups 62 file(s) under beets package (observed from repository paths and static analysis). Observed top-level classes: Action, AfterConvertEventArgs, AfterWriteEventArgs, AlbumChange, AlbumEventArgs, AlbumImportedEvent… |
| beetsplug package | library | Observed | Groups 94 file(s) under beetsplug package (observed from repository paths and static analysis). Observed top-level classes: ABSubmitCLIOpts, ABSubmitError, APIError, AcousticBrainzCLIOpts, AcousticBrainzSubmitPlugin, Ac… |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: ConfigCLIOpts, UnknownPairError. Observed top-level functions: config_edit, config_fu… |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Album, DBAccessError, DBCustomFunctionError, Database, DefaultTemplateFunctions, FormattedItemMapping.… |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Command, Flask. Observed routes: ROUTE /server, ROUTE /tracks, ROUTE /tracks/<… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: LastFmClient. |
| Tests | test | Observed | Groups 164 file(s) under tests (observed from repository paths and static analysis). Observed application object created via Command. Observed routes: PATCH pathlib.Path.samefile, PATCH beetsplug.bpd.asyncio.start_serve… |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/labeler.yaml` (config)
- `.github/problem-matchers/sphinx-build.json` (config)
- `.github/problem-matchers/sphinx-lint.json` (config)
- `.github/stale.yml` (config)
- `.github/workflows/changelog_reminder.yaml` (ci)
- `.github/workflows/ci.yaml` (ci)
- `.github/workflows/integration_test.yaml` (ci)
- `.github/workflows/label-issues.yaml` (ci)
- `.github/workflows/lint.yaml` (ci)
- `.github/workflows/make_release.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `beets/config_default.yaml` (config)
- `beetsplug/lastgenre/aliases.yaml` (config)
- `beetsplug/lastgenre/genres-tree.yaml` (config)
- `codecov.yml` (config)
- `pyproject.toml` (manifest)
- `setup.cfg` (manifest)

## Top-level layout

- `test` — 160 analysed file(s)
- `docs` — 126 analysed file(s)
- `beetsplug` — 105 analysed file(s)
- `beets` — 74 analysed file(s)
- `.github` — 16 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `extra` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `029ac6f37d0bc5ce478fb95e5b27547f74ac6100` is the revision these paths and observations refer to.
