# Project structure: mail-in-a-box/mailinabox

**Analysed commit:** `b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1`

**Commit reference:** [b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1](https://github.com/mail-in-a-box/mailinabox/commit/b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1)

**Tree at this commit:** [mail-in-a-box/mailinabox@b71c2e1ca6df](https://github.com/mail-in-a-box/mailinabox/tree/b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mail-in-a-box/mailinabox |
| Description | Mail-in-a-Box helps individuals take back control of their email by defining a one-click, easy-to-deploy SMTP+everything else server: a mail server in a box. |
| Stars | 15468 |
| Forks | 1569 |
| Licence | CC0-1.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1` |
| Retrieved at | 2026-11-14T19:09:02.285653+00:00 |
| Files in this snapshot | 110 |

## Directory tree

```text
api/  (3 files)
  docs/  (2 files)
    generate-docs.sh
    template.hbs
  mailinabox.yml
conf/  (26 files)
  fail2ban/  (7 files)
    filter.d/  (6 files)
      … 6 files under this directory
    jails.conf
  zpush/  (5 files)
    autodiscover_config.php
    backend_caldav.php
    backend_carddav.php
    backend_combined.php
    backend_imap.php
  dovecot-mailboxes.conf
  ios-profile.xml
  mailinabox.service
  mozilla-autoconfig.xml
  mta-sts.txt
  munin.service
  nginx-alldomains.conf
  nginx-primaryonly.conf
  nginx-ssl.conf
  nginx-top.conf
  nginx.conf
  postfix_outgoing_mail_header_filters
  sieve-spam.txt
  www_default.html
management/  (32 files)
  templates/  (15 files)
    aliases.html
    custom-dns.html
    external-dns.html
    index.html
    login.html
    mail-guide.html
    mfa.html
    munin.html
    ssl.html
    sync-guide.html
    system-backup.html
    system-status.html
    users.html
    web.html
    welcome.html
  auth.py
  backup.py
  cli.py
  csr_country_codes.tsv
  daemon.py
  daily_tasks.sh
  dns_update.py
  email_administrator.py
  mail_log.py
  mailconfig.py
  mfa.py
  munin_start.sh
  ssl_certificates.py
  status_checks.py
  utils.py
  web_update.py
  wsgi.py
setup/  (22 files)
  bootstrap.sh
  dkim.sh
  dns.sh
  firstuser.sh
  functions.sh
  mail-dovecot.sh
  mail-postfix.sh
  mail-users.sh
  management.sh
  migrate.py
  munin.sh
  network-checks.sh
  nextcloud.sh
  preflight.sh
  questions.sh
  spamassassin.sh
  ssl.sh
  start.sh
  system.sh
  web.sh
  webmail.sh
  zpush.sh
tests/  (7 files)
  fail2ban.py
  pip-requirements.txt
  test_dns.py
  test_mail.py
  test_smtp_server.py
  tls.py
  tls_results.txt
tools/  (10 files)
  archive_conf_files.sh
  dns_update
  editconf.py
  mail.py
  owncloud-restore.sh
  owncloud-unlockadmin.sh
  parse-nginx-log-bootstrap-accesses.py
  readable_bash.py
  ssl_cleanup
  web_update
.editorconfig
.gitignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
Vagrantfile
pyproject.toml
security.md
```

## Entry points

- [management/backup.py:625](https://github.com/mail-in-a-box/mailinabox/blob/b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1/management/backup.py#L625)
- [management/daemon.py:45](https://github.com/mail-in-a-box/mailinabox/blob/b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1/management/daemon.py#L45)
- [management/dns_update.py:1097](https://github.com/mail-in-a-box/mailinabox/blob/b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1/management/dns_update.py#L1097)
- [management/mail_log.py:787](https://github.com/mail-in-a-box/mailinabox/blob/b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1/management/mail_log.py#L787)
- [management/mailconfig.py:718](https://github.com/mail-in-a-box/mailinabox/blob/b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1/management/mailconfig.py#L718)
- [management/ssl_certificates.py:680](https://github.com/mail-in-a-box/mailinabox/blob/b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1/management/ssl_certificates.py#L680)
- [management/status_checks.py:1168](https://github.com/mail-in-a-box/mailinabox/blob/b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1/management/status_checks.py#L1168)
- [management/utils.py:212](https://github.com/mail-in-a-box/mailinabox/blob/b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1/management/utils.py#L212)
- [management/wsgi.py:6](https://github.com/mail-in-a-box/mailinabox/blob/b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1/management/wsgi.py#L6)
- [setup/migrate.py:271](https://github.com/mail-in-a-box/mailinabox/blob/b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1/setup/migrate.py#L271)
- [tools/readable_bash.py:482](https://github.com/mail-in-a-box/mailinabox/blob/b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1/tools/readable_bash.py#L482)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 12 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /, ROUTE /login, ROUTE /logout, ROUTE /mail/use… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| management package | library | Observed | Groups 6 file(s) under management package (observed from repository paths and static analysis). Observed top-level classes: AuthService. Observed top-level functions: disable_mfa, do_web_update, enable_mfa, get_domains_… |
| setup package | library | Observed | Groups 21 file(s) under setup package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 7 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: IsBlocked. Observed top-level functions: http_test, imap_test, managesieve_test, pop_test, restart_fail2ban_… |
| tools package | library | Observed | Groups 6 file(s) under tools package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `api/mailinabox.yml` (config)
- `pyproject.toml` (manifest)

## Top-level layout

- `management` — 32 analysed file(s)
- `conf` — 26 analysed file(s)
- `setup` — 22 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `tools` — 10 analysed file(s)
- `tests` — 7 analysed file(s)
- `api` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File tools/mail.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `b71c2e1ca6df9c56392ba0a2adbb05e02569d4c1` is the revision these paths and observations refer to.
