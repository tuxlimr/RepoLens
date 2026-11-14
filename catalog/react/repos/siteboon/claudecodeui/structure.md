# Project structure: siteboon/claudecodeui

**Analysed commit:** `7943e285fc814a54d5549a34b90fac0805135a24`

**Commit reference:** [7943e285fc814a54d5549a34b90fac0805135a24](https://github.com/siteboon/claudecodeui/commit/7943e285fc814a54d5549a34b90fac0805135a24)

**Tree at this commit:** [siteboon/claudecodeui@7943e285fc81](https://github.com/siteboon/claudecodeui/tree/7943e285fc814a54d5549a34b90fac0805135a24)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | siteboon/claudecodeui |
| Description | Use Claude Code, OpenCode, Cursor CLI, and Codex on mobile and web with CloudCLI (aka Claude Code UI). CloudCLI is a free open source webui/GUI that helps you manage your Claude Code session and projects remotely. |
| Stars | 14611 |
| Forks | 2132 |
| Licence | AGPL-3.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `7943e285fc814a54d5549a34b90fac0805135a24` |
| Retrieved at | 2026-11-14T19:13:17.190623+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.agents/  (4 files)
  skills/  (4 files)
    backend-module-standards/  (2 files)
      … 2 files under this directory
    frontend-module-standards/  (2 files)
      … 2 files under this directory
.github/  (9 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (7 files)
    desktop-linux-branch-build.yml
    desktop-macos-branch-build.yml
    desktop-release.yml
    desktop-windows-branch-build.yml
    discord-release.yml
    docker.yml
    release.yml
.husky/  (2 files)
  commit-msg
  pre-commit
docker/  (5 files)
  claude-code/  (1 files)
    Dockerfile
  codex/  (1 files)
    Dockerfile
  shared/  (2 files)
    install-cloudcli.sh
    start-cloudcli.sh
  README.md
docs/  (16 files)
  architecture/  (7 files)
    01-websocket-transport.md
    02-realtime-stream.md
    03-conversation-handoff.md
    04-message-store-and-lazy-loading.md
    05-scrolling.md
    06-tool-view.md
    README.md
  README.de.md
  README.id.md
  README.ja.md
  README.ko.md
  README.ru.md
  README.tr.md
  README.zh-CN.md
  README.zh-TW.md
  nginx-subpath-template.conf
electron/  (15 files)
  launcher/  (3 files)
    index.html
    launcher.css
    launcher.js
  scripts/  (3 files)
    generate-linux-icons.js
    generate-macos-icon.js
    logo-svg.js
  cloud.js
  desktopNotifications.js
  desktopWindow.js
  localServer.js
  main.js
  preload.cjs
  serverInstaller.js
  tabs.js
  viewHost.js
public/  (22 files)
  icons/  (14 files)
    claude-ai-icon.svg
    codex-white.svg
    codex.svg
    cursor-white.svg
    cursor.svg
    icon-128x128.svg
    icon-144x144.svg
    icon-152x152.svg
    icon-192x192.svg
    icon-384x384.svg
    icon-512x512.svg
    icon-72x72.svg
    icon-96x96.svg
    icon-template.svg
  api-docs.html
  clear-cache.html
  convert-icons.md
  favicon.svg
  generate-icons.js
  logo.svg
  manifest.json
  sw.js
redirect-package/  (4 files)
  README.md
  bin.js
  index.js
  package.json
scripts/  (4 files)
  release/  (2 files)
    build-server-bundle.js
    prepare-desktop-app.js
  fix-node-pty.js
  promote-dist-server.mjs
server/  (325 files)
  modules/  (307 files)
    agent/  (5 files)
      … 5 files under this directory
    assets/  (4 files)
      … 4 files under this directory
    auth/  (6 files)
      … 6 files under this directory
    browser-use/  (8 files)
      … 8 files under this directory
    cli/  (8 files)
      … 8 files under this directory
    commands/  (5 files)
      … 5 files under this directory
    database/  (26 files)
      … 26 files under this directory
    file-tree/  (6 files)
      … 6 files under this directory
    git/  (10 files)
      … 10 files under this directory
    notifications/  (10 files)
      … 10 files under this directory
    plugins/  (9 files)
      … 9 files under this directory
    projects/  (16 files)
      … 16 files under this directory
    providers/  (120 files)
      … 120 files under this directory
    scheduled-messages/  (5 files)
      … 5 files under this directory
    settings/  (5 files)
      … 5 files under this directory
    system/  (5 files)
      … 5 files under this directory
    taskmaster/  (6 files)
      … 6 files under this directory
    user/  (6 files)
      … 6 files under this directory
    voice/  (5 files)
      … 5 files under this directory
    websocket/  (24 files)
      … 24 files under this directory
    worktrees/  (18 files)
      … 18 files under this directory
  shared/  (15 files)
    tests/  (7 files)
      … 7 files under this directory
    claude-cli-path.ts
    frontmatter.ts
    image-attachments.ts
    index.ts
    interfaces.ts
    message-unification.ts
    types.ts
    utils.ts
  index.ts
  load-env.ts
  tsconfig.json
shared/  (1 files)
  networkHosts.js
src/  (375 files)
  modules/  (372 files)
    auth/  (11 files)
      … 11 files under this directory
    browser-use/  (3 files)
      … 3 files under this directory
    chat/  (200 files)
      … 200 files under this directory
    code-editor/  (26 files)
      … 26 files under this directory
    command-palette/  (10 files)
      … 10 files under this directory
    file-tree/  (24 files)
      … 24 files under this directory
    git-panel/  (32 files)
      … 32 files under this directory
    i18n/  (66 files)
      … 66 files under this directory
  App.tsx
  index.css
  main.tsx
.env.example
.gitignore
.gitmodules
.npmignore
.nvmrc
.oxlintrc.json
.release-it.json
AGENTS.md
CHANGELOG.md
CONTRIBUTING.md
LICENSE
NOTICE
README.md
commitlint.config.js
index.html
package.json
postcss.config.js
release.sh
```

## Entry points

- [redirect-package/index.js](https://github.com/siteboon/claudecodeui/blob/7943e285fc814a54d5549a34b90fac0805135a24/redirect-package/index.js)
- [redirect-package/bin.js](https://github.com/siteboon/claudecodeui/blob/7943e285fc814a54d5549a34b90fac0805135a24/redirect-package/bin.js)
- [electron/main.js](https://github.com/siteboon/claudecodeui/blob/7943e285fc814a54d5549a34b90fac0805135a24/electron/main.js)
- [server/index.ts](https://github.com/siteboon/claudecodeui/blob/7943e285fc814a54d5549a34b90fac0805135a24/server/index.ts)
- [server/modules/agent/index.ts](https://github.com/siteboon/claudecodeui/blob/7943e285fc814a54d5549a34b90fac0805135a24/server/modules/agent/index.ts)
- [server/modules/assets/index.ts](https://github.com/siteboon/claudecodeui/blob/7943e285fc814a54d5549a34b90fac0805135a24/server/modules/assets/index.ts)
- [server/modules/auth/index.ts](https://github.com/siteboon/claudecodeui/blob/7943e285fc814a54d5549a34b90fac0805135a24/server/modules/auth/index.ts)
- [server/modules/browser-use/index.ts](https://github.com/siteboon/claudecodeui/blob/7943e285fc814a54d5549a34b90fac0805135a24/server/modules/browser-use/index.ts)
- [server/modules/cli/index.ts](https://github.com/siteboon/claudecodeui/blob/7943e285fc814a54d5549a34b90fac0805135a24/server/modules/cli/index.ts)
- [server/modules/commands/index.ts](https://github.com/siteboon/claudecodeui/blob/7943e285fc814a54d5549a34b90fac0805135a24/server/modules/commands/index.ts)
- [server/modules/database/index.ts](https://github.com/siteboon/claudecodeui/blob/7943e285fc814a54d5549a34b90fac0805135a24/server/modules/database/index.ts)
- [server/modules/file-tree/index.ts](https://github.com/siteboon/claudecodeui/blob/7943e285fc814a54d5549a34b90fac0805135a24/server/modules/file-tree/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| App.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 74 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 21 file(s) under data layer (observed from repository paths and static analysis). |
| docker package | library | Observed | Groups 2 file(s) under docker package (observed from repository paths and static analysis). |
| electron package | library | Observed | Groups 13 file(s) under electron package (observed from repository paths and static analysis). |
| main.tsx package | library | Observed | Groups 1 file(s) under main.tsx package (observed from repository paths and static analysis). |
| modules package | library | Observed | Groups 207 file(s) under modules package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 2 file(s) under public package (observed from repository paths and static analysis). |
| redirect-package package | library | Observed | Groups 2 file(s) under redirect-package package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 124 file(s) under server package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 47 file(s) under service / domain layer (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 1 file(s) under shared package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 226 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.agents/skills/backend-module-standards/agents/openai.yaml` (config)
- `.agents/skills/frontend-module-standards/agents/openai.yaml` (config)
- `.env.example` (config)
- `.github/workflows/desktop-linux-branch-build.yml` (ci)
- `.github/workflows/desktop-macos-branch-build.yml` (ci)
- `.github/workflows/desktop-release.yml` (ci)
- `.github/workflows/desktop-windows-branch-build.yml` (ci)
- `.github/workflows/discord-release.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.oxlintrc.json` (config)
- `.release-it.json` (config)
- `docker/claude-code/Dockerfile` (container)
- `docker/codex/Dockerfile` (container)
- `package.json` (manifest)
- `public/manifest.json` (config)
- `redirect-package/package.json` (manifest)
- `server/tsconfig.json` (config)
- `src/modules/i18n/locales/cs/auth.json` (config)
- `src/modules/i18n/locales/cs/chat.json` (config)
- `src/modules/i18n/locales/cs/codeEditor.json` (config)
- `src/modules/i18n/locales/cs/common.json` (config)
- `src/modules/i18n/locales/cs/git.json` (config)
- `src/modules/i18n/locales/cs/settings.json` (config)
- `src/modules/i18n/locales/cs/sidebar.json` (config)
- `src/modules/i18n/locales/cs/tasks.json` (config)
- `src/modules/i18n/locales/de/auth.json` (config)
- `src/modules/i18n/locales/de/chat.json` (config)
- `src/modules/i18n/locales/de/codeEditor.json` (config)
- `src/modules/i18n/locales/de/common.json` (config)
- `src/modules/i18n/locales/de/settings.json` (config)
- `src/modules/i18n/locales/de/sidebar.json` (config)
- `src/modules/i18n/locales/de/tasks.json` (config)
- `src/modules/i18n/locales/en/auth.json` (config)
- `src/modules/i18n/locales/en/chat.json` (config)
- `src/modules/i18n/locales/en/codeEditor.json` (config)
- `src/modules/i18n/locales/en/common.json` (config)
- `src/modules/i18n/locales/en/git.json` (config)
- `src/modules/i18n/locales/en/settings.json` (config)
- `src/modules/i18n/locales/en/sidebar.json` (config)
- `src/modules/i18n/locales/en/tasks.json` (config)
- `src/modules/i18n/locales/es/auth.json` (config)
- `src/modules/i18n/locales/es/chat.json` (config)
- `src/modules/i18n/locales/es/codeEditor.json` (config)
- `src/modules/i18n/locales/es/common.json` (config)
- `src/modules/i18n/locales/es/git.json` (config)
- `src/modules/i18n/locales/es/settings.json` (config)
- `src/modules/i18n/locales/es/sidebar.json` (config)
- `src/modules/i18n/locales/es/tasks.json` (config)
- `src/modules/i18n/locales/fr/auth.json` (config)
- `src/modules/i18n/locales/fr/chat.json` (config)
- `src/modules/i18n/locales/fr/codeEditor.json` (config)
- `src/modules/i18n/locales/fr/common.json` (config)
- `src/modules/i18n/locales/fr/settings.json` (config)
- `src/modules/i18n/locales/fr/sidebar.json` (config)
- `src/modules/i18n/locales/fr/tasks.json` (config)
- `src/modules/i18n/locales/he/auth.json` (config)
- `src/modules/i18n/locales/he/chat.json` (config)
- `src/modules/i18n/locales/he/codeEditor.json` (config)
- `src/modules/i18n/locales/he/common.json` (config)
- `src/modules/i18n/locales/he/git.json` (config)
- `src/modules/i18n/locales/he/settings.json` (config)
- `src/modules/i18n/locales/he/sidebar.json` (config)
- `src/modules/i18n/locales/he/tasks.json` (config)
- `src/modules/i18n/locales/id/auth.json` (config)
- `src/modules/i18n/locales/id/chat.json` (config)
- `src/modules/i18n/locales/id/codeEditor.json` (config)
- `src/modules/i18n/locales/id/common.json` (config)
- `src/modules/i18n/locales/id/git.json` (config)
- `src/modules/i18n/locales/id/settings.json` (config)
- `src/modules/i18n/locales/id/sidebar.json` (config)
- `src/modules/i18n/locales/id/tasks.json` (config)
- `src/modules/i18n/locales/it/auth.json` (config)
- `src/modules/i18n/locales/it/chat.json` (config)
- `src/modules/i18n/locales/it/codeEditor.json` (config)
- `src/modules/i18n/locales/it/common.json` (config)
- `src/modules/i18n/locales/it/settings.json` (config)
- `src/modules/i18n/locales/it/sidebar.json` (config)
- `src/modules/i18n/locales/it/tasks.json` (config)
- `src/modules/i18n/locales/ja/auth.json` (config)

## Top-level layout

- `src` — 375 analysed file(s)
- `server` — 325 analysed file(s)
- `public` — 22 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `docs` — 16 analysed file(s)
- `electron` — 15 analysed file(s)
- `.github` — 9 analysed file(s)
- `docker` — 5 analysed file(s)
- `.agents` — 4 analysed file(s)
- `redirect-package` — 4 analysed file(s)
- `scripts` — 4 analysed file(s)
- `.husky` — 2 analysed file(s)
- `shared` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `7943e285fc814a54d5549a34b90fac0805135a24` is the revision these paths and observations refer to.
