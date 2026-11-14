# Project structure: iissnan/hexo-theme-next

**Analysed commit:** `9c8cea69bf0d4f91c07779d71b01814b27bbb6a1`

**Commit reference:** [9c8cea69bf0d4f91c07779d71b01814b27bbb6a1](https://github.com/iissnan/hexo-theme-next/commit/9c8cea69bf0d4f91c07779d71b01814b27bbb6a1)

**Tree at this commit:** [iissnan/hexo-theme-next@9c8cea69bf0d](https://github.com/iissnan/hexo-theme-next/tree/9c8cea69bf0d4f91c07779d71b01814b27bbb6a1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | iissnan/hexo-theme-next |
| Description | Elegant theme for Hexo.  |
| Stars | 15737 |
| Forks | 3497 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `9c8cea69bf0d4f91c07779d71b01814b27bbb6a1` |
| Retrieved at | 2026-11-14T19:11:36.059742+00:00 |
| Files in this snapshot | 292 |

## Directory tree

```text
.github/  (3 files)
  CONTRIBUTING.md
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
languages/  (16 files)
  de.yml
  default.yml
  en.yml
  fr-FR.yml
  id.yml
  it.yml
  ja.yml
  ko.yml
  nl-NL.yml
  pt-BR.yml
  pt.yml
  ru.yml
  vi.yml
  zh-Hans.yml
  zh-hk.yml
  zh-tw.yml
layout/  (75 files)
  _custom/  (2 files)
    header.swig
    sidebar.swig
  _macro/  (6 files)
    post-collapse.swig
    post-copyright.swig
    post.swig
    reward.swig
    sidebar.swig
    wechat-subscriber.swig
  _partials/  (16 files)
    head/  (2 files)
      … 2 files under this directory
    search/  (3 files)
      … 3 files under this directory
    share/  (4 files)
      … 4 files under this directory
    comments.swig
    footer.swig
    head.swig
    header.swig
    page-header.swig
    pagination.swig
    search.swig
  _scripts/  (8 files)
    pages/  (1 files)
      … 1 files under this directory
    schemes/  (4 files)
      … 4 files under this directory
    boostrap.swig
    commons.swig
    vendors.swig
  _third-party/  (35 files)
    analytics/  (13 files)
      … 13 files under this directory
    comments/  (9 files)
      … 9 files under this directory
    search/  (5 files)
      … 5 files under this directory
    seo/  (1 files)
      … 1 files under this directory
    duoshuo-hot-articles.swig
    exturl.swig
    mathjax.swig
    needsharebutton.swig
    rating.swig
    schedule.swig
    scroll-cookie.swig
  _layout.swig
  archive.swig
  category.swig
  index.swig
  page.swig
  post.swig
  schedule.swig
  tag.swig
scripts/  (11 files)
  tags/  (9 files)
    button.js
    center-quote.js
    exturl.js
    full-image.js
    group-pictures.js
    label.js
    lazy-image.js
    note.js
    tabs.js
  merge-configs.js
  merge.js
source/  (168 files)
  css/  (108 files)
    _common/  (72 files)
      … 72 files under this directory
    _custom/  (1 files)
      … 1 files under this directory
    _mixins/  (6 files)
      … 6 files under this directory
    _schemes/  (22 files)
      … 22 files under this directory
    _variables/  (6 files)
      … 6 files under this directory
    main.styl
  fonts/  (1 files)
    .gitkeep
  images/  (11 files)
    algolia_logo.svg
    cc-by-nc-nd.svg
    cc-by-nc-sa.svg
    cc-by-nc.svg
    cc-by-nd.svg
    cc-by-sa.svg
    cc-by.svg
    cc-zero.svg
    logo.svg
    quote-l.svg
    quote-r.svg
  js/  (12 files)
    src/  (12 files)
      … 12 files under this directory
  lib/  (36 files)
    canvas-ribbon/  (1 files)
      … 1 files under this directory
    fancybox/  (10 files)
      … 10 files under this directory
    fastclick/  (5 files)
      … 5 files under this directory
    font-awesome/  (6 files)
      … 6 files under this directory
    jquery/  (2 files)
      … 2 files under this directory
    jquery_lazyload/  (6 files)
      … 6 files under this directory
    needsharebutton/  (3 files)
      … 3 files under this directory
    velocity/  (3 files)
      … 3 files under this directory
test/  (3 files)
  .jshintrc
  helpers.js
  intern.js
.bowerrc
.editorconfig
.gitattributes
.gitignore
.hound.yml
.javascript_ignore
.jshintrc
.stylintrc
.travis.yml
LICENSE
README.cn.md
README.md
_config.yml
bower.json
gulpfile.coffee
package.json
```

## Entry points

- [source/lib/jquery/index.js](https://github.com/iissnan/hexo-theme-next/blob/9c8cea69bf0d4f91c07779d71b01814b27bbb6a1/source/lib/jquery/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 29 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 11 file(s) under scripts package (observed from repository paths and static analysis). |
| source package | library | Observed | Groups 24 file(s) under source package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.hound.yml` (config)
- `.travis.yml` (ci)
- `_config.yml` (config)
- `bower.json` (config)
- `languages/de.yml` (config)
- `languages/default.yml` (config)
- `languages/en.yml` (config)
- `languages/fr-FR.yml` (config)
- `languages/id.yml` (config)
- `languages/it.yml` (config)
- `languages/ja.yml` (config)
- `languages/ko.yml` (config)
- `languages/nl-NL.yml` (config)
- `languages/pt-BR.yml` (config)
- `languages/pt.yml` (config)
- `languages/ru.yml` (config)
- `languages/vi.yml` (config)
- `languages/zh-Hans.yml` (config)
- `languages/zh-hk.yml` (config)
- `languages/zh-tw.yml` (config)
- `package.json` (manifest)
- `source/lib/fancybox/.bower.json` (config)
- `source/lib/fastclick/.bower.json` (config)
- `source/lib/fastclick/bower.json` (config)
- `source/lib/font-awesome/.bower.json` (config)
- `source/lib/font-awesome/bower.json` (config)
- `source/lib/jquery/.bower.json` (config)
- `source/lib/jquery_lazyload/.bower.json` (config)
- `source/lib/jquery_lazyload/bower.json` (config)
- `source/lib/velocity/.bower.json` (config)
- `source/lib/velocity/bower.json` (config)

## Top-level layout

- `source` — 168 analysed file(s)
- `layout` — 75 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `languages` — 16 analysed file(s)
- `scripts` — 11 analysed file(s)
- `.github` — 3 analysed file(s)
- `test` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 19 file(s) were skipped during inventory (15 x generated/minified file excluded; 4 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9c8cea69bf0d4f91c07779d71b01814b27bbb6a1` is the revision these paths and observations refer to.
