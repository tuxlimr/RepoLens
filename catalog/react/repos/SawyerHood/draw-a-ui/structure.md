# Project structure: SawyerHood/draw-a-ui

**Analysed commit:** `1aca63b4d54a3065fe72fe9784c91265510fbe19`

**Commit reference:** [1aca63b4d54a3065fe72fe9784c91265510fbe19](https://github.com/SawyerHood/draw-a-ui/commit/1aca63b4d54a3065fe72fe9784c91265510fbe19)

**Tree at this commit:** [SawyerHood/draw-a-ui@1aca63b4d54a](https://github.com/SawyerHood/draw-a-ui/tree/1aca63b4d54a3065fe72fe9784c91265510fbe19)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | SawyerHood/draw-a-ui |
| Description | Draw a mockup and generate html for it |
| Stars | 13567 |
| Forks | 1609 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `1aca63b4d54a3065fe72fe9784c91265510fbe19` |
| Retrieved at | 2026-11-14T19:13:18.085909+00:00 |
| Files in this snapshot | 21 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    ci.yml
app/  (4 files)
  api/  (1 files)
    toHtml/  (1 files)
      … 1 files under this directory
  globals.css
  layout.tsx
  page.tsx
components/  (1 files)
  PreviewModal.tsx
lib/  (4 files)
  blobToBase64.ts
  getBrowserCanvasMaxSize.ts
  getSvgAsImage.ts
  png.ts
public/  (2 files)
  next.svg
  vercel.svg
.eslintrc.json
.gitignore
LICENSE
README.md
next.config.js
package.json
postcss.config.js
tailwind.config.ts
tsconfig.json
```

## Entry points

- [app/page.tsx](https://github.com/SawyerHood/draw-a-ui/blob/1aca63b4d54a3065fe72fe9784c91265510fbe19/app/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 2 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 1 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 4 file(s) under lib package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/workflows/ci.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `(root files)` — 9 analysed file(s)
- `app` — 4 analysed file(s)
- `lib` — 4 analysed file(s)
- `public` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `components` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1aca63b4d54a3065fe72fe9784c91265510fbe19` is the revision these paths and observations refer to.
