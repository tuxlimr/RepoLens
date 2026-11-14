# Project structure: learnapollo/learnapollo

**Analysed commit:** `dea1677ead6ed590599f9f29b69215d49ea6a0a9`

**Commit reference:** [dea1677ead6ed590599f9f29b69215d49ea6a0a9](https://github.com/learnapollo/learnapollo/commit/dea1677ead6ed590599f9f29b69215d49ea6a0a9)

**Tree at this commit:** [learnapollo/learnapollo@dea1677ead6e](https://github.com/learnapollo/learnapollo/tree/dea1677ead6ed590599f9f29b69215d49ea6a0a9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | learnapollo/learnapollo |
| Description | 👩🏻‍🏫   Learn Apollo - A hands-on tutorial for Apollo GraphQL Client (created by Graphcool) |
| Stars | 5143 |
| Forks | 63 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `dea1677ead6ed590599f9f29b69215d49ea6a0a9` |
| Retrieved at | 2026-11-14T19:14:28.189902+00:00 |
| Files in this snapshot | 101 |

## Directory tree

```text
content/  (26 files)
  excursions/  (2 files)
    excursion-01.md
    excursion-02.md
  go-further/  (1 files)
    wrap-up.md
  introduction/  (2 files)
    get-started-bottom.md
    get-started.md
  tutorial-angular/  (1 files)
    angular-playground.md
  tutorial-ios/  (6 files)
    ios-01.md
    ios-02.md
    ios-03.md
    ios-04.md
    ios-05.md
    ios-06.md
  tutorial-react/  (7 files)
    react-01.md
    react-02.md
    react-03.md
    react-04.md
    react-05.md
    react-06.md
    react-07.md
  tutorial-react-native/  (6 files)
    react-native-01.md
    react-native-02.md
    react-native-03.md
    react-native-04.md
    react-native-05.md
    react-native-06.md
  tutorial-vue/  (1 files)
    vue-playground.md
src/  (59 files)
  assets/  (17 files)
    icons/  (17 files)
      … 17 files under this directory
  components/  (23 files)
    App/  (3 files)
      … 3 files under this directory
    BrowserRow/  (2 files)
      … 2 files under this directory
    BrowserView/  (2 files)
      … 2 files under this directory
    ContentEndpoint/  (2 files)
      … 2 files under this directory
    Download/  (2 files)
      … 2 files under this directory
    Loading/  (2 files)
      … 2 files under this directory
    Markdown/  (2 files)
      … 2 files under this directory
    ServerLayover/  (1 files)
      … 1 files under this directory
    SetTrack/  (2 files)
      … 2 files under this directory
    SharePanel/  (2 files)
      … 2 files under this directory
    Sharing/  (2 files)
      … 2 files under this directory
    TrackLink/  (1 files)
      … 1 files under this directory
  mutations/  (3 files)
    AddPokemonMutation.ts
    DeletePokemonMutation.ts
    UpdatePokemonMutation.ts
  pages/  (4 files)
    landing/  (2 files)
      … 2 files under this directory
    markdown/  (2 files)
      … 2 files under this directory
  utils/  (8 files)
    content.ts
    dom.ts
    events.ts
    location.tsx
    markdown.ts
    smooch.ts
    statestore.ts
    string.ts
  index.html
  index.tsx
  polyfill.ts
  routes.tsx
static/  (3 files)
  _redirects
  humans.txt
  robots.txt
.babelrc
.gitignore
CONTRIBUTING.md
LICENSE
README.md
circle.yml
custom.d.ts
package.json
prep.ts
tsconfig.json
tslint.json
webpack.config.build.js
webpack.config.js
```

## Entry points

- [src/components/App/App.tsx](https://github.com/learnapollo/learnapollo/blob/dea1677ead6ed590599f9f29b69215d49ea6a0a9/src/components/App/App.tsx)
- [src/index.tsx](https://github.com/learnapollo/learnapollo/blob/dea1677ead6ed590599f9f29b69215d49ea6a0a9/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 12 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| mutations package | library | Observed | Groups 3 file(s) under mutations package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 2 file(s) under pages package (observed from repository paths and static analysis). |
| polyfill.ts package | library | Observed | Groups 1 file(s) under polyfill.ts package (observed from repository paths and static analysis). |
| routes.tsx package | library | Observed | Groups 1 file(s) under routes.tsx package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 8 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `circle.yml` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `tslint.json` (config)

## Top-level layout

- `src` — 59 analysed file(s)
- `content` — 26 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `static` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `dea1677ead6ed590599f9f29b69215d49ea6a0a9` is the revision these paths and observations refer to.
