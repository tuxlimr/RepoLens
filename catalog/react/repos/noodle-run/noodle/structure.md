# Project structure: noodle-run/noodle

**Analysed commit:** `4e26fb7c990ccccce203f1c30f79126ef1bfbcaa`

**Commit reference:** [4e26fb7c990ccccce203f1c30f79126ef1bfbcaa](https://github.com/noodle-run/noodle/commit/4e26fb7c990ccccce203f1c30f79126ef1bfbcaa)

**Tree at this commit:** [noodle-run/noodle@4e26fb7c990c](https://github.com/noodle-run/noodle/tree/4e26fb7c990ccccce203f1c30f79126ef1bfbcaa)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | noodle-run/noodle |
| Description | Rethinking Student Productivity |
| Stars | 12151 |
| Forks | 771 |
| Licence | AGPL-3.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `4e26fb7c990ccccce203f1c30f79126ef1bfbcaa` |
| Retrieved at | 2026-11-14T19:13:24.295999+00:00 |
| Files in this snapshot | 122 |

## Directory tree

```text
.changeset/  (1 files)
  config.json
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yaml
    feature_request.md
  PULL_REQUEST_TEMPLATE/  (1 files)
    pull_request_template.md
  workflows/  (3 files)
    main-ci.yml
    pr-ci.yml
    pr-cleanup.yml
  FUNDING.yaml
.husky/  (3 files)
  commit-msg
  pre-commit
  prepare-commit-msg
.vscode/  (2 files)
  extensions.json
  settings.json
drizzle/  (7 files)
  meta/  (4 files)
    0000_snapshot.json
    0001_snapshot.json
    0002_snapshot.json
    _journal.json
  0000_funny_johnny_blaze.sql
  0001_minor_warlock.sql
  0002_complex_sally_floyd.sql
public/  (3 files)
  .well-known/  (1 files)
    security.txt
  browserconfig.xml
  logo.svg
src/  (77 files)
  app/  (32 files)
    (dashboard)/  (13 files)
      … 13 files under this directory
    (site)/  (13 files)
      … 13 files under this directory
    api/  (1 files)
      … 1 files under this directory
    globals.css
    layout.tsx
    manifest.ts
    not-found.tsx
    robots.ts
  content/  (3 files)
    blog/  (1 files)
      … 1 files under this directory
    legal/  (2 files)
      … 2 files under this directory
  db/  (4 files)
    schema/  (3 files)
      … 3 files under this directory
    index.ts
  emails/  (4 files)
    layouts/  (1 files)
      … 1 files under this directory
    templates/  (1 files)
      … 1 files under this directory
    tailwind.ts
    utils.ts
  lib/  (6 files)
    trpc/  (3 files)
      … 3 files under this directory
    mdx.ts
    redis.ts
    resend.ts
  primitives/  (17 files)
    button.tsx
    checkbox.tsx
    dropdown-menu.tsx
    form.tsx
    icon.tsx
    input.tsx
    label.tsx
    navigation-menu.tsx
    popover.tsx
    resizable-panel.tsx
    scroll-area.tsx
    select.tsx
    separator.tsx
    skeleton.tsx
    sonner.tsx
    tabs.tsx
    textarea.tsx
  server/  (4 files)
    routers/  (2 files)
      … 2 files under this directory
    index.ts
    trpc.ts
  utils/  (3 files)
    base-url.ts
    cn.ts
    construct-metadata.ts
  constants.tsx
  env.ts
  mdx-components.tsx
  middleware.ts
.editorconfig
.env.example
.gitignore
.markdownlint.json
.prettierignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
cspell.config.yaml
drizzle.config.ts
eslint.config.js
eslint.d.ts
next.config.js
package.json
postcss.config.js
prettier.config.js
reset.d.ts
tailwind.config.ts
tsconfig.json
```

## Entry points

- [src/app/(site)/page.tsx](https://github.com/noodle-run/noodle/blob/4e26fb7c990ccccce203f1c30f79126ef1bfbcaa/src/app/%28site%29/page.tsx)
- [src/db/index.ts](https://github.com/noodle-run/noodle/blob/4e26fb7c990ccccce203f1c30f79126ef1bfbcaa/src/db/index.ts)
- [src/db/schema/index.ts](https://github.com/noodle-run/noodle/blob/4e26fb7c990ccccce203f1c30f79126ef1bfbcaa/src/db/schema/index.ts)
- [src/lib/trpc/server.ts](https://github.com/noodle-run/noodle/blob/4e26fb7c990ccccce203f1c30f79126ef1bfbcaa/src/lib/trpc/server.ts)
- [src/server/index.ts](https://github.com/noodle-run/noodle/blob/4e26fb7c990ccccce203f1c30f79126ef1bfbcaa/src/server/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 3 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 30 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants.tsx package | library | Observed | Groups 1 file(s) under constants.tsx package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 8 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). |
| emails package | library | Observed | Groups 4 file(s) under emails package (observed from repository paths and static analysis). |
| env.ts package | library | Observed | Groups 1 file(s) under env.ts package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 6 file(s) under lib package (observed from repository paths and static analysis). |
| mdx-components.tsx package | library | Observed | Groups 1 file(s) under mdx-components.tsx package (observed from repository paths and static analysis). |
| middleware.ts package | library | Observed | Groups 1 file(s) under middleware.ts package (observed from repository paths and static analysis). |
| primitives package | library | Observed | Groups 17 file(s) under primitives package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 2 file(s) under server package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 3 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.env.example` (config)
- `.github/FUNDING.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yaml` (config)
- `.github/workflows/main-ci.yml` (ci)
- `.github/workflows/pr-ci.yml` (ci)
- `.github/workflows/pr-cleanup.yml` (ci)
- `.markdownlint.json` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `cspell.config.yaml` (config)
- `drizzle/meta/0000_snapshot.json` (config)
- `drizzle/meta/0001_snapshot.json` (config)
- `drizzle/meta/0002_snapshot.json` (config)
- `drizzle/meta/_journal.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 77 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `.github` — 8 analysed file(s)
- `drizzle` — 7 analysed file(s)
- `.husky` — 3 analysed file(s)
- `public` — 3 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.changeset` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `4e26fb7c990ccccce203f1c30f79126ef1bfbcaa` is the revision these paths and observations refer to.
