# Project structure: showdownjs/showdown

**Analysed commit:** `d1a8d16344b855ea2f37677ee8a9e0cc2c597ea4`

**Commit reference:** [d1a8d16344b855ea2f37677ee8a9e0cc2c597ea4](https://github.com/showdownjs/showdown/commit/d1a8d16344b855ea2f37677ee8a9e0cc2c597ea4)

**Tree at this commit:** [showdownjs/showdown@d1a8d16344b8](https://github.com/showdownjs/showdown/tree/d1a8d16344b855ea2f37677ee8a9e0cc2c597ea4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | showdownjs/showdown |
| Description | A bidirectional Markdown to HTML to Markdown converter written in Javascript |
| Stars | 14881 |
| Forks | 1559 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `d1a8d16344b855ea2f37677ee8a9e0cc2c597ea4` |
| Retrieved at | 2026-11-14T19:11:42.820912+00:00 |
| Files in this snapshot | 132 |

## Directory tree

```text
.github/  (7 files)
  workflows/  (6 files)
    browser.yml
    browserstack.yml
    codeql-analysis.yml
    docs.yml
    node.linux.yml
    node.win.yml
  dependabot.yml
bin/  (1 files)
  showdown.js
docs/  (28 files)
  assets/  (1 files)
    extra.css
  tutorials/  (4 files)
    add-default-class-to-html.md
    index.md
    markdown-editor-with-showdown.md
    use-both-extension-types-together.md
  api-reference.md
  cli.md
  commonmark.md
  contribution-guide.md
  create-extension.md
  credits.md
  event-system.md
  extensions-list.md
  extensions.md
  flavors.md
  gfm.md
  html-to-markdown.md
  index.md
  integrations.md
  local-development.md
  markdown-syntax.md
  markdown-to-html.md
  options.md
  original.md
  quickstart.md
  requirements.txt
  syntax-overview.md
  xss.md
overrides/  (1 files)
  partials/  (1 files)
    nav.html
specs/  (3 files)
  comparison.md
  original.md
  showdown.md
src/  (78 files)
  cli/  (1 files)
    cli.js
  helpers/  (17 files)
    commonmark.js
    emojis.js
    encodeCode.js
    escapes.js
    gfmAutolinks.js
    hashBlock.js
    hashHTMLBlocks.js
    hashHTMLSpans.js
    htmlEntities.js
    lazyDocument.js
    markdownEscapes.js
    misc.js
    regexes.js
    text.js
    types.js
    unhashHTMLSpans.js
    url.js
  subParsers/  (55 files)
    makehtml/  (33 files)
      … 33 files under this directory
    makemarkdown/  (22 files)
      … 22 files under this directory
  converter.js
  event.js
  loader.js
  options.js
  showdown.js
CHANGELOG.md
CONTRIBUTING.md
DONATIONS.md
LICENSE
README.md
SECURITY.md
TASKS.TODO.md
bower.json
browserstack.yml
mkdocs.yml
package.json
playwright.bstack.config.js
vitest.browser.config.mjs
vitest.config.mjs
```

## Entry points

- [bin/showdown.js](https://github.com/showdownjs/showdown/blob/d1a8d16344b855ea2f37677ee8a9e0cc2c597ea4/bin/showdown.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| cli package | library | Observed | Groups 1 file(s) under cli package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| converter.js package | library | Observed | Groups 1 file(s) under converter.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| event.js package | library | Observed | Groups 1 file(s) under event.js package (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 17 file(s) under helpers package (observed from repository paths and static analysis). |
| loader.js package | library | Observed | Groups 1 file(s) under loader.js package (observed from repository paths and static analysis). |
| options.js package | library | Observed | Groups 1 file(s) under options.js package (observed from repository paths and static analysis). |
| showdown.js package | library | Observed | Groups 1 file(s) under showdown.js package (observed from repository paths and static analysis). |
| subParsers package | library | Observed | Groups 55 file(s) under subparsers package (observed from repository paths and static analysis). |

## Important files

- `.github/dependabot.yml` (config)
- `.github/workflows/browser.yml` (ci)
- `.github/workflows/browserstack.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/node.linux.yml` (ci)
- `.github/workflows/node.win.yml` (ci)
- `bower.json` (config)
- `browserstack.yml` (config)
- `docs/requirements.txt` (manifest)
- `mkdocs.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 78 analysed file(s)
- `docs` — 28 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 7 analysed file(s)
- `specs` — 3 analysed file(s)
- `bin` — 1 analysed file(s)
- `overrides` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d1a8d16344b855ea2f37677ee8a9e0cc2c597ea4` is the revision these paths and observations refer to.
