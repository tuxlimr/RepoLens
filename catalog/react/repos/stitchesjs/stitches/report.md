# Architecture report: stitchesjs/stitches

> Automated static analysis. **Observed** = directly seen in files/imports/AST; **Inferred** = interpretation from that evidence. Repository code was not executed.

## 1. Repository at a glance

| Item | Value |
| --- | --- |
| Repository | stitchesjs/stitches |
| Description | [Not Actively Maintained] CSS-in-JS with near-zero runtime, SSR, multi-variant support, and a best-in-class developer experience. |
| Language | JavaScript |
| Stars | 7758 |
| Licence | MIT |
| Analysed commit / branch | 50fd8a1adc6360340fe348a8b3ebc8b06d38e230 / canary |
| Framework(s) | React |
| Files analysed | 174 |
| Components | 4 |

## 2. Architecture in one minute

stitchesjs/stitches - [Not Actively Maintained] CSS-in-JS with near-zero runtime, SSR, multi-variant support, and a best-in-class developer experience.. This repository was analysed statically from 174 file(s) (0 Python). Detected technologies (observed from imports/manifests): GitHub Actions, React, TypeScript. Files are grouped into 4 component(s): Configuration and deployment, packages package, Service / domain layer, Tests. Findings below distinguish observed facts from inferred interpretation.

## 3. High-level block diagram

```mermaid
flowchart TD
    subgraph config_group
        config["Configuration and deployment"]
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
- **Responsibility:** Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis).
- **Paths:** `package.json`, `packages/core/package.json`, `packages/react/package.json`, `packages/stringify/package.json`, `tsconfig.json`, `tslint.json`
- **Evidence:** [package.json](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/package.json); [packages/core/package.json](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/package.json); [packages/react/package.json](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/package.json); [packages/stringify/package.json](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/stringify/package.json); [tsconfig.json](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/tsconfig.json); [tslint.json](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/tslint.json)

### packages package (`packages`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 16 file(s) under packages package (observed from repository paths and static analysis).
- **Paths:** `packages/react/src/createStitches.js`, `packages/react/src/features/styled.js`, `packages/react/src/index.js`, `packages/react/src/utility/getCachedConfig.js`, `packages/react/types/config.d.ts`, `packages/react/types/css-util.d.ts`, `packages/react/types/index.d.ts`, `packages/react/types/stitches.d.ts`, `packages/react/types/styled-component.d.ts`, `packages/react/types/theme.d.ts`, `packages/react/types/util.d.ts`, `packages/stringify/src/Array.js`, `packages/stringify/src/getResolvedSelectors.js`, `packages/stringify/src/index.js`, `packages/stringify/src/toCase.js`, `packages/stringify/types/index.d.ts`
- **Evidence:** [packages/react/src/createStitches.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/src/createStitches.js); [packages/react/src/features/styled.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/src/features/styled.js); [packages/react/src/index.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/src/index.js); [packages/react/src/utility/getCachedConfig.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/src/utility/getCachedConfig.js); [packages/react/types/config.d.ts](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/types/config.d.ts); [packages/react/types/css-util.d.ts](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/types/css-util.d.ts); [packages/react/types/index.d.ts](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/types/index.d.ts); [packages/react/types/stitches.d.ts](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/types/stitches.d.ts)

### Service / domain layer (`service_layer`)

- **Kind:** service
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 34 file(s) under service / domain layer (observed from repository paths and static analysis).
- **Paths:** `packages/core/src/ThemeToken.js`, `packages/core/src/convert/toCamelCase.js`, `packages/core/src/convert/toCssRules.js`, `packages/core/src/convert/toHash.js`, `packages/core/src/convert/toHyphenCase.js`, `packages/core/src/convert/toPolyfilledValue.js`, `packages/core/src/convert/toResolvedMediaQueryRanges.js`, `packages/core/src/convert/toResolvedSelectors.js`, `packages/core/src/convert/toSizingValue.js`, `packages/core/src/convert/toTailDashed.js`, `packages/core/src/convert/toTokenizedValue.js`, `packages/core/src/createStitches.js`, `packages/core/src/default/defaultThemeMap.js`, `packages/core/src/features/createTheme.js`, `packages/core/src/features/css.js`, `packages/core/src/features/globalCss.js`, `packages/core/src/features/keyframes.js`, `packages/core/src/index.js`, `packages/core/src/sheet.js`, `packages/core/src/utility/createMemo.js`, `packages/core/src/utility/define.js`, `packages/core/src/utility/getCachedConfig.js`, `packages/core/src/utility/getNonce.js`, `packages/core/src/utility/hasNames.js`, `packages/core/src/utility/hasOwn.js`, `packages/core/src/utility/index.d.ts`, `packages/core/src/utility/internal.js`, `packages/core/types/config.d.ts`, `packages/core/types/css-util.d.ts`, `packages/core/types/index.d.ts`, `packages/core/types/stitches.d.ts`, `packages/core/types/styled-component.d.ts`, `packages/core/types/theme.d.ts`, `packages/core/types/util.d.ts`
- **Evidence:** [packages/core/src/ThemeToken.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/ThemeToken.js); [packages/core/src/convert/toCamelCase.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/convert/toCamelCase.js); [packages/core/src/convert/toCssRules.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/convert/toCssRules.js); [packages/core/src/convert/toHash.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/convert/toHash.js); [packages/core/src/convert/toHyphenCase.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/convert/toHyphenCase.js); [packages/core/src/convert/toPolyfilledValue.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/convert/toPolyfilledValue.js); [packages/core/src/convert/toResolvedMediaQueryRanges.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/convert/toResolvedMediaQueryRanges.js); [packages/core/src/convert/toResolvedSelectors.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/convert/toResolvedSelectors.js)

### Tests (`tests`)

- **Kind:** test
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 79 file(s) under tests (observed from repository paths and static analysis).
- **Paths:** `packages/core/tests/basic.js`, `packages/core/tests/component-composition.js`, `packages/core/tests/component-conditions.js`, `packages/core/tests/component-css-prop.js`, `packages/core/tests/component-empty-variants.js`, `packages/core/tests/component-utils-and-types.js`, `packages/core/tests/component-variants.js`, `packages/core/tests/global-atrules.js`, `packages/core/tests/issue-450.js`, `packages/core/tests/issue-492.js`, `packages/core/tests/issue-652.js`, `packages/core/tests/issue-655.js`, `packages/core/tests/issue-725.js`, `packages/core/tests/issue-788.js`, `packages/core/tests/issue-908.js`, `packages/core/tests/issue-921.ts`, `packages/core/tests/issue-943.js`, `packages/core/tests/issue-999.js`, `packages/core/tests/keyframes.js`, `packages/core/tests/theme.js`, `packages/core/tests/types.test.ts`, `packages/core/tests/universal-autoprefixer.js`, `packages/core/tests/universal-functionality.js`, `packages/core/tests/universal-logical-properties.js`, `packages/core/tests/universal-nesting.js`, `packages/core/tests/universal-numeric-values.js`, `packages/core/tests/universal-polyfill-prefixed-values.js`, `packages/core/tests/universal-prefix.js`, `packages/core/tests/universal-serialization.js`, `packages/core/tests/universal-tokens.js`, `packages/core/tests/universal-with-typing.ts`, `packages/core/tests/utils.js`, `packages/core/tests/with-config-api.js`, `packages/react/tests/basic.js`, `packages/react/tests/component-as-props.js`, `packages/react/tests/component-className-prop.js`, `packages/react/tests/component-composition.js`, `packages/react/tests/component-css-prop-react.js`, `packages/react/tests/component-css-prop.js`, `packages/react/tests/component-repeated-variants.js`, `packages/react/tests/component-variants.js`, `packages/react/tests/component.js`, `packages/react/tests/issue-416.js`, `packages/react/tests/issue-450.js`, `packages/react/tests/issue-555.js`, `packages/react/tests/issue-671-forwardRef.js`, `packages/react/tests/issue-671.js`, `packages/react/tests/issue-737.js`, `packages/react/tests/issue-921.tsx`, `packages/react/tests/issue-943.js`, `packages/react/tests/react.js`, `packages/react/tests/types.test.tsx`, `packages/react/tests/universal-serialization.js`, `packages/react/tests/variants.js`, `packages/react/tests/with-config-api.js`, `packages/stringify/tests/at-rule-font-face.js`, `packages/stringify/tests/at-rule-import.js`, `packages/stringify/tests/at-rule-keyframes.js`, `packages/stringify/tests/index.js`, `packages/stringify/tests/internal-toCase.js`, `packages/stringify/tests/nesting-rules.js`, `packages/stringify/tests/replacer-prefixing.js`, `packages/test/.eslintrc`, `packages/test/Issue-803-core.ts`, `packages/test/Issue-803-react.ts`, `packages/test/Issue-813-core.ts`, `packages/test/Issue-813-react.ts`, `packages/test/built-types/Issue-803-core.d.ts`, `packages/test/built-types/Issue-803-react.d.ts`, `packages/test/built-types/Issue-813-core.d.ts`, `packages/test/built-types/Issue-813-react.d.ts`, `packages/test/built-types/built-types-test.tsx`, `packages/test/built-types/index.d.ts`, `packages/test/built-types/issue-749-react.d.ts`, `packages/test/index.tsx`, `packages/test/issue-749-react.tsx`, `packages/test/package.json`, `packages/test/stitches.config.ts`, `packages/test/tsconfig.json`
- **Evidence:** [packages/core/tests/basic.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/basic.js); [packages/core/tests/component-composition.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/component-composition.js); [packages/core/tests/component-conditions.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/component-conditions.js); [packages/core/tests/component-css-prop.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/component-css-prop.js); [packages/core/tests/component-empty-variants.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/component-empty-variants.js); [packages/core/tests/component-utils-and-types.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/component-utils-and-types.js); [packages/core/tests/component-variants.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/component-variants.js); [packages/core/tests/global-atrules.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/global-atrules.js)

## 5. Execution flow

**Observed** entry point(s):

- [packages/core/src/index.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/index.js)
- [packages/react/src/index.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/src/index.js)
- [packages/stringify/src/index.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/stringify/src/index.js)

Representative flow (derived from observed entry points and the import graph; steps beyond the entry point are **Inferred**):

1. Execution starts at an observed entry point listed above, if present.
2. No internal import relationships between components were observed.

## 6. Project structure

### `(root)`

- `.editorconfig` - config (210 bytes)
- `.gitignore` - other (1692 bytes)
- `CODE_OF_CONDUCT.md` - docs (3350 bytes)
- `CONTRIBUTING.md` - docs (2119 bytes)
- `LICENSE.md` - docs (1063 bytes)
- `README.md` - docs (1985 bytes)
- `package.json` - manifest (3909 bytes)
- `tsconfig.json` - config (397 bytes)
- `tslint.json` - config (1089 bytes)

### `.codesandbox`

- `.codesandbox/ci.json` - config (105 bytes)

### `.github`

- `.github/CODEOWNERS` - other (121 bytes)
- `.github/ISSUE_TEMPLATE/bug_report.md` - docs (765 bytes)
- `.github/ISSUE_TEMPLATE/feature_request.md` - docs (594 bytes)
- `.github/workflows/test.yml` - ci, YAML (279 bytes)

### `.task`

- `.task/build-csstype.js` - source, JavaScript (9868 bytes)
- `.task/build.js` - source, JavaScript (4627 bytes)
- `.task/internal/child_process.js` - source, JavaScript (462 bytes)
- `.task/internal/color.js` - source, JavaScript (2843 bytes)
- `.task/internal/dirs.js` - source, JavaScript (902 bytes)
- `.task/internal/expect.js` - source, JavaScript (2597 bytes)
- `.task/internal/fs-test.js` - source, JavaScript (171 bytes)
- `.task/internal/fs.js` - source, JavaScript (1212 bytes)
- `.task/internal/js.js` - source, JavaScript (7200 bytes)
- `.task/internal/js.transformDestructuring.js` - source, JavaScript (857 bytes)
- `.task/internal/js.transformIIFE.js` - source, JavaScript (891 bytes)
- `.task/internal/js.transformModulesToCJS.js` - source, JavaScript (1353 bytes)
- `.task/internal/js.transformOptionalCatchToParam.js` - source, JavaScript (267 bytes)
- `.task/internal/process.js` - source, JavaScript (590 bytes)
- `.task/internal/readline.js` - source, JavaScript (536 bytes)
- `.task/internal/url.js` - source, JavaScript (812 bytes)
- `.task/lint-esm.js` - source, JavaScript (1396 bytes)
- `.task/lint-pkg.js` - source, JavaScript (1038 bytes)
- `.task/lint-tsc.js` - source, JavaScript (1150 bytes)
- `.task/lint.js` - source, JavaScript (504 bytes)
- `.task/release.js` - source, JavaScript (2046 bytes)
- `.task/test-coverage.js` - source, JavaScript (5952 bytes)
- `.task/test.js` - source, JavaScript (4577 bytes)

### `.vscode`

- `.vscode/package.schema.json` - config (457 bytes)
- `.vscode/settings.json` - config (680 bytes)

### `packages`

- `packages/core/README.md` - docs (2036 bytes)
- `packages/core/package.json` - manifest (1526 bytes)
- `packages/core/src/ThemeToken.js` - source, JavaScript (551 bytes)
- `packages/core/src/convert/toCamelCase.js` - source, JavaScript (211 bytes)
- `packages/core/src/convert/toCssRules.js` - source, JavaScript (6317 bytes)
- `packages/core/src/convert/toHash.js` - source, JavaScript (598 bytes)
- `packages/core/src/convert/toHyphenCase.js` - source, JavaScript (323 bytes)
- `packages/core/src/convert/toPolyfilledValue.js` - source, JavaScript (1631 bytes)
- `packages/core/src/convert/toResolvedMediaQueryRanges.js` - source, JavaScript (1371 bytes)
- `packages/core/src/convert/toResolvedSelectors.js` - source, JavaScript (796 bytes)
- `packages/core/src/convert/toSizingValue.js` - source, JavaScript (975 bytes)
- `packages/core/src/convert/toTailDashed.js` - source, JavaScript (136 bytes)
- `packages/core/src/convert/toTokenizedValue.js` - source, JavaScript (844 bytes)
- `packages/core/src/createStitches.js` - source, JavaScript (1977 bytes)
- `packages/core/src/default/defaultThemeMap.js` - source, JavaScript (8433 bytes)
- `packages/core/src/features/createTheme.js` - source, JavaScript (1979 bytes)
- `packages/core/src/features/css.js` - source, JavaScript (12128 bytes)
- `packages/core/src/features/globalCss.js` - source, JavaScript (1353 bytes)
- `packages/core/src/features/keyframes.js` - source, JavaScript (1273 bytes)
- `packages/core/src/index.js` - source, JavaScript (474 bytes)
- `packages/core/src/sheet.js` - source, JavaScript (6392 bytes)
- `packages/core/src/utility/createMemo.js` - source, JavaScript (428 bytes)
- `packages/core/src/utility/define.js` - source, JavaScript (164 bytes)
- `packages/core/src/utility/getCachedConfig.js` - source, JavaScript (160 bytes)
- `packages/core/src/utility/getNonce.js` - source, JavaScript (195 bytes)
- `packages/core/src/utility/hasNames.js` - source, JavaScript (94 bytes)
- `packages/core/src/utility/hasOwn.js` - source, JavaScript (118 bytes)
- `packages/core/src/utility/index.d.ts` - source, TypeScript (281 bytes)
- `packages/core/src/utility/internal.js` - source, JavaScript (51 bytes)
- `packages/core/tests/basic.js` - test, JavaScript (7459 bytes)
- `packages/core/tests/component-composition.js` - test, JavaScript (1576 bytes)
- `packages/core/tests/component-conditions.js` - test, JavaScript (518 bytes)
- `packages/core/tests/component-css-prop.js` - test, JavaScript (615 bytes)
- `packages/core/tests/component-empty-variants.js` - test, JavaScript (963 bytes)
- `packages/core/tests/component-utils-and-types.js` - test, JavaScript (859 bytes)
- `packages/core/tests/component-variants.js` - test, JavaScript (16099 bytes)
- `packages/core/tests/global-atrules.js` - test, JavaScript (3874 bytes)
- `packages/core/tests/issue-450.js` - test, JavaScript (8469 bytes)
- `packages/core/tests/issue-492.js` - test, JavaScript (3931 bytes)
- `packages/core/tests/issue-652.js` - test, JavaScript (621 bytes)
- `packages/core/tests/issue-655.js` - test, JavaScript (489 bytes)
- `packages/core/tests/issue-725.js` - test, JavaScript (2655 bytes)
- `packages/core/tests/issue-788.js` - test, JavaScript (1056 bytes)
- `packages/core/tests/issue-908.js` - test, JavaScript (814 bytes)
- `packages/core/tests/issue-921.ts` - test, TypeScript (872 bytes)
- `packages/core/tests/issue-943.js` - test, JavaScript (617 bytes)
- `packages/core/tests/issue-999.js` - test, JavaScript (2868 bytes)
- `packages/core/tests/keyframes.js` - test, JavaScript (567 bytes)
- `packages/core/tests/theme.js` - test, JavaScript (1653 bytes)
- `packages/core/tests/types.test.ts` - test, TypeScript (2139 bytes)
- `packages/core/tests/universal-autoprefixer.js` - test, JavaScript (2530 bytes)
- `packages/core/tests/universal-functionality.js` - test, JavaScript (813 bytes)
- `packages/core/tests/universal-logical-properties.js` - test, JavaScript (2178 bytes)
- `packages/core/tests/universal-nesting.js` - test, JavaScript (2342 bytes)
- `packages/core/tests/universal-numeric-values.js` - test, JavaScript (3637 bytes)
- `packages/core/tests/universal-polyfill-prefixed-values.js` - test, JavaScript (640 bytes)
- `packages/core/tests/universal-prefix.js` - test, JavaScript (1295 bytes)
- `packages/core/tests/universal-serialization.js` - test, JavaScript (1976 bytes)
- `packages/core/tests/universal-tokens.js` - test, JavaScript (6995 bytes)
- `packages/core/tests/universal-with-typing.ts` - test, TypeScript (197 bytes)
- `packages/core/tests/utils.js` - test, JavaScript (479 bytes)
- `packages/core/tests/with-config-api.js` - test, JavaScript (5183 bytes)
- `packages/core/types/config.d.ts` - source, TypeScript (5760 bytes)
- `packages/core/types/css-util.d.ts` - source, TypeScript (3508 bytes)
- `packages/core/types/index.d.ts` - source, TypeScript (2706 bytes)
- `packages/core/types/stitches.d.ts` - source, TypeScript (5400 bytes)
- `packages/core/types/styled-component.d.ts` - source, TypeScript (2415 bytes)
- `packages/core/types/theme.d.ts` - source, TypeScript (1213 bytes)
- `packages/core/types/util.d.ts` - source, TypeScript (1035 bytes)
- `packages/react/README.md` - docs (2226 bytes)
- `packages/react/package.json` - manifest (1706 bytes)
- `packages/react/src/createStitches.js` - source, JavaScript (305 bytes)
- `packages/react/src/features/styled.js` - source, JavaScript (1918 bytes)
- `packages/react/src/index.js` - source, JavaScript (556 bytes)
- `packages/react/src/utility/getCachedConfig.js` - source, JavaScript (160 bytes)
- `packages/react/tests/basic.js` - test, JavaScript (1274 bytes)
- `packages/react/tests/component-as-props.js` - test, JavaScript (878 bytes)
- `packages/react/tests/component-className-prop.js` - test, JavaScript (1026 bytes)
- `packages/react/tests/component-composition.js` - test, JavaScript (1339 bytes)
- `packages/react/tests/component-css-prop-react.js` - test, JavaScript (3017 bytes)
- `packages/react/tests/component-css-prop.js` - test, JavaScript (1280 bytes)
- `packages/react/tests/component-repeated-variants.js` - test, JavaScript (797 bytes)
- `packages/react/tests/component-variants.js` - test, JavaScript (12147 bytes)
- `packages/react/tests/component.js` - test, JavaScript (1408 bytes)
- `packages/react/tests/issue-416.js` - test, JavaScript (2340 bytes)
- `packages/react/tests/issue-450.js` - test, JavaScript (4488 bytes)
- `packages/react/tests/issue-555.js` - test, JavaScript (1438 bytes)
- `packages/react/tests/issue-671-forwardRef.js` - test, JavaScript (1006 bytes)
- `packages/react/tests/issue-671.js` - test, JavaScript (830 bytes)
- `packages/react/tests/issue-737.js` - test, JavaScript (1173 bytes)
- `packages/react/tests/issue-921.tsx` - test, TypeScript (1115 bytes)
- `packages/react/tests/issue-943.js` - test, JavaScript (617 bytes)
- `packages/react/tests/react.js` - test, JavaScript (1467 bytes)
- `packages/react/tests/types.test.tsx` - test, TypeScript (3743 bytes)
- `packages/react/tests/universal-serialization.js` - test, JavaScript (1933 bytes)
- `packages/react/tests/variants.js` - test, JavaScript (1452 bytes)
- `packages/react/tests/with-config-api.js` - test, JavaScript (5602 bytes)
- `packages/react/types/config.d.ts` - source, TypeScript (5760 bytes)
- `packages/react/types/css-util.d.ts` - source, TypeScript (3508 bytes)
- `packages/react/types/index.d.ts` - source, TypeScript (2837 bytes)
- `packages/react/types/stitches.d.ts` - source, TypeScript (7761 bytes)
- `packages/react/types/styled-component.d.ts` - source, TypeScript (4181 bytes)
- `packages/react/types/theme.d.ts` - source, TypeScript (1213 bytes)
- `packages/react/types/util.d.ts` - source, TypeScript (1060 bytes)
- `packages/stringify/README.md` - docs (2888 bytes)
- `packages/stringify/package.json` - manifest (989 bytes)
- `packages/stringify/src/Array.js` - source, JavaScript (63 bytes)
- `packages/stringify/src/getResolvedSelectors.js` - source, JavaScript (734 bytes)
- `packages/stringify/src/index.js` - source, JavaScript (2265 bytes)
- `packages/stringify/src/toCase.js` - source, JavaScript (534 bytes)
- `packages/stringify/tests/at-rule-font-face.js` - test, JavaScript (969 bytes)
- `packages/stringify/tests/at-rule-import.js` - test, JavaScript (427 bytes)
- `packages/stringify/tests/at-rule-keyframes.js` - test, JavaScript (434 bytes)
- `packages/stringify/tests/index.js` - test, JavaScript (2436 bytes)
- `packages/stringify/tests/internal-toCase.js` - test, JavaScript (923 bytes)
- `packages/stringify/tests/nesting-rules.js` - test, JavaScript (1802 bytes)
- `packages/stringify/tests/replacer-prefixing.js` - test, JavaScript (910 bytes)
- `packages/stringify/types/index.d.ts` - source, TypeScript (103 bytes)
- `packages/test/.eslintrc` - test (540 bytes)
- `packages/test/Issue-803-core.ts` - test, TypeScript (1239 bytes)
- `packages/test/Issue-803-react.ts` - test, TypeScript (1240 bytes)
- `packages/test/Issue-813-core.ts` - test, TypeScript (1058 bytes)
- `packages/test/Issue-813-react.ts` - test, TypeScript (1073 bytes)
- `packages/test/built-types/Issue-803-core.d.ts` - test, TypeScript (11 bytes)
- `packages/test/built-types/Issue-803-react.d.ts` - test, TypeScript (11 bytes)
- `packages/test/built-types/Issue-813-core.d.ts` - test, TypeScript (2657 bytes)
- `packages/test/built-types/Issue-813-react.d.ts` - test, TypeScript (2686 bytes)
- `packages/test/built-types/built-types-test.tsx` - test, TypeScript (2183 bytes)
- `packages/test/built-types/index.d.ts` - test, TypeScript (28174 bytes)
- `packages/test/built-types/issue-749-react.d.ts` - test, TypeScript (44 bytes)
- `packages/test/index.tsx` - test, TypeScript (2183 bytes)
- `packages/test/issue-749-react.tsx` - test, TypeScript (490 bytes)
- `packages/test/package.json` - test (760 bytes)
- `packages/test/stitches.config.ts` - test, TypeScript (10063 bytes)
- `packages/test/tsconfig.json` - test (533 bytes)

## 7. Key dependencies and integrations

| Name | Category | Status | Confidence | Evidence |
| --- | --- | --- | --- | --- |
| GitHub Actions | ci | Observed | 0.85 | [.github/workflows/test.yml](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/.github/workflows/test.yml) |
| React | framework | Observed | 0.90 | [package.json:26](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/package.json#L26); [packages/react/package.json:2](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/package.json#L2) |
| TypeScript | tooling | Observed | 0.85 | [package.json:38](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/package.json#L38) |

## 8. Data and state

No database, cache, queue, or persistent-state usage was observed in the analysed files. State handling, if any, may be in-memory or in files that were not analysed.

## 9. Configuration and deployment clues

- `.codesandbox/ci.json` (config)
- `.editorconfig` (config)
- `.github/workflows/test.yml` (ci)
- `.vscode/package.schema.json` (config)
- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)
- `packages/react/package.json` (manifest)
- `packages/stringify/package.json` (manifest)
- `tsconfig.json` (config)
- `tslint.json` (config)

## 10. Design observations

- Service/domain code is distinct from entry and data code, suggesting layered separation (Inferred).
- Tests are present alongside source code (Observed from test file paths).

These observations are interpretations (**Inferred**) of the observed structure, not guarantees about runtime design.

## 11. Limitations and unknowns

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

## 12. Source references

- [.github/workflows/test.yml](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/.github/workflows/test.yml)
- [package.json](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/package.json)
- [package.json:26](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/package.json#L26)
- [package.json:38](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/package.json#L38)
- [packages/core/package.json](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/package.json)
- [packages/core/src/ThemeToken.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/ThemeToken.js)
- [packages/core/src/convert/toCamelCase.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/convert/toCamelCase.js)
- [packages/core/src/convert/toCssRules.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/convert/toCssRules.js)
- [packages/core/src/convert/toHash.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/convert/toHash.js)
- [packages/core/src/convert/toHyphenCase.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/convert/toHyphenCase.js)
- [packages/core/src/convert/toPolyfilledValue.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/convert/toPolyfilledValue.js)
- [packages/core/src/convert/toResolvedMediaQueryRanges.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/convert/toResolvedMediaQueryRanges.js)
- [packages/core/src/convert/toResolvedSelectors.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/convert/toResolvedSelectors.js)
- [packages/core/src/index.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/src/index.js)
- [packages/core/tests/basic.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/basic.js)
- [packages/core/tests/component-composition.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/component-composition.js)
- [packages/core/tests/component-conditions.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/component-conditions.js)
- [packages/core/tests/component-css-prop.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/component-css-prop.js)
- [packages/core/tests/component-empty-variants.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/component-empty-variants.js)
- [packages/core/tests/component-utils-and-types.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/component-utils-and-types.js)
- [packages/core/tests/component-variants.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/component-variants.js)
- [packages/core/tests/global-atrules.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/core/tests/global-atrules.js)
- [packages/react/package.json](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/package.json)
- [packages/react/package.json:2](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/package.json#L2)
- [packages/react/src/createStitches.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/src/createStitches.js)
- [packages/react/src/features/styled.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/src/features/styled.js)
- [packages/react/src/index.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/src/index.js)
- [packages/react/src/utility/getCachedConfig.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/src/utility/getCachedConfig.js)
- [packages/react/types/config.d.ts](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/types/config.d.ts)
- [packages/react/types/css-util.d.ts](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/types/css-util.d.ts)
- [packages/react/types/index.d.ts](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/types/index.d.ts)
- [packages/react/types/stitches.d.ts](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/react/types/stitches.d.ts)
- [packages/stringify/package.json](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/stringify/package.json)
- [packages/stringify/src/index.js](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/packages/stringify/src/index.js)
- [tsconfig.json](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/tsconfig.json)
- [tslint.json](https://github.com/stitchesjs/stitches/blob/50fd8a1adc6360340fe348a8b3ebc8b06d38e230/tslint.json)
