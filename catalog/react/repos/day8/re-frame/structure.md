# Project structure: day8/re-frame

**Analysed commit:** `1a1bf1df6570b17a148ebce70d500ec2da393cdc`

**Commit reference:** [1a1bf1df6570b17a148ebce70d500ec2da393cdc](https://github.com/day8/re-frame/commit/1a1bf1df6570b17a148ebce70d500ec2da393cdc)

**Tree at this commit:** [day8/re-frame@1a1bf1df6570](https://github.com/day8/re-frame/tree/1a1bf1df6570b17a148ebce70d500ec2da393cdc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | day8/re-frame |
| Description | A ClojureScript framework for building user interfaces, leveraging React |
| Stars | 5545 |
| Forks | 709 |
| Licence | MIT |
| Language | Clojure |
| Default branch | master |
| Analysed commit | `1a1bf1df6570b17a148ebce70d500ec2da393cdc` |
| Retrieved at | 2026-11-14T19:14:17.120482+00:00 |
| Files in this snapshot | 205 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    Bug-Report.yml
    New-Feature.yml
    config.yml
  workflows/  (3 files)
    continuous-deployment-workflow.yml
    continuous-integration-workflow.yml
    docs-workflow.yml
  FUNDING.yml
docs/  (97 files)
  EPs/  (6 files)
    001-CaptureHandlerMetadata.md
    002-ReframeInstances.md
    003-ReusableComponents.md
    004-ViewRegistration.md
    005-StateMachines.md
    README.md
  FAQs/  (20 files)
    BestPractice.md
    DB_Normalisation.md
    DoINeedReFrame.md
    FocusOnElement.md
    FullStackReframe.md
    GlobalInterceptors.md
    Inspecting-app-db.md
    LoadOnMount.md
    Logging.md
    Null-Dispatched-Events.md
    PollADatabaseEvery60.md
    UseASubscriptionInAnEventHandler.md
    ViewsOnGlobalRegistration.md
    When-Does-Dispatch-Happen.md
    Why-CLJC.md
    Why-Clear-Sub-Cache.md
    alpha.md
    laggy-input.md
    use-cofx-as-fx.md
    why-didnt-my-component-update.md
  images/  (3 files)
    logo/  (3 files)
      … 3 files under this directory
  releases/  (11 files)
    2015.md
    2016.md
    2017.md
    2018.md
    2019.md
    2020.md
    2021.md
    2022.md
    2023.md
    2024.md
    2026.md
  src/  (2 files)
    re_frame/  (1 files)
      … 1 files under this directory
    ns_to_markdown.clj
  styles/  (1 files)
    website.css
  stylesheets/  (2 files)
    dominoes-live.css
    mkdocs.css
  theme/  (4 files)
    overrides/  (2 files)
      … 2 files under this directory
    404.html
    main.html
  App-Structure.md
  Coeffects.md
  Debugging.md
  EffectfulHandlers.md
  Effects.md
  External-Resources.md
  Flows.md
  Interceptors.md
  Loading-Initial-Data.md
  Performance-Problems.md
  README.md
  Solve-the-CPU-hog-problem.md
  Subscribing-To-External-Data.md
  Talking-To-Servers.md
  Testing.md
  The-re-frame-logo.md
  Using-Stateful-JS-Components.md
  a-loop.md
  all-models-are-wrong.md
  api-builtin-effects.md
  api-intro.md
  api-re-frame.alpha-instrumented.md
  api-re-frame.core-instrumented.md
  api-re-frame.tooling.md
  … 24 more files
examples/  (26 files)
  flow/  (6 files)
    resources/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    deps.edn
    package.json
    shadow-cljs.edn
  simple/  (8 files)
    resources/  (2 files)
      … 2 files under this directory
    src/  (1 files)
      … 1 files under this directory
    .gitignore
    README.md
    deps.edn
    package.json
    shadow-cljs.edn
  todomvc/  (12 files)
    resources/  (2 files)
      … 2 files under this directory
    src/  (5 files)
      … 5 files under this directory
    .gitignore
    README.md
    deps.edn
    package.json
    shadow-cljs.edn
src/  (27 files)
  re_frame/  (26 files)
    flow/  (1 files)
      … 1 files under this directory
    query/  (1 files)
      … 1 files under this directory
    register/  (1 files)
      … 1 files under this directory
    subs/  (1 files)
      … 1 files under this directory
    alpha.cljc
    alpha_instrumented.cljc
    cofx.cljc
    config.cljc
    core.cljc
    core_instrumented.cljc
    db.cljc
    events.cljc
    fx.cljc
    instrumented_macros.clj
    interceptor.cljc
    interop.clj
    interop.cljs
    loggers.cljc
    registrar.cljc
    router.cljc
    settings.cljc
    std_interceptors.cljc
    subs.cljc
    tooling.cljc
    trace.cljc
    utils.cljc
  deps.cljs
test/  (35 files)
  re_frame/  (34 files)
    flow/  (1 files)
      … 1 files under this directory
    subs/  (1 files)
      … 1 files under this directory
    alpha_handler_source_meta_test.clj
    alpha_instrumented_standalone_require_test.clj
    core_instrumented_standalone_require_test.clj
    dispatch_source_meta_test.clj
    dispatch_source_meta_test.cljs
    dispatch_with_test.clj
    event_test.cljs
    fx_test.cljs
    handler_source_meta_test.clj
    handler_source_meta_test.cljs
    interceptor_test.cljs
    interop_test.clj
    live_query_vs_test.clj
    query_v_for_reaction_test.clj
    query_v_for_reaction_test.cljs
    reagent_id_test.clj
    registrar_test.clj
    registrar_test.cljs
    restore_test.cljs
    router_test.clj
    subs_test.clj
    subs_test.cljs
    subscribe_source_meta_test.clj
    subscribe_source_meta_test.cljs
    … 8 more files
  test.html
.editorconfig
.gitattributes
.gitignore
CHANGELOG.md
CITATION.md
CONTRIBUTING.md
README.md
SUPPORT.md
bb.edn
deps.edn
license.txt
mkdocs.yml
shadow-cljs.edn
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 35 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/Bug-Report.yml` (config)
- `.github/ISSUE_TEMPLATE/New-Feature.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/continuous-deployment-workflow.yml` (ci)
- `.github/workflows/continuous-integration-workflow.yml` (ci)
- `.github/workflows/docs-workflow.yml` (ci)
- `examples/flow/package.json` (manifest)
- `examples/simple/package.json` (manifest)
- `examples/todomvc/package.json` (manifest)
- `mkdocs.yml` (config)

## Top-level layout

- `docs` — 97 analysed file(s)
- `test` — 35 analysed file(s)
- `src` — 27 analysed file(s)
- `examples` — 26 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 7 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (3 x lockfile excluded; 3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `1a1bf1df6570b17a148ebce70d500ec2da393cdc` is the revision these paths and observations refer to.
