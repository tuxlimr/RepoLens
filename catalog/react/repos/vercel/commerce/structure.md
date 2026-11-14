# Project structure: vercel/commerce

**Analysed commit:** `f7521d57d29f0eb3d23c1399cf9bb299d61fcd21`

**Commit reference:** [f7521d57d29f0eb3d23c1399cf9bb299d61fcd21](https://github.com/vercel/commerce/commit/f7521d57d29f0eb3d23c1399cf9bb299d61fcd21)

**Tree at this commit:** [vercel/commerce@f7521d57d29f](https://github.com/vercel/commerce/tree/f7521d57d29f0eb3d23c1399cf9bb299d61fcd21)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vercel/commerce |
| Description | Next.js Commerce |
| Stars | 14309 |
| Forks | 5449 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `f7521d57d29f0eb3d23c1399cf9bb299d61fcd21` |
| Retrieved at | 2026-11-14T19:13:16.986142+00:00 |
| Files in this snapshot | 75 |

## Directory tree

```text
.vscode/  (2 files)
  launch.json
  settings.json
app/  (18 files)
  [page]/  (3 files)
    layout.tsx
    opengraph-image.tsx
    page.tsx
  api/  (1 files)
    revalidate/  (1 files)
      … 1 files under this directory
  product/  (1 files)
    [handle]/  (1 files)
      … 1 files under this directory
  search/  (6 files)
    [collection]/  (2 files)
      … 2 files under this directory
    children-wrapper.tsx
    layout.tsx
    loading.tsx
    page.tsx
  error.tsx
  globals.css
  layout.tsx
  opengraph-image.tsx
  page.tsx
  robots.ts
  sitemap.ts
components/  (32 files)
  cart/  (7 files)
    actions.ts
    add-to-cart.tsx
    cart-context.tsx
    delete-item-button.tsx
    edit-item-quantity-button.tsx
    modal.tsx
    open-cart.tsx
  grid/  (3 files)
    index.tsx
    three-items.tsx
    tile.tsx
  icons/  (1 files)
    logo.tsx
  layout/  (10 files)
    navbar/  (3 files)
      … 3 files under this directory
    search/  (4 files)
      … 4 files under this directory
    footer-menu.tsx
    footer.tsx
    product-grid-items.tsx
  product/  (3 files)
    gallery.tsx
    product-description.tsx
    variant-selector.tsx
  carousel.tsx
  label.tsx
  loading-dots.tsx
  logo-square.tsx
  opengraph-image.tsx
  price.tsx
  prose.tsx
  welcome-toast.tsx
lib/  (15 files)
  shopify/  (12 files)
    fragments/  (4 files)
      … 4 files under this directory
    mutations/  (1 files)
      … 1 files under this directory
    queries/  (5 files)
      … 5 files under this directory
    index.ts
    types.ts
  constants.ts
  type-guards.ts
  utils.ts
.env.example
.gitignore
README.md
license.md
next.config.ts
package.json
postcss.config.mjs
tsconfig.json
```

## Entry points

- [app/[page]/page.tsx](https://github.com/vercel/commerce/blob/f7521d57d29f0eb3d23c1399cf9bb299d61fcd21/app/%5Bpage%5D/page.tsx)
- [app/page.tsx](https://github.com/vercel/commerce/blob/f7521d57d29f0eb3d23c1399cf9bb299d61fcd21/app/page.tsx)
- [app/product/[handle]/page.tsx](https://github.com/vercel/commerce/blob/f7521d57d29f0eb3d23c1399cf9bb299d61fcd21/app/product/%5Bhandle%5D/page.tsx)
- [app/search/[collection]/page.tsx](https://github.com/vercel/commerce/blob/f7521d57d29f0eb3d23c1399cf9bb299d61fcd21/app/search/%5Bcollection%5D/page.tsx)
- [app/search/page.tsx](https://github.com/vercel/commerce/blob/f7521d57d29f0eb3d23c1399cf9bb299d61fcd21/app/search/page.tsx)
- [components/grid/index.tsx](https://github.com/vercel/commerce/blob/f7521d57d29f0eb3d23c1399cf9bb299d61fcd21/components/grid/index.tsx)
- [components/layout/navbar/index.tsx](https://github.com/vercel/commerce/blob/f7521d57d29f0eb3d23c1399cf9bb299d61fcd21/components/layout/navbar/index.tsx)
- [lib/shopify/index.ts](https://github.com/vercel/commerce/blob/f7521d57d29f0eb3d23c1399cf9bb299d61fcd21/lib/shopify/index.ts)
- [lib/shopify/queries/page.ts](https://github.com/vercel/commerce/blob/f7521d57d29f0eb3d23c1399cf9bb299d61fcd21/lib/shopify/queries/page.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 16 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 32 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 15 file(s) under lib package (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `components` — 32 analysed file(s)
- `app` — 18 analysed file(s)
- `lib` — 15 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.vscode` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `f7521d57d29f0eb3d23c1399cf9bb299d61fcd21` is the revision these paths and observations refer to.
