# Project structure: chenglou/react-motion

**Analysed commit:** `9e3ce95bacaa9a1b259f969870a21c727232cc68`

**Commit reference:** [9e3ce95bacaa9a1b259f969870a21c727232cc68](https://github.com/chenglou/react-motion/commit/9e3ce95bacaa9a1b259f969870a21c727232cc68)

**Tree at this commit:** [chenglou/react-motion@9e3ce95bacaa](https://github.com/chenglou/react-motion/tree/9e3ce95bacaa9a1b259f969870a21c727232cc68)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | chenglou/react-motion |
| Description | A spring that solves your animation problems. |
| Stars | 21910 |
| Forks | 1145 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `9e3ce95bacaa9a1b259f969870a21c727232cc68` |
| Retrieved at | 2026-11-14T19:11:10.041670+00:00 |
| Files in this snapshot | 68 |

## Directory tree

```text
demos/  (26 files)
  demo0-simple-transition/  (3 files)
    Demo.jsx
    index.html
    index.jsx
  demo1-chat-heads/  (3 files)
    Demo.jsx
    index.html
    index.jsx
  demo2-draggable-balls/  (3 files)
    Demo.jsx
    index.html
    index.jsx
  demo3-todomvc-list-transition/  (4 files)
    Demo.jsx
    index.css
    index.html
    index.jsx
  demo4-photo-gallery/  (3 files)
    Demo.jsx
    index.html
    index.jsx
  demo5-spring-parameters-chooser/  (3 files)
    Demo.jsx
    index.html
    index.jsx
  demo7-water-ripples/  (3 files)
    Demo.jsx
    index.html
    index.jsx
  demo8-draggable-list/  (3 files)
    Demo.jsx
    index.html
    index.jsx
  README.md
src/  (13 files)
  Motion.js
  StaggeredMotion.js
  TransitionMotion.js
  Types.js
  mapToZero.js
  mergeDiff.js
  presets.js
  react-motion.js
  reorderKeys.js
  shouldStopAnimation.js
  spring.js
  stepper.js
  stripStyle.js
test/  (11 files)
  integration/  (4 files)
    README.md
    bower.html
    bower.json
    package.json
  Motion-test.js
  StaggeredMotion-test.js
  TransitionMotion-test.js
  createMockRaf.js
  index.js
  mergeDiff-test.js
  stripStyle-test.js
.babelrc
.eslintignore
.eslintrc
.flowconfig
.gitignore
.npmignore
.size-snapshot.json
.travis.yml
AUTHORS
HISTORY.md
LICENSE
README.md
bower.json
karma.conf.js
package.json
rollup.config.js
server.js
webpack.config.js
```

## Entry points

- [demos/demo0-simple-transition/index.jsx](https://github.com/chenglou/react-motion/blob/9e3ce95bacaa9a1b259f969870a21c727232cc68/demos/demo0-simple-transition/index.jsx)
- [demos/demo1-chat-heads/index.jsx](https://github.com/chenglou/react-motion/blob/9e3ce95bacaa9a1b259f969870a21c727232cc68/demos/demo1-chat-heads/index.jsx)
- [demos/demo2-draggable-balls/index.jsx](https://github.com/chenglou/react-motion/blob/9e3ce95bacaa9a1b259f969870a21c727232cc68/demos/demo2-draggable-balls/index.jsx)
- [demos/demo3-todomvc-list-transition/index.jsx](https://github.com/chenglou/react-motion/blob/9e3ce95bacaa9a1b259f969870a21c727232cc68/demos/demo3-todomvc-list-transition/index.jsx)
- [demos/demo4-photo-gallery/index.jsx](https://github.com/chenglou/react-motion/blob/9e3ce95bacaa9a1b259f969870a21c727232cc68/demos/demo4-photo-gallery/index.jsx)
- [demos/demo5-spring-parameters-chooser/index.jsx](https://github.com/chenglou/react-motion/blob/9e3ce95bacaa9a1b259f969870a21c727232cc68/demos/demo5-spring-parameters-chooser/index.jsx)
- [demos/demo7-water-ripples/index.jsx](https://github.com/chenglou/react-motion/blob/9e3ce95bacaa9a1b259f969870a21c727232cc68/demos/demo7-water-ripples/index.jsx)
- [demos/demo8-draggable-list/index.jsx](https://github.com/chenglou/react-motion/blob/9e3ce95bacaa9a1b259f969870a21c727232cc68/demos/demo8-draggable-list/index.jsx)
- [server.js](https://github.com/chenglou/react-motion/blob/9e3ce95bacaa9a1b259f969870a21c727232cc68/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| demos package | library | Observed | Groups 16 file(s) under demos package (observed from repository paths and static analysis). |
| mapToZero.js package | library | Observed | Groups 1 file(s) under maptozero.js package (observed from repository paths and static analysis). |
| mergeDiff.js package | library | Observed | Groups 1 file(s) under mergediff.js package (observed from repository paths and static analysis). |
| Motion.js package | library | Observed | Groups 1 file(s) under motion.js package (observed from repository paths and static analysis). |
| presets.js package | library | Observed | Groups 1 file(s) under presets.js package (observed from repository paths and static analysis). |
| react-motion.js package | library | Observed | Groups 1 file(s) under react-motion.js package (observed from repository paths and static analysis). |
| reorderKeys.js package | library | Observed | Groups 1 file(s) under reorderkeys.js package (observed from repository paths and static analysis). |
| shouldStopAnimation.js package | library | Observed | Groups 1 file(s) under shouldstopanimation.js package (observed from repository paths and static analysis). |
| spring.js package | library | Observed | Groups 1 file(s) under spring.js package (observed from repository paths and static analysis). |
| StaggeredMotion.js package | library | Observed | Groups 1 file(s) under staggeredmotion.js package (observed from repository paths and static analysis). |
| stepper.js package | library | Observed | Groups 1 file(s) under stepper.js package (observed from repository paths and static analysis). |
| stripStyle.js package | library | Observed | Groups 1 file(s) under stripstyle.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 11 file(s) under tests (observed from repository paths and static analysis). |
| TransitionMotion.js package | library | Observed | Groups 1 file(s) under transitionmotion.js package (observed from repository paths and static analysis). |
| Types.js package | library | Observed | Groups 1 file(s) under types.js package (observed from repository paths and static analysis). |

## Important files

- `.size-snapshot.json` (config)
- `.travis.yml` (ci)
- `bower.json` (config)
- `package.json` (manifest)

## Top-level layout

- `demos` — 26 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `src` — 13 analysed file(s)
- `test` — 11 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9e3ce95bacaa9a1b259f969870a21c727232cc68` is the revision these paths and observations refer to.
