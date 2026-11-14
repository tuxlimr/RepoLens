# Project structure: papercups-io/papercups

**Analysed commit:** `6a6f5adc7f0cef5813b2c2f1c0659922defaf976`

**Commit reference:** [6a6f5adc7f0cef5813b2c2f1c0659922defaf976](https://github.com/papercups-io/papercups/commit/6a6f5adc7f0cef5813b2c2f1c0659922defaf976)

**Tree at this commit:** [papercups-io/papercups@6a6f5adc7f0c](https://github.com/papercups-io/papercups/tree/6a6f5adc7f0cef5813b2c2f1c0659922defaf976)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | papercups-io/papercups |
| Description | Open-source live customer chat |
| Stars | 6123 |
| Forks | 582 |
| Licence | MIT |
| Language | Elixir |
| Default branch | master |
| Analysed commit | `6a6f5adc7f0cef5813b2c2f1c0659922defaf976` |
| Retrieved at | 2026-11-14T19:14:09.970075+00:00 |
| Files in this snapshot | 681 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (2 files)
    papercups.yml
    release.yml
  pull_request_template.md
assets/  (217 files)
  public/  (20 files)
    github.svg
    gmail.svg
    hubspot.svg
    index.html
    intercom.svg
    jira-v0.svg
    jira.svg
    logo.svg
    manifest.json
    mattermost.svg
    microsoft-teams.svg
    robots.txt
    salesforce.svg
    ses.svg
    sheets.svg
    slack.svg
    twilio.svg
    whatsapp-v2.svg
    whatsapp.svg
    zendesk.svg
  src/  (192 files)
    components/  (173 files)
      … 173 files under this directory
    App.css
    App.tsx
    analytics.ts
    api.ts
    config.ts
    constants.ts
    index.css
    index.tsx
    logger.tsx
    logo.svg
    presence.ts
    react-app-env.d.ts
    serviceWorker.ts
    setupTests.ts
    socket.ts
    storage.ts
    types.ts
    utils.test.ts
    utils.ts
  .gitignore
  .prettierrc.js
  README.md
  package.json
  tsconfig.json
config/  (5 files)
  config.exs
  dev.exs
  prod.exs
  runtime.exs
  test.exs
docs/  (1 files)
  examples/  (1 files)
    add_conversations_api.md
lib/  (247 files)
  chat_api/  (119 files)
    accounts/  (3 files)
      … 3 files under this directory
    api_keys/  (1 files)
      … 1 files under this directory
    auth/  (1 files)
      … 1 files under this directory
    aws/  (1 files)
      … 1 files under this directory
    browser_replay_events/  (1 files)
      … 1 files under this directory
    browser_sessions/  (1 files)
      … 1 files under this directory
    canned_responses/  (1 files)
      … 1 files under this directory
    companies/  (1 files)
      … 1 files under this directory
    conversations/  (3 files)
      … 3 files under this directory
    customers/  (1 files)
      … 1 files under this directory
    emails/  (4 files)
      … 4 files under this directory
    event_subscriptions/  (1 files)
      … 1 files under this directory
    files/  (1 files)
      … 1 files under this directory
    forwarding_addresses/  (1 files)
      … 1 files under this directory
    github/  (4 files)
      … 4 files under this directory
    google/  (6 files)
      … 6 files under this directory
    hubspot/  (2 files)
      … 2 files under this directory
    inboxes/  (2 files)
      … 2 files under this directory
    intercom/  (2 files)
      … 2 files under this directory
    issues/  (3 files)
      … 3 files under this directory
    lambdas/  (1 files)
      … 1 files under this directory
    mailers/  (3 files)
      … 3 files under this directory
    mattermost/  (6 files)
      … 6 files under this directory
    mentions/  (1 files)
      … 1 files under this directory
    messages/  (4 files)
      … 4 files under this directory
    newsletters/  (1 files)
      … 1 files under this directory
    notes/  (1 files)
      … 1 files under this directory
    reporting/  (1 files)
      … 1 files under this directory
    slack/  (8 files)
      … 8 files under this directory
    slack_authorizations/  (2 files)
      … 2 files under this directory
    slack_conversation_threads/  (1 files)
      … 1 files under this directory
    tags/  (3 files)
      … 3 files under this directory
    twilio/  (3 files)
      … 3 files under this directory
    user_invitations/  (1 files)
      … 1 files under this directory
    users/  (3 files)
      … 3 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    widget_settings/  (1 files)
      … 1 files under this directory
    accounts.ex
    api_keys.ex
    application.ex
    aws.ex
    billing.ex
    browser_replay_events.ex
    browser_sessions.ex
    canned_responses.ex
    companies.ex
    conversations.ex
    customers.ex
    emails.ex
    event_subscriptions.ex
    files.ex
    forwarding_addresses.ex
    github.ex
    google.ex
    hubspot.ex
    inboxes.ex
    intercom.ex
    issues.ex
    lambdas.ex
    mattermost.ex
    mentions.ex
    … 14 more files
  chat_api_web/  (96 files)
    channels/  (6 files)
      … 6 files under this directory
    controllers/  (44 files)
      … 44 files under this directory
    views/  (35 files)
      … 35 files under this directory
    api_auth_error_handler.ex
    api_auth_plug.ex
    endpoint.ex
    ensure_role_plug.ex
    ensure_user_enabled_plug.ex
    gettext.ex
    ip_address_plug.ex
    presence.ex
    public_api_auth_plug.ex
    router.ex
    telemetry.ex
  mix/  (10 files)
    tasks/  (10 files)
      … 10 files under this directory
  workers/  (19 files)
    archive_stale_closed_conversations.ex
    archive_stale_free_tier_conversations.ex
    enable_gmail_inbox_sync.ex
    example.ex
    message_created_actions.ex
    process_ses_event.ex
    save_browser_replay_event.ex
    send_account_conversation_reminders.ex
    send_all_conversation_reminders.ex
    send_conversation_reply_email.ex
    send_gmail_notification.ex
    send_mention_notification.ex
    send_pg_newsletter.ex
    send_push_notifications.ex
    send_ses_reply_email.ex
    send_user_invitation_email.ex
    send_welcome_email.ex
    sync_gmail_inbox.ex
    sync_gmail_inboxes.ex
  chat_api.ex
  chat_api_web.ex
  release.ex
priv/  (95 files)
  gettext/  (2 files)
    en/  (1 files)
      … 1 files under this directory
    errors.pot
  repo/  (93 files)
    migrations/  (92 files)
      … 92 files under this directory
    seeds.exs
rel/  (4 files)
  overlays/  (4 files)
    createdb.sh
    migrate.sh
    rollback.sh
    seed.sh
scripts/  (4 files)
  lambdas/  (2 files)
    send-email-to-webhook/  (2 files)
      … 2 files under this directory
  compile_watch.sh
  ses_setup.sh
test/  (79 files)
  chat_api/  (33 files)
    conversations/  (1 files)
      … 1 files under this directory
    accounts_test.exs
    api_keys_test.exs
    aws_test.exs
    browser_replay_events_test.exs
    browser_sessions_test.exs
    canned_responses_test.exs
    companies_test.exs
    conversations_test.exs
    customers_test.exs
    emails_test.exs
    event_subscriptions_test.exs
    forwarding_addresses_test.exs
    github_test.exs
    google_test.exs
    hubspot_test.exs
    inboxes_test.exs
    intercom_test.exs
    issues_test.exs
    lambdas_test.exs
    mentions_test.exs
    messages_test.exs
    notes_test.exs
    reporting_test.exs
    slack_authorizations_test.exs
    … 8 more files
  chat_api_web/  (38 files)
    channels/  (4 files)
      … 4 files under this directory
    controllers/  (28 files)
      … 28 files under this directory
    plugs/  (1 files)
      … 1 files under this directory
    views/  (2 files)
      … 2 files under this directory
    api_auth_plug_test.exs
    ensure_role_plug_test.exs
    ensure_user_enabled_plug_test.exs
  support/  (4 files)
    channel_case.ex
    conn_case.ex
    data_case.ex
    factory.ex
  workers/  (3 files)
    process_ses_event_test.exs
    send_conversation_reply_email_test.exs
    send_ses_reply_email_test.exs
  test_helper.exs
.dockerignore
.env.example
.formatter.exs
.gitattributes
.gitignore
.nvmrc
.tool-versions
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
Procfile
README.md
app.json
compile
dev.Dockerfile
docker-compose.yml
docker-entrypoint-dev.sh
docker-entrypoint.sh
elixir_buildpack.config
mix.exs
mix.lock
phoenix_static_buildpack.config
```

## Entry points

- [scripts/lambdas/send-email-to-webhook/index.js](https://github.com/papercups-io/papercups/blob/6a6f5adc7f0cef5813b2c2f1c0659922defaf976/scripts/lambdas/send-email-to-webhook/index.js)
- [assets/src/App.tsx](https://github.com/papercups-io/papercups/blob/6a6f5adc7f0cef5813b2c2f1c0659922defaf976/assets/src/App.tsx)
- [assets/src/index.tsx](https://github.com/papercups-io/papercups/blob/6a6f5adc7f0cef5813b2c2f1c0659922defaf976/assets/src/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| assets package | library | Observed | Groups 153 file(s) under assets package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 18 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 24 file(s) under external integrations (observed from repository paths and static analysis). |
| rel package | library | Observed | Groups 4 file(s) under rel package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 79 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.env.example` (config)
- `.github/workflows/papercups.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `Dockerfile` (container)
- `app.json` (config)
- `assets/package.json` (manifest)
- `assets/public/manifest.json` (config)
- `assets/tsconfig.json` (config)
- `docker-compose.yml` (container)
- `scripts/lambdas/send-email-to-webhook/package.json` (manifest)

## Top-level layout

- `lib` — 247 analysed file(s)
- `assets` — 217 analysed file(s)
- `priv` — 95 analysed file(s)
- `test` — 79 analysed file(s)
- `(root files)` — 24 analysed file(s)
- `.github` — 5 analysed file(s)
- `config` — 5 analysed file(s)
- `rel` — 4 analysed file(s)
- `scripts` — 4 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `6a6f5adc7f0cef5813b2c2f1c0659922defaf976` is the revision these paths and observations refer to.
