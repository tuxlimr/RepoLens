# Project structure: mdx-editor/editor

**Analysed commit:** `0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce`

**Commit reference:** [0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce](https://github.com/mdx-editor/editor/commit/0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce)

**Tree at this commit:** [mdx-editor/editor@0d0cfbaabcee](https://github.com/mdx-editor/editor/tree/0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mdx-editor/editor |
| Description | A rich text editor React component for markdown |
| Stars | 3718 |
| Forks | 312 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce` |
| Retrieved at | 2026-11-14T19:15:07.047560+00:00 |
| Files in this snapshot | 329 |

## Directory tree

```text
.claude/  (1 files)
  settings.local.json
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    1.bug.md
    config.yml
  workflows/  (2 files)
    ci.yml
    release.yml
  FUNDING.yml
.ladle/  (1 files)
  config.mjs
docs/  (23 files)
  admonitions.md
  basic-formatting.md
  code-blocks.md
  content-styling.md
  custom-directive-editors.md
  customizing-toolbar.md
  diff-source.md
  error-handling.md
  extending-the-editor.md
  front-matter.md
  getting-started.md
  html.md
  i18n.md
  images.md
  jsx.md
  links.md
  live-demo-contents.md
  markdown-shortcuts.md
  overview.md
  search-replace.md
  tables.md
  theming.md
  upgrading-to-v2.md
locales/  (12 files)
  de-de/  (1 files)
    translation.json
  en/  (1 files)
    translation.json
  es-es/  (1 files)
    translation.json
  fr/  (1 files)
    translation.json
  ja-jp/  (1 files)
    translation.json
  ko-kr/  (1 files)
    translation.json
  pt-br/  (1 files)
    translation.json
  ru-ru/  (1 files)
    translation.json
  sv-se/  (1 files)
    translation.json
  uk-ua/  (1 files)
    translation.json
  zh-cn/  (1 files)
    translation.json
  zh-tw/  (1 files)
    translation.json
plans/  (10 files)
  research/  (4 files)
    003-selection-markdown/  (1 files)
      … 1 files under this directory
    004-state-backed-search/  (1 files)
      … 1 files under this directory
    005-extension-composer-history/  (2 files)
      … 2 files under this directory
  roadmaps/  (1 files)
    001-lexical-048-adoption.md
  001-lexical-compatibility-gate.md
  002-lexical-048-upgrade.md
  003-selection-markdown.md
  004-state-backed-search-replace.md
  005-extension-composer-history.md
reports/  (2 files)
  lexical-upgrade-0.35.0-to-0.48.0-assessment-2026-07-18.md
  pr-949-review.md
scripts/  (6 files)
  assert-lexical-versions.mjs
  export-figma-icons.mjs
  package-consumer-utils.mjs
  upgrade-lexical.sh
  verify-cross-version-markdown.mjs
  verify-package-consumer.mjs
src/  (229 files)
  @types/  (3 files)
    lexical/  (1 files)
      … 1 files under this directory
    micromark-util-symbol/  (1 files)
      … 1 files under this directory
    unidiff/  (1 files)
      … 1 files under this directory
  directive-editors/  (2 files)
    AdmonitionDirectiveDescriptor.tsx
    GenericDirectiveEditor.tsx
  examples/  (54 files)
    assets/  (10 files)
      … 10 files under this directory
    .eslintrc
    _boilerplate.tsx
    basics.tsx
    bug-654.tsx
    bug-683.tsx
    bug-733.tsx
    bug-920.tsx
    bug-921.tsx
    bug-936.tsx
    bug-953.tsx
    bug-97.stories.tsx
    bug-991.tsx
    cm-merge.tsx
    codemirror-languages.tsx
    colors.tsx
    controlled-mode.tsx
    dark-editor.css
    diff-source.tsx
    directives.tsx
    error-handling.tsx
    extension-compatibility.tsx
    file-backend.js
    get-selection-markdown.tsx
    html.tsx
    … 20 more files
  jsx-editors/  (1 files)
    GenericJsxEditor.tsx
  plugins/  (112 files)
    codeblock/  (5 files)
      … 5 files under this directory
    codemirror/  (3 files)
      … 3 files under this directory
    core/  (20 files)
      … 20 files under this directory
    diff-source/  (4 files)
      … 4 files under this directory
    directives/  (4 files)
      … 4 files under this directory
    frontmatter/  (5 files)
      … 5 files under this directory
    headings/  (3 files)
      … 3 files under this directory
    image/  (9 files)
      … 9 files under this directory
    jsx/  (11 files)
      … 11 files under this directory
    link/  (4 files)
      … 4 files under this directory
    link-dialog/  (2 files)
      … 2 files under this directory
    lists/  (5 files)
      … 5 files under this directory
    markdown-shortcut/  (1 files)
      … 1 files under this directory
    maxlength/  (1 files)
      … 1 files under this directory
    quote/  (3 files)
      … 3 files under this directory
    remote/  (1 files)
      … 1 files under this directory
    search/  (1 files)
      … 1 files under this directory
    table/  (5 files)
      … 5 files under this directory
    thematic-break/  (3 files)
      … 3 files under this directory
    toolbar/  (22 files)
      … 22 files under this directory
  styles/  (4 files)
    globals.css
    lexical-theme.module.css
    lexicalTheme.ts
    ui.module.css
  test/  (35 files)
    fixtures/  (7 files)
      … 7 files under this directory
    codeblock-in-list.test.tsx
    codemirror-lifecycle.test.tsx
    codemirror.test.ts
    compatibility.test.tsx
    core.test.tsx
    dialog-a11y.test.tsx
    extension-composer.test.tsx
    frontmatter.test.tsx
    image-upload-lifecycle.test.tsx
    impex.test.tsx
    jsx.test.tsx
    link-dialog.test.tsx
    linked-image.test.tsx
    lists.test.tsx
    markdown-shortcut.test.tsx
    nested-jsx-imports-integration.test.tsx
    nested-jsx-imports.test.tsx
    package-consumer-utils.test.ts
    search.test.tsx
    selection-markdown.test.tsx
    setup.ts
    source-insert-markdown.test.tsx
    table-history.test.tsx
    table-image-dialog.test.tsx
    … 4 more files
  utils/  (9 files)
    detectMac.ts
    fp.ts
    isPartOftheEditorUI.tsx
    lexicalHelpers.ts
    makeHslTransparent.ts
    mdastEquality.ts
    mergeStyleAttributes.ts
    uuid4.ts
    voidEmitter.ts
  FormatConstants.ts
  MDXEditor.tsx
  RealmWithPlugins.tsx
  defaultSvgIcons.tsx
  exportMarkdownFromLexical.ts
  importMarkdownToLexical.ts
  index.ts
  mdastUtilHtmlComment.ts
  realmSession.ts
tests/  (21 files)
  browser/  (16 files)
    conditional-history-toolbar.spec.ts
    extension-compatibility.spec.ts
    full-height.spec.ts
    heading-shortcuts.spec.ts
    image-upload-lifecycle.spec.ts
    lexical-compatibility.spec.ts
    linked-image.spec.ts
    nested-jsx-imports.spec.ts
    search-replace.spec.ts
    selection-markdown.spec.ts
    source-insert-markdown.spec.ts
    table-cell-edge-deletion.spec.ts
    table-column-insertion.spec.ts
    table-focus-after-insert.spec.ts
    table-history.spec.ts
    table-image-dialog.spec.ts
  package-consumer/  (5 files)
    react-18/  (1 files)
      … 1 files under this directory
    react-19/  (1 files)
      … 1 files under this directory
    shared/  (3 files)
      … 3 files under this directory
.env.example
.eslintrc.cjs
.gitattributes
.gitignore
.nvmrc
.prettierrc.cjs
AGENTS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
package.json
playwright.config.ts
postcss.config.mjs
tsconfig.docs.json
tsconfig.json
typedoc.json
vite.config.ts
vite.ladle.config.ts
```

## Entry points

- [src/index.ts](https://github.com/mdx-editor/editor/blob/0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce/src/index.ts)
- [src/plugins/codeblock/index.ts](https://github.com/mdx-editor/editor/blob/0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce/src/plugins/codeblock/index.ts)
- [src/plugins/codemirror/index.tsx](https://github.com/mdx-editor/editor/blob/0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce/src/plugins/codemirror/index.tsx)
- [src/plugins/core/index.ts](https://github.com/mdx-editor/editor/blob/0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce/src/plugins/core/index.ts)
- [src/plugins/diff-source/index.tsx](https://github.com/mdx-editor/editor/blob/0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce/src/plugins/diff-source/index.tsx)
- [src/plugins/directives/index.ts](https://github.com/mdx-editor/editor/blob/0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce/src/plugins/directives/index.ts)
- [src/plugins/frontmatter/index.ts](https://github.com/mdx-editor/editor/blob/0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce/src/plugins/frontmatter/index.ts)
- [src/plugins/headings/index.ts](https://github.com/mdx-editor/editor/blob/0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce/src/plugins/headings/index.ts)
- [src/plugins/image/index.ts](https://github.com/mdx-editor/editor/blob/0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce/src/plugins/image/index.ts)
- [src/plugins/jsx/index.ts](https://github.com/mdx-editor/editor/blob/0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce/src/plugins/jsx/index.ts)
- [src/plugins/link-dialog/index.ts](https://github.com/mdx-editor/editor/blob/0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce/src/plugins/link-dialog/index.ts)
- [src/plugins/link/index.tsx](https://github.com/mdx-editor/editor/blob/0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce/src/plugins/link/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 16 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| defaultSvgIcons.tsx package | library | Observed | Groups 1 file(s) under defaultsvgicons.tsx package (observed from repository paths and static analysis). |
| directive-editors package | library | Observed | Groups 2 file(s) under directive-editors package (observed from repository paths and static analysis). |
| examples package | library | Observed | Groups 42 file(s) under examples package (observed from repository paths and static analysis). |
| exportMarkdownFromLexical.ts package | library | Observed | Groups 1 file(s) under exportmarkdownfromlexical.ts package (observed from repository paths and static analysis). |
| FormatConstants.ts package | library | Observed | Groups 1 file(s) under formatconstants.ts package (observed from repository paths and static analysis). |
| importMarkdownToLexical.ts package | library | Observed | Groups 1 file(s) under importmarkdowntolexical.ts package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| jsx-editors package | library | Observed | Groups 1 file(s) under jsx-editors package (observed from repository paths and static analysis). |
| mdastUtilHtmlComment.ts package | library | Observed | Groups 1 file(s) under mdastutilhtmlcomment.ts package (observed from repository paths and static analysis). |
| MDXEditor.tsx package | library | Observed | Groups 1 file(s) under mdxeditor.tsx package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 92 file(s) under plugins package (observed from repository paths and static analysis). |
| realmSession.ts package | library | Observed | Groups 1 file(s) under realmsession.ts package (observed from repository paths and static analysis). |
| RealmWithPlugins.tsx package | library | Observed | Groups 1 file(s) under realmwithplugins.tsx package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 20 file(s) under service / domain layer (observed from repository paths and static analysis). |
| styles package | library | Observed | Groups 1 file(s) under styles package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 56 file(s) under tests (observed from repository paths and static analysis). |
| @types package | library | Observed | Groups 3 file(s) under @types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 9 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.claude/settings.local.json` (config)
- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `locales/de-de/translation.json` (config)
- `locales/en/translation.json` (config)
- `locales/es-es/translation.json` (config)
- `locales/fr/translation.json` (config)
- `locales/ja-jp/translation.json` (config)
- `locales/ko-kr/translation.json` (config)
- `locales/pt-br/translation.json` (config)
- `locales/ru-ru/translation.json` (config)
- `locales/sv-se/translation.json` (config)
- `locales/uk-ua/translation.json` (config)
- `locales/zh-cn/translation.json` (config)
- `locales/zh-tw/translation.json` (config)
- `package.json` (manifest)
- `tsconfig.docs.json` (config)
- `tsconfig.json` (config)
- `typedoc.json` (config)

## Top-level layout

- `src` — 229 analysed file(s)
- `docs` — 23 analysed file(s)
- `tests` — 21 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `locales` — 12 analysed file(s)
- `plans` — 10 analysed file(s)
- `scripts` — 6 analysed file(s)
- `.github` — 5 analysed file(s)
- `reports` — 2 analysed file(s)
- `.claude` — 1 analysed file(s)
- `.ladle` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0d0cfbaabcee8e6dc69b78e4f3517829f9c4fcce` is the revision these paths and observations refer to.
