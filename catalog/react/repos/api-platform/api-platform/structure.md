# Project structure: api-platform/api-platform

**Analysed commit:** `fa951e6b2fc161306bf195891429b9ba7a769ae4`

**Commit reference:** [fa951e6b2fc161306bf195891429b9ba7a769ae4](https://github.com/api-platform/api-platform/commit/fa951e6b2fc161306bf195891429b9ba7a769ae4)

**Tree at this commit:** [api-platform/api-platform@fa951e6b2fc1](https://github.com/api-platform/api-platform/tree/fa951e6b2fc161306bf195891429b9ba7a769ae4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | api-platform/api-platform |
| Description | 🕸️ Create REST and GraphQL APIs, scaffold Jamstack webapps, stream changes in real-time. |
| Stars | 9201 |
| Forks | 967 |
| Licence | MIT |
| Language | PHP |
| Default branch | main |
| Analysed commit | `fa951e6b2fc161306bf195891429b9ba7a769ae4` |
| Retrieved at | 2026-11-14T19:13:35.394764+00:00 |
| Files in this snapshot | 64 |

## Directory tree

```text
.devcontainer/  (2 files)
  devcontainer.json
  post-create.sh
.github/  (8 files)
  scripts/  (1 files)
    classify-issue.py
  workflows/  (5 files)
    ci.yml
    e2e.yml
    issue-core-transfer.yml
    release.yml
    symfony-docker-bump.yml
  CONTRIBUTING.md
  dependabot.yml
bin/  (1 files)
  api-platform
scripts/  (2 files)
  build-phar.php
  symfony-docker-pin.php
src/  (16 files)
  Scaffold/  (14 files)
    AdminRecipe.php
    AgentsScaffold.php
    ComposeOverrideWriter.php
    FileWriter.php
    LaravelAdminScaffold.php
    LaravelConfigPatcher.php
    LaravelScaffold.php
    NextPwaScaffold.php
    ProcessRunner.php
    ScaffoldOptions.php
    SymfonyAdminScaffold.php
    SymfonyDockerPin.php
    SymfonyScaffold.php
    ViteConfigPatcher.php
  InstallerCommand.php
  Templates.php
templates/  (13 files)
  Greetings.php
  admin-app.tsx
  admin-gitignore
  admin-index.html
  admin-main.tsx
  admin-package.json
  admin-tsconfig.json
  admin-vite.config.ts
  laravel-admin.blade.php
  laravel-resources.js
  laravel-welcome.blade.php
  pwa-page.tsx
  routes.yaml
tests/  (13 files)
  Scaffold/  (12 files)
    AgentsScaffoldTest.php
    ComposeOverrideWriterTest.php
    FileWriterTest.php
    LaravelAdminScaffoldTest.php
    LaravelConfigPatcherTest.php
    LaravelScaffoldTest.php
    NextPwaScaffoldTest.php
    ProcessRunnerTest.php
    SymfonyAdminScaffoldTest.php
    SymfonyDockerPinTest.php
    SymfonyScaffoldTest.php
    ViteConfigPatcherTest.php
  InstallerCommandTest.php
.editorconfig
.gitattributes
.gitignore
LICENSE
Makefile
README.md
composer.json
phpstan.neon.dist
phpunit.xml.dist
```

## Entry points

- [.github/scripts/classify-issue.py:167](https://github.com/api-platform/api-platform/blob/fa951e6b2fc161306bf195891429b9ba7a769ae4/.github/scripts/classify-issue.py#L167)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| InstallerCommand.php package | library | Observed | Groups 1 file(s) under installercommand.php package (observed from repository paths and static analysis). |
| Scaffold package | library | Observed | Groups 14 file(s) under scaffold package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| templates package | library | Observed | Groups 8 file(s) under templates package (observed from repository paths and static analysis). |
| Templates.php package | library | Observed | Groups 1 file(s) under templates.php package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 13 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/e2e.yml` (ci)
- `.github/workflows/issue-core-transfer.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/symfony-docker-bump.yml` (ci)
- `composer.json` (config)
- `templates/admin-package.json` (config)
- `templates/admin-tsconfig.json` (config)
- `templates/routes.yaml` (config)

## Top-level layout

- `src` — 16 analysed file(s)
- `templates` — 13 analysed file(s)
- `tests` — 13 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 8 analysed file(s)
- `.devcontainer` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `fa951e6b2fc161306bf195891429b9ba7a769ae4` is the revision these paths and observations refer to.
