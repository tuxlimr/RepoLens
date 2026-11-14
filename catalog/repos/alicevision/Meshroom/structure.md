# Project structure: alicevision/Meshroom

**Analysed commit:** `d787a6bf29f5e318f0e32d22d6e7109b065dad4c`

**Commit reference:** [d787a6bf29f5e318f0e32d22d6e7109b065dad4c](https://github.com/alicevision/Meshroom/commit/d787a6bf29f5e318f0e32d22d6e7109b065dad4c)

**Tree at this commit:** [alicevision/Meshroom@d787a6bf29f5](https://github.com/alicevision/Meshroom/tree/d787a6bf29f5e318f0e32d22d6e7109b065dad4c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | alicevision/Meshroom |
| Description | Node-based Visual Programming Toolbox |
| Stars | 13091 |
| Forks | 1242 |
| Licence | Other |
| Language | Python |
| Default branch | develop |
| Analysed commit | `d787a6bf29f5e318f0e32d22d6e7109b065dad4c` |
| Retrieved at | 2026-11-14T19:09:55.950999+00:00 |
| Files in this snapshot | 470 |

## Directory tree

```text
.claude/  (1 files)
  settings.json
.github/  (15 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    question_help.md
  scripts/  (4 files)
    nightly-check.sh
    nightly-common.sh
    nightly-publish.sh
    pyside6-smoke-test.py
  workflows/  (5 files)
    build-binary.yml
    build-pyside6-linux.yml
    continuous-integration.yml
    nightly.yml
    run-tests.yml
  FUNDING.yml
  pull_request_template.md
  stale.yml
.vscode/  (1 files)
  launch.json
bin/  (10 files)
  meshroom_batch
  meshroom_compute
  meshroom_createChunks
  meshroom_info
  meshroom_localfarm
  meshroom_newNodeType
  meshroom_plugins
  meshroom_statistics
  meshroom_status
  meshroom_submit
docker/  (12 files)
  Dockerfile
  Dockerfile_rocky_deps
  Dockerfile_ubuntu_deps
  build-all.sh
  build-image.sh
  build-rocky.sh
  build-ubuntu.sh
  common.sh
  download-models.sh
  extract-image.sh
  extract-rocky.sh
  extract-ubuntu.sh
docs/  (16 files)
  source/  (11 files)
    _ext/  (4 files)
      … 4 files under this directory
    _templates/  (2 files)
      … 2 files under this directory
    api.rst
    changes.rst
    conf.py
    index.rst
    install.rst
  .gitignore
  Makefile
  README.md
  make.bat
  requirements.txt
localfarm/  (6 files)
  README.md
  __init__.py
  localFarmBackend.py
  localFarmClient.py
  localFarmLauncher.py
  test.py
meshroom/  (319 files)
  common/  (5 files)
    PySignal.py
    __init__.py
    core.py
    deprecated.py
    qt.py
  core/  (53 files)
    desc/  (8 files)
      … 8 files under this directory
    node/  (8 files)
      … 8 files under this directory
    plugins/  (18 files)
      … 18 files under this directory
    __init__.py
    attribute.py
    cgroup.py
    evaluation.py
    exception.py
    fileUtils.py
    files.py
    graph.py
    graphIO.py
    httpUtils.py
    keyValues.py
    mixins.py
    mtyping.py
    nodeFactory.py
    stats.py
    submitter.py
    taskManager.py
    test.py
    utils.py
  nodes/  (21 files)
    general/  (20 files)
      … 20 files under this directory
    __init__.py
  submitters/  (3 files)
    localFarm/  (2 files)
      … 2 files under this directory
    __init__.py
  ui/  (234 files)
    components/  (17 files)
      … 17 files under this directory
    img/  (3 files)
      … 3 files under this directory
    qml/  (204 files)
      … 204 files under this directory
    __init__.py
    __main__.py
    app.py
    commands.py
    dockLayout.py
    dockLayoutManager.py
    graph.py
    palette.py
    scene.py
    utils.py
  __init__.py
  env.py
  multiview.py
tests/  (65 files)
  nodes/  (14 files)
    test/  (13 files)
      … 13 files under this directory
    __init__.py
  plugins/  (10 files)
    pluginA/  (6 files)
      … 6 files under this directory
    pluginB/  (2 files)
      … 2 files under this directory
    pluginC/  (1 files)
      … 1 files under this directory
    pluginSubmitter/  (1 files)
      … 1 files under this directory
  test_plugins/  (9 files)
    __init__.py
    test_loader.py
    test_localPluginsFolder.py
    test_manager.py
    test_metadata.py
    test_provider.py
    test_registry.py
    test_services.py
    test_task.py
  __init__.py
  appendTextAndFiles.mg
  conftest.py
  test_anySet_attribute.py
  test_attributeChoiceParam.py
  test_attributeDescDefaults.py
  test_attributeKeyValues.py
  test_attributeLambda.py
  test_attributeShape.py
  test_attributes.py
  test_compatibility.py
  test_compute.py
  test_computeMeshroomScene.py
  test_flowAttribute.py
  test_graph.py
  test_graphIO.py
  test_graphInputOutput.py
  test_groupAttributes.py
  test_invalidation.py
  test_listAttributes.py
  test_model.py
  test_multiview.py
  test_nodeAttributeChangedCallback.py
  test_nodeAttributesFormatting.py
  … 8 more files
.codecov.yml
.git-blame-ignore-revs
.gitignore
.readthedocs.yaml
AGENTS.md
CHANGES.md
CLAUDE.md
CMakeLists.txt
CODE_OF_CONDUCT.md
CONTRIBUTING.md
COPYING.md
INSTALL.md
INSTALL_PLUGINS.md
LICENSE-MPL2.md
NODE_DEVELOPMENT.md
README.md
RELEASING.md
WINDOWS_EXE.md
dev_requirements.txt
requirements.txt
setup.py
setupInitScriptUnix.py
setupInitScriptWindows.py
start.bat
… 1 more files
```

## Entry points

- [.github/scripts/pyside6-smoke-test.py:152](https://github.com/alicevision/Meshroom/blob/d787a6bf29f5e318f0e32d22d6e7109b065dad4c/.github/scripts/pyside6-smoke-test.py#L152)
- [localfarm/localFarmBackend.py:674](https://github.com/alicevision/Meshroom/blob/d787a6bf29f5e318f0e32d22d6e7109b065dad4c/localfarm/localFarmBackend.py#L674)
- [localfarm/localFarmLauncher.py:186](https://github.com/alicevision/Meshroom/blob/d787a6bf29f5e318f0e32d22d6e7109b065dad4c/localfarm/localFarmLauncher.py#L186)
- [localfarm/test.py:103](https://github.com/alicevision/Meshroom/blob/d787a6bf29f5e318f0e32d22d6e7109b065dad4c/localfarm/test.py#L103)
- [meshroom/nodes/general/scripts/extractMeshroomSceneParams.py:127](https://github.com/alicevision/Meshroom/blob/d787a6bf29f5e318f0e32d22d6e7109b065dad4c/meshroom/nodes/general/scripts/extractMeshroomSceneParams.py#L127)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: PlatformExecutable. |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). Observed top-level functions: run. |
| docker package | library | Observed | Groups 9 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 6 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: FarmLauncher, FileStatus, Job, LocalFarmEngine, LocalFarmRequestHandler, MeshroomApp. Obse… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| localfarm package | library | Observed | Groups 2 file(s) under localfarm package (observed from repository paths and static analysis). Observed top-level classes: Job, LocalFarmClient, LocalFarmClientContext, Task. Observed top-level functions: test. |
| meshroom package | library | Observed | Groups 62 file(s) under meshroom package (observed from repository paths and static analysis). Observed top-level classes: ActiveNode, AddAttributeKeyValueCommand, AddEdgeCommand, AddNodeCommand, AnySetNode, Backdrop. O… |
| Service / domain layer | service | Observed | Groups 52 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AVCommandLineNode, AnySet, ArchivePluginProvider, Attribute, AttributeValidator, BackdropN… |
| Tests | test | Observed | Groups 65 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AllAttributesNode, AppendFiles, AppendText, Color, ConnectedNodeV1, ConnectedNodeV2. Observed top-level fun… |

## Important files

- `.claude/settings.json` (config)
- `.codecov.yml` (config)
- `.github/FUNDING.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/build-binary.yml` (ci)
- `.github/workflows/build-pyside6-linux.yml` (ci)
- `.github/workflows/continuous-integration.yml` (ci)
- `.github/workflows/nightly.yml` (ci)
- `.github/workflows/run-tests.yml` (ci)
- `.readthedocs.yaml` (config)
- `.vscode/launch.json` (config)
- `docker/Dockerfile` (container)
- `docker/Dockerfile_rocky_deps` (container)
- `docker/Dockerfile_ubuntu_deps` (container)
- `docs/requirements.txt` (manifest)
- `meshroom/core/plugins/registries/meshroomHub.json` (config)
- `meshroom/nodes/general/pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `meshroom` — 319 analysed file(s)
- `tests` — 65 analysed file(s)
- `(root files)` — 25 analysed file(s)
- `docs` — 16 analysed file(s)
- `.github` — 15 analysed file(s)
- `docker` — 12 analysed file(s)
- `bin` — 10 analysed file(s)
- `localfarm` — 6 analysed file(s)
- `.claude` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `d787a6bf29f5e318f0e32d22d6e7109b065dad4c` is the revision these paths and observations refer to.
