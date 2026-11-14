# Project structure: webrtc/samples

**Analysed commit:** `6bd116932df29815b39ebcbba3415366a6202662`

**Commit reference:** [6bd116932df29815b39ebcbba3415366a6202662](https://github.com/webrtc/samples/commit/6bd116932df29815b39ebcbba3415366a6202662)

**Tree at this commit:** [webrtc/samples@6bd116932df2](https://github.com/webrtc/samples/tree/6bd116932df29815b39ebcbba3415366a6202662)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | webrtc/samples |
| Description | WebRTC Web demos and samples |
| Stars | 14645 |
| Forks | 5652 |
| Licence | BSD-3-Clause |
| Language | JavaScript |
| Default branch | gh-pages |
| Analysed commit | `6bd116932df29815b39ebcbba3415366a6202662` |
| Retrieved at | 2026-11-14T19:11:44.541392+00:00 |
| Files in this snapshot | 235 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    config.yml
  workflows/  (2 files)
    interop-tests.yml
    test.yml
  PULL_REQUEST_TEMPLATE.md
src/  (215 files)
  content/  (205 files)
    capture/  (25 files)
      … 25 files under this directory
    datachannel/  (19 files)
      … 19 files under this directory
    devices/  (6 files)
      … 6 files under this directory
    extensions/  (8 files)
      … 8 files under this directory
    getusermedia/  (27 files)
      … 27 files under this directory
    insertable-streams/  (39 files)
      … 39 files under this directory
    peerconnection/  (81 files)
      … 81 files under this directory
  css/  (1 files)
    main.css
  js/  (9 files)
    lib/  (1 files)
      … 1 files under this directory
    third_party/  (7 files)
      … 7 files under this directory
    videopipe.js
test/  (5 files)
  interop/  (1 files)
    connection.test.js
  download-browsers.js
  steps.js
  webdriver.js
  webrtcclient.js
.eslintrc.js
.gitignore
.stylelintrc
AUTHORS
CONTRIBUTING.md
LICENSE.md
README.md
google1b7eb21c5b594ba0.html
index.html
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| content package | library | Observed | Groups 100 file(s) under content package (observed from repository paths and static analysis). |
| js package | library | Observed | Groups 9 file(s) under js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 5 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/interop-tests.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `package.json` (manifest)
- `src/content/extensions/multipleroutes/src/_locales/en/messages.json` (config)
- `src/content/extensions/multipleroutes/src/manifest.json` (config)

## Top-level layout

- `src` — 215 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 5 analysed file(s)
- `test` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6bd116932df29815b39ebcbba3415366a6202662` is the revision these paths and observations refer to.
