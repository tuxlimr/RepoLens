# Project structure: BrasilAPI/BrasilAPI

**Analysed commit:** `0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b`

**Commit reference:** [0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b](https://github.com/BrasilAPI/BrasilAPI/commit/0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b)

**Tree at this commit:** [BrasilAPI/BrasilAPI@0c229b4e56d0](https://github.com/BrasilAPI/BrasilAPI/tree/0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | BrasilAPI/BrasilAPI |
| Description | Vamos transformar o Brasil em uma API? |
| Stars | 11571 |
| Forks | 805 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b` |
| Retrieved at | 2026-11-14T19:12:16.358501+00:00 |
| Files in this snapshot | 323 |

## Directory tree

```text
.claude/  (2 files)
  hooks/  (1 files)
    pre-merge-check.sh
  settings.json
.github/  (10 files)
  contributors-list/  (1 files)
    layout-strategy-custom.js
  workflows/  (4 files)
    banks-headquarters-snapshot.yml
    e2e-tests.yml
    hospitais-snapshot.yml
    pix-participants-snapshot.yml
  CODE_REVIEW_GUIDELINES.md
  PULL_REQUEST_TEMPLATE.md
  README.md
  copilot-instructions.md
  copilot-review-instructions.md
.husky/  (2 files)
  .gitignore
  pre-commit
.vscode/  (1 files)
  launch.json
components/  (2 files)
  Header/  (2 files)
    index.js
    styles.module.scss
docs/  (4 files)
  BANKS_HEADQUARTERS_ADDRESS.md
  ENDPOINT_GUIDE.md
  HOSPITAIS_MAPASUS.md
  audit-2026-08-10.md
errors/  (7 files)
  BadRequestError.js
  BaseError.js
  InternalError.js
  NotFoundError.js
  ServiceUnavailableError.js
  UnauthorizedError.js
  UnprocessableEntityError.js
lib/  (3 files)
  fetchGeocoordinateFromBrazilLocation.js
  fetchTimezoneNameFromBrazilLocation.js
  parseRequest.js
middlewares/  (4 files)
  cache.js
  errorHandler.js
  firewall.js
  logger.js
pages/  (125 files)
  api/  (87 files)
    banks/  (2 files)
      … 2 files under this directory
    cambio/  (2 files)
      … 2 files under this directory
    cep/  (3 files)
      … 3 files under this directory
    cnpj/  (1 files)
      … 1 files under this directory
    cpf/  (1 files)
      … 1 files under this directory
    cptec/  (9 files)
      … 9 files under this directory
    cvm/  (4 files)
      … 4 files under this directory
    ddd/  (4 files)
      … 4 files under this directory
    diasuteis/  (1 files)
      … 1 files under this directory
    eleicoes/  (5 files)
      … 5 files under this directory
    feriados/  (2 files)
      … 2 files under this directory
    fipe/  (7 files)
      … 7 files under this directory
    geolocation/  (1 files)
      … 1 files under this directory
    hospitais/  (6 files)
      … 6 files under this directory
    ibge/  (10 files)
      … 10 files under this directory
    ibpt/  (7 files)
      … 7 files under this directory
    indices/  (3 files)
      … 3 files under this directory
    isbn/  (1 files)
      … 1 files under this directory
    ncm/  (2 files)
      … 2 files under this directory
    oms/  (2 files)
      … 2 files under this directory
    pix/  (1 files)
      … 1 files under this directory
    registrobr/  (1 files)
      … 1 files under this directory
    solar/  (1 files)
      … 1 files under this directory
    status/  (1 files)
      … 1 files under this directory
    taxas/  (2 files)
      … 2 files under this directory
    tickers/  (2 files)
      … 2 files under this directory
    tuss/  (4 files)
      … 4 files under this directory
    universities/  (2 files)
      … 2 files under this directory
  docs/  (34 files)
    doc/  (33 files)
      … 33 files under this directory
    index.js
  sitemap.xml/  (1 files)
    index.jsx
  _app.js
  _document.js
  index.js
public/  (3 files)
  images/  (1 files)
    api-schema.svg
  powered-by-vercel.svg
  robots.txt
scripts/  (4 files)
  generate-bank-headquarters-snapshot.js
  generate-hospitais-snapshot.js
  generate-pix-participants-snapshot.js
  merge-pr.sh
services/  (63 files)
  banco-central/  (4 files)
    snapshots/  (1 files)
      … 1 files under this directory
    banksList.json
    index.js
    logo-urls.json
  cambio/  (2 files)
    cotacao.js
    moedas.js
  cep/  (1 files)
    cep.js
  cpf/  (1 files)
    cpf.js
  cptec/  (5 files)
    cities.js
    constants.js
    index.js
    swell.js
    weather.js
  cvm/  (2 files)
    corretoras.js
    fundos.js
  dados-abertos-br/  (1 files)
    cities.js
  eleicoes/  (6 files)
    anos-eleitorais.js
    candidaturas.js
    cargos-por-municipio.js
    constants.js
    index.js
    ordinarias.js
  fipe/  (9 files)
    automakers.js
    constants.js
    http.js
    parallelum.js
    price.js
    priceByModelAndYear.js
    referenceTable.js
    vehiclesByMakers.js
    yearsByModel.js
  holidays/  (1 files)
    index.js
  hospitais/  (5 files)
    snapshots/  (1 files)
      … 1 files under this directory
    index.js
    origem.js
    query.js
    vocabulario.js
  ibge/  (3 files)
    cnae.js
    gov.js
    wikipedia.js
  ibpt/  (1 files)
    index.js
  indices/  (4 files)
    codes.js
    helpers.js
    igpm.js
    schemas.js
  isbn/  (5 files)
    cbl.js
    googleBooks.js
    mercadoEditorial.js
    openLibrary.js
    tools.js
  oms/  (1 files)
    cid10/  (1 files)
      … 1 files under this directory
  pix/  (2 files)
    snapshots/  (1 files)
      … 1 files under this directory
    participants.js
  sefaz/  (1 files)
    index.js
  tickers/  (1 files)
    listTickers.js
  tuss/  (1 files)
    index.js
  cnpj.js
  date.js
  ddd.js
  getJsonDoc.js
  registro.js
  solarIncidenceService.js
  universities.js
styles/  (2 files)
  globals.scss
  home.module.scss
tests/  (65 files)
  cpetc/  (5 files)
    aeroporto-v1.test.js
    capital-v1.test.js
    cidade-v1.test.js
    ondas-v1.test.js
    previsao-v1.test.js
  eleicoes/  (8 files)
    candidatos/  (2 files)
      … 2 files under this directory
    anos-eleitorais-api.test.js
    anos-eleitorais.test.js
    cargos-por-municipio-api.test.js
    cargos-por-municipio.test.js
    ordinarias-api.test.js
    ordinarias.test.js
  feriados/  (1 files)
    getHolidays.test.js
  helpers/  (4 files)
    ddd/  (1 files)
      … 1 files under this directory
    feriados/  (1 files)
      … 1 files under this directory
    server/  (1 files)
      … 1 files under this directory
    cors.js
  indices/  (1 files)
    igpm.test.js
  pages/  (1 files)
    api/  (1 files)
      … 1 files under this directory
  services/  (3 files)
    hospitais/  (1 files)
      … 1 files under this directory
    isbn/  (1 files)
      … 1 files under this directory
    pix/  (1 files)
      … 1 files under this directory
  b3-v1.test.js
  banks-logo-url.test.js
  banks-v1.test.js
  cambio-v1.test.js
  cep-timeout.test.js
  cep-v1.test.js
  cep-v2.test.js
  cep-v3.test.js
  cnpj-contract.test.js
  cnpj-v1.test.js
  corretoras-v1.test.js
  cpf-v1.test.js
  ddd-uf-v1.test.js
  ddd-v1.test.js
  ddd-v2.test.js
  diasuteis-v1.test.js
  docs-spec-refs.test.js
  feriados-v1.test.js
  fetchGeocoordinateFromBrazilLocation.test.js
  fipe-v1.test.js
  fundos-v1.test.js
  geolocation-v1.test.js
  haversine.test.js
  holidays-uf-fix.test.js
  … 18 more files
util/  (7 files)
  cep-error-handler.js
  getCsvAsJson.js
  haversine.js
  mapUfToUfCode.js
  normalizeBrazilianDate.js
  rejectWhenEmptyArray.js
  removeSpecialChars.js
.codex
.editorconfig
.eslintignore
.eslintrc.js
.gitignore
.nvmrc
.prettierrc
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
GOOD_PRACTICES.md
LICENSE
README.md
app.js
jsconfig.json
next.config.js
package.json
vercel.json
vite.config.js
```

## Entry points

- [app.js](https://github.com/BrasilAPI/BrasilAPI/blob/0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b/app.js)
- [components/Header/index.js](https://github.com/BrasilAPI/BrasilAPI/blob/0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b/components/Header/index.js)
- [pages/index.js](https://github.com/BrasilAPI/BrasilAPI/blob/0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b/pages/index.js)
- [pages/sitemap.xml/index.jsx](https://github.com/BrasilAPI/BrasilAPI/blob/0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b/pages/sitemap.xml/index.jsx)
- [services/banco-central/index.js](https://github.com/BrasilAPI/BrasilAPI/blob/0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b/services/banco-central/index.js)
- [services/cptec/index.js](https://github.com/BrasilAPI/BrasilAPI/blob/0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b/services/cptec/index.js)
- [services/eleicoes/index.js](https://github.com/BrasilAPI/BrasilAPI/blob/0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b/services/eleicoes/index.js)
- [services/holidays/index.js](https://github.com/BrasilAPI/BrasilAPI/blob/0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b/services/holidays/index.js)
- [services/hospitais/index.js](https://github.com/BrasilAPI/BrasilAPI/blob/0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b/services/hospitais/index.js)
- [services/ibpt/index.js](https://github.com/BrasilAPI/BrasilAPI/blob/0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b/services/ibpt/index.js)
- [services/oms/cid10/index.js](https://github.com/BrasilAPI/BrasilAPI/blob/0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b/services/oms/cid10/index.js)
- [services/sefaz/index.js](https://github.com/BrasilAPI/BrasilAPI/blob/0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b/services/sefaz/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 87 file(s) under api layer (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 1 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 40 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| errors package | library | Observed | Groups 7 file(s) under errors package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 3 file(s) under lib package (observed from repository paths and static analysis). |
| middlewares package | library | Observed | Groups 4 file(s) under middlewares package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 4 file(s) under pages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 58 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 65 file(s) under tests (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 7 file(s) under util package (observed from repository paths and static analysis). |

## Important files

- `.claude/settings.json` (config)
- `.editorconfig` (config)
- `.github/workflows/banks-headquarters-snapshot.yml` (ci)
- `.github/workflows/e2e-tests.yml` (ci)
- `.github/workflows/hospitais-snapshot.yml` (ci)
- `.github/workflows/pix-participants-snapshot.yml` (ci)
- `.vscode/launch.json` (config)
- `jsconfig.json` (config)
- `package.json` (manifest)
- `pages/docs/doc/bank.json` (config)
- `pages/docs/doc/basic_info.json` (config)
- `pages/docs/doc/cambio.json` (config)
- `pages/docs/doc/cep.json` (config)
- `pages/docs/doc/cid10.json` (config)
- `pages/docs/doc/cnpj.json` (config)
- `pages/docs/doc/corretoras.json` (config)
- `pages/docs/doc/cpf.json` (config)
- `pages/docs/doc/cptec.json` (config)
- `pages/docs/doc/ddd.json` (config)
- `pages/docs/doc/diasuteis.json` (config)
- `pages/docs/doc/eleicoes.json` (config)
- `pages/docs/doc/error.json` (config)
- `pages/docs/doc/fipe.json` (config)
- `pages/docs/doc/fundos.json` (config)
- `pages/docs/doc/geolocation.json` (config)
- `pages/docs/doc/holydays.json` (config)
- `pages/docs/doc/hospitais.json` (config)
- `pages/docs/doc/ibge.json` (config)
- `pages/docs/doc/ibpt.json` (config)
- `pages/docs/doc/igpm.json` (config)
- `pages/docs/doc/isbn.json` (config)
- `pages/docs/doc/ncm.json` (config)
- `pages/docs/doc/pix.json` (config)
- `pages/docs/doc/registrobr.json` (config)
- `pages/docs/doc/solarIncidence.json` (config)
- `pages/docs/doc/statewideHolydays.json` (config)
- `pages/docs/doc/status.json` (config)
- `pages/docs/doc/taxas.json` (config)
- `pages/docs/doc/tickers.json` (config)
- `pages/docs/doc/tuss.json` (config)
- `pages/docs/doc/universities.json` (config)
- `services/banco-central/banksList.json` (config)
- `services/banco-central/logo-urls.json` (config)
- `services/banco-central/snapshots/metrics-latest.json` (config)
- `services/hospitais/snapshots/metrics-latest.json` (config)
- `services/pix/snapshots/metadata-latest.json` (config)
- `vercel.json` (config)

## Top-level layout

- `pages` — 125 analysed file(s)
- `tests` — 65 analysed file(s)
- `services` — 63 analysed file(s)
- `(root files)` — 19 analysed file(s)
- `.github` — 10 analysed file(s)
- `errors` — 7 analysed file(s)
- `util` — 7 analysed file(s)
- `docs` — 4 analysed file(s)
- `middlewares` — 4 analysed file(s)
- `scripts` — 4 analysed file(s)
- `lib` — 3 analysed file(s)
- `public` — 3 analysed file(s)
- `.claude` — 2 analysed file(s)
- `.husky` — 2 analysed file(s)
- `components` — 2 analysed file(s)
- `styles` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0c229b4e56d0c8f789e1162b6a71d6ea1d54fc8b` is the revision these paths and observations refer to.
