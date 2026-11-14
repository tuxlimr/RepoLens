# Project structure: cruip/tailwind-landing-page-template

**Analysed commit:** `909e38e3249ac575017864a202188b48ef016c9c`

**Commit reference:** [909e38e3249ac575017864a202188b48ef016c9c](https://github.com/cruip/tailwind-landing-page-template/commit/909e38e3249ac575017864a202188b48ef016c9c)

**Tree at this commit:** [cruip/tailwind-landing-page-template@909e38e3249a](https://github.com/cruip/tailwind-landing-page-template/tree/909e38e3249ac575017864a202188b48ef016c9c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | cruip/tailwind-landing-page-template |
| Description | Simple Light is a free landing page template built on top of TailwindCSS and fully coded in React / Next.js. Made by  |
| Stars | 4529 |
| Forks | 1719 |
| Licence | Not detected |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `909e38e3249ac575017864a202188b48ef016c9c` |
| Retrieved at | 2026-11-14T19:14:43.584884+00:00 |
| Files in this snapshot | 44 |

## Directory tree

```text
.vscode/  (1 files)
  settings.json
app/  (12 files)
  (auth)/  (4 files)
    reset-password/  (1 files)
      … 1 files under this directory
    signin/  (1 files)
      … 1 files under this directory
    signup/  (1 files)
      … 1 files under this directory
    layout.tsx
  (default)/  (2 files)
    layout.tsx
    page.tsx
  api/  (1 files)
    hello/  (1 files)
      … 1 files under this directory
  css/  (4 files)
    additional-styles/  (3 files)
      … 3 files under this directory
    style.css
  layout.tsx
components/  (11 files)
  ui/  (3 files)
    footer.tsx
    header.tsx
    logo.tsx
  accordion.tsx
  banner.tsx
  business-categories.tsx
  cta.tsx
  features-planet.tsx
  hero-home.tsx
  large-testimonial.tsx
  page-illustration.tsx
public/  (13 files)
  images/  (13 files)
    auth-bg.svg
    logo-01.svg
    logo-02.svg
    logo-03.svg
    logo-04.svg
    logo-05.svg
    logo-06.svg
    logo-07.svg
    logo-08.svg
    logo-09.svg
    planet-overlay.svg
    stripes-dark.svg
    stripes.svg
.gitignore
CHANGELOG.md
README.md
next.config.js
package.json
postcss.config.js
tsconfig.json
```

## Entry points

- [app/(auth)/reset-password/page.tsx](https://github.com/cruip/tailwind-landing-page-template/blob/909e38e3249ac575017864a202188b48ef016c9c/app/%28auth%29/reset-password/page.tsx)
- [app/(auth)/signin/page.tsx](https://github.com/cruip/tailwind-landing-page-template/blob/909e38e3249ac575017864a202188b48ef016c9c/app/%28auth%29/signin/page.tsx)
- [app/(auth)/signup/page.tsx](https://github.com/cruip/tailwind-landing-page-template/blob/909e38e3249ac575017864a202188b48ef016c9c/app/%28auth%29/signup/page.tsx)
- [app/(default)/page.tsx](https://github.com/cruip/tailwind-landing-page-template/blob/909e38e3249ac575017864a202188b48ef016c9c/app/%28default%29/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 7 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 11 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |

## Important files

- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `public` — 13 analysed file(s)
- `app` — 12 analysed file(s)
- `components` — 11 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `909e38e3249ac575017864a202188b48ef016c9c` is the revision these paths and observations refer to.
