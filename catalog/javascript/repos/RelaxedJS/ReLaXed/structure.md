# Project structure: RelaxedJS/ReLaXed

**Analysed commit:** `9e31cd446150afcaa1f2be1df09870ad4b444bfa`

**Commit reference:** [9e31cd446150afcaa1f2be1df09870ad4b444bfa](https://github.com/RelaxedJS/ReLaXed/commit/9e31cd446150afcaa1f2be1df09870ad4b444bfa)

**Tree at this commit:** [RelaxedJS/ReLaXed@9e31cd446150](https://github.com/RelaxedJS/ReLaXed/tree/9e31cd446150afcaa1f2be1df09870ad4b444bfa)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | RelaxedJS/ReLaXed |
| Description | Create PDF documents using web technologies |
| Stars | 11789 |
| Forks | 418 |
| Licence | ISC |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `9e31cd446150afcaa1f2be1df09870ad4b444bfa` |
| Retrieved at | 2026-11-14T19:12:14.958494+00:00 |
| Files in this snapshot | 65 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    npmpublish.yml
src/  (22 files)
  builtin_plugins/  (16 files)
    chartjs/  (2 files)
      … 2 files under this directory
    flowchart/  (2 files)
      … 2 files under this directory
    katex/  (2 files)
      … 2 files under this directory
    markdown/  (1 files)
      … 1 files under this directory
    mathjax/  (1 files)
      … 1 files under this directory
    mermaid/  (2 files)
      … 2 files under this directory
    scss/  (1 files)
      … 1 files under this directory
    table/  (2 files)
      … 2 files under this directory
    vegalite/  (2 files)
      … 2 files under this directory
    index.js
  cli-tools/  (2 files)
    pdf2gif.js
    pretty-pdf-thumbnail.js
  index.js
  masterToPDF.js
  parseLocals.js
  plugins.js
test/  (35 files)
  samples/  (34 files)
    interactive_example/  (6 files)
      … 6 files under this directory
    pug/  (21 files)
      … 21 files under this directory
    special_renderings/  (7 files)
      … 7 files under this directory
  test.js
.gitignore
.npmignore
.travis.yml
LICENCE.txt
README.md
changelog.md
package.json
```

## Entry points

- [src/masterToPDF.js](https://github.com/RelaxedJS/ReLaXed/blob/9e31cd446150afcaa1f2be1df09870ad4b444bfa/src/masterToPDF.js)
- [src/index.js](https://github.com/RelaxedJS/ReLaXed/blob/9e31cd446150afcaa1f2be1df09870ad4b444bfa/src/index.js)
- [src/cli-tools/pretty-pdf-thumbnail.js](https://github.com/RelaxedJS/ReLaXed/blob/9e31cd446150afcaa1f2be1df09870ad4b444bfa/src/cli-tools/pretty-pdf-thumbnail.js)
- [src/cli-tools/pdf2gif.js](https://github.com/RelaxedJS/ReLaXed/blob/9e31cd446150afcaa1f2be1df09870ad4b444bfa/src/cli-tools/pdf2gif.js)
- [src/builtin_plugins/chartjs/index.js](https://github.com/RelaxedJS/ReLaXed/blob/9e31cd446150afcaa1f2be1df09870ad4b444bfa/src/builtin_plugins/chartjs/index.js)
- [src/builtin_plugins/flowchart/index.js](https://github.com/RelaxedJS/ReLaXed/blob/9e31cd446150afcaa1f2be1df09870ad4b444bfa/src/builtin_plugins/flowchart/index.js)
- [src/builtin_plugins/index.js](https://github.com/RelaxedJS/ReLaXed/blob/9e31cd446150afcaa1f2be1df09870ad4b444bfa/src/builtin_plugins/index.js)
- [src/builtin_plugins/katex/index.js](https://github.com/RelaxedJS/ReLaXed/blob/9e31cd446150afcaa1f2be1df09870ad4b444bfa/src/builtin_plugins/katex/index.js)
- [src/builtin_plugins/markdown/index.js](https://github.com/RelaxedJS/ReLaXed/blob/9e31cd446150afcaa1f2be1df09870ad4b444bfa/src/builtin_plugins/markdown/index.js)
- [src/builtin_plugins/mathjax/index.js](https://github.com/RelaxedJS/ReLaXed/blob/9e31cd446150afcaa1f2be1df09870ad4b444bfa/src/builtin_plugins/mathjax/index.js)
- [src/builtin_plugins/mermaid/index.js](https://github.com/RelaxedJS/ReLaXed/blob/9e31cd446150afcaa1f2be1df09870ad4b444bfa/src/builtin_plugins/mermaid/index.js)
- [src/builtin_plugins/scss/index.js](https://github.com/RelaxedJS/ReLaXed/blob/9e31cd446150afcaa1f2be1df09870ad4b444bfa/src/builtin_plugins/scss/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| builtin_plugins package | library | Observed | Groups 10 file(s) under builtin_plugins package (observed from repository paths and static analysis). |
| cli-tools package | library | Observed | Groups 2 file(s) under cli-tools package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| masterToPDF.js package | library | Observed | Groups 1 file(s) under mastertopdf.js package (observed from repository paths and static analysis). |
| parseLocals.js package | library | Observed | Groups 1 file(s) under parselocals.js package (observed from repository paths and static analysis). |
| plugins.js package | library | Observed | Groups 1 file(s) under plugins.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 35 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/npmpublish.yml` (ci)
- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `test` — 35 analysed file(s)
- `src` — 22 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9e31cd446150afcaa1f2be1df09870ad4b444bfa` is the revision these paths and observations refer to.
