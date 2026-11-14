# Project structure: ccampbell/mousetrap

**Analysed commit:** `2f9a476ba6158ba69763e4fcf914966cc72ef433`

**Commit reference:** [2f9a476ba6158ba69763e4fcf914966cc72ef433](https://github.com/ccampbell/mousetrap/commit/2f9a476ba6158ba69763e4fcf914966cc72ef433)

**Tree at this commit:** [ccampbell/mousetrap@2f9a476ba615](https://github.com/ccampbell/mousetrap/tree/2f9a476ba6158ba69763e4fcf914966cc72ef433)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ccampbell/mousetrap |
| Description | Simple library for handling keyboard shortcuts in Javascript |
| Stars | 11770 |
| Forks | 948 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `2f9a476ba6158ba69763e4fcf914966cc72ef433` |
| Retrieved at | 2026-11-14T19:12:15.501485+00:00 |
| Files in this snapshot | 22 |

## Directory tree

```text
plugins/  (12 files)
  bind-dictionary/  (2 files)
    README.md
    mousetrap-bind-dictionary.js
  global-bind/  (2 files)
    README.md
    mousetrap-global-bind.js
  pause/  (2 files)
    README.md
    mousetrap-pause.js
  record/  (5 files)
    tests/  (3 files)
      … 3 files under this directory
    README.md
    mousetrap-record.js
  README.md
tests/  (3 files)
  libs/  (1 files)
    key-event.js
  mousetrap.html
  test.mousetrap.js
.gitignore
Gruntfile.js
LICENSE
README.md
mousetrap.js
mousetrap.sublime-project
package.json
```

## Entry points

- [mousetrap.js](https://github.com/ccampbell/mousetrap/blob/2f9a476ba6158ba69763e4fcf914966cc72ef433/mousetrap.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 4 file(s) under plugins package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `package.json` (manifest)

## Top-level layout

- `plugins` — 12 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `tests` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2f9a476ba6158ba69763e4fcf914966cc72ef433` is the revision these paths and observations refer to.
