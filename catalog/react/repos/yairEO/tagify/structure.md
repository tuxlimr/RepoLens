# Project structure: yairEO/tagify

**Analysed commit:** `ccff02c20cfa0af9f512bccd85cd5375da6fbf88`

**Commit reference:** [ccff02c20cfa0af9f512bccd85cd5375da6fbf88](https://github.com/yairEO/tagify/commit/ccff02c20cfa0af9f512bccd85cd5375da6fbf88)

**Tree at this commit:** [yairEO/tagify@ccff02c20cfa](https://github.com/yairEO/tagify/tree/ccff02c20cfa0af9f512bccd85cd5375da6fbf88)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | yairEO/tagify |
| Description | 🔖 lightweight, efficient Tags input component in Vanilla JS / React / Angular / Vue |
| Stars | 3891 |
| Forks | 446 |
| Licence | Other |
| Language | HTML |
| Default branch | master |
| Analysed commit | `ccff02c20cfa0af9f512bccd85cd5375da6fbf88` |
| Retrieved at | 2026-11-14T19:15:02.305717+00:00 |
| Files in this snapshot | 103 |

## Directory tree

```text
.cursor/  (4 files)
  docs/  (2 files)
    events--mix-mode--tag-deletion.md
    paste-as-tags-mix-mode.md
  plans/  (1 files)
    rollup_v3_then_v4.plan.md
  rules/  (1 files)
    repowise.mdc
.github/  (3 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    help-with-something.md
docs/  (57 files)
  examples/  (48 files)
    src/  (48 files)
      … 48 files under this directory
  homepage/  (5 files)
    head.html
    header.html
    index.html
    scripts.html
    section.njk
  codepen.css
  codepen.js
  logo.svg
  readme-header.svg
src/  (13 files)
  parts/  (10 files)
    EventDispatcher.js
    constants.js
    defaults.js
    dropdown.js
    events.js
    helpers.js
    persist.js
    suggestions.js
    templates.js
    texts.js
  react.tagify.js
  tagify.js
  tagify.scss
test/  (15 files)
  basic-RTL.html
  basic.html
  dragsort.html
  easy-to-customize.html
  manual-suggestions.html
  mix.html
  mode-select.html
  scroll-tracking.html
  tagify.test.js
  test.html
  test2.html
  text-input.html
  textarea.html
  users-list.html
  validate.html
tests/  (1 files)
  basic.spec.js
.eslintrc
.gitattributes
.gitignore
LICENSE
README.md
gulpfile.js
index.html
package.json
playwright.config.js
roadmap.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| parts package | library | Observed | Groups 10 file(s) under parts package (observed from repository paths and static analysis). |
| react.tagify.js package | library | Observed | Groups 1 file(s) under react.tagify.js package (observed from repository paths and static analysis). |
| tagify.js package | library | Observed | Groups 1 file(s) under tagify.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 16 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `package.json` (manifest)

## Top-level layout

- `docs` — 57 analysed file(s)
- `test` — 15 analysed file(s)
- `src` — 13 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.cursor` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 23 file(s) were skipped during inventory (1 x lockfile excluded; 22 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ccff02c20cfa0af9f512bccd85cd5375da6fbf88` is the revision these paths and observations refer to.
