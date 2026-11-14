# Project structure: statsd/statsd

**Analysed commit:** `f7157b880631152569b04d626f631b60eec366f8`

**Commit reference:** [f7157b880631152569b04d626f631b60eec366f8](https://github.com/statsd/statsd/commit/f7157b880631152569b04d626f631b60eec366f8)

**Tree at this commit:** [statsd/statsd@f7157b880631](https://github.com/statsd/statsd/tree/f7157b880631152569b04d626f631b60eec366f8)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | statsd/statsd |
| Description | Daemon for easy but powerful stats aggregation |
| Stars | 18075 |
| Forks | 1935 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `f7157b880631152569b04d626f631b60eec366f8` |
| Retrieved at | 2026-11-14T19:11:23.006486+00:00 |
| Files in this snapshot | 102 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    package-and-publish-image.yml
backends/  (3 files)
  console.js
  graphite.js
  repeater.js
bin/  (1 files)
  statsd
debian/  (16 files)
  changelog
  compat
  control
  copyright
  dirs
  docs
  localConfig.js
  postinst
  postrm
  proxyConfig.js
  rules
  statsd-proxy.upstart
  statsd.install
  statsd.statsd-proxy.service
  statsd.statsd.service
  statsd.upstart
docs/  (15 files)
  additional_tools.md
  admin_interface.md
  backend.md
  backend_interface.md
  client_implementations.md
  cluster_proxy.md
  graphite.md
  graphite_pickle.md
  history.md
  metric_types.md
  namespacing.md
  protocol.md
  server.md
  server_implementations.md
  server_interface.md
examples/  (18 files)
  Etsy/  (1 files)
    StatsD.pm
  go/  (3 files)
    README.md
    doc.go
    statsd.go
  README.md
  StatsD.scala
  StatsdClient.java
  StatsdClient.jl
  StatsdClient.kt
  csharp_example.cs
  perl-example.pl
  php-example.php
  python_example.py
  ruby_example.rb
  ruby_example2.rb
  statsd-client.sh
  statsd.clj
  statsd.erl
lib/  (8 files)
  config.js
  helpers.js
  logger.js
  mgmt_console.js
  mgmt_server.js
  process_metrics.js
  process_mgmt.js
  set.js
packager/  (2 files)
  Procfile
  postinst
servers/  (2 files)
  tcp.js
  udp.js
test/  (15 files)
  graphite_delete_counters_tests.js
  graphite_legacy_tests.js
  graphite_legacy_tests_statsprefix.js
  graphite_pickle_tests.js
  graphite_tests.js
  graphite_tests_filters.js
  graphite_tests_statsprefix.js
  graphite_tests_statssuffix.js
  helpers_tests.js
  mgmt_console_tests.js
  process_metrics_tests.js
  process_mgmt_tests.js
  repeater_tests.js
  server_tests.js
  set_tests.js
utils/  (3 files)
  check_statsd.pl
  check_statsd_health
  statsd-timer-metric-counts.sh
.dockerignore
.gitignore
.pkgr.yml
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Changelog.md
DCO.txt
Dockerfile
LICENSE
MAINTAINERS.md
README.md
docker-compose.yml
exampleConfig.js
exampleProxyConfig.js
package.json
proxy.js
run_tests.js
stats.js
```

## Entry points

- [bin/statsd](https://github.com/statsd/statsd/blob/f7157b880631152569b04d626f631b60eec366f8/bin/statsd)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| backends package | library | Observed | Groups 3 file(s) under backends package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| debian package | library | Observed | Groups 2 file(s) under debian package (observed from repository paths and static analysis). |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 8 file(s) under lib package (observed from repository paths and static analysis). |
| servers package | library | Observed | Groups 2 file(s) under servers package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 15 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/workflows/package-and-publish-image.yml` (ci)
- `.pkgr.yml` (config)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 18 analysed file(s)
- `examples` — 18 analysed file(s)
- `debian` — 16 analysed file(s)
- `docs` — 15 analysed file(s)
- `test` — 15 analysed file(s)
- `lib` — 8 analysed file(s)
- `backends` — 3 analysed file(s)
- `utils` — 3 analysed file(s)
- `packager` — 2 analysed file(s)
- `servers` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f7157b880631152569b04d626f631b60eec366f8` is the revision these paths and observations refer to.
