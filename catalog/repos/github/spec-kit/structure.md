# Project structure: github/spec-kit

**Analysed commit:** `2ee2b1e8005905db05f5717300a469b3068b908f`

**Commit reference:** [2ee2b1e8005905db05f5717300a469b3068b908f](https://github.com/github/spec-kit/commit/2ee2b1e8005905db05f5717300a469b3068b908f)

**Tree at this commit:** [github/spec-kit@2ee2b1e80059](https://github.com/github/spec-kit/tree/2ee2b1e8005905db05f5717300a469b3068b908f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | github/spec-kit |
| Description | 💫 Toolkit to help you get started with SDD or any other process! |
| Stars | 149786 |
| Forks | 13450 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `2ee2b1e8005905db05f5717300a469b3068b908f` |
| Retrieved at | 2026-11-14T19:06:02.670057+00:00 |
| Files in this snapshot | 717 |

## Directory tree

```text
.devcontainer/  (2 files)
  devcontainer.json
  post-create.sh
.github/  (48 files)
  ISSUE_TEMPLATE/  (8 files)
    agent_request.yml
    bug_report.yml
    bundle_submission.yml
    config.yml
    extension_submission.yml
    feature_request.yml
    preset_submission.yml
    workflow_step_submission.yml
  aw/  (1 files)
    actions-lock.json
  scripts/  (4 files)
    check_extension_version_bump.py
    check_security_requirements.py
    validate_community_preset.py
    validate_community_workflow_step.py
  skills/  (2 files)
    add-community-extension/  (1 files)
      … 1 files under this directory
    code-review/  (1 files)
      … 1 files under this directory
  workflows/  (29 files)
    RELEASE-PROCESS.md
    add-community-bundle.lock.yml
    add-community-bundle.md
    add-community-extension.lock.yml
    add-community-extension.md
    add-community-preset.lock.yml
    add-community-preset.md
    add-community-workflow-step.lock.yml
    add-community-workflow-step.md
    bug-assess.lock.yml
    bug-assess.md
    bug-fix.lock.yml
    bug-fix.md
    bug-test.lock.yml
    bug-test.md
    catalog-assign.yml
    codeql.yml
    docs.yml
    extension-version-guard.yml
    feature-assess.lock.yml
    feature-assess.md
    lint.yml
    pr-assess.lock.yml
    pr-assess.md
    … 5 more files
  CODEOWNERS
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  security-audit-requirements.txt
.specify/  (1 files)
  memory/  (1 files)
    constitution.md
bundles/  (6 files)
  assess/  (2 files)
    README.md
    bundle.yml
  bugfix/  (2 files)
    README.md
    bundle.yml
  catalog.community.json
  catalog.json
design/  (8 files)
  catalogs.md
  cli.md
  extension.md
  file-helper.md
  integration.md
  mcp.md
  shared.md
  workflow-step.md
docs/  (128 files)
  bundles/  (6 files)
    api.md
    catalogs.md
    cli.md
    developing.md
    overview.md
    publishing.md
  community/  (9 files)
    bundles.md
    extensions.md
    friends.md
    integrations.md
    overview.md
    presets.md
    walkthroughs.md
    workflow-steps.md
    workflows.md
  extensions/  (6 files)
    api.md
    catalogs.md
    cli.md
    developing.md
    overview.md
    publishing.md
  guides/  (3 files)
    agentic-sdlc.md
    assessment.md
    bugfix.md
  how-to/  (11 files)
    complex-features.md
    contract-driven-development.md
    customization.md
    evolving-specs.md
    existing-projects.md
    index.md
    local-development.md
    monorepo.md
    persisting-specs.md
    sdd.md
    spec-of-specs.md
  install/  (5 files)
    air-gapped.md
    one-time.md
    pipx.md
    pypi.md
    uv.md
  integrations/  (48 files)
    agy.md
    alquimia.md
    amp.md
    api.md
    auggie.md
    bob.md
    catalog.md
    claude.md
    cli.md
    cline.md
    codebuddy.md
    codex.md
    command-code.md
    contributing.md
    copilot.md
    cursor-agent.md
    devin.md
    docker-agent.md
    droid.md
    dsh.md
    firebender.md
    forge.md
    gemini.md
    generic.md
    … 24 more files
  overview/  (5 files)
    artifacts.md
    catalogs.md
    core.md
    history.md
    mcp.md
  presets/  (6 files)
    api.md
    catalogs.md
    cli.md
    developing.md
    overview.md
    publishing.md
  reference/  (4 files)
    agentic-assessment.md
    agentic-bugfix.md
    agentic-sdd.md
    authentication.md
  template/  (1 files)
    public/  (1 files)
      … 1 files under this directory
  workflow-steps/  (7 files)
    api.md
    catalogs.md
    cli.md
    developing.md
    overview.md
    publishing.md
    types.md
  workflows/  (9 files)
    api.md
    catalogs.md
    cli.md
    developing.md
    expressions.md
    functions.md
    overlays.md
    overview.md
    publishing.md
  .gitignore
  README.md
  docfx.json
  index.md
  installation.md
  quickstart.md
  toc.yml
  upgrade.md
extensions/  (59 files)
  agent-context/  (8 files)
    commands/  (1 files)
      … 1 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    README.md
    agent-context-config.yml
    agent-context-defaults.json
    extension.yml
  assess/  (7 files)
    commands/  (5 files)
      … 5 files under this directory
    README.md
    extension.yml
  bug/  (5 files)
    commands/  (3 files)
      … 3 files under this directory
    README.md
    extension.yml
  git/  (21 files)
    commands/  (5 files)
      … 5 files under this directory
    scripts/  (12 files)
      … 12 files under this directory
    README.md
    config-template.yml
    extension.yml
    git-config.yml
  github/  (6 files)
    commands/  (1 files)
      … 1 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    README.md
    extension.yml
  selftest/  (2 files)
    commands/  (1 files)
      … 1 files under this directory
    extension.yml
  template/  (8 files)
    commands/  (1 files)
      … 1 files under this directory
    .gitignore
    CHANGELOG.md
    EXAMPLE-README.md
    LICENSE
    README.md
    config-template.yml
    extension.yml
  README.md
  catalog.json
integrations/  (2 files)
  catalog.community.json
  catalog.json
newsletters/  (9 files)
  2026-April.md
  2026-August.md
  2026-February.md
  2026-July.md
  2026-June.md
  2026-March.md
  2026-May.md
  2026-October.md
  2026-September.md
presets/  (27 files)
  constitution-sync/  (3 files)
    commands/  (1 files)
      … 1 files under this directory
    README.md
    preset.yml
  lean/  (7 files)
    commands/  (5 files)
      … 5 files under this directory
    README.md
    preset.yml
  scaffold/  (6 files)
    commands/  (2 files)
      … 2 files under this directory
    templates/  (2 files)
      … 2 files under this directory
    README.md
    preset.yml
  self-test/  (8 files)
    commands/  (2 files)
      … 2 files under this directory
    templates/  (5 files)
      … 5 files under this directory
    preset.yml
  README.md
  catalog.community.json
  catalog.json
scripts/  (18 files)
  bash/  (6 files)
    check-prerequisites.sh
    common.sh
    create-new-feature.sh
    resolve-template.sh
    setup-plan.sh
    setup-tasks.sh
  powershell/  (6 files)
    check-prerequisites.ps1
    common.ps1
    create-new-feature.ps1
    resolve-template.ps1
    setup-plan.ps1
    setup-tasks.ps1
  python/  (6 files)
    check_prerequisites.py
    common.py
    create_new_feature.py
    resolve_template.py
    setup_plan.py
    setup_tasks.py
src/  (305 files)
  specify_cli/  (305 files)
    artifacts/  (14 files)
      … 14 files under this directory
    authentication/  (8 files)
      … 8 files under this directory
    bundles/  (36 files)
      … 36 files under this directory
    events/  (2 files)
      … 2 files under this directory
    extensions/  (19 files)
      … 19 files under this directory
    integrations/  (70 files)
      … 70 files under this directory
    mcp_server/  (5 files)
      … 5 files under this directory
    presets/  (24 files)
      … 24 files under this directory
    selfs/  (3 files)
      … 3 files under this directory
    workflows/  (93 files)
      … 93 files under this directory
    __init__.py
    _agent_config.py
    _assets.py
    _console.py
    _download_security.py
    _file_handles.py
    _file_policy.py
    _init_options.py
    _install_ignore.py
    _installed_info_json.py
    _installed_list_json.py
    _invocation_style.py
    _operation_version.py
    _project.py
    _toml_string.py
    _utils.py
    _version.py
    _windows_abi.py
    agents.py
    bundler.py
    catalogs.py
    command_check.py
    command_init.py
    command_mcp.py
    … 7 more files
templates/  (15 files)
  commands/  (9 files)
    analyze.md
    checklist.md
    clarify.md
    constitution.md
    converge.md
    implement.md
    plan.md
    specify.md
    tasks.md
  checklist-template.md
  constitution-template.md
  plan-template.md
  spec-template.md
  tasks-template.md
  vscode-settings.json
tests/  (67 files)
  contract/  (9 files)
    test_bundled_extension_update_delivery.py
    test_bundled_extension_versions.py
    test_catalog_schema.py
    test_extension_version_guard_script.py
    test_firstparty_bundle_catalog_consistency.py
    test_manifest_schema.py
    test_wheel_bundled_presets.py
    test_wheel_bundled_workflows.py
    test_wheel_core_pack_scripts.py
  extensions/  (15 files)
    assess/  (2 files)
      … 2 files under this directory
    bug/  (3 files)
      … 3 files under this directory
    git/  (3 files)
      … 3 files under this directory
    github/  (2 files)
      … 2 files under this directory
    __init__.py
    test_agent_context_cli_free.py
    test_extension_agent_context.py
    test_update_agent_context_feature_json.py
    test_update_agent_context_python_parity.py
  hooks/  (5 files)
    .specify/  (1 files)
      … 1 files under this directory
    TESTING.md
    plan.md
    spec.md
    tasks.md
  integration/  (1 files)
    test_preset_update_workflow.py
  integrations/  (29 files)
    __init__.py
    conftest.py
    test_base.py
    test_capture.py
    test_cli.py
    test_extra_args.py
    test_home_isolation.py
    test_integration_agy.py
    test_integration_alquimia.py
    test_integration_amp.py
    test_integration_auggie.py
    test_integration_base_markdown.py
    test_integration_base_skills.py
    test_integration_base_toml.py
    test_integration_base_yaml.py
    test_integration_bob.py
    test_integration_characterization.py
    test_integration_claude.py
    test_integration_cline.py
    test_integration_codebuddy.py
    test_integration_codex.py
    test_integration_command_code.py
    test_integration_copilot.py
    test_integration_cursor_agent.py
    … 5 more files
  specify_cli/  (5 files)
    bundles/  (2 files)
      … 2 files under this directory
    workflows/  (2 files)
      … 2 files under this directory
    __init__.py
  __init__.py
  conftest.py
  http_helpers.py
.editorconfig
.gitattributes
.gitignore
.markdownlint-cli2.jsonc
.pre-commit-config.yaml
.zenodo.json
AGENTS.md
CHANGELOG.md
CITATION.cff
CODE_OF_CONDUCT.md
CONTRIBUTING.md
DEVELOPMENT.md
LICENSE
README.ja.md
README.ko.md
README.md
README.zh-CN.md
SECURITY.md
SUPPORT.md
pyproject.toml
spec-driven.md
spec-kit.code-workspace
```

## Entry points

- [src/specify_cli/__init__.py](https://github.com/github/spec-kit/blob/2ee2b1e8005905db05f5717300a469b3068b908f/src/specify_cli/__init__.py)
- [src/specify_cli/artifacts/_commands.py:23](https://github.com/github/spec-kit/blob/2ee2b1e8005905db05f5717300a469b3068b908f/src/specify_cli/artifacts/_commands.py#L23)
- [src/specify_cli/artifacts/command_info.py:40](https://github.com/github/spec-kit/blob/2ee2b1e8005905db05f5717300a469b3068b908f/src/specify_cli/artifacts/command_info.py#L40)
- [src/specify_cli/artifacts/command_list.py:35](https://github.com/github/spec-kit/blob/2ee2b1e8005905db05f5717300a469b3068b908f/src/specify_cli/artifacts/command_list.py#L35)
- [src/specify_cli/artifacts/command_lookup.py:21](https://github.com/github/spec-kit/blob/2ee2b1e8005905db05f5717300a469b3068b908f/src/specify_cli/artifacts/command_lookup.py#L21)
- [src/specify_cli/bundles/_commands.py:24](https://github.com/github/spec-kit/blob/2ee2b1e8005905db05f5717300a469b3068b908f/src/specify_cli/bundles/_commands.py#L24)
- [src/specify_cli/bundles/catalog/__init__.py:7](https://github.com/github/spec-kit/blob/2ee2b1e8005905db05f5717300a469b3068b908f/src/specify_cli/bundles/catalog/__init__.py#L7)
- [src/specify_cli/bundles/catalog/command_add.py:16](https://github.com/github/spec-kit/blob/2ee2b1e8005905db05f5717300a469b3068b908f/src/specify_cli/bundles/catalog/command_add.py#L16)
- [src/specify_cli/bundles/catalog/command_list.py:15](https://github.com/github/spec-kit/blob/2ee2b1e8005905db05f5717300a469b3068b908f/src/specify_cli/bundles/catalog/command_list.py#L15)
- [src/specify_cli/bundles/catalog/command_remove.py:16](https://github.com/github/spec-kit/blob/2ee2b1e8005905db05f5717300a469b3068b908f/src/specify_cli/bundles/catalog/command_remove.py#L16)
- [src/specify_cli/bundles/command_add.py:12](https://github.com/github/spec-kit/blob/2ee2b1e8005905db05f5717300a469b3068b908f/src/specify_cli/bundles/command_add.py#L12)
- [src/specify_cli/bundles/command_build.py:16](https://github.com/github/spec-kit/blob/2ee2b1e8005905db05f5717300a469b3068b908f/src/specify_cli/bundles/command_build.py#L16)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 28 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AuthConfigEntry. Observed top-level functions: _default_config_path, _host_matches_p… |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AmbiguousArtifactError, Artifact, ArtifactError, ArtifactNotFoundError, ArtifactResolutionError, Contri… |
| Application entry point | entrypoint | Observed | Groups 30 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Typer. Observed top-level classes: Args, EventRefreshError, _ResponseBudget,… |
| extensions package | library | Observed | Groups 7 file(s) under extensions package (observed from repository paths and static analysis). Observed top-level functions: check_feature_branch, effective_branch_name, has_git. |
| External integrations | external | Observed | Groups 68 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AgyIntegration, AlquimiaAIIntegration, AmpIntegration, AuggieIntegration, BobIntegration, C… |
| scripts package | library | Observed | Groups 7 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: FeaturePaths, TemplateResolutionError, _DelegatedYAML, _DelegatedYAMLError, _NonNativeYAMLValue. O… |
| specify_cli package | library | Observed | Groups 215 file(s) under specify_cli package (observed from repository paths and static analysis). Observed top-level classes: ArchiveHooks, ArchiveRequest, ArtifactCatalog, ArtifactInfoAmbiguousError, ArtifactInfoError… |
| Tests | test | Observed | Groups 67 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: MarkdownIntegrationTests, SkillsIntegrationTests, StubIntegration, TestAgyBuildExecArgs, TestAgyHookCommand… |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/agent_request.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/bundle_submission.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/extension_submission.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/preset_submission.yml` (config)
- `.github/ISSUE_TEMPLATE/workflow_step_submission.yml` (config)
- `.github/aw/actions-lock.json` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/RELEASE-PROCESS.md` (ci)
- `.github/workflows/add-community-bundle.lock.yml` (ci)
- `.github/workflows/add-community-bundle.md` (ci)
- `.github/workflows/add-community-extension.lock.yml` (ci)
- `.github/workflows/add-community-extension.md` (ci)
- `.github/workflows/add-community-preset.lock.yml` (ci)
- `.github/workflows/add-community-preset.md` (ci)
- `.github/workflows/add-community-workflow-step.lock.yml` (ci)
- `.github/workflows/add-community-workflow-step.md` (ci)
- `.github/workflows/bug-assess.lock.yml` (ci)
- `.github/workflows/bug-assess.md` (ci)
- `.github/workflows/bug-fix.lock.yml` (ci)
- `.github/workflows/bug-fix.md` (ci)
- `.github/workflows/bug-test.lock.yml` (ci)
- `.github/workflows/bug-test.md` (ci)
- `.github/workflows/catalog-assign.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/extension-version-guard.yml` (ci)
- `.github/workflows/feature-assess.lock.yml` (ci)
- `.github/workflows/feature-assess.md` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/pr-assess.lock.yml` (ci)
- `.github/workflows/pr-assess.md` (ci)
- `.github/workflows/publish-pypi.yml` (ci)
- `.github/workflows/release-trigger.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.zenodo.json` (config)
- `bundles/assess/bundle.yml` (config)
- `bundles/bugfix/bundle.yml` (config)
- `bundles/catalog.community.json` (config)
- `bundles/catalog.json` (config)
- `docs/docfx.json` (config)
- `docs/toc.yml` (config)
- `extensions/agent-context/agent-context-config.yml` (config)
- `extensions/agent-context/agent-context-defaults.json` (config)
- `extensions/agent-context/extension.yml` (config)
- `extensions/assess/extension.yml` (config)
- `extensions/bug/extension.yml` (config)
- `extensions/catalog.json` (config)
- `extensions/git/config-template.yml` (config)
- `extensions/git/extension.yml` (config)
- `extensions/git/git-config.yml` (config)
- `extensions/github/extension.yml` (config)
- `extensions/selftest/extension.yml` (config)
- `extensions/template/config-template.yml` (config)
- `extensions/template/extension.yml` (config)
- `integrations/catalog.community.json` (config)
- `integrations/catalog.json` (config)
- `presets/catalog.community.json` (config)
- `presets/catalog.json` (config)
- `presets/constitution-sync/preset.yml` (config)
- `presets/lean/preset.yml` (config)
- `presets/scaffold/preset.yml` (config)
- `presets/self-test/preset.yml` (config)
- `pyproject.toml` (manifest)
- `templates/vscode-settings.json` (config)

## Top-level layout

- `src` — 305 analysed file(s)
- `docs` — 128 analysed file(s)
- `tests` — 67 analysed file(s)
- `extensions` — 59 analysed file(s)
- `.github` — 48 analysed file(s)
- `presets` — 27 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `scripts` — 18 analysed file(s)
- `templates` — 15 analysed file(s)
- `newsletters` — 9 analysed file(s)
- `design` — 8 analysed file(s)
- `bundles` — 6 analysed file(s)
- `.devcontainer` — 2 analysed file(s)
- `integrations` — 2 analysed file(s)
- `.specify` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `2ee2b1e8005905db05f5717300a469b3068b908f` is the revision these paths and observations refer to.
