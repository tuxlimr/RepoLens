# Project structure: node-inspector/node-inspector

**Analysed commit:** `79e01c049286374f86dd560742a614019c02402f`

**Commit reference:** [79e01c049286374f86dd560742a614019c02402f](https://github.com/node-inspector/node-inspector/commit/79e01c049286374f86dd560742a614019c02402f)

**Tree at this commit:** [node-inspector/node-inspector@79e01c049286](https://github.com/node-inspector/node-inspector/tree/79e01c049286374f86dd560742a614019c02402f)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | node-inspector/node-inspector |
| Description | Node.js debugger based on Blink Developer Tools |
| Stars | 12637 |
| Forks | 714 |
| Licence | BSD-2-Clause |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `79e01c049286374f86dd560742a614019c02402f` |
| Retrieved at | 2026-11-14T19:12:04.305659+00:00 |
| Files in this snapshot | 545 |

## Directory tree

```text
bin/  (3 files)
  inspector.js
  node-debug.js
  run-repl.js
docs/  (1 files)
  embedding.md
front-end/  (451 files)
  Images/  (8 files)
    src/  (8 files)
      … 8 files under this directory
  UglifyJS/  (1 files)
    parse-js.js
  audits/  (11 files)
    AuditCategories.js
    AuditCategory.js
    AuditController.js
    AuditExtensionCategory.js
    AuditFormatters.js
    AuditLauncherView.js
    AuditResultView.js
    AuditRules.js
    AuditsPanel.js
    auditsPanel.css
    module.json
  bindings/  (21 files)
    BreakpointManager.js
    CSSWorkspaceBinding.js
    CompilerScriptMapping.js
    ContentProviderBasedProjectDelegate.js
    ContentScriptProjectDecorator.js
    DebuggerWorkspaceBinding.js
    DefaultScriptMapping.js
    FileUtils.js
    Linkifier.js
    LiveLocation.js
    NetworkUISourceCodeProvider.js
    NetworkWorkspaceBinding.js
    PresentationConsoleMessageHelper.js
    ResourceScriptMapping.js
    ResourceUtils.js
    SASSSourceMapping.js
    ScriptSnippetModel.js
    StylesSourceMapping.js
    TempFile.js
    WorkspaceController.js
    module.json
  cm/  (20 files)
    LICENSE
    LICENSE_python
    PRESUBMIT.py
    clike.js
    closebrackets.js
    codemirror.css
    coffeescript.js
    comment.js
    css.js
    headlesscodemirror.js
    htmlembedded.js
    htmlmixed.js
    javascript.js
    markselection.js
    matchbrackets.js
    overlay.js
    php.js
    python.js
    shell.js
    xml.js
  common/  (20 files)
    Color.js
    Console.js
    ContentProvider.js
    Geometry.js
    Lock.js
    ModuleExtensionInterfaces.js
    NotificationService.js
    Object.js
    ParsedURL.js
    Progress.js
    ResourceType.js
    Settings.js
    StaticContentProvider.js
    TextRange.js
    TextUtils.js
    Throttler.js
    UIString.js
    WebInspector.js
    WorkerRuntime.js
    module.json
  components/  (16 files)
    CookiesTable.js
    DOMBreakpointsSidebarPane.js
    DOMPresentationUtils.js
    DockController.js
    Drawer.js
    ExecutionContextSelector.js
    HandlerRegistry.js
    InspectElementModeController.js
    InspectorView.js
    NativeBreakpointsSidebarPane.js
    ObjectPopoverHelper.js
    ObjectPropertiesSection.js
    ShortcutsScreen.js
    TargetsComboBoxController.js
    breakpointsList.css
    module.json
  console/  (5 files)
    ConsolePanel.js
    ConsoleView.js
    ConsoleViewMessage.js
    consoleView.css
    module.json
  devices/  (3 files)
    DevicesView.js
    devicesView.css
    module.json
  devtools_app/  (5 files)
    DevToolsAPI.js
    DevToolsApp.js
    InspectorFrontendHostImpl.js
    UITests.js
    module.json
  documentation/  (6 files)
    DocumentationCatalog.js
    DocumentationView.js
    JSArticle.js
    WikiParser.js
    documentationView.css
    module.json
  elements/  (17 files)
    AnimationsSidebarPane.js
    ElementsBreadcrumbs.js
    ElementsPanel.js
    ElementsSidebarPane.js
    ElementsTreeOutline.js
    EventListenersSidebarPane.js
    MetricsSidebarPane.js
    PlatformFontsSidebarPane.js
    PropertiesSidebarPane.js
    Spectrum.js
    StylesSectionModel.js
    StylesSidebarPane.js
    breadcrumbs.css
    elementsPanel.css
    elementsTreeOutline.css
    module.json
    spectrum.css
  extensions/  (7 files)
    ExtensionAPI.js
    ExtensionAuditCategory.js
    ExtensionPanel.js
    ExtensionRegistryStub.js
    ExtensionServer.js
    ExtensionView.js
    module.json
  heap_snapshot_worker/  (7 files)
    AllocationProfile.js
    HeapSnapshot.js
    HeapSnapshotLoader.js
    HeapSnapshotWorker.js
    HeapSnapshotWorkerDispatcher.js
    JSHeapSnapshot.js
    module.json
  host/  (4 files)
    InspectorFrontendHost.js
    Platform.js
    UserMetrics.js
    module.json
  layers/  (3 files)
    LayerPaintProfilerView.js
    LayersPanel.js
    module.json
  main/  (13 files)
    AdvancedApp.js
    App.js
    HelpScreenUntilReload.js
    Main.js
    OverridesView.js
    RenderingOptions.js
    ScreencastApp.js
    SimpleApp.js
    TestController.js
    Tests.js
    accelerometer.css
    module.json
    overrides.css
  network/  (22 files)
    FilterSuggestionBuilder.js
    HARWriter.js
    NetworkDataGridNode.js
    NetworkItemView.js
    NetworkLogView.js
    NetworkPanel.js
    NetworkTimeCalculator.js
    RequestCookiesView.js
    RequestHTMLView.js
    RequestHeadersView.js
    RequestJSONView.js
    RequestPreviewView.js
    RequestResponseView.js
    RequestTimingView.js
    RequestView.js
    ResourceWebSocketFrameView.js
    module.json
    networkLogView.css
    networkPanel.css
    requestCookiesView.css
    requestHeadersView.css
    webSocketFrameView.css
  platform/  (4 files)
    DOMExtension.js
    Promise.js
    module.json
    utilities.js
  profiler/  (19 files)
    CPUProfileBottomUpDataGrid.js
    CPUProfileDataGrid.js
    CPUProfileFlameChart.js
    CPUProfileTopDownDataGrid.js
    CPUProfileView.js
    CanvasProfileView.js
    CanvasReplayStateView.js
    HeapSnapshotCommon.js
    HeapSnapshotDataGrids.js
    HeapSnapshotGridNodes.js
    HeapSnapshotProxy.js
    HeapSnapshotView.js
    ProfileLauncherView.js
    ProfileTypeRegistry.js
    ProfilesPanel.js
    canvasProfiler.css
    heapProfiler.css
    module.json
    profilesPanel.css
  promises/  (3 files)
    PromisePane.js
    module.json
    promisePane.css
  resources/  (13 files)
    ApplicationCacheItemsView.js
    CookieItemsView.js
    DOMStorageItemsView.js
    DatabaseQueryView.js
    DatabaseTableView.js
    DirectoryContentView.js
    FileContentView.js
    FileSystemView.js
    IndexedDBViews.js
    ResourcesPanel.js
    indexedDBViews.css
    module.json
    resourcesPanel.css
  screencast/  (3 files)
    ScreencastView.js
    module.json
    screencastView.css
  script_formatter_worker/  (4 files)
    CSSFormatter.js
    JavaScriptFormatter.js
    ScriptFormatterWorker.js
    module.json
  sdk/  (39 files)
    AnimationModel.js
    ApplicationCacheModel.js
    BlackboxSupport.js
    CPUProfileDataModel.js
    CPUProfilerModel.js
    CSSMetadata.js
    CSSParser.js
    CSSStyleModel.js
    ConsoleModel.js
    ContentProviders.js
    CookieParser.js
    DOMModel.js
    DOMStorage.js
    Database.js
    DebuggerModel.js
    FileSystemModel.js
    HAREntry.js
    HeapProfilerModel.js
    IndexedDBModel.js
    InspectorBackend.js
    LayerTreeModel.js
    NetworkLog.js
    NetworkManager.js
    NetworkRequest.js
    … 15 more files
  settings/  (4 files)
    EditFileSystemDialog.js
    FrameworkBlackboxDialog.js
    SettingsScreen.js
    module.json
  source_frame/  (12 files)
    CodeMirrorTextEditor.js
    CodeMirrorUtils.js
    FontView.js
    GoToLineDialog.js
    ImageView.js
    ResourceSourceFrame.js
    SourceFrame.js
    cmdevtools.css
    fontView.css
    imageView.css
    module.json
    resourceSourceFrame.css
  sources/  (35 files)
    AddSourceMapURLDialog.js
    AdvancedSearchView.js
    BreakpointsSidebarPane.js
    CSSSourceFrame.js
    CallStackSidebarPane.js
    EditingLocationHistoryManager.js
    FileBasedSearchResultsPane.js
    FilePathScoreFunction.js
    FilteredItemSelectionDialog.js
    InplaceFormatterEditorAction.js
    JavaScriptSourceFrame.js
    NavigatorView.js
    Placard.js
    RevisionHistoryView.js
    ScopeChainSidebarPane.js
    ScriptFormatter.js
    ScriptFormatterEditorAction.js
    SimpleHistoryManager.js
    SourcesNavigator.js
    SourcesPanel.js
    SourcesSearchScope.js
    SourcesView.js
    StyleSheetOutlineDialog.js
    TabbedEditorContainer.js
    … 11 more files
  temp_storage_shared_worker/  (2 files)
    TempStorageSharedWorker.js
    module.json
  timeline/  (26 files)
    CountersGraph.js
    LayerDetailsView.js
    LayerTreeOutline.js
    Layers3DView.js
    MemoryCountersGraph.js
    PaintProfilerView.js
    TimelineEventOverview.js
    TimelineFlameChart.js
    TimelineFrameModel.js
    TimelineFrameOverview.js
    TimelineJSProfile.js
    TimelineLayersView.js
    TimelineMemoryOverview.js
    TimelineModel.js
    TimelineOverviewPane.js
    TimelinePaintProfilerView.js
    TimelinePanel.js
    TimelinePowerGraph.js
    TimelinePowerOverview.js
    TimelinePresentationModel.js
    TimelineUIUtils.js
    TimelineView.js
    TracingModel.js
    TransformController.js
    … 2 more files
  toolbox/  (6 files)
    InspectedPagePlaceholder.js
    MediaQueryInspector.js
    OverridesUI.js
    ResponsiveDesignView.js
    module.json
    responsiveDesignView.css
  toolbox_bootstrap/  (2 files)
    Toolbox.js
    module.json
  ui/  (57 files)
    ActionRegistry.js
    CompletionDictionary.js
    Context.js
    ContextMenu.js
    DOMSyntaxHighlighter.js
    DataGrid.js
    Dialog.js
    DropDownMenu.js
    EmptyView.js
    FilterBar.js
    FlameChart.js
    ForwardedInputEventHandler.js
    HelpScreen.js
    InplaceEditor.js
    KeyboardShortcut.js
    OverviewGrid.js
    Panel.js
    PieChart.js
    Popover.js
    ProgressIndicator.js
    ResizerWidget.js
    RootView.js
    SearchableView.js
    Section.js
    … 33 more files
  workspace/  (9 files)
    FileManager.js
    FileSystemMapping.js
    FileSystemWorkspaceBinding.js
    IsolatedFileSystem.js
    IsolatedFileSystemManager.js
    SearchConfig.js
    UISourceCode.js
    Workspace.js
    module.json
  OWNERS
  Runtime.js
  devtools.css
  devtools.html
  devtools.js
  devtools.json
  dialog.css
  externs.js
  inspector.css
  inspector.html
  inspector.js
  inspector.json
  inspectorCommon.css
  inspectorStyle.css
  inspectorSyntaxHighlight.css
  popover.css
  sidebarPane.css
  suggestBox.css
  tabbedPane.css
  toolbox.css
  toolbox.html
  toolbox.js
  toolbox.json
  treeoutline.js
front-end-node/  (17 files)
  console/  (2 files)
    ConsoleExtentions.js
    module.json
  main/  (2 files)
    MainOverrides.js
    module.json
  network/  (2 files)
    NetworkPanel.js
    module.json
  profiler/  (2 files)
    SaveOverrides.js
    module.json
  settings/  (3 files)
    SettingsScreenOverrides.css
    SettingsScreenOverrides.js
    module.json
  sources/  (2 files)
    SourcesOverrides.js
    module.json
  NodeInspectorOverrides.js
  inspector.json
  module.json
  protocol.json
lib/  (29 files)
  Injections/  (4 files)
    ConsoleAgent.js
    HeapProfilerAgent.js
    NetworkAgent.js
    ProfilerAgent.js
  BreakEventHandler.js
  CallFramesProvider.js
  ConsoleAgent.js
  ConsoleClient.js
  DebuggerAgent.js
  DebuggerClient.js
  FrontendClient.js
  FrontendCommandHandler.js
  HeapProfilerAgent.js
  HeapProfilerClient.js
  InjectorClient.js
  InjectorServer.js
  NetworkAgent.js
  PageAgent.js
  ProfilerAgent.js
  RuntimeAgent.js
  ScriptFileStorage.js
  ScriptManager.js
  callback.js
  config.js
  convert.js
  debug-server.js
  debugger.js
  plugins.js
  … 1 more files
test/  (28 files)
  fixtures/  (6 files)
    BreakInFunction.js
    Commandlet.js
    InspectObject.js
    LiveEdit.js
    PeriodicConsoleLog.js
    ssl_cert_and_key.txt
  helpers/  (3 files)
    SessionStub.js
    launcher.js
    wsmock.js
  CallFramesProvider.js
  ConsoleAgent.js
  DebuggerAgent.js
  DebuggerClient.js
  FrontendCommandHandler.test.js
  HeapProfilerAgent.js
  InjectorClient.js
  NetworkAgent.js
  PageAgent.js
  ProfilerAgent.js
  RuntimeAgent.js
  ScriptFileStorage.js
  ScriptManager.js
  config.js
  convert.js
  index.js
  mocha.opts
  node-debug.test.js
  plugins.js
tools/  (3 files)
  git-changelog.sh
  release.sh
  update-front-end.sh
.gitattributes
.gitignore
.jshintignore
.jshintrc
.npmignore
.travis.yml
CONTRIBUTING.md
ChangeLog.md
LICENSE
MAINTAINERS.md
README.md
index.js
package.json
```

## Entry points

- [bin/inspector.js](https://github.com/node-inspector/node-inspector/blob/79e01c049286374f86dd560742a614019c02402f/bin/inspector.js)
- [bin/node-debug.js](https://github.com/node-inspector/node-inspector/blob/79e01c049286374f86dd560742a614019c02402f/bin/node-debug.js)
- [front-end/main/App.js](https://github.com/node-inspector/node-inspector/blob/79e01c049286374f86dd560742a614019c02402f/front-end/main/App.js)
- [front-end/main/Main.js](https://github.com/node-inspector/node-inspector/blob/79e01c049286374f86dd560742a614019c02402f/front-end/main/Main.js)
- [index.js](https://github.com/node-inspector/node-inspector/blob/79e01c049286374f86dd560742a614019c02402f/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 3 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 48 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| front-end package | library | Observed | Groups 343 file(s) under front-end package (observed from repository paths and static analysis). Observed top-level functions: CheckChangeOnUpload, _CheckCodeMirrorChanges. |
| front-end-node package | library | Observed | Groups 6 file(s) under front-end-node package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 29 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 28 file(s) under tests (observed from repository paths and static analysis). |
| tools package | library | Observed | Groups 3 file(s) under tools package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `front-end-node/console/module.json` (config)
- `front-end-node/inspector.json` (config)
- `front-end-node/main/module.json` (config)
- `front-end-node/module.json` (config)
- `front-end-node/network/module.json` (config)
- `front-end-node/profiler/module.json` (config)
- `front-end-node/protocol.json` (config)
- `front-end-node/settings/module.json` (config)
- `front-end-node/sources/module.json` (config)
- `front-end/audits/module.json` (config)
- `front-end/bindings/module.json` (config)
- `front-end/common/module.json` (config)
- `front-end/components/module.json` (config)
- `front-end/console/module.json` (config)
- `front-end/devices/module.json` (config)
- `front-end/devtools.json` (config)
- `front-end/devtools_app/module.json` (config)
- `front-end/documentation/module.json` (config)
- `front-end/elements/module.json` (config)
- `front-end/extensions/module.json` (config)
- `front-end/heap_snapshot_worker/module.json` (config)
- `front-end/host/module.json` (config)
- `front-end/inspector.json` (config)
- `front-end/layers/module.json` (config)
- `front-end/main/module.json` (config)
- `front-end/network/module.json` (config)
- `front-end/platform/module.json` (config)
- `front-end/profiler/module.json` (config)
- `front-end/promises/module.json` (config)
- `front-end/resources/module.json` (config)
- `front-end/screencast/module.json` (config)
- `front-end/script_formatter_worker/module.json` (config)
- `front-end/sdk/module.json` (config)
- `front-end/settings/module.json` (config)
- `front-end/source_frame/module.json` (config)
- `front-end/sources/module.json` (config)
- `front-end/temp_storage_shared_worker/module.json` (config)
- `front-end/timeline/module.json` (config)
- `front-end/toolbox.json` (config)
- `front-end/toolbox/module.json` (config)
- `front-end/toolbox_bootstrap/module.json` (config)
- `front-end/ui/module.json` (config)
- `front-end/workspace/module.json` (config)
- `package.json` (manifest)

## Top-level layout

- `front-end` — 451 analysed file(s)
- `lib` — 29 analysed file(s)
- `test` — 28 analysed file(s)
- `front-end-node` — 17 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `bin` — 3 analysed file(s)
- `tools` — 3 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `79e01c049286374f86dd560742a614019c02402f` is the revision these paths and observations refer to.
