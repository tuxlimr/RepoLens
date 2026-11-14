# Project structure: BuilderIO/mitosis

**Analysed commit:** `2de76e9064d9e7916c5309c0a31206383403ae9d`

**Commit reference:** [2de76e9064d9e7916c5309c0a31206383403ae9d](https://github.com/BuilderIO/mitosis/commit/2de76e9064d9e7916c5309c0a31206383403ae9d)

**Tree at this commit:** [BuilderIO/mitosis@2de76e9064d9](https://github.com/BuilderIO/mitosis/tree/2de76e9064d9e7916c5309c0a31206383403ae9d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | BuilderIO/mitosis |
| Description | Write components once, run everywhere. Compiles to React, Vue, Qwik, Solid, Angular, Svelte, and more.  |
| Stars | 14464 |
| Forks | 677 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `2de76e9064d9e7916c5309c0a31206383403ae9d` |
| Retrieved at | 2026-11-14T19:13:17.456495+00:00 |
| Files in this snapshot | 786 |

## Directory tree

```text
.changeset/  (2 files)
  README.md
  config.json
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yaml
    feature_request.yaml
  actions/  (1 files)
    yarn-nm-install/  (1 files)
      … 1 files under this directory
  workflows/  (3 files)
    checks.yml
    crawl-docs-site.yml
    publish.yml
  pull_request_template.md
.vscode/  (2 files)
  extensions.json
  settings.json
.yarn/  (151 files)
  patches/  (1 files)
    @sveltejs-package-npm-1.0.0-next.1-2fd015530b.patch
  versions/  (150 files)
    026177fe.yml
    028828e2.yml
    06e5749f.yml
    0726b528.yml
    072aebc8.yml
    07c322cc.yml
    09d6af27.yml
    0a9221c4.yml
    0aafb6de.yml
    105b2055.yml
    12875928.yml
    1366a905.yml
    13ce8bab.yml
    144b1230.yml
    15c76034.yml
    173dde9b.yml
    1a44c65b.yml
    1aa27f56.yml
    1ccf07c6.yml
    1df68f61.yml
    1fad65fc.yml
    2199c3df.yml
    22e7ecc3.yml
    23758213.yml
    … 126 more files
developer/  (1 files)
  generators.md
docs/  (11 files)
  README.md
  cli.md
  components.md
  configuration.md
  context.md
  customizability.md
  feature-matrix-draft.md
  gotchas.md
  hooks.md
  project-structure.md
  test-status.md
e2e/  (140 files)
  e2e-alpine/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    README.md
    index.html
    package.json
    vite.config.ts
  e2e-angular/  (16 files)
    angular_src/  (9 files)
      … 9 files under this directory
    .browserslistrc
    .gitignore
    README.md
    angular.json
    package.json
    tsconfig.app.json
    tsconfig.json
  e2e-app/  (45 files)
    output/  (12 files)
      … 12 files under this directory
    src/  (20 files)
      … 20 files under this directory
    tests/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    allow-failures.json
    e2e-output.ts
    e2e.ts
    mitosis.config.cjs
    package.json
    playwright.config.ts
    project.json
    results.json
    tsconfig.json
    tsconfig.node.json
  e2e-qwikcity/  (25 files)
    .vscode/  (1 files)
      … 1 files under this directory
    public/  (3 files)
      … 3 files under this directory
    src/  (12 files)
      … 12 files under this directory
    .eslintignore
    .eslintrc.cjs
    .gitignore
    .prettierignore
    README.md
    package.json
    project.json
    tsconfig.json
    vite.config.ts
  e2e-react/  (11 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    project.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  e2e-solid/  (8 files)
    src/  (2 files)
      … 2 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  e2e-stencil/  (8 files)
    .editorconfig
    .gitignore
    .prettierrc.json
    LICENSE
    components.d.ts
    package.json
    stencil.config.ts
    tsconfig.json
  e2e-svelte/  (11 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    svelte.config.mjs
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
  e2e-vue3/  (11 files)
    src/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    index.html
    package.json
    tsconfig.json
    tsconfig.node.json
    vite.config.ts
examples/  (44 files)
  basic/  (23 files)
    overrides/  (5 files)
      … 5 files under this directory
    src/  (9 files)
      … 9 files under this directory
    .eslintignore
    .eslintrc.js
    .gitignore
    .prettierignore
    .prettierrc
    README.md
    mitosis.config.js
    package.json
    tsconfig.json
  metdata/  (10 files)
    src/  (4 files)
      … 4 files under this directory
    .eslintrc.js
    .gitignore
    README.md
    mitosis.config.js
    package.json
    tsconfig.json
  todo/  (11 files)
    src/  (5 files)
      … 5 files under this directory
    .eslintrc.js
    .gitignore
    README.md
    mitosis.config.js
    package.json
    tsconfig.json
packages/  (412 files)
  cli/  (27 files)
    bin/  (1 files)
      … 1 files under this directory
    docs/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    src/  (15 files)
      … 15 files under this directory
    .gitignore
    .yarnrc.yml
    CHANGELOG.md
    package.json
    readme.md
    tsconfig.build.json
    tsconfig.json
    vite.config.ts
  core/  (385 files)
    scripts/  (1 files)
      … 1 files under this directory
    src/  (379 files)
      … 379 files under this directory
    .yarnrc.yml
    CHANGELOG.md
    jsx-runtime.d.ts
    package.json
    project.json
.eslintignore
.eslintrc.js
.gitattributes
.gitguardian.yml
.gitignore
.nvmrc
.prettierignore
.prettierrc.js
.tool-versions
.yarnrc.yml
CODEOWNERS
CONTRIBUTING.md
LICENSE
README.MD
nx.json
package.json
```

## Entry points

- [packages/cli/bin/mitosis](https://github.com/BuilderIO/mitosis/blob/2de76e9064d9e7916c5309c0a31206383403ae9d/packages/cli/bin/mitosis)
- [e2e/e2e-alpine/src/main.ts](https://github.com/BuilderIO/mitosis/blob/2de76e9064d9e7916c5309c0a31206383403ae9d/e2e/e2e-alpine/src/main.ts)
- [e2e/e2e-angular/angular_src/main.ts](https://github.com/BuilderIO/mitosis/blob/2de76e9064d9e7916c5309c0a31206383403ae9d/e2e/e2e-angular/angular_src/main.ts)
- [e2e/e2e-app/src/index.ts](https://github.com/BuilderIO/mitosis/blob/2de76e9064d9e7916c5309c0a31206383403ae9d/e2e/e2e-app/src/index.ts)
- [e2e/e2e-react/src/App.tsx](https://github.com/BuilderIO/mitosis/blob/2de76e9064d9e7916c5309c0a31206383403ae9d/e2e/e2e-react/src/App.tsx)
- [e2e/e2e-react/src/main.tsx](https://github.com/BuilderIO/mitosis/blob/2de76e9064d9e7916c5309c0a31206383403ae9d/e2e/e2e-react/src/main.tsx)
- [e2e/e2e-solid/src/App.tsx](https://github.com/BuilderIO/mitosis/blob/2de76e9064d9e7916c5309c0a31206383403ae9d/e2e/e2e-solid/src/App.tsx)
- [e2e/e2e-solid/src/index.tsx](https://github.com/BuilderIO/mitosis/blob/2de76e9064d9e7916c5309c0a31206383403ae9d/e2e/e2e-solid/src/index.tsx)
- [e2e/e2e-svelte/src/main.ts](https://github.com/BuilderIO/mitosis/blob/2de76e9064d9e7916c5309c0a31206383403ae9d/e2e/e2e-svelte/src/main.ts)
- [e2e/e2e-vue3/src/main.ts](https://github.com/BuilderIO/mitosis/blob/2de76e9064d9e7916c5309c0a31206383403ae9d/e2e/e2e-vue3/src/main.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 3 file(s) under api layer (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 76 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 168 file(s) under data layer (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 61 file(s) under e2e package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 15 file(s) under packages package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 172 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.gitguardian.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yaml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yaml` (config)
- `.github/actions/yarn-nm-install/action.yml` (config)
- `.github/workflows/checks.yml` (ci)
- `.github/workflows/crawl-docs-site.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `.yarn/versions/026177fe.yml` (config)
- `.yarn/versions/028828e2.yml` (config)
- `.yarn/versions/06e5749f.yml` (config)
- `.yarn/versions/0726b528.yml` (config)
- `.yarn/versions/072aebc8.yml` (config)
- `.yarn/versions/07c322cc.yml` (config)
- `.yarn/versions/09d6af27.yml` (config)
- `.yarn/versions/0a9221c4.yml` (config)
- `.yarn/versions/0aafb6de.yml` (config)
- `.yarn/versions/105b2055.yml` (config)
- `.yarn/versions/12875928.yml` (config)
- `.yarn/versions/1366a905.yml` (config)
- `.yarn/versions/13ce8bab.yml` (config)
- `.yarn/versions/144b1230.yml` (config)
- `.yarn/versions/15c76034.yml` (config)
- `.yarn/versions/173dde9b.yml` (config)
- `.yarn/versions/1a44c65b.yml` (config)
- `.yarn/versions/1aa27f56.yml` (config)
- `.yarn/versions/1ccf07c6.yml` (config)
- `.yarn/versions/1df68f61.yml` (config)
- `.yarn/versions/1fad65fc.yml` (config)
- `.yarn/versions/2199c3df.yml` (config)
- `.yarn/versions/22e7ecc3.yml` (config)
- `.yarn/versions/23758213.yml` (config)
- `.yarn/versions/23da8025.yml` (config)
- `.yarn/versions/24584391.yml` (config)
- `.yarn/versions/25f00f22.yml` (config)
- `.yarn/versions/272ca396.yml` (config)
- `.yarn/versions/29fe0987.yml` (config)
- `.yarn/versions/2a247815.yml` (config)
- `.yarn/versions/2a5c447d.yml` (config)
- `.yarn/versions/2a69f5af.yml` (config)
- `.yarn/versions/2ceb5677.yml` (config)
- `.yarn/versions/2e8dddaa.yml` (config)
- `.yarn/versions/329ad4cc.yml` (config)
- `.yarn/versions/33308e54.yml` (config)
- `.yarn/versions/33caf697.yml` (config)
- `.yarn/versions/371922cb.yml` (config)
- `.yarn/versions/3777636b.yml` (config)
- `.yarn/versions/389436a2.yml` (config)
- `.yarn/versions/3a3f723c.yml` (config)
- `.yarn/versions/3b579a11.yml` (config)
- `.yarn/versions/3bb83c60.yml` (config)
- `.yarn/versions/3bff13d2.yml` (config)
- `.yarn/versions/3cb89724.yml` (config)
- `.yarn/versions/3ead9d18.yml` (config)
- `.yarn/versions/4053ebae.yml` (config)
- `.yarn/versions/411f782e.yml` (config)
- `.yarn/versions/42b588ef.yml` (config)
- `.yarn/versions/44068586.yml` (config)
- `.yarn/versions/46f8ffda.yml` (config)
- `.yarn/versions/47346a15.yml` (config)
- `.yarn/versions/4c1ff198.yml` (config)
- `.yarn/versions/4c9680f4.yml` (config)
- `.yarn/versions/4e3bceb6.yml` (config)
- `.yarn/versions/4f99b94c.yml` (config)
- `.yarn/versions/515392f0.yml` (config)
- `.yarn/versions/51d09e1d.yml` (config)
- `.yarn/versions/51fd1e43.yml` (config)
- `.yarn/versions/56419efb.yml` (config)
- `.yarn/versions/57f03ec9.yml` (config)
- `.yarn/versions/5a2242bb.yml` (config)
- `.yarn/versions/5bc0e0a1.yml` (config)
- `.yarn/versions/5d063d27.yml` (config)
- `.yarn/versions/5e0d43a5.yml` (config)
- `.yarn/versions/6157a043.yml` (config)
- `.yarn/versions/61b56588.yml` (config)
- `.yarn/versions/62c5b924.yml` (config)
- `.yarn/versions/63370d4e.yml` (config)
- `.yarn/versions/6629957d.yml` (config)
- `.yarn/versions/66376ce5.yml` (config)
- `.yarn/versions/6bc94a3b.yml` (config)
- `.yarn/versions/6f725cb4.yml` (config)
- `.yarn/versions/6fbd3750.yml` (config)
- `.yarn/versions/6ff24e83.yml` (config)
- `.yarn/versions/72b07268.yml` (config)
- `.yarn/versions/72ea0816.yml` (config)
- `.yarn/versions/735cc783.yml` (config)
- `.yarn/versions/73f711f2.yml` (config)
- `.yarn/versions/760e996e.yml` (config)
- `.yarn/versions/77fd690d.yml` (config)
- `.yarn/versions/7802d627.yml` (config)
- `.yarn/versions/78525628.yml` (config)
- `.yarn/versions/7970dbd4.yml` (config)
- `.yarn/versions/7a76f789.yml` (config)
- `.yarn/versions/7a985e40.yml` (config)
- `.yarn/versions/804757be.yml` (config)
- `.yarn/versions/81d9e719.yml` (config)
- `.yarn/versions/85f914ea.yml` (config)
- `.yarn/versions/88302145.yml` (config)
- `.yarn/versions/89184b6e.yml` (config)
- `.yarn/versions/8afacd42.yml` (config)
- `.yarn/versions/9288f7b9.yml` (config)
- `.yarn/versions/92f5ae87.yml` (config)
- `.yarn/versions/94fb767f.yml` (config)
- `.yarn/versions/9513e6ed.yml` (config)
- `.yarn/versions/9a0abe50.yml` (config)
- `.yarn/versions/a26ef46f.yml` (config)
- `.yarn/versions/a727eb3e.yml` (config)
- `.yarn/versions/a7426113.yml` (config)
- `.yarn/versions/a7d5432d.yml` (config)
- `.yarn/versions/ab01aaa4.yml` (config)
- `.yarn/versions/ac5e5b17.yml` (config)
- `.yarn/versions/aee7c6a5.yml` (config)
- `.yarn/versions/afee0844.yml` (config)
- `.yarn/versions/b2276c4b.yml` (config)
- `.yarn/versions/b2be75f1.yml` (config)
- `.yarn/versions/b918a4e2.yml` (config)
- `.yarn/versions/b9512246.yml` (config)
- `.yarn/versions/bf62388f.yml` (config)
- `.yarn/versions/bf6edf5d.yml` (config)
- `.yarn/versions/c0b2fa52.yml` (config)
- `.yarn/versions/c1093761.yml` (config)
- `.yarn/versions/c143ff23.yml` (config)
- `.yarn/versions/c21adc6a.yml` (config)
- `.yarn/versions/c281843c.yml` (config)
- `.yarn/versions/c2d75ce2.yml` (config)
- `.yarn/versions/c4fd8fbc.yml` (config)
- `.yarn/versions/c62b27f7.yml` (config)
- `.yarn/versions/c6e4f64b.yml` (config)
- `.yarn/versions/c7ca329d.yml` (config)
- `.yarn/versions/c9e3ca8b.yml` (config)
- `.yarn/versions/cb259f51.yml` (config)
- `.yarn/versions/cc461ac8.yml` (config)
- `.yarn/versions/cc9ed5cd.yml` (config)
- `.yarn/versions/cf48d14d.yml` (config)
- `.yarn/versions/cf4b5981.yml` (config)
- `.yarn/versions/cf7ae630.yml` (config)
- `.yarn/versions/d03a50ed.yml` (config)
- `.yarn/versions/db85d6c2.yml` (config)
- `.yarn/versions/e0705211.yml` (config)
- `.yarn/versions/e0755694.yml` (config)
- `.yarn/versions/e11beb4b.yml` (config)
- `.yarn/versions/e3ecba3b.yml` (config)
- `.yarn/versions/e4749842.yml` (config)
- `.yarn/versions/e5d3ce94.yml` (config)
- `.yarn/versions/e89e1791.yml` (config)
- `.yarn/versions/e9ce1193.yml` (config)
- `.yarn/versions/ec777010.yml` (config)
- `.yarn/versions/ed8e0a45.yml` (config)
- `.yarn/versions/edc58eba.yml` (config)
- `.yarn/versions/ef410112.yml` (config)
- `.yarn/versions/f1210054.yml` (config)
- `.yarn/versions/f34f5b8e.yml` (config)
- `.yarn/versions/f52489af.yml` (config)
- `.yarn/versions/f75f1951.yml` (config)
- `.yarn/versions/f8d96db9.yml` (config)
- `.yarn/versions/fb17c565.yml` (config)
- `.yarn/versions/fb202c06.yml` (config)
- `.yarn/versions/fb99b1b3.yml` (config)
- `.yarnrc.yml` (config)
- `e2e/e2e-alpine/package.json` (manifest)
- `e2e/e2e-angular/angular.json` (config)
- `e2e/e2e-angular/package.json` (manifest)
- `e2e/e2e-angular/tsconfig.app.json` (config)
- `e2e/e2e-angular/tsconfig.json` (config)
- `e2e/e2e-app/allow-failures.json` (config)
- `e2e/e2e-app/output/qwik/package.json` (manifest)
- `e2e/e2e-app/output/qwik/project.json` (config)
- `e2e/e2e-app/output/qwik/tsconfig.json` (config)
- `e2e/e2e-app/output/vue/package.json` (manifest)
- `e2e/e2e-app/output/vue/project.json` (config)
- `e2e/e2e-app/output/vue/tsconfig.config.json` (config)
- `e2e/e2e-app/output/vue/tsconfig.json` (config)
- `e2e/e2e-app/package.json` (manifest)
- `e2e/e2e-app/project.json` (config)
- `e2e/e2e-app/results.json` (config)
- `e2e/e2e-app/tsconfig.json` (config)
- `e2e/e2e-app/tsconfig.node.json` (config)
- `e2e/e2e-qwikcity/.vscode/extensions.json` (config)
- `e2e/e2e-qwikcity/package.json` (manifest)
- `e2e/e2e-qwikcity/project.json` (config)
- `e2e/e2e-qwikcity/public/manifest.json` (config)
- `e2e/e2e-qwikcity/tsconfig.json` (config)
- `e2e/e2e-react/package.json` (manifest)
- `e2e/e2e-react/project.json` (config)
- `e2e/e2e-react/tsconfig.json` (config)
- `e2e/e2e-react/tsconfig.node.json` (config)
- `e2e/e2e-solid/package.json` (manifest)
- `e2e/e2e-solid/tsconfig.json` (config)
- `e2e/e2e-stencil/.editorconfig` (config)
- `e2e/e2e-stencil/.prettierrc.json` (config)
- `e2e/e2e-stencil/package.json` (manifest)
- `e2e/e2e-stencil/tsconfig.json` (config)
- `e2e/e2e-svelte/package.json` (manifest)
- `e2e/e2e-svelte/tsconfig.json` (config)
- `e2e/e2e-svelte/tsconfig.node.json` (config)
- `e2e/e2e-vue3/package.json` (manifest)
- `e2e/e2e-vue3/tsconfig.json` (config)
- `e2e/e2e-vue3/tsconfig.node.json` (config)
- `examples/basic/package.json` (manifest)
- `examples/basic/tsconfig.json` (config)
- `examples/metdata/package.json` (manifest)
- `examples/metdata/tsconfig.json` (config)
- `examples/todo/package.json` (manifest)
- `examples/todo/tsconfig.json` (config)
- `nx.json` (config)
- `package.json` (manifest)
- `packages/cli/.yarnrc.yml` (config)
- `packages/cli/package.json` (manifest)
- `packages/cli/src/__tests__/compile/data/triptych.builder.json` (config)
- `packages/cli/tsconfig.build.json` (config)
- `packages/cli/tsconfig.json` (config)
- `packages/core/.yarnrc.yml` (config)
- `packages/core/package.json` (manifest)
- `packages/core/project.json` (config)
- `packages/core/src/__tests__/data/builder/boolean.json` (config)
- `packages/core/src/__tests__/data/builder/custom-component-slot-property.json` (config)
- `packages/core/src/__tests__/data/builder/custom-component-tags.json` (config)
- `packages/core/src/__tests__/data/builder/lazy-load-section.json` (config)
- `packages/core/src/__tests__/data/builder/localization.json` (config)
- `packages/core/src/__tests__/data/builder/slots.json` (config)
- `packages/core/src/__tests__/data/builder/slots2.json` (config)
- `packages/core/src/__tests__/data/builder/symbol-basic.json` (config)
- `packages/core/src/__tests__/data/builder/symbol-multiple.json` (config)
- `packages/core/src/__tests__/data/builder/symbol-with-inputs.json` (config)
- `packages/core/src/__tests__/data/builder/symbol-with-named-entry.json` (config)
- `packages/core/src/__tests__/data/builder/tag-name.json` (config)
- `packages/core/src/__tests__/data/builder/text-bindings.json` (config)
- `packages/core/src/__tests__/qwik/specs/qwik.test.accordion.json` (config)
- `packages/core/src/__tests__/qwik/specs/qwik.test.bindings.json` (config)
- `packages/core/src/__tests__/qwik/specs/qwik.test.button.json` (config)
- `packages/core/src/__tests__/qwik/specs/qwik.test.component-binding.json` (config)
- `packages/core/src/__tests__/qwik/specs/qwik.test.component-inputs.json` (config)
- `packages/core/src/__tests__/qwik/specs/qwik.test.for-loop.binding.json` (config)
- `packages/core/src/__tests__/qwik/specs/qwik.test.for-loop.json` (config)
- `packages/core/src/__tests__/qwik/specs/qwik.test.hello_world.json` (config)
- `packages/core/src/__tests__/qwik/specs/qwik.test.image.json` (config)
- `packages/core/src/__tests__/qwik/specs/qwik.test.mount.json` (config)
- `packages/core/src/__tests__/qwik/specs/qwik.test.page-with-symbol.json` (config)
- `packages/core/src/__tests__/qwik/specs/qwik.test.show-hide.json` (config)
- `packages/core/src/__tests__/qwik/specs/qwik.test.svg.json` (config)
- `packages/core/src/__tests__/tsconfig.json` (config)

## Top-level layout

- `packages` — 412 analysed file(s)
- `.yarn` — 151 analysed file(s)
- `e2e` — 140 analysed file(s)
- `examples` — 44 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `docs` — 11 analysed file(s)
- `.github` — 7 analysed file(s)
- `.changeset` — 2 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `developer` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 14 file(s) were skipped during inventory (3 x likely secret file excluded; 11 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2de76e9064d9e7916c5309c0a31206383403ae9d` is the revision these paths and observations refer to.
