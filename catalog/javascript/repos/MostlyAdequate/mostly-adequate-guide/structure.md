# Project structure: MostlyAdequate/mostly-adequate-guide

**Analysed commit:** `239468e9bc4ce1f0143722f312eb2487cac846ea`

**Commit reference:** [239468e9bc4ce1f0143722f312eb2487cac846ea](https://github.com/MostlyAdequate/mostly-adequate-guide/commit/239468e9bc4ce1f0143722f312eb2487cac846ea)

**Tree at this commit:** [MostlyAdequate/mostly-adequate-guide@239468e9bc4c](https://github.com/MostlyAdequate/mostly-adequate-guide/tree/239468e9bc4ce1f0143722f312eb2487cac846ea)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | MostlyAdequate/mostly-adequate-guide |
| Description | Mostly adequate guide to FP (in javascript) |
| Stars | 23817 |
| Forks | 1865 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `239468e9bc4ce1f0143722f312eb2487cac846ea` |
| Retrieved at | 2026-11-14T19:11:03.841995+00:00 |
| Files in this snapshot | 124 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    build.yml
exercises/  (87 files)
  ch04/  (9 files)
    exercise_a.js
    exercise_b.js
    exercise_c.js
    solution_a.js
    solution_b.js
    solution_c.js
    validation_a.js
    validation_b.js
    validation_c.js
  ch05/  (9 files)
    exercise_a.js
    exercise_b.js
    exercise_c.js
    solution_a.js
    solution_b.js
    solution_c.js
    validation_a.js
    validation_b.js
    validation_c.js
  ch06/  (2 files)
    index.html
    main.js
  ch08/  (12 files)
    exercise_a.js
    exercise_b.js
    exercise_c.js
    exercise_d.js
    solution_a.js
    solution_b.js
    solution_c.js
    solution_d.js
    validation_a.js
    validation_b.js
    validation_c.js
    validation_d.js
  ch09/  (9 files)
    exercise_a.js
    exercise_b.js
    exercise_c.js
    solution_a.js
    solution_b.js
    solution_c.js
    validation_a.js
    validation_b.js
    validation_c.js
  ch10/  (9 files)
    exercise_a.js
    exercise_b.js
    exercise_c.js
    solution_a.js
    solution_b.js
    solution_c.js
    validation_a.js
    validation_b.js
    validation_c.js
  ch11/  (9 files)
    exercise_a.js
    exercise_b.js
    exercise_c.js
    solution_a.js
    solution_b.js
    solution_c.js
    validation_a.js
    validation_b.js
    validation_c.js
  ch12/  (9 files)
    exercise_a.js
    exercise_b.js
    exercise_c.js
    solution_a.js
    solution_b.js
    solution_c.js
    validation_a.js
    validation_b.js
    validation_c.js
  test/  (14 files)
    ch04.js
    ch04.solutions.js
    ch05.js
    ch05.solutions.js
    ch08.js
    ch08.solutions.js
    ch09.js
    ch09.solutions.js
    ch10.js
    ch10.solutions.js
    ch11.js
    ch11.solutions.js
    ch12.js
    ch12.solutions.js
  .eslintrc.js
  README.md
  package.json
  support.js
  test-utils.js
styles/  (1 files)
  website.css
support/  (7 files)
  .eslintrc.js
  .npmignore
  CHANGELOG.md
  README.md
  build-appendixes
  index.js
  package.json
.editorconfig
.generate-summary.pl
.gitignore
.nvmrc
CONTRIBUTING.md
FAQ.md
LICENSE
README.md
SUMMARY.md
TRANSLATIONS.md
appendix_a.md
appendix_b.md
appendix_c.md
book.json
ch01.md
ch02.md
ch03.md
ch04.md
ch05.md
ch06.md
ch07.md
ch08.md
ch09.md
ch10.md
… 4 more files
```

## Entry points

- [support/index.js](https://github.com/MostlyAdequate/mostly-adequate-guide/blob/239468e9bc4ce1f0143722f312eb2487cac846ea/support/index.js)
- [exercises/ch06/main.js](https://github.com/MostlyAdequate/mostly-adequate-guide/blob/239468e9bc4ce1f0143722f312eb2487cac846ea/exercises/ch06/main.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| exercises package | library | Observed | Groups 70 file(s) under exercises package (observed from repository paths and static analysis). |
| support package | library | Observed | Groups 2 file(s) under support package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 14 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/build.yml` (ci)
- `book.json` (config)
- `exercises/package.json` (manifest)
- `package.json` (manifest)
- `support/package.json` (manifest)

## Top-level layout

- `exercises` — 87 analysed file(s)
- `(root files)` — 28 analysed file(s)
- `support` — 7 analysed file(s)
- `.github` — 1 analysed file(s)
- `styles` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `239468e9bc4ce1f0143722f312eb2487cac846ea` is the revision these paths and observations refer to.
