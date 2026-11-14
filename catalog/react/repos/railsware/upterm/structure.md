# Project structure: railsware/upterm

**Analysed commit:** `6db8d5b89625fca9a3058e1e5956084867225e9c`

**Commit reference:** [6db8d5b89625fca9a3058e1e5956084867225e9c](https://github.com/railsware/upterm/commit/6db8d5b89625fca9a3058e1e5956084867225e9c)

**Tree at this commit:** [railsware/upterm@6db8d5b89625](https://github.com/railsware/upterm/tree/6db8d5b89625fca9a3058e1e5956084867225e9c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | railsware/upterm |
| Description | A terminal emulator for the 21st century. |
| Stars | 19045 |
| Forks | 605 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `6db8d5b89625fca9a3058e1e5956084867225e9c` |
| Retrieved at | 2026-11-14T19:13:11.700222+00:00 |
| Files in this snapshot | 157 |

## Directory tree

```text
docs/  (1 files)
  vscodedebugging.md
images/  (2 files)
  prompt-decoration.svg
  prompt-history-mode-decoration.svg
src/  (104 files)
  main/  (1 files)
    Main.ts
  monaco/  (4 files)
    Loader.ts
    PromptTheme.ts
    ShellHistoryLanguage.ts
    ShellLanguage.ts
  plugins/  (42 files)
    completion/  (26 files)
      … 26 files under this directory
    completion_utils/  (4 files)
      … 4 files under this directory
    AliasSuggestions.ts
    DotEnvLoader.ts
    GitGrep.tsx
    JSON.tsx
    JobFinishedNotifications.ts
    NVM.ts
    PWDOperatingSystemIntegrator.ts
    RVM.ts
    SaveHistory.ts
    SaveWindowBounds.ts
    Show.tsx
    UpdateLastPresentWorkingDirectory.ts
  services/  (8 files)
    FontService.ts
    GitService.ts
    HistoryService.ts
    JobsService.ts
    SessionsService.ts
    UpdatesService.ts
    WindowService.ts
    index.ts
  shell/  (9 files)
    Aliases.ts
    BuiltInCommands.ts
    CommandExecutor.ts
    Environment.ts
    Job.ts
    Parser.ts
    Prompt.ts
    Scanner.ts
    Session.ts
  utils/  (10 files)
    Common.ts
    Git.ts
    HistoryTrie.ts
    JSONTree.tsx
    Link.tsx
    ManPageParsingUtils.ts
    ManPages.ts
    OrderedSet.ts
    Process.ts
    Shell.ts
  views/  (20 files)
    css/  (4 files)
      … 4 files under this directory
    keyevents/  (1 files)
      … 1 files under this directory
    menu/  (1 files)
      … 1 files under this directory
    mouseevents/  (1 files)
      … 1 files under this directory
    ApplicationComponent.tsx
    JobComponent.tsx
    JobHeaderComponent.tsx
    Main.tsx
    OutputComponent.tsx
    PrettifyToggleComponent.tsx
    PromptComponent.tsx
    SearchComponent.tsx
    SessionComponent.tsx
    TabComponent.tsx
    TabHeaderComponent.tsx
    ViewUtils.ts
    index.html
  Autocompletion.ts
  Char.ts
  Decorators.ts
  EmitterWithUniqueID.ts
  Enums.ts
  Interfaces.ts
  Output.ts
  PTY.ts
  PluginManager.ts
  references.d.ts
test/  (32 files)
  shell/  (1 files)
    scanner_spec.ts
  test_files/  (22 files)
    file_names_test/  (1 files)
      … 1 files under this directory
    vttest/  (21 files)
      … 21 files under this directory
  utils/  (4 files)
    ManPages_spec.ts
    common_spec.ts
    history_trie_spec.ts
    ordered_set_spec.ts
  e2e.ts
  environment_spec.ts
  output_spec.ts
  pty_spec.ts
  references.d.ts
typings/  (6 files)
  Interfaces.d.ts
  Overrides.d.ts
  child-process-promise.d.ts
  dirStat.d.ts
  mode-to-permissions.d.ts
  uuid.d.ts
.dockerignore
.gitignore
.node-version
.nvmrc
.travis.yml
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
package.json
tsconfig.json
tslint.json
```

## Entry points

- [src/main/Main.ts](https://github.com/railsware/upterm/blob/6db8d5b89625fca9a3058e1e5956084867225e9c/src/main/Main.ts)
- [src/services/index.ts](https://github.com/railsware/upterm/blob/6db8d5b89625fca9a3058e1e5956084867225e9c/src/services/index.ts)
- [src/views/Main.tsx](https://github.com/railsware/upterm/blob/6db8d5b89625fca9a3058e1e5956084867225e9c/src/views/Main.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 19 file(s) under api layer (observed from repository paths and static analysis). |
| Autocompletion.ts package | library | Observed | Groups 1 file(s) under autocompletion.ts package (observed from repository paths and static analysis). |
| Char.ts package | library | Observed | Groups 1 file(s) under char.ts package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Decorators.ts package | library | Observed | Groups 1 file(s) under decorators.ts package (observed from repository paths and static analysis). |
| EmitterWithUniqueID.ts package | library | Observed | Groups 1 file(s) under emitterwithuniqueid.ts package (observed from repository paths and static analysis). |
| Enums.ts package | library | Observed | Groups 1 file(s) under enums.ts package (observed from repository paths and static analysis). |
| Interfaces.ts package | library | Observed | Groups 1 file(s) under interfaces.ts package (observed from repository paths and static analysis). |
| main package | library | Observed | Groups 1 file(s) under main package (observed from repository paths and static analysis). |
| monaco package | library | Observed | Groups 4 file(s) under monaco package (observed from repository paths and static analysis). |
| Output.ts package | library | Observed | Groups 1 file(s) under output.ts package (observed from repository paths and static analysis). |
| PluginManager.ts package | library | Observed | Groups 1 file(s) under pluginmanager.ts package (observed from repository paths and static analysis). |
| plugins package | library | Observed | Groups 42 file(s) under plugins package (observed from repository paths and static analysis). |
| PTY.ts package | library | Observed | Groups 1 file(s) under pty.ts package (observed from repository paths and static analysis). |
| references.d.ts package | library | Observed | Groups 1 file(s) under references.d.ts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 8 file(s) under service / domain layer (observed from repository paths and static analysis). |
| shell package | library | Observed | Groups 9 file(s) under shell package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 32 file(s) under tests (observed from repository paths and static analysis). |
| typings package | library | Observed | Groups 6 file(s) under typings package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 10 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.travis.yml` (ci)
- `Dockerfile` (container)
- `package.json` (manifest)
- `tsconfig.json` (config)
- `tslint.json` (config)

## Top-level layout

- `src` — 104 analysed file(s)
- `test` — 32 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `typings` — 6 analysed file(s)
- `images` — 2 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `6db8d5b89625fca9a3058e1e5956084867225e9c` is the revision these paths and observations refer to.
