# Project structure: vercel/chatbot

**Analysed commit:** `a8989b522fa3672a2ae52f053105e40993b36ca1`

**Commit reference:** [a8989b522fa3672a2ae52f053105e40993b36ca1](https://github.com/vercel/chatbot/commit/a8989b522fa3672a2ae52f053105e40993b36ca1)

**Tree at this commit:** [vercel/chatbot@a8989b522fa3](https://github.com/vercel/chatbot/tree/a8989b522fa3672a2ae52f053105e40993b36ca1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vercel/chatbot |
| Description | A full-featured, hackable Next.js AI chatbot built by Vercel |
| Stars | 21050 |
| Forks | 6778 |
| Licence | Other |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `a8989b522fa3672a2ae52f053105e40993b36ca1` |
| Retrieved at | 2026-11-14T19:13:10.750841+00:00 |
| Files in this snapshot | 176 |

## Directory tree

```text
.cursor/  (1 files)
  rules/  (1 files)
    ultracite.mdc
.github/  (2 files)
  workflows/  (2 files)
    lint.yml
    playwright.yml
.husky/  (1 files)
  pre-commit
.vscode/  (2 files)
  extensions.json
  settings.json
app/  (24 files)
  (auth)/  (8 files)
    api/  (2 files)
      … 2 files under this directory
    login/  (1 files)
      … 1 files under this directory
    register/  (1 files)
      … 1 files under this directory
    actions.ts
    auth.config.ts
    auth.ts
    layout.tsx
  (chat)/  (14 files)
    api/  (10 files)
      … 10 files under this directory
    chat/  (1 files)
      … 1 files under this directory
    actions.ts
    layout.tsx
    page.tsx
  globals.css
  layout.tsx
artifacts/  (8 files)
  code/  (2 files)
    client.tsx
    server.ts
  image/  (1 files)
    client.tsx
  sheet/  (2 files)
    client.tsx
    server.ts
  text/  (2 files)
    client.tsx
    server.ts
  actions.ts
components/  (76 files)
  ai-elements/  (9 files)
    code-block.tsx
    conversation.tsx
    message.tsx
    model-selector.tsx
    prompt-input.tsx
    reasoning.tsx
    shimmer.tsx
    suggestion.tsx
    tool.tsx
  chat/  (44 files)
    app-sidebar.tsx
    artifact-actions.tsx
    artifact-close-button.tsx
    artifact-messages.tsx
    artifact.tsx
    auth-form.tsx
    chat-header.tsx
    code-editor.tsx
    console.tsx
    create-artifact.tsx
    data-stream-handler.tsx
    data-stream-provider.tsx
    diffview.tsx
    document-preview.tsx
    document-skeleton.tsx
    document.tsx
    greeting.tsx
    icons.tsx
    image-editor.tsx
    message-actions.tsx
    message-editor.tsx
    message-reasoning.tsx
    message.tsx
    messages.tsx
    … 20 more files
  ui/  (22 files)
    alert-dialog.tsx
    badge.tsx
    button-group.tsx
    button.tsx
    collapsible.tsx
    command.tsx
    dialog.tsx
    dropdown-menu.tsx
    hover-card.tsx
    input-group.tsx
    input.tsx
    label.tsx
    popover.tsx
    scroll-area.tsx
    select.tsx
    separator.tsx
    sheet.tsx
    sidebar.tsx
    skeleton.tsx
    spinner.tsx
    textarea.tsx
    tooltip.tsx
  theme-provider.tsx
hooks/  (7 files)
  use-active-chat.tsx
  use-artifact.ts
  use-auto-resume.ts
  use-chat-visibility.ts
  use-messages.tsx
  use-mobile.ts
  use-scroll-to-bottom.tsx
lib/  (29 files)
  ai/  (12 files)
    tools/  (5 files)
      … 5 files under this directory
    entitlements.ts
    generate-title.ts
    models.mock.ts
    models.test.ts
    models.ts
    prompts.ts
    providers.ts
  artifacts/  (1 files)
    server.ts
  db/  (6 files)
    migrations/  (2 files)
      … 2 files under this directory
    migrate.ts
    queries.ts
    schema.ts
    utils.ts
  editor/  (5 files)
    config.ts
    diff.js
    functions.tsx
    react-renderer.tsx
    suggestions.tsx
  constants.ts
  errors.ts
  ratelimit.ts
  types.ts
  utils.ts
tests/  (8 files)
  e2e/  (4 files)
    api.test.ts
    auth.test.ts
    chat.test.ts
    model-selector.test.ts
  pages/  (1 files)
    chat.ts
  prompts/  (1 files)
    utils.ts
  fixtures.ts
  helpers.ts
.env.example
.gitignore
LICENSE
README.md
biome.jsonc
components.json
drizzle.config.ts
instrumentation-client.ts
instrumentation.ts
next.config.ts
package.json
playwright.config.ts
pnpm-workspace.yaml
postcss.config.mjs
proxy.ts
tsconfig.json
vercel-template.json
vercel.json
```

## Entry points

- [app/(auth)/login/page.tsx](https://github.com/vercel/chatbot/blob/a8989b522fa3672a2ae52f053105e40993b36ca1/app/%28auth%29/login/page.tsx)
- [app/(auth)/register/page.tsx](https://github.com/vercel/chatbot/blob/a8989b522fa3672a2ae52f053105e40993b36ca1/app/%28auth%29/register/page.tsx)
- [app/(chat)/page.tsx](https://github.com/vercel/chatbot/blob/a8989b522fa3672a2ae52f053105e40993b36ca1/app/%28chat%29/page.tsx)
- [artifacts/code/server.ts](https://github.com/vercel/chatbot/blob/a8989b522fa3672a2ae52f053105e40993b36ca1/artifacts/code/server.ts)
- [artifacts/sheet/server.ts](https://github.com/vercel/chatbot/blob/a8989b522fa3672a2ae52f053105e40993b36ca1/artifacts/sheet/server.ts)
- [artifacts/text/server.ts](https://github.com/vercel/chatbot/blob/a8989b522fa3672a2ae52f053105e40993b36ca1/artifacts/text/server.ts)
- [lib/artifacts/server.ts](https://github.com/vercel/chatbot/blob/a8989b522fa3672a2ae52f053105e40993b36ca1/lib/artifacts/server.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 12 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 11 file(s) under app package (observed from repository paths and static analysis). |
| artifacts package | library | Observed | Groups 8 file(s) under artifacts package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 76 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 7 file(s) under hooks package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 23 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 8 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/playwright.yml` (ci)
- `.vscode/extensions.json` (config)
- `.vscode/settings.json` (config)
- `components.json` (config)
- `lib/db/migrations/meta/_journal.json` (config)
- `package.json` (manifest)
- `pnpm-workspace.yaml` (config)
- `tsconfig.json` (config)
- `vercel-template.json` (config)
- `vercel.json` (config)

## Top-level layout

- `components` — 76 analysed file(s)
- `lib` — 29 analysed file(s)
- `app` — 24 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `artifacts` — 8 analysed file(s)
- `tests` — 8 analysed file(s)
- `hooks` — 7 analysed file(s)
- `.github` — 2 analysed file(s)
- `.vscode` — 2 analysed file(s)
- `.cursor` — 1 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a8989b522fa3672a2ae52f053105e40993b36ca1` is the revision these paths and observations refer to.
