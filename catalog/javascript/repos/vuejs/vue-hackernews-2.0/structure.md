# Project structure: vuejs/vue-hackernews-2.0

**Analysed commit:** `98399b55c6f1da4197840ba76189795b3e95be0f`

**Commit reference:** [98399b55c6f1da4197840ba76189795b3e95be0f](https://github.com/vuejs/vue-hackernews-2.0/commit/98399b55c6f1da4197840ba76189795b3e95be0f)

**Tree at this commit:** [vuejs/vue-hackernews-2.0@98399b55c6f1](https://github.com/vuejs/vue-hackernews-2.0/tree/98399b55c6f1da4197840ba76189795b3e95be0f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vuejs/vue-hackernews-2.0 |
| Description | HackerNews clone built with Vue 2.0, vue-router & vuex, with server-side rendering |
| Stars | 10837 |
| Forks | 2102 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `98399b55c6f1da4197840ba76189795b3e95be0f` |
| Retrieved at | 2026-11-14T19:12:30.784583+00:00 |
| Files in this snapshot | 30 |

## Directory tree

```text
src/  (23 files)
  api/  (3 files)
    create-api-client.js
    create-api-server.js
    index.js
  components/  (4 files)
    Comment.vue
    Item.vue
    ProgressBar.vue
    Spinner.vue
  router/  (1 files)
    index.js
  store/  (4 files)
    actions.js
    getters.js
    index.js
    mutations.js
  util/  (2 files)
    filters.js
    title.js
  views/  (4 files)
    CreateListView.js
    ItemList.vue
    ItemView.vue
    UserView.vue
  App.vue
  app.js
  entry-client.js
  entry-server.js
  index.template.html
.babelrc
.gitignore
LICENSE
README.md
manifest.json
package.json
server.js
```

## Entry points

- [server.js](https://github.com/vuejs/vue-hackernews-2.0/blob/98399b55c6f1da4197840ba76189795b3e95be0f/server.js)
- [src/api/index.js](https://github.com/vuejs/vue-hackernews-2.0/blob/98399b55c6f1da4197840ba76189795b3e95be0f/src/api/index.js)
- [src/app.js](https://github.com/vuejs/vue-hackernews-2.0/blob/98399b55c6f1da4197840ba76189795b3e95be0f/src/app.js)
- [src/router/index.js](https://github.com/vuejs/vue-hackernews-2.0/blob/98399b55c6f1da4197840ba76189795b3e95be0f/src/router/index.js)
- [src/store/index.js](https://github.com/vuejs/vue-hackernews-2.0/blob/98399b55c6f1da4197840ba76189795b3e95be0f/src/store/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 7 file(s) under api layer (observed from repository paths and static analysis). |
| app.js package | library | Observed | Groups 1 file(s) under app.js package (observed from repository paths and static analysis). |
| App.vue package | library | Observed | Groups 1 file(s) under app.vue package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 4 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| entry-client.js package | library | Observed | Groups 1 file(s) under entry-client.js package (observed from repository paths and static analysis). |
| entry-server.js package | library | Observed | Groups 1 file(s) under entry-server.js package (observed from repository paths and static analysis). |
| router package | library | Observed | Groups 1 file(s) under router package (observed from repository paths and static analysis). |
| store package | library | Observed | Groups 4 file(s) under store package (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 2 file(s) under util package (observed from repository paths and static analysis). |

## Important files

- `manifest.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 23 analysed file(s)
- `(root files)` — 7 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 4 file(s) were skipped during inventory (4 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `98399b55c6f1da4197840ba76189795b3e95be0f` is the revision these paths and observations refer to.
