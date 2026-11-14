# Project structure: chaskiq/chaskiq

**Analysed commit:** `46dfdd11c63c6849ecde16a0dcc54d388e2613a3`

**Commit reference:** [46dfdd11c63c6849ecde16a0dcc54d388e2613a3](https://github.com/chaskiq/chaskiq/commit/46dfdd11c63c6849ecde16a0dcc54d388e2613a3)

**Tree at this commit:** [chaskiq/chaskiq@46dfdd11c63c](https://github.com/chaskiq/chaskiq/tree/46dfdd11c63c6849ecde16a0dcc54d388e2613a3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | chaskiq/chaskiq |
| Description | A full featured Live Chat, Support & Marketing platform, alternative to Intercom, Drift, Crisp. |
| Stars | 3584 |
| Forks | 510 |
| Licence | Other |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `46dfdd11c63c6849ecde16a0dcc54d388e2613a3` |
| Retrieved at | 2026-11-14T19:15:15.003569+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.devcontainer/  (1 files)
  devcontainer.json
.docker-files/  (3 files)
  deps.sh
  node.sh
  pg.sh
.dockerdev/  (3 files)
  .bashrc
  .psqlrc
  Aptfile
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (5 files)
    anchore-analysis.yml
    docker-image-ghcr.yml
    dockerimage.yml
    rubocop-analysis.yml
    ruby.yml
  .stale.yml
.husky/  (1 files)
  pre-commit
app/  (725 files)
  assets/  (7 files)
    builds/  (1 files)
      … 1 files under this directory
    config/  (1 files)
      … 1 files under this directory
    images/  (1 files)
      … 1 files under this directory
    javascripts/  (1 files)
      … 1 files under this directory
    stylesheets/  (3 files)
      … 3 files under this directory
  channels/  (7 files)
    application_cable/  (2 files)
      … 2 files under this directory
    agent_channel.rb
    events_channel.rb
    messenger_events_channel.rb
    presence_channel.rb
    rtc_channel.rb
  controllers/  (27 files)
    agents/  (7 files)
      … 7 files under this directory
    api/  (7 files)
      … 7 files under this directory
    concerns/  (5 files)
      … 5 files under this directory
    api_controller.rb
    application_controller.rb
    articles_controller.rb
    client_tester_controller.rb
    graphql_controller.rb
    home_controller.rb
    oembed_controller.rb
    widgets_controller.rb
  graphql/  (155 files)
    helpers/  (1 files)
      … 1 files under this directory
    mutations/  (94 files)
      … 94 files under this directory
    types/  (59 files)
      … 59 files under this directory
    chaskiq_schema.rb
  helpers/  (2 files)
    application_helper.rb
    sanitize_helpers.rb
  identities/  (1 files)
    app_identity.rb
  importers/  (1 files)
    list_importer.rb
  javascript/  (330 files)
    docs/  (1 files)
      … 1 files under this directory
    packages/  (220 files)
      … 220 files under this directory
    src/  (103 files)
      … 103 files under this directory
    application.js
    article.js
    docs.js
    embed.js
    locales.js
    twilio_phone_package.js
  jobs/  (19 files)
    api_channel_notificator_job.rb
    app_user_event_job.rb
    app_user_trigger_job.rb
    application_job.rb
    audit_job.rb
    contact_merger_job.rb
    conversation_channel_sync_job.rb
    data_enrichment_job.rb
    email_chat_notifier_job.rb
    event_trigger_processor_job.rb
    hook_message_receiver_job.rb
    list_importer_job.rb
    mail_importer_job.rb
    mail_sender_job.rb
    offline_checker_job.rb
    outgoing_webhook_dispatcher_job.rb
    outgoing_webhook_job.rb
    ses_sender_job.rb
    sns_receiver_job.rb
  mailers/  (5 files)
    application_mailer.rb
    assignee_mailer.rb
    campaign_mailer.rb
    chat_notifier_mailer.rb
    import_mailer.rb
  models/  (71 files)
    concerns/  (13 files)
      … 13 files under this directory
    events/  (12 files)
      … 12 files under this directory
    agent.rb
    agent_team.rb
    app.rb
    app_package.rb
    app_package_integration.rb
    app_user.rb
    application_record.rb
    article.rb
    article_collection.rb
    article_content.rb
    article_setting.rb
    assignment_rule.rb
    audit.rb
    auth_identity.rb
    banner.rb
    bot_task.rb
    campaign.rb
    collection_section.rb
    conversation.rb
    conversation_channel.rb
    conversation_part.rb
    conversation_part_block.rb
    conversation_part_channel_source.rb
    conversation_part_content.rb
    … 22 more files
  policies/  (1 files)
    app_policy.rb
  services/  (50 files)
    dante/  (10 files)
      … 10 files under this directory
    data_enrichment_service/  (1 files)
      … 1 files under this directory
    digital_ocean/  (1 files)
      … 1 files under this directory
    message_apis/  (19 files)
      … 19 files under this directory
    payment_services/  (2 files)
      … 2 files under this directory
    plugins/  (1 files)
      … 1 files under this directory
    action_trigger.rb
    action_trigger_factory.rb
    agent_dashboard.rb
    app_package_dashboard.rb
    app_user_dashboard.rb
    base_service.rb
    dashboard.rb
    eu_countries.rb
    fetch_link_card_service.rb
    origin_validator.rb
    outgoing_webhook_service.rb
    permissions_service.rb
    plugin_schema_validator.rb
    segment_factory.rb
    user_finder.rb
    visit_collector.rb
  validators/  (2 files)
    hex_validator.rb
    url_validator.rb
  views/  (47 files)
    app_packages/  (3 files)
      … 3 files under this directory
    assignee_mailer/  (1 files)
      … 1 files under this directory
    campaign_mailer/  (2 files)
      … 2 files under this directory
    campaigns/  (10 files)
      … 10 files under this directory
    chat_notifier_mailer/  (2 files)
      … 2 files under this directory
    client_tester/  (5 files)
      … 5 files under this directory
    devise/  (14 files)
      … 14 files under this directory
    home/  (2 files)
      … 2 files under this directory
    import_mailer/  (1 files)
      … 1 files under this directory
    layouts/  (6 files)
      … 6 files under this directory
    shared/  (1 files)
      … 1 files under this directory
bin/  (11 files)
  bundle
  dev
  heroku-web
  heroku-worker
  rails
  rake
  setup
  spring
  test
  update
  yarn
config/  (18 files)
  credentials/  (1 files)
    README.md
  environments/  (4 files)
    development.rb
    production.rb
    staging.rb
    test.rb
  initializers/  (5 files)
    app_subdomains.rb
    application_controller_renderer.rb
    assets.rb
    backtrace_silencers.rb
    before_start.rb
  anycable.yml
  application.rb
  boot.rb
  cable.yml
  chaskiq_boot.rb
  database.yml
  environment.rb
  i18n.yml
.codeclimate.yml
.dockerignore
.env.example
.eslintignore
.eslintrc.js
.gitignore
.prettierignore
.rspec
.rubocop.yml
.rubocop_todo.yml
.ruby-version
.unimportedrc.json
CODE_OF_CONDUCT.md
Dockerfile
Dockerfile.development
Gemfile
Gemfile.lock
LICENSE.txt
Procfile
Procfile.dev
Procfile.test
README.md
Rakefile
SECURITY.md
… 5 more files
```

## Entry points

- [app/javascript/src/App.tsx](https://github.com/chaskiq/chaskiq/blob/46dfdd11c63c6849ecde16a0dcc54d388e2613a3/app/javascript/src/App.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 26 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 479 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 40 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 70 file(s) under data layer (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 49 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 1 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.codeclimate.yml` (config)
- `.devcontainer/devcontainer.json` (config)
- `.dockerignore` (container)
- `.env.example` (config)
- `.github/.stale.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/anchore-analysis.yml` (ci)
- `.github/workflows/docker-image-ghcr.yml` (ci)
- `.github/workflows/dockerimage.yml` (ci)
- `.github/workflows/rubocop-analysis.yml` (ci)
- `.github/workflows/ruby.yml` (ci)
- `.rubocop.yml` (config)
- `.rubocop_todo.yml` (config)
- `.unimportedrc.json` (config)
- `Dockerfile` (container)
- `Dockerfile.development` (container)
- `app.json` (config)
- `app/javascript/packages/components/package.json` (manifest)
- `app/javascript/packages/docs/package.json` (manifest)
- `app/javascript/packages/messenger/package.json` (manifest)
- `app/javascript/packages/store/package.json` (manifest)
- `app/javascript/packages/store/src/graphql/package.json` (manifest)
- `app/javascript/src/locales/messenger-translations.json` (config)
- `config/anycable.yml` (config)
- `config/cable.yml` (config)
- `config/database.yml` (config)
- `config/i18n.yml` (config)

## Top-level layout

- `app` — 725 analysed file(s)
- `(root files)` — 29 analysed file(s)
- `config` — 18 analysed file(s)
- `bin` — 11 analysed file(s)
- `.github` — 9 analysed file(s)
- `.docker-files` — 3 analysed file(s)
- `.dockerdev` — 3 analysed file(s)
- `.devcontainer` — 1 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `46dfdd11c63c6849ecde16a0dcc54d388e2613a3` is the revision these paths and observations refer to.
