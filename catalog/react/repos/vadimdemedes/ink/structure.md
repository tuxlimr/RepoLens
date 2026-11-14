# Project structure: vadimdemedes/ink

**Analysed commit:** `e93d12ec7658deefe3f3c2e1e7e52dd123297b0b`

**Commit reference:** [e93d12ec7658deefe3f3c2e1e7e52dd123297b0b](https://github.com/vadimdemedes/ink/commit/e93d12ec7658deefe3f3c2e1e7e52dd123297b0b)

**Tree at this commit:** [vadimdemedes/ink@e93d12ec7658](https://github.com/vadimdemedes/ink/tree/e93d12ec7658deefe3f3c2e1e7e52dd123297b0b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vadimdemedes/ink |
| Description | 🌈 React for interactive command-line apps |
| Stars | 40270 |
| Forks | 1062 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `e93d12ec7658deefe3f3c2e1e7e52dd123297b0b` |
| Retrieved at | 2026-11-14T19:12:59.100740+00:00 |
| Files in this snapshot | 331 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    test.yml
    windows.yml
benchmark/  (6 files)
  layout/  (1 files)
    layout.tsx
  output/  (1 files)
    output.ts
  simple/  (2 files)
    index.ts
    simple.tsx
  static/  (2 files)
    index.ts
    static.tsx
examples/  (59 files)
  alternate-screen/  (2 files)
    alternate-screen.tsx
    index.ts
  aria/  (2 files)
    aria.tsx
    index.ts
  border-backgrounds/  (2 files)
    border-backgrounds.tsx
    index.ts
  borders/  (2 files)
    borders.tsx
    index.ts
  box-backgrounds/  (2 files)
    box-backgrounds.tsx
    index.ts
  chat/  (2 files)
    chat.tsx
    index.ts
  concurrent-suspense/  (2 files)
    concurrent-suspense.tsx
    index.ts
  counter/  (2 files)
    counter.tsx
    index.ts
  cursor-ime/  (2 files)
    cursor-ime.tsx
    index.ts
  incremental-rendering/  (2 files)
    incremental-rendering.tsx
    index.ts
  jest/  (4 files)
    index.ts
    jest.tsx
    summary.tsx
    test.tsx
  justify-content/  (2 files)
    index.ts
    justify-content.tsx
  render-throttle/  (1 files)
    index.tsx
  router/  (2 files)
    index.ts
    router.tsx
  scroll/  (2 files)
    index.ts
    scroll.tsx
  select-input/  (2 files)
    index.ts
    select-input.tsx
  static/  (2 files)
    index.ts
    static.tsx
  subprocess-output/  (2 files)
    index.ts
    subprocess-output.tsx
  suspend-terminal/  (2 files)
    index.ts
    suspend-terminal.tsx
  suspense/  (2 files)
    index.ts
    suspense.tsx
  table/  (2 files)
    index.ts
    table.tsx
  terminal-resize/  (2 files)
    index.ts
    terminal-resize.tsx
  use-animation/  (2 files)
    index.ts
    use-animation.tsx
  use-focus/  (2 files)
    index.ts
    use-focus.tsx
  use-focus-with-id/  (2 files)
    index.ts
    use-focus-with-id.tsx
  use-input/  (2 files)
    index.ts
    use-input.tsx
  use-stderr/  (2 files)
    index.ts
    use-stderr.tsx
  use-stdout/  (2 files)
    index.ts
    use-stdout.tsx
  use-transition/  (2 files)
    index.ts
    use-transition.tsx
media/  (2 files)
  demo.svg
  demo.tsx
recipes/  (1 files)
  routing.md
src/  (67 files)
  components/  (19 files)
    AccessibilityContext.ts
    AnimationContext.ts
    App.tsx
    AppContext.ts
    BackgroundContext.ts
    Box.tsx
    CursorContext.ts
    ErrorBoundary.tsx
    ErrorOverview.tsx
    FocusContext.ts
    Newline.tsx
    RootNodeContext.ts
    Spacer.tsx
    Static.tsx
    StderrContext.ts
    StdinContext.ts
    StdoutContext.ts
    Text.tsx
    Transform.tsx
  hooks/  (13 files)
    use-animation.ts
    use-app.ts
    use-box-metrics.ts
    use-cursor.ts
    use-focus-manager.ts
    use-focus.ts
    use-input.ts
    use-is-screen-reader-enabled.ts
    use-paste.ts
    use-stderr.ts
    use-stdin.ts
    use-stdout.ts
    use-window-size.ts
  ansi-tokenizer.ts
  colorize.ts
  cursor-helpers.ts
  devtools-window-polyfill.ts
  devtools.ts
  dom.ts
  get-max-width.ts
  global.d.ts
  index.ts
  ink.tsx
  input-parser.ts
  instances.ts
  is-devtools-reachable.ts
  kitty-keyboard.ts
  line-update.ts
  log-update.ts
  measure-element.ts
  measure-text.ts
  output.ts
  parse-keypress.ts
  reconciler.ts
  render-background.ts
  render-border.ts
  render-node-to-output.ts
  … 11 more files
test/  (186 files)
  fixtures/  (68 files)
    alternate-screen-example.tsx
    alternate-screen-full-board-win.tsx
    aria-example.tsx
    box-width-types.tsx
    ci-debug-after-exit.tsx
    ci-debug.tsx
    ci.tsx
    clear.tsx
    console.tsx
    devtools-exit-on-unmount.tsx
    erase-with-state-change.tsx
    erase-with-static.tsx
    erase.tsx
    error source.txt
    error-long-line.txt
    exit-after-signal-exit-v4-user.tsx
    exit-double-raw-mode.tsx
    exit-normally-render-on-before-exit.tsx
    exit-normally-two-instances.tsx
    exit-normally.tsx
    exit-on-exit-with-error-value-property.tsx
    exit-on-exit-with-error.tsx
    exit-on-exit-with-result.tsx
    exit-on-exit-with-value-object.tsx
    … 44 more files
  helpers/  (10 files)
    act.ts
    create-stdin.ts
    create-stdout.ts
    force-colors.ts
    mock-timer-calls.ts
    reconstruct-terminal.ts
    render-to-string.ts
    run.ts
    term.ts
    test-renderer.ts
  absolute-truncation.tsx
  alternate-screen-example.tsx
  ansi-newlines.tsx
  ansi-tokenizer.ts
  background.tsx
  border-backgrounds.tsx
  borders.tsx
  build-output.ts
  c1-rendering.tsx
  clear-rerender.tsx
  clip-wide-background.tsx
  colon-colors.tsx
  colorize.ts
  component-regressions.tsx
  components.tsx
  content-offset.tsx
  cursor-exit-position.tsx
  cursor-helpers.tsx
  cursor.tsx
  devtools.tsx
  display.tsx
  docs.ts
  error-overview.tsx
  errors.tsx
  … 84 more files
.editorconfig
.gitattributes
.gitignore
license
package.json
readme.md
tsconfig.json
xo.config.ts
```

## Entry points

- [benchmark/simple/index.ts](https://github.com/vadimdemedes/ink/blob/e93d12ec7658deefe3f3c2e1e7e52dd123297b0b/benchmark/simple/index.ts)
- [benchmark/static/index.ts](https://github.com/vadimdemedes/ink/blob/e93d12ec7658deefe3f3c2e1e7e52dd123297b0b/benchmark/static/index.ts)
- [src/components/App.tsx](https://github.com/vadimdemedes/ink/blob/e93d12ec7658deefe3f3c2e1e7e52dd123297b0b/src/components/App.tsx)
- [src/index.ts](https://github.com/vadimdemedes/ink/blob/e93d12ec7658deefe3f3c2e1e7e52dd123297b0b/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| ansi-tokenizer.ts package | library | Observed | Groups 1 file(s) under ansi-tokenizer.ts package (observed from repository paths and static analysis). |
| benchmark package | library | Observed | Groups 6 file(s) under benchmark package (observed from repository paths and static analysis). |
| colorize.ts package | library | Observed | Groups 1 file(s) under colorize.ts package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 19 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| cursor-helpers.ts package | library | Observed | Groups 1 file(s) under cursor-helpers.ts package (observed from repository paths and static analysis). |
| devtools.ts package | library | Observed | Groups 1 file(s) under devtools.ts package (observed from repository paths and static analysis). |
| devtools-window-polyfill.ts package | library | Observed | Groups 1 file(s) under devtools-window-polyfill.ts package (observed from repository paths and static analysis). |
| dom.ts package | library | Observed | Groups 1 file(s) under dom.ts package (observed from repository paths and static analysis). |
| get-max-width.ts package | library | Observed | Groups 1 file(s) under get-max-width.ts package (observed from repository paths and static analysis). |
| global.d.ts package | library | Observed | Groups 1 file(s) under global.d.ts package (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 13 file(s) under hooks package (observed from repository paths and static analysis). |
| index.ts package | library | Observed | Groups 1 file(s) under index.ts package (observed from repository paths and static analysis). |
| ink.tsx package | library | Observed | Groups 1 file(s) under ink.tsx package (observed from repository paths and static analysis). |
| input-parser.ts package | library | Observed | Groups 1 file(s) under input-parser.ts package (observed from repository paths and static analysis). |
| instances.ts package | library | Observed | Groups 1 file(s) under instances.ts package (observed from repository paths and static analysis). |
| is-devtools-reachable.ts package | library | Observed | Groups 1 file(s) under is-devtools-reachable.ts package (observed from repository paths and static analysis). |
| kitty-keyboard.ts package | library | Observed | Groups 1 file(s) under kitty-keyboard.ts package (observed from repository paths and static analysis). |
| line-update.ts package | library | Observed | Groups 1 file(s) under line-update.ts package (observed from repository paths and static analysis). |
| log-update.ts package | library | Observed | Groups 1 file(s) under log-update.ts package (observed from repository paths and static analysis). |
| measure-element.ts package | library | Observed | Groups 1 file(s) under measure-element.ts package (observed from repository paths and static analysis). |
| measure-text.ts package | library | Observed | Groups 1 file(s) under measure-text.ts package (observed from repository paths and static analysis). |
| media package | library | Observed | Groups 1 file(s) under media package (observed from repository paths and static analysis). |
| output.ts package | library | Observed | Groups 1 file(s) under output.ts package (observed from repository paths and static analysis). |
| parse-keypress.ts package | library | Observed | Groups 1 file(s) under parse-keypress.ts package (observed from repository paths and static analysis). |
| reconciler.ts package | library | Observed | Groups 1 file(s) under reconciler.ts package (observed from repository paths and static analysis). |
| render-background.ts package | library | Observed | Groups 1 file(s) under render-background.ts package (observed from repository paths and static analysis). |
| render-border.ts package | library | Observed | Groups 1 file(s) under render-border.ts package (observed from repository paths and static analysis). |
| render-node-to-output.ts package | library | Observed | Groups 1 file(s) under render-node-to-output.ts package (observed from repository paths and static analysis). |
| render-to-string.ts package | library | Observed | Groups 1 file(s) under render-to-string.ts package (observed from repository paths and static analysis). |
| render.ts package | library | Observed | Groups 1 file(s) under render.ts package (observed from repository paths and static analysis). |
| renderer.ts package | library | Observed | Groups 1 file(s) under renderer.ts package (observed from repository paths and static analysis). |
| sanitize-ansi.ts package | library | Observed | Groups 1 file(s) under sanitize-ansi.ts package (observed from repository paths and static analysis). |
| sized-cache.ts package | library | Observed | Groups 1 file(s) under sized-cache.ts package (observed from repository paths and static analysis). |
| squash-text-nodes.ts package | library | Observed | Groups 1 file(s) under squash-text-nodes.ts package (observed from repository paths and static analysis). |
| stream.ts package | library | Observed | Groups 1 file(s) under stream.ts package (observed from repository paths and static analysis). |
| styles.ts package | library | Observed | Groups 1 file(s) under styles.ts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 186 file(s) under tests (observed from repository paths and static analysis). |
| utils.ts package | library | Observed | Groups 1 file(s) under utils.ts package (observed from repository paths and static analysis). |
| wrap-text.ts package | library | Observed | Groups 1 file(s) under wrap-text.ts package (observed from repository paths and static analysis). |
| write-synchronized.ts package | library | Observed | Groups 1 file(s) under write-synchronized.ts package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/windows.yml` (ci)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `test` — 186 analysed file(s)
- `src` — 67 analysed file(s)
- `examples` — 59 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `benchmark` — 6 analysed file(s)
- `.github` — 2 analysed file(s)
- `media` — 2 analysed file(s)
- `recipes` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e93d12ec7658deefe3f3c2e1e7e52dd123297b0b` is the revision these paths and observations refer to.
