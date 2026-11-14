# Project structure: VerbalExpressions/JSVerbalExpressions

**Analysed commit:** `34a9dddc18132f167fb4f4ceabbd7358e22bf7d8`

**Commit reference:** [34a9dddc18132f167fb4f4ceabbd7358e22bf7d8](https://github.com/VerbalExpressions/JSVerbalExpressions/commit/34a9dddc18132f167fb4f4ceabbd7358e22bf7d8)

**Tree at this commit:** [VerbalExpressions/JSVerbalExpressions@34a9dddc1813](https://github.com/VerbalExpressions/JSVerbalExpressions/tree/34a9dddc18132f167fb4f4ceabbd7358e22bf7d8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | VerbalExpressions/JSVerbalExpressions |
| Description | JavaScript Regular expressions made easy |
| Stars | 12112 |
| Forks | 492 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `34a9dddc18132f167fb4f4ceabbd7358e22bf7d8` |
| Retrieved at | 2026-11-14T19:12:10.504390+00:00 |
| Files in this snapshot | 34 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (4 files)
    automerge.yml
    codeql-analysis.yml
    gh-pages.yml
    test.yml
  dependabot.yml
docs/  (17 files)
  VerbalExpression/  (9 files)
    capture-groups.md
    constructor.md
    index.md
    loops.md
    miscellaneous.md
    modifiers.md
    rules.md
    special-characters.md
    utilities.md
  _layouts/  (1 files)
    default.html
  assets/  (1 files)
    css/  (1 files)
      … 1 files under this directory
  404.md
  Gemfile
  Gemfile.lock
  VerEx.md
  _config.yml
  index.md
test/  (1 files)
  tests.js
typings/  (1 files)
  VerbalExpressions.d.ts
.editorconfig
.eslintrc
.gitignore
.mdlintrc.json
Gruntfile.js
LICENSE
README.md
VerbalExpressions.js
bower.json
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |
| typings package | library | Observed | Groups 1 file(s) under typings package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/automerge.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/gh-pages.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.mdlintrc.json` (config)
- `bower.json` (config)
- `docs/_config.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `docs` — 17 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 5 analysed file(s)
- `test` — 1 analysed file(s)
- `typings` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `34a9dddc18132f167fb4f4ceabbd7358e22bf7d8` is the revision these paths and observations refer to.
