# Project structure: miurla/morphic

**Analysed commit:** `244ea609ab0d604f6c7020fee214ac087f0129c9`

**Commit reference:** [244ea609ab0d604f6c7020fee214ac087f0129c9](https://github.com/miurla/morphic/commit/244ea609ab0d604f6c7020fee214ac087f0129c9)

**Tree at this commit:** [miurla/morphic@244ea609ab0d](https://github.com/miurla/morphic/tree/244ea609ab0d604f6c7020fee214ac087f0129c9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | miurla/morphic |
| Description | An AI-powered search engine with a generative UI |
| Stars | 9329 |
| Forks | 2375 |
| Licence | Apache-2.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `244ea609ab0d604f6c7020fee214ac087f0129c9` |
| Retrieved at | 2026-11-14T19:13:34.585496+00:00 |
| Files in this snapshot | 659 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    feature_request.yml
  workflows/  (5 files)
    ci.yml
    close-search-provider-prs.yml
    docker-build.yml
    eval.yml
    release.yml
  FUNDING.yml
  dependabot.yml
.vscode/  (1 files)
  settings.json
app/  (37 files)
  api/  (18 files)
    advanced-search/  (1 files)
      … 1 files under this directory
    auth/  (2 files)
      … 2 files under this directory
    chat/  (2 files)
      … 2 files under this directory
    chats/  (3 files)
      … 3 files under this directory
    favicon/  (2 files)
      … 2 files under this directory
    feedback/  (2 files)
      … 2 files under this directory
    search/  (2 files)
      … 2 files under this directory
    upload/  (2 files)
      … 2 files under this directory
    usage/  (2 files)
      … 2 files under this directory
  auth/  (10 files)
    __tests__/  (1 files)
      … 1 files under this directory
    admin/  (1 files)
      … 1 files under this directory
    confirm/  (1 files)
      … 1 files under this directory
    error/  (1 files)
      … 1 files under this directory
    forgot-password/  (1 files)
      … 1 files under this directory
    login/  (1 files)
      … 1 files under this directory
    oauth/  (1 files)
      … 1 files under this directory
    sign-up/  (1 files)
      … 1 files under this directory
    sign-up-success/  (1 files)
      … 1 files under this directory
    update-password/  (1 files)
      … 1 files under this directory
  relay/  (2 files)
    [...path]/  (2 files)
      … 2 files under this directory
  search/  (4 files)
    [id]/  (2 files)
      … 2 files under this directory
    loading.tsx
    page.tsx
  globals.css
  layout.tsx
  page.tsx
components/  (164 files)
  __tests__/  (20 files)
    account-settings-dialog.test.tsx
    app-sidebar.test.tsx
    chat-cache-invalidation.test.tsx
    chat-cache.test.tsx
    chat-messages.test.tsx
    chat-panel.test.tsx
    draft-panel.test.tsx
    invitations-manager.test.tsx
    login-form.test.tsx
    member-role-manager.test.tsx
    message-actions.test.tsx
    render-message.test.tsx
    research-process-section.test.tsx
    reset-member-password-form.test.tsx
    search-mode-selector.test.tsx
    sign-up-form.test.tsx
    spec-block.test.tsx
    update-password-form.test.tsx
    usage-budget.test.tsx
    user-menu.test.tsx
  admin/  (3 files)
    invitations-manager.tsx
    member-role-manager.tsx
    reset-member-password-form.tsx
  artifact/  (8 files)
    artifact-content.tsx
    artifact-context.tsx
    artifact-root.tsx
    chat-artifact-container.tsx
    reasoning-content.tsx
    search-artifact-content.tsx
    todo-invocation-content.tsx
    tool-invocation-content.tsx
  draft/  (3 files)
    draft-card.tsx
    draft-panel.tsx
    draft-store.ts
  inspector/  (2 files)
    inspector-drawer.tsx
    inspector-panel.tsx
  library/  (5 files)
    __tests__/  (1 files)
      … 1 files under this directory
    library-context.tsx
    library-panel.tsx
    library-picker-dialog.tsx
    save-note-auth-dialog.tsx
  sidebar/  (16 files)
    __tests__/  (4 files)
      … 4 files under this directory
    chat-history-client.tsx
    chat-history-search.tsx
    chat-history-section.tsx
    chat-history-skeleton.tsx
    chat-menu-item.tsx
    clear-history-action.tsx
    home-link.test.tsx
    home-link.tsx
    library-menu-item.tsx
    new-chat-menu-item.tsx
    version-footer-skeleton.tsx
    version-footer.tsx
  ui/  (35 files)
    __tests__/  (1 files)
      … 1 files under this directory
    alert-dialog.tsx
    animated-logo.tsx
    avatar.tsx
    badge.tsx
    button.tsx
    card.tsx
    carousel.tsx
    checkbox.tsx
    collapsible.tsx
    command.tsx
    dialog.tsx
    drawer.tsx
    dropdown-menu.tsx
    hover-card.tsx
    icons.tsx
    index.ts
    input.tsx
    label.tsx
    password-input.tsx
    popover.tsx
    select.tsx
    separator.tsx
    sheet.tsx
    sidebar.tsx
    … 10 more files
  account-settings-dialog.tsx
  action-buttons.tsx
  answer-section.tsx
  app-sidebar.tsx
  attachment-preview.tsx
  auth-modal.tsx
  chat-error.tsx
  chat-footer-message.tsx
  chat-messages.tsx
  chat-panel.tsx
  chat-share.tsx
  chat.tsx
  citation-context.tsx
  citation-link.tsx
  collapsible-message.tsx
  current-user-avatar.tsx
  custom-link.tsx
  default-skeleton.tsx
  drag-overlay.tsx
  dynamic-tool-display.tsx
  error-modal.tsx
  external-link-items.tsx
  feedback-modal.tsx
  fetch-section.tsx
  … 48 more files
config/  (1 files)
  models/  (1 files)
    cloud.json
docs/  (4 files)
  CONFIGURATION.md
  DOCKER.md
  PRIVACY.md
  REVISE_ANALYTICS.md
drizzle/  (42 files)
  meta/  (18 files)
    0000_snapshot.json
    0001_snapshot.json
    0002_snapshot.json
    0003_snapshot.json
    0004_snapshot.json
    0005_snapshot.json
    0006_snapshot.json
    0007_snapshot.json
    0008_snapshot.json
    0009_snapshot.json
    0010_snapshot.json
    0011_snapshot.json
    0016_snapshot.json
    0018_snapshot.json
    0019_snapshot.json
    0020_snapshot.json
    0021_snapshot.json
    _journal.json
  0000_black_lifeguard.sql
  0001_thin_supreme_intelligence.sql
  0002_material_crystal.sql
  0003_heavy_whirlwind.sql
  0004_natural_wallow.sql
  0005_awesome_riptide.sql
  0006_brainy_wrecking_crew.sql
  0007_illegal_mephistopheles.sql
  0008_glamorous_riptide.sql
  0009_thankful_may_parker.sql
  0010_lonely_kang.sql
  0011_feedback_anonymization.sql
  0012_knowledge_library_notes.sql
  0013_library_files.sql
  0014_private_file_object_keys.sql
  0015_library_file_object_keys_only.sql
  0016_wrap_rls_current_setting.sql
  0017_usage_budget.sql
  0018_reconcile_usage_budget_snapshot.sql
  0019_rainy_jack_flag.sql
  0020_add_parts_search_fts.sql
  0021_add_spaces.sql
  relations.ts
  schema.ts
evals/  (30 files)
  datasets/  (3 files)
    draft-edits.json
    related-questions.json
    source-cards.json
  evaluators/  (4 files)
    __tests__/  (1 files)
      … 1 files under this directory
    draft-edits.ts
    related-questions.ts
    source-cards.ts
  lib/  (12 files)
    __tests__/  (5 files)
      … 5 files under this directory
    dataset.ts
    draft-edits.ts
    gate.ts
    otel.ts
    related-questions.ts
    source-cards.ts
    space-instructions.ts
  tasks/  (5 files)
    adaptive-answer.ts
    draft-turn.ts
    fixture-tools.ts
    quick-answer.ts
    run-answer-task.ts
  README.md
  run-draft-edits.ts
  run-related-questions.ts
  run-source-cards.ts
  run-space-instructions.ts
  thresholds.json
hooks/  (8 files)
  __tests__/  (1 files)
    user-hooks.test.tsx
  use-auth-check.tsx
  use-current-user-image.ts
  use-current-user-name.ts
  use-file-dropzone.ts
  use-keyboard-shortcut.ts
  use-mobile.tsx
  use-typewriter-cycle.ts
lib/  (323 files)
  __tests__/  (3 files)
    bot-protection.test.ts
    maintenance.test.ts
    search-mode-availability.test.ts
  actions/  (18 files)
    __tests__/  (8 files)
      … 8 files under this directory
    account.ts
    admin-views.ts
    admin.ts
    auth.ts
    chat.ts
    feedback.ts
    files.ts
    notes.ts
    site-feedback.ts
    spaces.ts
  agents/  (8 files)
    __tests__/  (3 files)
      … 3 files under this directory
    prompts/  (3 files)
      … 3 files under this directory
    researcher.ts
    title-generator.ts
  analytics/  (18 files)
    __tests__/  (5 files)
      … 5 files under this directory
    providers/  (1 files)
      … 1 files under this directory
    dispatch.ts
    genui-summary.ts
    index.ts
    posthog-client.ts
    relay-target.ts
    sanitize.ts
    track-account-event.ts
    track-adaptive-limit-event.ts
    track-chat-event.ts
    track-chat-limit-event.ts
    types.ts
    utils.ts
  auth/  (25 files)
    __tests__/  (8 files)
      … 8 files under this directory
    better-auth/  (7 files)
      … 7 files under this directory
    providers/  (3 files)
      … 3 files under this directory
    get-current-user.ts
    oauth-config.ts
    provider.ts
    rate-limit.ts
    redirect-target.ts
    request.ts
    types.ts
  chat-store/  (2 files)
    index.test.ts
    index.ts
  config/  (7 files)
    default-model.ts
    load-models-config.ts
    model-metadata.json
    model-selection-cookie.ts
    model-types.ts
    ollama-validator.ts
    search-modes.ts
  constants/  (1 files)
    index.ts
  contexts/  (3 files)
    app-user-context.tsx
    chat-context.tsx
    user-context.tsx
  db/  (12 files)
    __tests__/  (6 files)
      … 6 files under this directory
    actions.ts
    index.ts
    migrate.ts
    relations.ts
    schema.ts
    with-rls.ts
  draft/  (5 files)
    __tests__/  (2 files)
      … 2 files under this directory
    draft.ts
    prompt.ts
    revise.ts
  errors/  (5 files)
    __tests__/  (2 files)
      … 2 files under this directory
    deterministic-preparation-error.ts
    public-error.ts
    tool-error.ts
  firecrawl/  (3 files)
    client.ts
    index.ts
    types.ts
  hooks/  (2 files)
    use-copy-to-clipboard.ts
    use-media-query.ts
  model-selector/  (1 files)
    get-model-selector-data.ts
  models/  (2 files)
    __tests__/  (1 files)
      … 1 files under this directory
    fetch-models.ts
  ollama/  (2 files)
    client.ts
    types.ts
  rate-limit/  (5 files)
    __tests__/  (2 files)
      … 2 files under this directory
    adaptive-limit.ts
    chat-limits.ts
    guest-limit.ts
  render/  (33 files)
    __tests__/  (11 files)
      … 11 files under this directory
    components/  (9 files)
      … 9 files under this directory
    catalog.ts
    highlight-markers.ts
    linked-cards-markdown.ts
    migrations.ts
    parse-spec-block.ts
    prompt.ts
    registry.tsx
    revise-suggestions.ts
    schema.ts
    spec-fence.ts
    streamdown-spec.tsx
    strip-source-context-blocks.ts
    strip-spec-blocks.ts
  schema/  (3 files)
    fetch.tsx
    question.ts
    search.tsx
  spaces/  (1 files)
    space.ts
  storage/  (4 files)
    __tests__/  (2 files)
      … 2 files under this directory
    file-signature.ts
    r2-client.ts
  streaming/  (54 files)
    __tests__/  (3 files)
      … 3 files under this directory
    helpers/  (48 files)
      … 48 files under this directory
    create-chat-stream-response.ts
    create-ephemeral-chat-stream-response.ts
    types.ts
  supabase/  (7 files)
    __tests__/  (2 files)
      … 2 files under this directory
    admin.ts
    client.ts
    keys.ts
    middleware.ts
    server.ts
  tools/  (24 files)
    __tests__/  (5 files)
      … 5 files under this directory
    search/  (13 files)
      … 13 files under this directory
    draft.ts
    dynamic.ts
    fetch.ts
    question.ts
    search.ts
    todo.ts
  types/  (8 files)
    agent.ts
    ai.ts
    dynamic-tools.ts
    index.ts
    message-persistence.ts
    model-selector.ts
    models.ts
    search.ts
  usage-budget/  (18 files)
    __tests__/  (7 files)
      … 7 files under this directory
    analytics.ts
    attempt-id.ts
    config.ts
    events.ts
    gate.ts
    grants.ts
    index.ts
    refund-handler.ts
    response.ts
    time.ts
    types.ts
  utils/  (34 files)
    __tests__/  (12 files)
      … 12 files under this directory
    attachment-limits.ts
    attachment-tokens.ts
    citation.ts
    context-window.ts
    cookies.ts
    domain.ts
    favicon.ts
    index.ts
    markdown.ts
    message-mapping.ts
    message-utils.ts
    model-selection.ts
    perf-logging.ts
    perf-tracking.ts
    registry.ts
    retry.ts
    safe-fetch.ts
    search-config.ts
    search-query.ts
    telemetry.ts
    url.ts
    usage-logging.ts
  version/  (10 files)
    __tests__/  (5 files)
      … 5 files under this directory
    admins.ts
    config.ts
    install-method.ts
    semver.ts
    update-check.ts
  bot-protection.ts
  footer-tips.ts
  keyboard-shortcuts.ts
  maintenance.ts
  search-mode-availability.ts
public/  (6 files)
  providers/  (6 files)
    logos/  (6 files)
      … 6 files under this directory
scripts/  (5 files)
  README.md
  backfill-file-object-keys.ts
  chat-cli.ts
  generate-model-metadata.ts
  test-cache-performance.ts
.dockerignore
.gitignore
.mcp.json
.prettierignore
AGENTS.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
components.json
docker-compose.yaml
docker-entrypoint.sh
drizzle.config.ts
eslint.config.mjs
instrumentation-client.ts
instrumentation.test.ts
instrumentation.ts
next.config.mjs
package.json
postcss.config.mjs
prettier.config.js
proxy.test.ts
proxy.ts
… 5 more files
```

## Entry points

- [app/auth/admin/page.tsx](https://github.com/miurla/morphic/blob/244ea609ab0d604f6c7020fee214ac087f0129c9/app/auth/admin/page.tsx)
- [app/auth/error/page.tsx](https://github.com/miurla/morphic/blob/244ea609ab0d604f6c7020fee214ac087f0129c9/app/auth/error/page.tsx)
- [app/auth/forgot-password/page.tsx](https://github.com/miurla/morphic/blob/244ea609ab0d604f6c7020fee214ac087f0129c9/app/auth/forgot-password/page.tsx)
- [app/auth/login/page.tsx](https://github.com/miurla/morphic/blob/244ea609ab0d604f6c7020fee214ac087f0129c9/app/auth/login/page.tsx)
- [app/auth/sign-up-success/page.tsx](https://github.com/miurla/morphic/blob/244ea609ab0d604f6c7020fee214ac087f0129c9/app/auth/sign-up-success/page.tsx)
- [app/auth/sign-up/page.tsx](https://github.com/miurla/morphic/blob/244ea609ab0d604f6c7020fee214ac087f0129c9/app/auth/sign-up/page.tsx)
- [app/auth/update-password/page.tsx](https://github.com/miurla/morphic/blob/244ea609ab0d604f6c7020fee214ac087f0129c9/app/auth/update-password/page.tsx)
- [app/page.tsx](https://github.com/miurla/morphic/blob/244ea609ab0d604f6c7020fee214ac087f0129c9/app/page.tsx)
- [app/search/[id]/page.tsx](https://github.com/miurla/morphic/blob/244ea609ab0d604f6c7020fee214ac087f0129c9/app/search/%5Bid%5D/page.tsx)
- [app/search/page.tsx](https://github.com/miurla/morphic/blob/244ea609ab0d604f6c7020fee214ac087f0129c9/app/search/page.tsx)
- [components/ui/index.ts](https://github.com/miurla/morphic/blob/244ea609ab0d604f6c7020fee214ac087f0129c9/components/ui/index.ts)
- [lib/analytics/index.ts](https://github.com/miurla/morphic/blob/244ea609ab0d604f6c7020fee214ac087f0129c9/lib/analytics/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 18 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 18 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 164 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 37 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 12 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 18 file(s) under data layer (observed from repository paths and static analysis). |
| drizzle package | library | Observed | Groups 2 file(s) under drizzle package (observed from repository paths and static analysis). |
| evals package | library | Observed | Groups 25 file(s) under evals package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 8 file(s) under hooks package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 298 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/close-search-provider-prs.yml` (ci)
- `.github/workflows/docker-build.yml` (ci)
- `.github/workflows/eval.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.mcp.json` (config)
- `.vscode/settings.json` (config)
- `Dockerfile` (container)
- `components.json` (config)
- `config/models/cloud.json` (config)
- `docker-compose.yaml` (container)
- `drizzle/meta/0000_snapshot.json` (config)
- `drizzle/meta/0001_snapshot.json` (config)
- `drizzle/meta/0002_snapshot.json` (config)
- `drizzle/meta/0003_snapshot.json` (config)
- `drizzle/meta/0004_snapshot.json` (config)
- `drizzle/meta/0005_snapshot.json` (config)
- `drizzle/meta/0006_snapshot.json` (config)
- `drizzle/meta/0007_snapshot.json` (config)
- `drizzle/meta/0008_snapshot.json` (config)
- `drizzle/meta/0009_snapshot.json` (config)
- `drizzle/meta/0010_snapshot.json` (config)
- `drizzle/meta/0011_snapshot.json` (config)
- `drizzle/meta/0016_snapshot.json` (config)
- `drizzle/meta/0018_snapshot.json` (config)
- `drizzle/meta/0019_snapshot.json` (config)
- `drizzle/meta/0020_snapshot.json` (config)
- `drizzle/meta/0021_snapshot.json` (config)
- `drizzle/meta/_journal.json` (config)
- `evals/datasets/draft-edits.json` (config)
- `evals/datasets/related-questions.json` (config)
- `evals/datasets/source-cards.json` (config)
- `evals/thresholds.json` (config)
- `lib/config/model-metadata.json` (config)
- `package.json` (manifest)
- `searxng-limiter.toml` (config)
- `searxng-settings.yml` (config)
- `tsconfig.json` (config)

## Top-level layout

- `lib` — 323 analysed file(s)
- `components` — 164 analysed file(s)
- `drizzle` — 42 analysed file(s)
- `app` — 37 analysed file(s)
- `evals` — 30 analysed file(s)
- `(root files)` — 29 analysed file(s)
- `.github` — 9 analysed file(s)
- `hooks` — 8 analysed file(s)
- `public` — 6 analysed file(s)
- `scripts` — 5 analysed file(s)
- `docs` — 4 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `config` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `244ea609ab0d604f6c7020fee214ac087f0129c9` is the revision these paths and observations refer to.
