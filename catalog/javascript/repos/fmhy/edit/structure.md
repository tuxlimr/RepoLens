# Project structure: fmhy/edit

**Analysed commit:** `0450bd41abe146ff23887131105489f5139ac730`

**Commit reference:** [0450bd41abe146ff23887131105489f5139ac730](https://github.com/fmhy/edit/commit/0450bd41abe146ff23887131105489f5139ac730)

**Tree at this commit:** [fmhy/edit@0450bd41abe1](https://github.com/fmhy/edit/tree/0450bd41abe146ff23887131105489f5139ac730)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | fmhy/edit |
| Description | Make changes to FMHY |
| Stars | 12818 |
| Forks | 3339 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `0450bd41abe146ff23887131105489f5139ac730` |
| Retrieved at | 2026-11-14T19:12:03.533225+00:00 |
| Files in this snapshot | 318 |

## Directory tree

```text
.devcontainer/  (1 files)
  devcontainer.json
.github/  (15 files)
  ISSUE_TEMPLATE/  (1 files)
    wiki.yml
  assets/  (5 files)
    bluesky.svg
    discord.svg
    firefish.svg
    github.svg
    nginx.conf
  workflows/  (4 files)
    deploy-api.yml
    deploy-gh-pages.yml
    labeler.yml
    pr-checks.yml
  CODEOWNERS
  CONTRIBUTING.md
  POST_TEMPLATE.md
  README.md
  labeler.yml
api/  (7 files)
  middleware/  (2 files)
    cors.ts
    ratelimit.ts
  routes/  (3 files)
    feedback.post.ts
    index.ts
    single-page.ts
  README.md
  tsconfig.json
docs/  (274 files)
  .vitepress/  (180 files)
    hooks/  (4 files)
      … 4 files under this directory
    markdown/  (4 files)
      … 4 files under this directory
    notes/  (105 files)
      … 105 files under this directory
    theme/  (53 files)
      … 53 files under this directory
    transformer/  (3 files)
      … 3 files under this directory
    types/  (1 files)
      … 1 files under this directory
    utils/  (2 files)
      … 2 files under this directory
    LICENSE
    README.md
    config.mts
    constants.ts
    shared.ts
    transformer.ts
    utils.ts
    vue-shim.d.ts
  other/  (5 files)
    FAQ.md
    backups.md
    contributing.md
    selfhosting.md
    wallpapers.md
  posts/  (53 files)
    FCC.md
    Internet-Archive.md
    KeepAndroidOpen.md
    Nov-2025.md
    WWH.md
    april-2023.md
    april-2024.md
    april-2025.md
    april-2026.md
    aug-2023.md
    aug-2024.md
    aug-2025.md
    aug-2026.md
    changelog-sites.md
    dec-2023.md
    dec-2024.md
    dec-2025.md
    discord.md
    feb-2024.md
    feb-2025.md
    feb-2026.md
    jan-2024.md
    jan-2025.md
    jan-2026.md
    … 29 more files
  public/  (6 files)
    _headers
    key.txt
    logo-uwu.svg
    manifest.json
    note.svg
    robots.txt
  ai.md
  audio.md
  beginners-guide.md
  developer-tools.md
  downloading.md
  educational.md
  feedback.md
  file-tools.md
  gaming-tools.md
  gaming.md
  image-tools.md
  index.md
  internet-tools.md
  linux-macos.md
  misc.md
  mobile.md
  non-english.md
  posts.md
  privacy.md
  reading.md
  sandbox.md
  social-media-tools.md
  startpage.md
  storage.md
  … 6 more files
scripts/  (5 files)
  generate-removed.js
  generate-single-page.js
  lint-markdown.js
  mirror-links.test.mjs
  pre-commit.sh
.dockerignore
.editorconfig
.lintstagedrc.format.json
.prettierignore
.prettierrc.yaml
Dockerfile
docker-compose.yaml
eslint.config.js
flake.lock
flake.nix
nitro.config.ts
package.json
pnpm-workspace.yaml
tsconfig.json
unocss.config.ts
wrangler.toml
```

## Entry points

- [api/routes/index.ts](https://github.com/fmhy/edit/blob/0450bd41abe146ff23887131105489f5139ac730/api/routes/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 5 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.devcontainer/devcontainer.json` (config)
- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/wiki.yml` (config)
- `.github/labeler.yml` (config)
- `.github/workflows/deploy-api.yml` (ci)
- `.github/workflows/deploy-gh-pages.yml` (ci)
- `.github/workflows/labeler.yml` (ci)
- `.github/workflows/pr-checks.yml` (ci)
- `.lintstagedrc.format.json` (config)
- `.prettierrc.yaml` (config)
- `Dockerfile` (container)
- `api/tsconfig.json` (config)
- `docker-compose.yaml` (container)
- `docs/.vitepress/transformer/headers.json` (config)
- `docs/public/manifest.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `wrangler.toml` (config)

## Top-level layout

- `docs` — 274 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 15 analysed file(s)
- `api` — 7 analysed file(s)
- `scripts` — 5 analysed file(s)
- `.devcontainer` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0450bd41abe146ff23887131105489f5139ac730` is the revision these paths and observations refer to.
