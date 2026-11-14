# Project structure: wwebjs/whatsapp-web.js

**Analysed commit:** `eb076b0c4075f5c295d5633f4c587d02ef4e5cf1`

**Commit reference:** [eb076b0c4075f5c295d5633f4c587d02ef4e5cf1](https://github.com/wwebjs/whatsapp-web.js/commit/eb076b0c4075f5c295d5633f4c587d02ef4e5cf1)

**Tree at this commit:** [wwebjs/whatsapp-web.js@eb076b0c4075](https://github.com/wwebjs/whatsapp-web.js/tree/eb076b0c4075f5c295d5633f4c587d02ef4e5cf1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | wwebjs/whatsapp-web.js |
| Description | A WhatsApp client library for NodeJS that connects through the WhatsApp Web browser app |
| Stars | 22909 |
| Forks | 5203 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `eb076b0c4075f5c295d5633f4c587d02ef4e5cf1` |
| Retrieved at | 2026-11-14T19:11:06.054911+00:00 |
| Files in this snapshot | 184 |

## Directory tree

```text
.github/  (23 files)
  ISSUE_TEMPLATE/  (3 files)
    01-bug_report.yml
    02-feature_request.yml
    config.yml
  workflows/  (9 files)
    format-issue-bug.yml
    issue-triage.yml
    labels-sync.yml
    lint.yml
    pr-triage.yml
    release.yml
    stale.yml
    tests.yml
    update.yml
  CODE_OF_CONDUCT.md
  COMMIT_CONVENTION.md
  CONTRIBUTING.md
  DISCLAIMER.md
  FUNDING.yml
  SUPPORT.md
  dependabot.yml
  issue-labeler.yml
  labels.yml
  pr-labeler.yml
  pull_request_template.md
.husky/  (2 files)
  commit-msg
  pre-commit
docs/  (88 files)
  css/  (1 files)
    baseline.css
  scripts/  (6 files)
    jsdoc-toc.js
    lang-css.js
    linenumber.js
    prettify.js
    scrollanchor.js
    tree.jquery.js
  Base.html
  BaseAuthStrategy.html
  Broadcast.html
  BusinessContact.html
  Buttons.html
  CNAME
  Call.html
  Channel.html
  Chat.html
  Client.html
  Client.js.html
  ClientInfo.html
  Contact.html
  GroupChat.html
  GroupNotification.html
  InterfaceController.html
  Label.html
  LegacySessionAuth.html
  List.html
  LocalAuth.html
  LocalWebCache.html
  Location.html
  Message.html
  MessageMedia.html
  … 57 more files
src/  (43 files)
  authStrategies/  (4 files)
    BaseAuthStrategy.js
    LocalAuth.js
    NoAuth.js
    RemoteAuth.js
  factories/  (2 files)
    ChatFactory.js
    ContactFactory.js
  structures/  (27 files)
    Base.js
    Broadcast.js
    BusinessContact.js
    Buttons.js
    Call.js
    Channel.js
    Chat.js
    ClientInfo.js
    Contact.js
    GroupChat.js
    GroupNotification.js
    Label.js
    List.js
    Location.js
    Message.js
    MessageMedia.js
    Order.js
    Payment.js
    Poll.js
    PollVote.js
    PrivateChat.js
    PrivateContact.js
    Product.js
    ProductMetadata.js
    … 3 more files
  util/  (5 files)
    Injected/  (1 files)
      … 1 files under this directory
    Constants.js
    InterfaceController.js
    Puppeteer.js
    Util.js
  webCache/  (4 files)
    LocalWebCache.js
    RemoteWebCache.js
    WebCache.js
    WebCacheFactory.js
  Client.js
tests/  (6 files)
  structures/  (3 files)
    chat.js
    group.js
    message.js
  README.md
  client.js
  helper.js
tools/  (4 files)
  version-checker/  (2 files)
    .version
    update-version
  changelog.sh
  publish
.editorconfig
.env.example
.gitattributes
.gitignore
.jsdoc.json
.lintstagedrc.json
.npmignore
.prettierignore
.prettierrc.json
LICENSE
README.md
commitlint.config.js
eslint.config.mjs
example.js
index.d.ts
index.js
package.json
shell.js
```

## Entry points

- [index.js](https://github.com/wwebjs/whatsapp-web.js/blob/eb076b0c4075f5c295d5633f4c587d02ef4e5cf1/index.js)
- [src/structures/index.js](https://github.com/wwebjs/whatsapp-web.js/blob/eb076b0c4075f5c295d5633f4c587d02ef4e5cf1/src/structures/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| authStrategies package | library | Observed | Groups 4 file(s) under authstrategies package (observed from repository paths and static analysis). |
| Client.js package | library | Observed | Groups 1 file(s) under client.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| factories package | library | Observed | Groups 2 file(s) under factories package (observed from repository paths and static analysis). |
| structures package | library | Observed | Groups 27 file(s) under structures package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 6 file(s) under tests (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 1 file(s) under tools package (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 5 file(s) under util package (observed from repository paths and static analysis). |
| webCache package | library | Observed | Groups 4 file(s) under webcache package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/01-bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/02-feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/issue-labeler.yml` (config)
- `.github/labels.yml` (config)
- `.github/pr-labeler.yml` (config)
- `.github/workflows/format-issue-bug.yml` (ci)
- `.github/workflows/issue-triage.yml` (ci)
- `.github/workflows/labels-sync.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/pr-triage.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.github/workflows/update.yml` (ci)
- `.jsdoc.json` (config)
- `.lintstagedrc.json` (config)
- `.prettierrc.json` (config)
- `package.json` (manifest)

## Top-level layout

- `docs` — 88 analysed file(s)
- `src` — 43 analysed file(s)
- `.github` — 23 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `tests` — 6 analysed file(s)
- `tools` — 4 analysed file(s)
- `.husky` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `eb076b0c4075f5c295d5633f4c587d02ef4e5cf1` is the revision these paths and observations refer to.
