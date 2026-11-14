# Project structure: stackryze/FreeDomains

**Analysed commit:** `2ef23a775dfe06f5d4b1a80e9a28e62f45313827`

**Commit reference:** [2ef23a775dfe06f5d4b1a80e9a28e62f45313827](https://github.com/stackryze/FreeDomains/commit/2ef23a775dfe06f5d4b1a80e9a28e62f45313827)

**Tree at this commit:** [stackryze/FreeDomains@2ef23a775dfe](https://github.com/stackryze/FreeDomains/tree/2ef23a775dfe06f5d4b1a80e9a28e62f45313827)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | stackryze/FreeDomains |
| Description | Stackryze Domains: Free Domain for Everyone, Claim yours today. |
| Stars | 14635 |
| Forks | 300 |
| Licence | AGPL-3.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `2ef23a775dfe06f5d4b1a80e9a28e62f45313827` |
| Retrieved at | 2026-11-14T19:11:44.075077+00:00 |
| Files in this snapshot | 119 |

## Directory tree

```text
.github/  (1 files)
  FUNDING.yml
public/  (4 files)
  Cloudflare_Logo.svg
  _headers
  robots.txt
  sitemap.xml
src/  (102 files)
  assets/  (1 files)
    react.svg
  components/  (65 files)
    ui/  (53 files)
      … 53 files under this directory
    IncidentAnnouncement.jsx
    domain-extensions.jsx
    faq-section.jsx
    feature-cards.jsx
    footer-section.jsx
    header.jsx
    hero-section.jsx
    live-stats.jsx
    mission-section.jsx
    network-map-section.jsx
    sponsors-section.jsx
    theme-provider.jsx
  context/  (2 files)
    auth-context.jsx
    dashboard-context.jsx
  hooks/  (2 files)
    use-mobile.js
    use-toast.js
  layouts/  (2 files)
    DashboardLayout.jsx
    LegalLayout.jsx
  lib/  (2 files)
    api.js
    utils.js
  pages/  (23 files)
    dashboard/  (9 files)
      … 9 files under this directory
    legal/  (4 files)
      … 4 files under this directory
    About.jsx
    ChangeEmail.jsx
    CompleteProfile.jsx
    Donate.jsx
    Landing.jsx
    Login.jsx
    NotFound.jsx
    Signup.jsx
    VerifyEmail.jsx
    Whois.jsx
  App.css
  App.jsx
  ErrorBoundary.jsx
  index.css
  main.jsx
.env.example
.gitignore
.node-version
CODE_OF_CONDUCT.md
Dockerfile
LICENSE
README.md
eslint.config.js
index.html
package.json
vite.config.js
wrangler.toml
```

## Entry points

- [src/App.jsx](https://github.com/stackryze/FreeDomains/blob/2ef23a775dfe06f5d4b1a80e9a28e62f45313827/src/App.jsx)
- [src/main.jsx](https://github.com/stackryze/FreeDomains/blob/2ef23a775dfe06f5d4b1a80e9a28e62f45313827/src/main.jsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| App.jsx package | library | Observed | Groups 1 file(s) under app.jsx package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 65 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| context package | library | Observed | Groups 2 file(s) under context package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| ErrorBoundary.jsx package | library | Observed | Groups 1 file(s) under errorboundary.jsx package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 2 file(s) under hooks package (observed from repository paths and static analysis). |
| layouts package | library | Observed | Groups 2 file(s) under layouts package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 2 file(s) under lib package (observed from repository paths and static analysis). |
| main.jsx package | library | Observed | Groups 1 file(s) under main.jsx package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 23 file(s) under pages package (observed from repository paths and static analysis). |

## Important files

- `.env.example` (config)
- `.github/FUNDING.yml` (config)
- `Dockerfile` (container)
- `package.json` (manifest)
- `wrangler.toml` (config)

## Top-level layout

- `src` — 102 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `public` — 4 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `2ef23a775dfe06f5d4b1a80e9a28e62f45313827` is the revision these paths and observations refer to.
