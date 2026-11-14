# Project structure: airbnb/react-sketchapp

**Analysed commit:** `b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7`

**Commit reference:** [b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7](https://github.com/airbnb/react-sketchapp/commit/b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7)

**Tree at this commit:** [airbnb/react-sketchapp@b238e69c6f1e](https://github.com/airbnb/react-sketchapp/tree/b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | airbnb/react-sketchapp |
| Description | render React components to Sketch ⚛️💎 |
| Stars | 14848 |
| Forks | 793 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7` |
| Retrieved at | 2026-11-14T19:13:16.468978+00:00 |
| Files in this snapshot | 320 |

## Directory tree

```text
.github/  (3 files)
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  ISSUE_TEMPLATE.md
__tests__/  (34 files)
  jest/  (31 files)
    components/  (18 files)
      … 18 files under this directory
    jsonUtils/  (7 files)
      … 7 files under this directory
    sharedStyles/  (1 files)
      … 1 files under this directory
    utils/  (3 files)
      … 3 files under this directory
    index.ts
    reactTreeToFlexTree.ts
  skpm/  (3 files)
    basic.test.js
    render-context.test.js
    render-in-wrapped-object.test.js
docs/  (11 files)
  guides/  (7 files)
    README.md
    data-fetching.md
    getting-started.md
    rendering.md
    styling.md
    universal-rendering.md
    using-skpm.md
  API.md
  FAQ.md
  README.md
  examples.md
examples/  (137 files)
  basic-setup/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    README.md
    package.json
    webpack.skpm.config.js
  basic-setup-typescript/  (8 files)
    src/  (2 files)
      … 2 files under this directory
    .gitignore
    README.md
    manifest.json
    package.json
    tsconfig.json
    webpack.skpm.config.js
  basic-svg/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    README.md
    package.json
    webpack.skpm.config.js
  colors/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    README.md
    package.json
    webpack.skpm.config.js
  emotion/  (4 files)
    src/  (2 files)
      … 2 files under this directory
    package.json
    webpack.skpm.config.js
  form-validation/  (15 files)
    src/  (12 files)
      … 12 files under this directory
    README.md
    package.json
    webpack.skpm.config.js
  foursquare-maps/  (9 files)
    src/  (5 files)
      … 5 files under this directory
    .eslintrc
    README.md
    package.json
    webpack.skpm.config.js
  glamorous/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    README.md
    package.json
    webpack.skpm.config.js
  profile-cards/  (8 files)
    src/  (5 files)
      … 5 files under this directory
    README.md
    package.json
    webpack.skpm.config.js
  profile-cards-graphql/  (8 files)
    src/  (5 files)
      … 5 files under this directory
    README.md
    package.json
    webpack.skpm.config.js
  profile-cards-primitives/  (11 files)
    src/  (7 files)
      … 7 files under this directory
    README.md
    nwb.config.js
    package.json
    webpack.skpm.config.js
  profile-cards-react-with-styles/  (9 files)
    src/  (6 files)
      … 6 files under this directory
    README.md
    package.json
    webpack.skpm.config.js
  react-router-prototyping/  (12 files)
    src/  (9 files)
      … 9 files under this directory
    README.md
    package.json
    webpack.skpm.config.js
  styled-components/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    README.md
    package.json
    webpack.skpm.config.js
  styleguide/  (15 files)
    src/  (11 files)
      … 11 files under this directory
    .flowconfig
    README.md
    package.json
    webpack.skpm.config.js
  symbols/  (5 files)
    src/  (2 files)
      … 2 files under this directory
    README.md
    package.json
    webpack.skpm.config.js
  timeline-airtable/  (6 files)
    src/  (2 files)
      … 2 files under this directory
    .eslintrc
    README.md
    package.json
    webpack.skpm.config.js
  .eslintrc
  .gitignore
src/  (116 files)
  components/  (38 files)
    Svg/  (23 files)
      … 23 files under this directory
    Artboard.tsx
    Document.tsx
    Image.tsx
    ImageStylePropTypes.ts
    Page.tsx
    PageStylePropTypes.ts
    RedBox.tsx
    ResizeModePropTypes.ts
    ResizingConstraintPropTypes.ts
    ShadowsPropTypes.ts
    Text.tsx
    TextStylePropTypes.ts
    View.tsx
    ViewStylePropTypes.ts
    index.ts
  jsonUtils/  (20 files)
    makeSvgLayer/  (7 files)
      … 7 files under this directory
    sketchJson/  (2 files)
      … 2 files under this directory
    borders.ts
    computeTextTree.ts
    computeYogaNode.ts
    computeYogaTree.ts
    hotspotLayer.ts
    layerGroup.ts
    models.ts
    resizeConstraint.ts
    shapeLayers.ts
    style.ts
    textLayers.ts
  platformBridges/  (5 files)
    sketch/  (4 files)
      … 4 files under this directory
    macos.ts
  renderers/  (9 files)
    ArtboardRenderer.ts
    ImageRenderer.ts
    SketchRenderer.ts
    SvgRenderer.ts
    SymbolInstanceRenderer.ts
    SymbolMasterRenderer.ts
    TextRenderer.ts
    ViewRenderer.ts
    index.ts
  sharedStyles/  (1 files)
    TextStyles.ts
  stylesheet/  (3 files)
    expandStyle.ts
    index.ts
    types.ts
  types/  (7 files)
    globals.d.ts
    index.ts
    intrinsic.d.ts
    js-sha1.d.ts
    murmur2js.d.ts
    node-sketch-bridge.d.ts
    normalize-css-color.d.ts
  utils/  (22 files)
    processTransform/  (4 files)
      … 4 files under this directory
    sharedTextStyles/  (2 files)
      … 2 files under this directory
    Context.ts
    constants.ts
    createStringMeasurer.ts
    getDocument.ts
    getImageDataFromURL.ts
    getSketchVersion.ts
    hasAnyDefined.ts
    hashStyle.ts
    isDefined.ts
    isNativeDocument.ts
    isNativePage.ts
    isNativeSymbolsPage.ts
    pick.ts
    same.ts
    sortObjectKeys.ts
    zIndex.ts
  Platform.ts
  buildTree.ts
  context.tsx
  entrypoint.sketch.ts
  entrypoint.ts
  flexToSketchJSON.ts
  index.ts
  render.tsx
  renderToJSON.ts
  resets.ts
  symbol.tsx
template/  (5 files)
  src/  (2 files)
    manifest.json
    my-command.js
  .gitignore
  README.md
  package.json
.bookignore
.editorconfig
.gitignore
.npmignore
.travis.yml
CHANGELOG.md
LICENSE
README.md
book.json
jest.config.js
package.json
prettier.config.js
tsconfig.json
tsconfig.module.json
```

## Entry points

- [src/components/Page.tsx](https://github.com/airbnb/react-sketchapp/blob/b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7/src/components/Page.tsx)
- [src/components/Svg/index.tsx](https://github.com/airbnb/react-sketchapp/blob/b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7/src/components/Svg/index.tsx)
- [src/components/index.ts](https://github.com/airbnb/react-sketchapp/blob/b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7/src/components/index.ts)
- [src/index.ts](https://github.com/airbnb/react-sketchapp/blob/b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7/src/index.ts)
- [src/jsonUtils/makeSvgLayer/index.ts](https://github.com/airbnb/react-sketchapp/blob/b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7/src/jsonUtils/makeSvgLayer/index.ts)
- [src/platformBridges/sketch/index.ts](https://github.com/airbnb/react-sketchapp/blob/b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7/src/platformBridges/sketch/index.ts)
- [src/renderers/index.ts](https://github.com/airbnb/react-sketchapp/blob/b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7/src/renderers/index.ts)
- [src/stylesheet/index.ts](https://github.com/airbnb/react-sketchapp/blob/b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7/src/stylesheet/index.ts)
- [src/types/index.ts](https://github.com/airbnb/react-sketchapp/blob/b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7/src/types/index.ts)
- [src/utils/processTransform/index.ts](https://github.com/airbnb/react-sketchapp/blob/b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7/src/utils/processTransform/index.ts)
- [src/utils/sharedTextStyles/index.ts](https://github.com/airbnb/react-sketchapp/blob/b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7/src/utils/sharedTextStyles/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| buildTree.ts package | library | Observed | Groups 1 file(s) under buildtree.ts package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 38 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| context.tsx package | library | Observed | Groups 1 file(s) under context.tsx package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| entrypoint.sketch.ts package | library | Observed | Groups 1 file(s) under entrypoint.sketch.ts package (observed from repository paths and static analysis). |
| entrypoint.ts package | library | Observed | Groups 1 file(s) under entrypoint.ts package (observed from repository paths and static analysis). |
| flexToSketchJSON.ts package | library | Observed | Groups 1 file(s) under flextosketchjson.ts package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| jsonUtils package | library | Observed | Groups 20 file(s) under jsonutils package (observed from repository paths and static analysis). |
| Platform.ts package | library | Observed | Groups 1 file(s) under platform.ts package (observed from repository paths and static analysis). |
| platformBridges package | library | Observed | Groups 5 file(s) under platformbridges package (observed from repository paths and static analysis). |
| render.tsx package | library | Observed | Groups 1 file(s) under render.tsx package (observed from repository paths and static analysis). |
| renderers package | library | Observed | Groups 9 file(s) under renderers package (observed from repository paths and static analysis). |
| renderToJSON.ts package | library | Observed | Groups 1 file(s) under rendertojson.ts package (observed from repository paths and static analysis). |
| resets.ts package | library | Observed | Groups 1 file(s) under resets.ts package (observed from repository paths and static analysis). |
| sharedStyles package | library | Observed | Groups 1 file(s) under sharedstyles package (observed from repository paths and static analysis). |
| stylesheet package | library | Observed | Groups 3 file(s) under stylesheet package (observed from repository paths and static analysis). |
| symbol.tsx package | library | Observed | Groups 1 file(s) under symbol.tsx package (observed from repository paths and static analysis). |
| template package | library | Observed | Groups 1 file(s) under template package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 25 file(s) under __tests__ package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 7 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 22 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `book.json` (config)
- `examples/basic-setup-typescript/manifest.json` (config)
- `examples/basic-setup-typescript/package.json` (manifest)
- `examples/basic-setup-typescript/tsconfig.json` (config)
- `examples/basic-setup/package.json` (manifest)
- `examples/basic-setup/src/manifest.json` (config)
- `examples/basic-svg/package.json` (manifest)
- `examples/basic-svg/src/manifest.json` (config)
- `examples/colors/package.json` (manifest)
- `examples/colors/src/manifest.json` (config)
- `examples/emotion/package.json` (manifest)
- `examples/emotion/src/manifest.json` (config)
- `examples/form-validation/package.json` (manifest)
- `examples/form-validation/src/manifest.json` (config)
- `examples/foursquare-maps/package.json` (manifest)
- `examples/foursquare-maps/src/manifest.json` (config)
- `examples/glamorous/package.json` (manifest)
- `examples/glamorous/src/manifest.json` (config)
- `examples/profile-cards-graphql/package.json` (manifest)
- `examples/profile-cards-graphql/src/manifest.json` (config)
- `examples/profile-cards-primitives/package.json` (manifest)
- `examples/profile-cards-primitives/src/manifest.json` (config)
- `examples/profile-cards-react-with-styles/package.json` (manifest)
- `examples/profile-cards-react-with-styles/src/manifest.json` (config)
- `examples/profile-cards/package.json` (manifest)
- `examples/profile-cards/src/manifest.json` (config)
- `examples/react-router-prototyping/package.json` (manifest)
- `examples/react-router-prototyping/src/manifest.json` (config)
- `examples/styled-components/package.json` (manifest)
- `examples/styled-components/src/manifest.json` (config)
- `examples/styleguide/package.json` (manifest)
- `examples/styleguide/src/manifest.json` (config)
- `examples/symbols/package.json` (manifest)
- `examples/symbols/src/manifest.json` (config)
- `examples/timeline-airtable/package.json` (manifest)
- `examples/timeline-airtable/src/manifest.json` (config)
- `package.json` (manifest)
- `template/package.json` (manifest)
- `template/src/manifest.json` (config)
- `tsconfig.json` (config)
- `tsconfig.module.json` (config)

## Top-level layout

- `examples` — 137 analysed file(s)
- `src` — 116 analysed file(s)
- `__tests__` — 34 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `docs` — 11 analysed file(s)
- `template` — 5 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b238e69c6f1e65ec6b1d8a908a91fbd9a8cc43a7` is the revision these paths and observations refer to.
