# Project structure: BartoszJarocki/cv

**Analysed commit:** `8faa527766b0504f4a016bc283dbd960b0707314`

**Commit reference:** [8faa527766b0504f4a016bc283dbd960b0707314](https://github.com/BartoszJarocki/cv/commit/8faa527766b0504f4a016bc283dbd960b0707314)

**Tree at this commit:** [BartoszJarocki/cv@8faa527766b0](https://github.com/BartoszJarocki/cv/tree/8faa527766b0504f4a016bc283dbd960b0707314)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | BartoszJarocki/cv |
| Description | Print-friendly, minimalist CV page |
| Stars | 9677 |
| Forks | 1062 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `8faa527766b0504f4a016bc283dbd960b0707314` |
| Retrieved at | 2026-11-14T19:13:33.164203+00:00 |
| Files in this snapshot | 44 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
scripts/  (1 files)
  verify.mjs
src/  (32 files)
  app/  (15 files)
    components/  (6 files)
      … 6 files under this directory
    index.md/  (1 files)
      … 1 files under this directory
    index.txt/  (1 files)
      … 1 files under this directory
    llms.txt/  (1 files)
      … 1 files under this directory
    globals.css
    layout.tsx
    opengraph-image.tsx
    page.tsx
    robots.ts
    sitemap.ts
  components/  (9 files)
    icons/  (3 files)
      … 3 files under this directory
    ui/  (4 files)
      … 4 files under this directory
    command-menu-dialog.tsx
    command-menu.tsx
  data/  (1 files)
    resume-data.ts
  lib/  (7 files)
    document.ts
    markdown.ts
    resume.ts
    structured-data.ts
    text.ts
    types.ts
    utils.ts
.gitignore
LICENSE
README.md
biome.json
next.config.js
package.json
pnpm-workspace.yaml
postcss.config.js
tailwind.config.js
tsconfig.json
```

## Entry points

- [src/app/page.tsx](https://github.com/BartoszJarocki/cv/blob/8faa527766b0504f4a016bc283dbd960b0707314/src/app/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 14 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 9 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 1 file(s) under data layer (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 7 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/ci.yml` (ci)
- `biome.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 32 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `8faa527766b0504f4a016bc283dbd960b0707314` is the revision these paths and observations refer to.
