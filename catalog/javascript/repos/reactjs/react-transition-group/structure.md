# Project structure: reactjs/react-transition-group

**Analysed commit:** `2989b5b87b4b4d1001f21c8efa503049ffb4fe8d`

**Commit reference:** [2989b5b87b4b4d1001f21c8efa503049ffb4fe8d](https://github.com/reactjs/react-transition-group/commit/2989b5b87b4b4d1001f21c8efa503049ffb4fe8d)

**Tree at this commit:** [reactjs/react-transition-group@2989b5b87b4b](https://github.com/reactjs/react-transition-group/tree/2989b5b87b4b4d1001f21c8efa503049ffb4fe8d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | reactjs/react-transition-group |
| Description | An easy way to perform animations when a React component enters or leaves the DOM |
| Stars | 10213 |
| Forks | 638 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `2989b5b87b4b4d1001f21c8efa503049ffb4fe8d` |
| Retrieved at | 2026-11-14T19:12:42.564626+00:00 |
| Files in this snapshot | 68 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.md
    feature-request.md
  workflows/  (1 files)
    ci.yml
.storybook/  (2 files)
  main.js
  preview.js
src/  (12 files)
  utils/  (4 files)
    ChildMapping.js
    PropTypes.js
    SimpleSet.js
    reflow.js
  CSSTransition.js
  ReplaceTransition.js
  SwitchTransition.js
  Transition.js
  TransitionGroup.js
  TransitionGroupContext.js
  config.js
  index.js
stories/  (13 files)
  transitions/  (4 files)
    Bootstrap.js
    CSSFade.js
    CSSFadeForTransitionGroup.js
    Scale.js
  .eslintrc.yml
  CSSTransition.js
  CSSTransitionGroupFixture.js
  NestedTransition.js
  ReplaceTransition.js
  StoryFixture.js
  Transition.js
  TransitionGroup.js
  index.js
test/  (11 files)
  .eslintrc.yml
  CSSTransition-test.js
  CSSTransitionGroup-test.js
  ChildMapping-test.js
  SSR-test.js
  SwitchTransition-test.js
  Transition-test.js
  TransitionGroup-test.js
  setup.js
  setupAfterEnv.js
  utils.js
www/  (14 files)
  src/  (9 files)
    components/  (2 files)
      … 2 files under this directory
    css/  (3 files)
      … 3 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    templates/  (1 files)
      … 1 files under this directory
  .babelrc.js
  .gitignore
  gatsby-config.js
  gatsby-node.js
  package.json
.babelrc.js
.eslintignore
.eslintrc.yml
.gitignore
.prettierignore
.size-snapshot.json
CHANGELOG.md
LICENSE
Migration.md
README.md
package.json
prettier.config.js
rollup.config.js
```

## Entry points

- [.storybook/main.js](https://github.com/reactjs/react-transition-group/blob/2989b5b87b4b4d1001f21c8efa503049ffb4fe8d/.storybook/main.js)
- [src/index.js](https://github.com/reactjs/react-transition-group/blob/2989b5b87b4b4d1001f21c8efa503049ffb4fe8d/src/index.js)
- [stories/index.js](https://github.com/reactjs/react-transition-group/blob/2989b5b87b4b4d1001f21c8efa503049ffb4fe8d/stories/index.js)
- [www/src/pages/index.js](https://github.com/reactjs/react-transition-group/blob/2989b5b87b4b4d1001f21c8efa503049ffb4fe8d/www/src/pages/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.js package | library | Observed | Groups 1 file(s) under config.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| CSSTransition.js package | library | Observed | Groups 1 file(s) under csstransition.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| ReplaceTransition.js package | library | Observed | Groups 1 file(s) under replacetransition.js package (observed from repository paths and static analysis). |
| stories package | library | Observed | Groups 12 file(s) under stories package (observed from repository paths and static analysis). |
| SwitchTransition.js package | library | Observed | Groups 1 file(s) under switchtransition.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 11 file(s) under tests (observed from repository paths and static analysis). |
| Transition.js package | library | Observed | Groups 1 file(s) under transition.js package (observed from repository paths and static analysis). |
| TransitionGroup.js package | library | Observed | Groups 1 file(s) under transitiongroup.js package (observed from repository paths and static analysis). |
| TransitionGroupContext.js package | library | Observed | Groups 1 file(s) under transitiongroupcontext.js package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 4 file(s) under utils package (observed from repository paths and static analysis). |
| www package | library | Observed | Groups 9 file(s) under www package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.size-snapshot.json` (config)
- `package.json` (manifest)
- `stories/.eslintrc.yml` (config)
- `www/package.json` (manifest)

## Top-level layout

- `www` — 14 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `stories` — 13 analysed file(s)
- `src` — 12 analysed file(s)
- `test` — 11 analysed file(s)
- `.github` — 3 analysed file(s)
- `.storybook` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2989b5b87b4b4d1001f21c8efa503049ffb4fe8d` is the revision these paths and observations refer to.
