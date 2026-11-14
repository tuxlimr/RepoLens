# Project structure: caronc/apprise

**Analysed commit:** `c6f76f3599ec9bc1591abfd4fc8c27a5124f88fa`

**Commit reference:** [c6f76f3599ec9bc1591abfd4fc8c27a5124f88fa](https://github.com/caronc/apprise/commit/c6f76f3599ec9bc1591abfd4fc8c27a5124f88fa)

**Tree at this commit:** [caronc/apprise@c6f76f3599ec](https://github.com/caronc/apprise/tree/c6f76f3599ec9bc1591abfd4fc8c27a5124f88fa)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | caronc/apprise |
| Description | Apprise - Push Notifications that work with just about every platform! |
| Stars | 17765 |
| Forks | 700 |
| Licence | BSD-2-Clause |
| Language | Python |
| Default branch | master |
| Analysed commit | `c6f76f3599ec9bc1591abfd4fc8c27a5124f88fa` |
| Retrieved at | 2026-11-14T19:08:29.435237+00:00 |
| Files in this snapshot | 390 |

## Directory tree

```text
.github/  (13 files)
  ISSUE_TEMPLATE/  (5 files)
    1_bug_report.md
    2_enhancement_request.md
    3_new-notification-request.md
    4_question.md
    config.yaml
  badges/  (1 files)
    loc.svg
  workflows/  (5 files)
    codeql-analysis.yml
    lint.yml
    loc-badge.yml
    pkgbuild.yml
    tests.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
.vscode/  (2 files)
  extensions.json
  settings.json
apprise/  (301 files)
  assets/  (2 files)
    NotifyXML-1.0.xsd
    NotifyXML-1.1.xsd
  attachment/  (5 files)
    __init__.py
    base.py
    file.py
    http.py
    memory.py
  compat/  (3 files)
    __init__.py
    markdown33.py
    py39.py
  config/  (5 files)
    __init__.py
    base.py
    file.py
    http.py
    memory.py
  conversion/  (5 files)
    __init__.py
    commonmark.py
    dialect.py
    format.py
    html.py
  decorators/  (3 files)
    __init__.py
    base.py
    notify.py
  i18n/  (21 files)
    ar/  (1 files)
      … 1 files under this directory
    de/  (1 files)
      … 1 files under this directory
    en/  (1 files)
      … 1 files under this directory
    es/  (1 files)
      … 1 files under this directory
    fr/  (1 files)
      … 1 files under this directory
    hi/  (1 files)
      … 1 files under this directory
    id/  (1 files)
      … 1 files under this directory
    it/  (1 files)
      … 1 files under this directory
    ja/  (1 files)
      … 1 files under this directory
    ko/  (1 files)
      … 1 files under this directory
    ms/  (1 files)
      … 1 files under this directory
    nl/  (1 files)
      … 1 files under this directory
    pl/  (1 files)
      … 1 files under this directory
    pt/  (1 files)
      … 1 files under this directory
    ru/  (1 files)
      … 1 files under this directory
    th/  (1 files)
      … 1 files under this directory
    tl/  (1 files)
      … 1 files under this directory
    tr/  (1 files)
      … 1 files under this directory
    vi/  (1 files)
      … 1 files under this directory
    zh/  (1 files)
      … 1 files under this directory
    __init__.py
  plugins/  (214 files)
    amqp/  (5 files)
      … 5 files under this directory
    email/  (5 files)
      … 5 files under this directory
    fcm/  (5 files)
      … 5 files under this directory
    irc/  (6 files)
      … 6 files under this directory
    matrix/  (5 files)
      … 5 files under this directory
    nostr/  (4 files)
      … 4 files under this directory
    vapid/  (2 files)
      … 2 files under this directory
    xmpp/  (4 files)
      … 4 files under this directory
    __init__.py
    africas_talking.py
    apprise_api.py
    aprs.py
    awswhatsapp.py
    bark.py
    base.py
    betterstack.py
    blink1.py
    bluesky.py
    brevo.py
    bulksms.py
    bulkvs.py
    burstsms.py
    chanify.py
    clickatell.py
    clicksend.py
    cliq.py
    cm.py
    custom_form.py
    custom_json.py
    custom_xml.py
    d7networks.py
    dapnet.py
    … 154 more files
  utils/  (21 files)
    __init__.py
    base64.py
    cwe312.py
    disk.py
    format.py
    http.py
    json.py
    logic.py
    module.py
    parse.py
    pem.py
    pgp.py
    sanitize.py
    singleton.py
    socket.py
    template.py
    templates.py
    time.py
    wkd.py
    xml.py
    yaml.py
  __init__.py
  apprise.py
  apprise_attachment.py
  apprise_config.py
  asset.py
  cli.py
  common.py
  dispatch.py
  emojis.py
  exception.py
  locale.py
  logger.py
  manager.py
  manager_attachment.py
  manager_config.py
  manager_plugins.py
  persistent_store.py
  py.typed
  result.py
  tag.py
  template.py
  url.py
bin/  (5 files)
  README.md
  apprise
  build-rpm.sh
  checkdone.sh
  test.sh
packaging/  (10 files)
  man/  (3 files)
    apprise.1
    apprise.1.html
    apprise.md
  redhat/  (3 files)
    python-apprise.rpmlintrc.el10
    python-apprise.rpmlintrc.el9
    python-apprise.spec
  README.md
  i18n_normalize.sh
  i18n_status.py
  verify_translations.py
tests/  (43 files)
  docker/  (8 files)
    Dockerfile.el10
    Dockerfile.el9
    Dockerfile.f44
    Dockerfile.py310
    Dockerfile.py311
    Dockerfile.py312
    Dockerfile.py39
    Dockerfile.rawhide
  helpers/  (6 files)
    __init__.py
    asyncio.py
    delivery.py
    environment.py
    module.py
    rest.py
  conftest.py
  test_api.py
  test_apprise_asset.py
  test_apprise_attachments.py
  test_apprise_cli.py
  test_apprise_config.py
  test_apprise_emojis.py
  test_apprise_helpers.py
  test_apprise_jsonencoder.py
  test_apprise_pickle.py
  test_apprise_template.py
  test_apprise_template_placement.py
  test_apprise_translations.py
  test_apprise_utils.py
  test_asyncio.py
  test_attach_base.py
  test_attach_file.py
  test_attach_http.py
  test_attach_memory.py
  test_compat_markdown33.py
  test_compat_py39.py
  test_config_base.py
  test_config_file.py
  test_config_http.py
  … 5 more files
.codecov.yml
.gitignore
.gitleaks.toml
ACKNOWLEDGEMENTS.md
CONTRIBUTING.md
LICENSE
MANIFEST.in
README.md
SECURITY.md
all-plugin-requirements.txt
babel.cfg
dev-requirements.txt
docker-compose.yml
pyproject.toml
requirements.txt
setup.py
```

## Entry points

- [apprise/cli.py](https://github.com/caronc/apprise/blob/c6f76f3599ec9bc1591abfd4fc8c27a5124f88fa/apprise/cli.py)
- [packaging/i18n_status.py:424](https://github.com/caronc/apprise/blob/c6f76f3599ec9bc1591abfd4fc8c27a5124f88fa/packaging/i18n_status.py#L424)
- [packaging/verify_translations.py:118](https://github.com/caronc/apprise/blob/c6f76f3599ec9bc1591abfd4fc8c27a5124f88fa/packaging/verify_translations.py#L118)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apprise package | library | Observed | Groups 269 file(s) under apprise package (observed from repository paths and static analysis). Observed top-level classes: AMQP091Adapter, AMQP10Adapter, AMQPConfig, AMQPError, AMQPMessage, AMQPVersion. Observed top-lev… |
| bin package | library | Observed | Groups 3 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 19 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BuildPyWithTranslations, ConfigBase, ConfigFile, ConfigHTTP, ConfigMemory. Observed… |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Catalog, CustomHelpCommand, Entry, PersistentStorageMode. Observed top-level functions: _e… |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: AppriseAPIMethod, AppriseAPIVersion, IRCClient, NotifyAppriseAPI, NotifySignalAPI. |
| packaging package | library | Observed | Groups 1 file(s) under packaging package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 35 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH requests.get, PATCH requests.post, PATCH requests.request, PATCH requests.get, PATCH requests.post. Observed top… |

## Important files

- `.codecov.yml` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yaml` (config)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/loc-badge.yml` (ci)
- `.github/workflows/pkgbuild.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.gitleaks.toml` (config)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `MANIFEST.in` (manifest)
- `babel.cfg` (config)
- `docker-compose.yml` (container)
- `pyproject.toml` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)
- `tests/docker/Dockerfile.el10` (container)
- `tests/docker/Dockerfile.el9` (container)
- `tests/docker/Dockerfile.f44` (container)
- `tests/docker/Dockerfile.py310` (container)
- `tests/docker/Dockerfile.py311` (container)
- `tests/docker/Dockerfile.py312` (container)
- `tests/docker/Dockerfile.py39` (container)
- `tests/docker/Dockerfile.rawhide` (container)

## Top-level layout

- `apprise` — 301 analysed file(s)
- `tests` — 43 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 13 analysed file(s)
- `packaging` — 10 analysed file(s)
- `bin` — 5 analysed file(s)
- `.vscode` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `c6f76f3599ec9bc1591abfd4fc8c27a5124f88fa` is the revision these paths and observations refer to.
