# Project structure: joshwcomeau/react-flip-move

**Analysed commit:** `ae9bd77adaf4a21d3a0d829c4901339478384b71`

**Commit reference:** [ae9bd77adaf4a21d3a0d829c4901339478384b71](https://github.com/joshwcomeau/react-flip-move/commit/ae9bd77adaf4a21d3a0d829c4901339478384b71)

**Tree at this commit:** [joshwcomeau/react-flip-move@ae9bd77adaf4](https://github.com/joshwcomeau/react-flip-move/tree/ae9bd77adaf4a21d3a0d829c4901339478384b71)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | joshwcomeau/react-flip-move |
| Description | Effortless animation between DOM changes (eg. list reordering) using the FLIP technique. |
| Stars | 4135 |
| Forks | 250 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `ae9bd77adaf4a21d3a0d829c4901339478384b71` |
| Retrieved at | 2026-11-14T19:14:52.265912+00:00 |
| Files in this snapshot | 51 |

## Directory tree

```text
.storybook/  (4 files)
  .babelrc
  config.js
  head.html
  webpack.config.js
.vscode/  (1 files)
  settings.json
documentation/  (2 files)
  api_reference.md
  enter_leave_animations.md
flow-typed/  (1 files)
  react-flip-move_v2.9.x-v2.10.x.js
src/  (9 files)
  CODE_TOUR.md
  FlipMove.js
  dom-manipulation.js
  enter-leave-presets.js
  error-messages.js
  helpers.js
  index.js
  prop-converter.js
  typings.js
stories/  (14 files)
  helpers/  (4 files)
    Controls.js
    FlipMoveListItem.js
    FlipMoveListItemLegacy.js
    FlipMoveWrapper.js
  appear-animations.stories.js
  enter-leave-animations.stories.js
  github-issues.stories.js
  hooks.stories.js
  invalid.stories.js
  legacy.stories.js
  misc.stories.js
  primary.stories.js
  sequencing.stories.js
  special-props.stories.js
test/  (2 files)
  helpers/  (1 files)
    index.js
  index.spec.js
typings/  (2 files)
  react-flip-move.d.ts
  test.tsx
.babelrc
.babelrc.js
.eslintignore
.eslintrc.js
.flowconfig
.gitignore
.travis.yml
LICENSE.md
README.md
SUMMARY.md
karma.conf.js
package.json
rollup.config.js
tslint.json
webpack.config.base.js
webpack.config.development.js
```

## Entry points

- [src/index.js](https://github.com/joshwcomeau/react-flip-move/blob/ae9bd77adaf4a21d3a0d829c4901339478384b71/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| dom-manipulation.js package | library | Observed | Groups 1 file(s) under dom-manipulation.js package (observed from repository paths and static analysis). |
| enter-leave-presets.js package | library | Observed | Groups 1 file(s) under enter-leave-presets.js package (observed from repository paths and static analysis). |
| error-messages.js package | library | Observed | Groups 1 file(s) under error-messages.js package (observed from repository paths and static analysis). |
| FlipMove.js package | library | Observed | Groups 1 file(s) under flipmove.js package (observed from repository paths and static analysis). |
| flow-typed package | library | Observed | Groups 1 file(s) under flow-typed package (observed from repository paths and static analysis). |
| helpers.js package | library | Observed | Groups 1 file(s) under helpers.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| prop-converter.js package | library | Observed | Groups 1 file(s) under prop-converter.js package (observed from repository paths and static analysis). |
| stories package | library | Observed | Groups 14 file(s) under stories package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 2 file(s) under tests (observed from repository paths and static analysis). |
| typings package | library | Observed | Groups 2 file(s) under typings package (observed from repository paths and static analysis). |
| typings.js package | library | Observed | Groups 1 file(s) under typings.js package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `tslint.json` (config)

## Top-level layout

- `(root files)` — 16 analysed file(s)
- `stories` — 14 analysed file(s)
- `src` — 9 analysed file(s)
- `.storybook` — 4 analysed file(s)
- `documentation` — 2 analysed file(s)
- `test` — 2 analysed file(s)
- `typings` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `flow-typed` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ae9bd77adaf4a21d3a0d829c4901339478384b71` is the revision these paths and observations refer to.
