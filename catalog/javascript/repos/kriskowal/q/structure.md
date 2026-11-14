# Project structure: kriskowal/q

**Analysed commit:** `d180f4a0b22499607ac750b56766c8829d6bff43`

**Commit reference:** [d180f4a0b22499607ac750b56766c8829d6bff43](https://github.com/kriskowal/q/commit/d180f4a0b22499607ac750b56766c8829d6bff43)

**Tree at this commit:** [kriskowal/q@d180f4a0b224](https://github.com/kriskowal/q/tree/d180f4a0b22499607ac750b56766c8829d6bff43)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | kriskowal/q |
| Description | A promise library for JavaScript |
| Stars | 14983 |
| Forks | 1176 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `d180f4a0b22499607ac750b56766c8829d6bff43` |
| Retrieved at | 2026-11-14T19:11:41.490539+00:00 |
| Files in this snapshot | 43 |

## Directory tree

```text
benchmark/  (2 files)
  compare-with-callbacks.js
  scenarios.js
design/  (9 files)
  README.md
  q0.js
  q1.js
  q2.js
  q3.js
  q4.js
  q5.js
  q6.js
  q7.js
examples/  (7 files)
  async-generators/  (6 files)
    0.html
    1-return.js
    2-error-propagation.js
    3-spawn.js
    4-flow-control.js
    README.md
  all.js
spec/  (9 files)
  lib/  (5 files)
    jasmine-1.2.0/  (4 files)
      … 4 files under this directory
    jasmine-promise.js
  aplus-adapter.js
  q-spec.html
  q-spec.js
  queue-spec.js
.coverignore
.gitignore
.jshintrc
.mailmap
.travis.yml
CHANGES.md
CONTRIBUTING.md
Gruntfile.js
LICENSE
README.md
VERSIONS.md
package.json
q.js
q.svg
queue.js
ref_send.md
```

## Entry points

- [q.js](https://github.com/kriskowal/q/blob/d180f4a0b22499607ac750b56766c8829d6bff43/q.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmark package | library | Observed | Groups 2 file(s) under benchmark package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| design package | library | Observed | Groups 8 file(s) under design package (observed from repository paths and static analysis). |
| spec package | library | Observed | Groups 6 file(s) under spec package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 16 analysed file(s)
- `design` — 9 analysed file(s)
- `spec` — 9 analysed file(s)
- `examples` — 7 analysed file(s)
- `benchmark` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `d180f4a0b22499607ac750b56766c8829d6bff43` is the revision these paths and observations refer to.
