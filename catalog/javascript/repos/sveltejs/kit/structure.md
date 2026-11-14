# Project structure: sveltejs/kit

**Analysed commit:** `089db3f6e460dbe16a1f32caa181ef6b2fa374b7`

**Commit reference:** [089db3f6e460dbe16a1f32caa181ef6b2fa374b7](https://github.com/sveltejs/kit/commit/089db3f6e460dbe16a1f32caa181ef6b2fa374b7)

**Tree at this commit:** [sveltejs/kit@089db3f6e460](https://github.com/sveltejs/kit/tree/089db3f6e460dbe16a1f32caa181ef6b2fa374b7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | sveltejs/kit |
| Description | web development, streamlined |
| Stars | 20913 |
| Forks | 2384 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `089db3f6e460dbe16a1f32caa181ef6b2fa374b7` |
| Retrieved at | 2026-11-14T19:11:11.664042+00:00 |
| Files in this snapshot | 794 |

## Directory tree

```text
.changeset/  (9 files)
  changelog.js
  config.json
  crawl-backslash-attribute.md
  hash-page-bytes.md
  node-sse-charset.md
  quote-digit-params.md
  skip-etag-with-nonce.md
  tidy-package-watch-output.md
  vercel-skew-bundle-strategies.md
.eslint/  (3 files)
  no-exports-to-runtime-imports.js
  no-runtime-to-exports-imports.js
  require-path-to-file-url.js
.githooks/  (1 files)
  pre-push
.github/  (13 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  actions/  (2 files)
    node-setup/  (1 files)
      … 1 files under this directory
    playwright-setup/  (1 files)
      … 1 files under this directory
  workflows/  (6 files)
    audit.yml
    autofix-lint.yml
    ci.yml
    platform-test.yml
    platform-tests-all.yml
    release.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
.vscode/  (1 files)
  settings.json
.well-known/  (1 files)
  funding-manifest-urls
documentation/  (88 files)
  docs/  (88 files)
    +assets/  (1 files)
      … 1 files under this directory
    10-getting-started/  (6 files)
      … 6 files under this directory
    20-core-concepts/  (8 files)
      … 8 files under this directory
    25-build-and-deploy/  (13 files)
      … 13 files under this directory
    30-advanced/  (11 files)
      … 11 files under this directory
    40-best-practices/  (7 files)
      … 7 files under this directory
    60-appendix/  (9 files)
      … 9 files under this directory
    98-reference/  (24 files)
      … 24 files under this directory
    99-legacy-reference/  (8 files)
      … 8 files under this directory
    index.md
packages/  (667 files)
  adapter-auto/  (10 files)
    test/  (2 files)
      … 2 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    adapters.js
    index.d.ts
    index.js
    package.json
    tsconfig.json
  adapter-bun/  (47 files)
    src/  (4 files)
      … 4 files under this directory
    test/  (32 files)
      … 32 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    ambient.d.ts
    index.d.ts
    index.js
    internal.d.ts
    package.json
    tsconfig.json
  adapter-cloudflare/  (45 files)
    files/  (3 files)
      … 3 files under this directory
    src/  (1 files)
      … 1 files under this directory
    test/  (31 files)
      … 31 files under this directory
    CHANGELOG.md
    README.md
    globals.d.ts
    index.d.ts
    index.js
    index.spec.js
    package.json
    tsconfig.json
    utils.js
    utils.spec.js
  adapter-netlify/  (91 files)
    files/  (3 files)
      … 3 files under this directory
    test/  (77 files)
      … 77 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    ambient.d.ts
    index.d.ts
    index.js
    package.json
    tsconfig.json
    utils.js
    utils.spec.js
    vitest.config.js
  adapter-node/  (59 files)
    src/  (9 files)
      … 9 files under this directory
    test/  (39 files)
      … 39 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    ambient.d.ts
    index.d.ts
    index.js
    internal.d.ts
    package.json
    tsconfig.json
    vitest.config.js
  adapter-static/  (41 files)
    test/  (32 files)
      … 32 files under this directory
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    index.d.ts
    index.js
    package.json
    platforms.js
    tsconfig.json
  adapter-vercel/  (67 files)
    files/  (2 files)
      … 2 files under this directory
    test/  (55 files)
      … 55 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    index.d.ts
    index.js
    internal.d.ts
    package.json
    tsconfig.json
    utils.js
    utils.spec.js
  enhanced-img/  (24 files)
    src/  (2 files)
      … 2 files under this directory
    test/  (15 files)
      … 15 files under this directory
    types/  (3 files)
      … 3 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
  kit/  (283 files)
    messages/  (40 files)
      … 40 files under this directory
    scripts/  (12 files)
      … 12 files under this directory
    src/  (227 files)
      … 227 files under this directory
    .gitignore
    CHANGELOG-pre-1.md
    README.md
    package.json
.editorconfig
.gitattributes
.gitignore
.oxfmtrc.json
AGENTS.md
CONTRIBUTING.md
FUNDING.json
LICENSE
README.md
eslint.config.js
package.json
```

## Entry points

- [packages/adapter-auto/index.js](https://github.com/sveltejs/kit/blob/089db3f6e460dbe16a1f32caa181ef6b2fa374b7/packages/adapter-auto/index.js)
- [packages/adapter-bun/index.js](https://github.com/sveltejs/kit/blob/089db3f6e460dbe16a1f32caa181ef6b2fa374b7/packages/adapter-bun/index.js)
- [packages/adapter-bun/src/index.js](https://github.com/sveltejs/kit/blob/089db3f6e460dbe16a1f32caa181ef6b2fa374b7/packages/adapter-bun/src/index.js)
- [packages/adapter-cloudflare/index.js](https://github.com/sveltejs/kit/blob/089db3f6e460dbe16a1f32caa181ef6b2fa374b7/packages/adapter-cloudflare/index.js)
- [packages/adapter-netlify/index.js](https://github.com/sveltejs/kit/blob/089db3f6e460dbe16a1f32caa181ef6b2fa374b7/packages/adapter-netlify/index.js)
- [packages/adapter-node/index.js](https://github.com/sveltejs/kit/blob/089db3f6e460dbe16a1f32caa181ef6b2fa374b7/packages/adapter-node/index.js)
- [packages/adapter-node/src/index.js](https://github.com/sveltejs/kit/blob/089db3f6e460dbe16a1f32caa181ef6b2fa374b7/packages/adapter-node/src/index.js)
- [packages/adapter-static/index.js](https://github.com/sveltejs/kit/blob/089db3f6e460dbe16a1f32caa181ef6b2fa374b7/packages/adapter-static/index.js)
- [packages/adapter-vercel/index.js](https://github.com/sveltejs/kit/blob/089db3f6e460dbe16a1f32caa181ef6b2fa374b7/packages/adapter-vercel/index.js)
- [packages/enhanced-img/src/index.js](https://github.com/sveltejs/kit/blob/089db3f6e460dbe16a1f32caa181ef6b2fa374b7/packages/enhanced-img/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 39 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 71 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 47 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 426 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/actions/node-setup/action.yml` (config)
- `.github/actions/playwright-setup/action.yml` (config)
- `.github/workflows/audit.yml` (ci)
- `.github/workflows/autofix-lint.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/platform-test.yml` (ci)
- `.github/workflows/platform-tests-all.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.oxfmtrc.json` (config)
- `.vscode/settings.json` (config)
- `FUNDING.json` (config)
- `documentation/docs/+assets/messages.json` (config)
- `package.json` (manifest)
- `packages/adapter-auto/package.json` (manifest)
- `packages/adapter-auto/tsconfig.json` (config)
- `packages/adapter-bun/package.json` (manifest)
- `packages/adapter-bun/tsconfig.json` (config)
- `packages/adapter-cloudflare/files/tsconfig.json` (config)
- `packages/adapter-cloudflare/package.json` (manifest)
- `packages/adapter-cloudflare/tsconfig.json` (config)
- `packages/adapter-netlify/files/tsconfig.json` (config)
- `packages/adapter-netlify/package.json` (manifest)
- `packages/adapter-netlify/tsconfig.json` (config)
- `packages/adapter-node/package.json` (manifest)
- `packages/adapter-node/tsconfig.json` (config)
- `packages/adapter-static/package.json` (manifest)
- `packages/adapter-static/tsconfig.json` (config)
- `packages/adapter-vercel/package.json` (manifest)
- `packages/adapter-vercel/tsconfig.json` (config)
- `packages/enhanced-img/package.json` (manifest)
- `packages/enhanced-img/tsconfig.json` (config)
- `packages/kit/package.json` (manifest)
- `packages/kit/src/core/postbuild/fixtures/backslash-in-attribute/output.json` (config)
- `packages/kit/src/core/postbuild/fixtures/base/output.json` (config)
- `packages/kit/src/core/postbuild/fixtures/basic-href/output.json` (config)
- `packages/kit/src/core/postbuild/fixtures/basic-src/output.json` (config)
- `packages/kit/src/core/postbuild/fixtures/basic-srcset/output.json` (config)
- `packages/kit/src/core/postbuild/fixtures/encoded-ids/output.json` (config)
- `packages/kit/src/core/postbuild/fixtures/href-with-character-reference/output.json` (config)
- `packages/kit/src/core/postbuild/fixtures/ids/output.json` (config)
- `packages/kit/src/core/postbuild/fixtures/include-rel-external/output.json` (config)
- `packages/kit/src/core/postbuild/fixtures/invalid-url/output.json` (config)
- `packages/kit/src/core/postbuild/fixtures/meta/output.json` (config)
- `packages/kit/src/core/postbuild/fixtures/unquoted-attributes/output.json` (config)
- `packages/kit/src/core/sync/write_tsconfig/test-app/package.json` (manifest)

## Top-level layout

- `packages` — 667 analysed file(s)
- `documentation` — 88 analysed file(s)
- `.github` — 13 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.changeset` — 9 analysed file(s)
- `.eslint` — 3 analysed file(s)
- `.githooks` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `.well-known` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (6 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `089db3f6e460dbe16a1f32caa181ef6b2fa374b7` is the revision these paths and observations refer to.
