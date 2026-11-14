# Project structure: cruip/open-react-template

**Analysed commit:** `9da36763df216be7840f3c063edcdcaf7862401e`

**Commit reference:** [9da36763df216be7840f3c063edcdcaf7862401e](https://github.com/cruip/open-react-template/commit/9da36763df216be7840f3c063edcdcaf7862401e)

**Tree at this commit:** [cruip/open-react-template@9da36763df21](https://github.com/cruip/open-react-template/tree/9da36763df216be7840f3c063edcdcaf7862401e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | cruip/open-react-template |
| Description | A free React / Next.js landing page template designed to showcase open source projects, SaaS products, online services, and more. Made by |
| Stars | 4716 |
| Forks | 2078 |
| Licence | Not detected |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `9da36763df216be7840f3c063edcdcaf7862401e` |
| Retrieved at | 2026-11-14T19:14:38.245002+00:00 |
| Files in this snapshot | 47 |

## Directory tree

```text
.vscode/  (1 files)
  settings.json
app/  (11 files)
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
  css/  (3 files)
    additional-styles/  (2 files)
      … 2 files under this directory
    style.css
  layout.tsx
components/  (11 files)
  ui/  (3 files)
    footer.tsx
    header.tsx
    logo.tsx
  cta.tsx
  features.tsx
  hero-home.tsx
  modal-video.tsx
  page-illustration.tsx
  spotlight.tsx
  testimonials.tsx
  workflows.tsx
public/  (15 files)
  images/  (15 files)
    blurred-shape-gray.svg
    blurred-shape.svg
    client-logo-01.svg
    client-logo-02.svg
    client-logo-03.svg
    client-logo-04.svg
    client-logo-05.svg
    client-logo-06.svg
    client-logo-07.svg
    client-logo-08.svg
    client-logo-09.svg
    footer-illustration.svg
    logo.svg
    page-illustration.svg
    secondary-illustration.svg
utils/  (2 files)
  useMasonry.tsx
  useMousePosition.tsx
.gitignore
CHANGELOG.md
README.md
next.config.js
package.json
postcss.config.js
tsconfig.json
```

## Entry points

- [app/(auth)/reset-password/page.tsx](https://github.com/cruip/open-react-template/blob/9da36763df216be7840f3c063edcdcaf7862401e/app/%28auth%29/reset-password/page.tsx)
- [app/(auth)/signin/page.tsx](https://github.com/cruip/open-react-template/blob/9da36763df216be7840f3c063edcdcaf7862401e/app/%28auth%29/signin/page.tsx)
- [app/(auth)/signup/page.tsx](https://github.com/cruip/open-react-template/blob/9da36763df216be7840f3c063edcdcaf7862401e/app/%28auth%29/signup/page.tsx)
- [app/(default)/page.tsx](https://github.com/cruip/open-react-template/blob/9da36763df216be7840f3c063edcdcaf7862401e/app/%28default%29/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 7 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 11 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 2 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `public` — 15 analysed file(s)
- `app` — 11 analysed file(s)
- `components` — 11 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `utils` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `9da36763df216be7840f3c063edcdcaf7862401e` is the revision these paths and observations refer to.
