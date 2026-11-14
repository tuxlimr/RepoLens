# Project structure: Anarios/return-youtube-dislike

**Analysed commit:** `895c1fb9d47d32b8af066b80969abca734554b04`

**Commit reference:** [895c1fb9d47d32b8af066b80969abca734554b04](https://github.com/Anarios/return-youtube-dislike/commit/895c1fb9d47d32b8af066b80969abca734554b04)

**Tree at this commit:** [Anarios/return-youtube-dislike@895c1fb9d47d](https://github.com/Anarios/return-youtube-dislike/tree/895c1fb9d47d32b8af066b80969abca734554b04)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Anarios/return-youtube-dislike |
| Description | Chrome extension to return youtube dislikes |
| Stars | 13853 |
| Forks | 644 |
| Licence | GPL-3.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `895c1fb9d47d32b8af066b80969abca734554b04` |
| Retrieved at | 2026-11-14T19:11:49.790445+00:00 |
| Files in this snapshot | 570 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (2 files)
    bug.yml
    feature-request.yml
  workflows/  (3 files)
    build.yaml
    commentcommands.yml
    weblint.yml
  FUNDING.yml
  dependabot.yml
Docs/  (53 files)
  FAQ.md
  FAQar.md
  FAQaz.md
  FAQbe.md
  FAQbg.md
  FAQcn.md
  FAQde.md
  FAQfa.md
  FAQfr.md
  FAQid.md
  FAQnl.md
  FAQpl.md
  FAQpt_BR.md
  FAQru.md
  FAQsl.md
  FAQtr.md
  FAQuk.md
  FAQvi.md
  Guide__Installing.md
  Guide__Installingvi.md
  Guide__Troubleshooting.md
  Guide__Troubleshootingvi.md
  Privacy Policy
  Privacy Policyvi
  … 29 more files
Extensions/  (338 files)
  UserScript/  (65 files)
    e2e/  (34 files)
      … 34 files under this directory
    live/  (18 files)
      … 18 files under this directory
    src/  (9 files)
      … 9 files under this directory
    Return Youtube Dislike.user.js
    userscript-artifact.spec.js
    userscript-version.json
    userscript.meta.js
  combined/  (180 files)
    _locales/  (25 files)
      … 25 files under this directory
    changelog/  (5 files)
      … 5 files under this directory
    icons/  (2 files)
      … 2 files under this directory
    src/  (119 files)
      … 119 files under this directory
    comments-bridge.js
    consent.css
    consent.html
    consent.js
    consent.spec.js
    content-style.css
    manifest-chrome.json
    manifest-firefox.json
    manifest-safari.json
    menu-fixer.js
    message-keys.spec.js
    popup-colors.spec.js
    popup-context.js
    popup-context.spec.js
    popup-locale.spec.js
    popup-permissions.spec.js
    popup-private.spec.js
    popup-settings-layout.spec.js
    popup.css
    popup.html
    popup.js
    popup.spec.js
    readme.md
    ryd.background-changelog.spec.js
    … 5 more files
  common/  (13 files)
    color-themes.js
    color-themes.spec.js
    delegated-vote-activation.js
    delegated-vote-activation.spec.js
    live-video-id.js
    live-video-id.spec.js
    shorts-control-readiness.js
    shorts-control-readiness.spec.js
    vote-client.js
    vote-client.spec.js
    vote-transition-core.js
    vote-transition.js
    vote-transition.spec.js
  e2e/  (80 files)
    discussion/  (5 files)
      … 5 files under this directory
    extension/  (24 files)
      … 24 files under this directory
    fixtures/  (1 files)
      … 1 files under this directory
    README.md
    action-overflow-contract.js
    action-overflow-contract.spec.js
    continuous-invariants.js
    continuous-invariants.spec.js
    feature-identity-smoke.js
    feature-permissions-fixtures.js
    firefox-changelog-lifecycle.js
    firefox-consent-smoke.js
    firefox-feature-permissions.js
    firefox-install-consent.js
    firefox-install-consent.spec.js
    firefox-live-youtube.js
    firefox-toolbar-popup.js
    generate-hide-clutter-tooltip-assets.js
    hermetic-api-contract.js
    hermetic-api-contract.spec.js
    hermetic-artifact-smoke.js
    hermetic-artifact-smoke.spec.js
    hide-clutter-tooltip-assets.spec.js
    live-runtime-adapter.js
    navigation-runtime-contract.js
    navigation-runtime-contract.spec.js
    notification-recovery-smoke.js
    … 26 more files
Icons/  (1 files)
  Return Youtube Dislike - Transparent.svg
Website/  (62 files)
  _locales/  (22 files)
    az.ts
    be.ts
    cs.ts
    de.ts
    en.ts
    es.ts
    fa.ts
    fr.ts
    hu.ts
    id.ts
    it-IT.ts
    ja.ts
    ko.ts
    nl.ts
    pl.ts
    pt_BR.ts
    ru.ts
    sl.ts
    sv.ts
    tr.ts
    uk.ts
    vi.ts
  layouts/  (3 files)
    default.spec.js
    default.vue
    error.vue
  pages/  (14 files)
    docs/  (5 files)
      … 5 files under this directory
    pay/  (1 files)
      … 1 files under this directory
    debug.vue
    docs.vue
    donate.vue
    faq.vue
    help.vue
    index.vue
    install.vue
    links.vue
  static/  (2 files)
    ui/  (1 files)
      … 1 files under this directory
    logo.svg
  store/  (7 files)
    README.md
    READMEbe.md
    READMEbg.md
    READMEde.md
    READMEnl.md
    READMEtr.md
    READMEvi.md
  utils/  (2 files)
    locale.js
    locale.spec.js
  .eslintignore
  .eslintrc.js
  README.md
  READMEaz.md
  READMEbe.md
  READMEbg.md
  READMEde.md
  READMEnl.md
  READMEtr.md
  READMEvi.md
  nuxt.config.js
  package.json
scripts/  (7 files)
  build-firefox-source.mjs
  check-locales.js
  check-locales.spec.js
  package-amo-release.cjs
  package-amo-release.spec.js
  with-trusted-node.cjs
  with-trusted-node.spec.js
.babelrc
.gitattributes
.gitignore
.nvmrc
AMO_RELEASE_NOTES.md
CONTRIBUTING.md
CONTRIBUTINGar.md
CONTRIBUTINGaz.md
CONTRIBUTINGbe.md
CONTRIBUTINGbg.md
CONTRIBUTINGcn.md
CONTRIBUTINGda.md
CONTRIBUTINGde.md
CONTRIBUTINGes.md
CONTRIBUTINGfa.md
CONTRIBUTINGfr.md
CONTRIBUTINGgr.md
CONTRIBUTINGhu.md
CONTRIBUTINGid.md
CONTRIBUTINGja.md
CONTRIBUTINGkr.md
CONTRIBUTINGnl.md
CONTRIBUTINGpl.md
CONTRIBUTINGpt_BR.md
… 78 more files
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 31 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 14 file(s) under core modules (observed from repository paths and static analysis). |
| Extensions package | library | Observed | Groups 290 file(s) under extensions package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 7 file(s) under scripts package (observed from repository paths and static analysis). |
| Website package | library | Observed | Groups 38 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/build.yaml` (ci)
- `.github/workflows/commentcommands.yml` (ci)
- `.github/workflows/weblint.yml` (ci)
- `Extensions/UserScript/userscript-version.json` (config)
- `Extensions/combined/_locales/az/messages.json` (config)
- `Extensions/combined/_locales/be/messages.json` (config)
- `Extensions/combined/_locales/cs/messages.json` (config)
- `Extensions/combined/_locales/de/messages.json` (config)
- `Extensions/combined/_locales/el/messages.json` (config)
- `Extensions/combined/_locales/en/messages.json` (config)
- `Extensions/combined/_locales/es/messages.json` (config)
- `Extensions/combined/_locales/fa/messages.json` (config)
- `Extensions/combined/_locales/fr/messages.json` (config)
- `Extensions/combined/_locales/hu/messages.json` (config)
- `Extensions/combined/_locales/id/messages.json` (config)
- `Extensions/combined/_locales/it/messages.json` (config)
- `Extensions/combined/_locales/ja/messages.json` (config)
- `Extensions/combined/_locales/ko/messages.json` (config)
- `Extensions/combined/_locales/nl/messages.json` (config)
- `Extensions/combined/_locales/pl/messages.json` (config)
- `Extensions/combined/_locales/pt_BR/messages.json` (config)
- `Extensions/combined/_locales/ru/messages.json` (config)
- `Extensions/combined/_locales/sl/messages.json` (config)
- `Extensions/combined/_locales/sv_SE/messages.json` (config)
- `Extensions/combined/_locales/tr/messages.json` (config)
- `Extensions/combined/_locales/uk/messages.json` (config)
- `Extensions/combined/_locales/vi/messages.json` (config)
- `Extensions/combined/_locales/zh_CN/messages.json` (config)
- `Extensions/combined/_locales/zh_TW/messages.json` (config)
- `Extensions/combined/manifest-chrome.json` (config)
- `Extensions/combined/manifest-firefox.json` (config)
- `Extensions/combined/manifest-safari.json` (config)
- `Website/package.json` (manifest)
- `package.json` (manifest)

## Top-level layout

- `Extensions` — 338 analysed file(s)
- `(root files)` — 102 analysed file(s)
- `Website` — 62 analysed file(s)
- `Docs` — 53 analysed file(s)
- `.github` — 7 analysed file(s)
- `scripts` — 7 analysed file(s)
- `Icons` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `895c1fb9d47d32b8af066b80969abca734554b04` is the revision these paths and observations refer to.
