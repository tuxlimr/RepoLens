# Project structure: ant-design/ant-design-landing

**Analysed commit:** `54f4360f0df75dd53e2febcd90b1b095801efb41`

**Commit reference:** [54f4360f0df75dd53e2febcd90b1b095801efb41](https://github.com/ant-design/ant-design-landing/commit/54f4360f0df75dd53e2febcd90b1b095801efb41)

**Tree at this commit:** [ant-design/ant-design-landing@54f4360f0df7](https://github.com/ant-design/ant-design-landing/tree/54f4360f0df75dd53e2febcd90b1b095801efb41)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ant-design/ant-design-landing |
| Description | :mountain_bicyclist: Landing Pages of Ant Design System |
| Stars | 6539 |
| Forks | 665 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `54f4360f0df75dd53e2febcd90b1b095801efb41` |
| Retrieved at | 2026-11-14T19:14:03.563206+00:00 |
| Files in this snapshot | 305 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
docs/  (19 files)
  edit/  (2 files)
    edit-block.md
    video.md
  guide/  (6 files)
    banner.md
    content.md
    examples.md
    header-footer.md
    layout.md
    type.md
  use/  (8 files)
    create-react-app.en-US.md
    create-react-app.zh-CN.md
    dumi.md
    dva-cli.md
    getting-started.md
    pro-1-x.md
    pro.md
    umi.md
  cases.md
  download.md
  introduce.md
prettier/  (7 files)
  lib/  (4 files)
    parser-graphql.js
    parser-parse5.js
    parser-vue.js
    sw-toolbox.js
  install-service-worker.js
  service-worker.js
  worker.js
site/  (264 files)
  edit/  (63 files)
    static/  (24 files)
      … 24 files under this directory
    template/  (36 files)
      … 36 files under this directory
    en-US.js
    index.js
    zh-CN.js
  shared/  (16 files)
    redux/  (10 files)
      … 10 files under this directory
    constants.js
    defaultTemplate.js
    leancloud.js
    localStorage.js
    url.js
    utils.js
  templates/  (128 files)
    static/  (8 files)
      … 8 files under this directory
    template/  (119 files)
      … 119 files under this directory
    index.js
  theme/  (52 files)
    static/  (23 files)
      … 23 files under this directory
    template/  (26 files)
      … 26 files under this directory
    en-US.js
    index.js
    zh-CN.js
  bisheng.common.config.js
  bisheng.edit.config.js
  bisheng.index.config.js
  bisheng.templates.config.js
  utils.jsx
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.stylelintrc
CNAME
LICENSE
README-zh_CN.md
README.md
documentation.md
index.text
package.json
renovate.json
webpack.config.js
```

## Entry points

- [site/edit/index.js](https://github.com/ant-design/ant-design-landing/blob/54f4360f0df75dd53e2febcd90b1b095801efb41/site/edit/index.js)
- [site/edit/template/index.jsx](https://github.com/ant-design/ant-design-landing/blob/54f4360f0df75dd53e2febcd90b1b095801efb41/site/edit/template/index.jsx)
- [site/shared/redux/index.js](https://github.com/ant-design/ant-design-landing/blob/54f4360f0df75dd53e2febcd90b1b095801efb41/site/shared/redux/index.js)
- [site/templates/index.js](https://github.com/ant-design/ant-design-landing/blob/54f4360f0df75dd53e2febcd90b1b095801efb41/site/templates/index.js)
- [site/templates/template/index.jsx](https://github.com/ant-design/ant-design-landing/blob/54f4360f0df75dd53e2febcd90b1b095801efb41/site/templates/template/index.jsx)
- [site/theme/index.js](https://github.com/ant-design/ant-design-landing/blob/54f4360f0df75dd53e2febcd90b1b095801efb41/site/theme/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| prettier package | library | Observed | Groups 7 file(s) under prettier package (observed from repository paths and static analysis). |
| site package | library | Observed | Groups 172 file(s) under site package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `package.json` (manifest)
- `renovate.json` (config)
- `site/theme/template/Home/component/data.json` (config)

## Top-level layout

- `site` — 264 analysed file(s)
- `docs` — 19 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `prettier` — 7 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `54f4360f0df75dd53e2febcd90b1b095801efb41` is the revision these paths and observations refer to.
