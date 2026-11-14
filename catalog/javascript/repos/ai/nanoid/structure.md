# Project structure: ai/nanoid

**Analysed commit:** `055d1700cc67ac843e3efb5235d806b419ec7b2b`

**Commit reference:** [055d1700cc67ac843e3efb5235d806b419ec7b2b](https://github.com/ai/nanoid/commit/055d1700cc67ac843e3efb5235d806b419ec7b2b)

**Tree at this commit:** [ai/nanoid@055d1700cc67](https://github.com/ai/nanoid/tree/055d1700cc67ac843e3efb5235d806b419ec7b2b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ai/nanoid |
| Description | A tiny (118 bytes), secure, URL-friendly, unique string ID generator for JavaScript |
| Stars | 27130 |
| Forks | 896 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `055d1700cc67ac843e3efb5235d806b419ec7b2b` |
| Retrieved at | 2026-11-14T19:10:54.278611+00:00 |
| Files in this snapshot | 44 |

## Directory tree

```text
.github/  (4 files)
  workflows/  (3 files)
    benchmark.yml
    release.yml
    test.yml
  FUNDING.yml
bin/  (1 files)
  nanoid.js
img/  (2 files)
  icon.svg
  logo.svg
non-secure/  (2 files)
  index.d.ts
  index.js
test/  (10 files)
  demo/  (2 files)
    index.html
    index.js
  benchmark.js
  bin.test.js
  check-prebuild.js
  index.test.js
  non-secure.test.js
  pool.test.js
  prebuild.js
  update-prebuild.js
url-alphabet/  (1 files)
  index.js
.devcontainer.json
.editorconfig
.gitignore
.npmignore
.prettierignore
.prettierrc.js
CHANGELOG.md
LICENSE
README.ar.md
README.id-ID.md
README.ja.md
README.ko.md
README.md
README.ru.md
README.zh-CN.md
SECURITY.md
index.browser.js
index.d.ts
index.js
nanoid.js
oxfmt.config.ts
oxlint.config.ts
package.json
pnpm-workspace.yaml
```

## Entry points

- [bin/nanoid.js](https://github.com/ai/nanoid/blob/055d1700cc67ac843e3efb5235d806b419ec7b2b/bin/nanoid.js)
- [index.js](https://github.com/ai/nanoid/blob/055d1700cc67ac843e3efb5235d806b419ec7b2b/index.js)
- [non-secure/index.js](https://github.com/ai/nanoid/blob/055d1700cc67ac843e3efb5235d806b419ec7b2b/non-secure/index.js)
- [url-alphabet/index.js](https://github.com/ai/nanoid/blob/055d1700cc67ac843e3efb5235d806b419ec7b2b/url-alphabet/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| non-secure package | library | Observed | Groups 2 file(s) under non-secure package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 10 file(s) under tests (observed from repository paths and static analysis). |
| url-alphabet package | library | Observed | Groups 1 file(s) under url-alphabet package (observed from repository paths and static analysis). |

## Important files

- `.devcontainer.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/benchmark.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)

## Top-level layout

- `(root files)` — 24 analysed file(s)
- `test` — 10 analysed file(s)
- `.github` — 4 analysed file(s)
- `img` — 2 analysed file(s)
- `non-secure` — 2 analysed file(s)
- `bin` — 1 analysed file(s)
- `url-alphabet` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `055d1700cc67ac843e3efb5235d806b419ec7b2b` is the revision these paths and observations refer to.
