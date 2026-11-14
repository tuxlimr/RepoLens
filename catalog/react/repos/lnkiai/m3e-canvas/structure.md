# Project structure: lnkiai/m3e-canvas

**Analysed commit:** `49378e1e35f5de6aaadfcd3f852eeb0edffdbb95`

**Commit reference:** [49378e1e35f5de6aaadfcd3f852eeb0edffdbb95](https://github.com/lnkiai/m3e-canvas/commit/49378e1e35f5de6aaadfcd3f852eeb0edffdbb95)

**Tree at this commit:** [lnkiai/m3e-canvas@49378e1e35f5](https://github.com/lnkiai/m3e-canvas/tree/49378e1e35f5de6aaadfcd3f852eeb0edffdbb95)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | lnkiai/m3e-canvas |
| Description | Sketch Material 3 Expressive screens in the browser and turn them into vibe-coding prompts. |
| Stars | 10345 |
| Forks | 1137 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `49378e1e35f5de6aaadfcd3f852eeb0edffdbb95` |
| Retrieved at | 2026-11-14T19:13:31.516507+00:00 |
| Files in this snapshot | 98 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.yml
    config.yml
    feature_request.yml
    part_request.yml
  workflows/  (2 files)
    ci.yml
    deploy.yml
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
app/  (5 files)
  globals.css
  icon.svg
  layout.tsx
  manifest.webmanifest
  page.tsx
components/  (29 files)
  __snapshots__/  (1 files)
    Loading.test.tsx.snap
  AiPanel.tsx
  ButtonInspector.tsx
  CardStage.tsx
  ColorPanel.tsx
  FramePanel.tsx
  IconPicker.tsx
  Inspector.tsx
  Layers.tsx
  Loading.test.tsx
  Loading.tsx
  Logo.tsx
  M3Node.tsx
  Menus.tsx
  Mobile.tsx
  PartInspector.tsx
  PartPanel.tsx
  PartsPalette.tsx
  Pickers.tsx
  Preview.test.tsx
  Preview.tsx
  PromptPanel.tsx
  ShareMenu.tsx
  SizeHandles.tsx
  Skeleton.tsx
  … 4 more files
lib/  (33 files)
  ai.test.ts
  ai.ts
  button.test.ts
  color.extended.test.ts
  color.test.ts
  color.ts
  i18n.parity.test.ts
  i18n.test.ts
  i18n.ts
  pickers.test.ts
  project.test.ts
  project.ts
  prompt.extended.test.ts
  prompt.test.ts
  prompt.ts
  promptMarks.test.ts
  rail.test.ts
  rail.ts
  railView.test.ts
  railView.ts
  shapes.extended.test.ts
  shapes.test.ts
  shapes.ts
  share.test.ts
  … 9 more files
public/  (6 files)
  logos/  (4 files)
    claude.svg
    deepseek.svg
    gemini.svg
    openai.svg
  .nojekyll
  agent.md
.gitignore
AGENTS.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
NOTICE
README.ja.md
README.ko.md
README.md
README.zh.md
SECURITY.md
next.config.ts
package.json
postcss.config.mjs
tsconfig.json
```

## Entry points

- [app/page.tsx](https://github.com/lnkiai/m3e-canvas/blob/49378e1e35f5de6aaadfcd3f852eeb0edffdbb95/app/page.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 2 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 28 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 33 file(s) under lib package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/ISSUE_TEMPLATE/part_request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/deploy.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `lib` — 33 analysed file(s)
- `components` — 29 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 9 analysed file(s)
- `public` — 6 analysed file(s)
- `app` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `49378e1e35f5de6aaadfcd3f852eeb0edffdbb95` is the revision these paths and observations refer to.
