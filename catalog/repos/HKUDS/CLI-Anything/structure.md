# Project structure: HKUDS/CLI-Anything

**Analysed commit:** `34f519533bc175d2fe287ab8316b0dd99bb9cc43`

**Commit reference:** [34f519533bc175d2fe287ab8316b0dd99bb9cc43](https://github.com/HKUDS/CLI-Anything/commit/34f519533bc175d2fe287ab8316b0dd99bb9cc43)

**Tree at this commit:** [HKUDS/CLI-Anything@34f519533bc1](https://github.com/HKUDS/CLI-Anything/tree/34f519533bc175d2fe287ab8316b0dd99bb9cc43)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | HKUDS/CLI-Anything |
| Description | "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/ |
| Stars | 58733 |
| Forks | 5289 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `34f519533bc175d2fe287ab8316b0dd99bb9cc43` |
| Retrieved at | 2026-11-14T19:06:27.302302+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.claude-plugin/  (1 files)
  marketplace.json
.cursor-plugin/  (1 files)
  marketplace.json
.github/  (23 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.yml
    cli-wishlist.yml
    config.yml
    contributor-signup.yml
    feature_request.yml
  scripts/  (8 files)
    tests/  (3 files)
      … 3 files under this directory
    generate_meta_skill.py
    pr-labeler.js
    sync_root_skills.py
    update_registry_dates.py
    validate_root_skills.py
  workflows/  (7 files)
    check-codex-skill.yml
    check-cursor-plugin.yml
    check-root-skills.yml
    deploy-pages.yml
    pr-labeler-tests.yml
    pr-labeler.yml
    publish-cli-hub.yml
  CODEOWNERS
  PULL_REQUEST_TEMPLATE.md
  labeler.yml
.pi-extension/  (4 files)
  cli-anything/  (4 files)
    tests/  (1 files)
      … 1 files under this directory
    README.md
    index.ts
    install.sh
3MF/  (17 files)
  agent-harness/  (17 files)
    cli_anything/  (15 files)
      … 15 files under this directory
    3MF.md
    setup.py
QGIS/  (22 files)
  agent-harness/  (22 files)
    cli_anything/  (19 files)
      … 19 files under this directory
    QGIS.md
    pytest.ini
    setup.py
adguardhome/  (26 files)
  agent-harness/  (26 files)
    cli_anything/  (23 files)
      … 23 files under this directory
    .gitignore
    ADGUARDHOME.md
    setup.py
anygen/  (18 files)
  agent-harness/  (18 files)
    cli_anything/  (16 files)
      … 16 files under this directory
    ANYGEN.md
    setup.py
assets/  (2 files)
  demos/  (1 files)
    README.md
  .gitkeep
audacity/  (34 files)
  agent-harness/  (34 files)
    cli_anything/  (32 files)
      … 32 files under this directory
    AUDACITY.md
    setup.py
blender/  (27 files)
  agent-harness/  (27 files)
    cli_anything/  (25 files)
      … 25 files under this directory
    BLENDER.md
    setup.py
browser/  (20 files)
  agent-harness/  (20 files)
    cli_anything/  (18 files)
      … 18 files under this directory
    HARNESS.md
    setup.py
calibre/  (23 files)
  agent-harness/  (23 files)
    cli_anything/  (19 files)
      … 19 files under this directory
    .gitignore
    CALIBRE.md
    FIX_NOTES.md
    setup.py
cc-switch/  (14 files)
  agent-harness/  (14 files)
    cli_anything/  (12 files)
      … 12 files under this directory
    CCSWITCH.md
    setup.py
chromadb/  (20 files)
  agent-harness/  (20 files)
    cli_anything/  (18 files)
      … 18 files under this directory
    CHROMADB.md
    setup.py
cli-anything-plugin/  (26 files)
  .claude-plugin/  (1 files)
    plugin.json
  commands/  (5 files)
    cli-anything.md
    list.md
    refine.md
    test.md
    validate.md
  guides/  (8 files)
    auto-save-dry-run.md
    filter-translation.md
    mcp-backend.md
    preview-methodology.md
    pypi-publishing.md
    session-locking.md
    skill-generation.md
    timecode-precision.md
  scripts/  (1 files)
    setup-cli-anything.sh
  templates/  (1 files)
    SKILL.md.template
  tests/  (1 files)
    test_skill_generator.py
  HARNESS.md
  LICENSE
  PUBLISHING.md
  QUICKSTART.md
  README.md
  preview_bundle.py
  repl_skin.py
  skill_generator.py
  verify-plugin.sh
cli-hub/  (14 files)
  cli_hub/  (8 files)
    __init__.py
    analytics.py
    cli.py
    installer.py
    matrix.py
    matrix_skill.py
    preview.py
    registry.py
  tests/  (3 files)
    __init__.py
    test_cli_hub.py
    test_matrix_skill_dist.py
  MANIFEST.in
  README.md
  setup.py
cli-hub-matrix/  (13 files)
  3d-cad/  (1 files)
    SKILL.md
  game-development/  (1 files)
    SKILL.md
  image-design/  (1 files)
    SKILL.md
  knowledge-research/  (1 files)
    SKILL.md
  video-creation/  (9 files)
    references/  (7 files)
      … 7 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
cli-hub-meta-skill/  (1 files)
  SKILL.md
cloudanalyzer/  (17 files)
  agent-harness/  (17 files)
    cli_anything/  (15 files)
      … 15 files under this directory
    CLOUDANALYZER.md
    setup.py
cloudcompare/  (18 files)
  agent-harness/  (18 files)
    cli_anything/  (16 files)
      … 16 files under this directory
    CLOUDCOMPARE.md
    setup.py
codex-skill/  (5 files)
  agents/  (1 files)
    openai.yaml
  scripts/  (2 files)
    install.ps1
    install.sh
  tests/  (1 files)
    test_install.sh
  SKILL.md
comfyui/  (17 files)
  agent-harness/  (17 files)
    cli_anything/  (16 files)
      … 16 files under this directory
    setup.py
cursor-plugin/  (17 files)
  .cursor-plugin/  (1 files)
    plugin.json
  commands/  (5 files)
    cli-anything-list.md
    cli-anything-refine.md
    cli-anything-test.md
    cli-anything-validate.md
    cli-anything.md
  rules/  (1 files)
    cli-anything-generator.mdc
  scripts/  (6 files)
    install.ps1
    install.sh
    lib.ps1
    lib.sh
    uninstall.ps1
    uninstall.sh
  skills/  (1 files)
    cli-anything-generator/  (1 files)
      … 1 files under this directory
  tests/  (2 files)
    test_install.ps1
    test_install.sh
  README.md
dify-workflow/  (15 files)
  agent-harness/  (15 files)
    cli_anything/  (12 files)
      … 12 files under this directory
    DIFY_WORKFLOW.md
    MANIFEST.in
    setup.py
docs/  (24 files)
  hub/  (16 files)
    .well-known/  (4 files)
      … 4 files under this directory
    _config.yml
    demos.html
    docs.html
    index-modern.html
    index.html
    index.md
    llms-full.txt
    llms.txt
    openapi.json
    pricing.md
    robots.txt
    sitemap.xml
  scripts/  (4 files)
    blender_gyro_observatory_demo.py
    blender_orbital_relay_drone_demo.py
    blender_preview_story_demo.py
    freecad_live_preview_demo.py
  FREECAD_VIDEO_REFERENCE.md
  PREVIEW_MECHANISM_PROGRESS.md
  PREVIEW_PROGRESS.md
  PREVIEW_PROTOCOL.md
drawio/  (21 files)
  agent-harness/  (21 files)
    cli_anything/  (19 files)
      … 19 files under this directory
    DRAWIO.md
    setup.py
eez-studio/  (19 files)
  agent-harness/  (19 files)
    cli_anything/  (17 files)
      … 17 files under this directory
    EEZ_STUDIO.md
    setup.py
eth2-quickstart/  (21 files)
  agent-harness/  (21 files)
    cli_anything/  (19 files)
      … 19 files under this directory
    ETH2-QUICKSTART.md
    setup.py
exa/  (16 files)
  agent-harness/  (16 files)
    cli_anything/  (14 files)
      … 14 files under this directory
    EXA.md
    setup.py
firefly-iii/  (33 files)
  agent-harness/  (33 files)
    cli_anything/  (30 files)
      … 30 files under this directory
    skills/  (1 files)
      … 1 files under this directory
    README.md
    setup.py
freecad/  (36 files)
  agent-harness/  (36 files)
    cli_anything/  (34 files)
      … 34 files under this directory
    FREECAD.md
    setup.py
gimp/  (22 files)
  agent-harness/  (22 files)
    cli_anything/  (20 files)
      … 20 files under this directory
    GIMP.md
    setup.py
godot/  (19 files)
  agent-harness/  (19 files)
    cli_anything/  (17 files)
      … 17 files under this directory
    GODOT.md
    setup.py
hermes-skill/  (4 files)
  agents/  (1 files)
    hermes.yaml
  scripts/  (2 files)
    install.ps1
    install.sh
  SKILL.md
inkscape/  (26 files)
  agent-harness/  (26 files)
    cli_anything/  (24 files)
      … 24 files under this directory
    INKSCAPE.md
    setup.py
intelwatch/  (11 files)
  agent-harness/  (11 files)
    cli_anything/  (9 files)
      … 9 files under this directory
    INTELWATCH.md
    setup.py
iterm2/  (39 files)
  agent-harness/  (39 files)
    cli_anything/  (36 files)
      … 36 files under this directory
    ITERM2.md
    README.md
    setup.py
joplin/  (29 files)
  agent-harness/  (29 files)
    cli_anything/  (26 files)
      … 26 files under this directory
    JOPLIN.md
    README.md
    setup.py
jumpserver/  (24 files)
  agent-harness/  (24 files)
    cli_anything/  (21 files)
      … 21 files under this directory
    JUMPSERVER.md
    pyproject.toml
    setup.py
kdenlive/  (24 files)
  agent-harness/  (24 files)
    cli_anything/  (22 files)
      … 22 files under this directory
    KDENLIVE.md
    setup.py
krita/  (19 files)
  agent-harness/  (19 files)
    cli_anything/  (17 files)
      … 17 files under this directory
    KRITA.md
    setup.py
libreoffice/  (9 files)
  agent-harness/  (9 files)
    cli_anything/  (8 files)
      … 8 files under this directory
    LIBREOFFICE.md
.gitignore
CITATION.cff
CONTRIBUTING.md
LICENSE
README.md
README_CN.md
README_DE.md
README_JA.md
SECURITY.md
```

## Entry points

- [.github/scripts/generate_meta_skill.py:207](https://github.com/HKUDS/CLI-Anything/blob/34f519533bc175d2fe287ab8316b0dd99bb9cc43/.github/scripts/generate_meta_skill.py#L207)
- [.github/scripts/sync_root_skills.py:92](https://github.com/HKUDS/CLI-Anything/blob/34f519533bc175d2fe287ab8316b0dd99bb9cc43/.github/scripts/sync_root_skills.py#L92)
- [.github/scripts/update_registry_dates.py:325](https://github.com/HKUDS/CLI-Anything/blob/34f519533bc175d2fe287ab8316b0dd99bb9cc43/.github/scripts/update_registry_dates.py#L325)
- [.github/scripts/validate_root_skills.py:113](https://github.com/HKUDS/CLI-Anything/blob/34f519533bc175d2fe287ab8316b0dd99bb9cc43/.github/scripts/validate_root_skills.py#L113)
- [3MF/agent-harness/cli_anything/threemf/threemf_cli.py:101](https://github.com/HKUDS/CLI-Anything/blob/34f519533bc175d2fe287ab8316b0dd99bb9cc43/3MF/agent-harness/cli_anything/threemf/threemf_cli.py#L101)
- [QGIS/agent-harness/cli_anything/qgis/__main__.py:6](https://github.com/HKUDS/CLI-Anything/blob/34f519533bc175d2fe287ab8316b0dd99bb9cc43/QGIS/agent-harness/cli_anything/qgis/__main__.py#L6)
- [QGIS/agent-harness/cli_anything/qgis/qgis_cli.py:224](https://github.com/HKUDS/CLI-Anything/blob/34f519533bc175d2fe287ab8316b0dd99bb9cc43/QGIS/agent-harness/cli_anything/qgis/qgis_cli.py#L224)
- [adguardhome/agent-harness/cli_anything/adguardhome/__main__.py:4](https://github.com/HKUDS/CLI-Anything/blob/34f519533bc175d2fe287ab8316b0dd99bb9cc43/adguardhome/agent-harness/cli_anything/adguardhome/__main__.py#L4)
- [adguardhome/agent-harness/cli_anything/adguardhome/adguardhome_cli.py:69](https://github.com/HKUDS/CLI-Anything/blob/34f519533bc175d2fe287ab8316b0dd99bb9cc43/adguardhome/agent-harness/cli_anything/adguardhome/adguardhome_cli.py#L69)
- [anygen/agent-harness/cli_anything/anygen/anygen_cli.py:108](https://github.com/HKUDS/CLI-Anything/blob/34f519533bc175d2fe287ab8316b0dd99bb9cc43/anygen/agent-harness/cli_anything/anygen/anygen_cli.py#L108)
- [audacity/agent-harness/cli_anything/audacity/audacity_cli.py:137](https://github.com/HKUDS/CLI-Anything/blob/34f519533bc175d2fe287ab8316b0dd99bb9cc43/audacity/agent-harness/cli_anything/audacity/audacity_cli.py#L137)
- [blender/agent-harness/cli_anything/blender/blender_cli.py:198](https://github.com/HKUDS/CLI-Anything/blob/34f519533bc175d2fe287ab8316b0dd99bb9cc43/blender/agent-harness/cli_anything/blender/blender_cli.py#L198)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| adguardhome package | library | Observed | Groups 4 file(s) under adguardhome package (observed from repository paths and static analysis). Observed top-level classes: AdGuardHomeClient, ReplSkin. Observed top-level functions: _display_home_path, _strip_ansi, _v… |
| anygen package | library | Observed | Groups 4 file(s) under anygen package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _display_home_path, _make_auth_token, _require_api_key, _st… |
| audacity package | library | Observed | Groups 13 file(s) under audacity package (observed from repository paths and static analysis). Observed top-level classes: EvalContext, ReplSkin, TaskSpec. Observed top-level functions: _build_summary, _display_home_pat… |
| blender package | library | Observed | Groups 6 file(s) under blender package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _clean_none_fields, _display_home_path, _engine_to_bpy, _g… |
| browser package | library | Observed | Groups 5 file(s) under browser package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _anchor_path_cmd, _assert_single_line, _build_server_args,… |
| 3MF package | library | Observed | Groups 4 file(s) under 3mf package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _axis_plane_normal, _project_to_2d, _strip_ansi, _visible_len,… |
| calibre package | library | Observed | Groups 4 file(s) under calibre package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _english_env, _strip_ansi, _visible_len, find_calibredb, f… |
| cc-switch package | library | Observed | Groups 3 file(s) under cc-switch package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _display_home_path, _strip_ansi, _visible_len. |
| chromadb package | library | Observed | Groups 5 file(s) under chromadb package (observed from repository paths and static analysis). Observed top-level classes: ChromaDBBackend, ReplSkin. Observed top-level functions: _display_home_path, _strip_ansi, _visibl… |
| cli-anything-plugin package | library | Observed | Groups 4 file(s) under cli-anything-plugin package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _clean_none_fields, _display_home_path, _iter_… |
| cli-hub package | library | Observed | Groups 7 file(s) under cli-hub package (observed from repository paths and static analysis). Observed top-level classes: _NoCacheHandler. Observed top-level functions: _analytics_dir, _apply_session_trajectory_metadata,… |
| cloudanalyzer package | library | Observed | Groups 4 file(s) under cloudanalyzer package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _display_home_path, _ensure_ca, _strip_ansi, _visibl… |
| cloudcompare package | library | Observed | Groups 4 file(s) under cloudcompare package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _display_home_path, _strip_ansi, _visible_len, apply_… |
| codex-skill package | library | Observed | Groups 1 file(s) under codex-skill package (observed from repository paths and static analysis). |
| comfyui package | library | Observed | Groups 4 file(s) under comfyui package (observed from repository paths and static analysis). Observed top-level functions: api_delete, api_get, api_get_raw, api_post. |
| Configuration and deployment | config | Observed | Groups 39 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: build_py, sdist. Observed top-level functions: _handle_metadata_query, _sync_matrix_… |
| cursor-plugin package | library | Observed | Groups 3 file(s) under cursor-plugin package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level functions: connect_db, get_cc_switch_dir, get_config_path, get_db_path, get_node_info, get_settings_path. |
| dify-workflow package | library | Observed | Groups 4 file(s) under dify-workflow package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _decode_output, _display_home_path, _strip_ansi, _vi… |
| drawio package | library | Observed | Groups 5 file(s) under drawio package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _display_home_path, _new_id, _strip_ansi, _visible_len, add… |
| eez-studio package | library | Observed | Groups 4 file(s) under eez-studio package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _display_home_path, _run_node, _strip_ansi, _visible_le… |
| Application entry point | entrypoint | Observed | Groups 61 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CommandGroup, CommandInfo, Example, JumpServerREPL, JumpserverCLI, SkillMetadata. Observe… |
| eth2-quickstart package | library | Observed | Groups 4 file(s) under eth2-quickstart package (observed from repository paths and static analysis). Observed top-level classes: Eth2QuickStartBackend, ReplSkin. Observed top-level functions: _display_home_path, _strip_… |
| exa package | library | Observed | Groups 4 file(s) under exa package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _strip_ansi, _visible_len, build_contents_param, check_connect… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| firefly-iii package | library | Observed | Groups 4 file(s) under firefly-iii package (observed from repository paths and static analysis). Observed top-level classes: FireflyIIIBackend, ReplSkin. |
| freecad package | library | Observed | Groups 6 file(s) under freecad package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _clean_none_fields, _display_home_path, _dominant_axis, _e… |
| gimp package | library | Observed | Groups 4 file(s) under gimp package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _build_export_cmd, _build_layer_script, _display_home_path, _… |
| godot package | library | Observed | Groups 5 file(s) under godot package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _display_home_path, _strip_ansi, _visible_len, find_godot_bi… |
| hermes-skill package | library | Observed | Groups 1 file(s) under hermes-skill package (observed from repository paths and static analysis). |
| inkscape package | library | Observed | Groups 5 file(s) under inkscape package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _display_home_path, _ns, _strip_ansi, _visible_len, creat… |
| intelwatch package | library | Observed | Groups 4 file(s) under intelwatch package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _display_home_path, _strip_ansi, _visible_len. |
| iterm2 package | library | Observed | Groups 4 file(s) under iterm2 package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _display_home_path, _strip_ansi, _visible_len, async_find_s… |
| joplin package | library | Observed | Groups 4 file(s) under joplin package (observed from repository paths and static analysis). Observed top-level classes: BackendConfig, ReplSkin. Observed top-level functions: _display_home_path, _line_is_benign_node_war… |
| jumpserver package | library | Observed | Groups 2 file(s) under jumpserver package (observed from repository paths and static analysis). Observed top-level classes: CLIError. Observed top-level functions: _iter_context_chain, handle_api_error, is_json_mode, ma… |
| kdenlive package | library | Observed | Groups 5 file(s) under kdenlive package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _add_disabled_filter, _add_prop, _avformat_indexes, _clip… |
| krita package | library | Observed | Groups 5 file(s) under krita package (observed from repository paths and static analysis). Observed top-level classes: ReplSkin. Observed top-level functions: _display_home_path, _run, _strip_ansi, _visible_len, _write_… |
| libreoffice package | library | Observed | Groups 1 file(s) under libreoffice package (observed from repository paths and static analysis). |
| QGIS package | library | Observed | Groups 4 file(s) under qgis package (observed from repository paths and static analysis). Observed top-level classes: QgisBackendError, QgisProcessError, ReplSkin. Observed top-level functions: _detect_qgis_prefix, _ext… |
| Service / domain layer | service | Observed | Groups 214 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: CLIState, DetectedHole, HistoryEntry, InspectParams, JumpServerClient, MeshData. Observed… |
| Tests | test | Observed | Groups 121 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH cli_anything.anygen.utils.anygen_backend.requests.post, PATCH cli_anything.anygen.utils.anygen_backend.requests… |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.cursor-plugin/marketplace.json` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/cli-wishlist.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/contributor-signup.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/labeler.yml` (config)
- `.github/workflows/check-codex-skill.yml` (ci)
- `.github/workflows/check-cursor-plugin.yml` (ci)
- `.github/workflows/check-root-skills.yml` (ci)
- `.github/workflows/deploy-pages.yml` (ci)
- `.github/workflows/pr-labeler-tests.yml` (ci)
- `.github/workflows/pr-labeler.yml` (ci)
- `.github/workflows/publish-cli-hub.yml` (ci)
- `3MF/agent-harness/setup.py` (manifest)
- `QGIS/agent-harness/pytest.ini` (config)
- `QGIS/agent-harness/setup.py` (manifest)
- `adguardhome/agent-harness/setup.py` (manifest)
- `anygen/agent-harness/setup.py` (manifest)
- `audacity/agent-harness/setup.py` (manifest)
- `blender/agent-harness/setup.py` (manifest)
- `browser/agent-harness/setup.py` (manifest)
- `calibre/agent-harness/setup.py` (manifest)
- `cc-switch/agent-harness/setup.py` (manifest)
- `chromadb/agent-harness/setup.py` (manifest)
- `cli-anything-plugin/.claude-plugin/plugin.json` (config)
- `cli-hub/MANIFEST.in` (manifest)
- `cli-hub/setup.py` (manifest)
- `cloudanalyzer/agent-harness/setup.py` (manifest)
- `cloudcompare/agent-harness/setup.py` (manifest)
- `codex-skill/agents/openai.yaml` (config)
- `comfyui/agent-harness/setup.py` (manifest)
- `cursor-plugin/.cursor-plugin/plugin.json` (config)
- `dify-workflow/agent-harness/MANIFEST.in` (manifest)
- `dify-workflow/agent-harness/setup.py` (manifest)
- `docs/hub/.well-known/agent-card.json` (config)
- `docs/hub/.well-known/agent-skills/index.json` (config)
- `docs/hub/.well-known/agent.json` (config)
- `docs/hub/.well-known/ai-plugin.json` (config)
- `docs/hub/_config.yml` (config)
- `docs/hub/openapi.json` (config)
- `drawio/agent-harness/setup.py` (manifest)
- `eez-studio/agent-harness/setup.py` (manifest)
- `eth2-quickstart/agent-harness/setup.py` (manifest)
- `exa/agent-harness/setup.py` (manifest)
- `firefly-iii/agent-harness/setup.py` (manifest)
- `freecad/agent-harness/setup.py` (manifest)
- `gimp/agent-harness/setup.py` (manifest)
- `godot/agent-harness/setup.py` (manifest)
- `hermes-skill/agents/hermes.yaml` (config)
- `inkscape/agent-harness/setup.py` (manifest)
- `intelwatch/agent-harness/setup.py` (manifest)
- `iterm2/agent-harness/setup.py` (manifest)
- `joplin/agent-harness/setup.py` (manifest)
- `jumpserver/agent-harness/pyproject.toml` (manifest)
- `jumpserver/agent-harness/setup.py` (manifest)
- `kdenlive/agent-harness/setup.py` (manifest)
- `krita/agent-harness/setup.py` (manifest)

## Top-level layout

- `iterm2` — 39 analysed file(s)
- `freecad` — 36 analysed file(s)
- `audacity` — 34 analysed file(s)
- `firefly-iii` — 33 analysed file(s)
- `joplin` — 29 analysed file(s)
- `blender` — 27 analysed file(s)
- `adguardhome` — 26 analysed file(s)
- `cli-anything-plugin` — 26 analysed file(s)
- `inkscape` — 26 analysed file(s)
- `docs` — 24 analysed file(s)
- `jumpserver` — 24 analysed file(s)
- `kdenlive` — 24 analysed file(s)
- `.github` — 23 analysed file(s)
- `calibre` — 23 analysed file(s)
- `QGIS` — 22 analysed file(s)
- `gimp` — 22 analysed file(s)
- `drawio` — 21 analysed file(s)
- `eth2-quickstart` — 21 analysed file(s)
- `browser` — 20 analysed file(s)
- `chromadb` — 20 analysed file(s)
- `eez-studio` — 19 analysed file(s)
- `godot` — 19 analysed file(s)
- `krita` — 19 analysed file(s)
- `anygen` — 18 analysed file(s)
- `cloudcompare` — 18 analysed file(s)
- `3MF` — 17 analysed file(s)
- `cloudanalyzer` — 17 analysed file(s)
- `comfyui` — 17 analysed file(s)
- `cursor-plugin` — 17 analysed file(s)
- `exa` — 16 analysed file(s)
- `dify-workflow` — 15 analysed file(s)
- `cc-switch` — 14 analysed file(s)
- `cli-hub` — 14 analysed file(s)
- `cli-hub-matrix` — 13 analysed file(s)
- `intelwatch` — 11 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `libreoffice` — 9 analysed file(s)
- `codex-skill` — 5 analysed file(s)
- `.pi-extension` — 4 analysed file(s)
- `hermes-skill` — 4 analysed file(s)
- `assets` — 2 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)
- `.cursor-plugin` — 1 analysed file(s)
- `cli-hub-meta-skill` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File audacity/agent-harness/cli_anything/audacity/utils/file_io.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `34f519533bc175d2fe287ab8316b0dd99bb9cc43` is the revision these paths and observations refer to.
