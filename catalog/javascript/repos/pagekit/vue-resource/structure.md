# Project structure: pagekit/vue-resource

**Analysed commit:** `1b2d0c94e0b5b4efbbbb136987401423b84e8cba`

**Commit reference:** [1b2d0c94e0b5b4efbbbb136987401423b84e8cba](https://github.com/pagekit/vue-resource/commit/1b2d0c94e0b5b4efbbbb136987401423b84e8cba)

**Tree at this commit:** [pagekit/vue-resource@1b2d0c94e0b5](https://github.com/pagekit/vue-resource/tree/1b2d0c94e0b5b4efbbbb136987401423b84e8cba)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pagekit/vue-resource |
| Description | The HTTP client for Vue.js |
| Stars | 9965 |
| Forks | 1559 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | develop |
| Analysed commit | `1b2d0c94e0b5b4efbbbb136987401423b84e8cba` |
| Retrieved at | 2026-11-14T19:12:46.756875+00:00 |
| Files in this snapshot | 58 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (1 files)
  ISSUE_TEMPLATE.md
docs/  (6 files)
  README.md
  api.md
  config.md
  http.md
  recipes.md
  resource.md
src/  (26 files)
  http/  (16 files)
    client/  (5 files)
      … 5 files under this directory
    interceptor/  (7 files)
      … 7 files under this directory
    headers.js
    index.js
    request.js
    response.js
  lib/  (2 files)
    promise.js
    url-template.js
  url/  (4 files)
    index.js
    query.js
    root.js
    template.js
  index.js
  promise.js
  resource.js
  util.js
test/  (12 files)
  data/  (3 files)
    invalid.json
    text.txt
    valid.json
  http.js
  http.test.js
  index.html
  index.js
  karma.conf.js
  promise.js
  resource.js
  url.js
  webpack.config.js
types/  (3 files)
  index.d.ts
  vue.d.ts
  vue_resource.ts
.babelrc.js
.eslintignore
.eslintrc.js
.gitignore
.npmignore
LICENSE
README.md
bower.json
package.json
```

## Entry points

- [src/http/client/index.js](https://github.com/pagekit/vue-resource/blob/1b2d0c94e0b5b4efbbbb136987401423b84e8cba/src/http/client/index.js)
- [src/http/index.js](https://github.com/pagekit/vue-resource/blob/1b2d0c94e0b5b4efbbbb136987401423b84e8cba/src/http/index.js)
- [src/index.js](https://github.com/pagekit/vue-resource/blob/1b2d0c94e0b5b4efbbbb136987401423b84e8cba/src/index.js)
- [src/url/index.js](https://github.com/pagekit/vue-resource/blob/1b2d0c94e0b5b4efbbbb136987401423b84e8cba/src/url/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 5 file(s) under external integrations (observed from repository paths and static analysis). |
| http package | library | Observed | Groups 11 file(s) under http package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 2 file(s) under lib package (observed from repository paths and static analysis). |
| promise.js package | library | Observed | Groups 1 file(s) under promise.js package (observed from repository paths and static analysis). |
| resource.js package | library | Observed | Groups 1 file(s) under resource.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 12 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 3 file(s) under types package (observed from repository paths and static analysis). |
| url package | library | Observed | Groups 4 file(s) under url package (observed from repository paths and static analysis). |
| util.js package | library | Observed | Groups 1 file(s) under util.js package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `bower.json` (config)
- `package.json` (manifest)

## Top-level layout

- `src` — 26 analysed file(s)
- `test` — 12 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `docs` — 6 analysed file(s)
- `types` — 3 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (6 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `1b2d0c94e0b5b4efbbbb136987401423b84e8cba` is the revision these paths and observations refer to.
