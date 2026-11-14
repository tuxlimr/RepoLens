# Project structure: lingui/js-lingui

**Analysed commit:** `bbaae0e8d3ea427f52970ab7d3891aecdac6aaad`

**Commit reference:** [bbaae0e8d3ea427f52970ab7d3891aecdac6aaad](https://github.com/lingui/js-lingui/commit/bbaae0e8d3ea427f52970ab7d3891aecdac6aaad)

**Tree at this commit:** [lingui/js-lingui@bbaae0e8d3ea](https://github.com/lingui/js-lingui/tree/bbaae0e8d3ea427f52970ab7d3891aecdac6aaad)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lingui/js-lingui |
| Description | 🌍 📖 A readable, automated, and optimized (2 kb) internationalization for JavaScript |
| Stars | 5937 |
| Forks | 477 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `bbaae0e8d3ea427f52970ab7d3891aecdac6aaad` |
| Retrieved at | 2026-11-14T19:14:11.745810+00:00 |
| Files in this snapshot | 791 |

## Directory tree

```text
.github/  (19 files)
  ISSUE_TEMPLATE/  (4 files)
    01_bug_report.yml
    02_feature_request.yml
    03_documentation.yml
    config.yml
  verdaccio/  (2 files)
    .yarnrc.yml
    config.yaml
  workflows/  (10 files)
    docs-suite.yml
    lint-pr-title.yml
    main-suite.yml
    next-sync.yml
    reindex-docs.yml
    release-test.yml
    release.yml
    size-limit.yml
    update-cldr-data.yml
    version-bump.yml
  PULL_REQUEST_TEMPLATE.md
  codecov.yml
  dependabot.yml
.husky/  (1 files)
  pre-commit
examples/  (262 files)
  js/  (10 files)
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    lingui.config.js
    package.json
    vite.config.js
  nextjs-babel/  (22 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (13 files)
      … 13 files under this directory
    .babelrc
    .gitignore
    .yarnrc.yml
    README.md
    lingui.config.ts
    next.config.ts
    package.json
    tsconfig.json
  nextjs-swc/  (24 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (15 files)
      … 15 files under this directory
    .gitignore
    .prettierrc.js
    .yarnrc.yml
    README.md
    lingui.config.ts
    next.config.ts
    package.json
    tsconfig.json
  react-native/  (18 files)
    src/  (6 files)
      … 6 files under this directory
    .eslintrc.js
    .gitignore
    .prettierrc
    .yarnrc.yml
    App.tsx
    README.md
    app.json
    babel.config.js
    lingui.config.js
    metro.config.js
    package.json
    tsconfig.json
  react-webpack-gettext/  (16 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (8 files)
      … 8 files under this directory
    .babelrc
    .gitignore
    README.md
    lingui.config.js
    package.json
    tsconfig.json
    webpack.config.js
  remix-vite-babel/  (18 files)
    app/  (11 files)
      … 11 files under this directory
    .eslintrc.cjs
    .gitignore
    README.md
    lingui.config.ts
    package.json
    tsconfig.json
    vite.config.ts
  rspack/  (18 files)
    src/  (10 files)
      … 10 files under this directory
    .gitignore
    LICENSE
    README.md
    index.html
    lingui.config.ts
    package.json
    rspack.config.js
    tsconfig.json
  tanstack-start/  (50 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (42 files)
      … 42 files under this directory
    .gitignore
    .prettierignore
    README.md
    lingui.config.ts
    package.json
    tsconfig.json
    vite.config.ts
  vite-project-react-babel/  (22 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (13 files)
      … 13 files under this directory
    .gitignore
    .prettierrc.json
    index.html
    lingui.config.ts
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  vite-project-react-swc/  (19 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (10 files)
      … 10 files under this directory
    .gitignore
    README.md
    index.html
    lingui.config.ts
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  vite-project-solid/  (22 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (13 files)
      … 13 files under this directory
    .gitignore
    .prettierrc.json
    index.html
    lingui.config.ts
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  vite-project-vue/  (23 files)
    public/  (1 files)
      … 1 files under this directory
    src/  (14 files)
      … 14 files under this directory
    .gitignore
    .prettierrc.json
    index.html
    lingui.config.ts
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
packages/  (495 files)
  babel-plugin-extract-messages/  (19 files)
    src/  (1 files)
      … 1 files under this directory
    test/  (12 files)
      … 12 files under this directory
    CHANGELOG.md
    README.md
    build.config.ts
    package.json
    tsconfig.json
    vitest.config.ts
  babel-plugin-lingui-macro/  (59 files)
    .vitest/  (1 files)
      … 1 files under this directory
    src/  (17 files)
      … 17 files under this directory
    test/  (36 files)
      … 36 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    vitest.config.ts
  cli/  (224 files)
    .vitest/  (2 files)
      … 2 files under this directory
    src/  (136 files)
      … 136 files under this directory
    test/  (78 files)
      … 78 files under this directory
    .gitignore
    CHANGELOG.md
    README.md
    api.ts
    package.json
    tsconfig.build.json
    tsconfig.json
    vitest.config.ts
  conf/  (31 files)
    __typetests__/  (2 files)
      … 2 files under this directory
    src/  (24 files)
      … 24 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    vitest.config.ts
  core/  (32 files)
    __typetests__/  (6 files)
      … 6 files under this directory
    macro/  (6 files)
      … 6 files under this directory
    src/  (15 files)
      … 15 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    vitest.config.ts
  detect-locale/  (26 files)
    src/  (21 files)
      … 21 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    vitest.config.ts
  extractor-vue/  (18 files)
    src/  (13 files)
      … 13 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    vitest.config.ts
  format-csv/  (11 files)
    __typetests__/  (2 files)
      … 2 files under this directory
    src/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    vitest.config.ts
  format-json/  (11 files)
    __typetests__/  (2 files)
      … 2 files under this directory
    src/  (4 files)
      … 4 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    vitest.config.ts
  format-po/  (14 files)
    __typetests__/  (2 files)
      … 2 files under this directory
    src/  (7 files)
      … 7 files under this directory
    CHANGELOG.md
    README.md
    package.json
    tsconfig.json
    vitest.config.ts
  format-po-gettext/  (20 files)
    __typetests__/  (2 files)
      … 2 files under this directory
    src/  (12 files)
      … 12 files under this directory
    CHANGELOG.md
    README.md
    gettext-plurals.json
    package.json
    tsconfig.json
    vitest.config.ts
  loader/  (30 files)
    src/  (2 files)
      … 2 files under this directory
    test/  (25 files)
      … 25 files under this directory
    CHANGELOG.md
    README.md
    package.json
.gitignore
.nvmrc
.prettierignore
.prettierrc.json
.yarnrc.yml
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
context7.json
eslint.config.js
lerna.json
package.json
```

## Entry points

- [examples/react-webpack-gettext/src/index.tsx](https://github.com/lingui/js-lingui/blob/bbaae0e8d3ea427f52970ab7d3891aecdac6aaad/examples/react-webpack-gettext/src/index.tsx)
- [packages/babel-plugin-extract-messages/src/index.ts](https://github.com/lingui/js-lingui/blob/bbaae0e8d3ea427f52970ab7d3891aecdac6aaad/packages/babel-plugin-extract-messages/src/index.ts)
- [packages/babel-plugin-lingui-macro/src/index.ts](https://github.com/lingui/js-lingui/blob/bbaae0e8d3ea427f52970ab7d3891aecdac6aaad/packages/babel-plugin-lingui-macro/src/index.ts)
- [packages/cli/src/index.ts](https://github.com/lingui/js-lingui/blob/bbaae0e8d3ea427f52970ab7d3891aecdac6aaad/packages/cli/src/index.ts)
- [packages/conf/src/index.ts](https://github.com/lingui/js-lingui/blob/bbaae0e8d3ea427f52970ab7d3891aecdac6aaad/packages/conf/src/index.ts)
- [packages/core/src/index.ts](https://github.com/lingui/js-lingui/blob/bbaae0e8d3ea427f52970ab7d3891aecdac6aaad/packages/core/src/index.ts)
- [packages/detect-locale/src/index.ts](https://github.com/lingui/js-lingui/blob/bbaae0e8d3ea427f52970ab7d3891aecdac6aaad/packages/detect-locale/src/index.ts)
- [packages/extractor-vue/src/index.ts](https://github.com/lingui/js-lingui/blob/bbaae0e8d3ea427f52970ab7d3891aecdac6aaad/packages/extractor-vue/src/index.ts)
- [packages/loader/src/index.ts](https://github.com/lingui/js-lingui/blob/bbaae0e8d3ea427f52970ab7d3891aecdac6aaad/packages/loader/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 75 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 59 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 122 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 29 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 158 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/01_bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/02_feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/03_documentation.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/codecov.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/verdaccio/.yarnrc.yml` (config)
- `.github/verdaccio/config.yaml` (config)
- `.github/workflows/docs-suite.yml` (ci)
- `.github/workflows/lint-pr-title.yml` (ci)
- `.github/workflows/main-suite.yml` (ci)
- `.github/workflows/next-sync.yml` (ci)
- `.github/workflows/reindex-docs.yml` (ci)
- `.github/workflows/release-test.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/size-limit.yml` (ci)
- `.github/workflows/update-cldr-data.yml` (ci)
- `.github/workflows/version-bump.yml` (ci)
- `.prettierrc.json` (config)
- `.yarnrc.yml` (config)
- `context7.json` (config)
- `examples/js/package.json` (manifest)
- `examples/nextjs-babel/.yarnrc.yml` (config)
- `examples/nextjs-babel/package.json` (manifest)
- `examples/nextjs-babel/tsconfig.json` (config)
- `examples/nextjs-swc/.yarnrc.yml` (config)
- `examples/nextjs-swc/package.json` (manifest)
- `examples/nextjs-swc/tsconfig.json` (config)
- `examples/react-native/.yarnrc.yml` (config)
- `examples/react-native/app.json` (config)
- `examples/react-native/package.json` (manifest)
- `examples/react-native/tsconfig.json` (config)
- `examples/react-webpack-gettext/package.json` (manifest)
- `examples/react-webpack-gettext/src/locales/cs.json` (config)
- `examples/react-webpack-gettext/src/locales/en.json` (config)
- `examples/react-webpack-gettext/tsconfig.json` (config)
- `examples/remix-vite-babel/package.json` (manifest)
- `examples/remix-vite-babel/tsconfig.json` (config)
- `examples/rspack/package.json` (manifest)
- `examples/rspack/tsconfig.json` (config)
- `examples/tanstack-start/package.json` (manifest)
- `examples/tanstack-start/tsconfig.json` (config)
- `examples/vite-project-react-babel/.prettierrc.json` (config)
- `examples/vite-project-react-babel/package.json` (manifest)
- `examples/vite-project-react-babel/tsconfig.json` (config)
- `examples/vite-project-react-babel/tsconfig.node.json` (config)
- `examples/vite-project-react-swc/package.json` (manifest)
- `examples/vite-project-react-swc/tsconfig.json` (config)
- `examples/vite-project-react-swc/tsconfig.node.json` (config)
- `examples/vite-project-solid/.prettierrc.json` (config)
- `examples/vite-project-solid/package.json` (manifest)
- `examples/vite-project-solid/tsconfig.json` (config)
- `examples/vite-project-solid/tsconfig.node.json` (config)
- `examples/vite-project-vue/.prettierrc.json` (config)
- `examples/vite-project-vue/package.json` (manifest)
- `examples/vite-project-vue/tsconfig.json` (config)
- `examples/vite-project-vue/tsconfig.node.json` (config)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/babel-plugin-extract-messages/package.json` (manifest)
- `packages/babel-plugin-extract-messages/tsconfig.json` (config)
- `packages/babel-plugin-lingui-macro/package.json` (manifest)
- `packages/babel-plugin-lingui-macro/tsconfig.json` (config)
- `packages/cli/package.json` (manifest)
- `packages/cli/tsconfig.build.json` (config)
- `packages/cli/tsconfig.json` (config)
- `packages/conf/__typetests__/tsconfig.json` (config)
- `packages/conf/package.json` (manifest)
- `packages/conf/src/fixtures/valid/package.json` (manifest)
- `packages/conf/tsconfig.json` (config)
- `packages/core/__typetests__/tsconfig.json` (config)
- `packages/core/__typetests__/typed-ids/tsconfig.json` (config)
- `packages/core/macro/__typetests__/tsconfig.json` (config)
- `packages/core/package.json` (manifest)
- `packages/core/tsconfig.json` (config)
- `packages/detect-locale/package.json` (manifest)
- `packages/detect-locale/tsconfig.json` (config)
- `packages/extractor-vue/package.json` (manifest)
- `packages/extractor-vue/tsconfig.json` (config)
- `packages/format-csv/__typetests__/tsconfig.json` (config)
- `packages/format-csv/package.json` (manifest)
- `packages/format-csv/tsconfig.json` (config)
- `packages/format-json/__typetests__/tsconfig.json` (config)
- `packages/format-json/package.json` (manifest)
- `packages/format-json/src/fixtures/messages.json` (config)
- `packages/format-json/tsconfig.json` (config)
- `packages/format-po-gettext/__typetests__/tsconfig.json` (config)
- `packages/format-po-gettext/gettext-plurals.json` (config)
- `packages/format-po-gettext/package.json` (manifest)
- `packages/format-po-gettext/tsconfig.json` (config)
- `packages/format-po/__typetests__/tsconfig.json` (config)
- `packages/format-po/package.json` (manifest)
- `packages/format-po/tsconfig.json` (config)
- `packages/loader/package.json` (manifest)

## Top-level layout

- `packages` — 495 analysed file(s)
- `examples` — 262 analysed file(s)
- `.github` — 19 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 9 file(s) were skipped during inventory (9 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `bbaae0e8d3ea427f52970ab7d3891aecdac6aaad` is the revision these paths and observations refer to.
