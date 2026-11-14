# Project structure: gkurt/tegaki

**Analysed commit:** `bf18556996d9683326e8f2130bd50e7632e9f187`

**Commit reference:** [bf18556996d9683326e8f2130bd50e7632e9f187](https://github.com/gkurt/tegaki/commit/bf18556996d9683326e8f2130bd50e7632e9f187)

**Tree at this commit:** [gkurt/tegaki@bf18556996d9](https://github.com/gkurt/tegaki/tree/bf18556996d9683326e8f2130bd50e7632e9f187)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gkurt/tegaki |
| Description | Handwriting animation for the web. Supports any font or text. |
| Stars | 3307 |
| Forks | 127 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `bf18556996d9683326e8f2130bd50e7632e9f187` |
| Retrieved at | 2026-11-14T19:15:26.214782+00:00 |
| Files in this snapshot | 663 |

## Directory tree

```text
.agents/  (42 files)
  skills/  (42 files)
    padrone/  (3 files)
      … 3 files under this directory
    remotion-best-practices/  (39 files)
      … 39 files under this directory
.claude/  (2 files)
  launch.json
  settings.json
.github/  (8 files)
  workflows/  (7 files)
    ci.yml
    deploy-docs.yml
    release-smoke.yml
    release.yml
    scoreboard.yml
    tegami-pr-comment.yml
    tegami-pr.yml
  ISSUE_TEMPLATE.md
.husky/  (1 files)
  pre-commit
.tegami/  (1 files)
  publish-lock.yaml
.vscode/  (2 files)
  extensions.json
  settings.json
e2e/  (5 files)
  examples/  (5 files)
    check-remotion-still.ts
    check-wc-cdn.ts
    package.json
    playwright.config.ts
    smoke.e2e.ts
examples/  (106 files)
  astro/  (5 files)
    src/  (1 files)
      … 1 files under this directory
    .gitignore
    astro.config.ts
    package.json
    tsconfig.json
  editframe/  (11 files)
    src/  (6 files)
      … 6 files under this directory
    README.md
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  next/  (9 files)
    app/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    next.config.ts
    package.json
    tsconfig.json
  nuxt/  (6 files)
    pages/  (1 files)
      … 1 files under this directory
    .gitignore
    app.vue
    nuxt.config.ts
    package.json
    tsconfig.json
  remotion/  (39 files)
    scripts/  (4 files)
      … 4 files under this directory
    src/  (31 files)
      … 31 files under this directory
    .gitignore
    package.json
    remotion.config.ts
    tsconfig.json
  solid/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  svelte/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  vanilla/  (6 files)
    src/  (2 files)
      … 2 files under this directory
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  vite/  (8 files)
    src/  (3 files)
      … 3 files under this directory
    .gitignore
    index.html
    package.json
    tsconfig.json
    vite.config.ts
  vue/  (8 files)
    src/  (4 files)
      … 4 files under this directory
    index.html
    package.json
    tsconfig.json
    vite.config.ts
media/  (2 files)
  hello-world.svg
  tegaki.svg
packages/  (472 files)
  generator/  (133 files)
    scripts/  (3 files)
      … 3 files under this directory
    src/  (129 files)
      … 129 files under this directory
    package.json
  renderer/  (142 files)
    fonts/  (28 files)
      … 28 files under this directory
    scoreboard/  (11 files)
      … 11 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    src/  (95 files)
      … 95 files under this directory
    .gitignore
    CHANGELOG.md
    FONTS-LICENSE.md
    package.json
    tsdown.config.ts
  website/  (197 files)
    public/  (3 files)
      … 3 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    src/  (183 files)
      … 183 files under this directory
    tests/  (3 files)
      … 3 files under this directory
    .gitignore
    astro.config.ts
    bunfig.toml
    package.json
    playwright.config.ts
    svelte.config.js
    tsconfig.json
scripts/  (8 files)
  brand/  (2 files)
    lib.ts
    write.ts
  generate-card.ts
  generate-logo.ts
  generate-readme-svg.ts
  prepareForRelease.ts
  tegami.mts
  test-published-examples.ts
.editorconfig
.gitignore
AGENTS.md
CHANGELOG.md
CLAUDE.md
CONTRIBUTING.md
LICENSE
README.md
biome.jsonc
bunfig.toml
package.json
skills-lock.json
tegaki.code-workspace
tsconfig.json
```

## Entry points

- [packages/generator/src/index.ts](https://github.com/gkurt/tegaki/blob/bf18556996d9683326e8f2130bd50e7632e9f187/packages/generator/src/index.ts)
- [packages/renderer/src/index.ts](https://github.com/gkurt/tegaki/blob/bf18556996d9683326e8f2130bd50e7632e9f187/packages/renderer/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 34 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| e2e package | library | Observed | Groups 4 file(s) under e2e package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 369 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 7 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 22 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.claude/launch.json` (config)
- `.claude/settings.json` (config)
- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deploy-docs.yml` (ci)
- `.github/workflows/release-smoke.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/scoreboard.yml` (ci)
- `.github/workflows/tegami-pr-comment.yml` (ci)
- `.github/workflows/tegami-pr.yml` (ci)
- `.tegami/publish-lock.yaml` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `bunfig.toml` (config)
- `e2e/examples/package.json` (manifest)
- `examples/astro/package.json` (manifest)
- `examples/astro/tsconfig.json` (config)
- `examples/editframe/package.json` (manifest)
- `examples/editframe/tsconfig.json` (config)
- `examples/next/package.json` (manifest)
- `examples/next/tsconfig.json` (config)
- `examples/nuxt/package.json` (manifest)
- `examples/nuxt/tsconfig.json` (config)
- `examples/remotion/package.json` (manifest)
- `examples/remotion/tsconfig.json` (config)
- `examples/solid/package.json` (manifest)
- `examples/solid/tsconfig.json` (config)
- `examples/svelte/package.json` (manifest)
- `examples/svelte/tsconfig.json` (config)
- `examples/vanilla/package.json` (manifest)
- `examples/vanilla/tsconfig.json` (config)
- `examples/vite/package.json` (manifest)
- `examples/vite/tsconfig.json` (config)
- `examples/vue/package.json` (manifest)
- `examples/vue/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/generator/package.json` (manifest)
- `packages/renderer/fonts/amiri/glyphData.json` (config)
- `packages/renderer/fonts/atma/glyphData.json` (config)
- `packages/renderer/fonts/caveat/glyphData.json` (config)
- `packages/renderer/fonts/ems-allure/glyphData.json` (config)
- `packages/renderer/fonts/hershey-script/glyphData.json` (config)
- `packages/renderer/fonts/italianno/glyphData.json` (config)
- `packages/renderer/fonts/italianno/glyphDataById.json` (config)
- `packages/renderer/fonts/parisienne/glyphData.json` (config)
- `packages/renderer/fonts/parisienne/glyphDataById.json` (config)
- `packages/renderer/fonts/suez-one/glyphData.json` (config)
- `packages/renderer/fonts/suez-one/glyphDataById.json` (config)
- `packages/renderer/fonts/tangerine/glyphData.json` (config)
- `packages/renderer/fonts/tillana/glyphData.json` (config)
- `packages/renderer/package.json` (manifest)
- `packages/renderer/scoreboard/amiri.json` (config)
- `packages/renderer/scoreboard/atma.json` (config)
- `packages/renderer/scoreboard/caveat.json` (config)
- `packages/renderer/scoreboard/italianno.json` (config)
- `packages/renderer/scoreboard/klee-one.json` (config)
- `packages/renderer/scoreboard/lxgw-wenkai.json` (config)
- `packages/renderer/scoreboard/nanum-pen-script.json` (config)
- `packages/renderer/scoreboard/parisienne.json` (config)
- `packages/renderer/scoreboard/suez-one.json` (config)
- `packages/renderer/scoreboard/tangerine.json` (config)
- `packages/renderer/scoreboard/tillana.json` (config)
- `packages/website/bunfig.toml` (config)
- `packages/website/package.json` (manifest)
- `packages/website/tsconfig.json` (config)
- `skills-lock.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `packages` — 472 analysed file(s)
- `examples` — 106 analysed file(s)
- `.agents` — 42 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 8 analysed file(s)
- `scripts` — 8 analysed file(s)
- `e2e` — 5 analysed file(s)
- `.claude` — 2 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `media` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)
- `.tegami` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `bf18556996d9683326e8f2130bd50e7632e9f187` is the revision these paths and observations refer to.
