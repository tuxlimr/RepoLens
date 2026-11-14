# Project structure: ant-design/ant-motion

**Analysed commit:** `b37b07bea15927f83ec3518ca3af1fae91c1c6b5`

**Commit reference:** [b37b07bea15927f83ec3518ca3af1fae91c1c6b5](https://github.com/ant-design/ant-motion/commit/b37b07bea15927f83ec3518ca3af1fae91c1c6b5)

**Tree at this commit:** [ant-design/ant-motion@b37b07bea159](https://github.com/ant-design/ant-motion/tree/b37b07bea15927f83ec3518ca3af1fae91c1c6b5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ant-design/ant-motion |
| Description |   :bicyclist: Animate specification and components of Ant Design |
| Stars | 4630 |
| Forks | 355 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `b37b07bea15927f83ec3518ca3af1fae91c1c6b5` |
| Retrieved at | 2026-11-14T19:14:40.702967+00:00 |
| Files in this snapshot | 147 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
components/  (45 files)
  animate/  (5 files)
    demo/  (3 files)
      … 3 files under this directory
    index.en-US.md
    index.zh-CN.md
  banner-anim/  (8 files)
    demo/  (6 files)
      … 6 files under this directory
    index.en-US.md
    index.zh-CN.md
  queue-anim/  (8 files)
    demo/  (6 files)
      … 6 files under this directory
    index.en-US.md
    index.zh-CN.md
  scroll-anim/  (6 files)
    demo/  (4 files)
      … 4 files under this directory
    index.en-US.md
    index.zh-CN.md
  texty/  (7 files)
    demo/  (5 files)
      … 5 files under this directory
    index.en-US.md
    index.zh-CN.md
  tween-one/  (11 files)
    demo/  (9 files)
      … 9 files under this directory
    index.en-US.md
    index.zh-CN.md
exhibition/  (30 files)
  demo/  (9 files)
    carousel3d.md
    detail-switch.md
    linked-animate.md
    list-anim.md
    list-sort.md
    logo-gather-anim.md
    pic-details-anim.md
    snow.md
    table-enter-leave.md
  js/  (21 files)
    carousel3d.css
    carousel3d.jsx
    detail-swich.css
    detail-swich.jsx
    linked-animate.css
    linked-animate.jsx
    list-anim-animateDemo.css
    list-anim-animateDemo.jsx
    list-anim-tweeOneDemo.css
    list-anim-tweenOneDemo.jsx
    list-sort.css
    list-sort.jsx
    logo-gather-anim.css
    logo-gather-anim.jsx
    money.less
    pic-details-anim.css
    pic-details-anim.jsx
    snow.css
    snow.jsx
    table-enter-leave.css
    table-enter-leave.jsx
language/  (10 files)
  animate-term.md
  basic.en-US.md
  basic.zh-CN.md
  combined.md
  principle.en-US.md
  principle.zh-CN.md
  space.md
  speed.md
  transition.en-US.md
  transition.zh-CN.md
site/  (48 files)
  theme/  (47 files)
    static/  (16 files)
      … 16 files under this directory
    template/  (28 files)
      … 28 files under this directory
    en-US.js
    index.js
    zh-CN.js
  bisheng.config.js
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.stylelintrc
CNAME
LICENSE.md
README.cn.md
README.md
package.json
renovate.json
theme.js
webpack.config.js
```

## Entry points

- [site/theme/index.js](https://github.com/ant-design/ant-motion/blob/b37b07bea15927f83ec3518ca3af1fae91c1c6b5/site/theme/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| exhibition package | library | Observed | Groups 10 file(s) under exhibition package (observed from repository paths and static analysis). |
| site package | library | Observed | Groups 31 file(s) under site package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `package.json` (manifest)
- `renovate.json` (config)

## Top-level layout

- `site` — 48 analysed file(s)
- `components` — 45 analysed file(s)
- `exhibition` — 30 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `language` — 10 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b37b07bea15927f83ec3518ca3af1fae91c1c6b5` is the revision these paths and observations refer to.
