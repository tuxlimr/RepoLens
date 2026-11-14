# Project structure: jojoldu/junior-recruit-scheduler

**Analysed commit:** `0347115bab838376b9daafa48dd14ff392f64383`

**Commit reference:** [0347115bab838376b9daafa48dd14ff392f64383](https://github.com/jojoldu/junior-recruit-scheduler/commit/0347115bab838376b9daafa48dd14ff392f64383)

**Tree at this commit:** [jojoldu/junior-recruit-scheduler@0347115bab83](https://github.com/jojoldu/junior-recruit-scheduler/tree/0347115bab838376b9daafa48dd14ff392f64383)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jojoldu/junior-recruit-scheduler |
| Description | 주니어 개발자 채용 정보 |
| Stars | 11251 |
| Forks | 1591 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `0347115bab838376b9daafa48dd14ff392f64383` |
| Retrieved at | 2026-11-14T19:12:23.503969+00:00 |
| Files in this snapshot | 15 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
data/  (1 files)
  db.json
json-validate/  (1 files)
  src/  (1 files)
    build.js
.eslintrc.js
.gitignore
.nvmrc
.prettierrc
.travis.yml
README-en_EN.md
README-zh_CN.md
README.md
package.json
tsconfig.build.json
tsconfig.eslint.json
tsconfig.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| json-validate package | library | Observed | Groups 1 file(s) under json-validate package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/ci.yml` (ci)
- `.travis.yml` (ci)
- `data/db.json` (config)
- `package.json` (manifest)
- `tsconfig.build.json` (config)
- `tsconfig.eslint.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `(root files)` — 12 analysed file(s)
- `.github` — 1 analysed file(s)
- `data` — 1 analysed file(s)
- `json-validate` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0347115bab838376b9daafa48dd14ff392f64383` is the revision these paths and observations refer to.
