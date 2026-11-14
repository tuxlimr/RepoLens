# Project structure: Fei-Away/Codex-Dream-Skin

**Analysed commit:** `6fc42df48a6a5365011f55cc349e20c038e56d1d`

**Commit reference:** [6fc42df48a6a5365011f55cc349e20c038e56d1d](https://github.com/Fei-Away/Codex-Dream-Skin/commit/6fc42df48a6a5365011f55cc349e20c038e56d1d)

**Tree at this commit:** [Fei-Away/Codex-Dream-Skin@6fc42df48a6a](https://github.com/Fei-Away/Codex-Dream-Skin/tree/6fc42df48a6a5365011f55cc349e20c038e56d1d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Fei-Away/Codex-Dream-Skin |
| Description | Codex Dream Skin |
| Stars | 15410 |
| Forks | 1395 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `6fc42df48a6a5365011f55cc349e20c038e56d1d` |
| Retrieved at | 2026-11-14T19:11:40.318093+00:00 |
| Files in this snapshot | 266 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (2 files)
    ci.yml
    release.yml
  CONTRIBUTING.en.md
  CONTRIBUTING.md
  pull_request_template.md
docs/  (26 files)
  images/  (2 files)
    dreamskin-mark.svg
    sponsor-passion8.svg
  releases/  (8 files)
    README.md
    v1.5.18.md
    v1.5.19-en.md
    v1.5.19.md
    v1.5.20-en.md
    v1.5.20.md
    v1.5.21-en.md
    v1.5.21.md
  validation/  (1 files)
    issues-427-429-windows.md
  PROJECT.md
  background-generation-prompts.md
  compat-26-930-windows-validation.md
  compat-profile-design.md
  handoff-2026-08-27.md
  install-macos.md
  install-windows.md
  platforms.md
  pr-324-windows-validation.md
  pr-351-windows-validation.md
  promo-copy.md
  reference-background-prompt-guide.en.md
  reference-background-prompt-guide.md
  theme-management.md
  windows-26-930-performance.md
macos/  (123 files)
  agents/  (1 files)
    openai.yaml
  assets/  (8 files)
    dream-skin.css
    renderer-inject.js
    safe-css-policy.json
    safe-css-validator.mjs
    selectors.json
    theme-package-validator.mjs
    theme-preferences.mjs
    theme.json
  client-delivery/  (2 files)
    使用说明.txt
    给 Codex 的部署提示词.md
  menubar/  (1 files)
    codex_dream_skin.10s.sh
  menubar-app/  (19 files)
    Resources/  (1 files)
      … 1 files under this directory
    Sources/  (12 files)
      … 12 files under this directory
    Tests/  (3 files)
      … 3 files under this directory
    Tools/  (1 files)
      … 1 files under this directory
    .gitignore
    Package.swift
  presets/  (3 files)
    preset-arina-hashimoto/  (1 files)
      … 1 files under this directory
    preset-gothic-void-crusade/  (1 files)
      … 1 files under this directory
    README.md
  references/  (5 files)
    acceptance-report-2026-07-15.md
    asset-provenance.md
    incident-review.md
    qa-inventory.md
    runtime-notes.md
  scripts/  (37 files)
    apply-community-theme-macos.sh
    apply-from-menubar-macos.sh
    build-client-release.sh
    build-dmg.sh
    build-menubar-app.sh
    build-release.sh
    check-image-dimensions.mjs
    check-update-macos.sh
    common-macos.sh
    customize-theme-macos.sh
    doctor-macos.sh
    extract-theme-zip-macos.sh
    generate-app-icon.sh
    image-metadata.mjs
    import-theme-zip-macos.sh
    injector.mjs
    install-dream-skin-macos.sh
    install-menubar-macos.sh
    load-image-theme-macos.sh
    localization-macos.sh
    pause-dream-skin-macos.sh
    prepare-standalone-docs.sh
    publish-theme-import.mjs
    recover-theme-imports-macos.sh
    … 13 more files
  tests/  (32 files)
    fixtures/  (2 files)
      … 2 files under this directory
    bounded-community-http.test.mjs
    bounded-community-http.test.swift
    community-apply-transaction.test.sh
    discovery-backoff.test.mjs
    image-metadata.test.mjs
    injector-bootstrap.test.mjs
    installer-preflight.test.sh
    localization-contract.test.mjs
    payload-template-integrity.test.mjs
    process-identity-locale.test.mjs
    release-workflow.test.mjs
    renderer-inject.test.mjs
    renderer-verification.test.mjs
    restart-cancellation.test.mjs
    run-tests.sh
    runtime-css-nested-has.test.mjs
    safe-css-validator.test.mjs
    shell-braced-vars-before-cjk.test.mjs
    theme-config.test.mjs
    theme-import-identity.test.sh
    theme-import-kill-hook.cjs
    theme-import-publish.test.mjs
    theme-package-validator.test.mjs
    theme-stage.test.mjs
    … 6 more files
  .gitignore
  CHANGELOG.md
  CLIENT_DEPLOY_PROMPT.md
  Customize Codex Dream Skin.command
  Install Codex Dream Skin.command
  Install Menu Bar.command
  LICENSE
  NOTICE.md
  README.md
  Restore Codex Dream Skin.command
  SKILL.md
  Start Codex Dream Skin.command
  VERSION
  Verify Codex Dream Skin.command
  package.json
runtime/  (8 files)
  dream-skin.css
  image-metadata.mjs
  renderer-inject.js
  safe-css-policy.json
  safe-css-validator.mjs
  theme-package-validator.mjs
  theme-preferences.mjs
  validate-safe-css-file.mjs
tools/  (18 files)
  active-page-verification.test.mjs
  build-theme-manager.mjs
  capture-dom-fixture.mjs
  check-selector-provenance.mjs
  check-selector-provenance.test.mjs
  css-predicate-cache.mjs
  css-predicate-cache.test.mjs
  doctor-selectors.mjs
  doctor-selectors.test.mjs
  renderer-runtime.test.mjs
  selectors.json
  sync-runtime-assets.mjs
  theme-preferences.test.mjs
  windows-home-css.mjs
  windows-home-css.test.mjs
  windows-motion-css.mjs
  windows-motion-css.test.mjs
  windows-shell.css
windows/  (75 files)
  agents/  (1 files)
    openai.yaml
  assets/  (8 files)
    dream-skin.css
    renderer-inject.js
    safe-css-policy.json
    safe-css-validator.mjs
    selectors.json
    theme-package-validator.mjs
    theme-preferences.mjs
    theme.json
  installer/  (6 files)
    languages/  (2 files)
      … 2 files under this directory
    build-release.ps1
    codex-dream-skin.iss
    node-runtime.json
    setup-bootstrap.ps1
  presets/  (1 files)
    preset-gothic-void-crusade/  (1 files)
      … 1 files under this directory
  references/  (2 files)
    qa-inventory.md
    runtime-notes.md
  scripts/  (14 files)
    apply-community-theme.ps1
    check-update.ps1
    common-windows.ps1
    config-utf8.ps1
    image-metadata.mjs
    injector.mjs
    install-dream-skin.ps1
    localization-windows.ps1
    restore-dream-skin.ps1
    start-dream-skin.ps1
    theme-windows.ps1
    tray-dream-skin.ps1
    validate-safe-css-file.mjs
    verify-dream-skin.ps1
  tests/  (24 files)
    background-replacement-contract.test.mjs
    codex-home.tests.ps1
    community-theme-link.tests.ps1
    config-startup-rollback.tests.ps1
    image-metadata.test.mjs
    injector-bootstrap.test.mjs
    injector-one-shot.test.mjs
    injector-window-readiness.test.mjs
    installer-static.tests.ps1
    localization-contract.test.mjs
    native-stderr.tests.ps1
    payload-template-integrity.test.mjs
    renderer-inject.test.mjs
    run-tests.ps1
    start-cdp-failure-appearance-recovery.tests.ps1
    start-post-launch-appearance-recovery.tests.ps1
    start-renderer-readiness.tests.ps1
    start-result-contract.tests.ps1
    start-verified-skin-preserved.tests.ps1
    theme-manager-maintenance.tests.ps1
    theme-path-containment.test.mjs
    theme-schema-contract.test.mjs
    theme-zip-import.tests.ps1
    tray-apply-result.tests.ps1
  theme-manager/  (14 files)
    App/  (6 files)
      … 6 files under this directory
    Core/  (2 files)
      … 2 files under this directory
    NativeTests/  (2 files)
      … 2 files under this directory
    Tests/  (2 files)
      … 2 files under this directory
    .gitignore
    README.md
  CHANGELOG.md
  README.en.md
  README.md
  SKILL.md
  VERSION
.editorconfig
.gitattributes
.gitignore
AGENTS.md
LICENSE
README.md
README.zh-CN.md
SECURITY.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 15 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| macos package | library | Observed | Groups 42 file(s) under macos package (observed from repository paths and static analysis). |
| runtime package | library | Observed | Groups 6 file(s) under runtime package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 61 file(s) under tests (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 16 file(s) under tools package (observed from repository paths and static analysis). |
| windows package | library | Observed | Groups 12 file(s) under windows package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `macos/agents/openai.yaml` (config)
- `macos/assets/safe-css-policy.json` (config)
- `macos/assets/selectors.json` (config)
- `macos/assets/theme.json` (config)
- `macos/package.json` (manifest)
- `macos/presets/preset-arina-hashimoto/theme.json` (config)
- `macos/presets/preset-gothic-void-crusade/theme.json` (config)
- `runtime/safe-css-policy.json` (config)
- `tools/selectors.json` (config)
- `windows/agents/openai.yaml` (config)
- `windows/assets/safe-css-policy.json` (config)
- `windows/assets/selectors.json` (config)
- `windows/assets/theme.json` (config)
- `windows/installer/node-runtime.json` (config)
- `windows/presets/preset-gothic-void-crusade/theme.json` (config)

## Top-level layout

- `macos` — 123 analysed file(s)
- `windows` — 75 analysed file(s)
- `docs` — 26 analysed file(s)
- `tools` — 18 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 8 analysed file(s)
- `runtime` — 8 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6fc42df48a6a5365011f55cc349e20c038e56d1d` is the revision these paths and observations refer to.
