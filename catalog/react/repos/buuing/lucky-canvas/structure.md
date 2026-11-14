# Project structure: buuing/lucky-canvas

**Analysed commit:** `7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9`

**Commit reference:** [7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9](https://github.com/buuing/lucky-canvas/commit/7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9)

**Tree at this commit:** [buuing/lucky-canvas@7a8c0bbcb992](https://github.com/buuing/lucky-canvas/tree/7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | buuing/lucky-canvas |
| Description | 🎖🎖🎖 基于 TS + Canvas 开发的【大转盘 / 九宫格 / 老虎机】抽奖插件，🌈 一套源码适配多端框架 JS / Vue / React / Taro / UniApp / 微信小程序等，🎨 奖品 / 文字 / 图片 / 颜色 / 按钮均可配置，支持同步 / 异步抽奖，🎯 概率前 / 后端可控，🚀 自动根据 dpr 调整清晰度适配移动端 |
| Stars | 8785 |
| Forks | 1033 |
| Licence | Apache-2.0 |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9` |
| Retrieved at | 2026-11-14T19:13:37.660591+00:00 |
| Files in this snapshot | 206 |

## Directory tree

```text
.github/  (1 files)
  ISSUE_TEMPLATE.md
packages/  (176 files)
  core/  (36 files)
    examples/  (4 files)
      … 4 files under this directory
    src/  (19 files)
      … 19 files under this directory
    types/  (1 files)
      … 1 files under this directory
    .babelrc
    .eslintrc.js
    .gitignore
    .npmignore
    LICENSE
    README.md
    index.js
    package.json
    postinstall.js
    rollup.config.build.js
    rollup.config.dev.js
    tsconfig.json
  mini/  (78 files)
    src/  (13 files)
      … 13 files under this directory
    test/  (3 files)
      … 3 files under this directory
    tools/  (53 files)
      … 53 files under this directory
    .babelrc
    .eslintrc.js
    .gitignore
    .npmignore
    LICENSE
    README.md
    gulpfile.js
    package.json
    tsconfig.json
  react/  (18 files)
    example/  (2 files)
      … 2 files under this directory
    src/  (8 files)
      … 8 files under this directory
    .babelrc
    .gitignore
    .npmignore
    LICENSE
    README.md
    package.json
    rollup.config.build.js
    rollup.config.dev.js
  taro/  (15 files)
    react/  (4 files)
      … 4 files under this directory
    utils/  (2 files)
      … 2 files under this directory
    vue/  (4 files)
      … 4 files under this directory
    .gitignore
    .npmignore
    LICENSE
    README.md
    package.json
  uni/  (9 files)
    .gitignore
    .npmignore
    LICENSE
    README.md
    lucky-grid.vue
    lucky-wheel.vue
    package.json
    slot-machine.vue
    utils.js
  vue/  (20 files)
    src/  (5 files)
      … 5 files under this directory
    types/  (1 files)
      … 1 files under this directory
    .gitignore
    .npmignore
    LICENSE
    README.md
    composition-api.js
    index.js
    package.json
    rollup.config.build.js
    rollup.config.dev.js
    shims-vue.d.ts
    tsconfig.json
    vue-demi.js
    vue2.html
    vue3.html
website/  (23 files)
  public/  (16 files)
    assets/  (16 files)
      … 16 files under this directory
  src/  (4 files)
    components/  (2 files)
      … 2 files under this directory
    main.js
    styles.css
  .gitignore
  index.html
  package.json
.gitignore
AGENTS.md
LICENSE
README.md
lerna.json
package.json
```

## Entry points

- [packages/core/index.js](https://github.com/buuing/lucky-canvas/blob/7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9/packages/core/index.js)
- [packages/core/src/index.ts](https://github.com/buuing/lucky-canvas/blob/7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9/packages/core/src/index.ts)
- [packages/react/src/app.js](https://github.com/buuing/lucky-canvas/blob/7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9/packages/react/src/app.js)
- [packages/react/src/index.js](https://github.com/buuing/lucky-canvas/blob/7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9/packages/react/src/index.js)
- [packages/taro/react/index.js](https://github.com/buuing/lucky-canvas/blob/7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9/packages/taro/react/index.js)
- [packages/taro/utils/index.js](https://github.com/buuing/lucky-canvas/blob/7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9/packages/taro/utils/index.js)
- [packages/taro/vue/index.js](https://github.com/buuing/lucky-canvas/blob/7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9/packages/taro/vue/index.js)
- [packages/vue/index.js](https://github.com/buuing/lucky-canvas/blob/7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9/packages/vue/index.js)
- [packages/vue/src/index.ts](https://github.com/buuing/lucky-canvas/blob/7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9/packages/vue/src/index.ts)
- [website/src/main.js](https://github.com/buuing/lucky-canvas/blob/7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9/website/src/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 28 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 60 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 25 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 3 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `lerna.json` (config)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.json` (config)
- `packages/mini/package.json` (manifest)
- `packages/mini/src/lucky-grid/index.json` (config)
- `packages/mini/src/lucky-wheel/index.json` (config)
- `packages/mini/src/slot-machine/index.json` (config)
- `packages/mini/tools/demo/app.json` (config)
- `packages/mini/tools/demo/package.json` (manifest)
- `packages/mini/tools/demo/pages/cjl/index.json` (config)
- `packages/mini/tools/demo/pages/index/index.json` (config)
- `packages/mini/tools/demo/pages/jd/index.json` (config)
- `packages/mini/tools/demo/pages/slot/index.json` (config)
- `packages/mini/tools/demo/pages/xc/index.json` (config)
- `packages/mini/tools/demo/pages/xdf/index.json` (config)
- `packages/mini/tools/demo/pages/ymc/index.json` (config)
- `packages/mini/tools/demo/pages/yx/index.json` (config)
- `packages/mini/tools/demo/pages/yyjk/index.json` (config)
- `packages/mini/tools/demo/pages/yyx/index.json` (config)
- `packages/mini/tools/demo/project.config.json` (config)
- `packages/mini/tsconfig.json` (config)
- `packages/react/package.json` (manifest)
- `packages/taro/package.json` (manifest)
- `packages/uni/package.json` (manifest)
- `packages/vue/package.json` (manifest)
- `packages/vue/tsconfig.json` (config)
- `website/package.json` (manifest)

## Top-level layout

- `packages` — 176 analysed file(s)
- `website` — 23 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `7a8c0bbcb992a297b390e3a2ebaa1a3385c1f2f9` is the revision these paths and observations refer to.
