# Project structure: bevacqua/dragula

**Analysed commit:** `09ab978dd550490f1f8e456551a1a39ed0d7f984`

**Commit reference:** [09ab978dd550490f1f8e456551a1a39ed0d7f984](https://github.com/bevacqua/dragula/commit/09ab978dd550490f1f8e456551a1a39ed0d7f984)

**Tree at this commit:** [bevacqua/dragula@09ab978dd550](https://github.com/bevacqua/dragula/tree/09ab978dd550490f1f8e456551a1a39ed0d7f984)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | bevacqua/dragula |
| Description | :ok_hand: Drag and drop so simple it hurts |
| Stars | 22113 |
| Forks | 1913 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `09ab978dd550490f1f8e456551a1a39ed0d7f984` |
| Retrieved at | 2026-11-14T19:11:09.279987+00:00 |
| Files in this snapshot | 33 |

## Directory tree

```text
.github/  (3 files)
  FUNDING.yml
  contributing.markdown
  issue_template.markdown
example/  (2 files)
  example.css
  example.js
resources/  (3 files)
  icon.svg
  logo.svg
  patreon.svg
test/  (12 files)
  lib/  (1 files)
    events.js
  cancel.js
  classes.js
  containers.js
  defaults.js
  destroy.js
  drag.js
  drake-api.js
  end.js
  events.js
  public-api.js
  remove.js
.editorconfig
.gitignore
.jshintignore
.jshintrc
.travis.yml
changelog.markdown
classes.js
dragula.js
dragula.styl
index.html
license
package.json
readme.markdown
```

## Entry points

- [dragula.js](https://github.com/bevacqua/dragula/blob/09ab978dd550490f1f8e456551a1a39ed0d7f984/dragula.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 12 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 13 analysed file(s)
- `test` — 12 analysed file(s)
- `.github` — 3 analysed file(s)
- `resources` — 3 analysed file(s)
- `example` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `09ab978dd550490f1f8e456551a1a39ed0d7f984` is the revision these paths and observations refer to.
