# Project structure: srizzon/git-city

**Analysed commit:** `85601619a7cc3f5c742f88dc817e0fe2b21d7d04`

**Commit reference:** [85601619a7cc3f5c742f88dc817e0fe2b21d7d04](https://github.com/srizzon/git-city/commit/85601619a7cc3f5c742f88dc817e0fe2b21d7d04)

**Tree at this commit:** [srizzon/git-city@85601619a7cc](https://github.com/srizzon/git-city/tree/85601619a7cc3f5c742f88dc817e0fe2b21d7d04)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | srizzon/git-city |
| Description | Your GitHub profile as a 3D pixel art building in an interactive city |
| Stars | 5994 |
| Forks | 295 |
| Licence | AGPL-3.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `85601619a7cc3f5c742f88dc817e0fe2b21d7d04` |
| Retrieved at | 2026-11-14T19:14:11.890761+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.claude/  (19 files)
  skills/  (19 files)
    gg/  (19 files)
      … 19 files under this directory
.conductor/  (1 files)
  settings.toml
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
docs/  (1 files)
  plans/  (1 files)
    2026-03-16-pro-plan-design.md
packages/  (17 files)
  vscode-extension/  (17 files)
    src/  (9 files)
      … 9 files under this directory
    .vscodeignore
    CHANGELOG.md
    LICENSE
    README.md
    esbuild.mjs
    gen-icon.html
    package.json
    tsconfig.json
party/  (17 files)
  arcade.ts
  bossToken.ts
  drift.ts
  drive.ts
  fly.ts
  heist.ts
  heistToken.ts
  killToken.ts
  lapToken.ts
  lobby.ts
  race.ts
  rallyToken.ts
  room.ts
  server.ts
  smash.ts
  townlive.ts
  tsconfig.json
public/  (31 files)
  audio/  (1 files)
    .gitkeep
  currencies/  (2 files)
    gitc.svg
    pixels.svg
  gpu-benchmarks/  (16 files)
    d-adreno.json
    d-amd.json
    d-apple.json
    d-geforce.json
    d-intel.json
    d-nvidia.json
    d-radeon.json
    m-adreno.json
    m-apple-ipad.json
    m-apple.json
    m-intel.json
    m-mali-t.json
    m-mali.json
    m-nvidia.json
    m-powervr.json
    m-samsung.json
  maps/  (1 files)
    lobby.json
  partners/  (7 files)
    sponsors/  (6 files)
      … 6 files under this directory
    videos/  (1 files)
      … 1 files under this directory
  sponsors/  (1 files)
    firecrawl-wordmark.svg
  sprites/  (1 files)
    arcade/  (1 files)
      … 1 files under this directory
  gc-pixel.js
  robots.txt
src/  (689 files)
  app/  (362 files)
    admin/  (56 files)
      … 56 files under this directory
    api/  (180 files)
      … 180 files under this directory
    arcade/  (4 files)
      … 4 files under this directory
    auth/  (3 files)
      … 3 files under this directory
    battle/  (6 files)
      … 6 files under this directory
    brasil/  (2 files)
      … 2 files under this directory
    brasil-preview/  (3 files)
      … 3 files under this directory
    communities/  (4 files)
      … 4 files under this directory
    compare/  (3 files)
      … 3 files under this directory
    dev/  (3 files)
      … 3 files under this directory
    drift/  (8 files)
      … 8 files under this directory
    email-preferences/  (4 files)
      … 4 files under this directory
    leaderboard/  (1 files)
      … 1 files under this directory
    levels/  (1 files)
      … 1 files under this directory
    live/  (1 files)
      … 1 files under this directory
    media-kit/  (1 files)
      … 1 files under this directory
    partners/  (13 files)
      … 13 files under this directory
    pixels/  (3 files)
      … 3 files under this directory
    poc/  (3 files)
      … 3 files under this directory
    privacy/  (1 files)
      … 1 files under this directory
    rabbit/  (2 files)
      … 2 files under this directory
    roadmap/  (3 files)
      … 3 files under this directory
    settings/  (2 files)
      … 2 files under this directory
    shop/  (7 files)
      … 7 files under this directory
    terms/  (1 files)
      … 1 files under this directory
    token/  (1 files)
      … 1 files under this directory
    town/  (14 files)
      … 14 files under this directory
    towns/  (13 files)
      … 13 files under this directory
    trailer/  (8 files)
      … 8 files under this directory
    unsubscribe/  (1 files)
      … 1 files under this directory
    wallpaper/  (1 files)
      … 1 files under this directory
    error.tsx
    global-error.tsx
    globals.css
    layout.tsx
    manifest.ts
    opengraph-image.tsx
    page.tsx
    robots.ts
    sitemap.ts
  components/  (273 files)
    activity/  (5 files)
      … 5 files under this directory
    arcade/  (3 files)
      … 3 files under this directory
    city/  (3 files)
      … 3 files under this directory
    cosmetics/  (9 files)
      … 9 files under this directory
    drift/  (9 files)
      … 9 files under this directory
    email/  (1 files)
      … 1 files under this directory
    games/  (2 files)
      … 2 files under this directory
    league/  (78 files)
      … 78 files under this directory
    leagues/  (1 files)
      … 1 files under this directory
    pixels/  (1 files)
      … 1 files under this directory
    profile/  (9 files)
      … 9 files under this directory
    race/  (8 files)
      … 8 files under this directory
    towns/  (44 files)
      … 44 files under this directory
    trailer/  (5 files)
      … 5 files under this directory
    ui/  (2 files)
      … 2 files under this directory
    BankPanel.tsx
    BankSwapTab.tsx
    BayBridge.tsx
    BossEvent.tsx
    BossEventHUD.tsx
    BossFlyStrip.tsx
    BossInvasionCard.tsx
    BossMinions.tsx
    BossPOC.tsx
    BossPreview.tsx
    BossShareCard.tsx
    BossVictoryScreen.tsx
    Building3D.tsx
    BuildingAds.tsx
    BuildingEffects.tsx
    CaptureMode.tsx
    CelebrationEffect.tsx
    CityBench.tsx
    CityCanvas.tsx
    CityPOC.tsx
    CityScene.tsx
    ClaimButton.tsx
    CommitsInfo.tsx
    CompareChallenge.tsx
    … 69 more files
  lib/  (54 files)
    arcade/  (11 files)
      … 11 files under this directory
    campaigns/  (4 files)
      … 4 files under this directory
    cosmetics/  (5 files)
      … 5 files under this directory
    drift/  (6 files)
      … 6 files under this directory
    account-delete.ts
    achievement-tiers.ts
    achievements.ts
    admin-emails.ts
    admin.ts
    auth-identity.ts
    auth-provision.ts
    bossEventStore.ts
    bossEventToken.ts
    chat-filter.test.ts
    chat-filter.ts
    city-extras.ts
    city-first-frame.ts
    city-layout-core.ts
    city-load.worker.ts
    city-lots.ts
    city-sf-layout.ts
    city-snapshot-client.ts
    city-snapshot-format.ts
    cityCache.ts
    concurrency.ts
    consent.ts
    contribution-refresh.ts
    create-developer.ts
    … 4 more files
.editorconfig
.env.example
.gitignore
.mcp.json
.prettierignore
.prettierrc
.vercelignore
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
EMAILS.md
ENVIRONMENTS.md
LICENSE
README.md
SECURITY.md
eslint.config.mjs
instrumentation-client.ts
next.config.ts
package.json
podcast.md
postcss.config.mjs
```

## Entry points

- [party/server.ts](https://github.com/srizzon/git-city/blob/85601619a7cc3f5c742f88dc817e0fe2b21d7d04/party/server.ts)
- [src/app/admin/page.tsx](https://github.com/srizzon/git-city/blob/85601619a7cc3f5c742f88dc817e0fe2b21d7d04/src/app/admin/page.tsx)
- [src/app/arcade/page.tsx](https://github.com/srizzon/git-city/blob/85601619a7cc3f5c742f88dc817e0fe2b21d7d04/src/app/arcade/page.tsx)
- [src/app/brasil-preview/page.tsx](https://github.com/srizzon/git-city/blob/85601619a7cc3f5c742f88dc817e0fe2b21d7d04/src/app/brasil-preview/page.tsx)
- [src/app/brasil/page.tsx](https://github.com/srizzon/git-city/blob/85601619a7cc3f5c742f88dc817e0fe2b21d7d04/src/app/brasil/page.tsx)
- [src/app/communities/page.tsx](https://github.com/srizzon/git-city/blob/85601619a7cc3f5c742f88dc817e0fe2b21d7d04/src/app/communities/page.tsx)
- [src/app/drift/page.tsx](https://github.com/srizzon/git-city/blob/85601619a7cc3f5c742f88dc817e0fe2b21d7d04/src/app/drift/page.tsx)
- [src/app/email-preferences/page.tsx](https://github.com/srizzon/git-city/blob/85601619a7cc3f5c742f88dc817e0fe2b21d7d04/src/app/email-preferences/page.tsx)
- [src/app/leaderboard/page.tsx](https://github.com/srizzon/git-city/blob/85601619a7cc3f5c742f88dc817e0fe2b21d7d04/src/app/leaderboard/page.tsx)
- [src/app/levels/page.tsx](https://github.com/srizzon/git-city/blob/85601619a7cc3f5c742f88dc817e0fe2b21d7d04/src/app/levels/page.tsx)
- [src/app/live/page.tsx](https://github.com/srizzon/git-city/blob/85601619a7cc3f5c742f88dc817e0fe2b21d7d04/src/app/live/page.tsx)
- [src/app/media-kit/page.tsx](https://github.com/srizzon/git-city/blob/85601619a7cc3f5c742f88dc817e0fe2b21d7d04/src/app/media-kit/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 182 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 177 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 273 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 25 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 54 file(s) under lib package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 8 file(s) under packages package (observed from repository paths and static analysis). |
| party package | library | Observed | Groups 16 file(s) under party package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 1 file(s) under public package (observed from repository paths and static analysis). |

## Important files

- `.conductor/settings.toml` (config)
- `.editorconfig` (config)
- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.mcp.json` (config)
- `package.json` (manifest)
- `packages/vscode-extension/package.json` (manifest)
- `packages/vscode-extension/tsconfig.json` (config)
- `party/tsconfig.json` (config)
- `public/gpu-benchmarks/d-adreno.json` (config)
- `public/gpu-benchmarks/d-amd.json` (config)
- `public/gpu-benchmarks/d-apple.json` (config)
- `public/gpu-benchmarks/d-geforce.json` (config)
- `public/gpu-benchmarks/d-intel.json` (config)
- `public/gpu-benchmarks/d-nvidia.json` (config)
- `public/gpu-benchmarks/d-radeon.json` (config)
- `public/gpu-benchmarks/m-adreno.json` (config)
- `public/gpu-benchmarks/m-apple-ipad.json` (config)
- `public/gpu-benchmarks/m-apple.json` (config)
- `public/gpu-benchmarks/m-intel.json` (config)
- `public/gpu-benchmarks/m-mali-t.json` (config)
- `public/gpu-benchmarks/m-mali.json` (config)
- `public/gpu-benchmarks/m-nvidia.json` (config)
- `public/gpu-benchmarks/m-powervr.json` (config)
- `public/gpu-benchmarks/m-samsung.json` (config)
- `public/maps/lobby.json` (config)

## Top-level layout

- `src` — 689 analysed file(s)
- `public` — 31 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `.claude` — 19 analysed file(s)
- `packages` — 17 analysed file(s)
- `party` — 17 analysed file(s)
- `.github` — 4 analysed file(s)
- `.conductor` — 1 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `85601619a7cc3f5c742f88dc817e0fe2b21d7d04` is the revision these paths and observations refer to.
