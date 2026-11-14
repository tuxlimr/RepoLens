# Project structure: Chalarangelo/30-seconds-of-interviews

**Analysed commit:** `da235b6185721161b7ebc413075b76dc70339ccf`

**Commit reference:** [da235b6185721161b7ebc413075b76dc70339ccf](https://github.com/Chalarangelo/30-seconds-of-interviews/commit/da235b6185721161b7ebc413075b76dc70339ccf)

**Tree at this commit:** [Chalarangelo/30-seconds-of-interviews@da235b618572](https://github.com/Chalarangelo/30-seconds-of-interviews/tree/da235b6185721161b7ebc413075b76dc70339ccf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Chalarangelo/30-seconds-of-interviews |
| Description | A curated collection of common interview questions to help you prepare for your next interview. |
| Stars | 12124 |
| Forks | 964 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `da235b6185721161b7ebc413075b76dc70339ccf` |
| Retrieved at | 2026-11-14T19:12:09.964179+00:00 |
| Files in this snapshot | 183 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    new-feature.md
    wrong-answer.md
  PULL_REQUEST_TEMPLATE.md
.travis/  (6 files)
  build.sh
  checkIfCron.sh
  forcepush.sh
  lintweb.sh
  push.sh
  write_cname.sh
data/  (1 files)
  questions.json
docs/  (8 files)
  .nojekyll
  CNAME
  header.f710438d.svg
  index.html
  modern-normalize.1ceaea8e.css
  prism.610ed272.css
  website.29127d6f.css
  website.972908d6.css
questions/  (110 files)
  .eslintrc.js
  accessibility-aria.md
  accessibility-contrast.md
  accessibility-testing.md
  accessibility-tree.md
  alt-attribute.md
  async-defer-attributes.md
  async-functions.md
  batches.md
  bem.md
  big-o-notation.md
  bind-function.md
  cache-busting.md
  callback-hell.md
  callback-in-setState.md
  callback-refs-vs-finddomnode.md
  callbacks.md
  children-prop.md
  class-name.md
  clone-object.md
  closures.md
  comparing-objects.md
  context.md
  cors.md
  … 86 more files
scripts/  (4 files)
  .eslintrc.js
  build.js
  extract.js
  util.js
static-parts/  (2 files)
  README-end.md
  README-start.md
website/  (35 files)
  css/  (13 files)
    components/  (9 files)
      … 9 files under this directory
    _base.scss
    _prism.scss
    _vars.scss
    index.scss
  img/  (1 files)
    header.svg
  js/  (19 files)
    components/  (14 files)
      … 14 files under this directory
    actions.js
    browser.js
    state.js
    utils.js
    view.js
  index.html
  index.js
.babelrc
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.prettierrc.js
.travis.yml
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
logo.svg
package.json
question-template.md
```

## Entry points

- [website/index.js](https://github.com/Chalarangelo/30-seconds-of-interviews/blob/da235b6185721161b7ebc413075b76dc70339ccf/website/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| questions package | library | Observed | Groups 1 file(s) under questions package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 20 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `data/questions.json` (config)
- `package.json` (manifest)

## Top-level layout

- `questions` — 110 analysed file(s)
- `website` — 35 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `docs` — 8 analysed file(s)
- `.travis` — 6 analysed file(s)
- `scripts` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `static-parts` — 2 analysed file(s)
- `data` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `da235b6185721161b7ebc413075b76dc70339ccf` is the revision these paths and observations refer to.
