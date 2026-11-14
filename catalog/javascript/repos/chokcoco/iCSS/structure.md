# Project structure: chokcoco/iCSS

**Analysed commit:** `e03eb3e59021dff1e51434cc81626e8a53c525cc`

**Commit reference:** [e03eb3e59021dff1e51434cc81626e8a53c525cc](https://github.com/chokcoco/iCSS/commit/e03eb3e59021dff1e51434cc81626e8a53c525cc)

**Tree at this commit:** [chokcoco/iCSS@e03eb3e59021](https://github.com/chokcoco/iCSS/tree/e03eb3e59021dff1e51434cc81626e8a53c525cc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | chokcoco/iCSS |
| Description | 不止于 CSS |
| Stars | 20623 |
| Forks | 2041 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e03eb3e59021dff1e51434cc81626e8a53c525cc` |
| Retrieved at | 2026-11-14T19:11:12.527425+00:00 |
| Files in this snapshot | 53 |

## Directory tree

```text
MCP/  (20 files)
  bin/  (2 files)
    icss-mcp.js
    install.js
  scripts/  (4 files)
    cursor-config.json
    fetch-inspiration.js
    fetch-issues.js
    publish-check.js
  .gitignore
  LICENSE
  README.en.md
  README.md
  debug-interactive.js
  debug-local.js
  debug-query.js
  debug.js
  diagnose-mcp.js
  package.json
  server.js
  setup.js
  test-inspiration.js
  test-server.js
website/  (31 files)
  app/  (20 files)
    api/  (3 files)
      … 3 files under this directory
    article/  (1 files)
      … 1 files under this directory
    components/  (3 files)
      … 3 files under this directory
    contexts/  (1 files)
      … 1 files under this directory
    lib/  (5 files)
      … 5 files under this directory
    test-api/  (1 files)
      … 1 files under this directory
    test-demo/  (1 files)
      … 1 files under this directory
    test-fixes/  (1 files)
      … 1 files under this directory
    test-theme-lang/  (1 files)
      … 1 files under this directory
    globals.css
    layout.tsx
    page.tsx
  public/  (1 files)
    index.md
  README.md
  THEME_LANG_FEATURES.md
  next-env.d.ts
  next.config.js
  package.json
  postcss.config.js
  tailwind.config.js
  test-features.md
  tsconfig.json
  vercel.json
.gitattributes
readme.md
```

## Entry points

- [MCP/server.js](https://github.com/chokcoco/iCSS/blob/e03eb3e59021dff1e51434cc81626e8a53c525cc/MCP/server.js)
- [MCP/bin/icss-mcp.js](https://github.com/chokcoco/iCSS/blob/e03eb3e59021dff1e51434cc81626e8a53c525cc/MCP/bin/icss-mcp.js)
- [MCP/bin/install.js](https://github.com/chokcoco/iCSS/blob/e03eb3e59021dff1e51434cc81626e8a53c525cc/MCP/bin/install.js)
- [website/app/page.tsx](https://github.com/chokcoco/iCSS/blob/e03eb3e59021dff1e51434cc81626e8a53c525cc/website/app/page.tsx)
- [website/app/test-api/page.tsx](https://github.com/chokcoco/iCSS/blob/e03eb3e59021dff1e51434cc81626e8a53c525cc/website/app/test-api/page.tsx)
- [website/app/test-demo/page.tsx](https://github.com/chokcoco/iCSS/blob/e03eb3e59021dff1e51434cc81626e8a53c525cc/website/app/test-demo/page.tsx)
- [website/app/test-fixes/page.tsx](https://github.com/chokcoco/iCSS/blob/e03eb3e59021dff1e51434cc81626e8a53c525cc/website/app/test-fixes/page.tsx)
- [website/app/test-theme-lang/page.tsx](https://github.com/chokcoco/iCSS/blob/e03eb3e59021dff1e51434cc81626e8a53c525cc/website/app/test-theme-lang/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 3 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| MCP package | library | Observed | Groups 14 file(s) under mcp package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 20 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `MCP/package.json` (manifest)
- `MCP/scripts/cursor-config.json` (config)
- `website/package.json` (manifest)
- `website/tsconfig.json` (config)
- `website/vercel.json` (config)

## Top-level layout

- `website` — 31 analysed file(s)
- `MCP` — 20 analysed file(s)
- `(root files)` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e03eb3e59021dff1e51434cc81626e8a53c525cc` is the revision these paths and observations refer to.
