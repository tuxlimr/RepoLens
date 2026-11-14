# Project structure: forwardemail/superagent

**Analysed commit:** `d26bf6ae1a181a00dc71b756d03e8120b92207c4`

**Commit reference:** [d26bf6ae1a181a00dc71b756d03e8120b92207c4](https://github.com/forwardemail/superagent/commit/d26bf6ae1a181a00dc71b756d03e8120b92207c4)

**Tree at this commit:** [forwardemail/superagent@d26bf6ae1a18](https://github.com/forwardemail/superagent/tree/d26bf6ae1a181a00dc71b756d03e8120b92207c4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | forwardemail/superagent |
| Description | Ajax for Node.js and browsers (JS HTTP client). Maintained for @forwardemail, @ladjs, @spamscanner, @breejs, @cabinjs, and @lassjs. |
| Stars | 16638 |
| Forks | 1326 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `d26bf6ae1a181a00dc71b756d03e8120b92207c4` |
| Retrieved at | 2026-11-14T19:11:30.987994+00:00 |
| Files in this snapshot | 113 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
.husky/  (2 files)
  commit-msg
  pre-commit
ci/  (1 files)
  remove-deps-4-old-node.js
docs/  (8 files)
  ko_KR/  (2 files)
    index.html
    index.md
  zh_CN/  (2 files)
    index.html
    index.md
  head.html
  index.md
  style.css
  tail.html
examples/  (1 files)
  simple-get.js
src/  (16 files)
  node/  (11 files)
    parsers/  (5 files)
      … 5 files under this directory
    agent.js
    decompress.js
    http2wrapper.js
    index.js
    response.js
    unzip.js
  agent-base.js
  client.js
  request-base.js
  response-base.js
  utils.js
test/  (58 files)
  client/  (3 files)
    request.js
    serialize.js
    xdomain.js
  node/  (37 files)
    fixtures/  (5 files)
      … 5 files under this directory
    agency.js
    basic-auth.js
    basic.js
    buffers.js
    exports.js
    flags.js
    form.js
    http2.js
    https.js
    image.js
    incoming-multipart.js
    inflate.js
    lookup.js
    multipart.js
    network-error.js
    not-modified.js
    parsers.js
    pipe-callback.js
    pipe-redirect.js
    pipe.js
    query.js
    redirects-other-host.js
    redirects.js
    request-dispose.js
    … 8 more files
  support/  (8 files)
    express/  (4 files)
      … 4 files under this directory
    blank.js
    client.js
    server.js
    setup.js
  agent-base.js
  basic.js
  content-type.js
  form.js
  json.js
  redirects.js
  request.js
  retry.js
  timeout.js
  use.js
.browserslistrc
.commitlintrc.js
.dist.babelrc
.dist.eslintrc
.editorconfig
.eslintrc
.gitattributes
.gitignore
.lib.babelrc
.lib.eslintrc
.lintstagedrc.js
.prettierrc.js
.remarkignore
.remarkrc.js
.test.babelrc
.travis.yml
.xo-config.js
.zuul.yml
CONTRIBUTING.md
HISTORY.md
LICENSE
Makefile
README.md
SECURITY.md
… 2 more files
```

## Entry points

- [src/node/index.js](https://github.com/forwardemail/superagent/blob/d26bf6ae1a181a00dc71b756d03e8120b92207c4/src/node/index.js)
- [src/node/parsers/index.js](https://github.com/forwardemail/superagent/blob/d26bf6ae1a181a00dc71b756d03e8120b92207c4/src/node/parsers/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| agent-base.js package | library | Observed | Groups 1 file(s) under agent-base.js package (observed from repository paths and static analysis). |
| ci package | library | Observed | Groups 1 file(s) under ci package (observed from repository paths and static analysis). |
| client.js package | library | Observed | Groups 1 file(s) under client.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| node package | library | Observed | Groups 11 file(s) under node package (observed from repository paths and static analysis). |
| request-base.js package | library | Observed | Groups 1 file(s) under request-base.js package (observed from repository paths and static analysis). |
| response-base.js package | library | Observed | Groups 1 file(s) under response-base.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 58 file(s) under tests (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/ci.yml` (ci)
- `.travis.yml` (ci)
- `.zuul.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 58 analysed file(s)
- `(root files)` — 26 analysed file(s)
- `src` — 16 analysed file(s)
- `docs` — 8 analysed file(s)
- `.husky` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `ci` — 1 analysed file(s)
- `examples` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (5 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `d26bf6ae1a181a00dc71b756d03e8120b92207c4` is the revision these paths and observations refer to.
