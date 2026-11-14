# Project structure: nginx-proxy/nginx-proxy

**Analysed commit:** `bff2cddfece8e4f2c6d00b62ba45b8214c4727c5`

**Commit reference:** [bff2cddfece8e4f2c6d00b62ba45b8214c4727c5](https://github.com/nginx-proxy/nginx-proxy/commit/bff2cddfece8e4f2c6d00b62ba45b8214c4727c5)

**Tree at this commit:** [nginx-proxy/nginx-proxy@bff2cddfece8](https://github.com/nginx-proxy/nginx-proxy/tree/bff2cddfece8e4f2c6d00b62ba45b8214c4727c5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nginx-proxy/nginx-proxy |
| Description | Automated Nginx Reverse Proxy for Docker |
| Stars | 19942 |
| Forks | 3037 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `bff2cddfece8e4f2c6d00b62ba45b8214c4727c5` |
| Retrieved at | 2026-11-14T19:08:04.879237+00:00 |
| Files in this snapshot | 304 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    config.yml
  workflows/  (4 files)
    build-publish-dispatch.yml
    build-publish.yml
    dockerhub-description.yml
    test.yml
  ISSUE_TEMPLATE.md
  dependabot.yml
app/  (2 files)
  Procfile
  docker-entrypoint.sh
docs/  (1 files)
  README.md
test/  (281 files)
  certs/  (3 files)
    README.md
    ca-root.crt
    create_server_certificate.sh
  requirements/  (6 files)
    web/  (3 files)
      … 3 files under this directory
    Dockerfile-nginx-proxy-tester
    README.md
    python-requirements.txt
  test_acme-http-challenge-location/  (11 files)
    acme_root/  (1 files)
      … 1 files under this directory
    certs/  (1 files)
      … 1 files under this directory
    compose.base.override.yml
    test_acme-http-challenge-location-accept-unknown-host.py
    test_acme-http-challenge-location-accept-unknown-host.yml
    test_acme-http-challenge-location-disabled.py
    test_acme-http-challenge-location-disabled.yml
    test_acme-http-challenge-location-enabled-is-default.py
    test_acme-http-challenge-location-enabled-is-default.yml
    test_acme-http-challenge-location-legacy.py
    test_acme-http-challenge-location-legacy.yml
  test_build/  (1 files)
    test_build.py
  test_custom/  (13 files)
    my_custom_proxy_settings_bar.conf
    my_custom_proxy_settings_baz.conf
    my_custom_proxy_settings_f00.conf
    test_defaults.py
    test_defaults.yml
    test_location-defaults.py
    test_location-defaults.yml
    test_location-per-vhost.py
    test_location-per-vhost.yml
    test_per-vhost.py
    test_per-vhost.yml
    test_proxy-wide.py
    test_proxy-wide.yml
  test_custom-error-page/  (3 files)
    50x.html
    test_custom-error-page.py
    test_custom-error-page.yml
  test_debug-endpoint/  (4 files)
    test_global.py
    test_global.yml
    test_per-container.py
    test_per-container.yml
  test_default-host/  (2 files)
    test_default-host.py
    test_default-host.yml
  test_docker-unix-socket/  (2 files)
    test_docker-unix-socket.py
    test_docker-unix-socket.yml
  test_dockergen/  (6 files)
    test_dockergen.base.yml
    test_dockergen.py
    test_dockergen_network_segregation-custom-label.base.yml
    test_dockergen_network_segregation-custom-label.py
    test_dockergen_network_segregation.base.yml
    test_dockergen_network_segregation.py
  test_enable-http-on-missing-cert/  (2 files)
    test_enable-http-on-missing-cert.py
    test_enable-http-on-missing-cert.yml
  test_events/  (2 files)
    test_events.py
    test_events.yml
  test_external-ports/  (8 files)
    certs/  (1 files)
      … 1 files under this directory
    compose.base.override.yml
    test_multiports-priority.py
    test_multiports-priority.yml
    test_virtual-host-multiport.py
    test_virtual-host-multiport.yml
    test_virtual-host.py
    test_virtual-host.yml
  test_fallback/  (19 files)
    test_fallback.data/  (18 files)
      … 18 files under this directory
    test_fallback.py
  test_headers/  (7 files)
    certs/  (3 files)
      … 3 files under this directory
    test_http.py
    test_http.yml
    test_https.py
    test_https.yml
  test_host-network-mode/  (4 files)
    test_host-network-mode.py
    test_host-network-mode.yml
    test_proxy-host-network-mode.base.yml
    test_proxy-host-network-mode.py
  test_htpasswd/  (10 files)
    htpasswd/  (3 files)
      … 3 files under this directory
    compose.base.override.yml
    test_htpasswd-regex-virtual-host.py
    test_htpasswd-regex-virtual-host.yml
    test_htpasswd-virtual-host.py
    test_htpasswd-virtual-host.yml
    test_htpasswd-virtual-path.py
    test_htpasswd-virtual-path.yml
  test_http-port/  (2 files)
    test_http-port.py
    test_http-port.yml
  test_http2/  (2 files)
    test_http2-global-disabled.py
    test_http2-global-disabled.yml
  test_http3/  (6 files)
    test_http3-global-disabled.py
    test_http3-global-disabled.yml
    test_http3-global-enabled.py
    test_http3-global-enabled.yml
    test_http3-vhost.py
    test_http3-vhost.yml
  test_internal/  (6 files)
    compose.base.override.yml
    network_internal.conf
    test_internal-per-vhost.py
    test_internal-per-vhost.yml
    test_internal-per-vpath.py
    test_internal-per-vpath.yml
  test_ipv6/  (6 files)
    test_ipv6-prefer-ipv4-network.py
    test_ipv6-prefer-ipv4-network.yml
    test_ipv6-prefer-ipv6-network.py
    test_ipv6-prefer-ipv6-network.yml
    test_ipv6.py
    test_ipv6.yml
  test_keepalive/  (2 files)
    test_keepalive.py
    test_keepalive.yml
  test_loadbalancing/  (2 files)
    test_loadbalancing.py
    test_loadbalancing.yml
  test_location-override/  (11 files)
    vhost.d/  (9 files)
      … 9 files under this directory
    test_location-override.py
    test_location-override.yml
  test_logs/  (8 files)
    test_log-disabled.py
    test_log-disabled.yml
    test_log-format.py
    test_log-format.yml
    test_log-json-format.py
    test_log-json-format.yml
    test_log-json.py
    test_log-json.yml
  test_multiple-hosts/  (2 files)
    test_multiple-hosts.py
    test_multiple-hosts.yml
  test_multiple-networks/  (2 files)
    test_multiple-networks.py
    test_multiple-networks.yml
  test_multiports/  (8 files)
    test_multiports-base-json.py
    test_multiports-base-json.yml
    test_multiports-base-yaml.py
    test_multiports-base-yaml.yml
    test_multiports-invalid-syntax.py
    test_multiports-invalid-syntax.yml
    test_multiports-merge.py
    test_multiports-merge.yml
  test_nominal/  (2 files)
    test_nominal.py
    test_nominal.yml
  test_ocsp-stapling/  (7 files)
    certs/  (1 files)
      … 1 files under this directory
    compose.base.override.yml
    helpers.py
    test_ocsp-stapling-proxy-disabled.py
    test_ocsp-stapling-proxy-disabled.yml
    test_ocsp-stapling-proxy-enabled.py
    test_ocsp-stapling-proxy-enabled.yml
  test_ports/  (8 files)
    test_default-80.py
    test_default-80.yml
    test_single-port-not-80.py
    test_single-port-not-80.yml
    test_virtual-port-single-different-from-single-port.py
    test_virtual-port-single-different-from-single-port.yml
    test_virtual-port.py
    test_virtual-port.yml
  test_proxy_protocol/  (4 files)
    test_proxy-protocol-global-disabled.py
    test_proxy-protocol-global-disabled.yml
    test_proxy-protocol-global-enabled.py
    test_proxy-protocol-global-enabled.yml
  test_raw-ip-vhost/  (2 files)
    test_raw-ip-vhost.py
    test_raw-ip-vhost.yml
  test_resolvers/  (2 files)
    test_resolvers.base.yml
    test_resolvers.py
  test_server-down/  (6 files)
    test_load-balancing.py
    test_load-balancing.yml
    test_no-server-down.py
    test_no-server-down.yml
    test_server-down.py
    test_server-down.yml
  test_ssl/  (43 files)
    acme_root/  (1 files)
      … 1 files under this directory
    cert_selection/  (2 files)
      … 2 files under this directory
    certs/  (3 files)
      … 3 files under this directory
    certs_mtls/  (6 files)
      … 6 files under this directory
    certs_wildcard_nohttps/  (2 files)
      … 2 files under this directory
    clientcerts/  (2 files)
      … 2 files under this directory
    compose.base.override.yml
    test_cert-selection.py
    test_cert-selection.yml
    test_dhparam.base.yml
    test_dhparam.py
    test_hsts.py
    test_hsts.yml
    test_https-port.py
    test_https-port.yml
    test_mtls-client-certificate.py
    test_mtls-client-certificate.yml
    test_nohttp.py
    test_nohttp.yml
    test_nohttps.py
    test_nohttps.yml
    test_noredirect.py
    test_noredirect.yml
    test_redirect_custom.py
    test_redirect_custom.yml
    test_redirect_default.py
    test_redirect_default.yml
    test_virtual-path.py
    test_virtual-path.yml
    test_wildcard-cert-nohttps.py
    … 3 more files
  test_trust-downstream-proxy/  (8 files)
    certs/  (1 files)
      … 1 files under this directory
    compose.base.override.yml
    test_default.py
    test_default.yml
    test_disabled.py
    test_disabled.yml
    test_enabled.py
    test_enabled.yml
  test_unreachable-network/  (3 files)
    README.md
    test_unreachable-network.py
    test_unreachable-network.yml
  test_upstream-name/  (4 files)
    test_predictable-name.py
    test_predictable-name.yml
    test_sha1-name.py
    test_sha1-name.yml
  test_vhost-empty-string/  (2 files)
    test_vhost-empty-string.py
    test_vhost-empty-string.yml
  test_vhost-in-multiple-networks/  (2 files)
    test_vhost-in-multiple-networks.py
    test_vhost-in-multiple-networks.yml
  test_virtual-path/  (16 files)
    alternate.conf
    bar.conf
    default.conf
    foo.conf
    host.conf
    path.conf
    test_custom-conf.py
    test_custom-conf.yml
    test_default-root-none.py
    test_default-root-none.yml
    test_forwarding.py
    test_forwarding.yml
    test_location-precedence.py
    test_location-precedence.yml
    test_virtual-paths.py
    test_virtual-paths.yml
  test_virtual-proto/  (5 files)
    nginx-proxy.tld.crt
    ssl-app-multi-ports.conf
    ssl-app-single-port.conf
    test_virtual-proto.py
    test_virtual-proto.yml
  test_wildcard-host/  (2 files)
    test_wildcard-host.py
    test_wildcard-host.yml
  README.md
  compose.base.yml
  conftest.py
  pytest.ini
  pytest.sh
.dockerignore
.gitignore
Dockerfile.alpine
Dockerfile.debian
Dockerfile.dockergen
LICENSE
Makefile
README.md
docker-compose-separate-containers.yml
docker-compose.yml
network_internal.conf
nginx.tmpl
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 1 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 279 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: DockerComposer, Handler, NginxProxyAdapter, RequestsForDocker. Observed top-level functions: __prepare_and… |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/build-publish-dispatch.yml` (ci)
- `.github/workflows/build-publish.yml` (ci)
- `.github/workflows/dockerhub-description.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `Dockerfile.alpine` (container)
- `Dockerfile.debian` (container)
- `Dockerfile.dockergen` (container)
- `docker-compose-separate-containers.yml` (config)
- `docker-compose.yml` (container)
- `test/requirements/Dockerfile-nginx-proxy-tester` (container)
- `test/requirements/web/Dockerfile` (container)

## Top-level layout

- `test` — 281 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `.github` — 8 analysed file(s)
- `app` — 2 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 34 file(s) were skipped during inventory (34 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `bff2cddfece8e4f2c6d00b62ba45b8214c4727c5` is the revision these paths and observations refer to.
