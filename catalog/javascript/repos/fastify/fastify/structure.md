# Project structure: fastify/fastify

**Analysed commit:** `7e0c8febb2a1ba4d55309cdc2ccd51694eca46d3`

**Commit reference:** [7e0c8febb2a1ba4d55309cdc2ccd51694eca46d3](https://github.com/fastify/fastify/commit/7e0c8febb2a1ba4d55309cdc2ccd51694eca46d3)

**Tree at this commit:** [fastify/fastify@7e0c8febb2a1](https://github.com/fastify/fastify/tree/7e0c8febb2a1ba4d55309cdc2ccd51694eca46d3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | fastify/fastify |
| Description | Fast and low overhead web framework, for Node.js |
| Stars | 37419 |
| Forks | 3057 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `7e0c8febb2a1ba4d55309cdc2ccd51694eca46d3` |
| Retrieved at | 2026-11-14T19:10:41.688343+00:00 |
| Files in this snapshot | 391 |

## Directory tree

```text
.github/  (24 files)
  scripts/  (1 files)
    lint-ecosystem.js
  workflows/  (20 files)
    backport.yml
    ci-alternative-runtime.yml
    ci.yml
    citgm-package.yml
    citgm.yml
    coverage-nix.yml
    coverage-win.yml
    integration-alternative-runtimes.yml
    integration.yml
    labeler.yml
    links-check.yml
    lint-ecosystem-order.yml
    lock-threads.yml
    md-lint.yml
    missing_types.yml
    package-manager-ci.yml
    pull-request-title.yml
    test-compare.yml
    validate-ecosystem-links.yml
    website.yml
  dependabot.yml
  labeler.yml
  problem-matcher.json
docs/  (44 files)
  Guides/  (20 files)
    Benchmarking.md
    Contributing.md
    Database.md
    Delay-Accepting-Requests.md
    Detecting-When-Clients-Abort.md
    Ecosystem.md
    Fluent-Schema.md
    Getting-Started.md
    Index.md
    Migration-Guide-V3.md
    Migration-Guide-V4.md
    Migration-Guide-V5.md
    Plugins-Guide.md
    Prototype-Poisoning.md
    Recommendations.md
    Serverless.md
    Style-Guide.md
    Testing.md
    Write-Plugin.md
    Write-Type-Provider.md
  Reference/  (21 files)
    ContentTypeParser.md
    Decorators.md
    Encapsulation.md
    Errors.md
    HTTP2.md
    Hooks.md
    Index.md
    LTS.md
    Lifecycle.md
    Logging.md
    Middleware.md
    Plugins.md
    Principles.md
    Reply.md
    Request.md
    Routes.md
    Server.md
    Type-Providers.md
    TypeScript.md
    Validation-and-Serialization.md
    Warnings.md
  resources/  (2 files)
    encapsulation_context.drawio
    encapsulation_context.svg
  index.md
examples/  (19 files)
  benchmark/  (6 files)
    body.json
    hooks-benchmark-async-await.js
    hooks-benchmark.js
    parser.js
    simple.js
    webstream.js
  asyncawait.js
  hooks.js
  http2.js
  https.js
  parser.js
  plugin.js
  route-prefix.js
  shared-schema.js
  simple-stream.js
  simple.js
  simple.mjs
  typescript-server.ts
  use-plugin.js
integration/  (2 files)
  server.js
  test.sh
lib/  (31 files)
  config-validator.js
  content-type-parser.js
  content-type.js
  context.js
  decorate.js
  error-handler.js
  error-serializer.js
  error-status.js
  errors.js
  four-oh-four.js
  handle-request.js
  head-route.js
  hooks.js
  initial-config-validation.js
  log-controller.js
  logger-factory.js
  logger-pino.js
  noop-set.js
  plugin-override.js
  plugin-utils.js
  reply.js
  req-id-gen-factory.js
  request.js
  route.js
  … 7 more files
scripts/  (1 files)
  validate-ecosystem-links.js
test/  (234 files)
  bundler/  (10 files)
    esbuild/  (4 files)
      … 4 files under this directory
    webpack/  (5 files)
      … 5 files under this directory
    README.md
  diagnostics-channel/  (11 files)
    404.test.js
    async-delay-request.test.js
    async-error-handler.test.js
    async-request.test.js
    error-before-handler.test.js
    error-request.test.js
    error-status.test.js
    init.test.js
    sync-delay-request.test.js
    sync-request-reply.test.js
    sync-request.test.js
  esm/  (6 files)
    errorCodes.test.mjs
    esm.test.mjs
    index.test.js
    named-exports.mjs
    other.mjs
    plugin.mjs
  http-methods/  (14 files)
    copy.test.js
    custom-http-methods.test.js
    get.test.js
    head.test.js
    lock.test.js
    mkcalendar.test.js
    mkcol.test.js
    move.test.js
    propfind.test.js
    proppatch.test.js
    report.test.js
    search.test.js
    trace.test.js
    unlock.test.js
  http2/  (7 files)
    closing.test.js
    constraint.test.js
    head.test.js
    plain.test.js
    secure-with-fallback.test.js
    secure.test.js
    unknown-http-method.test.js
  https/  (2 files)
    custom-https-server.test.js
    https.test.js
  internals/  (19 files)
    all.test.js
    content-type-parser.test.js
    context.test.js
    decorator.test.js
    errors.test.js
    handle-request.test.js
    hook-runner.test.js
    hooks.test.js
    initial-config.test.js
    logger.test.js
    plugin.test.js
    reply-serialize.test.js
    reply.test.js
    req-id-gen-factory.test.js
    request-validate.test.js
    request.test.js
    schema-controller-perf.test.js
    server.test.js
    validation.test.js
  logger/  (7 files)
    instantiation.test.js
    logger-test-utils.js
    logging.test.js
    options.test.js
    request.test.js
    response.test.js
    tap-parallel-not-ok
  scripts/  (1 files)
    validate-ecosystem-links.test.js
  types/  (18 files)
    content-type-parser.tst.ts
    decorate-request-reply.tst.ts
    dummy-plugin.mts
    errors.tst.ts
    fastify.tst.ts
    hooks.tst.ts
    instance.tst.ts
    logger.tst.ts
    plugin.tst.ts
    register.tst.ts
    reply.tst.ts
    request.tst.ts
    route.tst.ts
    schema.tst.ts
    serverFactory.tst.ts
    tsconfig.json
    type-provider.tst.ts
    using.tst.ts
  404s.test.js
  500s.test.js
  allow-unsafe-regex.test.js
  als.test.js
  async-await.test.js
  async-dispose.test.js
  async_hooks.test.js
  body-limit.test.js
  buffer.test.js
  build-certificate.js
  case-insensitive.test.js
  chainable.test.js
  child-logger-factory.test.js
  client-timeout.test.js
  close-disposable.test.js
  close-pipelining.test.js
  close.test.js
  conditional-pino.test.js
  connection-timeout.test.js
  constrained-routes.test.js
  content-length.test.js
  content-parser.test.js
  content-type-parser-async-context.test.js
  content-type.test.js
  … 115 more files
types/  (15 files)
  content-type-parser.d.ts
  context.d.ts
  errors.d.ts
  hooks.d.ts
  instance.d.ts
  logger.d.ts
  plugin.d.ts
  register.d.ts
  reply.d.ts
  request.d.ts
  route.d.ts
  schema.d.ts
  server-factory.d.ts
  type-provider.d.ts
  utils.d.ts
.borp.yaml
.editorconfig
.gitattributes
.gitignore
.gitpod.yml
.markdownlint-cli2.yaml
.npmignore
.prettierignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
EXPENSE_POLICY.md
GOVERNANCE.md
LICENSE
PROJECT_CHARTER.md
README.md
SECURITY.md
SPONSORS.md
eslint.config.js
fastify.d.ts
fastify.js
package.json
```

## Entry points

- [fastify.js](https://github.com/fastify/fastify/blob/7e0c8febb2a1ba4d55309cdc2ccd51694eca46d3/fastify.js)
- [integration/server.js](https://github.com/fastify/fastify/blob/7e0c8febb2a1ba4d55309cdc2ccd51694eca46d3/integration/server.js)
- [lib/server.js](https://github.com/fastify/fastify/blob/7e0c8febb2a1ba4d55309cdc2ccd51694eca46d3/lib/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 2 file(s) under external integrations (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 31 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 234 file(s) under tests (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 15 file(s) under types package (observed from repository paths and static analysis). |

## Important files

- `.borp.yaml` (config)
- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/labeler.yml` (config)
- `.github/problem-matcher.json` (config)
- `.github/workflows/backport.yml` (ci)
- `.github/workflows/ci-alternative-runtime.yml` (ci)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/citgm-package.yml` (ci)
- `.github/workflows/citgm.yml` (ci)
- `.github/workflows/coverage-nix.yml` (ci)
- `.github/workflows/coverage-win.yml` (ci)
- `.github/workflows/integration-alternative-runtimes.yml` (ci)
- `.github/workflows/integration.yml` (ci)
- `.github/workflows/labeler.yml` (ci)
- `.github/workflows/links-check.yml` (ci)
- `.github/workflows/lint-ecosystem-order.yml` (ci)
- `.github/workflows/lock-threads.yml` (ci)
- `.github/workflows/md-lint.yml` (ci)
- `.github/workflows/missing_types.yml` (ci)
- `.github/workflows/package-manager-ci.yml` (ci)
- `.github/workflows/pull-request-title.yml` (ci)
- `.github/workflows/test-compare.yml` (ci)
- `.github/workflows/validate-ecosystem-links.yml` (ci)
- `.github/workflows/website.yml` (ci)
- `.gitpod.yml` (config)
- `.markdownlint-cli2.yaml` (config)
- `examples/benchmark/body.json` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 234 analysed file(s)
- `docs` — 44 analysed file(s)
- `lib` — 31 analysed file(s)
- `.github` — 24 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `examples` — 19 analysed file(s)
- `types` — 15 analysed file(s)
- `integration` — 2 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (1 x likely secret file excluded; 5 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `7e0c8febb2a1ba4d55309cdc2ccd51694eca46d3` is the revision these paths and observations refer to.
