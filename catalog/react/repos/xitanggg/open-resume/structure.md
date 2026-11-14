# Project structure: xitanggg/open-resume

**Analysed commit:** `4f8255a2c763479837f69f1dccf2a3338730cd79`

**Commit reference:** [4f8255a2c763479837f69f1dccf2a3338730cd79](https://github.com/xitanggg/open-resume/commit/4f8255a2c763479837f69f1dccf2a3338730cd79)

**Tree at this commit:** [xitanggg/open-resume@4f8255a2c763](https://github.com/xitanggg/open-resume/tree/4f8255a2c763479837f69f1dccf2a3338730cd79)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | xitanggg/open-resume |
| Description | OpenResume is a powerful open-source resume builder and resume parser. https://open-resume.com/ |
| Stars | 8983 |
| Forks | 1046 |
| Licence | AGPL-3.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `4f8255a2c763479837f69f1dccf2a3338730cd79` |
| Retrieved at | 2026-11-14T19:13:39.078291+00:00 |
| Files in this snapshot | 130 |

## Directory tree

```text
public/  (17 files)
  assets/  (13 files)
    add-pdf.svg
    dots.svg
    feature-free.svg
    feature-open-source.svg
    feature-privacy.svg
    feature-us.svg
    heart.svg
    logo-amazon.svg
    logo-columbia.svg
    logo-cornell.svg
    logo-dropbox.svg
    logo-google.svg
    logo-northeastern.svg
  fonts/  (3 files)
    OFL.txt
    fonts-zh.css
    fonts.css
  logo.svg
src/  (98 files)
  app/  (98 files)
    components/  (48 files)
      … 48 files under this directory
    home/  (8 files)
      … 8 files under this directory
    lib/  (33 files)
      … 33 files under this directory
    resume-builder/  (1 files)
      … 1 files under this directory
    resume-import/  (1 files)
      … 1 files under this directory
    resume-parser/  (3 files)
      … 3 files under this directory
    globals-css.ts
    globals.css
    layout.tsx
    page.tsx
.dockerignore
.eslintrc.json
.gitignore
.prettierignore
Dockerfile
LICENSE
README.md
jest.config.mjs
next.config.js
package.json
postcss.config.js
prettier.config.js
prettierignore
tailwind.config.js
tsconfig.json
```

## Entry points

- [src/app/page.tsx](https://github.com/xitanggg/open-resume/blob/4f8255a2c763479837f69f1dccf2a3338730cd79/src/app/page.tsx)
- [src/app/resume-builder/page.tsx](https://github.com/xitanggg/open-resume/blob/4f8255a2c763479837f69f1dccf2a3338730cd79/src/app/resume-builder/page.tsx)
- [src/app/resume-import/page.tsx](https://github.com/xitanggg/open-resume/blob/4f8255a2c763479837f69f1dccf2a3338730cd79/src/app/resume-import/page.tsx)
- [src/app/resume-parser/page.tsx](https://github.com/xitanggg/open-resume/blob/4f8255a2c763479837f69f1dccf2a3338730cd79/src/app/resume-parser/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 97 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.eslintrc.json` (config)
- `Dockerfile` (container)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 98 analysed file(s)
- `public` — 17 analysed file(s)
- `(root files)` — 15 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4f8255a2c763479837f69f1dccf2a3338730cd79` is the revision these paths and observations refer to.
