# Project structure: ahujasid/mcp-for-blender

**Analysed commit:** `8f40787fbde8e6d8fe51c5a3553e5635fff40d2b`

**Commit reference:** [8f40787fbde8e6d8fe51c5a3553e5635fff40d2b](https://github.com/ahujasid/mcp-for-blender/commit/8f40787fbde8e6d8fe51c5a3553e5635fff40d2b)

**Tree at this commit:** [ahujasid/mcp-for-blender@8f40787fbde8](https://github.com/ahujasid/mcp-for-blender/tree/8f40787fbde8e6d8fe51c5a3553e5635fff40d2b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ahujasid/mcp-for-blender |
| Description | Community plugin to control Blender 3D with any LLM of your choice. Not affiliated with the official Blender Foundation. |
| Stars | 34429 |
| Forks | 3138 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `8f40787fbde8e6d8fe51c5a3553e5635fff40d2b` |
| Retrieved at | 2026-11-14T19:06:58.848984+00:00 |
| Files in this snapshot | 79 |

## Directory tree

```text
.claude-plugin/  (1 files)
  marketplace.json
assets/  (1 files)
  logo-banner.svg
integrations/  (8 files)
  claude/  (4 files)
    mcp-for-blender/  (4 files)
      … 4 files under this directory
  codex/  (4 files)
    .agents/  (1 files)
      … 1 files under this directory
    plugins/  (3 files)
      … 3 files under this directory
src/  (25 files)
  blender_mcp/  (25 files)
    apps/  (1 files)
      … 1 files under this directory
    bundled/  (1 files)
      … 1 files under this directory
    guides/  (7 files)
      … 7 files under this directory
    __init__.py
    addon_manager.py
    blender_scripts.py
    consent_prompt.py
    context_log.py
    generation.py
    guides.py
    openai_apps.py
    premium_hint.py
    safe_mode.py
    server.py
    setup_cli.py
    telemetry.py
    telemetry_decorator.py
    trajectory.py
    update_cli.py
tests/  (33 files)
  blender_bind_address_smoke.py
  conftest.py
  test_addon_autostart.py
  test_addon_compat.py
  test_addon_manager.py
  test_addon_updater.py
  test_claude_plugin.py
  test_compat_matrix.py
  test_connection_args.py
  test_consolidated_tools.py
  test_context_log.py
  test_export_scene.py
  test_generation.py
  test_hunyuan_api_profile.py
  test_hunyuan_import_security.py
  test_image_input_security.py
  test_look_telemetry.py
  test_meshy.py
  test_openai_apps.py
  test_polyhaven.py
  test_polypizza.py
  test_premium_guidance.py
  test_process_bbox_validation.py
  test_safe_mode.py
  … 9 more files
.dockerignore
.gitignore
.python-version
Dockerfile
LICENSE
README.md
TERMS_AND_CONDITIONS.md
install.ps1
install.sh
main.py
pyproject.toml
```

## Entry points

- [src/blender_mcp/server.py](https://github.com/ahujasid/mcp-for-blender/blob/8f40787fbde8e6d8fe51c5a3553e5635fff40d2b/src/blender_mcp/server.py)
- [main.py:7](https://github.com/ahujasid/mcp-for-blender/blob/8f40787fbde8e6d8fe51c5a3553e5635fff40d2b/main.py#L7)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| blender_mcp package | library | Observed | Groups 16 file(s) under blender_mcp package (observed from repository paths and static analysis). Observed top-level classes: AddonHandshake, AddonInstallResult, AddonOutcome, AddonStatusReport, AddonUpdate, Client. Obs… |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 2 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AddonTooOld, BlenderConnection, _LookRefused. Observed top-level functions: _addon_lacks,… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 33 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: CustomPropMixin, FakeAddon, FakeBlender, FakeCollection, FakeCollections, FakeColorspace. Observed top-leve… |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.dockerignore` (container)
- `Dockerfile` (container)
- `integrations/claude/mcp-for-blender/.claude-plugin/plugin.json` (config)
- `integrations/claude/mcp-for-blender/.mcp.json` (config)
- `integrations/codex/.agents/plugins/marketplace.json` (config)
- `integrations/codex/plugins/mcp-for-blender/.codex-plugin/plugin.json` (config)
- `integrations/codex/plugins/mcp-for-blender/.mcp.json` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `tests` — 33 analysed file(s)
- `src` — 25 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `integrations` — 8 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)
- `assets` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `8f40787fbde8e6d8fe51c5a3553e5635fff40d2b` is the revision these paths and observations refer to.
