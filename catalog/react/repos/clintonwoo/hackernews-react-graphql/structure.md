# Project structure: clintonwoo/hackernews-react-graphql

**Analysed commit:** `6875c7233c2e0d82a910f8427c8d230f0858d048`

**Commit reference:** [6875c7233c2e0d82a910f8427c8d230f0858d048](https://github.com/clintonwoo/hackernews-react-graphql/commit/6875c7233c2e0d82a910f8427c8d230f0858d048)

**Tree at this commit:** [clintonwoo/hackernews-react-graphql@6875c7233c2e](https://github.com/clintonwoo/hackernews-react-graphql/tree/6875c7233c2e0d82a910f8427c8d230f0858d048)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | clintonwoo/hackernews-react-graphql |
| Description | Hacker News clone rewritten with universal JavaScript, using React and GraphQL. |
| Stars | 4444 |
| Forks | 545 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `6875c7233c2e0d82a910f8427c8d230f0858d048` |
| Retrieved at | 2026-11-14T19:14:45.552081+00:00 |
| Files in this snapshot | 154 |

## Directory tree

```text
docs/  (1 files)
  README.md
pages/  (37 files)
  active.tsx
  ask.tsx
  best.tsx
  bestcomments.tsx
  bookmarklet.tsx
  changepw.tsx
  dmca.tsx
  favorites.tsx
  forgot.tsx
  formatdoc.tsx
  front.tsx
  hidden.tsx
  index.tsx
  item.tsx
  jobs.tsx
  leaders.tsx
  lists.tsx
  login.tsx
  newcomments.tsx
  newest.tsx
  newpoll.tsx
  newsfaq.tsx
  newsguidelines.tsx
  newswelcome.tsx
  … 13 more files
public/  (5 files)
  static/  (4 files)
    README.md
    dmca.css
    news.css
    yc.css
  robots.txt
server/  (13 files)
  database/  (3 files)
    cache-warmer.ts
    cache.ts
    database.ts
  services/  (6 files)
    comment-service.spec.ts
    comment-service.ts
    feed-service.ts
    news-item-service.spec.ts
    news-item-service.ts
    user-service.ts
  graphql-resolvers.spec.ts
  graphql-resolvers.ts
  graphql-schema.ts
  server.ts
src/  (79 files)
  @types/  (1 files)
    global.ts
  __tests__/  (33 files)
    active.spec.tsx
    ask.spec.tsx
    best.spec.tsx
    bestcomments.spec.tsx
    bookmarklet.spec.tsx
    changepw.spec.tsx
    dmca.spec.tsx
    formatdoc.spec.tsx
    front.spec.tsx
    hidden.spec.tsx
    index.spec.tsx
    item.spec.tsx
    jobs.spec.tsx
    leaders.spec.tsx
    lists.spec.tsx
    login.spec.tsx
    newcomments.spec.tsx
    newest.spec.tsx
    newpoll.spec.tsx
    newsfaq.spec.tsx
    newsguidelines.spec.tsx
    newswelcome.spec.tsx
    noobcomments.spec.tsx
    noobstories.spec.tsx
    … 9 more files
  components/  (21 files)
    __snapshots__/  (5 files)
      … 5 files under this directory
    comment-box.spec.tsx
    comment-box.tsx
    comment.spec.tsx
    comment.tsx
    comments.tsx
    footer.tsx
    header-nav.tsx
    header.tsx
    loading-spinner.tsx
    news-detail.spec.tsx
    news-detail.tsx
    news-feed.spec.tsx
    news-feed.tsx
    news-item-with-comments.tsx
    news-title.spec.tsx
    news-title.tsx
  data/  (12 files)
    models/  (5 files)
      … 5 files under this directory
    mutations/  (3 files)
      … 3 files under this directory
    queries/  (1 files)
      … 1 files under this directory
    validation/  (2 files)
      … 2 files under this directory
    sample-data.ts
  helpers/  (7 files)
    convert-number-to-time-ago.spec.ts
    convert-number-to-time-ago.ts
    hash-password.ts
    init-apollo.tsx
    is-valid-url.ts
    user-login-error-code.ts
    with-data.tsx
  layouts/  (3 files)
    blank-layout.tsx
    main-layout.tsx
    notice-layout.tsx
  README.md
  config.ts
.dockerignore
.eslintrc.js
.gitattributes
.gitignore
.prettierignore
Dockerfile
LICENSE
README.md
babel.config.js
healthcheck.js
jest-setup.js
jest.config.js
next-env.d.ts
next.config.js
nodemon.json
package.json
prettier.config.js
tsconfig-server.json
tsconfig.json
```

## Entry points

- [pages/index.tsx](https://github.com/clintonwoo/hackernews-react-graphql/blob/6875c7233c2e0d82a910f8427c8d230f0858d048/pages/index.tsx)
- [server/server.ts](https://github.com/clintonwoo/hackernews-react-graphql/blob/6875c7233c2e0d82a910f8427c8d230f0858d048/server/server.ts)
- [src/data/models/index.ts](https://github.com/clintonwoo/hackernews-react-graphql/blob/6875c7233c2e0d82a910f8427c8d230f0858d048/src/data/models/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 16 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config.ts package | library | Observed | Groups 1 file(s) under config.ts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 15 file(s) under data layer (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 7 file(s) under helpers package (observed from repository paths and static analysis). |
| layouts package | library | Observed | Groups 3 file(s) under layouts package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 37 file(s) under pages package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 4 file(s) under server package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 6 file(s) under service / domain layer (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 33 file(s) under __tests__ package (observed from repository paths and static analysis). |
| @types package | library | Observed | Groups 1 file(s) under @types package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `Dockerfile` (container)
- `nodemon.json` (config)
- `package.json` (manifest)
- `tsconfig-server.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 79 analysed file(s)
- `pages` — 37 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `server` — 13 analysed file(s)
- `public` — 5 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6875c7233c2e0d82a910f8427c8d230f0858d048` is the revision these paths and observations refer to.
