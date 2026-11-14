# Project structure: pomber/git-history

**Analysed commit:** `a20f6085cf9055b350a4db13cea6e013936da9cd`

**Commit reference:** [a20f6085cf9055b350a4db13cea6e013936da9cd](https://github.com/pomber/git-history/commit/a20f6085cf9055b350a4db13cea6e013936da9cd)

**Tree at this commit:** [pomber/git-history@a20f6085cf90](https://github.com/pomber/git-history/tree/a20f6085cf9055b350a4db13cea6e013936da9cd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pomber/git-history |
| Description | Quickly browse the history of a file from any git repository |
| Stars | 13684 |
| Forks | 543 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `a20f6085cf9055b350a4db13cea6e013936da9cd` |
| Retrieved at | 2026-11-14T19:11:51.591571+00:00 |
| Files in this snapshot | 72 |

## Directory tree

```text
.github/  (2 files)
  FUNDING.yml
  opencollective.yml
.storybook/  (2 files)
  addons.js
  config.js
cli/  (6 files)
  .gitignore
  cli.js
  git.js
  package.json
  readme.md
  server.js
public/  (2 files)
  index.html
  manifest.json
src/  (42 files)
  airframe/  (2 files)
    airframe.js
    easing.js
  git-providers/  (17 files)
    bitbucket-commit-fetcher.js
    bitbucket-provider.js
    cli-commit-fetcher.js
    cli-provider.js
    differ.js
    github-commit-fetcher.js
    github-provider.js
    gitlab-commit-fetcher.js
    gitlab-provider.js
    language-detector.js
    language-detector.test.js
    providers.js
    sources.js
    tokenizer.js
    versioner.js
    versioner.worker.js
    vscode-provider.js
  icons/  (4 files)
    chrome.svg
    cli.svg
    firefox.svg
    vscode.svg
  animation.js
  app-helpers.js
  app.js
  comment-box.css
  duotoneLight.js
  history.js
  index.js
  landing.css
  landing.js
  nightOwl.js
  scroller.css
  scroller.js
  scroller.story.js
  slide.js
  use-spring.js
  use-spring.story.js
  use-virtual-children.js
  utils.js
  utils.test.js
vscode-ext/  (11 files)
  .vscode/  (1 files)
    launch.json
  test/  (2 files)
    extension.test.js
    index.js
  .gitignore
  extension.js
  git.js
  jsconfig.json
  package.json
  readme.md
  test-git.js
  vsc-extension-quickstart.md
.gitignore
.travis.yml
craco.config.js
license
netlify.toml
package.json
readme.md
```

## Entry points

- [cli/cli.js](https://github.com/pomber/git-history/blob/a20f6085cf9055b350a4db13cea6e013936da9cd/cli/cli.js)
- [vscode-ext/extension.js](https://github.com/pomber/git-history/blob/a20f6085cf9055b350a4db13cea6e013936da9cd/vscode-ext/extension.js)
- [cli/server.js](https://github.com/pomber/git-history/blob/a20f6085cf9055b350a4db13cea6e013936da9cd/cli/server.js)
- [src/app.js](https://github.com/pomber/git-history/blob/a20f6085cf9055b350a4db13cea6e013936da9cd/src/app.js)
- [src/index.js](https://github.com/pomber/git-history/blob/a20f6085cf9055b350a4db13cea6e013936da9cd/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| airframe package | library | Observed | Groups 2 file(s) under airframe package (observed from repository paths and static analysis). |
| animation.js package | library | Observed | Groups 1 file(s) under animation.js package (observed from repository paths and static analysis). |
| app-helpers.js package | library | Observed | Groups 1 file(s) under app-helpers.js package (observed from repository paths and static analysis). |
| app.js package | library | Observed | Groups 1 file(s) under app.js package (observed from repository paths and static analysis). |
| cli package | library | Observed | Groups 3 file(s) under cli package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| duotoneLight.js package | library | Observed | Groups 1 file(s) under duotonelight.js package (observed from repository paths and static analysis). |
| git-providers package | library | Observed | Groups 17 file(s) under git-providers package (observed from repository paths and static analysis). |
| history.js package | library | Observed | Groups 1 file(s) under history.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| landing.js package | library | Observed | Groups 1 file(s) under landing.js package (observed from repository paths and static analysis). |
| nightOwl.js package | library | Observed | Groups 1 file(s) under nightowl.js package (observed from repository paths and static analysis). |
| scroller.js package | library | Observed | Groups 1 file(s) under scroller.js package (observed from repository paths and static analysis). |
| scroller.story.js package | library | Observed | Groups 1 file(s) under scroller.story.js package (observed from repository paths and static analysis). |
| slide.js package | library | Observed | Groups 1 file(s) under slide.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |
| use-spring.js package | library | Observed | Groups 1 file(s) under use-spring.js package (observed from repository paths and static analysis). |
| use-spring.story.js package | library | Observed | Groups 1 file(s) under use-spring.story.js package (observed from repository paths and static analysis). |
| use-virtual-children.js package | library | Observed | Groups 1 file(s) under use-virtual-children.js package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |
| utils.test.js package | library | Observed | Groups 1 file(s) under utils.test.js package (observed from repository paths and static analysis). |
| vscode-ext package | library | Observed | Groups 3 file(s) under vscode-ext package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/opencollective.yml` (config)
- `.travis.yml` (ci)
- `cli/package.json` (manifest)
- `netlify.toml` (config)
- `package.json` (manifest)
- `public/manifest.json` (config)
- `vscode-ext/.vscode/launch.json` (config)
- `vscode-ext/jsconfig.json` (config)
- `vscode-ext/package.json` (manifest)

## Top-level layout

- `src` — 42 analysed file(s)
- `vscode-ext` — 11 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `cli` — 6 analysed file(s)
- `.github` — 2 analysed file(s)
- `.storybook` — 2 analysed file(s)
- `public` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a20f6085cf9055b350a4db13cea6e013936da9cd` is the revision these paths and observations refer to.
