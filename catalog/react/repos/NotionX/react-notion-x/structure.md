# Project structure: NotionX/react-notion-x

**Analysed commit:** `dd4c891997f6c42413623f6ea836c3ba34e042fb`

**Commit reference:** [dd4c891997f6c42413623f6ea836c3ba34e042fb](https://github.com/NotionX/react-notion-x/commit/dd4c891997f6c42413623f6ea836c3ba34e042fb)

**Tree at this commit:** [NotionX/react-notion-x@dd4c891997f6](https://github.com/NotionX/react-notion-x/tree/dd4c891997f6c42413623f6ea836c3ba34e042fb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | NotionX/react-notion-x |
| Description | Fast and accurate React renderer for Notion. TS batteries included. ⚡️ |
| Stars | 5442 |
| Forks | 645 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `dd4c891997f6c42413623f6ea836c3ba34e042fb` |
| Retrieved at | 2026-11-14T19:14:19.068684+00:00 |
| Files in this snapshot | 399 |

## Directory tree

```text
.claude/  (1 files)
  settings.local.json
.github/  (6 files)
  workflows/  (3 files)
    notion-image-canary.yml
    release.yml
    test.yml
  funding.yml
  issue_template.md
  pull_request_template.md
.vscode/  (1 files)
  launch.json
examples/  (40 files)
  full/  (20 files)
    components/  (4 files)
      … 4 files under this directory
    lib/  (4 files)
      … 4 files under this directory
    pages/  (4 files)
      … 4 files under this directory
    public/  (1 files)
      … 1 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    next-env.d.ts
    next.config.js
    package.json
    readme.md
    tsconfig.json
    turbo.json
  minimal/  (20 files)
    components/  (1 files)
      … 1 files under this directory
    lib/  (4 files)
      … 4 files under this directory
    pages/  (6 files)
      … 6 files under this directory
    public/  (1 files)
      … 1 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    next-env.d.ts
    next.config.js
    package.json
    readme.md
    tsconfig.json
    turbo.json
packages/  (335 files)
  notion-client/  (27 files)
    fixtures/  (15 files)
      … 15 files under this directory
    src/  (8 files)
      … 8 files under this directory
    package.json
    readme.md
    tsconfig.json
    tsdown.config.ts
  notion-compat/  (14 files)
    src/  (10 files)
      … 10 files under this directory
    package.json
    readme.md
    tsconfig.json
    tsdown.config.ts
  notion-types/  (14 files)
    src/  (10 files)
      … 10 files under this directory
    package.json
    readme.md
    tsconfig.json
    tsdown.config.ts
  notion-utils/  (124 files)
    fixtures/  (77 files)
      … 77 files under this directory
    src/  (43 files)
      … 43 files under this directory
    package.json
    readme.md
    tsconfig.json
    tsdown.config.ts
  notion-x-to-md/  (36 files)
    examples/  (20 files)
      … 20 files under this directory
    src/  (12 files)
      … 12 files under this directory
    package.json
    readme.md
    tsconfig.json
    tsdown.config.ts
  react-notion-x/  (120 files)
    src/  (116 files)
      … 116 files under this directory
    package.json
    readme.md
    tsconfig.json
    tsdown.config.ts
.editorconfig
.gitignore
AGENTS.md
CODE_OF_CONDUCT.md
GOVERNANCE.md
SECURITY.md
contributing.md
funding.json
license
oxfmt.config.ts
oxlint.config.ts
package.json
pnpm-workspace.yaml
readme.md
tsconfig.json
turbo.json
```

## Entry points

- [packages/notion-x-to-md/src/cli.ts](https://github.com/NotionX/react-notion-x/blob/dd4c891997f6c42413623f6ea836c3ba34e042fb/packages/notion-x-to-md/src/cli.ts)
- [packages/notion-client/src/index.ts](https://github.com/NotionX/react-notion-x/blob/dd4c891997f6c42413623f6ea836c3ba34e042fb/packages/notion-client/src/index.ts)
- [packages/notion-compat/src/index.ts](https://github.com/NotionX/react-notion-x/blob/dd4c891997f6c42413623f6ea836c3ba34e042fb/packages/notion-compat/src/index.ts)
- [packages/notion-types/src/index.ts](https://github.com/NotionX/react-notion-x/blob/dd4c891997f6c42413623f6ea836c3ba34e042fb/packages/notion-types/src/index.ts)
- [packages/notion-utils/src/index.ts](https://github.com/NotionX/react-notion-x/blob/dd4c891997f6c42413623f6ea836c3ba34e042fb/packages/notion-utils/src/index.ts)
- [packages/notion-x-to-md/src/index.ts](https://github.com/NotionX/react-notion-x/blob/dd4c891997f6c42413623f6ea836c3ba34e042fb/packages/notion-x-to-md/src/index.ts)
- [packages/react-notion-x/src/index.ts](https://github.com/NotionX/react-notion-x/blob/dd4c891997f6c42413623f6ea836c3ba34e042fb/packages/react-notion-x/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 109 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 173 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.claude/settings.local.json` (config)
- `.editorconfig` (config)
- `.github/funding.yml` (config)
- `.github/workflows/notion-image-canary.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.vscode/launch.json` (config)
- `examples/full/package.json` (manifest)
- `examples/full/tsconfig.json` (config)
- `examples/full/turbo.json` (config)
- `examples/minimal/package.json` (manifest)
- `examples/minimal/tsconfig.json` (config)
- `examples/minimal/turbo.json` (config)
- `funding.json` (config)
- `package.json` (manifest)
- `packages/notion-client/fixtures/blocks/audio.json` (config)
- `packages/notion-client/fixtures/blocks/drive.json` (config)
- `packages/notion-client/fixtures/blocks/equation.json` (config)
- `packages/notion-client/fixtures/blocks/file.json` (config)
- `packages/notion-client/fixtures/blocks/pdf.json` (config)
- `packages/notion-client/fixtures/board-results.json` (config)
- `packages/notion-client/fixtures/board.json` (config)
- `packages/notion-client/fixtures/collection-row-page.json` (config)
- `packages/notion-client/fixtures/collection-view-page.json` (config)
- `packages/notion-client/fixtures/gallery.json` (config)
- `packages/notion-client/fixtures/list.json` (config)
- `packages/notion-client/fixtures/page.json` (config)
- `packages/notion-client/fixtures/search.json` (config)
- `packages/notion-client/fixtures/signed-urls.json` (config)
- `packages/notion-client/fixtures/table.json` (config)
- `packages/notion-client/package.json` (manifest)
- `packages/notion-client/tsconfig.json` (config)
- `packages/notion-compat/package.json` (manifest)
- `packages/notion-compat/tsconfig.json` (config)
- `packages/notion-types/package.json` (manifest)
- `packages/notion-types/tsconfig.json` (config)
- `packages/notion-utils/fixtures/nba/1a425309-21c0-4ca1-8548-c5915137b566.json` (config)
- `packages/notion-utils/fixtures/nba/Atlanta Hawks.json` (config)
- `packages/notion-utils/fixtures/nba/Boston Celtics.json` (config)
- `packages/notion-utils/fixtures/nba/Brooklyn Nets.json` (config)
- `packages/notion-utils/fixtures/nba/Charlotte Hornets.json` (config)
- `packages/notion-utils/fixtures/nba/Chicago Bulls.json` (config)
- `packages/notion-utils/fixtures/nba/Cleveland Cavaliers.json` (config)
- `packages/notion-utils/fixtures/nba/Dallas Mavericks.json` (config)
- `packages/notion-utils/fixtures/nba/Denver Nuggest.json` (config)
- `packages/notion-utils/fixtures/nba/Detroit Pistons.json` (config)
- `packages/notion-utils/fixtures/nba/Duke University.json` (config)
- `packages/notion-utils/fixtures/nba/Golden State Warriors.json` (config)
- `packages/notion-utils/fixtures/nba/Houston Rockets.json` (config)
- `packages/notion-utils/fixtures/nba/Indiana Pacers.json` (config)
- `packages/notion-utils/fixtures/nba/List.json` (config)
- `packages/notion-utils/fixtures/nba/Los Angeles Clippers.json` (config)
- `packages/notion-utils/fixtures/nba/Los Angeles Lakers.json` (config)
- `packages/notion-utils/fixtures/nba/Memphis Grizzlies.json` (config)
- `packages/notion-utils/fixtures/nba/Miami Heat.json` (config)
- `packages/notion-utils/fixtures/nba/Milwaukee Bucks.json` (config)
- `packages/notion-utils/fixtures/nba/Minnesota Timberwolves.json` (config)
- `packages/notion-utils/fixtures/nba/New Orleans Pelicans.json` (config)
- `packages/notion-utils/fixtures/nba/New York Knicks.json` (config)
- `packages/notion-utils/fixtures/nba/Oklahoma City Thunder.json` (config)
- `packages/notion-utils/fixtures/nba/Orlando Magic.json` (config)
- `packages/notion-utils/fixtures/nba/Philadelphia 76ers.json` (config)
- `packages/notion-utils/fixtures/nba/Phoenix Suns.json` (config)
- `packages/notion-utils/fixtures/nba/Portland Trail Blazers.json` (config)
- `packages/notion-utils/fixtures/nba/Raw Table.json` (config)
- `packages/notion-utils/fixtures/nba/Sacramento Kings.json` (config)
- `packages/notion-utils/fixtures/nba/San Antonio Spurs.json` (config)
- `packages/notion-utils/fixtures/nba/Toronto Raptors.json` (config)
- `packages/notion-utils/fixtures/nba/UCLA.json` (config)
- `packages/notion-utils/fixtures/nba/University of Kentucky.json` (config)
- `packages/notion-utils/fixtures/nba/University of North Carolina.json` (config)
- `packages/notion-utils/fixtures/nba/University of Texas.json` (config)
- `packages/notion-utils/fixtures/nba/Utah Jazz.json` (config)
- `packages/notion-utils/fixtures/nba/Washington Wizards.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-048d8535-b957-488a-89f0-ade8d3c4c026.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-1a1863bd-f819-41dc-a228-831ca7a75d2a.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-1d79cc15-d040-43eb-9d65-7e35bafbcf74.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-367ecf41-f124-4652-bb7d-464b3789aefd.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-3815e8d7-e5f2-4399-a761-9ceaed565257.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-385ed123-6a39-46e5-984c-9704bcfd6494.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-43d091fb-a648-40cc-ae10-9d9784c34524.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-448a76b8-847d-4a40-a494-9a6da9c41a58.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-52718a79-d339-4d26-873f-734004af8823.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-5662c1f4-a011-4629-9616-3a2d53f6c9af.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-5742eaed-3c36-495a-bde5-7d33cba0ddb5.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-59a7246f-e923-4faf-9246-75851294365b.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-5ae81e49-33ad-47bf-9c14-14adb9145b4d.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-5c20b593-23d4-4884-9102-3ef3b1049273.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-63717bf3-3af6-4112-989d-acbe665ccf91.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-693b4304-0bbd-4f9a-85f1-7c9cb1768110.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-7687ad1f-ccbe-4abb-8e95-a3685543aefe.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-85e4d626-09cc-45f6-9a28-07d5d490ca1d.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-93fe8a38-e32b-4c6a-87f2-03f1a438de75.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-99cd3dfb-97fb-493d-bfaa-518bd872dda4.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-9a43758f-21c5-4fc2-a4b5-0fc82971b79f.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-9fdf39a1-64c3-464c-a4c9-f3e4d9a9aa2c.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-ab6c9a56-5322-4bd1-a384-7797a81478c5.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-b6c6b669-659e-4487-8d48-8a538b8a0d82.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-bd226193-3647-4ed1-bbe3-a5baa69954c7.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-bdc489ac-13dd-46bd-97f9-86866d76bc43.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-c14e33fe-19d2-4266-a935-0ef6528a77ff.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-c34ab79e-df2d-4a6d-af71-8aef61a65aa7.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-c69e1799-88cb-4135-a10d-1ec4617f0aa6.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-cfe27a86-00d0-4322-b2db-2bc3e69269e2.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-d4102177-3cb3-4d36-8f39-92d84147f825.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-d8f02741-e03a-4e40-91d7-0b821ee4014d.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-dac0d378-1774-47fc-a3a3-103ae120a3c1.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-e1c31992-ad30-4ab5-a497-c69fc579e2ec.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-e3d28d4f-e72e-430a-92f8-263cd01ea452.json` (config)
- `packages/notion-utils/fixtures/nba/data/1a425309-21c0-4ca1-8548-c5915137b566-e8feed24-4bf6-41b5-84a7-6134f9160cc1.json` (config)
- `packages/notion-utils/fixtures/nba/data/e777a528-9404-4e96-9f26-0014be705592-c01c2f48-5442-47d8-adb3-01c4f8bb8e58.json` (config)
- `packages/notion-utils/fixtures/nba/data/e777a528-9404-4e96-9f26-0014be705592-c0d2d91c-e2a5-4ea5-a9b7-2b2d8ae2d591.json` (config)
- `packages/notion-utils/fixtures/nba/e777a528-9404-4e96-9f26-0014be705592.json` (config)
- `packages/notion-utils/package.json` (manifest)
- `packages/notion-utils/tsconfig.json` (config)
- `packages/notion-x-to-md/package.json` (manifest)
- `packages/notion-x-to-md/tsconfig.json` (config)
- `packages/react-notion-x/package.json` (manifest)
- `packages/react-notion-x/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `turbo.json` (config)

## Top-level layout

- `packages` — 335 analysed file(s)
- `examples` — 40 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 6 analysed file(s)
- `.claude` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `dd4c891997f6c42413623f6ea836c3ba34e042fb` is the revision these paths and observations refer to.
