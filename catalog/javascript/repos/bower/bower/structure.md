# Project structure: bower/bower

**Analysed commit:** `4e0c3c1181c21624c5b3ab5bdf5d3becdb172b5a`

**Commit reference:** [4e0c3c1181c21624c5b3ab5bdf5d3becdb172b5a](https://github.com/bower/bower/commit/4e0c3c1181c21624c5b3ab5bdf5d3becdb172b5a)

**Tree at this commit:** [bower/bower@4e0c3c1181c2](https://github.com/bower/bower/tree/4e0c3c1181c21624c5b3ab5bdf5d3becdb172b5a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | bower/bower |
| Description | A package manager for the web |
| Stars | 14892 |
| Forks | 1787 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `4e0c3c1181c21624c5b3ab5bdf5d3becdb172b5a` |
| Retrieved at | 2026-11-14T19:11:42.053913+00:00 |
| Files in this snapshot | 246 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (1 files)
    nodejs.yml
  FUNDING.yml
  ISSUE_TEMPLATE.md
bin/  (1 files)
  bower
lib/  (98 files)
  bin/  (1 files)
    bower.js
  commands/  (19 files)
    cache/  (2 files)
      … 2 files under this directory
    help.js
    home.js
    index.js
    info.js
    init.js
    install.js
    link.js
    list.js
    login.js
    lookup.js
    prune.js
    register.js
    search.js
    uninstall.js
    unregister.js
    update.js
    version.js
  core/  (16 files)
    resolvers/  (10 files)
      … 10 files under this directory
    Manager.js
    PackageRepository.js
    Project.js
    ResolveCache.js
    resolverFactory.js
    scripts.js
  renderers/  (3 files)
    JsonRenderer.js
    StandardRenderer.js
    index.js
  templates/  (34 files)
    helpers/  (6 files)
      … 6 files under this directory
    json/  (19 files)
      … 19 files under this directory
    std/  (9 files)
      … 9 files under this directory
  util/  (22 files)
    abbreviations.js
    childProcess.js
    cli.js
    cmd.js
    copy.js
    createError.js
    createLink.js
    download.js
    extract.js
    fs.js
    isPathAbsolute.js
    readJson.js
    relativeToBaseDir.js
    removeIgnores.js
    resolve.js
    rimraf.js
    rootCheck.js
    semver.js
    template.js
    userAgent.js
    validLink.js
    which.js
  config.js
  index.js
  version.js
packages/  (78 files)
  bower-config/  (22 files)
    lib/  (6 files)
      … 6 files under this directory
    test/  (10 files)
      … 10 files under this directory
    .editorconfig
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  bower-endpoint-parser/  (7 files)
    test/  (1 files)
      … 1 files under this directory
    .editorconfig
    .gitignore
    LICENSE
    README.md
    index.js
    package.json
  bower-json/  (17 files)
    lib/  (4 files)
      … 4 files under this directory
    test/  (7 files)
      … 7 files under this directory
    .editorconfig
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    package.json
  bower-logger/  (7 files)
    lib/  (1 files)
      … 1 files under this directory
    test/  (1 files)
      … 1 files under this directory
    .editorconfig
    .gitignore
    LICENSE
    README.md
    package.json
  bower-registry-client/  (25 files)
    lib/  (9 files)
      … 9 files under this directory
    test/  (10 files)
      … 10 files under this directory
    .editorconfig
    .gitignore
    Client.js
    LICENSE
    README.md
    package.json
test/  (54 files)
  assets/  (3 files)
    resolve-cache/  (1 files)
      … 1 files under this directory
    test-temp-dir/  (2 files)
      … 2 files under this directory
  commands/  (20 files)
    cache/  (2 files)
      … 2 files under this directory
    bower.js
    help.js
    home.js
    index.js
    info.js
    init.js
    install.js
    link.js
    list.js
    login.js
    lookup.js
    prune.js
    register.js
    search.js
    uninstall.js
    unregister.js
    update.js
    version.js
  core/  (14 files)
    resolvers/  (9 files)
      … 9 files under this directory
    Manager.js
    packageRepository.js
    resolveCache.js
    resolverFactory.js
    scripts.js
  renderers/  (2 files)
    JsonRenderer.js
    StandardRenderer.js
  sample/  (1 files)
    bower.json
  util/  (8 files)
    createLink.js
    download.js
    index.js
    isPathAbsolute.js
    nock.js
    relativeToBaseDir.js
    removeIgnores.js
    template.js
  helpers.js
  packages-svn.js
  packages-svn.json
  packages.js
  packages.json
  test.js
.editorconfig
.eslintignore
.eslintrc
.gitignore
.prettierignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
package.json
publish.js
```

## Entry points

- [bin/bower](https://github.com/bower/bower/blob/4e0c3c1181c21624c5b3ab5bdf5d3becdb172b5a/bin/bower)
- [packages/bower-endpoint-parser/index.js](https://github.com/bower/bower/blob/4e0c3c1181c21624c5b3ab5bdf5d3becdb172b5a/packages/bower-endpoint-parser/index.js)
- [lib/commands/index.js](https://github.com/bower/bower/blob/4e0c3c1181c21624c5b3ab5bdf5d3becdb172b5a/lib/commands/index.js)
- [lib/core/resolvers/index.js](https://github.com/bower/bower/blob/4e0c3c1181c21624c5b3ab5bdf5d3becdb172b5a/lib/core/resolvers/index.js)
- [lib/index.js](https://github.com/bower/bower/blob/4e0c3c1181c21624c5b3ab5bdf5d3becdb172b5a/lib/index.js)
- [lib/renderers/index.js](https://github.com/bower/bower/blob/4e0c3c1181c21624c5b3ab5bdf5d3becdb172b5a/lib/renderers/index.js)
- [lib/templates/helpers/index.js](https://github.com/bower/bower/blob/4e0c3c1181c21624c5b3ab5bdf5d3becdb172b5a/lib/templates/helpers/index.js)
- [packages/bower-registry-client/lib/index.js](https://github.com/bower/bower/blob/4e0c3c1181c21624c5b3ab5bdf5d3becdb172b5a/packages/bower-registry-client/lib/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 30 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 54 file(s) under lib package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 22 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 16 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 83 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/nodejs.yml` (ci)
- `lib/templates/json/help-cache.json` (config)
- `lib/templates/json/help-cache/clean.json` (config)
- `lib/templates/json/help-cache/list.json` (config)
- `lib/templates/json/help-home.json` (config)
- `lib/templates/json/help-info.json` (config)
- `lib/templates/json/help-init.json` (config)
- `lib/templates/json/help-install.json` (config)
- `lib/templates/json/help-link.json` (config)
- `lib/templates/json/help-list.json` (config)
- `lib/templates/json/help-login.json` (config)
- `lib/templates/json/help-lookup.json` (config)
- `lib/templates/json/help-prune.json` (config)
- `lib/templates/json/help-register.json` (config)
- `lib/templates/json/help-search.json` (config)
- `lib/templates/json/help-uninstall.json` (config)
- `lib/templates/json/help-unregister.json` (config)
- `lib/templates/json/help-update.json` (config)
- `lib/templates/json/help-version.json` (config)
- `lib/templates/json/help.json` (config)
- `package.json` (manifest)
- `packages/bower-config/.editorconfig` (config)
- `packages/bower-config/package.json` (manifest)
- `packages/bower-endpoint-parser/.editorconfig` (config)
- `packages/bower-endpoint-parser/package.json` (manifest)
- `packages/bower-json/.editorconfig` (config)
- `packages/bower-json/package.json` (manifest)
- `packages/bower-logger/.editorconfig` (config)
- `packages/bower-logger/package.json` (manifest)
- `packages/bower-registry-client/.editorconfig` (config)
- `packages/bower-registry-client/package.json` (manifest)

## Top-level layout

- `lib` — 98 analysed file(s)
- `packages` — 78 analysed file(s)
- `test` — 54 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 3 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (1 x lockfile excluded; 2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4e0c3c1181c21624c5b3ab5bdf5d3becdb172b5a` is the revision these paths and observations refer to.
