# Project structure: ConardLi/easy-dataset

**Analysed commit:** `4002b09d9c5726cafb9f61a8d12765cb96a2d94b`

**Commit reference:** [4002b09d9c5726cafb9f61a8d12765cb96a2d94b](https://github.com/ConardLi/easy-dataset/commit/4002b09d9c5726cafb9f61a8d12765cb96a2d94b)

**Tree at this commit:** [ConardLi/easy-dataset@4002b09d9c57](https://github.com/ConardLi/easy-dataset/tree/4002b09d9c5726cafb9f61a8d12765cb96a2d94b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | ConardLi/easy-dataset |
| Description | A powerful tool for creating datasets for LLM fine-tuning 、RAG and Eval |
| Stars | 15117 |
| Forks | 1546 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `4002b09d9c5726cafb9f61a8d12765cb96a2d94b` |
| Retrieved at | 2026-11-14T19:11:41.435014+00:00 |
| Files in this snapshot | 535 |

## Directory tree

```text
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature-or-enhancement-.md
    question.md
  workflows/  (1 files)
    docker-build.yml
  PULL_REQUEST_TEMPLATE.md
.husky/  (2 files)
  commit-msg
  pre-commit
app/  (238 files)
  api/  (104 files)
    check-update/  (1 files)
      … 1 files under this directory
    llm/  (4 files)
      … 4 files under this directory
    monitoring/  (3 files)
      … 3 files under this directory
    projects/  (95 files)
      … 95 files under this directory
    update/  (1 files)
      … 1 files under this directory
  dataset-square/  (1 files)
    page.js
  monitoring/  (5 files)
    components/  (3 files)
      … 3 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    page.js
  projects/  (125 files)
    [projectId]/  (125 files)
      … 125 files under this directory
  globals.css
  layout.js
  page.js
components/  (99 files)
  Navbar/  (9 files)
    ActionButtons.js
    ContextBar.js
    DesktopMenus.js
    Logo.js
    MobileDrawer.js
    NavigationTabs.js
    contextBarStyles.js
    index.js
    styles.js
  common/  (1 files)
    MessageAlert.js
  conversations/  (4 files)
    ConversationContent.js
    ConversationHeader.js
    ConversationMetadata.js
    ConversationRatingSection.js
  dataset-square/  (3 files)
    DatasetSearchBar.js
    DatasetSiteCard.js
    DatasetSiteList.js
  datasets/  (14 files)
    import/  (3 files)
      … 3 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    DatasetHeader.js
    DatasetMetadata.js
    DatasetRatingSection.js
    EditableField.js
    EvalVariantDialog.js
    ImportDatasetDialog.js
    NoteInput.js
    OptimizeDialog.js
    StarRating.js
    TagSelector.js
  distill/  (11 files)
    AutoDistillDialog.js
    AutoDistillProgress.js
    ConfirmDialog.js
    DistillTreeView.js
    QuestionGenerationDialog.js
    QuestionListItem.js
    TagEditDialog.js
    TagGenerationDialog.js
    TagMenu.js
    TagTreeItem.js
    utils.js
  export/  (3 files)
    HuggingFaceTab.js
    LlamaFactoryTab.js
    LocalExportTab.js
  home/  (7 files)
    CreateProjectDialog.js
    HeroSection.js
    MigrationDialog.js
    ParticleBackground.js
    ProjectCard.js
    ProjectList.js
    StatsCard.js
  mga/  (2 files)
    GaPairsIndicator.js
    GaPairsManager.js
  playground/  (5 files)
    ChatArea.js
    ChatMessage.js
    MessageInput.js
    ModelSelector.js
    PlaygroundHeader.js
  questions/  (2 files)
    QuestionListView.js
    QuestionTreeView.js
  settings/  (3 files)
    BasicSettings.js
    ModelSettings.js
    TaskSettings.js
  tasks/  (5 files)
    TaskActions.js
    TaskFilters.js
    TaskProgress.js
    TaskStatusChip.js
    TasksTable.js
  text-split/  (22 files)
    components/  (9 files)
      … 9 files under this directory
    BatchEditChunkDialog.js
    ChunkBatchDeleteDialog.js
    ChunkCard.js
    ChunkDeleteDialog.js
    ChunkFilterDialog.js
    ChunkList.js
    ChunkListHeader.js
    ChunkViewDialog.js
    DomainAnalysis.js
    FileUploader.js
    LoadingBackdrop.js
    MarkdownViewDialog.js
    PdfSettings.js
  ExportDatasetDialog.js
  ExportProgressDialog.js
  I18nProvider.js
  LanguageSwitcher.js
  ModelSelect.js
  TaskIcon.js
  ThemeRegistry.js
  UpdateChecker.js
constant/  (4 files)
  index.js
  model.js
  setting.js
  sites.json
electron/  (14 files)
  modules/  (9 files)
    cache.js
    database.js
    db-updater.js
    ipc-handlers.js
    logger.js
    menu.js
    server.js
    updater.js
    window-manager.js
  entitlements.mac.plist
  loading.html
  main.js
  preload.js
  util.js
hooks/  (6 files)
  useDebounce.js
  useFileProcessingStatus.js
  useGenerateDataset.js
  useModelPlayground.js
  useSnackbar.js
  useTaskSettings.js
lib/  (119 files)
  api/  (4 files)
    chunk.js
    file.js
    index.js
    task.js
  db/  (22 files)
    base.js
    chunks.js
    custom-prompts.js
    dataset-conversations.js
    datasets.js
    evalDatasets.js
    evalResults.js
    fileToDb.js
    files.js
    ga-pairs.js
    imageDatasets.js
    images.js
    index.js
    llm-models.js
    llm-providers.js
    model-config.js
    projects.js
    questionTemplates.js
    questions.js
    tags.js
    texts.js
    upload-files.js
  file/  (24 files)
    file-process/  (15 files)
      … 15 files under this directory
    split-markdown/  (8 files)
      … 8 files under this directory
    text-splitter.js
  llm/  (32 files)
    common/  (3 files)
      … 3 files under this directory
    core/  (8 files)
      … 8 files under this directory
    prompts/  (20 files)
      … 20 files under this directory
    usageLogger.js
  services/  (25 files)
    datasets/  (2 files)
      … 2 files under this directory
    eval/  (1 files)
      … 1 files under this directory
    evaluation/  (1 files)
      … 1 files under this directory
    ga/  (2 files)
      … 2 files under this directory
    images/  (1 files)
      … 1 files under this directory
    multi-turn/  (1 files)
      … 1 files under this directory
    questions/  (2 files)
      … 2 files under this directory
    tasks/  (13 files)
      … 13 files under this directory
    clean.js
    models.js
  util/  (10 files)
    async.js
    domain-tree.js
    file.js
    image.js
    logger.js
    modelIcon.js
    processInParallel.js
    providerLogo.js
    request.js
    sites-i18n.js
  i18n.js
  store.js
local-db/  (1 files)
  empty.txt
locales/  (5 files)
  en/  (1 files)
    translation.json
  it/  (1 files)
    translation.json
  pt-BR/  (1 files)
    translation.json
  tr/  (1 files)
    translation.json
  zh-CN/  (1 files)
    translation.json
prisma/  (3 files)
  generate-template.js
  schema.prisma
  sql.json
public/  (15 files)
  imgs/  (15 files)
    models/  (13 files)
      … 13 files under this directory
    providers/  (1 files)
      … 1 files under this directory
    logo.svg
styles/  (4 files)
  blindTest.js
  globals.css
  home.js
  playground.js
.dockerignore
.gitattributes
.gitignore
.prettierrc.js
.windsurfrules
AGENTS.md
AGENTS.tr.md
ARCHITECTURE.md
ARCHITECTURE.tr.md
Dockerfile
LICENSE
README.md
README.tr.md
README.zh-CN.md
commitlint.config.mjs
docker-compose.yml
docker-entrypoint.sh
jsconfig.json
next.config.js
package.json
```

## Entry points

- [electron/main.js](https://github.com/ConardLi/easy-dataset/blob/4002b09d9c5726cafb9f61a8d12765cb96a2d94b/electron/main.js)
- [app/dataset-square/page.js](https://github.com/ConardLi/easy-dataset/blob/4002b09d9c5726cafb9f61a8d12765cb96a2d94b/app/dataset-square/page.js)
- [app/monitoring/page.js](https://github.com/ConardLi/easy-dataset/blob/4002b09d9c5726cafb9f61a8d12765cb96a2d94b/app/monitoring/page.js)
- [app/page.js](https://github.com/ConardLi/easy-dataset/blob/4002b09d9c5726cafb9f61a8d12765cb96a2d94b/app/page.js)
- [app/projects/[projectId]/page.js](https://github.com/ConardLi/easy-dataset/blob/4002b09d9c5726cafb9f61a8d12765cb96a2d94b/app/projects/%5BprojectId%5D/page.js)
- [components/Navbar/index.js](https://github.com/ConardLi/easy-dataset/blob/4002b09d9c5726cafb9f61a8d12765cb96a2d94b/components/Navbar/index.js)
- [constant/index.js](https://github.com/ConardLi/easy-dataset/blob/4002b09d9c5726cafb9f61a8d12765cb96a2d94b/constant/index.js)
- [electron/modules/server.js](https://github.com/ConardLi/easy-dataset/blob/4002b09d9c5726cafb9f61a8d12765cb96a2d94b/electron/modules/server.js)
- [lib/api/index.js](https://github.com/ConardLi/easy-dataset/blob/4002b09d9c5726cafb9f61a8d12765cb96a2d94b/lib/api/index.js)
- [lib/db/index.js](https://github.com/ConardLi/easy-dataset/blob/4002b09d9c5726cafb9f61a8d12765cb96a2d94b/lib/db/index.js)
- [lib/file/file-process/index.js](https://github.com/ConardLi/easy-dataset/blob/4002b09d9c5726cafb9f61a8d12765cb96a2d94b/lib/file/file-process/index.js)
- [lib/file/split-markdown/index.js](https://github.com/ConardLi/easy-dataset/blob/4002b09d9c5726cafb9f61a8d12765cb96a2d94b/lib/file/split-markdown/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 108 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 126 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 96 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 21 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constant package | library | Observed | Groups 3 file(s) under constant package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 22 file(s) under data layer (observed from repository paths and static analysis). |
| electron package | library | Observed | Groups 12 file(s) under electron package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 6 file(s) under hooks package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 56 file(s) under lib package (observed from repository paths and static analysis). |
| prisma package | library | Observed | Groups 1 file(s) under prisma package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 37 file(s) under service / domain layer (observed from repository paths and static analysis). |
| styles package | library | Observed | Groups 3 file(s) under styles package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/workflows/docker-build.yml` (ci)
- `Dockerfile` (container)
- `constant/sites.json` (config)
- `docker-compose.yml` (container)
- `jsconfig.json` (config)
- `locales/en/translation.json` (config)
- `locales/it/translation.json` (config)
- `locales/pt-BR/translation.json` (config)
- `locales/tr/translation.json` (config)
- `locales/zh-CN/translation.json` (config)
- `package.json` (manifest)
- `prisma/sql.json` (config)

## Top-level layout

- `app` — 238 analysed file(s)
- `lib` — 119 analysed file(s)
- `components` — 99 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `public` — 15 analysed file(s)
- `electron` — 14 analysed file(s)
- `hooks` — 6 analysed file(s)
- `.github` — 5 analysed file(s)
- `locales` — 5 analysed file(s)
- `constant` — 4 analysed file(s)
- `styles` — 4 analysed file(s)
- `prisma` — 3 analysed file(s)
- `.husky` — 2 analysed file(s)
- `local-db` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4002b09d9c5726cafb9f61a8d12765cb96a2d94b` is the revision these paths and observations refer to.
