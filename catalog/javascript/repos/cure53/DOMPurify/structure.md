# Project structure: cure53/DOMPurify

**Analysed commit:** `027a09f844af3bdc7b5d21f9a97b69635b7c2dfc`

**Commit reference:** [027a09f844af3bdc7b5d21f9a97b69635b7c2dfc](https://github.com/cure53/DOMPurify/commit/027a09f844af3bdc7b5d21f9a97b69635b7c2dfc)

**Tree at this commit:** [cure53/DOMPurify@027a09f844af](https://github.com/cure53/DOMPurify/tree/027a09f844af3bdc7b5d21f9a97b69635b7c2dfc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | cure53/DOMPurify |
| Description | DOMPurify - a DOM-only, super-fast, uber-tolerant XSS sanitizer for HTML, MathML and SVG. DOMPurify works with a secure default, but offers a lot of configurability and hooks. Demo: |
| Stars | 17531 |
| Forks | 906 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `027a09f844af3bdc7b5d21f9a97b69635b7c2dfc` |
| Retrieved at | 2026-11-14T19:11:26.626680+00:00 |
| Files in this snapshot | 104 |

## Directory tree

```text
.github/  (13 files)
  workflows/  (9 files)
    build-and-test-skip.yml
    build-and-test.yml
    codeql-analysis.yml
    dependency-review.yml
    fuzz.yml
    legacy-browsers.yml
    scorecard.yml
    sign-release.yml
    slsa-provenance.yml
  FUNDING.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
.husky/  (1 files)
  pre-commit
config/  (4 files)
  playwright.config.js
  rolldown.config.js
  rolldown.coverage.config.js
  tsconfig.json
demos/  (16 files)
  README.md
  advanced-config-demo.html
  basic-demo.html
  config-demo.html
  hooks-demo.html
  hooks-link-proxy-demo.html
  hooks-mentaljs-demo.html
  hooks-node-removal-demo.html
  hooks-node-removal2-demo.html
  hooks-proxy-demo.html
  hooks-removal-demo.html
  hooks-sanitize-css-demo.html
  hooks-scheme-allowlist.html
  hooks-svg-demo.html
  hooks-target-blank-demo.html
  trusted-types-demo.html
scripts/  (3 files)
  benchmark.js
  commit-amend-build.sh
  fix-types.js
src/  (8 files)
  attrs.ts
  config.ts
  license_header
  purify.ts
  regexp.ts
  tags.ts
  types.ts
  utils.ts
test/  (18 files)
  browser/  (5 files)
    entry.js
    index.html
    index.min.html
    legacy-runner.js
    server.js
  config/  (1 files)
    setup.js
  fixtures/  (1 files)
    expect.mjs
  fuzz/  (1 files)
    sanitize.fast-check.js
  legacy-playwright/  (2 files)
    osv-scanner.toml
    package.json
  bootstrap-test-suite.js
  browser.spec.js
  happydom-node-runner.js
  happydom-node.js
  jsdom-node-runner.js
  jsdom-node.js
  purify-edge-node-runner.js
  purify-edge-node.js
typescript/  (24 files)
  commonjs/  (2 files)
    index.ts
    tsconfig.json
  commonjs-typescript-4.4/  (3 files)
    index.ts
    package.json
    tsconfig.json
  commonjs-with-no-types/  (3 files)
    types/  (1 files)
      … 1 files under this directory
    index.ts
    tsconfig.json
  commonjs-with-specific-types/  (2 files)
    index.ts
    tsconfig.json
  esm/  (3 files)
    index.ts
    package.json
    tsconfig.json
  esm-with-no-types/  (4 files)
    types/  (1 files)
      … 1 files under this directory
    index.ts
    package.json
    tsconfig.json
  esm-with-specific-types/  (3 files)
    index.ts
    package.json
    tsconfig.json
  nodenext/  (2 files)
    index.ts
    tsconfig.json
  package.json
  verify.js
website/  (1 files)
  index.html
.babelrc
.editorconfig
.gitattributes
.gitignore
.nvmrc
.prettierrc
CODEOWNERS
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
LICENSE-MPL
README.md
SECURITY.md
git
osv-scanner.toml
package.json
```

## Entry points

- [typescript/commonjs-typescript-4.4/index.ts](https://github.com/cure53/DOMPurify/blob/027a09f844af3bdc7b5d21f9a97b69635b7c2dfc/typescript/commonjs-typescript-4.4/index.ts)
- [typescript/commonjs-with-no-types/index.ts](https://github.com/cure53/DOMPurify/blob/027a09f844af3bdc7b5d21f9a97b69635b7c2dfc/typescript/commonjs-with-no-types/index.ts)
- [typescript/commonjs-with-specific-types/index.ts](https://github.com/cure53/DOMPurify/blob/027a09f844af3bdc7b5d21f9a97b69635b7c2dfc/typescript/commonjs-with-specific-types/index.ts)
- [typescript/commonjs/index.ts](https://github.com/cure53/DOMPurify/blob/027a09f844af3bdc7b5d21f9a97b69635b7c2dfc/typescript/commonjs/index.ts)
- [typescript/esm-with-no-types/index.ts](https://github.com/cure53/DOMPurify/blob/027a09f844af3bdc7b5d21f9a97b69635b7c2dfc/typescript/esm-with-no-types/index.ts)
- [typescript/esm-with-specific-types/index.ts](https://github.com/cure53/DOMPurify/blob/027a09f844af3bdc7b5d21f9a97b69635b7c2dfc/typescript/esm-with-specific-types/index.ts)
- [typescript/esm/index.ts](https://github.com/cure53/DOMPurify/blob/027a09f844af3bdc7b5d21f9a97b69635b7c2dfc/typescript/esm/index.ts)
- [typescript/nodenext/index.ts](https://github.com/cure53/DOMPurify/blob/027a09f844af3bdc7b5d21f9a97b69635b7c2dfc/typescript/nodenext/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| attrs.ts package | library | Observed | Groups 1 file(s) under attrs.ts package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 19 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.ts package | library | Observed | Groups 1 file(s) under config.ts package (observed from repository paths and static analysis). |
| purify.ts package | library | Observed | Groups 1 file(s) under purify.ts package (observed from repository paths and static analysis). |
| regexp.ts package | library | Observed | Groups 1 file(s) under regexp.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| tags.ts package | library | Observed | Groups 1 file(s) under tags.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 18 file(s) under tests (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| typescript package | library | Observed | Groups 9 file(s) under typescript package (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/build-and-test-skip.yml` (ci)
- `.github/workflows/build-and-test.yml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/dependency-review.yml` (ci)
- `.github/workflows/fuzz.yml` (ci)
- `.github/workflows/legacy-browsers.yml` (ci)
- `.github/workflows/scorecard.yml` (ci)
- `.github/workflows/sign-release.yml` (ci)
- `.github/workflows/slsa-provenance.yml` (ci)
- `config/tsconfig.json` (config)
- `osv-scanner.toml` (config)
- `package.json` (manifest)
- `typescript/commonjs-typescript-4.4/package.json` (manifest)
- `typescript/commonjs-typescript-4.4/tsconfig.json` (config)
- `typescript/commonjs-with-no-types/tsconfig.json` (config)
- `typescript/commonjs-with-specific-types/tsconfig.json` (config)
- `typescript/commonjs/tsconfig.json` (config)
- `typescript/esm-with-no-types/package.json` (manifest)
- `typescript/esm-with-no-types/tsconfig.json` (config)
- `typescript/esm-with-specific-types/package.json` (manifest)
- `typescript/esm-with-specific-types/tsconfig.json` (config)
- `typescript/esm/package.json` (manifest)
- `typescript/esm/tsconfig.json` (config)
- `typescript/nodenext/tsconfig.json` (config)
- `typescript/package.json` (manifest)

## Top-level layout

- `typescript` — 24 analysed file(s)
- `test` — 18 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `demos` — 16 analysed file(s)
- `.github` — 13 analysed file(s)
- `src` — 8 analysed file(s)
- `config` — 4 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.husky` — 1 analysed file(s)
- `website` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (1 x lockfile excluded; 5 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `027a09f844af3bdc7b5d21f9a97b69635b7c2dfc` is the revision these paths and observations refer to.
