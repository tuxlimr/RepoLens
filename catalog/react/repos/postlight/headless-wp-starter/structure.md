# Project structure: postlight/headless-wp-starter

**Analysed commit:** `6334c8db447442bb1f01a4148a2f6e6e7d291c8e`

**Commit reference:** [6334c8db447442bb1f01a4148a2f6e6e7d291c8e](https://github.com/postlight/headless-wp-starter/commit/6334c8db447442bb1f01a4148a2f6e6e7d291c8e)

**Tree at this commit:** [postlight/headless-wp-starter@6334c8db4474](https://github.com/postlight/headless-wp-starter/tree/6334c8db447442bb1f01a4148a2f6e6e7d291c8e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | postlight/headless-wp-starter |
| Description | 🔪 WordPress + React Starter Kit: Spin up a WordPress-powered React app in one step |
| Stars | 4538 |
| Forks | 639 |
| Licence | GPL-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `6334c8db447442bb1f01a4148a2f6e6e7d291c8e` |
| Retrieved at | 2026-11-14T19:14:43.107776+00:00 |
| Files in this snapshot | 75 |

## Directory tree

```text
docker/  (3 files)
  install_wordpress.sh
  migratedb_import.sh
  postlightheadlesswpstarter.wordpress.xml
frontend/  (25 files)
  components/  (5 files)
    Footer.js
    Header.js
    Layout.js
    Menu.js
    PageWrapper.js
  pages/  (6 files)
    category.js
    index.js
    login.js
    post.js
    preview.js
    search.js
  src/  (1 files)
    styles/  (1 files)
      … 1 files under this directory
  static/  (3 files)
    images/  (3 files)
      … 3 files under this directory
  .dockerignore
  .eslintrc
  .gitignore
  .gitkeep
  .prettierrc
  config.js
  next.config.js
  package.json
  postcss.config.js
  server.js
frontend-graphql/  (23 files)
  public/  (2 files)
    index.html
    manifest.json
  src/  (16 files)
    components/  (9 files)
      … 9 files under this directory
    static/  (3 files)
      … 3 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    config.js
    constants.js
    index.js
  .eslintrc
  .gitignore
  .prettierrc
  LICENSE.txt
  package.json
wordpress/  (16 files)
  wp-content/  (14 files)
    themes/  (14 files)
      … 14 files under this directory
  .gitignore
  .htaccess
.gitignore
.travis.yml
Dockerfile
LICENSE
README.md
docker-compose.yml
itermocil.yml
package.json
```

## Entry points

- [frontend-graphql/src/components/App.js](https://github.com/postlight/headless-wp-starter/blob/6334c8db447442bb1f01a4148a2f6e6e7d291c8e/frontend-graphql/src/components/App.js)
- [frontend-graphql/src/components/Page.js](https://github.com/postlight/headless-wp-starter/blob/6334c8db447442bb1f01a4148a2f6e6e7d291c8e/frontend-graphql/src/components/Page.js)
- [frontend-graphql/src/index.js](https://github.com/postlight/headless-wp-starter/blob/6334c8db447442bb1f01a4148a2f6e6e7d291c8e/frontend-graphql/src/index.js)
- [frontend/pages/index.js](https://github.com/postlight/headless-wp-starter/blob/6334c8db447442bb1f01a4148a2f6e6e7d291c8e/frontend/pages/index.js)
- [frontend/server.js](https://github.com/postlight/headless-wp-starter/blob/6334c8db447442bb1f01a4148a2f6e6e7d291c8e/frontend/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| docker package | library | Observed | Groups 2 file(s) under docker package (observed from repository paths and static analysis). |
| frontend package | library | Observed | Groups 15 file(s) under frontend package (observed from repository paths and static analysis). |
| frontend-graphql package | library | Observed | Groups 12 file(s) under frontend-graphql package (observed from repository paths and static analysis). |
| wordpress package | library | Observed | Groups 12 file(s) under wordpress package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `frontend-graphql/package.json` (manifest)
- `frontend-graphql/public/manifest.json` (config)
- `frontend/.dockerignore` (container)
- `frontend/package.json` (manifest)
- `itermocil.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `frontend` — 25 analysed file(s)
- `frontend-graphql` — 23 analysed file(s)
- `wordpress` — 16 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `docker` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6334c8db447442bb1f01a4148a2f6e6e7d291c8e` is the revision these paths and observations refer to.
