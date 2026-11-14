# Project structure: shelljs/shelljs

**Analysed commit:** `060e8ac15aa32b1311db15c5e12cd64016637932`

**Commit reference:** [060e8ac15aa32b1311db15c5e12cd64016637932](https://github.com/shelljs/shelljs/commit/060e8ac15aa32b1311db15c5e12cd64016637932)

**Tree at this commit:** [shelljs/shelljs@060e8ac15aa3](https://github.com/shelljs/shelljs/tree/060e8ac15aa32b1311db15c5e12cd64016637932)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | shelljs/shelljs |
| Description | :shell: Portable Unix shell commands for Node.js |
| Stars | 14400 |
| Forks | 766 |
| Licence | BSD-3-Clause |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `060e8ac15aa32b1311db15c5e12cd64016637932` |
| Retrieved at | 2026-11-14T19:11:45.368254+00:00 |
| Files in this snapshot | 170 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (1 files)
    main.yml
  ISSUE_TEMPLATE.md
  SECURITY.md
scripts/  (2 files)
  check-node-support.js
  generate-docs.js
src/  (34 files)
  cat.js
  cd.js
  chmod.js
  cmd.js
  common.js
  cp.js
  dirs.js
  echo.js
  error.js
  errorCode.js
  exec-child.js
  exec.js
  find.js
  grep.js
  head.js
  ln.js
  ls.js
  mkdir.js
  mv.js
  popd.js
  pushd.js
  pwd.js
  rm.js
  sed.js
  … 10 more files
test/  (116 files)
  resources/  (75 files)
    cat/  (5 files)
      … 5 files under this directory
    chmod/  (6 files)
      … 6 files under this directory
    cp/  (8 files)
      … 8 files under this directory
    cp-mode-bits/  (1 files)
      … 1 files under this directory
    exec/  (1 files)
      … 1 files under this directory
    external/  (1 files)
      … 1 files under this directory
    find/  (6 files)
      … 6 files under this directory
    grep/  (6 files)
      … 6 files under this directory
    head/  (4 files)
      … 4 files under this directory
    issue44/  (1 files)
      … 1 files under this directory
    ls/  (10 files)
      … 10 files under this directory
    pushd/  (2 files)
      … 2 files under this directory
    rm/  (1 files)
      … 1 files under this directory
    sed/  (1 files)
      … 1 files under this directory
    sort/  (4 files)
      … 4 files under this directory
    uniq/  (10 files)
      … 10 files under this directory
    which/  (1 files)
      … 1 files under this directory
    a.txt
    file1
    file1.js
    file1.txt
    file2
    file2.js
    file2.txt
  utils/  (2 files)
    mocks.js
    utils.js
  .eslintrc.json
  cat.js
  cd.js
  chmod.js
  cmd.js
  common.js
  config.js
  cp.js
  dirs.js
  docs.js
  echo.js
  env.js
  exec.js
  exit.js
  find.js
  global.js
  grep.js
  head.js
  ln.js
  ls.js
  mkdir.js
  mv.js
  pipe.js
  plugin.js
  … 15 more files
.editorconfig
.eslintignore
.eslintrc.json
.gitattributes
.gitignore
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
RELEASE.md
global.js
make.js
package.json
plugin.js
shell.js
```

## Entry points

- [shell.js](https://github.com/shelljs/shelljs/blob/060e8ac15aa32b1311db15c5e12cd64016637932/shell.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cat.js package | library | Observed | Groups 1 file(s) under cat.js package (observed from repository paths and static analysis). |
| cd.js package | library | Observed | Groups 1 file(s) under cd.js package (observed from repository paths and static analysis). |
| chmod.js package | library | Observed | Groups 1 file(s) under chmod.js package (observed from repository paths and static analysis). |
| cmd.js package | library | Observed | Groups 1 file(s) under cmd.js package (observed from repository paths and static analysis). |
| common.js package | library | Observed | Groups 1 file(s) under common.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| cp.js package | library | Observed | Groups 1 file(s) under cp.js package (observed from repository paths and static analysis). |
| dirs.js package | library | Observed | Groups 1 file(s) under dirs.js package (observed from repository paths and static analysis). |
| echo.js package | library | Observed | Groups 1 file(s) under echo.js package (observed from repository paths and static analysis). |
| error.js package | library | Observed | Groups 1 file(s) under error.js package (observed from repository paths and static analysis). |
| errorCode.js package | library | Observed | Groups 1 file(s) under errorcode.js package (observed from repository paths and static analysis). |
| exec-child.js package | library | Observed | Groups 1 file(s) under exec-child.js package (observed from repository paths and static analysis). |
| exec.js package | library | Observed | Groups 1 file(s) under exec.js package (observed from repository paths and static analysis). |
| find.js package | library | Observed | Groups 1 file(s) under find.js package (observed from repository paths and static analysis). |
| grep.js package | library | Observed | Groups 1 file(s) under grep.js package (observed from repository paths and static analysis). |
| head.js package | library | Observed | Groups 1 file(s) under head.js package (observed from repository paths and static analysis). |
| ln.js package | library | Observed | Groups 1 file(s) under ln.js package (observed from repository paths and static analysis). |
| ls.js package | library | Observed | Groups 1 file(s) under ls.js package (observed from repository paths and static analysis). |
| mkdir.js package | library | Observed | Groups 1 file(s) under mkdir.js package (observed from repository paths and static analysis). |
| mv.js package | library | Observed | Groups 1 file(s) under mv.js package (observed from repository paths and static analysis). |
| popd.js package | library | Observed | Groups 1 file(s) under popd.js package (observed from repository paths and static analysis). |
| pushd.js package | library | Observed | Groups 1 file(s) under pushd.js package (observed from repository paths and static analysis). |
| pwd.js package | library | Observed | Groups 1 file(s) under pwd.js package (observed from repository paths and static analysis). |
| rm.js package | library | Observed | Groups 1 file(s) under rm.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| sed.js package | library | Observed | Groups 1 file(s) under sed.js package (observed from repository paths and static analysis). |
| set.js package | library | Observed | Groups 1 file(s) under set.js package (observed from repository paths and static analysis). |
| sort.js package | library | Observed | Groups 1 file(s) under sort.js package (observed from repository paths and static analysis). |
| tail.js package | library | Observed | Groups 1 file(s) under tail.js package (observed from repository paths and static analysis). |
| tempdir.js package | library | Observed | Groups 1 file(s) under tempdir.js package (observed from repository paths and static analysis). |
| test.js package | library | Observed | Groups 1 file(s) under test.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 116 file(s) under tests (observed from repository paths and static analysis). |
| to.js package | library | Observed | Groups 1 file(s) under to.js package (observed from repository paths and static analysis). |
| toEnd.js package | library | Observed | Groups 1 file(s) under toend.js package (observed from repository paths and static analysis). |
| touch.js package | library | Observed | Groups 1 file(s) under touch.js package (observed from repository paths and static analysis). |
| uniq.js package | library | Observed | Groups 1 file(s) under uniq.js package (observed from repository paths and static analysis). |
| which.js package | library | Observed | Groups 1 file(s) under which.js package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/workflows/main.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `test` — 116 analysed file(s)
- `src` — 34 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 3 analysed file(s)
- `scripts` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `060e8ac15aa32b1311db15c5e12cd64016637932` is the revision these paths and observations refer to.
