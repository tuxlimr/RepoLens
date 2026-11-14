# Project structure: kern/filepizza

**Analysed commit:** `1e4d02fa91527d8dc83f4094ca394f8c29a88b56`

**Commit reference:** [1e4d02fa91527d8dc83f4094ca394f8c29a88b56](https://github.com/kern/filepizza/commit/1e4d02fa91527d8dc83f4094ca394f8c29a88b56)

**Tree at this commit:** [kern/filepizza@1e4d02fa9152](https://github.com/kern/filepizza/tree/1e4d02fa91527d8dc83f4094ca394f8c29a88b56)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | kern/filepizza |
| Description | :pizza: Peer-to-peer file transfers in your browser |
| Stars | 10282 |
| Forks | 621 |
| Licence | Other |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `1e4d02fa91527d8dc83f4094ca394f8c29a88b56` |
| Retrieved at | 2026-11-14T19:13:31.559796+00:00 |
| Files in this snapshot | 122 |

## Directory tree

```text
.claude/  (1 files)
  settings.local.json
.github/  (2 files)
  workflows/  (2 files)
    main.yml
    tests.yml
bin/  (1 files)
  peerjs.js
docs/  (1 files)
  file-transfer-protocol.md
public/  (3 files)
  robots.txt
  stream.html
  sw.js
scripts/  (1 files)
  pull-and-run.sh
src/  (59 files)
  app/  (9 files)
    api/  (4 files)
      … 4 files under this directory
    download/  (1 files)
      … 1 files under this directory
    reported/  (1 files)
      … 1 files under this directory
    layout.tsx
    not-found.tsx
    page.tsx
  components/  (30 files)
    AddFilesButton.tsx
    CancelButton.tsx
    ConnectionListItem.tsx
    CopyableInput.tsx
    DownloadButton.tsx
    Downloader.tsx
    DropZone.tsx
    ErrorMessage.tsx
    Footer.tsx
    InputLabel.tsx
    Loading.tsx
    ModeToggle.tsx
    PasswordField.tsx
    ProgressBar.tsx
    QueryClientProvider.tsx
    ReportTermsViolationButton.tsx
    ReturnHome.tsx
    Spinner.tsx
    StartButton.tsx
    StopButton.tsx
    SubtitleText.tsx
    TermsAcceptance.tsx
    ThemeProvider.tsx
    TitleText.tsx
    … 6 more files
  hooks/  (5 files)
    useClipboard.ts
    useDownloader.ts
    useRotatingSpinner.ts
    useUploaderChannel.ts
    useUploaderConnections.ts
  utils/  (2 files)
    download.ts
    pluralize.ts
  channel.ts
  config.ts
  coturn.ts
  fs.ts
  log.ts
  messages.ts
  redisClient.ts
  routes.ts
  slugs.ts
  styles.css
  toppings.ts
  types.ts
  zip-stream.ts
tests/  (34 files)
  e2e/  (4 files)
    add-files.test.ts
    basic.test.ts
    file-transfer.test.ts
    helpers.ts
  unit/  (30 files)
    CancelButton.test.tsx
    ConnectionListItem.test.tsx
    CopyableInput.test.tsx
    DownloadButton.test.tsx
    Downloader.subcomponents.test.tsx
    DropZone.test.tsx
    ErrorMessage.test.tsx
    Footer.test.tsx
    InputLabel.test.tsx
    Loading.test.tsx
    ModeToggle.test.tsx
    PasswordField.test.tsx
    ProgressBar.test.tsx
    QueryClientProvider.test.tsx
    ReportTermsViolationButton.test.tsx
    ReturnHome.test.tsx
    Spinner.test.tsx
    StartButton.test.tsx
    StopButton.test.tsx
    TermsAcceptance.test.tsx
    ThemeProvider.test.tsx
    TitleText.test.tsx
    TypeBadge.test.tsx
    UnlockButton.test.tsx
    … 6 more files
.cursorrules
.dockerignore
.gitignore
.prettierrc.js
CLAUDE.md
Dockerfile
LICENSE
README.md
docker-compose.production.yml
docker-compose.yml
eslint.config.mjs
next-env.d.ts
next.config.js
package.json
playwright.config.ts
postcss.config.js
renovate.json
tsconfig.json
vitest.config.ts
vitest.setup.ts
```

## Entry points

- [src/app/page.tsx](https://github.com/kern/filepizza/blob/1e4d02fa91527d8dc83f4094ca394f8c29a88b56/src/app/page.tsx)
- [src/app/reported/page.tsx](https://github.com/kern/filepizza/blob/1e4d02fa91527d8dc83f4094ca394f8c29a88b56/src/app/reported/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 4 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 5 file(s) under app package (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| channel.ts package | library | Observed | Groups 1 file(s) under channel.ts package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 30 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.ts package | library | Observed | Groups 1 file(s) under config.ts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| coturn.ts package | library | Observed | Groups 1 file(s) under coturn.ts package (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| fs.ts package | library | Observed | Groups 1 file(s) under fs.ts package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 5 file(s) under hooks package (observed from repository paths and static analysis). |
| log.ts package | library | Observed | Groups 1 file(s) under log.ts package (observed from repository paths and static analysis). |
| messages.ts package | library | Observed | Groups 1 file(s) under messages.ts package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 1 file(s) under public package (observed from repository paths and static analysis). |
| redisClient.ts package | library | Observed | Groups 1 file(s) under redisclient.ts package (observed from repository paths and static analysis). |
| routes.ts package | library | Observed | Groups 1 file(s) under routes.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| slugs.ts package | library | Observed | Groups 1 file(s) under slugs.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 34 file(s) under tests (observed from repository paths and static analysis). |
| toppings.ts package | library | Observed | Groups 1 file(s) under toppings.ts package (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 2 file(s) under utils package (observed from repository paths and static analysis). |
| zip-stream.ts package | library | Observed | Groups 1 file(s) under zip-stream.ts package (observed from repository paths and static analysis). |

## Important files

- `.claude/settings.local.json` (config)
- `.dockerignore` (container)
- `.github/workflows/main.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `Dockerfile` (container)
- `docker-compose.production.yml` (config)
- `docker-compose.yml` (container)
- `package.json` (manifest)
- `renovate.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 59 analysed file(s)
- `tests` — 34 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `public` — 3 analysed file(s)
- `.github` — 2 analysed file(s)
- `.claude` — 1 analysed file(s)
- `bin` — 1 analysed file(s)
- `docs` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1e4d02fa91527d8dc83f4094ca394f8c29a88b56` is the revision these paths and observations refer to.
