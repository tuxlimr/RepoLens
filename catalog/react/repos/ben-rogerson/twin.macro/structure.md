# Project structure: ben-rogerson/twin.macro

**Analysed commit:** `e1b2f7abe8da358669d0c49995ecda6912cd1476`

**Commit reference:** [e1b2f7abe8da358669d0c49995ecda6912cd1476](https://github.com/ben-rogerson/twin.macro/commit/e1b2f7abe8da358669d0c49995ecda6912cd1476)

**Tree at this commit:** [ben-rogerson/twin.macro@e1b2f7abe8da](https://github.com/ben-rogerson/twin.macro/tree/e1b2f7abe8da358669d0c49995ecda6912cd1476)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ben-rogerson/twin.macro |
| Description | 🦹‍♂️ Twin blends the magic of Tailwind with the flexibility of css-in-js (emotion, styled-components, solid-styled-components, stitches and goober) at build time. |
| Stars | 8028 |
| Forks | 182 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `e1b2f7abe8da358669d0c49995ecda6912cd1476` |
| Retrieved at | 2026-11-14T19:13:43.358406+00:00 |
| Files in this snapshot | 392 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.md
    config.yml
  workflows/  (1 files)
    main.yml
  FUNDING.yml
  logo-dark.svg
  logo-light.svg
docs/  (10 files)
  advanced-theming.md
  arbitrary-values.md
  customizing-config.md
  fonts.md
  group.md
  index.md
  options.md
  prop-styling-guide.md
  screen-import.md
  styled-component-guide.md
sandbox/  (1 files)
  in.tsx
src/  (55 files)
  core/  (30 files)
    lib/  (23 files)
      … 23 files under this directory
    types/  (1 files)
      … 1 files under this directory
    constants.ts
    createCoreContext.ts
    extractRuleStyles.ts
    getGlobalStyles.ts
    getStyles.ts
    index.ts
  macro/  (15 files)
    lib/  (4 files)
      … 4 files under this directory
    types/  (1 files)
      … 1 files under this directory
    className.ts
    css.ts
    dataProp.ts
    globalStyles.ts
    screen.ts
    shortCss.ts
    styled.ts
    theme.ts
    tw.ts
    twin.ts
  suggestions/  (9 files)
    lib/  (7 files)
      … 7 files under this directory
    types/  (1 files)
      … 1 files under this directory
    index.ts
  macro.ts
tests/  (296 files)
  __fixtures__/  (273 files)
    addBase/  (2 files)
      … 2 files under this directory
    arbitraryProperties/  (1 files)
      … 1 files under this directory
    arbitraryVariants/  (2 files)
      … 2 files under this directory
    autoCssProp/  (1 files)
      … 1 files under this directory
    colorFunctions/  (2 files)
      … 2 files under this directory
    comments/  (2 files)
      … 2 files under this directory
    config/  (2 files)
      … 2 files under this directory
    configTS/  (2 files)
      … 2 files under this directory
    content/  (2 files)
      … 2 files under this directory
    cssPropEmotion/  (2 files)
      … 2 files under this directory
    cssPropStyledComponents/  (3 files)
      … 3 files under this directory
    darkLightModeArray/  (2 files)
      … 2 files under this directory
    directionalBorders/  (1 files)
      … 1 files under this directory
    fluidContainer/  (2 files)
      … 2 files under this directory
    globalStyles/  (3 files)
      … 3 files under this directory
    group/  (1 files)
      … 1 files under this directory
    includeClassNames/  (2 files)
      … 2 files under this directory
    lineClamp/  (1 files)
      … 1 files under this directory
    negative/  (2 files)
      … 2 files under this directory
    peers/  (1 files)
      … 1 files under this directory
    pluginAspectRatio/  (2 files)
      … 2 files under this directory
    pluginDaisyUi/  (2 files)
      … 2 files under this directory
    pluginExamples/  (2 files)
      … 2 files under this directory
    pluginForms/  (2 files)
      … 2 files under this directory
    pluginFormsClassStrategy/  (2 files)
      … 2 files under this directory
    pluginGapFallback/  (2 files)
      … 2 files under this directory
    pluginTypography/  (2 files)
      … 2 files under this directory
    pluginUserParentSelector/  (2 files)
      … 2 files under this directory
    plugins/  (3 files)
      … 3 files under this directory
    prefix/  (3 files)
      … 3 files under this directory
    preflight/  (2 files)
      … 2 files under this directory
    presets/  (2 files)
      … 2 files under this directory
    sassyPseudo/  (3 files)
      … 3 files under this directory
    screenImport/  (2 files)
      … 2 files under this directory
    screens/  (2 files)
      … 2 files under this directory
    separator/  (2 files)
      … 2 files under this directory
    shortCss/  (2 files)
      … 2 files under this directory
    stitches/  (6 files)
      … 6 files under this directory
    themeValuesToString/  (2 files)
      … 2 files under this directory
    userPluginOrdering/  (2 files)
      … 2 files under this directory
    utilitiesAccessibility/  (1 files)
      … 1 files under this directory
    utilitiesBackgrounds/  (11 files)
      … 11 files under this directory
    utilitiesBorders/  (20 files)
      … 20 files under this directory
    utilitiesEffects/  (5 files)
      … 5 files under this directory
    utilitiesFilters/  (19 files)
      … 19 files under this directory
    utilitiesLayout/  (21 files)
      … 21 files under this directory
    utilitiesSpacing/  (3 files)
      … 3 files under this directory
    utilitiesSvg/  (4 files)
      … 4 files under this directory
    utilitiesTransforms/  (7 files)
      … 7 files under this directory
    utilitiesTransitionsAnimation/  (6 files)
      … 6 files under this directory
    utiltiesFlexboxGrid/  (25 files)
      … 25 files under this directory
    utiltiesInteractivity/  (16 files)
      … 16 files under this directory
    utiltiesSizing/  (6 files)
      … 6 files under this directory
    utiltiesTables/  (4 files)
      … 4 files under this directory
    utiltiesTypography/  (29 files)
      … 29 files under this directory
    variables/  (2 files)
      … 2 files under this directory
    variantOrdering/  (1 files)
      … 1 files under this directory
    visitedOpacity/  (1 files)
      … 1 files under this directory
    !general.tsx
    !important.tsx
    !imports.tsx
    !namelessImport.tsx
    !ordering.tsx
    !properties.tsx
    !variantGrouping.tsx
    !variants.tsx
    .eslintrc.js
  types/  (2 files)
    index.ts
    types.d.ts
  util/  (2 files)
    customMatchers.ts
    run.ts
  @applyInPlugins.test.ts
  animations.test.ts
  arbitraryProperties.test.ts
  arbitraryValues.test.ts
  arbitraryVariants.test.ts
  config.test.ts
  containerQueries.test.ts
  dividers.test.ts
  escaping.test.ts
  fontSize.test.ts
  minMaxScreenVariants.test.ts
  plugin.test.js
  presetEmotion.test.ts
  presetGoober.test.ts
  presetSolid.test.ts
  presetStitches.test.ts
  presetStyledComponents.test.ts
  screens.test.ts
  stitches.config.js
types/  (13 files)
  tests/  (9 files)
    __fixtures__/  (2 files)
      … 2 files under this directory
    basic/  (3 files)
      … 3 files under this directory
    emotion/  (2 files)
      … 2 files under this directory
    styled-components/  (2 files)
      … 2 files under this directory
  index.d.ts
  macro.d.ts
  tsconfig.base.json
  tsconfig.json
.babelrc
.eslintrc.js
.gitignore
.nvmrc
.prettierrc
CODE_OF_CONDUCT.md
LICENSE
README.md
jest.config.ts
package.json
tsconfig.json
```

## Entry points

- [src/core/index.ts](https://github.com/ben-rogerson/twin.macro/blob/e1b2f7abe8da358669d0c49995ecda6912cd1476/src/core/index.ts)
- [src/core/types/index.ts](https://github.com/ben-rogerson/twin.macro/blob/e1b2f7abe8da358669d0c49995ecda6912cd1476/src/core/types/index.ts)
- [src/macro/types/index.ts](https://github.com/ben-rogerson/twin.macro/blob/e1b2f7abe8da358669d0c49995ecda6912cd1476/src/macro/types/index.ts)
- [src/suggestions/index.ts](https://github.com/ben-rogerson/twin.macro/blob/e1b2f7abe8da358669d0c49995ecda6912cd1476/src/suggestions/index.ts)
- [src/suggestions/types/index.ts](https://github.com/ben-rogerson/twin.macro/blob/e1b2f7abe8da358669d0c49995ecda6912cd1476/src/suggestions/types/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| macro package | library | Observed | Groups 15 file(s) under macro package (observed from repository paths and static analysis). |
| macro.ts package | library | Observed | Groups 1 file(s) under macro.ts package (observed from repository paths and static analysis). |
| sandbox package | library | Observed | Groups 1 file(s) under sandbox package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 30 file(s) under service / domain layer (observed from repository paths and static analysis). |
| suggestions package | library | Observed | Groups 9 file(s) under suggestions package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 305 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 2 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/main.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `types/tsconfig.base.json` (config)
- `types/tsconfig.json` (config)

## Top-level layout

- `tests` — 296 analysed file(s)
- `src` — 55 analysed file(s)
- `types` — 13 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `docs` — 10 analysed file(s)
- `.github` — 6 analysed file(s)
- `sandbox` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e1b2f7abe8da358669d0c49995ecda6912cd1476` is the revision these paths and observations refer to.
