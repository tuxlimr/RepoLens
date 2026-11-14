# Project structure: forwardemail/supertest

**Analysed commit:** `aff97e7c8eed2ff88d650f6b451f04a321790f88`

**Commit reference:** [aff97e7c8eed2ff88d650f6b451f04a321790f88](https://github.com/forwardemail/supertest/commit/aff97e7c8eed2ff88d650f6b451f04a321790f88)

**Tree at this commit:** [forwardemail/supertest@aff97e7c8eed](https://github.com/forwardemail/supertest/tree/aff97e7c8eed2ff88d650f6b451f04a321790f88)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | forwardemail/supertest |
| Description | 🕷 Super-agent driven library for testing node.js HTTP servers using a fluent API.   Maintained for @forwardemail, @ladjs, @spamscanner, @breejs, @cabinjs, and @lassjs. |
| Stars | 14410 |
| Forks | 788 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `aff97e7c8eed2ff88d650f6b451f04a321790f88` |
| Retrieved at | 2026-11-14T19:11:45.076699+00:00 |
| Files in this snapshot | 20 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
ci/  (1 files)
  remove-deps-4-old-node.js
lib/  (4 files)
  cookies/  (2 files)
    assertion.js
    index.js
  agent.js
  test.js
test/  (5 files)
  .eslintrc
  cookies.js
  issue-fixes.js
  supertest.js
  throwError.js
.commitlintrc.js
.editorconfig
.eslintrc
.gitignore
.npmignore
LICENSE
README.md
index.js
package.json
```

## Entry points

- [index.js](https://github.com/forwardemail/supertest/blob/aff97e7c8eed2ff88d650f6b451f04a321790f88/index.js)
- [lib/cookies/index.js](https://github.com/forwardemail/supertest/blob/aff97e7c8eed2ff88d650f6b451f04a321790f88/lib/cookies/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| ci package | library | Observed | Groups 1 file(s) under ci package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 4 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 5 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 9 analysed file(s)
- `test` — 5 analysed file(s)
- `lib` — 4 analysed file(s)
- `.github` — 1 analysed file(s)
- `ci` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (3 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `aff97e7c8eed2ff88d650f6b451f04a321790f88` is the revision these paths and observations refer to.
