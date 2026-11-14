# Project structure: tyroprogrammer/learn-react-app

**Analysed commit:** `a41485ee612d35f32fca56c2d2de41d2092fc026`

**Commit reference:** [a41485ee612d35f32fca56c2d2de41d2092fc026](https://github.com/tyroprogrammer/learn-react-app/commit/a41485ee612d35f32fca56c2d2de41d2092fc026)

**Tree at this commit:** [tyroprogrammer/learn-react-app@a41485ee612d](https://github.com/tyroprogrammer/learn-react-app/tree/a41485ee612d35f32fca56c2d2de41d2092fc026)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tyroprogrammer/learn-react-app |
| Description | Application that will help you learn React fundamentals. Install this application locally - there's tutorial, code snippets and exercises. The main objective of this project is to help you get off the ground with React! |
| Stars | 3841 |
| Forks | 338 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `a41485ee612d35f32fca56c2d2de41d2092fc026` |
| Retrieved at | 2026-11-14T19:15:03.697997+00:00 |
| Files in this snapshot | 74 |

## Directory tree

```text
public/  (2 files)
  index.html
  manifest.json
scripts/  (1 files)
  processMarkdown.js
src/  (64 files)
  api/  (2 files)
    CompanyDataGenerator.js
    DataApi.js
  capstone/  (9 files)
    solution/  (5 files)
      … 5 files under this directory
    Capstone.js
    CompanyFinancial.jsx
    CompanyProfile.jsx
    Search.jsx
  exercise/  (24 files)
    solution/  (8 files)
      … 8 files under this directory
    01-HelloWorld.js
    01-HelloWorld_ts.tsx
    02-IntroToJSX.js
    02-IntroToJSX_ts.tsx
    03-PowerOfJSX.js
    03-PowerOfJSX_ts.tsx
    04-Props.js
    04-Props_ts.tsx
    05-State.js
    05-State_ts.tsx
    06-LifecycleMethods.js
    06-LifecycleMethods_ts.tsx
    07-HandlingEvents.js
    07-HandlingEvents_ts.tsx
    08-ComposingComponents.js
    08-ComposingComponents_ts.tsx
  setup/  (13 files)
    renderer/  (3 files)
      … 3 files under this directory
    AppShell.js
    Exercise.jsx
    Home.js
    Markdown.jsx
    ScrollToTop.js
    Solution.jsx
    Tutorial.jsx
    TutorialMetadataApi.js
    TutorialNavigation.jsx
    tutorialMetadata.js
  tutorial/  (11 files)
    00-ReactIntroduction.md
    01-HelloWorld.md
    02-IntroToJSX.md
    03-PowerOfJSX.md
    04-Props.md
    05-State.md
    06-LifecycleMethods.md
    07-HandlingEvents.md
    08-ComposingComponents.md
    09-Capstone.md
    10-Conclusion.md
  App.js
  FileReader.js
  index.css
  index.js
  react-app-env.d.ts
.gitignore
.gitpod.yml
.travis.yml
LICENSE
README.md
package.json
tsconfig.json
```

## Entry points

- [src/App.js](https://github.com/tyroprogrammer/learn-react-app/blob/a41485ee612d35f32fca56c2d2de41d2092fc026/src/App.js)
- [src/index.js](https://github.com/tyroprogrammer/learn-react-app/blob/a41485ee612d35f32fca56c2d2de41d2092fc026/src/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 2 file(s) under api layer (observed from repository paths and static analysis). |
| App.js package | library | Observed | Groups 1 file(s) under app.js package (observed from repository paths and static analysis). |
| capstone package | library | Observed | Groups 9 file(s) under capstone package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| exercise package | library | Observed | Groups 24 file(s) under exercise package (observed from repository paths and static analysis). |
| FileReader.js package | library | Observed | Groups 1 file(s) under filereader.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| react-app-env.d.ts package | library | Observed | Groups 1 file(s) under react-app-env.d.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| setup package | library | Observed | Groups 12 file(s) under setup package (observed from repository paths and static analysis). |

## Important files

- `.gitpod.yml` (config)
- `.travis.yml` (ci)
- `package.json` (manifest)
- `public/manifest.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `src` — 64 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `public` — 2 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `a41485ee612d35f32fca56c2d2de41d2092fc026` is the revision these paths and observations refer to.
