# Project structure: schlagmichdoch/PairDrop

**Analysed commit:** `1b0c9c9d903c3cfc706df1303dc75c3b54d04c77`

**Commit reference:** [1b0c9c9d903c3cfc706df1303dc75c3b54d04c77](https://github.com/schlagmichdoch/PairDrop/commit/1b0c9c9d903c3cfc706df1303dc75c3b54d04c77)

**Tree at this commit:** [schlagmichdoch/PairDrop@1b0c9c9d903c](https://github.com/schlagmichdoch/PairDrop/tree/1b0c9c9d903c3cfc706df1303dc75c3b54d04c77)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | schlagmichdoch/PairDrop |
| Description | PairDrop: Transfer Files Cross-Platform. No Setup, No Signup. |
| Stars | 11806 |
| Forks | 724 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `1b0c9c9d903c3cfc706df1303dc75c3b54d04c77` |
| Retrieved at | 2026-11-14T19:12:15.474020+00:00 |
| Files in this snapshot | 99 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug-report.md
    enhancement.md
  workflows/  (3 files)
    docker-image.yml
    github-image.yml
    zip-release.yml
  FUNDING.yml
  dependabot.yml
dev/  (5 files)
  nginx/  (1 files)
    default.conf
  openssl/  (3 files)
    create.sh
    pairdropCA.cnf
    pairdropCert.cnf
  nginx-with-openssl.Dockerfile
docs/  (5 files)
  docker-swarm-usage.md
  faq.md
  host-your-own.md
  how-to.md
  technical-documentation.md
licenses/  (3 files)
  BSD_3-Clause-zip-js
  MIT-NoSleep
  MIT-heic2any
pairdrop-cli/  (6 files)
  .gitignore
  .pairdrop-cli-config.example
  pairdrop
  pairdrop.sh
  send-with-pairdrop
  send-with-pairdrop.ps1
public/  (56 files)
  fonts/  (2 files)
    OpenSans/  (2 files)
      … 2 files under this directory
  images/  (1 files)
    safari-pinned-tab.svg
  lang/  (38 files)
    ar.json
    be.json
    bg.json
    bn.json
    ca.json
    cs.json
    da.json
    de.json
    en.json
    es.json
    et.json
    eu.json
    fa.json
    fi.json
    fr.json
    he.json
    hu.json
    id.json
    it.json
    ja.json
    kab.json
    kn.json
    ko.json
    nb.json
    … 14 more files
  scripts/  (9 files)
    worker/  (1 files)
      … 1 files under this directory
    browser-tabs-connector.js
    localization.js
    main.js
    network.js
    persistent-storage.js
    ui-main.js
    ui.js
    util.js
  styles/  (2 files)
    styles-deferred.css
    styles-main.css
  index.html
  manifest.json
  robots.txt
  service-worker.js
server/  (5 files)
  helper.js
  index.js
  peer.js
  server.js
  ws-server.js
.dockerignore
.gitignore
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
docker-compose-coturn.yml
docker-compose-dev.yml
docker-compose.yml
package.json
rtc_config_example.json
turnserver_example.conf
```

## Entry points

- [server/index.js](https://github.com/schlagmichdoch/PairDrop/blob/1b0c9c9d903c3cfc706df1303dc75c3b54d04c77/server/index.js)
- [public/scripts/main.js](https://github.com/schlagmichdoch/PairDrop/blob/1b0c9c9d903c3cfc706df1303dc75c3b54d04c77/public/scripts/main.js)
- [server/server.js](https://github.com/schlagmichdoch/PairDrop/blob/1b0c9c9d903c3cfc706df1303dc75c3b54d04c77/server/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 45 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| dev package | library | Observed | Groups 1 file(s) under dev package (observed from repository paths and static analysis). |
| pairdrop-cli package | library | Observed | Groups 1 file(s) under pairdrop-cli package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 10 file(s) under public package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 5 file(s) under server package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/docker-image.yml` (ci)
- `.github/workflows/github-image.yml` (ci)
- `.github/workflows/zip-release.yml` (ci)
- `Dockerfile` (container)
- `docker-compose-coturn.yml` (config)
- `docker-compose-dev.yml` (config)
- `docker-compose.yml` (container)
- `package.json` (manifest)
- `public/lang/ar.json` (config)
- `public/lang/be.json` (config)
- `public/lang/bg.json` (config)
- `public/lang/bn.json` (config)
- `public/lang/ca.json` (config)
- `public/lang/cs.json` (config)
- `public/lang/da.json` (config)
- `public/lang/de.json` (config)
- `public/lang/en.json` (config)
- `public/lang/es.json` (config)
- `public/lang/et.json` (config)
- `public/lang/eu.json` (config)
- `public/lang/fa.json` (config)
- `public/lang/fi.json` (config)
- `public/lang/fr.json` (config)
- `public/lang/he.json` (config)
- `public/lang/hu.json` (config)
- `public/lang/id.json` (config)
- `public/lang/it.json` (config)
- `public/lang/ja.json` (config)
- `public/lang/kab.json` (config)
- `public/lang/kn.json` (config)
- `public/lang/ko.json` (config)
- `public/lang/nb.json` (config)
- `public/lang/nl.json` (config)
- `public/lang/nn.json` (config)
- `public/lang/pl.json` (config)
- `public/lang/pt-BR.json` (config)
- `public/lang/ro.json` (config)
- `public/lang/ru.json` (config)
- `public/lang/sk.json` (config)
- `public/lang/ta.json` (config)
- `public/lang/th.json` (config)
- `public/lang/tr.json` (config)
- `public/lang/uk.json` (config)
- `public/lang/zh-CN.json` (config)
- `public/lang/zh-HK.json` (config)
- `public/lang/zh-TW.json` (config)
- `public/manifest.json` (config)
- `rtc_config_example.json` (config)

## Top-level layout

- `public` — 56 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 7 analysed file(s)
- `pairdrop-cli` — 6 analysed file(s)
- `dev` — 5 analysed file(s)
- `docs` — 5 analysed file(s)
- `server` — 5 analysed file(s)
- `licenses` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1b0c9c9d903c3cfc706df1303dc75c3b54d04c77` is the revision these paths and observations refer to.
