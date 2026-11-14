# Project structure: sadmann7/tablecn

**Analysed commit:** `44ac3879d0db81e92c011971cb43261fbbdc059a`

**Commit reference:** [44ac3879d0db81e92c011971cb43261fbbdc059a](https://github.com/sadmann7/tablecn/commit/44ac3879d0db81e92c011971cb43261fbbdc059a)

**Tree at this commit:** [sadmann7/tablecn@44ac3879d0db](https://github.com/sadmann7/tablecn/tree/44ac3879d0db81e92c011971cb43261fbbdc059a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | sadmann7/tablecn |
| Description | Data table and data grid components built with shadcn/ui, featuring sorting, filtering, pagination, infinite scrolling, and real-time collaboration. |
| Stars | 6384 |
| Forks | 559 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `44ac3879d0db81e92c011971cb43261fbbdc059a` |
| Retrieved at | 2026-11-14T19:14:06.819633+00:00 |
| Files in this snapshot | 414 |

## Directory tree

```text
.claude/  (1 files)
  launch.json
.cursor/  (1 files)
  rules/  (1 files)
    react-patterns.mdc
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  setup/  (1 files)
    action.yml
  workflows/  (1 files)
    code-check.yml
.vscode/  (1 files)
  settings.json
drizzle/  (1 files)
  meta/  (1 files)
    _journal.json
e2e/  (2 files)
  data-table.spec.ts
  record-data-table-launch.spec.ts
lint/  (4 files)
  comment-style.test.ts
  comment-style.ts
  plugin.ts
  top-down-order.ts
party/  (5 files)
  constants.ts
  index.ts
  seeds.ts
  tsconfig.json
  types.ts
public/  (7 files)
  doom/  (6 files)
    COPYING.md
    README.md
    default.cfg
    doom-wasm.patch
    extra.cfg
    websockets-doom.js
  r/  (1 files)
    styles/  (1 files)
      … 1 files under this directory
registry/  (3 files)
  base-differences.json
  bases.ts
  styles.tsx
scripts/  (4 files)
  build-registry.ts
  check-bases.ts
  clean-registry.ts
  profile-data-grid-scroll.ts
src/  (354 files)
  app/  (90 files)
    api/  (3 files)
      … 3 files under this directory
    bases/  (18 files)
      … 18 files under this directory
    components/  (5 files)
      … 5 files under this directory
    data-grid/  (9 files)
      … 9 files under this directory
    data-grid-doom/  (8 files)
      … 8 files under this directory
    data-grid-multiplayer/  (13 files)
      … 13 files under this directory
    data-grid-rapid/  (4 files)
      … 4 files under this directory
    data-table-launch/  (15 files)
      … 15 files under this directory
    lib/  (8 files)
      … 8 files under this directory
    icon.svg
    layout.tsx
    manifest.ts
    opengraph-image.alt.txt
    page.tsx
    robots.ts
    sitemap.ts
  components/  (14 files)
    layouts/  (4 files)
      … 4 files under this directory
    action-bar-tooltip-item.tsx
    active-link.tsx
    data-mode-toggle.tsx
    icons.tsx
    providers.tsx
    skip-nav.tsx
    tailwind-indicator.tsx
    theme-color.tsx
    theme-shortcut.tsx
    uploadthing-ssr.tsx
  db/  (6 files)
    extensions.ts
    index.ts
    migrate.ts
    schema.ts
    seed.ts
    utils.ts
  hooks/  (31 files)
    test/  (22 files)
      … 22 files under this directory
    use-badge-overflow.ts
    use-debounced-callback.ts
    use-isomorphic-layout-effect.ts
    use-media-query.ts
    use-mounted.ts
    use-multiplayer-room.ts
    use-ref-with-init.ts
    use-value-as-ref.ts
    use-window-size.ts
  lib/  (30 files)
    test/  (8 files)
      … 8 files under this directory
    constants.ts
    data-grid-features.ts
    data-grid-filters.ts
    data-grid-row-models.ts
    data-grid-types.ts
    data-grid-utils.ts
    data-table-config.ts
    data-table-features.ts
    data-table-filters.ts
    data-table-parsers.ts
    data-table-types.ts
    data-table-utils.ts
    error.ts
    export.ts
    flag.ts
    fonts.ts
    format.ts
    id.ts
    rate-limit.ts
    site.ts
    uploadthing.ts
    utils.ts
  registry/  (181 files)
    bases/  (180 files)
      … 180 files under this directory
    icons/  (1 files)
      … 1 files under this directory
  styles/  (1 files)
    globals.css
  env.ts
.env.example
.gitignore
.markdownlint-cli2.yaml
.oxfmtrc.json
.oxlintrc.json
AGENTS.md
CONTRIBUTING.md
LICENSE.md
README.md
REVIEW.md
components.json
docker-compose.yml
drizzle.config.ts
next.config.ts
package.json
playwright.config.ts
playwright.record.config.ts
pnpm-workspace.yaml
postcss.config.cjs
registry.json
renovate.json
tsconfig.json
tsconfig.scripts.json
vitest.config.ts
… 2 more files
```

## Entry points

- [party/index.ts](https://github.com/sadmann7/tablecn/blob/44ac3879d0db81e92c011971cb43261fbbdc059a/party/index.ts)
- [src/app/bases/page.tsx](https://github.com/sadmann7/tablecn/blob/44ac3879d0db81e92c011971cb43261fbbdc059a/src/app/bases/page.tsx)
- [src/app/data-grid-doom/page.tsx](https://github.com/sadmann7/tablecn/blob/44ac3879d0db81e92c011971cb43261fbbdc059a/src/app/data-grid-doom/page.tsx)
- [src/app/data-grid-multiplayer/page.tsx](https://github.com/sadmann7/tablecn/blob/44ac3879d0db81e92c011971cb43261fbbdc059a/src/app/data-grid-multiplayer/page.tsx)
- [src/app/data-grid-rapid/page.tsx](https://github.com/sadmann7/tablecn/blob/44ac3879d0db81e92c011971cb43261fbbdc059a/src/app/data-grid-rapid/page.tsx)
- [src/app/data-grid/page.tsx](https://github.com/sadmann7/tablecn/blob/44ac3879d0db81e92c011971cb43261fbbdc059a/src/app/data-grid/page.tsx)
- [src/app/data-table-launch/page.tsx](https://github.com/sadmann7/tablecn/blob/44ac3879d0db81e92c011971cb43261fbbdc059a/src/app/data-table-launch/page.tsx)
- [src/app/page.tsx](https://github.com/sadmann7/tablecn/blob/44ac3879d0db81e92c011971cb43261fbbdc059a/src/app/page.tsx)
- [src/db/index.ts](https://github.com/sadmann7/tablecn/blob/44ac3879d0db81e92c011971cb43261fbbdc059a/src/db/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 3 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 77 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 14 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 6 file(s) under data layer (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 2 file(s) under e2e package (observed from repository paths and static analysis). |
| env.ts package | library | Observed | Groups 1 file(s) under env.ts package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 9 file(s) under hooks package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 22 file(s) under lib package (observed from repository paths and static analysis). |
| lint package | library | Observed | Groups 4 file(s) under lint package (observed from repository paths and static analysis). |
| party package | library | Observed | Groups 4 file(s) under party package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 1 file(s) under public package (observed from repository paths and static analysis). |
| registry package | library | Observed | Groups 183 file(s) under registry package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 33 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.claude/launch.json` (config)
- `.env.example` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/setup/action.yml` (config)
- `.github/workflows/code-check.yml` (ci)
- `.markdownlint-cli2.yaml` (config)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `.vscode/settings.json` (config)
- `components.json` (config)
- `docker-compose.yml` (container)
- `drizzle/meta/_journal.json` (config)
- `package.json` (manifest)
- `party/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `public/doom/default.cfg` (config)
- `public/doom/extra.cfg` (config)
- `public/r/styles/index.json` (config)
- `registry.json` (config)
- `registry/base-differences.json` (config)
- `renovate.json` (config)
- `tsconfig.json` (config)
- `tsconfig.scripts.json` (config)

## Top-level layout

- `src` — 354 analysed file(s)
- `(root files)` — 26 analysed file(s)
- `public` — 7 analysed file(s)
- `.github` — 5 analysed file(s)
- `party` — 5 analysed file(s)
- `lint` — 4 analysed file(s)
- `scripts` — 4 analysed file(s)
- `registry` — 3 analysed file(s)
- `e2e` — 2 analysed file(s)
- `.claude` — 1 analysed file(s)
- `.cursor` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `drizzle` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `44ac3879d0db81e92c011971cb43261fbbdc059a` is the revision these paths and observations refer to.
