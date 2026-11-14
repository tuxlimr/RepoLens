# Project structure: jxnblk/mdx-deck

**Analysed commit:** `a4779fc0555e26bc241afd8176661d41fd6981ac`

**Commit reference:** [a4779fc0555e26bc241afd8176661d41fd6981ac](https://github.com/jxnblk/mdx-deck/commit/a4779fc0555e26bc241afd8176661d41fd6981ac)

**Tree at this commit:** [jxnblk/mdx-deck@a4779fc0555e](https://github.com/jxnblk/mdx-deck/tree/a4779fc0555e26bc241afd8176661d41fd6981ac)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jxnblk/mdx-deck |
| Description | ♠️ React MDX-based presentation decks |
| Stars | 11494 |
| Forks | 594 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `a4779fc0555e26bc241afd8176661d41fd6981ac` |
| Retrieved at | 2026-11-14T19:12:17.940783+00:00 |
| Files in this snapshot | 181 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
cypress/  (4 files)
  integration/  (1 files)
    hello.js
  plugins/  (1 files)
    index.js
  support/  (2 files)
    commands.js
    index.js
docs/  (11 files)
  Counter.js
  api.md
  components.md
  demo.mdx
  exporting.md
  gatsby.md
  layouts.md
  package.json
  presenting.md
  themes.md
  theming.md
examples/  (34 files)
  aspect-ratio/  (2 files)
    deck.mdx
    package.json
  basic/  (2 files)
    deck.mdx
    package.json
  gatsby/  (5 files)
    decks/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    gatsby-config.js
    package.json
  head/  (2 files)
    deck.mdx
    package.json
  header-footer/  (2 files)
    deck.mdx
    package.json
  images/  (2 files)
    deck.mdx
    package.json
  layouts/  (2 files)
    deck.mdx
    package.json
  multiple/  (4 files)
    deck.js
    one.mdx
    package.json
    two.mdx
  prism/  (2 files)
    deck.mdx
    package.json
  provider/  (3 files)
    deck.mdx
    package.json
    theme.js
  steps/  (2 files)
    deck.mdx
    package.json
  syntax-highlighting/  (2 files)
    deck.mdx
    package.json
  themes/  (3 files)
    deck.mdx
    package.json
    theme.js
  README.md
packages/  (115 files)
  create-deck/  (3 files)
    README.md
    cli.js
    package.json
  gatsby-plugin/  (29 files)
    src/  (16 files)
      … 16 files under this directory
    test/  (4 files)
      … 4 files under this directory
    .gitignore
    .npmignore
    README.md
    gatsby-browser.js
    gatsby-config.js
    gatsby-node.js
    gatsby-ssr.js
    index.js
    package.json
  gatsby-theme/  (48 files)
    decks/  (2 files)
      … 2 files under this directory
    src/  (38 files)
      … 38 files under this directory
    .gitignore
    README.md
    gatsby-browser.js
    gatsby-config.js
    gatsby-node.js
    gatsby-ssr.js
    index.js
    package.json
  mdx-deck/  (8 files)
    .gitignore
    .npmignore
    README.md
    cli.js
    gatsby-config.js
    hello.mdx
    index.js
    package.json
  starter/  (3 files)
    decks/  (1 files)
      … 1 files under this directory
    gatsby-config.js
    package.json
  themes/  (19 files)
    README.md
    base.js
    big.js
    book.js
    code.js
    comic.js
    condensed.js
    dark.js
    future.js
    index.js
    lobster.js
    notes.js
    package.json
    poppins.js
    script.js
    swiss.js
    syntax-highlighter-prism.js
    syntax-highlighter.js
    yellow.js
  website-pdf/  (5 files)
    .gitignore
    README.md
    cli.js
    index.js
    package.json
templates/  (5 files)
  basic/  (5 files)
    .gitignore
    README.md
    deck.mdx
    package.json
    theme.js
.gitignore
.prettierrc
CHANGELOG.md
CONTRIBUTING.md
LICENSE.md
MIGRATION.md
babel.config.js
cypress.json
lerna.json
netlify.toml
package.json
```

## Entry points

- [packages/create-deck/cli.js](https://github.com/jxnblk/mdx-deck/blob/a4779fc0555e26bc241afd8176661d41fd6981ac/packages/create-deck/cli.js)
- [packages/gatsby-plugin/index.js](https://github.com/jxnblk/mdx-deck/blob/a4779fc0555e26bc241afd8176661d41fd6981ac/packages/gatsby-plugin/index.js)
- [packages/gatsby-theme/index.js](https://github.com/jxnblk/mdx-deck/blob/a4779fc0555e26bc241afd8176661d41fd6981ac/packages/gatsby-theme/index.js)
- [packages/mdx-deck/index.js](https://github.com/jxnblk/mdx-deck/blob/a4779fc0555e26bc241afd8176661d41fd6981ac/packages/mdx-deck/index.js)
- [packages/mdx-deck/cli.js](https://github.com/jxnblk/mdx-deck/blob/a4779fc0555e26bc241afd8176661d41fd6981ac/packages/mdx-deck/cli.js)
- [packages/themes/index.js](https://github.com/jxnblk/mdx-deck/blob/a4779fc0555e26bc241afd8176661d41fd6981ac/packages/themes/index.js)
- [packages/website-pdf/cli.js](https://github.com/jxnblk/mdx-deck/blob/a4779fc0555e26bc241afd8176661d41fd6981ac/packages/website-pdf/cli.js)
- [cypress/plugins/index.js](https://github.com/jxnblk/mdx-deck/blob/a4779fc0555e26bc241afd8176661d41fd6981ac/cypress/plugins/index.js)
- [cypress/support/index.js](https://github.com/jxnblk/mdx-deck/blob/a4779fc0555e26bc241afd8176661d41fd6981ac/cypress/support/index.js)
- [packages/gatsby-plugin/src/index.js](https://github.com/jxnblk/mdx-deck/blob/a4779fc0555e26bc241afd8176661d41fd6981ac/packages/gatsby-plugin/src/index.js)
- [packages/gatsby-theme/src/index.js](https://github.com/jxnblk/mdx-deck/blob/a4779fc0555e26bc241afd8176661d41fd6981ac/packages/gatsby-theme/src/index.js)
- [packages/website-pdf/index.js](https://github.com/jxnblk/mdx-deck/blob/a4779fc0555e26bc241afd8176661d41fd6981ac/packages/website-pdf/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| cypress package | library | Observed | Groups 3 file(s) under cypress package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 88 file(s) under packages package (observed from repository paths and static analysis). |
| templates package | library | Observed | Groups 1 file(s) under templates package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `cypress.json` (config)
- `docs/package.json` (manifest)
- `examples/aspect-ratio/package.json` (manifest)
- `examples/basic/package.json` (manifest)
- `examples/gatsby/package.json` (manifest)
- `examples/head/package.json` (manifest)
- `examples/header-footer/package.json` (manifest)
- `examples/images/package.json` (manifest)
- `examples/layouts/package.json` (manifest)
- `examples/multiple/package.json` (manifest)
- `examples/prism/package.json` (manifest)
- `examples/provider/package.json` (manifest)
- `examples/steps/package.json` (manifest)
- `examples/syntax-highlighting/package.json` (manifest)
- `examples/themes/package.json` (manifest)
- `lerna.json` (config)
- `netlify.toml` (config)
- `package.json` (manifest)
- `packages/create-deck/package.json` (manifest)
- `packages/gatsby-plugin/package.json` (manifest)
- `packages/gatsby-theme/package.json` (manifest)
- `packages/mdx-deck/package.json` (manifest)
- `packages/starter/package.json` (manifest)
- `packages/themes/package.json` (manifest)
- `packages/website-pdf/package.json` (manifest)
- `templates/basic/package.json` (manifest)

## Top-level layout

- `packages` — 115 analysed file(s)
- `examples` — 34 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `docs` — 11 analysed file(s)
- `templates` — 5 analysed file(s)
- `cypress` — 4 analysed file(s)
- `.circleci` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a4779fc0555e26bc241afd8176661d41fd6981ac` is the revision these paths and observations refer to.
