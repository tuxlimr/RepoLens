# Project structure: digitalocean/nginxconfig.io

**Analysed commit:** `dd290c0b706b8a8c2f86cfbffaae9c17715b431d`

**Commit reference:** [dd290c0b706b8a8c2f86cfbffaae9c17715b431d](https://github.com/digitalocean/nginxconfig.io/commit/dd290c0b706b8a8c2f86cfbffaae9c17715b431d)

**Tree at this commit:** [digitalocean/nginxconfig.io@dd290c0b706b](https://github.com/digitalocean/nginxconfig.io/tree/dd290c0b706b8a8c2f86cfbffaae9c17715b431d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | digitalocean/nginxconfig.io |
| Description | ⚙️ NGINX config generator on steroids 💉 |
| Stars | 28244 |
| Forks | 2030 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `dd290c0b706b8a8c2f86cfbffaae9c17715b431d` |
| Retrieved at | 2026-11-14T19:10:49.937659+00:00 |
| Files in this snapshot | 515 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    help.md
    report-a-bug.md
    request-a-feature.md
  workflows/  (3 files)
    do-spaces-workflow.yml
    gh-pages-workflow.yml
    test-workflow.yml
  PULL_REQUEST_TEMPLATE.md
.husky/  (1 files)
  pre-commit
src/  (494 files)
  nginxconfig/  (493 files)
    generators/  (17 files)
      … 17 files under this directory
    i18n/  (398 files)
      … 398 files under this directory
    scss/  (13 files)
      … 13 files under this directory
    templates/  (39 files)
      … 39 files under this directory
    util/  (25 files)
      … 25 files under this directory
    mount.js
  static/  (1 files)
    robots.txt
test/  (1 files)
  testBrowserLanguage.js
.babelrc
.editorconfig
.eslintrc.cjs
.gitignore
.lintstagedrc.json
.nvmrc
.prettierignore
.prettierrc.json
LICENSE
README.md
package.json
vue.config.js
```

## Entry points

- [src/nginxconfig/mount.js](https://github.com/digitalocean/nginxconfig.io/blob/dd290c0b706b8a8c2f86cfbffaae9c17715b431d/src/nginxconfig/mount.js)
- [src/nginxconfig/generators/index.js](https://github.com/digitalocean/nginxconfig.io/blob/dd290c0b706b8a8c2f86cfbffaae9c17715b431d/src/nginxconfig/generators/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| nginxconfig package | library | Observed | Groups 468 file(s) under nginxconfig package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/do-spaces-workflow.yml` (ci)
- `.github/workflows/gh-pages-workflow.yml` (ci)
- `.github/workflows/test-workflow.yml` (ci)
- `.lintstagedrc.json` (config)
- `.prettierrc.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 494 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 7 analysed file(s)
- `.husky` — 1 analysed file(s)
- `test` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `dd290c0b706b8a8c2f86cfbffaae9c17715b431d` is the revision these paths and observations refer to.
