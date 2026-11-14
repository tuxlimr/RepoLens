# Project structure: kefranabg/readme-md-generator

**Analysed commit:** `f0370c8efe602bfc1e1334ea556214de4c1b0f04`

**Commit reference:** [f0370c8efe602bfc1e1334ea556214de4c1b0f04](https://github.com/kefranabg/readme-md-generator/commit/f0370c8efe602bfc1e1334ea556214de4c1b0f04)

**Tree at this commit:** [kefranabg/readme-md-generator@f0370c8efe60](https://github.com/kefranabg/readme-md-generator/tree/f0370c8efe602bfc1e1334ea556214de4c1b0f04)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | kefranabg/readme-md-generator |
| Description | 📄 CLI that generates beautiful README.md files |
| Stars | 11135 |
| Forks | 1368 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `f0370c8efe602bfc1e1334ea556214de4c1b0f04` |
| Retrieved at | 2026-11-14T19:12:25.164351+00:00 |
| Files in this snapshot | 81 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    nodejs.yml
  CODE_OF_CONDUCT.md
  FUNDING.yml
.vscode/  (1 files)
  settings.json
src/  (62 files)
  __snapshots__/  (1 files)
    readme.spec.js.snap
  questions/  (44 files)
    author-github.js
    author-github.spec.js
    author-linkedin.js
    author-linkedin.spec.js
    author-name.js
    author-name.spec.js
    author-patreon.js
    author-patreon.spec.js
    author-twitter.js
    author-twitter.spec.js
    author-website.js
    author-website.spec.js
    contributing-url.js
    contributing-url.spec.js
    index.js
    index.spec.js
    install-command.js
    install-command.spec.js
    issues-url.js
    issues-url.spec.js
    license-name.js
    license-name.spec.js
    license-url.js
    license-url.spec.js
    … 20 more files
  ask-overwrite.js
  ask-overwrite.spec.js
  ask-questions.js
  ask-questions.spec.js
  choose-template.js
  choose-template.spec.js
  clean-context.js
  clean-context.spec.js
  cli.js
  cli.spec.js
  index.js
  project-infos.js
  project-infos.spec.js
  readme.js
  readme.spec.js
  utils.js
  utils.spec.js
templates/  (3 files)
  default-no-html.md
  default.md
  footer.md
.eslintrc.js
.gitignore
.prettierignore
.prettierrc
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
jest.config.js
package.json
```

## Entry points

- [src/index.js](https://github.com/kefranabg/readme-md-generator/blob/f0370c8efe602bfc1e1334ea556214de4c1b0f04/src/index.js)
- [src/questions/index.js](https://github.com/kefranabg/readme-md-generator/blob/f0370c8efe602bfc1e1334ea556214de4c1b0f04/src/questions/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| ask-overwrite.js package | library | Observed | Groups 1 file(s) under ask-overwrite.js package (observed from repository paths and static analysis). |
| ask-overwrite.spec.js package | library | Observed | Groups 1 file(s) under ask-overwrite.spec.js package (observed from repository paths and static analysis). |
| ask-questions.js package | library | Observed | Groups 1 file(s) under ask-questions.js package (observed from repository paths and static analysis). |
| ask-questions.spec.js package | library | Observed | Groups 1 file(s) under ask-questions.spec.js package (observed from repository paths and static analysis). |
| choose-template.js package | library | Observed | Groups 1 file(s) under choose-template.js package (observed from repository paths and static analysis). |
| choose-template.spec.js package | library | Observed | Groups 1 file(s) under choose-template.spec.js package (observed from repository paths and static analysis). |
| clean-context.js package | library | Observed | Groups 1 file(s) under clean-context.js package (observed from repository paths and static analysis). |
| clean-context.spec.js package | library | Observed | Groups 1 file(s) under clean-context.spec.js package (observed from repository paths and static analysis). |
| cli.js package | library | Observed | Groups 1 file(s) under cli.js package (observed from repository paths and static analysis). |
| cli.spec.js package | library | Observed | Groups 1 file(s) under cli.spec.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| project-infos.js package | library | Observed | Groups 1 file(s) under project-infos.js package (observed from repository paths and static analysis). |
| project-infos.spec.js package | library | Observed | Groups 1 file(s) under project-infos.spec.js package (observed from repository paths and static analysis). |
| questions package | library | Observed | Groups 44 file(s) under questions package (observed from repository paths and static analysis). |
| readme.js package | library | Observed | Groups 1 file(s) under readme.js package (observed from repository paths and static analysis). |
| readme.spec.js package | library | Observed | Groups 1 file(s) under readme.spec.js package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |
| utils.spec.js package | library | Observed | Groups 1 file(s) under utils.spec.js package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/nodejs.yml` (ci)
- `.vscode/settings.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 62 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 5 analysed file(s)
- `templates` — 3 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f0370c8efe602bfc1e1334ea556214de4c1b0f04` is the revision these paths and observations refer to.
