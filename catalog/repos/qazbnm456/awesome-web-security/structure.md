# Project structure: qazbnm456/awesome-web-security

**Analysed commit:** `23b4ecc5ec5949dcae14bd2178c81172bb6ac862`

**Commit reference:** [23b4ecc5ec5949dcae14bd2178c81172bb6ac862](https://github.com/qazbnm456/awesome-web-security/commit/23b4ecc5ec5949dcae14bd2178c81172bb6ac862)

**Tree at this commit:** [qazbnm456/awesome-web-security@23b4ecc5ec59](https://github.com/qazbnm456/awesome-web-security/tree/23b4ecc5ec5949dcae14bd2178c81172bb6ac862)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | qazbnm456/awesome-web-security |
| Description | 🐶 A curated list of Web Security materials and resources. |
| Stars | 14059 |
| Forks | 1850 |
| Licence | Not detected |
| Language | Python |
| Default branch | master |
| Analysed commit | `23b4ecc5ec5949dcae14bd2178c81172bb6ac862` |
| Retrieved at | 2026-11-14T19:09:35.542394+00:00 |
| Files in this snapshot | 130 |

## Directory tree

```text
.claude-plugin/  (1 files)
  marketplace.json
.github/  (10 files)
  ISSUE_TEMPLATE/  (1 files)
    propose-resource.yml
  workflows/  (7 files)
    content-drift.yml
    diff-sentry.yml
    health-link-check.yml
    post-merge-archive.yml
    pr-review-backlog.yml
    pr-review-publish.yml
    pr-review.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
.vscode/  (1 files)
  settings.json
data/  (94 files)
  entries/  (91 files)
    angularjs.yml
    aws.yml
    azure.yml
    blogs.yml
    browser-backend.yml
    browser-frontend.yml
    cheetsheets.yml
    clickjacking.yml
    command-injection.yml
    community.yml
    crypto.yml
    csrf.yml
    csv-injection.yml
    deserialization.yml
    digests.yml
    dns-rebinding.yml
    evasions-authentication.yml
    evasions-csp.yml
    evasions-jsmvc.yml
    evasions-waf.yml
    evasions-xxe.yml
    fingerprint.yml
    forums.yml
    ftp-injection.yml
    … 67 more files
  templates/  (2 files)
    postamble.md
    preamble.md
  categories.yml
scripts/  (15 files)
  ci/  (10 files)
    templates/  (4 files)
      … 4 files under this directory
    archive.py
    check_content_drift.py
    port_legacy_pr.py
    pr_review.py
    publish_review.py
    triage_dead_links.py
  generate.py
  migrate.py
  verify_anchors.py
  verify_schema.py
  verify_skill.sh
skills/  (1 files)
  awesome-web-security/  (1 files)
    SKILL.md
.gitignore
CLAUDE.md
CONTRIBUTING.md
README-jp.md
README-zh.md
README.md
RUBRIC.md
code-of-conduct.md
```

## Entry points

- [scripts/ci/archive.py:335](https://github.com/qazbnm456/awesome-web-security/blob/23b4ecc5ec5949dcae14bd2178c81172bb6ac862/scripts/ci/archive.py#L335)
- [scripts/ci/check_content_drift.py:344](https://github.com/qazbnm456/awesome-web-security/blob/23b4ecc5ec5949dcae14bd2178c81172bb6ac862/scripts/ci/check_content_drift.py#L344)
- [scripts/ci/port_legacy_pr.py:195](https://github.com/qazbnm456/awesome-web-security/blob/23b4ecc5ec5949dcae14bd2178c81172bb6ac862/scripts/ci/port_legacy_pr.py#L195)
- [scripts/ci/pr_review.py:833](https://github.com/qazbnm456/awesome-web-security/blob/23b4ecc5ec5949dcae14bd2178c81172bb6ac862/scripts/ci/pr_review.py#L833)
- [scripts/ci/publish_review.py:234](https://github.com/qazbnm456/awesome-web-security/blob/23b4ecc5ec5949dcae14bd2178c81172bb6ac862/scripts/ci/publish_review.py#L234)
- [scripts/ci/triage_dead_links.py:719](https://github.com/qazbnm456/awesome-web-security/blob/23b4ecc5ec5949dcae14bd2178c81172bb6ac862/scripts/ci/triage_dead_links.py#L719)
- [scripts/generate.py:380](https://github.com/qazbnm456/awesome-web-security/blob/23b4ecc5ec5949dcae14bd2178c81172bb6ac862/scripts/generate.py#L380)
- [scripts/migrate.py:587](https://github.com/qazbnm456/awesome-web-security/blob/23b4ecc5ec5949dcae14bd2178c81172bb6ac862/scripts/migrate.py#L587)
- [scripts/verify_anchors.py:86](https://github.com/qazbnm456/awesome-web-security/blob/23b4ecc5ec5949dcae14bd2178c81172bb6ac862/scripts/verify_anchors.py#L86)
- [scripts/verify_schema.py:130](https://github.com/qazbnm456/awesome-web-security/blob/23b4ecc5ec5949dcae14bd2178c81172bb6ac862/scripts/verify_schema.py#L130)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 92 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 10 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Entry, ParsedReadme, Section, YamlError, _BlockInternalRedirect, _NoRedirect. Observed to… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/propose-resource.yml` (config)
- `.github/workflows/content-drift.yml` (ci)
- `.github/workflows/diff-sentry.yml` (ci)
- `.github/workflows/health-link-check.yml` (ci)
- `.github/workflows/post-merge-archive.yml` (ci)
- `.github/workflows/pr-review-backlog.yml` (ci)
- `.github/workflows/pr-review-publish.yml` (ci)
- `.github/workflows/pr-review.yml` (ci)
- `.vscode/settings.json` (config)
- `data/categories.yml` (config)
- `data/entries/angularjs.yml` (config)
- `data/entries/aws.yml` (config)
- `data/entries/azure.yml` (config)
- `data/entries/blogs.yml` (config)
- `data/entries/browser-backend.yml` (config)
- `data/entries/browser-frontend.yml` (config)
- `data/entries/cheetsheets.yml` (config)
- `data/entries/clickjacking.yml` (config)
- `data/entries/command-injection.yml` (config)
- `data/entries/community.yml` (config)
- `data/entries/crypto.yml` (config)
- `data/entries/csrf.yml` (config)
- `data/entries/csv-injection.yml` (config)
- `data/entries/deserialization.yml` (config)
- `data/entries/digests.yml` (config)
- `data/entries/dns-rebinding.yml` (config)
- `data/entries/evasions-authentication.yml` (config)
- `data/entries/evasions-csp.yml` (config)
- `data/entries/evasions-jsmvc.yml` (config)
- `data/entries/evasions-waf.yml` (config)
- `data/entries/evasions-xxe.yml` (config)
- `data/entries/fingerprint.yml` (config)
- `data/entries/forums.yml` (config)
- `data/entries/ftp-injection.yml` (config)
- `data/entries/jwt.yml` (config)
- `data/entries/miscellaneous.yml` (config)
- `data/entries/nfs.yml` (config)
- `data/entries/oauth.yml` (config)
- `data/entries/open-redirect.yml` (config)
- `data/entries/orm-injection.yml` (config)
- `data/entries/osint.yml` (config)
- `data/entries/pocs-database.yml` (config)
- `data/entries/practices-application.yml` (config)
- `data/entries/practices-aws.yml` (config)
- `data/entries/practices-modsecurity.yml` (config)
- `data/entries/practices-xss.yml` (config)
- `data/entries/prototype-pollution.yml` (config)
- `data/entries/rails.yml` (config)
- `data/entries/reactjs.yml` (config)
- `data/entries/relative-path-overwrite.yml` (config)
- `data/entries/saml.yml` (config)
- `data/entries/social-engineering-database.yml` (config)
- `data/entries/sql-injection.yml` (config)
- `data/entries/ssl-tls.yml` (config)
- `data/entries/ssrf.yml` (config)
- `data/entries/sub-domain-enumeration.yml` (config)
- `data/entries/tools-auditing.yml` (config)
- `data/entries/tools-code-generating.yml` (config)
- `data/entries/tools-command-injection.yml` (config)
- `data/entries/tools-csrf.yml` (config)
- `data/entries/tools-decompiler.yml` (config)
- `data/entries/tools-detecting.yml` (config)
- `data/entries/tools-disassembler.yml` (config)
- `data/entries/tools-dns-rebinding.yml` (config)
- `data/entries/tools-fuzzing.yml` (config)
- `data/entries/tools-leaking.yml` (config)
- `data/entries/tools-osint.yml` (config)
- `data/entries/tools-others.yml` (config)
- `data/entries/tools-penetration-testing.yml` (config)
- `data/entries/tools-preventing.yml` (config)
- `data/entries/tools-proxy.yml` (config)
- `data/entries/tools-scanning.yml` (config)
- `data/entries/tools-sql-injection.yml` (config)
- `data/entries/tools-ssrf.yml` (config)
- `data/entries/tools-sub-domain-enumeration.yml` (config)
- `data/entries/tools-template-injection.yml` (config)
- `data/entries/tools-webshell.yml` (config)
- `data/entries/tools-xss.yml` (config)
- `data/entries/tools-xxe.yml` (config)
- `data/entries/tricks-clickjacking.yml` (config)
- `data/entries/tricks-csrf.yml` (config)
- `data/entries/tricks-deserialization.yml` (config)
- `data/entries/tricks-ftp-injection.yml` (config)
- `data/entries/tricks-header-injection.yml` (config)
- `data/entries/tricks-nosql-injection.yml` (config)
- `data/entries/tricks-oauth.yml` (config)
- `data/entries/tricks-others.yml` (config)
- `data/entries/tricks-rce.yml` (config)
- `data/entries/tricks-sql-injection.yml` (config)
- `data/entries/tricks-ssrf.yml` (config)
- `data/entries/tricks-url.yml` (config)
- `data/entries/tricks-web-cache-poisoning.yml` (config)
- `data/entries/tricks-xss.yml` (config)
- `data/entries/tricks-xxe.yml` (config)
- `data/entries/twitter-users.yml` (config)
- `data/entries/upload.yml` (config)
- `data/entries/web-cache-poisoning.yml` (config)
- `data/entries/web-shell.yml` (config)
- `data/entries/webmail.yml` (config)
- `data/entries/xss.yml` (config)
- `data/entries/xxe.yml` (config)

## Top-level layout

- `data` — 94 analysed file(s)
- `scripts` — 15 analysed file(s)
- `.github` — 10 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.claude-plugin` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `skills` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `23b4ecc5ec5949dcae14bd2178c81172bb6ac862` is the revision these paths and observations refer to.
