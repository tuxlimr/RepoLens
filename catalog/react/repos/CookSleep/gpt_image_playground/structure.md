# Project structure: CookSleep/gpt_image_playground

**Analysed commit:** `b7f168b512dc6b2854f8a68f457ca5ecf9b646f4`

**Commit reference:** [b7f168b512dc6b2854f8a68f457ca5ecf9b646f4](https://github.com/CookSleep/gpt_image_playground/commit/b7f168b512dc6b2854f8a68f457ca5ecf9b646f4)

**Tree at this commit:** [CookSleep/gpt_image_playground@b7f168b512dc](https://github.com/CookSleep/gpt_image_playground/tree/b7f168b512dc6b2854f8a68f457ca5ecf9b646f4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | CookSleep/gpt_image_playground |
| Description | 支持 GPT Image、Gemini（Nano Banana）、Grok 和 Seedream 5.5 的图片生成与编辑工具 |
| Stars | 4090 |
| Forks | 1013 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `b7f168b512dc6b2854f8a68f457ca5ecf9b646f4` |
| Retrieved at | 2026-11-14T19:14:55.523715+00:00 |
| Files in this snapshot | 351 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (4 files)
    deploy.yml
    docker.yml
    tauri-release.yml
    vercel-tag-deploy.yml
deploy/  (4 files)
  Dockerfile
  inject-api-url.sh
  migrate-api-env.envsh
  nginx.conf
docs/  (2 files)
  custom-provider-llm-prompt.md
  mock-image-api.md
fonts/  (2 files)
  harmonyos-sans-sc.css
  maple-mono-nf-cn.css
public/  (12 files)
  announcements/  (6 files)
    client-intro.css
    client-intro.html
    client-intro.js
    models-intro-3.css
    models-intro-3.html
    models-intro-3.js
  announcements.json
  color-mode.js
  manifest.webmanifest
  pwa-icon.svg
  pwa-maskable-icon.svg
  sw.js
scripts/  (2 files)
  build-notices.mjs
  mock-image-api.mjs
skills/  (4 files)
  gpt-image-playground/  (4 files)
    references/  (3 files)
      … 3 files under this directory
    SKILL.md
src/  (254 files)
  components/  (70 files)
    editor/  (1 files)
      … 1 files under this directory
    favorites/  (6 files)
      … 6 files under this directory
    input/  (9 files)
      … 9 files under this directory
    settings/  (15 files)
      … 15 files under this directory
    AgentWorkspace.tsx
    AnnouncementModal.tsx
    Checkbox.tsx
    CommentMarks.tsx
    ConfirmDialog.tsx
    DataProgressDialog.tsx
    DbBlockedNotice.tsx
    DetailModal.test.tsx
    DetailModal.tsx
    FavoriteCollections.tsx
    Header.tsx
    HelpModal.tsx
    HistoryModal.tsx
    ImageContextMenu.tsx
    ImageSearchSources.tsx
    ImportLinkDiff.tsx
    InputBar.test.tsx
    InputBar.tsx
    Lightbox.tsx
    MarkdownRenderer.test.tsx
    MarkdownRenderer.tsx
    MaskEditorModal.tsx
    SearchBar.tsx
    Select.tsx
    … 15 more files
  hooks/  (25 files)
    useAnnouncements.ts
    useAppFonts.ts
    useClientUpdate.test.ts
    useClientUpdate.ts
    useCloseConfirm.ts
    useCloseOnEscape.ts
    useColorMode.ts
    useDockerApiUrlMigrationNotice.ts
    useDragSelect.ts
    useEditorViewport.ts
    useHintTooltip.ts
    useImportLinks.test.ts
    useImportLinks.ts
    useNearViewport.test.tsx
    useNearViewport.ts
    usePopoverDismiss.ts
    usePreventBackgroundScroll.ts
    usePrivacyMode.ts
    usePullUpToLoad.test.tsx
    usePullUpToLoad.ts
    useReleaseUpdates.ts
    useSaveLocationPrompt.tsx
    useSketchComments.ts
    useTooltip.ts
    … 1 more files
  lib/  (154 files)
    agentApi.test.ts
    agentApi.ts
    agentAssistantBlocks.test.ts
    agentAssistantBlocks.ts
    agentConversationState.test.ts
    agentConversationState.ts
    agentImageReferences.test.ts
    agentImageReferences.ts
    agentInputBuilder.test.ts
    agentInputBuilder.ts
    agentResponseState.test.ts
    agentResponseState.ts
    agentWebSearch.ts
    announcements.test.ts
    announcements.ts
    api.test.ts
    api.ts
    apiProfiles.test.ts
    apiProfiles.ts
    batchPrompts.test.ts
    batchPrompts.ts
    browserNotification.ts
    canvasImage.ts
    cliBridge.test.ts
    … 130 more files
  App.tsx
  index.css
  main.tsx
  types.ts
  vite-env.d.ts
src-tauri/  (35 files)
  capabilities/  (1 files)
    default.json
  permissions/  (8 files)
    cli.toml
    close.toml
    diagnostics.toml
    files.toml
    http.toml
    proxy.toml
    storage.toml
    update.toml
  src/  (20 files)
    bin/  (1 files)
      … 1 files under this directory
    cli/  (5 files)
      … 5 files under this directory
    storage/  (3 files)
      … 3 files under this directory
    cli.rs
    close_watch.rs
    data_dir.rs
    diagnostics.rs
    files.rs
    http.rs
    lib.rs
    main.rs
    migrate.rs
    proxy.rs
    update.rs
  windows/  (1 files)
    installer.nsi
  .taurignore
  Cargo.toml
  about.toml
  build.rs
  tauri.conf.json
third-party-licenses/  (10 files)
  npm/  (7 files)
    rehype-katex.txt
    remark-math.txt
    robot3.txt
    tauri-apps__plugin-clipboard-manager.txt
    tauri-apps__plugin-deep-link.txt
    tauri-apps__plugin-log.txt
    tauri-apps__plugin-opener.txt
  HarmonyOS-Sans-LICENSE.txt
  LobeIcons-LICENSE.txt
  MapleMono-LICENSE.txt
.dockerignore
.gitattributes
.gitignore
AGENTS.md
LICENSE
README.md
RELEASE.md
dev-proxy.config.example.json
gpt-image-config.agent.example.json
gpt-image-config.example.json
index.html
package.json
postcss.config.js
sponsor-presets.json
tailwind.config.js
tsconfig.json
vercel.json
vite.config.ts
wrangler.jsonc
```

## Entry points

- [src/App.tsx](https://github.com/CookSleep/gpt_image_playground/blob/b7f168b512dc6b2854f8a68f457ca5ecf9b646f4/src/App.tsx)
- [src/main.tsx](https://github.com/CookSleep/gpt_image_playground/blob/b7f168b512dc6b2854f8a68f457ca5ecf9b646f4/src/main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| App.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 55 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 36 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). |
| deploy package | library | Observed | Groups 1 file(s) under deploy package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 25 file(s) under hooks package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 154 file(s) under lib package (observed from repository paths and static analysis). |
| main.tsx package | library | Observed | Groups 1 file(s) under main.tsx package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 4 file(s) under public package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| src-tauri package | library | Observed | Groups 18 file(s) under src-tauri package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| vite-env.d.ts package | library | Observed | Groups 1 file(s) under vite-env.d.ts package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/deploy.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.github/workflows/tauri-release.yml` (ci)
- `.github/workflows/vercel-tag-deploy.yml` (ci)
- `deploy/Dockerfile` (container)
- `dev-proxy.config.example.json` (config)
- `gpt-image-config.agent.example.json` (config)
- `gpt-image-config.example.json` (config)
- `package.json` (manifest)
- `public/announcements.json` (config)
- `sponsor-presets.json` (config)
- `src-tauri/Cargo.toml` (manifest)
- `src-tauri/about.toml` (config)
- `src-tauri/capabilities/default.json` (config)
- `src-tauri/permissions/cli.toml` (config)
- `src-tauri/permissions/close.toml` (config)
- `src-tauri/permissions/diagnostics.toml` (config)
- `src-tauri/permissions/files.toml` (config)
- `src-tauri/permissions/http.toml` (config)
- `src-tauri/permissions/proxy.toml` (config)
- `src-tauri/permissions/storage.toml` (config)
- `src-tauri/permissions/update.toml` (config)
- `src-tauri/tauri.conf.json` (config)
- `tsconfig.json` (config)
- `vercel.json` (config)

## Top-level layout

- `src` — 254 analysed file(s)
- `src-tauri` — 35 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `public` — 12 analysed file(s)
- `third-party-licenses` — 10 analysed file(s)
- `.github` — 7 analysed file(s)
- `deploy` — 4 analysed file(s)
- `skills` — 4 analysed file(s)
- `docs` — 2 analysed file(s)
- `fonts` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (2 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b7f168b512dc6b2854f8a68f457ca5ecf9b646f4` is the revision these paths and observations refer to.
