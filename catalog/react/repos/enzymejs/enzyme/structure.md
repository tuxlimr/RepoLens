# Project structure: enzymejs/enzyme

**Analysed commit:** `61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0`

**Commit reference:** [61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0](https://github.com/enzymejs/enzyme/commit/61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0)

**Tree at this commit:** [enzymejs/enzyme@61e1b47c4bdc](https://github.com/enzymejs/enzyme/tree/61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | enzymejs/enzyme |
| Description | JavaScript Testing utilities for React |
| Stars | 19800 |
| Forks | 1959 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0` |
| Retrieved at | 2026-11-14T19:13:11.081594+00:00 |
| Files in this snapshot | 399 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    Bug_report.md
    Feature_request.md
  workflows/  (4 files)
    node-pretest.yml
    node.yml
    rebase.yml
    require-allow-edits.yml
  FUNDING.yml
docs/  (153 files)
  api/  (133 files)
    ReactWrapper/  (65 files)
      … 65 files under this directory
    ShallowWrapper/  (63 files)
      … 63 files under this directory
    README.md
    mount.md
    render.md
    selector.md
    shallow.md
  guides/  (11 files)
    browserify.md
    jest.md
    jsdom.md
    karma.md
    lab.md
    migration-from-2-to-3.md
    mocha.md
    react-native.md
    systemjs.md
    tape-ava.md
    webpack.md
  installation/  (5 files)
    README.md
    react-013.md
    react-014.md
    react-15.md
    react-16.md
  GLOSSARY.md
  common-issues.md
  future.md
  guides.md
packages/  (218 files)
  enzyme/  (23 files)
    src/  (14 files)
      … 14 files under this directory
    .babelrc
    .eslintrc
    ReactWrapper.js
    ShallowWrapper.js
    mount.js
    package.json
    render.js
    shallow.js
    withDom.js
  enzyme-adapter-react-13/  (7 files)
    src/  (4 files)
      … 4 files under this directory
    .babelrc
    .eslintrc
    package.json
  enzyme-adapter-react-14/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    .babelrc
    .eslintrc
    package.json
  enzyme-adapter-react-15/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    .babelrc
    .eslintrc
    package.json
  enzyme-adapter-react-15.4/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    .babelrc
    .eslintrc
    package.json
  enzyme-adapter-react-16/  (7 files)
    src/  (4 files)
      … 4 files under this directory
    .babelrc
    .eslintrc
    package.json
  enzyme-adapter-react-16.1/  (6 files)
    src/  (2 files)
      … 2 files under this directory
    .babelrc
    .eslintignore
    .eslintrc
    package.json
  enzyme-adapter-react-16.2/  (6 files)
    src/  (2 files)
      … 2 files under this directory
    .babelrc
    .eslintignore
    .eslintrc
    package.json
  enzyme-adapter-react-16.3/  (6 files)
    src/  (2 files)
      … 2 files under this directory
    .babelrc
    .eslintignore
    .eslintrc
    package.json
  enzyme-adapter-react-helper/  (8 files)
    src/  (5 files)
      … 5 files under this directory
    .babelrc
    .eslintrc
    package.json
  enzyme-adapter-utils/  (9 files)
    src/  (6 files)
      … 6 files under this directory
    .babelrc
    .eslintrc
    package.json
  enzyme-example-mocha/  (11 files)
    src/  (2 files)
      … 2 files under this directory
    test/  (2 files)
      … 2 files under this directory
    .babelrc
    .eslintrc
    .gitignore
    .nycrc
    LICENSE
    README.md
    package.json
  enzyme-shallow-equal/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    .babelrc
    .eslintrc
    README.md
    package.json
  enzyme-test-suite/  (115 files)
    test/  (112 files)
      … 112 files under this directory
    .babelrc
    .eslintrc
    package.json
test/  (1 files)
  mocha.opts
.babelrc
.eslintrc
.gitignore
.lgtm
.nycrc
CHANGELOG.md
CONTRIBUTING.md
INTHEWILD.md
LICENSE.md
MAINTAINERS
README.md
SUMMARY.md
book.json
env.js
install-relevant-react.sh
karma.conf.js
lerna.json
package.json
since.js
tea.yaml
```

## Entry points

- [packages/enzyme-adapter-react-13/src/index.js](https://github.com/enzymejs/enzyme/blob/61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0/packages/enzyme-adapter-react-13/src/index.js)
- [packages/enzyme-adapter-react-14/src/index.js](https://github.com/enzymejs/enzyme/blob/61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0/packages/enzyme-adapter-react-14/src/index.js)
- [packages/enzyme-adapter-react-15.4/src/index.js](https://github.com/enzymejs/enzyme/blob/61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0/packages/enzyme-adapter-react-15.4/src/index.js)
- [packages/enzyme-adapter-react-15/src/index.js](https://github.com/enzymejs/enzyme/blob/61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0/packages/enzyme-adapter-react-15/src/index.js)
- [packages/enzyme-adapter-react-16.1/src/index.js](https://github.com/enzymejs/enzyme/blob/61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0/packages/enzyme-adapter-react-16.1/src/index.js)
- [packages/enzyme-adapter-react-16.2/src/index.js](https://github.com/enzymejs/enzyme/blob/61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0/packages/enzyme-adapter-react-16.2/src/index.js)
- [packages/enzyme-adapter-react-16.3/src/index.js](https://github.com/enzymejs/enzyme/blob/61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0/packages/enzyme-adapter-react-16.3/src/index.js)
- [packages/enzyme-adapter-react-16/src/index.js](https://github.com/enzymejs/enzyme/blob/61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0/packages/enzyme-adapter-react-16/src/index.js)
- [packages/enzyme-adapter-react-helper/src/index.js](https://github.com/enzymejs/enzyme/blob/61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0/packages/enzyme-adapter-react-helper/src/index.js)
- [packages/enzyme-adapter-utils/src/index.js](https://github.com/enzymejs/enzyme/blob/61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0/packages/enzyme-adapter-utils/src/index.js)
- [packages/enzyme-shallow-equal/src/index.js](https://github.com/enzymejs/enzyme/blob/61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0/packages/enzyme-shallow-equal/src/index.js)
- [packages/enzyme/src/index.js](https://github.com/enzymejs/enzyme/blob/61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0/packages/enzyme/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 18 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 54 file(s) under packages package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 115 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/node-pretest.yml` (ci)
- `.github/workflows/node.yml` (ci)
- `.github/workflows/rebase.yml` (ci)
- `.github/workflows/require-allow-edits.yml` (ci)
- `book.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/enzyme-adapter-react-13/package.json` (manifest)
- `packages/enzyme-adapter-react-14/package.json` (manifest)
- `packages/enzyme-adapter-react-15.4/package.json` (manifest)
- `packages/enzyme-adapter-react-15/package.json` (manifest)
- `packages/enzyme-adapter-react-16.1/package.json` (manifest)
- `packages/enzyme-adapter-react-16.2/package.json` (manifest)
- `packages/enzyme-adapter-react-16.3/package.json` (manifest)
- `packages/enzyme-adapter-react-16/package.json` (manifest)
- `packages/enzyme-adapter-react-helper/package.json` (manifest)
- `packages/enzyme-adapter-utils/package.json` (manifest)
- `packages/enzyme-example-mocha/package.json` (manifest)
- `packages/enzyme-shallow-equal/package.json` (manifest)
- `packages/enzyme-test-suite/package.json` (manifest)
- `packages/enzyme/package.json` (manifest)
- `tea.yaml` (config)

## Top-level layout

- `packages` — 218 analysed file(s)
- `docs` — 153 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 7 analysed file(s)
- `test` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `61e1b47c4bdc4509b2ac286c0d3ae3df172d26f0` is the revision these paths and observations refer to.
