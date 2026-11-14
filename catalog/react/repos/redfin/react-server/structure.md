# Project structure: redfin/react-server

**Analysed commit:** `572ff229d51d25515ab4b8f13cd15a87cd787f61`

**Commit reference:** [572ff229d51d25515ab4b8f13cd15a87cd787f61](https://github.com/redfin/react-server/commit/572ff229d51d25515ab4b8f13cd15a87cd787f61)

**Tree at this commit:** [redfin/react-server@572ff229d51d](https://github.com/redfin/react-server/tree/572ff229d51d25515ab4b8f13cd15a87cd787f61)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | redfin/react-server |
| Description | :rocket: Blazing fast page load and seamless navigation. |
| Stars | 3861 |
| Forks | 181 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `572ff229d51d25515ab4b8f13cd15a87cd787f61` |
| Retrieved at | 2026-11-14T19:15:03.036763+00:00 |
| Files in this snapshot | 538 |

## Directory tree

```text
docs/  (15 files)
  guides/  (8 files)
    client-transitions.md
    logging.md
    production.md
    react-server-cli.md
    understanding-rendering.md
    using-react-server-agent.md
    writing-middleware.md
    writing-pages.md
  intro/  (2 files)
    design.md
    why-react-server.md
  README.md
  _contents.json
  page-api.md
  testing-ports.md
  using-react-server-agent.md
packages/  (507 files)
  babel-plugin-react-server/  (28 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (22 files)
      … 22 files under this directory
    .gitignore
    .npmignore
    README.md
    babel.config.js
    package.json
  babel-preset-react-server/  (9 files)
    tst/  (2 files)
      … 2 files under this directory
    .eslintignore
    .gitignore
    .npmignore
    README.md
    index.js
    package.json
    test.js
  flab/  (8 files)
    .eslintignore
    .gitignore
    LAB.src.js
    README.md
    index.js
    minify.js
    package.json
    stringify.js
  generator-react-server/  (17 files)
    generators/  (12 files)
      … 12 files under this directory
    test/  (1 files)
      … 1 files under this directory
    .gitignore
    .npmignore
    README.md
    package.json
  react-server/  (52 files)
    core/  (47 files)
      … 47 files under this directory
    .gitignore
    .npmignore
    README.md
    gulpfile.js
    package.json
  react-server-cli/  (43 files)
    bin/  (1 files)
      … 1 files under this directory
    src/  (25 files)
      … 25 files under this directory
    test/  (11 files)
      … 11 files under this directory
    .babelrc
    .gitignore
    .npmignore
    README.md
    gulpfile.babel.js
    package.json
  react-server-core-middleware/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    .gitignore
    .npmignore
    README.md
    index.js
    package.json
  react-server-data-bundle-cache/  (18 files)
    src/  (12 files)
      … 12 files under this directory
    .gitignore
    .npmignore
    README.md
    gulpfile.js
    main.js
    package.json
  react-server-examples/  (97 files)
    bike-share/  (25 files)
      … 25 files under this directory
    code-splitting/  (13 files)
      … 13 files under this directory
    hello-world/  (8 files)
      … 8 files under this directory
    meteor-site/  (20 files)
      … 20 files under this directory
    redux-basic/  (10 files)
      … 10 files under this directory
    styled-components/  (17 files)
      … 17 files under this directory
    .babelrc
    .eslintignore
    README.md
    package.json
  react-server-gulp-module-tagger/  (23 files)
    test/  (19 files)
      … 19 files under this directory
    .npmignore
    README.md
    index.js
    package.json
  react-server-integration-tests/  (66 files)
    src/  (60 files)
      … 60 files under this directory
    .babelrc
    .gitignore
    README.md
    config.json
    gulpfile.babel.js
    package.json
  react-server-middleware-json-response/  (4 files)
    .gitignore
    README.md
    index.src.js
    package.json
  react-server-module-tagger/  (4 files)
    README.md
    index.js
    package.json
    test.js
  react-server-redux/  (8 files)
    src/  (3 files)
      … 3 files under this directory
    test/  (1 files)
      … 1 files under this directory
    .gitignore
    .npmignore
    gulpfile.babel.js
    package.json
  react-server-test-pages/  (49 files)
    middleware/  (1 files)
      … 1 files under this directory
    pages/  (39 files)
      … 39 files under this directory
    .eslintignore
    .gitignore
    .npmignore
    .reactserverrc
    README.md
    babel.config.js
    entrypoints.js
    package.json
    routes.js
  react-server-website/  (74 files)
    components/  (24 files)
      … 24 files under this directory
    deployment/  (9 files)
      … 9 files under this directory
    lib/  (5 files)
      … 5 files under this directory
    middleware/  (12 files)
      … 12 files under this directory
    pages/  (10 files)
      … 10 files under this directory
    .babelrc
    .dockerignore
    .eslintignore
    .gitignore
    .reactserverrc
    Dockerfile
    README.md
    build-dir-contents.js
    docker-compose.yml
    nginx.conf
    package.json
    routes.js
    running-with-docker-compose.md
    test.js
.dockerignore
.editorconfig
.eslintrc
.gitattributes
.gitignore
.travis.yml
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
MAINTAINING.md
README.md
babel.config.js
lerna.json
package.json
```

## Entry points

- [packages/babel-preset-react-server/index.js](https://github.com/redfin/react-server/blob/572ff229d51d25515ab4b8f13cd15a87cd787f61/packages/babel-preset-react-server/index.js)
- [packages/flab/index.js](https://github.com/redfin/react-server/blob/572ff229d51d25515ab4b8f13cd15a87cd787f61/packages/flab/index.js)
- [packages/generator-react-server/generators/app/index.js](https://github.com/redfin/react-server/blob/572ff229d51d25515ab4b8f13cd15a87cd787f61/packages/generator-react-server/generators/app/index.js)
- [packages/react-server-cli/bin/react-server-cli](https://github.com/redfin/react-server/blob/572ff229d51d25515ab4b8f13cd15a87cd787f61/packages/react-server-cli/bin/react-server-cli)
- [packages/react-server-core-middleware/index.js](https://github.com/redfin/react-server/blob/572ff229d51d25515ab4b8f13cd15a87cd787f61/packages/react-server-core-middleware/index.js)
- [packages/react-server-examples/hello-world/HelloWorld.js](https://github.com/redfin/react-server/blob/572ff229d51d25515ab4b8f13cd15a87cd787f61/packages/react-server-examples/hello-world/HelloWorld.js)
- [packages/react-server-gulp-module-tagger/index.js](https://github.com/redfin/react-server/blob/572ff229d51d25515ab4b8f13cd15a87cd787f61/packages/react-server-gulp-module-tagger/index.js)
- [packages/react-server-module-tagger/index.js](https://github.com/redfin/react-server/blob/572ff229d51d25515ab4b8f13cd15a87cd787f61/packages/react-server-module-tagger/index.js)
- [packages/babel-plugin-react-server/src/index.js](https://github.com/redfin/react-server/blob/572ff229d51d25515ab4b8f13cd15a87cd787f61/packages/babel-plugin-react-server/src/index.js)
- [packages/react-server-cli/src/index.js](https://github.com/redfin/react-server/blob/572ff229d51d25515ab4b8f13cd15a87cd787f61/packages/react-server-cli/src/index.js)
- [packages/react-server-data-bundle-cache/main.js](https://github.com/redfin/react-server/blob/572ff229d51d25515ab4b8f13cd15a87cd787f61/packages/react-server-data-bundle-cache/main.js)
- [packages/react-server-data-bundle-cache/src/index.js](https://github.com/redfin/react-server/blob/572ff229d51d25515ab4b8f13cd15a87cd787f61/packages/react-server-data-bundle-cache/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 2 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 42 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 241 file(s) under packages package (observed from repository paths and static analysis). Observed top-level classes: Ec2Inventory. |
| Service / domain layer | service | Observed | Groups 46 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 55 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.travis.yml` (ci)
- `Dockerfile` (container)
- `docs/_contents.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/babel-plugin-react-server/package.json` (manifest)
- `packages/babel-preset-react-server/package.json` (manifest)
- `packages/flab/package.json` (manifest)
- `packages/generator-react-server/generators/app/templates/Dockerfile` (container)
- `packages/generator-react-server/generators/app/templates/docker-compose.yml` (container)
- `packages/generator-react-server/generators/app/templates/package.json` (manifest)
- `packages/generator-react-server/generators/app/templates/routes.json` (config)
- `packages/generator-react-server/package.json` (manifest)
- `packages/react-server-cli/package.json` (manifest)
- `packages/react-server-core-middleware/package.json` (manifest)
- `packages/react-server-data-bundle-cache/package.json` (manifest)
- `packages/react-server-examples/bike-share/Dockerfile` (container)
- `packages/react-server-examples/bike-share/docker-compose.yml` (container)
- `packages/react-server-examples/bike-share/package.json` (manifest)
- `packages/react-server-examples/code-splitting/package.json` (manifest)
- `packages/react-server-examples/hello-world/package.json` (manifest)
- `packages/react-server-examples/meteor-site/package.json` (manifest)
- `packages/react-server-examples/meteor-site/routes.json` (config)
- `packages/react-server-examples/package.json` (manifest)
- `packages/react-server-examples/redux-basic/package.json` (manifest)
- `packages/react-server-examples/styled-components/package.json` (manifest)
- `packages/react-server-examples/styled-components/routes.json` (config)
- `packages/react-server-gulp-module-tagger/package.json` (manifest)
- `packages/react-server-integration-tests/config.json` (config)
- `packages/react-server-integration-tests/package.json` (manifest)
- `packages/react-server-middleware-json-response/package.json` (manifest)
- `packages/react-server-module-tagger/package.json` (manifest)
- `packages/react-server-redux/package.json` (manifest)
- `packages/react-server-test-pages/package.json` (manifest)
- `packages/react-server-website/.dockerignore` (container)
- `packages/react-server-website/Dockerfile` (container)
- `packages/react-server-website/deployment/deploy.yml` (config)
- `packages/react-server-website/deployment/docker-compose.yml` (container)
- `packages/react-server-website/deployment/ec2.ini` (config)
- `packages/react-server-website/deployment/requirements.txt` (manifest)
- `packages/react-server-website/deployment/setup.yml` (config)
- `packages/react-server-website/docker-compose.yml` (container)
- `packages/react-server-website/package.json` (manifest)
- `packages/react-server/package.json` (manifest)

## Top-level layout

- `packages` — 507 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `docs` — 15 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (2 x likely secret file excluded; 2 x lockfile excluded).
- File packages/react-server-website/deployment/decrypt_credentials.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File packages/react-server-website/deployment/encrypt_credentials.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `572ff229d51d25515ab4b8f13cd15a87cd787f61` is the revision these paths and observations refer to.
