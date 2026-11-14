# Project structure: react-cosmos/react-cosmos

**Analysed commit:** `6ef55459bdbb6b3f70868581679eed678259af00`

**Commit reference:** [6ef55459bdbb6b3f70868581679eed678259af00](https://github.com/react-cosmos/react-cosmos/commit/6ef55459bdbb6b3f70868581679eed678259af00)

**Tree at this commit:** [react-cosmos/react-cosmos@6ef55459bdbb](https://github.com/react-cosmos/react-cosmos/tree/6ef55459bdbb6b3f70868581679eed678259af00)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | react-cosmos/react-cosmos |
| Description | Sandbox for developing and testing UI components in isolation |
| Stars | 8697 |
| Forks | 382 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `6ef55459bdbb6b3f70868581679eed678259af00` |
| Retrieved at | 2026-11-14T19:13:40.342282+00:00 |
| Files in this snapshot | 798 |

## Directory tree

```text
.agents/  (3 files)
  skills/  (3 files)
    gh-release-notes/  (1 files)
      … 1 files under this directory
    review-dep-upgrade/  (2 files)
      … 2 files under this directory
.github/  (11 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (4 files)
    docs.yml
    release-canary.yml
    test-pnp.yml
    test.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  FUNDING.yml
  SECURITY.md
  pull_request_template.md
docs/  (94 files)
  components/  (34 files)
    svg/  (14 files)
      … 14 files under this directory
    Benefits.module.css
    Benefits.tsx
    ConfigTable.mdx
    Features.module.css
    Features.tsx
    Footer.module.css
    Footer.tsx
    Homepage.module.css
    Homepage.tsx
    HomepageHero.module.css
    HomepageHero.tsx
    HomepageLogos.module.css
    HomepageLogos.tsx
    Logo.module.css
    Logo.tsx
    NavbarWrapper.tsx
    OgImage.module.css
    OgImage.tsx
    Rocket.module.css
    Rocket.tsx
  images/  (2 files)
    hero/  (2 files)
      … 2 files under this directory
  pages/  (43 files)
    docs/  (38 files)
      … 38 files under this directory
    _app.mdx
    _meta.json
    about.mdx
    index.mdx
    og-image.mdx
  utils/  (4 files)
    flattenConfigSchema.ts
    getStargazersCount.ts
    useStargazersCount.ts
    useViewportEnter.ts
  .gitignore
  next-env.d.ts
  next.config.js
  package.json
  postcss.config.cjs
  styles.css
  styles.d.ts
  svgs.d.ts
  tailwind.config.js
  theme.config.jsx
  tsconfig.json
examples/  (55 files)
  shared/  (3 files)
    components/  (2 files)
      … 2 files under this directory
    package.json
  todo/  (19 files)
    src/  (14 files)
      … 14 files under this directory
    .gitignore
    cosmos.config.json
    index.html
    package.json
    vite.config.js
  vite/  (17 files)
    src/  (11 files)
      … 11 files under this directory
    static/  (1 files)
      … 1 files under this directory
    .gitignore
    cosmos.config.json
    index.html
    package.json
    vite.config.js
  webpack/  (16 files)
    src/  (10 files)
      … 10 files under this directory
    static/  (1 files)
      … 1 files under this directory
    .gitignore
    babel.config.js
    cosmos.config.json
    package.json
    webpack.override.js
packages/  (627 files)
  react-cosmos-core/  (73 files)
    src/  (70 files)
      … 70 files under this directory
    .npmignore
    package.json
    tsconfig.build.json
  react-cosmos-dom/  (15 files)
    src/  (12 files)
      … 12 files under this directory
    .npmignore
    package.json
    tsconfig.build.json
  react-cosmos-native/  (7 files)
    src/  (4 files)
      … 4 files under this directory
    .npmignore
    package.json
    tsconfig.build.json
  react-cosmos-next/  (10 files)
    src/  (7 files)
      … 7 files under this directory
    .npmignore
    package.json
    tsconfig.build.json
  react-cosmos-plugin-boolean-input/  (7 files)
    src/  (2 files)
      … 2 files under this directory
    .npmignore
    cosmos.plugin.json
    package.json
    tsconfig.build.json
    webpack.config.js
  react-cosmos-plugin-open-fixture/  (9 files)
    src/  (4 files)
      … 4 files under this directory
    .npmignore
    cosmos.plugin.json
    package.json
    tsconfig.build.json
    webpack.config.js
  react-cosmos-plugin-vite/  (24 files)
    src/  (19 files)
      … 19 files under this directory
    .npmignore
    cosmos.plugin.json
    dom.js
    package.json
    tsconfig.build.json
  react-cosmos-plugin-webpack/  (44 files)
    src/  (39 files)
      … 39 files under this directory
    .npmignore
    cosmos.plugin.json
    package.json
    tsconfig.build.client.json
    tsconfig.build.server.json
  react-cosmos-renderer/  (121 files)
    src/  (114 files)
      … 114 files under this directory
    .npmignore
    client.d.ts
    client.js
    index.d.ts
    index.js
    package.json
    tsconfig.build.json
  react-cosmos-ui/  (317 files)
    src/  (312 files)
      … 312 files under this directory
    .npmignore
    cosmos.config.json
    package.json
    pluginMocks.d.ts
    pluginMocks.js
.codecov.yml
.gitignore
.oxfmtrc.json
.oxlintrc.json
AGENTS.md
LICENSE
lerna.json
package.json
```

## Entry points

- [packages/react-cosmos-plugin-boolean-input/cosmos.plugin.json](https://github.com/react-cosmos/react-cosmos/blob/6ef55459bdbb6b3f70868581679eed678259af00/packages/react-cosmos-plugin-boolean-input/cosmos.plugin.json)
- [packages/react-cosmos-plugin-open-fixture/cosmos.plugin.json](https://github.com/react-cosmos/react-cosmos/blob/6ef55459bdbb6b3f70868581679eed678259af00/packages/react-cosmos-plugin-open-fixture/cosmos.plugin.json)
- [packages/react-cosmos-plugin-vite/cosmos.plugin.json](https://github.com/react-cosmos/react-cosmos/blob/6ef55459bdbb6b3f70868581679eed678259af00/packages/react-cosmos-plugin-vite/cosmos.plugin.json)
- [packages/react-cosmos-plugin-webpack/cosmos.plugin.json](https://github.com/react-cosmos/react-cosmos/blob/6ef55459bdbb6b3f70868581679eed678259af00/packages/react-cosmos-plugin-webpack/cosmos.plugin.json)
- [packages/react-cosmos-core/src/index.ts](https://github.com/react-cosmos/react-cosmos/blob/6ef55459bdbb6b3f70868581679eed678259af00/packages/react-cosmos-core/src/index.ts)
- [packages/react-cosmos-dom/src/index.ts](https://github.com/react-cosmos/react-cosmos/blob/6ef55459bdbb6b3f70868581679eed678259af00/packages/react-cosmos-dom/src/index.ts)
- [packages/react-cosmos-native/src/index.ts](https://github.com/react-cosmos/react-cosmos/blob/6ef55459bdbb6b3f70868581679eed678259af00/packages/react-cosmos-native/src/index.ts)
- [packages/react-cosmos-next/src/index.ts](https://github.com/react-cosmos/react-cosmos/blob/6ef55459bdbb6b3f70868581679eed678259af00/packages/react-cosmos-next/src/index.ts)
- [packages/react-cosmos-plugin-boolean-input/src/index.tsx](https://github.com/react-cosmos/react-cosmos/blob/6ef55459bdbb6b3f70868581679eed678259af00/packages/react-cosmos-plugin-boolean-input/src/index.tsx)
- [packages/react-cosmos-plugin-open-fixture/src/index.tsx](https://github.com/react-cosmos/react-cosmos/blob/6ef55459bdbb6b3f70868581679eed678259af00/packages/react-cosmos-plugin-open-fixture/src/index.tsx)
- [packages/react-cosmos-renderer/index.js](https://github.com/react-cosmos/react-cosmos/blob/6ef55459bdbb6b3f70868581679eed678259af00/packages/react-cosmos-renderer/index.js)
- [packages/react-cosmos-renderer/src/index.ts](https://github.com/react-cosmos/react-cosmos/blob/6ef55459bdbb6b3f70868581679eed678259af00/packages/react-cosmos-renderer/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 27 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 6 file(s) under external integrations (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 318 file(s) under packages package (observed from repository paths and static analysis). |

## Important files

- `.codecov.yml` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/release-canary.yml` (ci)
- `.github/workflows/test-pnp.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.oxfmtrc.json` (config)
- `.oxlintrc.json` (config)
- `docs/package.json` (manifest)
- `docs/pages/_meta.json` (config)
- `docs/pages/docs/_meta.json` (config)
- `docs/pages/docs/configuration/_meta.json` (config)
- `docs/pages/docs/dev/_meta.json` (config)
- `docs/pages/docs/fixtures/_meta.json` (config)
- `docs/pages/docs/getting-started/_meta.json` (config)
- `docs/pages/docs/plugins/_meta.json` (config)
- `docs/tsconfig.json` (config)
- `examples/shared/package.json` (manifest)
- `examples/todo/cosmos.config.json` (config)
- `examples/todo/package.json` (manifest)
- `examples/vite/cosmos.config.json` (config)
- `examples/vite/package.json` (manifest)
- `examples/webpack/cosmos.config.json` (config)
- `examples/webpack/package.json` (manifest)
- `lerna.json` (config)
- `package.json` (manifest)
- `packages/react-cosmos-core/package.json` (manifest)
- `packages/react-cosmos-core/tsconfig.build.json` (config)
- `packages/react-cosmos-dom/package.json` (manifest)
- `packages/react-cosmos-dom/tsconfig.build.json` (config)
- `packages/react-cosmos-native/package.json` (manifest)
- `packages/react-cosmos-native/tsconfig.build.json` (config)
- `packages/react-cosmos-next/package.json` (manifest)
- `packages/react-cosmos-next/tsconfig.build.json` (config)
- `packages/react-cosmos-plugin-boolean-input/cosmos.plugin.json` (config)
- `packages/react-cosmos-plugin-boolean-input/package.json` (manifest)
- `packages/react-cosmos-plugin-boolean-input/tsconfig.build.json` (config)
- `packages/react-cosmos-plugin-open-fixture/cosmos.plugin.json` (config)
- `packages/react-cosmos-plugin-open-fixture/package.json` (manifest)
- `packages/react-cosmos-plugin-open-fixture/tsconfig.build.json` (config)
- `packages/react-cosmos-plugin-vite/cosmos.plugin.json` (config)
- `packages/react-cosmos-plugin-vite/package.json` (manifest)
- `packages/react-cosmos-plugin-vite/tsconfig.build.json` (config)
- `packages/react-cosmos-plugin-webpack/cosmos.plugin.json` (config)
- `packages/react-cosmos-plugin-webpack/package.json` (manifest)
- `packages/react-cosmos-plugin-webpack/tsconfig.build.client.json` (config)
- `packages/react-cosmos-plugin-webpack/tsconfig.build.server.json` (config)
- `packages/react-cosmos-renderer/package.json` (manifest)
- `packages/react-cosmos-renderer/tsconfig.build.json` (config)
- `packages/react-cosmos-ui/cosmos.config.json` (config)
- `packages/react-cosmos-ui/package.json` (manifest)

## Top-level layout

- `packages` — 627 analysed file(s)
- `docs` — 94 analysed file(s)
- `examples` — 55 analysed file(s)
- `.github` — 11 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.agents` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6ef55459bdbb6b3f70868581679eed678259af00` is the revision these paths and observations refer to.
