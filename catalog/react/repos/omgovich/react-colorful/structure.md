# Project structure: omgovich/react-colorful

**Analysed commit:** `5f665a8bbfd735af8a1a4a9ae482b5b54c47c825`

**Commit reference:** [5f665a8bbfd735af8a1a4a9ae482b5b54c47c825](https://github.com/omgovich/react-colorful/commit/5f665a8bbfd735af8a1a4a9ae482b5b54c47c825)

**Tree at this commit:** [omgovich/react-colorful@5f665a8bbfd7](https://github.com/omgovich/react-colorful/tree/5f665a8bbfd735af8a1a4a9ae482b5b54c47c825)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | omgovich/react-colorful |
| Description | 🎨 A tiny (3,1 KB) color picker component for React and Preact apps |
| Stars | 3565 |
| Forks | 125 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `5f665a8bbfd735af8a1a4a9ae482b5b54c47c825` |
| Retrieved at | 2026-11-14T19:15:14.438060+00:00 |
| Files in this snapshot | 73 |

## Directory tree

```text
.changeset/  (3 files)
  README.md
  changelog.mjs
  config.json
.github/  (4 files)
  workflows/  (3 files)
    node.yml
    release.yml
    size.yml
  FUNDING.yml
demo/  (11 files)
  src/  (11 files)
    components/  (4 files)
      … 4 files under this directory
    hooks/  (4 files)
      … 4 files under this directory
    index.html
    index.tsx
    styles.ts
src/  (38 files)
  components/  (23 files)
    common/  (8 files)
      … 8 files under this directory
    HexAlphaColorPicker.tsx
    HexColorInput.tsx
    HexColorPicker.tsx
    HslColorPicker.tsx
    HslStringColorPicker.tsx
    HslaColorPicker.tsx
    HslaStringColorPicker.tsx
    HsvColorPicker.tsx
    HsvStringColorPicker.tsx
    HsvaColorPicker.tsx
    HsvaStringColorPicker.tsx
    RgbColorPicker.tsx
    RgbStringColorPicker.tsx
    RgbaColorPicker.tsx
    RgbaStringColorPicker.tsx
  css/  (2 files)
    styles.css
    styles.css.d.ts
  hooks/  (4 files)
    useColorManipulation.ts
    useEventCallback.ts
    useIsomorphicLayoutEffect.ts
    useStyleSheet.ts
  utils/  (7 files)
    clamp.ts
    compare.ts
    convert.ts
    format.ts
    nonce.ts
    round.ts
    validate.ts
  index.ts
  types.ts
tests/  (6 files)
  __mocks__/  (1 files)
    styles.css.mock.ts
  __snapshots__/  (1 files)
    components.test.js.snap
  components.test.js
  csp.test.js
  shadowDom.test.js
  utils.test.js
.eslintrc
.gitignore
.prettierrc
ACKNOWLEDGMENTS
CHANGELOG.md
CLAUDE.md
LICENSE
README.md
package.json
tsconfig.build.json
tsconfig.json
```

## Entry points

- [demo/src/index.tsx](https://github.com/omgovich/react-colorful/blob/5f665a8bbfd735af8a1a4a9ae482b5b54c47c825/demo/src/index.tsx)
- [src/index.ts](https://github.com/omgovich/react-colorful/blob/5f665a8bbfd735af8a1a4a9ae482b5b54c47c825/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 23 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| css package | library | Observed | Groups 1 file(s) under css package (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 10 file(s) under demo package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 4 file(s) under hooks package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |
| types.ts package | library | Observed | Groups 1 file(s) under types.ts package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 7 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/node.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/size.yml` (ci)
- `package.json` (manifest)
- `tsconfig.build.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 38 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `demo` — 11 analysed file(s)
- `tests` — 6 analysed file(s)
- `.github` — 4 analysed file(s)
- `.changeset` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `5f665a8bbfd735af8a1a4a9ae482b5b54c47c825` is the revision these paths and observations refer to.
