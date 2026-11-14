# Project structure: SFTtech/openage

**Analysed commit:** `5f042b9ce84ed13f78473faebf4a8ed90a1da8cd`

**Commit reference:** [5f042b9ce84ed13f78473faebf4a8ed90a1da8cd](https://github.com/SFTtech/openage/commit/5f042b9ce84ed13f78473faebf4a8ed90a1da8cd)

**Tree at this commit:** [SFTtech/openage@5f042b9ce84e](https://github.com/SFTtech/openage/tree/5f042b9ce84ed13f78473faebf4a8ed90a1da8cd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | SFTtech/openage |
| Description | Clone of the Age of Empires II engine 🚀  |
| Stars | 14604 |
| Forks | 1287 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `5f042b9ce84ed13f78473faebf4a8ed90a1da8cd` |
| Retrieved at | 2026-11-14T19:09:23.102961+00:00 |
| Files in this snapshot | 797 |

## Directory tree

```text
.github/  (4 files)
  PULL_REQUEST_TEMPLATES/  (2 files)
    pull_request_template.md
    release_template.md
  workflows/  (2 files)
    macos.yml
    ubuntu-26.04.yml
assets/  (124 files)
  doc/  (5 files)
    liberapay.svg
    license.svg
    matrix.svg
    matrixroom.svg
    reddit.svg
  logo/  (5 files)
    CMakeLists.txt
    banner-xlink.svg
    banner.svg
    crown.svg
    crown_print.svg
  qml/  (19 files)
    .gitignore
    Actions.qml
    ActionsGrid.qml
    BindsHelp.qml
    ButtonExtruded.qml
    ButtonExtrudedStyle.qml
    ButtonFlat.qml
    ButtonFlatStyle.qml
    CheckBoxFlat.qml
    CheckBoxFlatStyle.qml
    CreateGameWhenReady.qml
    GeneratorControl.qml
    GeneratorParametersConfiguration.qml
    IngameHud.qml
    Paper.qml
    TextFieldFlat.qml
    TextFieldFlatStyle.qml
    TypePicker.qml
    main.qml
  shaders/  (21 files)
    CMakeLists.txt
    alphamask.frag.glsl
    alphamask.vert.glsl
    equalsEpsilon.glsl
    final.frag.glsl
    final.vert.glsl
    hud_drag_select.frag.glsl
    hud_drag_select.vert.glsl
    identity.vert.glsl
    maptexture.frag.glsl
    maptexture.vert.glsl
    skybox.frag.glsl
    skybox.vert.glsl
    teamcolors.frag.glsl
    terrain.frag.glsl
    terrain.vert.glsl
    texturefont.frag.glsl
    texturefont.vert.glsl
    world2d.frag.glsl
    world2d.vert.glsl
    world3d.vert.glsl
  test/  (70 files)
    nyan/  (2 files)
      … 2 files under this directory
    qml/  (2 files)
      … 2 files under this directory
    shaders/  (51 files)
      … 51 files under this directory
    textures/  (14 files)
      … 14 files under this directory
    CMakeLists.txt
  textures/  (2 files)
    CMakeLists.txt
    torn_paper_edge.docx
  .gitignore
  CMakeLists.txt
buildsystem/  (54 files)
  codecompliance/  (13 files)
    __init__.py
    __main__.py
    authors.py
    clangtidy.py
    cppstyle.py
    cython.py
    headerguards.py
    legal.py
    modes.py
    ruff.py
    textfiles.py
    ty.py
    util.py
  modules/  (11 files)
    DownloadCache.cmake
    FindCython.cmake
    FindEpoxy.cmake
    FindGCCBacktrace.cmake
    FindGPerfTools.cmake
    FindHarfBuzz.cmake
    FindInotify.cmake
    FindOgg.cmake
    FindOpusfile.cmake
    FindPython.cmake
    FindPython_test.cpp
  scripts/  (4 files)
    EmbedFont.cmake
    EmbedPython.cmake
    EmbedWinDependencies.cmake
    copy_modules.py
  templates/  (5 files)
    Doxyfile.in
    ExternalFetch.cmake.in
    ForwardVariables.cmake.in
    openage.bat.in
    qt.conf
  CheckCompilerFeatures.cmake
  CheckInSourceBuild.cmake
  CheckRuntimeDependencies.cmake
  DependencyFetch.cmake
  DetectProjectVersion.cmake
  HandleCXXOptions.cmake
  HandlePythonOptions.cmake
  StdHeaderUnit.cmake
  __init__.py
  check_py_file_list.py
  codegen.cmake
  compilepy.py
  cpp.cmake
  cythonize.py
  doxygen.cmake
  doxygen_custom.css
  inplacemodules.py
  options.cmake
  pxdgen.py
  python.cmake
  util.cmake
cfg/  (17 files)
  converter/  (14 files)
    games/  (14 files)
      … 14 files under this directory
  .gitignore
  CMakeLists.txt
  keybinds.oac
doc/  (223 files)
  build_instructions/  (11 files)
    arch_linux.md
    debian.md
    docker.md
    fedora.md
    freebsd.md
    gentoo.md
    macos.md
    nix.md
    opensuse.md
    ubuntu.md
    windows_msvc.md
  changelogs/  (22 files)
    engine/  (15 files)
      … 15 files under this directory
    nyan_api/  (7 files)
      … 7 files under this directory
  code/  (64 files)
    converter/  (4 files)
      … 4 files under this directory
    game_simulation/  (20 files)
      … 20 files under this directory
    images/  (16 files)
      … 16 files under this directory
    input/  (3 files)
      … 3 files under this directory
    pathfinding/  (2 files)
      … 2 files under this directory
    renderer/  (7 files)
      … 7 files under this directory
    README.md
    architecture.md
    coordinate-systems.md
    curves.md
    event_system.md
    exceptions.md
    gui.md
    logger.md
    optimization.md
    pyinterface.md
    testing.md
    time.md
  code_style/  (6 files)
    .gitignore
    cat.cpp
    cat.cppm
    cat.h
    inttypes.md
    tabs_n_spaces.md
  convert/  (5 files)
    README.md
    convert_single_file.md
    debugger.md
    interactive.md
    nyan.md
  ide/  (5 files)
    configs/  (1 files)
      … 1 files under this directory
    README.md
    emacs.md
    qt_creator.md
    vscode.md
  ideas/  (14 files)
    editor/  (9 files)
      … 9 files under this directory
    ai.md
    fr_technical_overview.md
    gameplay.md
    interface.md
    technical.md
  media/  (27 files)
    images/  (1 files)
      … 1 files under this directory
    openage/  (9 files)
      … 9 files under this directory
    patterns/  (3 files)
      … 3 files under this directory
    aoc-slp-list.md
    blendomatic.md
    drs-files.md
    evolution-openage-gource.md
    filtermaps-dat.md
    lzx_compression_info.md
    original-metadata.md
    sld-files.md
    slp-files.md
    smp-files.md
    smx-files.md
    sound.md
    stemplet-dat.md
    terrain.md
  nyan/  (8 files)
    api_reference/  (6 files)
      … 6 files under this directory
    README.md
    openage-lib.md
  reverse_engineering/  (49 files)
    game_mechanics/  (23 files)
      … 23 files under this directory
    networking/  (16 files)
      … 16 files under this directory
    unit_stats/  (7 files)
      … 7 files under this directory
    aoc_structures_00_09_26_0809
    civilizations.md
    scoring.md
  README.md
  assets.md
  building.md
  buildsystem.md
  contributing.md
  debug.md
  development.md
  media_convert.md
  project_structure.md
  releasing.md
  running.md
  troubleshooting.md
etc/  (5 files)
  gdb_pretty/  (2 files)
    __init__.py
    printers.py
  lsan.supp
  openage.gdbinit
  valgrind-python.supp
legal/  (3 files)
  BSD-3-clause
  GPLv3
  LGPLv2.0
libopenage/  (353 files)
  assets/  (5 files)
    CMakeLists.txt
    mod_manager.cpp
    mod_manager.h
    modpack.cpp
    modpack.h
  audio/  (33 files)
    CMakeLists.txt
    audio_manager.cpp
    audio_manager.h
    category.cpp
    category.h
    dynamic_loader.cpp
    dynamic_loader.h
    dynamic_resource.cpp
    dynamic_resource.h
    error.cpp
    error.h
    format.cpp
    format.h
    hash_functions.h
    in_memory_loader.cpp
    in_memory_loader.h
    in_memory_resource.cpp
    in_memory_resource.h
    loader_policy.cpp
    loader_policy.h
    opus_dynamic_loader.cpp
    opus_dynamic_loader.h
    opus_in_memory_loader.cpp
    opus_in_memory_loader.h
    … 9 more files
  console/  (8 files)
    CMakeLists.txt
    buf.cpp
    buf.h
    console.cpp
    console.h
    draw.cpp
    draw.h
    tests.cpp
  coord/  (18 files)
    CMakeLists.txt
    chunk.cpp
    chunk.h
    coord.cpp.template
    coord.h.template
    coord_test.cpp
    declarations.cpp
    declarations.h
    phys.cpp
    phys.h
    pixel.cpp
    pixel.h
    scene.cpp
    scene.h
    term.cpp
    term.h
    tile.cpp
    tile.h
  curve/  (35 files)
    container/  (15 files)
      … 15 files under this directory
    tests/  (3 files)
      … 3 files under this directory
    CMakeLists.txt
    base_curve.cpp
    base_curve.h
    continuous.cpp
    continuous.h
    discrete.cpp
    discrete.h
    discrete_mod.cpp
    discrete_mod.h
    interpolated.cpp
    interpolated.h
    keyframe.cpp
    keyframe.h
    keyframe_container.cpp
    keyframe_container.h
    segmented.cpp
    segmented.h
  cvar/  (3 files)
    CMakeLists.txt
    cvar.cpp
    cvar.h
  datastructure/  (6 files)
    CMakeLists.txt
    concurrent_queue.h
    constexpr_map.h
    pairing_heap.h
    tests.cpp
    tests.h
  engine/  (3 files)
    CMakeLists.txt
    engine.cpp
    engine.h
  error/  (10 files)
    CMakeLists.txt
    backtrace.cpp
    backtrace.h
    demo.cpp
    error.cpp
    error.h
    handlers.cpp
    handlers.h
    stackanalyzer.cpp
    stackanalyzer.h
  event/  (27 files)
    demo/  (11 files)
      … 11 files under this directory
    CMakeLists.txt
    event.cpp
    event.h
    event_loop.cpp
    event_loop.h
    evententity.cpp
    evententity.h
    eventhandler.cpp
    eventhandler.h
    eventqueue.cpp
    eventqueue.h
    eventstore.cpp
    eventstore.h
    state.cpp
    state.h
    tests.cpp
  gamestate/  (151 files)
    activity/  (30 files)
      … 30 files under this directory
    api/  (23 files)
      … 23 files under this directory
    component/  (40 files)
      … 40 files under this directory
    demo/  (5 files)
      … 5 files under this directory
    event/  (11 files)
      … 11 files under this directory
    system/  (9 files)
      … 9 files under this directory
    CMakeLists.txt
    definitions.cpp
    definitions.h
    entity_factory.cpp
    entity_factory.h
    game.cpp
    game.h
    game_entity.cpp
    game_entity.h
    game_state.cpp
    game_state.h
    manager.cpp
    manager.h
    map.cpp
    map.h
    player.cpp
    player.h
    simulation.cpp
    simulation.h
    terrain.cpp
    terrain.h
    terrain_chunk.cpp
    terrain_chunk.h
    terrain_factory.cpp
    … 9 more files
  input/  (34 files)
    controller/  (22 files)
      … 22 files under this directory
    CMakeLists.txt
    action.cpp
    action.h
    event.cpp
    event.h
    input_context.cpp
    input_context.h
    input_manager.cpp
    input_manager.h
    tests.cpp
    text_to_event.cpp
    text_to_event.h
  job/  (15 files)
    CMakeLists.txt
    abortable_job_state.h
    job.h
    job_aborted_exception.h
    job_group.cpp
    job_group.h
    job_manager.cpp
    job_manager.h
    job_state.h
    job_state_base.h
    tests.cpp
    typed_job_state_base.h
    types.h
    worker.cpp
    worker.h
  log/  (1 files)
    CMakeLists.txt
  .gitignore
  CMakeLists.txt
  config.cpp.in
  config.h.in
.clang-format
.clangd
.gitignore
.mailmap
AGENTS.md
CMakeLists.txt
README.md
changelog.md
configure
copying.md
flake.lock
flake.nix
justfile
kevinfile
```

## Entry points

- [buildsystem/check_py_file_list.py:62](https://github.com/SFTtech/openage/blob/5f042b9ce84ed13f78473faebf4a8ed90a1da8cd/buildsystem/check_py_file_list.py#L62)
- [buildsystem/codecompliance/__main__.py:313](https://github.com/SFTtech/openage/blob/5f042b9ce84ed13f78473faebf4a8ed90a1da8cd/buildsystem/codecompliance/__main__.py#L313)
- [buildsystem/compilepy.py:106](https://github.com/SFTtech/openage/blob/5f042b9ce84ed13f78473faebf4a8ed90a1da8cd/buildsystem/compilepy.py#L106)
- [buildsystem/cythonize.py:253](https://github.com/SFTtech/openage/blob/5f042b9ce84ed13f78473faebf4a8ed90a1da8cd/buildsystem/cythonize.py#L253)
- [buildsystem/inplacemodules.py:71](https://github.com/SFTtech/openage/blob/5f042b9ce84ed13f78473faebf4a8ed90a1da8cd/buildsystem/inplacemodules.py#L71)
- [buildsystem/pxdgen.py:472](https://github.com/SFTtech/openage/blob/5f042b9ce84ed13f78473faebf4a8ed90a1da8cd/buildsystem/pxdgen.py#L472)
- [buildsystem/scripts/copy_modules.py:46](https://github.com/SFTtech/openage/blob/5f042b9ce84ed13f78473faebf4a8ed90a1da8cd/buildsystem/scripts/copy_modules.py#L46)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 32 file(s) under api layer (observed from repository paths and static analysis). |
| buildsystem package | library | Observed | Groups 14 file(s) under buildsystem package (observed from repository paths and static analysis). Observed top-level classes: HeaderError, Strlazy. Observed top-level functions: _create_fix, _run_tool, check_mode, clamp… |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 7 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: CythonFilter, LineFilter, PXDGenerator, ParserError. Observed top-level functions: clone_f… |
| etc package | library | Observed | Groups 2 file(s) under etc package (observed from repository paths and static analysis). Observed top-level classes: CoordPrinter, FixedPointPrinter, KeyframePrinter, PathFlowTypePrinter, PathIntegratedFlagsTypePrinter,… |
| libopenage package | library | Observed | Groups 281 file(s) under libopenage package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 73 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/macos.yml` (ci)
- `.github/workflows/ubuntu-26.04.yml` (ci)
- `cfg/converter/games/aoc/version_hashes.toml` (config)
- `cfg/converter/games/aoc_demo/version_hashes.toml` (config)
- `cfg/converter/games/aok/version_hashes.toml` (config)
- `cfg/converter/games/de1/version_hashes.toml` (config)
- `cfg/converter/games/de2/version_hashes.toml` (config)
- `cfg/converter/games/game_editions.toml` (config)
- `cfg/converter/games/game_expansions.toml` (config)
- `cfg/converter/games/hd/version_hashes.toml` (config)
- `cfg/converter/games/hd_ak/version_hashes.toml` (config)
- `cfg/converter/games/hd_fgt/version_hashes.toml` (config)
- `cfg/converter/games/hd_raj/version_hashes.toml` (config)
- `cfg/converter/games/ror/version_hashes.toml` (config)
- `cfg/converter/games/swgb/version_hashes.toml` (config)
- `cfg/converter/games/swgb_cc/version_hashes.toml` (config)
- `doc/ide/configs/vscode/tasks.json` (config)

## Top-level layout

- `libopenage` — 353 analysed file(s)
- `doc` — 223 analysed file(s)
- `assets` — 124 analysed file(s)
- `buildsystem` — 54 analysed file(s)
- `cfg` — 17 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `etc` — 5 analysed file(s)
- `.github` — 4 analysed file(s)
- `legal` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5f042b9ce84ed13f78473faebf4a8ed90a1da8cd` is the revision these paths and observations refer to.
