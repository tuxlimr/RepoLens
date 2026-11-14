# Project structure: andrewyng/context-hub

**Analysed commit:** `67dcbeb2eb42c808549f08397920ad58be7c2206`

**Commit reference:** [67dcbeb2eb42c808549f08397920ad58be7c2206](https://github.com/andrewyng/context-hub/commit/67dcbeb2eb42c808549f08397920ad58be7c2206)

**Tree at this commit:** [andrewyng/context-hub@67dcbeb2eb42](https://github.com/andrewyng/context-hub/tree/67dcbeb2eb42c808549f08397920ad58be7c2206)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | andrewyng/context-hub |
| Description | Not provided |
| Stars | 13985 |
| Forks | 1206 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `67dcbeb2eb42c808549f08397920ad58be7c2206` |
| Retrieved at | 2026-11-14T19:11:48.434757+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (3 files)
    ci.yml
    deploy-content.yml
    publish.yml
  PULL_REQUEST_TEMPLATE.md
cli/  (71 files)
  bin/  (2 files)
    chub
    chub-mcp
  skills/  (1 files)
    get-api-docs/  (1 files)
      … 1 files under this directory
  src/  (27 files)
    commands/  (8 files)
      … 8 files under this directory
    lib/  (15 files)
      … 15 files under this directory
    mcp/  (3 files)
      … 3 files under this directory
    index.js
  test/  (12 files)
    fixtures/  (8 files)
      … 8 files under this directory
    lib/  (3 files)
      … 3 files under this directory
    e2e.test.js
  tests/  (26 files)
    commands/  (8 files)
      … 8 files under this directory
    lib/  (16 files)
      … 16 files under this directory
    mcp/  (2 files)
      … 2 files under this directory
  .npmignore
  README.md
  package.json
content/  (716 files)
  accelerate/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  aiofiles/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  aiohttp/  (2 files)
    docs/  (2 files)
      … 2 files under this directory
  aiohttp-cors/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  aiomysql/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  aiosignal/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  aiosqlite/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  airtable/  (2 files)
    docs/  (2 files)
      … 2 files under this directory
  albumentations/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  alembic/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  altair/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  amplitude/  (2 files)
    docs/  (2 files)
      … 2 files under this directory
  amqp/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  angular/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  annotated-types/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  ansible/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  antd/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  anthropic/  (3 files)
    docs/  (3 files)
      … 3 files under this directory
  anyio/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  apache-airflow/  (91 files)
    docs/  (91 files)
      … 91 files under this directory
  apache-beam/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  appdirs/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  applitools/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  apscheduler/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  ariadne/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  arq/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  arrow/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  asana/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  assemblyai/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  astro/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  async-timeout/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  asyncpg/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  atlassian/  (2 files)
    docs/  (2 files)
      … 2 files under this directory
  attrs/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  auth0/  (2 files)
    docs/  (2 files)
      … 2 files under this directory
  authlib/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  autogen/  (3 files)
    docs/  (3 files)
      … 3 files under this directory
  autopep8/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  av/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  aws/  (236 files)
    docs/  (236 files)
      … 236 files under this directory
  axios/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  azure/  (133 files)
    docs/  (133 files)
      … 133 files under this directory
  babel/  (41 files)
    docs/  (41 files)
      … 41 files under this directory
  backoff/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  bandit/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  bcrypt/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  beautifulsoup4/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  bentoml/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  billiard/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  binance/  (2 files)
    docs/  (2 files)
      … 2 files under this directory
  bitsandbytes/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  black/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  bokeh/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  bottle/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  braintree/  (2 files)
    docs/  (2 files)
      … 2 files under this directory
  cachetools/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cairosvg/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  camelot-py/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cartopy/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cassandra-driver/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  catboost/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cattrs/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cbor2/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  celery/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cerberus/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  certifi/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cffi/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cfgv/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  chalk/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  charset-normalizer/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  chokidar/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  chromadb/  (3 files)
    docs/  (3 files)
      … 3 files under this directory
  clearml/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  clerk/  (2 files)
    docs/  (2 files)
      … 2 files under this directory
  click/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  click-plugins/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  clickhouse-connect/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cloudflare/  (4 files)
    docs/  (4 files)
      … 4 files under this directory
  cloudpickle/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cockroachdb/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cohere/  (2 files)
    docs/  (2 files)
      … 2 files under this directory
  colorama/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  colorlog/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  comet-ml/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  commander/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  commitizen/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  confluent-kafka/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cookiecutter/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  copier/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  crewai/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  croniter/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cryptography/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cssselect/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cypress/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cython/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  cytoolz/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  dagster/  (25 files)
    docs/  (25 files)
      … 25 files under this directory
  dash/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  dask/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  databases/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  dataclasses-json/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  datadog/  (3 files)
    docs/  (3 files)
      … 3 files under this directory
  datahub/  (5 files)
    docs/  (5 files)
      … 5 files under this directory
  datasets/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  datashader/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  dateparser/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  dbt-core/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  debug/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  decorator/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  deepgram/  (2 files)
    docs/  (2 files)
      … 2 files under this directory
  deepl/  (2 files)
    docs/  (2 files)
      … 2 files under this directory
  deepseek/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  deepspeed/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  deprecated/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  detect-secrets/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  devise/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  diffusers/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  dill/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  directus/  (2 files)
    docs/  (2 files)
      … 2 files under this directory
  dirty-equals/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  discord/  (2 files)
    docs/  (2 files)
      … 2 files under this directory
  diskcache/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  django/  (40 files)
    docs/  (40 files)
      … 40 files under this directory
  dlt/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  docker/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  docling/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  docutils/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
  dramatiq/  (1 files)
    docs/  (1 files)
      … 1 files under this directory
.gitignore
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
```

## Entry points

- [cli/bin/chub](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/cli/bin/chub)
- [cli/bin/chub-mcp](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/cli/bin/chub-mcp)
- [cli/src/index.js](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/cli/src/index.js)
- [cli/src/mcp/server.js](https://github.com/andrewyng/context-hub/blob/67dcbeb2eb42c808549f08397920ad58be7c2206/cli/src/mcp/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cli package | library | Observed | Groups 27 file(s) under cli package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 38 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deploy-content.yml` (ci)
- `.github/workflows/publish.yml` (ci)
- `cli/package.json` (manifest)

## Top-level layout

- `content` — 716 analysed file(s)
- `cli` — 71 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.github` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `67dcbeb2eb42c808549f08397920ad58be7c2206` is the revision these paths and observations refer to.
