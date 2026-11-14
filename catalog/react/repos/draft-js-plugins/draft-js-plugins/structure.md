# Project structure: draft-js-plugins/draft-js-plugins

**Analysed commit:** `6049db73855df56edf41cd5ece5369f97fac10e6`

**Commit reference:** [6049db73855df56edf41cd5ece5369f97fac10e6](https://github.com/draft-js-plugins/draft-js-plugins/commit/6049db73855df56edf41cd5ece5369f97fac10e6)

**Tree at this commit:** [draft-js-plugins/draft-js-plugins@6049db73855d](https://github.com/draft-js-plugins/draft-js-plugins/tree/6049db73855df56edf41cd5ece5369f97fac10e6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | draft-js-plugins/draft-js-plugins |
| Description | React Plugin Architecture for Draft.js including Slack-Like Emojis, FB-Like Mentions and Stickers |
| Stars | 4084 |
| Forks | 1037 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `6049db73855df56edf41cd5ece5369f97fac10e6` |
| Retrieved at | 2026-11-14T19:14:55.058365+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (11 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (5 files)
    dependabot-auto-merge.yml
    deployWebsite.yml
    release.yml
    stale.yml
    tests.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
  stale.yml
.husky/  (2 files)
  .gitignore
  pre-commit
.storybook/  (4 files)
  main.js
  preview-head.html
  preview.js
  webpack.config.js
interfaces/  (1 files)
  CSSModule.js
packages/  (620 files)
  alignment/  (11 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  anchor/  (18 files)
    src/  (11 files)
      … 11 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  buttons/  (32 files)
    src/  (25 files)
      … 25 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  counter/  (17 files)
    src/  (10 files)
      … 10 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  divider/  (11 files)
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    jest.config.js
    package.json
    tsconfig.json
  docs/  (236 files)
    components/  (182 files)
      … 182 files under this directory
    pages/  (41 files)
      … 41 files under this directory
    public/  (3 files)
      … 3 files under this directory
    styles/  (4 files)
      … 4 files under this directory
    README.md
    env.d.ts
    next-env.d.ts
    next.config.js
    package.json
    tsconfig.json
  drag-n-drop/  (13 files)
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  drag-n-drop-upload/  (17 files)
    src/  (9 files)
      … 9 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    server.js
    tsconfig.json
  editor/  (19 files)
    src/  (12 files)
      … 12 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  emoji/  (43 files)
    src/  (36 files)
      … 36 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  focus/  (19 files)
    src/  (12 files)
      … 12 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  hashtag/  (15 files)
    src/  (8 files)
      … 8 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  image/  (10 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  inline-toolbar/  (12 files)
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  linkify/  (14 files)
    src/  (7 files)
      … 7 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  mention/  (34 files)
    src/  (27 files)
      … 27 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  resizeable/  (9 files)
    src/  (2 files)
      … 2 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  side-toolbar/  (13 files)
    src/  (6 files)
      … 6 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  static-toolbar/  (11 files)
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    jest.config.js
    package.json
    tsconfig.json
  sticker/  (16 files)
    src/  (9 files)
      … 9 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  text-alignment/  (10 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  undo/  (14 files)
    src/  (7 files)
      … 7 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  utils/  (11 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
  video/  (15 files)
    src/  (8 files)
      … 8 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    jest.config.js
    package.json
    tsconfig.json
scripts/  (2 files)
  build-css.js
  publishGithubPages.sh
stories/  (139 files)
  adding-images/  (5 files)
    src/  (5 files)
      … 5 files under this directory
  adding-video/  (5 files)
    src/  (5 files)
      … 5 files under this directory
  align-drag-focus-and-resize-images/  (3 files)
    src/  (3 files)
      … 3 files under this directory
  alignment/  (4 files)
    src/  (4 files)
      … 4 files under this directory
  counter-plugin-simple/  (3 files)
    src/  (3 files)
      … 3 files under this directory
  displaying-images/  (3 files)
    src/  (3 files)
      … 3 files under this directory
  divider-with-side-toolbar/  (3 files)
    src/  (3 files)
      … 3 files under this directory
  drag-n-drop/  (3 files)
    src/  (3 files)
      … 3 files under this directory
  drag-n-drop-upload/  (4 files)
    src/  (4 files)
      … 4 files under this directory
  emoji/  (3 files)
    src/  (3 files)
      … 3 files under this directory
  emoji-styled/  (4 files)
    src/  (4 files)
      … 4 files under this directory
  focus/  (4 files)
    src/  (4 files)
      … 4 files under this directory
  hashtag/  (3 files)
    src/  (3 files)
      … 3 files under this directory
  hashtag-styled/  (4 files)
    src/  (4 files)
      … 4 files under this directory
  inline-toolbar/  (3 files)
    src/  (3 files)
      … 3 files under this directory
  inline-toolbar-custom-buttons/  (3 files)
    src/  (3 files)
      … 3 files under this directory
  inline-toolbar-custom-styled/  (5 files)
    src/  (5 files)
      … 5 files under this directory
  inline-toolbar-relative-parent/  (3 files)
    src/  (3 files)
      … 3 files under this directory
  inline-toolbar-with-anchor-plugin/  (3 files)
    src/  (3 files)
      … 3 files under this directory
  kitchensink/  (6 files)
    src/  (6 files)
      … 6 files under this directory
  linkify/  (3 files)
    src/  (3 files)
      … 3 files under this directory
  linkify-configured/  (3 files)
    src/  (3 files)
      … 3 files under this directory
  mentions/  (4 files)
    src/  (4 files)
      … 4 files under this directory
  mentions-custom-component/  (7 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (4 files)
      … 4 files under this directory
  mentions-custom-container-component/  (4 files)
    src/  (4 files)
      … 4 files under this directory
  mentions-custom-styled/  (8 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (5 files)
      … 5 files under this directory
  mentions-custom-trigger/  (4 files)
    src/  (4 files)
      … 4 files under this directory
  mentions-multi-triggers/  (4 files)
    src/  (4 files)
      … 4 files under this directory
  mentions-remote/  (6 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (3 files)
      … 3 files under this directory
  mentions-trigger-in-trigger/  (4 files)
    MentionsTriggerInTrigger.stories.tsx
    MentionsTriggerInTrigger.tsx
    editorStyles.css
    mentions.ts
  mentions-with-whitespace/  (8 files)
    public/  (3 files)
      … 3 files under this directory
    src/  (5 files)
      … 5 files under this directory
  public/  (3 files)
    data/  (3 files)
      … 3 files under this directory
  resizable/  (4 files)
    src/  (4 files)
      … 4 files under this directory
  blockTypeSelectStyles.css
  buttonStyles.css
  editorStyles.css
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.nvmrc
.prettierrc.js
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
FAQ.md
HOW_TO_CREATE_A_PLUGIN.md
LICENSE
README.md
babel.config.js
jest.config.base.js
jest.config.js
jestHelper.js
package.json
rollup.config.js
```

## Entry points

- [.storybook/main.js](https://github.com/draft-js-plugins/draft-js-plugins/blob/6049db73855df56edf41cd5ece5369f97fac10e6/.storybook/main.js)
- [packages/alignment/src/index.tsx](https://github.com/draft-js-plugins/draft-js-plugins/blob/6049db73855df56edf41cd5ece5369f97fac10e6/packages/alignment/src/index.tsx)
- [packages/anchor/src/index.tsx](https://github.com/draft-js-plugins/draft-js-plugins/blob/6049db73855df56edf41cd5ece5369f97fac10e6/packages/anchor/src/index.tsx)
- [packages/buttons/src/index.ts](https://github.com/draft-js-plugins/draft-js-plugins/blob/6049db73855df56edf41cd5ece5369f97fac10e6/packages/buttons/src/index.ts)
- [packages/counter/src/index.tsx](https://github.com/draft-js-plugins/draft-js-plugins/blob/6049db73855df56edf41cd5ece5369f97fac10e6/packages/counter/src/index.tsx)
- [packages/divider/src/index.tsx](https://github.com/draft-js-plugins/draft-js-plugins/blob/6049db73855df56edf41cd5ece5369f97fac10e6/packages/divider/src/index.tsx)
- [packages/drag-n-drop-upload/server.js](https://github.com/draft-js-plugins/draft-js-plugins/blob/6049db73855df56edf41cd5ece5369f97fac10e6/packages/drag-n-drop-upload/server.js)
- [packages/drag-n-drop-upload/src/index.ts](https://github.com/draft-js-plugins/draft-js-plugins/blob/6049db73855df56edf41cd5ece5369f97fac10e6/packages/drag-n-drop-upload/src/index.ts)
- [packages/drag-n-drop/src/index.tsx](https://github.com/draft-js-plugins/draft-js-plugins/blob/6049db73855df56edf41cd5ece5369f97fac10e6/packages/drag-n-drop/src/index.tsx)
- [packages/editor/src/index.ts](https://github.com/draft-js-plugins/draft-js-plugins/blob/6049db73855df56edf41cd5ece5369f97fac10e6/packages/editor/src/index.ts)
- [packages/emoji/src/index.tsx](https://github.com/draft-js-plugins/draft-js-plugins/blob/6049db73855df56edf41cd5ece5369f97fac10e6/packages/emoji/src/index.tsx)
- [packages/focus/src/index.tsx](https://github.com/draft-js-plugins/draft-js-plugins/blob/6049db73855df56edf41cd5ece5369f97fac10e6/packages/focus/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 67 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| interfaces package | library | Observed | Groups 1 file(s) under interfaces package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 248 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| stories package | library | Observed | Groups 81 file(s) under stories package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/stale.yml` (config)
- `.github/workflows/dependabot-auto-merge.yml` (ci)
- `.github/workflows/deployWebsite.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `package.json` (manifest)
- `packages/alignment/package.json` (manifest)
- `packages/alignment/tsconfig.json` (config)
- `packages/anchor/package.json` (manifest)
- `packages/anchor/tsconfig.json` (config)
- `packages/buttons/package.json` (manifest)
- `packages/buttons/tsconfig.json` (config)
- `packages/counter/package.json` (manifest)
- `packages/counter/tsconfig.json` (config)
- `packages/divider/package.json` (manifest)
- `packages/divider/tsconfig.json` (config)
- `packages/docs/package.json` (manifest)
- `packages/docs/public/data/mentionsA.json` (config)
- `packages/docs/public/data/mentionsB.json` (config)
- `packages/docs/public/data/mentionsC.json` (config)
- `packages/docs/tsconfig.json` (config)
- `packages/drag-n-drop-upload/package.json` (manifest)
- `packages/drag-n-drop-upload/tsconfig.json` (config)
- `packages/drag-n-drop/package.json` (manifest)
- `packages/drag-n-drop/tsconfig.json` (config)
- `packages/editor/package.json` (manifest)
- `packages/editor/tsconfig.json` (config)
- `packages/emoji/package.json` (manifest)
- `packages/emoji/tsconfig.json` (config)
- `packages/focus/package.json` (manifest)
- `packages/focus/tsconfig.json` (config)
- `packages/hashtag/package.json` (manifest)
- `packages/hashtag/tsconfig.json` (config)
- `packages/image/package.json` (manifest)
- `packages/image/tsconfig.json` (config)
- `packages/inline-toolbar/package.json` (manifest)
- `packages/inline-toolbar/tsconfig.json` (config)
- `packages/linkify/package.json` (manifest)
- `packages/linkify/tsconfig.json` (config)
- `packages/mention/package.json` (manifest)
- `packages/mention/tsconfig.json` (config)
- `packages/resizeable/package.json` (manifest)
- `packages/resizeable/tsconfig.json` (config)
- `packages/side-toolbar/package.json` (manifest)
- `packages/side-toolbar/tsconfig.json` (config)
- `packages/static-toolbar/package.json` (manifest)
- `packages/static-toolbar/tsconfig.json` (config)
- `packages/sticker/package.json` (manifest)
- `packages/sticker/tsconfig.json` (config)
- `packages/text-alignment/package.json` (manifest)
- `packages/text-alignment/tsconfig.json` (config)
- `packages/undo/package.json` (manifest)
- `packages/undo/tsconfig.json` (config)
- `packages/utils/package.json` (manifest)
- `packages/utils/tsconfig.json` (config)
- `packages/video/package.json` (manifest)
- `packages/video/tsconfig.json` (config)
- `stories/mentions-custom-component/public/data/mentionsA.json` (config)
- `stories/mentions-custom-component/public/data/mentionsB.json` (config)
- `stories/mentions-custom-component/public/data/mentionsC.json` (config)
- `stories/mentions-custom-styled/public/data/mentionsA.json` (config)
- `stories/mentions-custom-styled/public/data/mentionsB.json` (config)
- `stories/mentions-custom-styled/public/data/mentionsC.json` (config)
- `stories/mentions-remote/public/data/mentionsA.json` (config)
- `stories/mentions-remote/public/data/mentionsB.json` (config)
- `stories/mentions-remote/public/data/mentionsC.json` (config)
- `stories/mentions-with-whitespace/public/data/mentionsA.json` (config)
- `stories/mentions-with-whitespace/public/data/mentionsB.json` (config)
- `stories/mentions-with-whitespace/public/data/mentionsC.json` (config)
- `stories/public/data/mentionsA.json` (config)
- `stories/public/data/mentionsB.json` (config)
- `stories/public/data/mentionsC.json` (config)

## Top-level layout

- `packages` — 620 analysed file(s)
- `stories` — 139 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 11 analysed file(s)
- `.storybook` — 4 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.husky` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `interfaces` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `6049db73855df56edf41cd5ece5369f97fac10e6` is the revision these paths and observations refer to.
