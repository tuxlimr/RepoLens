# Project structure: PatrickJS/angular-webpack-starter

**Analysed commit:** `23ef49ac3f5dcebde5845a68b62b3d000ade72d0`

**Commit reference:** [23ef49ac3f5dcebde5845a68b62b3d000ade72d0](https://github.com/PatrickJS/angular-webpack-starter/commit/23ef49ac3f5dcebde5845a68b62b3d000ade72d0)

**Tree at this commit:** [PatrickJS/angular-webpack-starter@23ef49ac3f5d](https://github.com/PatrickJS/angular-webpack-starter/tree/23ef49ac3f5dcebde5845a68b62b3d000ade72d0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | PatrickJS/angular-webpack-starter |
| Description | Angular Webpack Starter |
| Stars | 10208 |
| Forks | 4673 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `23ef49ac3f5dcebde5845a68b62b3d000ade72d0` |
| Retrieved at | 2026-11-14T19:12:43.090277+00:00 |
| Files in this snapshot | 114 |

## Directory tree

```text
.github/  (4 files)
  CONTRIBUTING.md
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
.vscode/  (2 files)
  launch.json
  settings.json
config/  (19 files)
  github-deploy/  (1 files)
    index.js
  html-elements-plugin/  (1 files)
    index.js
  build-utils.js
  config.common.json
  config.dev.json
  config.prod.json
  empty.js
  head-config.common.js
  helpers.js
  karma.conf.js
  nginx-custom.conf
  protractor.conf.js
  resource-override.js
  spec-bundle.js
  webpack.common.js
  webpack.dev.js
  webpack.github-deploy.js
  webpack.prod.js
  webpack.test.js
src/  (67 files)
  app/  (46 files)
    +barrel/  (8 files)
      … 8 files under this directory
    +detail/  (8 files)
      … 8 files under this directory
    +dev-module/  (4 files)
      … 4 files under this directory
    about/  (3 files)
      … 3 files under this directory
    home/  (12 files)
      … 12 files under this directory
    no-content/  (2 files)
      … 2 files under this directory
    app.component.css
    app.component.spec.ts
    app.component.ts
    app.e2e.ts
    app.module.ts
    app.resolver.ts
    app.routes.ts
    app.service.ts
    index.ts
  assets/  (8 files)
    css/  (1 files)
      … 1 files under this directory
    icon/  (1 files)
      … 1 files under this directory
    mock-data/  (1 files)
      … 1 files under this directory
    data.json
    humans.txt
    manifest.json
    robots.txt
    service-worker.js
  environments/  (4 files)
    environment.e2e.prod.ts
    environment.prod.ts
    environment.ts
    model.ts
  meta/  (2 files)
    humans.txt
    robots.txt
  styles/  (3 files)
    _variables.scss
    headings.css
    styles.scss
  custom-typings.d.ts
  index.html
  main.browser.ts
  polyfills.browser.ts
.dockerignore
.editorconfig
.gitattributes
.gitignore
.nvmrc
.travis.yml
Dockerfile
Dockerfile-dev
LICENSE
README.md
docker-compose.yml
firebase.json
karma.conf.js
netlify.toml
package.json
protractor.conf.js
sonar-project.properties
tsconfig.json
tsconfig.webpack.json
tslint.json
typedoc.json
webpack.config.js
```

## Entry points

- [config/github-deploy/index.js](https://github.com/PatrickJS/angular-webpack-starter/blob/23ef49ac3f5dcebde5845a68b62b3d000ade72d0/config/github-deploy/index.js)
- [config/html-elements-plugin/index.js](https://github.com/PatrickJS/angular-webpack-starter/blob/23ef49ac3f5dcebde5845a68b62b3d000ade72d0/config/html-elements-plugin/index.js)
- [src/app/+barrel/index.ts](https://github.com/PatrickJS/angular-webpack-starter/blob/23ef49ac3f5dcebde5845a68b62b3d000ade72d0/src/app/%2Bbarrel/index.ts)
- [src/app/+detail/index.ts](https://github.com/PatrickJS/angular-webpack-starter/blob/23ef49ac3f5dcebde5845a68b62b3d000ade72d0/src/app/%2Bdetail/index.ts)
- [src/app/+dev-module/index.ts](https://github.com/PatrickJS/angular-webpack-starter/blob/23ef49ac3f5dcebde5845a68b62b3d000ade72d0/src/app/%2Bdev-module/index.ts)
- [src/app/about/index.ts](https://github.com/PatrickJS/angular-webpack-starter/blob/23ef49ac3f5dcebde5845a68b62b3d000ade72d0/src/app/about/index.ts)
- [src/app/home/index.ts](https://github.com/PatrickJS/angular-webpack-starter/blob/23ef49ac3f5dcebde5845a68b62b3d000ade72d0/src/app/home/index.ts)
- [src/app/index.ts](https://github.com/PatrickJS/angular-webpack-starter/blob/23ef49ac3f5dcebde5845a68b62b3d000ade72d0/src/app/index.ts)
- [src/app/no-content/index.ts](https://github.com/PatrickJS/angular-webpack-starter/blob/23ef49ac3f5dcebde5845a68b62b3d000ade72d0/src/app/no-content/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 43 file(s) under app package (observed from repository paths and static analysis). |
| assets package | library | Observed | Groups 1 file(s) under assets package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 31 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| custom-typings.d.ts package | library | Observed | Groups 1 file(s) under custom-typings.d.ts package (observed from repository paths and static analysis). |
| environments package | library | Observed | Groups 4 file(s) under environments package (observed from repository paths and static analysis). |
| main.browser.ts package | library | Observed | Groups 1 file(s) under main.browser.ts package (observed from repository paths and static analysis). |
| polyfills.browser.ts package | library | Observed | Groups 1 file(s) under polyfills.browser.ts package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.travis.yml` (ci)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `Dockerfile-dev` (container)
- `config/config.common.json` (config)
- `config/config.dev.json` (config)
- `config/config.prod.json` (config)
- `docker-compose.yml` (container)
- `firebase.json` (config)
- `netlify.toml` (config)
- `package.json` (manifest)
- `src/assets/data.json` (config)
- `src/assets/manifest.json` (config)
- `src/assets/mock-data/mock-data.json` (config)
- `tsconfig.json` (config)
- `tsconfig.webpack.json` (config)
- `tslint.json` (config)
- `typedoc.json` (config)

## Top-level layout

- `src` — 67 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `config` — 19 analysed file(s)
- `.github` — 4 analysed file(s)
- `.vscode` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `23ef49ac3f5dcebde5845a68b62b3d000ade72d0` is the revision these paths and observations refer to.
