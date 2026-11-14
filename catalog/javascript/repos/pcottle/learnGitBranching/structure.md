# Project structure: pcottle/learnGitBranching

**Analysed commit:** `6b9db44494ad62922c73936c5cef14b57492ae94`

**Commit reference:** [6b9db44494ad62922c73936c5cef14b57492ae94](https://github.com/pcottle/learnGitBranching/commit/6b9db44494ad62922c73936c5cef14b57492ae94)

**Tree at this commit:** [pcottle/learnGitBranching@6b9db44494ad](https://github.com/pcottle/learnGitBranching/tree/6b9db44494ad62922c73936c5cef14b57492ae94)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pcottle/learnGitBranching |
| Description | An interactive git visualization and tutorial. Aspiring students of git can use this app to educate and challenge themselves towards mastery of git! |
| Stars | 34224 |
| Forks | 6036 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `6b9db44494ad62922c73936c5cef14b57492ae94` |
| Retrieved at | 2026-11-14T19:10:44.615574+00:00 |
| Files in this snapshot | 195 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (2 files)
    build-docker.yml
    pages.yml
  FUNDING.yml
  dependabot.yml
  settings.yml
__tests__/  (33 files)
  CommandLineStore.spec.js
  GlobalStateStore.spec.js
  LevelStore.spec.js
  LocaleStore.spec.js
  animation.spec.js
  appInit.spec.js
  base.js
  certificate.spec.js
  cloneSemantics.spec.js
  collections.spec.js
  commandLine.spec.js
  commandModel.spec.js
  commandParsing.spec.js
  create.js
  errors.spec.js
  eventEmitter.spec.js
  generatedArtifacts.spec.js
  git.spec.js
  intl.spec.js
  levelUndoBookkeeping.spec.js
  levels.spec.js
  mercurial.spec.js
  optionParser.spec.js
  remote.spec.js
  … 9 more files
assets/  (1 files)
  font/  (1 files)
    fontawesome-webfont.svg
generatedDocs/  (2 files)
  github-markdown.css
  levels.html
scripts/  (9 files)
  check-package-manager.js
  extract-translation-template.js
  generate.js
  generateIntlStrings.js
  generateLevelDocs.js
  generateLevelManifest.js
  postbuild.js
  translate.js
  validate-locale.js
spec/  (1 files)
  support/  (1 files)
    jasmine.json
src/  (126 files)
  js/  (86 files)
    actions/  (4 files)
      … 4 files under this directory
    app/  (1 files)
      … 1 files under this directory
    commands/  (2 files)
      … 2 files under this directory
    constants/  (1 files)
      … 1 files under this directory
    dialogs/  (4 files)
      … 4 files under this directory
    dispatcher/  (1 files)
      … 1 files under this directory
    git/  (4 files)
      … 4 files under this directory
    graph/  (2 files)
      … 2 files under this directory
    intl/  (3 files)
      … 3 files under this directory
    level/  (7 files)
      … 7 files under this directory
    log/  (1 files)
      … 1 files under this directory
    mercurial/  (1 files)
      … 1 files under this directory
    models/  (2 files)
      … 2 files under this directory
    react_views/  (7 files)
      … 7 files under this directory
    sandbox/  (2 files)
      … 2 files under this directory
    stores/  (4 files)
      … 4 files under this directory
    util/  (21 files)
      … 21 files under this directory
    views/  (8 files)
      … 8 files under this directory
    visuals/  (11 files)
      … 11 files under this directory
  levels/  (36 files)
    advanced/  (1 files)
      … 1 files under this directory
    intro/  (4 files)
      … 4 files under this directory
    mixed/  (5 files)
      … 5 files under this directory
    rampup/  (6 files)
      … 6 files under this directory
    rebase/  (2 files)
      … 2 files under this directory
    remote/  (14 files)
      … 14 files under this directory
    workingDir/  (2 files)
      … 2 files under this directory
    index.js
    sequenceInfo.js
  style/  (4 files)
    font-awesome.css
    index.css
    main.css
    rainbows.css
.dockerignore
.editorconfig
.gitignore
.gitpod.yml
.nvmrc
CLAUDE.md
CNAME
CONTRIBUTING.md
Dockerfile
LICENSE.md
Makefile
README.md
TRANSLATING.md
eslint.config.js
index.html
netlify.toml
package.json
vite.config.mjs
```

## Entry points

- [src/js/app/index.js](https://github.com/pcottle/learnGitBranching/blob/6b9db44494ad62922c73936c5cef14b57492ae94/src/js/app/index.js)
- [src/js/commands/index.js](https://github.com/pcottle/learnGitBranching/blob/6b9db44494ad62922c73936c5cef14b57492ae94/src/js/commands/index.js)
- [src/js/git/index.js](https://github.com/pcottle/learnGitBranching/blob/6b9db44494ad62922c73936c5cef14b57492ae94/src/js/git/index.js)
- [src/js/graph/index.js](https://github.com/pcottle/learnGitBranching/blob/6b9db44494ad62922c73936c5cef14b57492ae94/src/js/graph/index.js)
- [src/js/intl/index.js](https://github.com/pcottle/learnGitBranching/blob/6b9db44494ad62922c73936c5cef14b57492ae94/src/js/intl/index.js)
- [src/js/level/index.js](https://github.com/pcottle/learnGitBranching/blob/6b9db44494ad62922c73936c5cef14b57492ae94/src/js/level/index.js)
- [src/js/log/index.js](https://github.com/pcottle/learnGitBranching/blob/6b9db44494ad62922c73936c5cef14b57492ae94/src/js/log/index.js)
- [src/js/sandbox/index.js](https://github.com/pcottle/learnGitBranching/blob/6b9db44494ad62922c73936c5cef14b57492ae94/src/js/sandbox/index.js)
- [src/js/util/index.js](https://github.com/pcottle/learnGitBranching/blob/6b9db44494ad62922c73936c5cef14b57492ae94/src/js/util/index.js)
- [src/js/views/index.js](https://github.com/pcottle/learnGitBranching/blob/6b9db44494ad62922c73936c5cef14b57492ae94/src/js/views/index.js)
- [src/js/visuals/index.js](https://github.com/pcottle/learnGitBranching/blob/6b9db44494ad62922c73936c5cef14b57492ae94/src/js/visuals/index.js)
- [src/levels/index.js](https://github.com/pcottle/learnGitBranching/blob/6b9db44494ad62922c73936c5cef14b57492ae94/src/levels/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 8 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 76 file(s) under js package (observed from repository paths and static analysis). |
| levels package | library | Observed | Groups 36 file(s) under levels package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 9 file(s) under scripts package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 33 file(s) under __tests__ package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/settings.yml` (config)
- `.github/workflows/build-docker.yml` (ci)
- `.github/workflows/pages.yml` (ci)
- `.gitpod.yml` (config)
- `Dockerfile` (container)
- `netlify.toml` (config)
- `package.json` (manifest)
- `spec/support/jasmine.json` (config)

## Top-level layout

- `src` — 126 analysed file(s)
- `__tests__` — 33 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `scripts` — 9 analysed file(s)
- `.github` — 5 analysed file(s)
- `generatedDocs` — 2 analysed file(s)
- `assets` — 1 analysed file(s)
- `spec` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x generated/minified file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6b9db44494ad62922c73936c5cef14b57492ae94` is the revision these paths and observations refer to.
