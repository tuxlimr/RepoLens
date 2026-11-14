# Project structure: mattdelacdev/WOW

**Analysed commit:** `c248bd26104b759f5efc7a1f5dcca7e758b5c793`

**Commit reference:** [c248bd26104b759f5efc7a1f5dcca7e758b5c793](https://github.com/mattdelacdev/WOW/commit/c248bd26104b759f5efc7a1f5dcca7e758b5c793)

**Tree at this commit:** [mattdelacdev/WOW@c248bd26104b](https://github.com/mattdelacdev/WOW/tree/c248bd26104b759f5efc7a1f5dcca7e758b5c793)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mattdelacdev/WOW |
| Description | Reveal CSS animation as you scroll down a page |
| Stars | 9890 |
| Forks | 3936 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `c248bd26104b759f5efc7a1f5dcca7e758b5c793` |
| Retrieved at | 2026-11-14T19:12:47.504047+00:00 |
| Files in this snapshot | 17 |

## Directory tree

```text
css/  (2 files)
  libs/  (1 files)
    animate.css
  site.css
spec/  (7 files)
  coffeescripts/  (2 files)
    helpers/  (1 files)
      … 1 files under this directory
    wow-spec.coffee
  javascripts/  (5 files)
    fixtures/  (2 files)
      … 2 files under this directory
    helpers/  (1 files)
      … 1 files under this directory
    libs/  (1 files)
      … 1 files under this directory
    wow-spec.js
src/  (1 files)
  wow.coffee
.gitignore
.travis.yml
Gruntfile.js
README.md
bower.json
demo.html
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| spec package | library | Observed | Groups 3 file(s) under spec package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `bower.json` (config)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 7 analysed file(s)
- `spec` — 7 analysed file(s)
- `css` — 2 analysed file(s)
- `src` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `c248bd26104b759f5efc7a1f5dcca7e758b5c793` is the revision these paths and observations refer to.
