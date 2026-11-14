# Project structure: expressjs/express

**Analysed commit:** `43fca52d28a422c8be48fd489cbd4f2d6152bab6`

**Commit reference:** [43fca52d28a422c8be48fd489cbd4f2d6152bab6](https://github.com/expressjs/express/commit/43fca52d28a422c8be48fd489cbd4f2d6152bab6)

**Tree at this commit:** [expressjs/express@43fca52d28a4](https://github.com/expressjs/express/tree/43fca52d28a422c8be48fd489cbd4f2d6152bab6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | expressjs/express |
| Description | Fast, unopinionated, minimalist web framework for node. |
| Stars | 69674 |
| Forks | 25443 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `43fca52d28a422c8be48fd489cbd4f2d6152bab6` |
| Retrieved at | 2026-11-14T19:10:33.991659+00:00 |
| Files in this snapshot | 215 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (5 files)
    ci.yml
    codeql.yml
    legacy.yml
    npm-publish.yml
    scorecard.yml
  dependabot.yml
examples/  (80 files)
  auth/  (4 files)
    views/  (3 files)
      … 3 files under this directory
    index.js
  content-negotiation/  (3 files)
    db.js
    index.js
    users.js
  cookie-sessions/  (1 files)
    index.js
  cookies/  (1 files)
    index.js
  downloads/  (4 files)
    files/  (3 files)
      … 3 files under this directory
    index.js
  ejs/  (5 files)
    public/  (1 files)
      … 1 files under this directory
    views/  (3 files)
      … 3 files under this directory
    index.js
  error/  (1 files)
    index.js
  error-pages/  (6 files)
    views/  (5 files)
      … 5 files under this directory
    index.js
  hello-world/  (1 files)
    index.js
  markdown/  (2 files)
    views/  (1 files)
      … 1 files under this directory
    index.js
  multi-router/  (3 files)
    controllers/  (2 files)
      … 2 files under this directory
    index.js
  mvc/  (15 files)
    controllers/  (9 files)
      … 9 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    public/  (1 files)
      … 1 files under this directory
    views/  (2 files)
      … 2 files under this directory
    db.js
    index.js
  online/  (1 files)
    index.js
  params/  (1 files)
    index.js
  resource/  (1 files)
    index.js
  route-map/  (1 files)
    index.js
  route-middleware/  (1 files)
    index.js
  route-separation/  (12 files)
    public/  (1 files)
      … 1 files under this directory
    views/  (7 files)
      … 7 files under this directory
    index.js
    post.js
    site.js
    user.js
  search/  (3 files)
    public/  (2 files)
      … 2 files under this directory
    index.js
  session/  (2 files)
    index.js
    redis.js
  static-files/  (4 files)
    public/  (3 files)
      … 3 files under this directory
    index.js
  vhost/  (1 files)
    index.js
  view-constructor/  (2 files)
    github-view.js
    index.js
  view-locals/  (3 files)
    views/  (1 files)
      … 1 files under this directory
    index.js
    user.js
  web-service/  (1 files)
    index.js
  README.md
lib/  (6 files)
  application.js
  express.js
  request.js
  response.js
  utils.js
  view.js
test/  (114 files)
  acceptance/  (18 files)
    auth.js
    content-negotiation.js
    cookie-sessions.js
    cookies.js
    downloads.js
    ejs.js
    error-pages.js
    error.js
    hello-world.js
    markdown.js
    multi-router.js
    mvc.js
    params.js
    resource.js
    route-map.js
    route-separation.js
    vhost.js
    web-service.js
  fixtures/  (22 files)
    blog/  (2 files)
      … 2 files under this directory
    default_layout/  (2 files)
      … 2 files under this directory
    local_layout/  (1 files)
      … 1 files under this directory
    pets/  (1 files)
      … 1 files under this directory
    snow ☃/  (1 files)
      … 1 files under this directory
    users/  (2 files)
      … 2 files under this directory
    % of dogs.txt
    .name
    broken.send
    email.tmpl
    empty.txt
    name.tmpl
    name.txt
    nums.txt
    todo.html
    todo.txt
    user.ejs
    user.html
    user.tmpl
  support/  (3 files)
    env.js
    tmpl.js
    utils.js
  Route.js
  Router.js
  app.all.js
  app.engine.js
  app.head.js
  app.js
  app.listen.js
  app.locals.js
  app.options.js
  app.param.js
  app.render.js
  app.request.js
  app.response.js
  app.route.js
  app.router.js
  app.routes.error.js
  app.use.js
  config.js
  exports.js
  express.json.js
  express.raw.js
  express.static.js
  express.text.js
  express.urlencoded.js
  … 47 more files
.editorconfig
.eslintignore
.eslintrc.yml
.gitignore
History.md
LICENSE
Readme.md
index.js
package.json
```

## Entry points

- [index.js](https://github.com/expressjs/express/blob/43fca52d28a422c8be48fd489cbd4f2d6152bab6/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 6 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 114 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.eslintrc.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/legacy.yml` (ci)
- `.github/workflows/npm-publish.yml` (ci)
- `.github/workflows/scorecard.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `test` — 114 analysed file(s)
- `examples` — 80 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 6 analysed file(s)
- `lib` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `43fca52d28a422c8be48fd489cbd4f2d6152bab6` is the revision these paths and observations refer to.
