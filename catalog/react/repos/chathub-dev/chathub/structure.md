# Project structure: chathub-dev/chathub

**Analysed commit:** `852efba00ca7f2888093510b3add33f3ee01dc9b`

**Commit reference:** [852efba00ca7f2888093510b3add33f3ee01dc9b](https://github.com/chathub-dev/chathub/commit/852efba00ca7f2888093510b3add33f3ee01dc9b)

**Tree at this commit:** [chathub-dev/chathub@852efba00ca7](https://github.com/chathub-dev/chathub/tree/852efba00ca7f2888093510b3add33f3ee01dc9b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | chathub-dev/chathub |
| Description | Not provided |
| Stars | 10657 |
| Forks | 1108 |
| Licence | GPL-3.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `852efba00ca7f2888093510b3add33f3ee01dc9b` |
| Retrieved at | 2026-11-14T19:13:30.433147+00:00 |
| Files in this snapshot | 255 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    release.yml
  dependabot.yml
_locales/  (12 files)
  de/  (1 files)
    messages.json
  en/  (1 files)
    messages.json
  es/  (1 files)
    messages.json
  fr/  (1 files)
    messages.json
  in/  (1 files)
    messages.json
  ja/  (1 files)
    messages.json
  pt_BR/  (1 files)
    messages.json
  pt_PT/  (1 files)
    messages.json
  ru/  (1 files)
    messages.json
  th/  (1 files)
    messages.json
  zh_CN/  (1 files)
    messages.json
  zh_TW/  (1 files)
    messages.json
public/  (1 files)
  js/  (1 files)
    v2/  (1 files)
      … 1 files under this directory
src/  (218 files)
  app/  (149 files)
    bots/  (50 files)
      … 50 files under this directory
    components/  (60 files)
      … 60 files under this directory
    hooks/  (5 files)
      … 5 files under this directory
    i18n/  (10 files)
      … 10 files under this directory
    pages/  (5 files)
      … 5 files under this directory
    state/  (1 files)
      … 1 files under this directory
    utils/  (9 files)
      … 9 files under this directory
    base.scss
    consts.ts
    context.ts
    main.tsx
    plausible.ts
    router.tsx
    sidepanel.css
    sidepanel.tsx
    theme.ts
  assets/  (31 files)
    icons/  (20 files)
      … 20 files under this directory
    logos/  (6 files)
      … 6 files under this directory
    all-in-one.svg
    icon.svg
    logo.svg
    minimal-logo.svg
    user-avatar.svg
  background/  (3 files)
    index.ts
    source.ts
    twitter-cookie.ts
  content-script/  (1 files)
    chatgpt-inpage-proxy.ts
  rules/  (5 files)
    baichuan.json
    bing.json
    ddg.json
    pplx.json
    qianwen.json
  services/  (19 files)
    agent/  (6 files)
      … 6 files under this directory
    storage/  (3 files)
      … 3 files under this directory
    chat-history.ts
    lemonsqueezy.ts
    premium.ts
    prompts.ts
    proxy-fetch.ts
    release-notes.ts
    sentry.ts
    server-api.ts
    theme.ts
    user-config.ts
  types/  (3 files)
    chat.ts
    index.ts
    messaging.ts
  utils/  (6 files)
    encoding.ts
    errors.ts
    format.ts
    index.ts
    sse.ts
    stream-async-iterable.ts
  vite-env.d.ts
.eslintrc.json
.gitignore
.prettierignore
.prettierrc
.yarnrc.yml
LICENSE
README.md
README_IN.md
README_JA.md
README_ZH-CN.md
README_ZH-TW.md
app.html
global.d.ts
manifest.config.ts
package.json
postcss.config.cjs
sidepanel.html
tailwind.config.cjs
tsconfig.json
vite.config.ts
```

## Entry points

- [src/app/bots/index.ts](https://github.com/chathub-dev/chathub/blob/852efba00ca7f2888093510b3add33f3ee01dc9b/src/app/bots/index.ts)
- [src/app/components/Page.tsx](https://github.com/chathub-dev/chathub/blob/852efba00ca7f2888093510b3add33f3ee01dc9b/src/app/components/Page.tsx)
- [src/app/i18n/index.ts](https://github.com/chathub-dev/chathub/blob/852efba00ca7f2888093510b3add33f3ee01dc9b/src/app/i18n/index.ts)
- [src/app/main.tsx](https://github.com/chathub-dev/chathub/blob/852efba00ca7f2888093510b3add33f3ee01dc9b/src/app/main.tsx)
- [src/app/state/index.ts](https://github.com/chathub-dev/chathub/blob/852efba00ca7f2888093510b3add33f3ee01dc9b/src/app/state/index.ts)
- [src/background/index.ts](https://github.com/chathub-dev/chathub/blob/852efba00ca7f2888093510b3add33f3ee01dc9b/src/background/index.ts)
- [src/services/agent/index.ts](https://github.com/chathub-dev/chathub/blob/852efba00ca7f2888093510b3add33f3ee01dc9b/src/services/agent/index.ts)
- [src/types/index.ts](https://github.com/chathub-dev/chathub/blob/852efba00ca7f2888093510b3add33f3ee01dc9b/src/types/index.ts)
- [src/utils/index.ts](https://github.com/chathub-dev/chathub/blob/852efba00ca7f2888093510b3add33f3ee01dc9b/src/utils/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 115 file(s) under app package (observed from repository paths and static analysis). |
| background package | library | Observed | Groups 3 file(s) under background package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 43 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| content-script package | library | Observed | Groups 1 file(s) under content-script package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 1 file(s) under public package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 16 file(s) under service / domain layer (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 3 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 6 file(s) under utils package (observed from repository paths and static analysis). |
| vite-env.d.ts package | library | Observed | Groups 1 file(s) under vite-env.d.ts package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/release.yml` (ci)
- `.yarnrc.yml` (config)
- `_locales/de/messages.json` (config)
- `_locales/en/messages.json` (config)
- `_locales/es/messages.json` (config)
- `_locales/fr/messages.json` (config)
- `_locales/in/messages.json` (config)
- `_locales/ja/messages.json` (config)
- `_locales/pt_BR/messages.json` (config)
- `_locales/pt_PT/messages.json` (config)
- `_locales/ru/messages.json` (config)
- `_locales/th/messages.json` (config)
- `_locales/zh_CN/messages.json` (config)
- `_locales/zh_TW/messages.json` (config)
- `package.json` (manifest)
- `src/app/i18n/locales/french.json` (config)
- `src/app/i18n/locales/german.json` (config)
- `src/app/i18n/locales/indonesia.json` (config)
- `src/app/i18n/locales/japanese.json` (config)
- `src/app/i18n/locales/portuguese.json` (config)
- `src/app/i18n/locales/simplified-chinese.json` (config)
- `src/app/i18n/locales/spanish.json` (config)
- `src/app/i18n/locales/thai.json` (config)
- `src/app/i18n/locales/traditional-chinese.json` (config)
- `src/rules/baichuan.json` (config)
- `src/rules/bing.json` (config)
- `src/rules/ddg.json` (config)
- `src/rules/pplx.json` (config)
- `src/rules/qianwen.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 218 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `_locales` — 12 analysed file(s)
- `.github` — 4 analysed file(s)
- `public` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `852efba00ca7f2888093510b3add33f3ee01dc9b` is the revision these paths and observations refer to.
