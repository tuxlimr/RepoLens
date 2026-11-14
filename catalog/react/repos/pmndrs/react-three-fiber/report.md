# Architecture report: pmndrs/react-three-fiber

> Automated static analysis. **Observed** = directly seen in files/imports/AST; **Inferred** = interpretation from that evidence. Repository code was not executed.

## 1. Repository at a glance

| Item | Value |
| --- | --- |
| Repository | pmndrs/react-three-fiber |
| Description | 🇨🇭 A React renderer for Three.js |
| Language | TypeScript |
| Stars | 33723 |
| Licence | MIT |
| Analysed commit / branch | d74622ea8ed717f7212d7e19d65ff3e325508389 / master |
| Framework(s) | React |
| Files analysed | 185 |
| Components | 5 |

## 2. Architecture in one minute

pmndrs/react-three-fiber - 🇨🇭 A React renderer for Three.js. This repository was analysed statically from 185 file(s) (0 Python). Detected technologies (observed from imports/manifests): GitHub Actions, React, Jest, TypeScript, Vite. Files are grouped into 5 component(s): Configuration and deployment, Core modules, packages package, Service / domain layer, Tests. Findings below distinguish observed facts from inferred interpretation.

## 3. High-level block diagram

```mermaid
flowchart TD
    subgraph config_group
        config["Configuration and deployment"]
    end
    subgraph core_group
        core["Core modules"]
    end
    subgraph library_group
        packages["packages package"]
    end
    subgraph service_group
        service_layer["Service / domain layer"]
    end
    subgraph test_group
        tests["Tests"]
    end
```

## 4. Main components

### Configuration and deployment (`config`)

- **Kind:** config
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis).
- **Paths:** `package.json`, `packages/eslint-plugin/package.json`, `packages/eslint-plugin/src/configs/all.ts`, `packages/eslint-plugin/src/configs/recommended.ts`, `packages/fiber/native/package.json`, `packages/fiber/package.json`, `packages/test-renderer/package.json`, `tsconfig.json`
- **Evidence:** [package.json](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/package.json); [packages/eslint-plugin/package.json](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/package.json); [packages/eslint-plugin/src/configs/all.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/configs/all.ts); [packages/eslint-plugin/src/configs/recommended.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/configs/recommended.ts); [packages/fiber/native/package.json](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/native/package.json); [packages/fiber/package.json](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/package.json); [packages/test-renderer/package.json](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/test-renderer/package.json); [tsconfig.json](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/tsconfig.json)

### Core modules (`core`)

- **Kind:** core
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 3 file(s) under core modules (observed from repository paths and static analysis).
- **Paths:** `babel.config.js`, `jest.config.js`, `vite.config.ts`
- **Evidence:** [babel.config.js](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/babel.config.js); [jest.config.js](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/jest.config.js); [vite.config.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/vite.config.ts)

### packages package (`packages`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 38 file(s) under packages package (observed from repository paths and static analysis).
- **Paths:** `packages/eslint-plugin/scripts/codegen.ts`, `packages/eslint-plugin/src/index.ts`, `packages/eslint-plugin/src/lib/url.ts`, `packages/eslint-plugin/src/rules/index.ts`, `packages/eslint-plugin/src/rules/no-clone-in-loop.ts`, `packages/eslint-plugin/src/rules/no-new-in-loop.ts`, `packages/fiber/__mocks__/expo-asset.ts`, `packages/fiber/__mocks__/expo-file-system.ts`, `packages/fiber/__mocks__/expo-gl.ts`, `packages/fiber/__mocks__/react-native.ts`, `packages/fiber/__mocks__/react-use-measure.ts`, `packages/fiber/src/index.tsx`, `packages/fiber/src/native.tsx`, `packages/fiber/src/native/Canvas.tsx`, `packages/fiber/src/native/events.ts`, `packages/fiber/src/native/polyfills.ts`, `packages/fiber/src/three-types.ts`, `packages/fiber/src/web/Canvas.tsx`, `packages/fiber/src/web/events.ts`, `packages/shared/setupTests.ts`, `packages/test-renderer/src/WebGL2RenderingContext.ts`, `packages/test-renderer/src/__tests__/RTTR.core.test.tsx`, `packages/test-renderer/src/__tests__/RTTR.events.test.tsx`, `packages/test-renderer/src/__tests__/RTTR.hooks.test.tsx`, `packages/test-renderer/src/__tests__/RTTR.methods.test.tsx`, `packages/test-renderer/src/createTestCanvas.ts`, `packages/test-renderer/src/createTestInstance.ts`, `packages/test-renderer/src/fireEvent.ts`, `packages/test-renderer/src/helpers/events.ts`, `packages/test-renderer/src/helpers/graph.ts`, `packages/test-renderer/src/helpers/strings.ts`, `packages/test-renderer/src/helpers/testInstance.ts`, `packages/test-renderer/src/helpers/tree.ts`, `packages/test-renderer/src/helpers/waitFor.ts`, `packages/test-renderer/src/index.tsx`, `packages/test-renderer/src/types/index.ts`, `packages/test-renderer/src/types/internal.ts`, `packages/test-renderer/src/types/public.ts`
- **Evidence:** [packages/eslint-plugin/scripts/codegen.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/scripts/codegen.ts); [packages/eslint-plugin/src/index.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/index.ts); [packages/eslint-plugin/src/lib/url.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/lib/url.ts); [packages/eslint-plugin/src/rules/index.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/rules/index.ts); [packages/eslint-plugin/src/rules/no-clone-in-loop.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/rules/no-clone-in-loop.ts); [packages/eslint-plugin/src/rules/no-new-in-loop.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/rules/no-new-in-loop.ts); [packages/fiber/__mocks__/expo-asset.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/__mocks__/expo-asset.ts); [packages/fiber/__mocks__/expo-file-system.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/__mocks__/expo-file-system.ts)

### Service / domain layer (`service_layer`)

- **Kind:** service
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 14 file(s) under service / domain layer (observed from repository paths and static analysis).
- **Paths:** `packages/fiber/src/core/configuration.ts`, `packages/fiber/src/core/events.ts`, `packages/fiber/src/core/extend.ts`, `packages/fiber/src/core/hooks.tsx`, `packages/fiber/src/core/index.tsx`, `packages/fiber/src/core/loop.ts`, `packages/fiber/src/core/portal.tsx`, `packages/fiber/src/core/reconciler.tsx`, `packages/fiber/src/core/renderer.ts`, `packages/fiber/src/core/root.tsx`, `packages/fiber/src/core/store.ts`, `packages/fiber/src/core/utils.tsx`, `packages/fiber/src/core/utils/promise.ts`, `packages/fiber/src/core/utils/react.tsx`
- **Evidence:** [packages/fiber/src/core/configuration.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/configuration.ts); [packages/fiber/src/core/events.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/events.ts); [packages/fiber/src/core/extend.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/extend.ts); [packages/fiber/src/core/hooks.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/hooks.tsx); [packages/fiber/src/core/index.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/index.tsx); [packages/fiber/src/core/loop.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/loop.ts); [packages/fiber/src/core/portal.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/portal.tsx); [packages/fiber/src/core/reconciler.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/reconciler.tsx)

### Tests (`tests`)

- **Kind:** test
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 18 file(s) under tests (observed from repository paths and static analysis).
- **Paths:** `packages/eslint-plugin/tests/rules/no-clone-in-loop.test.ts`, `packages/eslint-plugin/tests/rules/no-new-in-loop.test.ts`, `packages/fiber/tests/__snapshots__/canvas.native.test.tsx.snap`, `packages/fiber/tests/__snapshots__/canvas.test.tsx.snap`, `packages/fiber/tests/__snapshots__/index.test.tsx.snap`, `packages/fiber/tests/__snapshots__/utils.test.ts.snap`, `packages/fiber/tests/canvas.native.test.tsx`, `packages/fiber/tests/canvas.test.tsx`, `packages/fiber/tests/configuration.test.tsx`, `packages/fiber/tests/dpr.test.tsx`, `packages/fiber/tests/events.test.tsx`, `packages/fiber/tests/hooks.test.tsx`, `packages/fiber/tests/index.test.tsx`, `packages/fiber/tests/polyfills.test.ts`, `packages/fiber/tests/reconciler.test.ts`, `packages/fiber/tests/renderer.test.tsx`, `packages/fiber/tests/types.test.tsx`, `packages/fiber/tests/utils.test.ts`
- **Evidence:** [packages/eslint-plugin/tests/rules/no-clone-in-loop.test.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/tests/rules/no-clone-in-loop.test.ts); [packages/eslint-plugin/tests/rules/no-new-in-loop.test.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/tests/rules/no-new-in-loop.test.ts); [packages/fiber/tests/__snapshots__/canvas.native.test.tsx.snap](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/tests/__snapshots__/canvas.native.test.tsx.snap); [packages/fiber/tests/__snapshots__/canvas.test.tsx.snap](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/tests/__snapshots__/canvas.test.tsx.snap); [packages/fiber/tests/__snapshots__/index.test.tsx.snap](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/tests/__snapshots__/index.test.tsx.snap); [packages/fiber/tests/__snapshots__/utils.test.ts.snap](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/tests/__snapshots__/utils.test.ts.snap); [packages/fiber/tests/canvas.native.test.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/tests/canvas.native.test.tsx); [packages/fiber/tests/canvas.test.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/tests/canvas.test.tsx)

## 5. Execution flow

**Observed** entry point(s):

- [packages/eslint-plugin/src/index.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/index.ts)
- [packages/fiber/src/index.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/index.tsx)
- [packages/test-renderer/src/index.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/test-renderer/src/index.tsx)

Representative flow (derived from observed entry points and the import graph; steps beyond the entry point are **Inferred**):

1. Execution starts at an observed entry point listed above, if present.
2. No internal import relationships between components were observed.

## 6. Project structure

### `(root)`

- `.eslintignore` - other (26 bytes)
- `.eslintrc.json` - config (2027 bytes)
- `.gitignore` - other (331 bytes)
- `.prettierignore` - other (82 bytes)
- `.prettierrc` - other (157 bytes)
- `CONTRIBUTING.md` - docs (2771 bytes)
- `LICENSE` - docs (1072 bytes)
- `babel.config.js` - source, JavaScript (650 bytes)
- `jest.config.js` - source, JavaScript (811 bytes)
- `package.json` - manifest (2933 bytes)
- `readme.md` - docs (14301 bytes)
- `tsconfig.json` - config (547 bytes)
- `vite.config.ts` - source, TypeScript (2406 bytes)

### `.changeset`

- `.changeset/README.md` - docs (510 bytes)
- `.changeset/config.json` - config (370 bytes)
- `.changeset/portal-leaks-v9.md` - docs (250 bytes)
- `.changeset/quiet-tags-narrow.md` - docs (309 bytes)
- `.changeset/sharp-screens-follow.md` - docs (617 bytes)

### `.github`

- `.github/FUNDING.yml` - config (97 bytes)
- `.github/ISSUE_TEMPLATE/bug_report.md` - docs (289 bytes)
- `.github/ISSUE_TEMPLATE/feature_request.md` - docs (105 bytes)
- `.github/issue_template.md` - docs (454 bytes)
- `.github/pull_request_template.md` - docs (730 bytes)
- `.github/workflows/docs.yml` - ci, YAML (10040 bytes)
- `.github/workflows/test.yml` - ci, YAML (1836 bytes)

### `.husky`

- `.husky/.gitignore` - other (2 bytes)
- `.husky/pre-commit` - other (68 bytes)

### `docs`

- `docs/API/additional-exports.mdx` - docs (1662 bytes)
- `docs/API/canvas.mdx` - docs (13570 bytes)
- `docs/API/events.mdx` - docs (8325 bytes)
- `docs/API/hooks.mdx` - docs (16247 bytes)
- `docs/API/objects.mdx` - docs (9087 bytes)
- `docs/API/testing.mdx` - docs (4048 bytes)
- `docs/API/typescript.mdx` - docs (4618 bytes)
- `docs/advanced/pitfalls.mdx` - docs (7563 bytes)
- `docs/advanced/scaling-performance.mdx` - docs (16026 bytes)
- `docs/development/CORE.md` - docs (4815 bytes)
- `docs/getting-started/basic-example-sandpack/index.jsx` - docs (1367 bytes)
- `docs/getting-started/basic-example-sandpack/styles.css` - docs (55 bytes)
- `docs/getting-started/community-r3f-components.mdx` - docs (8078 bytes)
- `docs/getting-started/examples.mdx` - docs (31360 bytes)
- `docs/getting-started/installation.mdx` - docs (5497 bytes)
- `docs/getting-started/introduction.mdx` - docs (9601 bytes)
- `docs/getting-started/your-first-scene.mdx` - docs (5592 bytes)
- `docs/tutorials/basic-animations.mdx` - docs (3514 bytes)
- `docs/tutorials/events-and-interaction.mdx` - docs (2854 bytes)
- `docs/tutorials/how-it-works.mdx` - docs (5895 bytes)
- `docs/tutorials/loading-models.mdx` - docs (6828 bytes)
- `docs/tutorials/loading-textures.mdx` - docs (4304 bytes)
- `docs/tutorials/v9-migration-guide.mdx` - docs (8825 bytes)

### `example`

- `example/.gitignore` - other (45 bytes)
- `example/CHANGELOG.md` - docs (282 bytes)
- `example/favicon.svg` - other (403 bytes)
- `example/index.html` - other (377 bytes)
- `example/package.json` - manifest (742 bytes)
- `example/public/apple.gltf` - other (10407 bytes)
- `example/public/bottle.gltf` - other (5071 bytes)
- `example/public/farm.gltf` - other (155334 bytes)
- `example/public/lightning.gltf` - other (12557 bytes)
- `example/public/ramen.gltf` - other (14756 bytes)
- `example/src/App.tsx` - source, TypeScript (1831 bytes)
- `example/src/components.tsx` - source, TypeScript (667 bytes)
- `example/src/demos/Activity.tsx` - source, TypeScript (2560 bytes)
- `example/src/demos/AutoDispose.tsx` - source, TypeScript (1788 bytes)
- `example/src/demos/ChangeTexture.tsx` - source, TypeScript (750 bytes)
- `example/src/demos/ClickAndHover.tsx` - source, TypeScript (1245 bytes)
- `example/src/demos/ContextMenuOverride.tsx` - source, TypeScript (809 bytes)
- `example/src/demos/FlushSync.tsx` - source, TypeScript (1347 bytes)
- `example/src/demos/Gestures.tsx` - source, TypeScript (1600 bytes)
- `example/src/demos/Gltf.tsx` - source, TypeScript (687 bytes)
- `example/src/demos/Inject.tsx` - source, TypeScript (1566 bytes)
- `example/src/demos/Layers.tsx` - source, TypeScript (1166 bytes)
- `example/src/demos/Lines.tsx` - source, TypeScript (1954 bytes)
- `example/src/demos/MultiMaterial.tsx` - source, TypeScript (3764 bytes)
- `example/src/demos/MultiRender.tsx` - source, TypeScript (1105 bytes)
- `example/src/demos/MultiView.tsx` - source, TypeScript (5693 bytes)
- `example/src/demos/Pointcloud.tsx` - source, TypeScript (2161 bytes)
- `example/src/demos/Portals.tsx` - source, TypeScript (5208 bytes)
- `example/src/demos/Reparenting.tsx` - source, TypeScript (1393 bytes)
- `example/src/demos/ResetProps.tsx` - source, TypeScript (3027 bytes)
- `example/src/demos/SVGRenderer.tsx` - source, TypeScript (1166 bytes)
- `example/src/demos/Selection.tsx` - source, TypeScript (2054 bytes)
- `example/src/demos/ShaderMaterial.tsx` - source, TypeScript (1625 bytes)
- `example/src/demos/StopPropagation.tsx` - source, TypeScript (3042 bytes)
- `example/src/demos/SuspenseAndErrors.tsx` - source, TypeScript (1177 bytes)
- `example/src/demos/SuspenseMaterial.tsx` - source, TypeScript (805 bytes)
- `example/src/demos/Test.tsx` - source, TypeScript (1658 bytes)
- `example/src/demos/ViewTracking.tsx` - source, TypeScript (8549 bytes)
- `example/src/demos/Viewcube.tsx` - source, TypeScript (2224 bytes)
- `example/src/demos/WebGPU.tsx` - source, TypeScript (1788 bytes)
- `example/src/demos/index.tsx` - source, TypeScript (2381 bytes)
- `example/src/index.tsx` - source, TypeScript (140 bytes)
- `example/src/styles.css` - other (2895 bytes)
- `example/tsconfig.json` - config (511 bytes)
- `example/vite.config.ts` - source, TypeScript (193 bytes)

### `packages`

- `packages/eslint-plugin/.npmignore` - other (23 bytes)
- `packages/eslint-plugin/CHANGELOG.md` - docs (260 bytes)
- `packages/eslint-plugin/README.md` - docs (3220 bytes)
- `packages/eslint-plugin/docs/rules/no-clone-in-loop.md` - docs (1264 bytes)
- `packages/eslint-plugin/docs/rules/no-new-in-loop.md` - docs (1245 bytes)
- `packages/eslint-plugin/package.json` - manifest (1325 bytes)
- `packages/eslint-plugin/scripts/codegen.ts` - source, TypeScript (4505 bytes)
- `packages/eslint-plugin/src/configs/all.ts` - source, TypeScript (236 bytes)
- `packages/eslint-plugin/src/configs/recommended.ts` - source, TypeScript (236 bytes)
- `packages/eslint-plugin/src/index.ts` - source, TypeScript (262 bytes)
- `packages/eslint-plugin/src/lib/url.ts` - source, TypeScript (156 bytes)
- `packages/eslint-plugin/src/rules/index.ts` - source, TypeScript (262 bytes)
- `packages/eslint-plugin/src/rules/no-clone-in-loop.ts` - source, TypeScript (856 bytes)
- `packages/eslint-plugin/src/rules/no-new-in-loop.ts` - source, TypeScript (812 bytes)
- `packages/eslint-plugin/tests/rules/no-clone-in-loop.test.ts` - test, TypeScript (629 bytes)
- `packages/eslint-plugin/tests/rules/no-new-in-loop.test.ts` - test, TypeScript (1069 bytes)
- `packages/fiber/.npmignore` - other (82 bytes)
- `packages/fiber/CHANGELOG.md` - docs (24678 bytes)
- `packages/fiber/__mocks__/expo-asset.ts` - source, TypeScript (499 bytes)
- `packages/fiber/__mocks__/expo-file-system.ts` - source, TypeScript (246 bytes)
- `packages/fiber/__mocks__/expo-gl.ts` - source, TypeScript (509 bytes)
- `packages/fiber/__mocks__/react-native.ts` - source, TypeScript (972 bytes)
- `packages/fiber/__mocks__/react-use-measure.ts` - source, TypeScript (427 bytes)
- `packages/fiber/native/package.json` - manifest (158 bytes)
- `packages/fiber/package.json` - manifest (2205 bytes)
- `packages/fiber/readme.md` - docs (10080 bytes)
- `packages/fiber/src/core/configuration.ts` - source, TypeScript (12637 bytes)
- `packages/fiber/src/core/events.ts` - source, TypeScript (23538 bytes)
- `packages/fiber/src/core/extend.ts` - source, TypeScript (1148 bytes)
- `packages/fiber/src/core/hooks.tsx` - source, TypeScript (6253 bytes)
- `packages/fiber/src/core/index.tsx` - source, TypeScript (1308 bytes)
- `packages/fiber/src/core/loop.ts` - source, TypeScript (5491 bytes)
- `packages/fiber/src/core/portal.tsx` - source, TypeScript (4688 bytes)
- `packages/fiber/src/core/reconciler.tsx` - source, TypeScript (27707 bytes)
- `packages/fiber/src/core/renderer.ts` - source, TypeScript (2406 bytes)
- `packages/fiber/src/core/root.tsx` - source, TypeScript (10396 bytes)
- `packages/fiber/src/core/store.ts` - source, TypeScript (12053 bytes)
- `packages/fiber/src/core/utils.tsx` - source, TypeScript (19026 bytes)
- `packages/fiber/src/core/utils/promise.ts` - source, TypeScript (1410 bytes)
- `packages/fiber/src/core/utils/react.tsx` - source, TypeScript (4130 bytes)
- `packages/fiber/src/index.tsx` - source, TypeScript (219 bytes)
- `packages/fiber/src/native.tsx` - source, TypeScript (351 bytes)
- `packages/fiber/src/native/Canvas.tsx` - source, TypeScript (8435 bytes)
- `packages/fiber/src/native/events.ts` - source, TypeScript (2689 bytes)
- `packages/fiber/src/native/polyfills.ts` - source, TypeScript (6023 bytes)
- `packages/fiber/src/three-types.ts` - source, TypeScript (3149 bytes)
- `packages/fiber/src/web/Canvas.tsx` - source, TypeScript (6915 bytes)
- `packages/fiber/src/web/events.ts` - source, TypeScript (2604 bytes)
- `packages/fiber/tests/__snapshots__/canvas.native.test.tsx.snap` - test (513 bytes)
- `packages/fiber/tests/__snapshots__/canvas.test.tsx.snap` - test (460 bytes)
- `packages/fiber/tests/__snapshots__/index.test.tsx.snap` - test (1590 bytes)
- `packages/fiber/tests/__snapshots__/utils.test.ts.snap` - test (445 bytes)
- `packages/fiber/tests/canvas.native.test.tsx` - test, TypeScript (5934 bytes)
- `packages/fiber/tests/canvas.test.tsx` - test, TypeScript (26611 bytes)
- `packages/fiber/tests/configuration.test.tsx` - test, TypeScript (14255 bytes)
- `packages/fiber/tests/dpr.test.tsx` - test, TypeScript (8777 bytes)
- `packages/fiber/tests/events.test.tsx` - test, TypeScript (23441 bytes)
- `packages/fiber/tests/hooks.test.tsx` - test, TypeScript (7402 bytes)
- `packages/fiber/tests/index.test.tsx` - test, TypeScript (17413 bytes)
- `packages/fiber/tests/polyfills.test.ts` - test, TypeScript (1419 bytes)
- `packages/fiber/tests/reconciler.test.ts` - test, TypeScript (3336 bytes)
- `packages/fiber/tests/renderer.test.tsx` - test, TypeScript (51808 bytes)
- `packages/fiber/tests/types.test.tsx` - test, TypeScript (1076 bytes)
- `packages/fiber/tests/utils.test.ts` - test, TypeScript (20229 bytes)
- `packages/shared/setupTests.ts` - source, TypeScript (1593 bytes)
- `packages/test-renderer/.npmignore` - other (15 bytes)
- `packages/test-renderer/CHANGELOG.md` - docs (8245 bytes)
- `packages/test-renderer/README.md` - docs (2788 bytes)
- `packages/test-renderer/markdown/rttr-instance.md` - docs (3955 bytes)
- `packages/test-renderer/markdown/rttr.md` - docs (4646 bytes)
- `packages/test-renderer/package.json` - manifest (812 bytes)
- `packages/test-renderer/src/WebGL2RenderingContext.ts` - source, TypeScript (18816 bytes)
- `packages/test-renderer/src/__tests__/RTTR.core.test.tsx` - source, TypeScript (12841 bytes)
- `packages/test-renderer/src/__tests__/RTTR.events.test.tsx` - source, TypeScript (2014 bytes)
- `packages/test-renderer/src/__tests__/RTTR.hooks.test.tsx` - source, TypeScript (2310 bytes)
- `packages/test-renderer/src/__tests__/RTTR.methods.test.tsx` - source, TypeScript (3532 bytes)
- `packages/test-renderer/src/__tests__/__snapshots__/RTTR.core.test.tsx.snap` - other (9802 bytes)
- `packages/test-renderer/src/createTestCanvas.ts` - source, TypeScript (1334 bytes)
- `packages/test-renderer/src/createTestInstance.ts` - source, TypeScript (4208 bytes)
- `packages/test-renderer/src/fireEvent.ts` - source, TypeScript (1966 bytes)
- `packages/test-renderer/src/helpers/events.ts` - source, TypeScript (378 bytes)
- `packages/test-renderer/src/helpers/graph.ts` - source, TypeScript (1204 bytes)
- `packages/test-renderer/src/helpers/strings.ts` - source, TypeScript (221 bytes)
- `packages/test-renderer/src/helpers/testInstance.ts` - source, TypeScript (1660 bytes)
- `packages/test-renderer/src/helpers/tree.ts` - source, TypeScript (706 bytes)
- `packages/test-renderer/src/helpers/waitFor.ts` - source, TypeScript (600 bytes)
- `packages/test-renderer/src/index.tsx` - source, TypeScript (2965 bytes)
- `packages/test-renderer/src/types/index.ts` - source, TypeScript (25 bytes)
- `packages/test-renderer/src/types/internal.ts` - source, TypeScript (442 bytes)
- `packages/test-renderer/src/types/public.ts` - source, TypeScript (1286 bytes)

## 7. Key dependencies and integrations

| Name | Category | Status | Confidence | Evidence |
| --- | --- | --- | --- | --- |
| GitHub Actions | ci | Observed | 0.90 | [.github/workflows/docs.yml](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/.github/workflows/docs.yml); [.github/workflows/test.yml](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/.github/workflows/test.yml) |
| React | framework | Observed | 0.90 | [example/package.json:11](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/example/package.json#L11); [example/package.json:14](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/example/package.json#L14); [package.json:2](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/package.json#L2); [package.json:58](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/package.json#L58) |
| Jest | tooling | Observed | 0.85 | [package.json:35](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/package.json#L35) |
| TypeScript | tooling | Observed | 0.90 | [example/package.json:28](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/example/package.json#L28); [package.json:51](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/package.json#L51) |
| Vite | tooling | Observed | 0.90 | [example/package.json:6](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/example/package.json#L6); [package.json:28](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/package.json#L28) |

## 8. Data and state

No database, cache, queue, or persistent-state usage was observed in the analysed files. State handling, if any, may be in-memory or in files that were not analysed.

## 9. Configuration and deployment clues

- `.changeset/config.json` (config)
- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `example/package.json` (manifest)
- `example/tsconfig.json` (config)
- `package.json` (manifest)
- `packages/eslint-plugin/package.json` (manifest)
- `packages/fiber/native/package.json` (manifest)
- `packages/fiber/package.json` (manifest)
- `packages/test-renderer/package.json` (manifest)
- `tsconfig.json` (config)

## 10. Design observations

- Service/domain code is distinct from entry and data code, suggesting layered separation (Inferred).
- Tests are present alongside source code (Observed from test file paths).

These observations are interpretations (**Inferred**) of the observed structure, not guarantees about runtime design.

## 11. Limitations and unknowns

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

## 12. Source references

- [.github/workflows/docs.yml](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/.github/workflows/docs.yml)
- [.github/workflows/test.yml](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/.github/workflows/test.yml)
- [babel.config.js](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/babel.config.js)
- [example/package.json:6](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/example/package.json#L6)
- [example/package.json:11](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/example/package.json#L11)
- [example/package.json:14](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/example/package.json#L14)
- [example/package.json:28](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/example/package.json#L28)
- [jest.config.js](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/jest.config.js)
- [package.json](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/package.json)
- [package.json:2](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/package.json#L2)
- [package.json:28](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/package.json#L28)
- [package.json:35](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/package.json#L35)
- [package.json:51](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/package.json#L51)
- [package.json:58](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/package.json#L58)
- [packages/eslint-plugin/package.json](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/package.json)
- [packages/eslint-plugin/scripts/codegen.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/scripts/codegen.ts)
- [packages/eslint-plugin/src/configs/all.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/configs/all.ts)
- [packages/eslint-plugin/src/configs/recommended.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/configs/recommended.ts)
- [packages/eslint-plugin/src/index.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/index.ts)
- [packages/eslint-plugin/src/lib/url.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/lib/url.ts)
- [packages/eslint-plugin/src/rules/index.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/rules/index.ts)
- [packages/eslint-plugin/src/rules/no-clone-in-loop.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/rules/no-clone-in-loop.ts)
- [packages/eslint-plugin/src/rules/no-new-in-loop.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/src/rules/no-new-in-loop.ts)
- [packages/eslint-plugin/tests/rules/no-clone-in-loop.test.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/tests/rules/no-clone-in-loop.test.ts)
- [packages/eslint-plugin/tests/rules/no-new-in-loop.test.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/eslint-plugin/tests/rules/no-new-in-loop.test.ts)
- [packages/fiber/__mocks__/expo-asset.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/__mocks__/expo-asset.ts)
- [packages/fiber/__mocks__/expo-file-system.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/__mocks__/expo-file-system.ts)
- [packages/fiber/native/package.json](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/native/package.json)
- [packages/fiber/package.json](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/package.json)
- [packages/fiber/package.json:2](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/package.json#L2)
- [packages/fiber/package.json:67](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/package.json#L67)
- [packages/fiber/src/core/configuration.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/configuration.ts)
- [packages/fiber/src/core/events.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/events.ts)
- [packages/fiber/src/core/extend.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/extend.ts)
- [packages/fiber/src/core/hooks.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/hooks.tsx)
- [packages/fiber/src/core/index.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/index.tsx)
- [packages/fiber/src/core/loop.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/loop.ts)
- [packages/fiber/src/core/portal.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/portal.tsx)
- [packages/fiber/src/core/reconciler.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/core/reconciler.tsx)
- [packages/fiber/src/index.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/src/index.tsx)
- [packages/fiber/tests/__snapshots__/canvas.native.test.tsx.snap](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/tests/__snapshots__/canvas.native.test.tsx.snap)
- [packages/fiber/tests/__snapshots__/canvas.test.tsx.snap](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/tests/__snapshots__/canvas.test.tsx.snap)
- [packages/fiber/tests/__snapshots__/index.test.tsx.snap](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/tests/__snapshots__/index.test.tsx.snap)
- [packages/fiber/tests/__snapshots__/utils.test.ts.snap](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/tests/__snapshots__/utils.test.ts.snap)
- [packages/fiber/tests/canvas.native.test.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/tests/canvas.native.test.tsx)
- [packages/fiber/tests/canvas.test.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/fiber/tests/canvas.test.tsx)
- [packages/test-renderer/package.json](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/test-renderer/package.json)
- [packages/test-renderer/package.json:2](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/test-renderer/package.json#L2)
- [packages/test-renderer/src/index.tsx](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/packages/test-renderer/src/index.tsx)
- [tsconfig.json](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/tsconfig.json)
- [vite.config.ts](https://github.com/pmndrs/react-three-fiber/blob/d74622ea8ed717f7212d7e19d65ff3e325508389/vite.config.ts)
