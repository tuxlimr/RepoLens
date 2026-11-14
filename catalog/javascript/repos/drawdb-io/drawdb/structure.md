# Project structure: drawdb-io/drawdb

**Analysed commit:** `af09640e1238c36e11f3c9b582bf1f88e89c46cf`

**Commit reference:** [af09640e1238c36e11f3c9b582bf1f88e89c46cf](https://github.com/drawdb-io/drawdb/commit/af09640e1238c36e11f3c9b582bf1f88e89c46cf)

**Tree at this commit:** [drawdb-io/drawdb@af09640e1238](https://github.com/drawdb-io/drawdb/tree/af09640e1238c36e11f3c9b582bf1f88e89c46cf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | drawdb-io/drawdb |
| Description | Free, simple, and intuitive online database diagram editor and SQL generator. |
| Stars | 40327 |
| Forks | 3365 |
| Licence | AGPL-3.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `af09640e1238c36e11f3c9b582bf1f88e89c46cf` |
| Retrieved at | 2026-11-14T19:10:40.550304+00:00 |
| Files in this snapshot | 284 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (2 files)
    build.yml
    docker.yml
  FUNDING.yml
.husky/  (1 files)
  pre-commit
public/  (2 files)
  config.js
  robots.txt
src/  (260 files)
  animations/  (2 files)
    FadeIn.jsx
    SlideIn.jsx
  api/  (2 files)
    email.js
    gists.js
  components/  (83 files)
    CodeEditor/  (2 files)
      … 2 files under this directory
    EditorCanvas/  (7 files)
      … 7 files under this directory
    EditorHeader/  (23 files)
      … 23 files under this directory
    EditorSidePanel/  (35 files)
      … 35 files under this directory
    LexicalEditor/  (6 files)
      … 6 files under this directory
    SortableList/  (3 files)
      … 3 files under this directory
    FloatingControls.jsx
    MigrationBanner.jsx
    Navbar.jsx
    SimpleCanvas.jsx
    StartModal.jsx
    Thumbnail.jsx
    Workspace.jsx
  config/  (1 files)
    index.js
  context/  (15 files)
    AreasContext.jsx
    CanvasContext.jsx
    CollabContext.jsx
    DiagramContext.jsx
    EnumsContext.jsx
    ExtensionsContext.jsx
    LayoutContext.jsx
    NotesContext.jsx
    SaveStateContext.jsx
    SelectContext.jsx
    SettingsContext.jsx
    TransformContext.jsx
    TypesContext.jsx
    UndoRedoContext.jsx
    ViewsContext.jsx
  data/  (10 files)
    constants.js
    databases.js
    datatypes.js
    db.js
    editorConfig.js
    heroDiagram.js
    schemas.js
    seeds.js
    socials.js
    surveyQuestions.js
  hooks/  (19 files)
    index.js
    useAreaMembership.js
    useAreas.js
    useCanvas.js
    useCollab.js
    useDiagram.js
    useEnums.js
    useFullscreen.js
    useLayout.js
    useNavigateWithParams.js
    useNotes.js
    useSaveState.js
    useSelect.js
    useSettings.js
    useThemedPage.js
    useTransform.js
    useTypes.js
    useUndoRedo.js
    useViews.js
  i18n/  (53 files)
    locales/  (51 files)
      … 51 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    i18n.js
  icons/  (8 files)
    IconAddArea.jsx
    IconAddNote.jsx
    IconAddTable.jsx
    IconAddView.jsx
    IconRelationship.jsx
    IconSparkles.jsx
    IconTable.jsx
    index.js
  pages/  (5 files)
    BugReport.jsx
    Editor.jsx
    LandingPage.jsx
    NotFound.jsx
    Templates.jsx
  templates/  (6 files)
    template1.js
    template2.js
    template3.js
    template4.js
    template5.js
    template6.js
  utils/  (53 files)
    dbml/  (5 files)
      … 5 files under this directory
    exportAs/  (3 files)
      … 3 files under this directory
    exportSQL/  (9 files)
      … 9 files under this directory
    importFrom/  (8 files)
      … 8 files under this directory
    importSQL/  (8 files)
      … 8 files under this directory
    migrations/  (1 files)
      … 1 files under this directory
    arrangeTables.js
    autoArrange.js
    autoRelationships.js
    cache.js
    calcPath.js
    customTypes.js
    diff.js
    dismissedBanners.js
    exportSavedData.js
    fullscreen.js
    importAiDiagram.js
    issues.js
    layout.js
    modalData.js
    queryConfig.js
    rect.js
    utils.js
    validateSchema.js
    views.js
  App.jsx
  index.css
  main.jsx
.dockerignore
.env.sample
.eslintrc.cjs
.gitignore
.prettierrc.json
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
compose.yml
index.html
package.json
postcss.config.js
tailwind.config.js
vercel.json
vite.config.js
```

## Entry points

- [src/App.jsx](https://github.com/drawdb-io/drawdb/blob/af09640e1238c36e11f3c9b582bf1f88e89c46cf/src/App.jsx)
- [src/components/CodeEditor/index.jsx](https://github.com/drawdb-io/drawdb/blob/af09640e1238c36e11f3c9b582bf1f88e89c46cf/src/components/CodeEditor/index.jsx)
- [src/config/index.js](https://github.com/drawdb-io/drawdb/blob/af09640e1238c36e11f3c9b582bf1f88e89c46cf/src/config/index.js)
- [src/hooks/index.js](https://github.com/drawdb-io/drawdb/blob/af09640e1238c36e11f3c9b582bf1f88e89c46cf/src/hooks/index.js)
- [src/icons/index.js](https://github.com/drawdb-io/drawdb/blob/af09640e1238c36e11f3c9b582bf1f88e89c46cf/src/icons/index.js)
- [src/main.jsx](https://github.com/drawdb-io/drawdb/blob/af09640e1238c36e11f3c9b582bf1f88e89c46cf/src/main.jsx)
- [src/utils/exportSQL/index.js](https://github.com/drawdb-io/drawdb/blob/af09640e1238c36e11f3c9b582bf1f88e89c46cf/src/utils/exportSQL/index.js)
- [src/utils/importSQL/index.js](https://github.com/drawdb-io/drawdb/blob/af09640e1238c36e11f3c9b582bf1f88e89c46cf/src/utils/importSQL/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| animations package | library | Observed | Groups 2 file(s) under animations package (observed from repository paths and static analysis). |
| API layer | api | Observed | Groups 2 file(s) under api layer (observed from repository paths and static analysis). |
| App.jsx package | library | Observed | Groups 1 file(s) under app.jsx package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 82 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| context package | library | Observed | Groups 15 file(s) under context package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 10 file(s) under data layer (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 19 file(s) under hooks package (observed from repository paths and static analysis). |
| i18n package | library | Observed | Groups 53 file(s) under i18n package (observed from repository paths and static analysis). |
| icons package | library | Observed | Groups 8 file(s) under icons package (observed from repository paths and static analysis). |
| main.jsx package | library | Observed | Groups 1 file(s) under main.jsx package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 5 file(s) under pages package (observed from repository paths and static analysis). |
| public package | library | Observed | Groups 1 file(s) under public package (observed from repository paths and static analysis). |
| templates package | library | Observed | Groups 6 file(s) under templates package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 53 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.env.sample` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/docker.yml` (ci)
- `.prettierrc.json` (config)
- `Dockerfile` (container)
- `compose.yml` (container)
- `package.json` (manifest)
- `vercel.json` (config)

## Top-level layout

- `src` — 260 analysed file(s)
- `(root files)` — 16 analysed file(s)
- `.github` — 5 analysed file(s)
- `public` — 2 analysed file(s)
- `.husky` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `af09640e1238c36e11f3c9b582bf1f88e89c46cf` is the revision these paths and observations refer to.
