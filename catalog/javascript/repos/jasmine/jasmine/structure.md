# Project structure: jasmine/jasmine

**Analysed commit:** `69d3743e64763daaae19f228a50c4d72862df1ba`

**Commit reference:** [69d3743e64763daaae19f228a50c4d72862df1ba](https://github.com/jasmine/jasmine/commit/69d3743e64763daaae19f228a50c4d72862df1ba)

**Tree at this commit:** [jasmine/jasmine@69d3743e6476](https://github.com/jasmine/jasmine/tree/69d3743e64763daaae19f228a50c4d72862df1ba)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | jasmine/jasmine |
| Description | Simple JavaScript testing framework for browsers and node.js |
| Stars | 15808 |
| Forks | 2239 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `69d3743e64763daaae19f228a50c4d72862df1ba` |
| Retrieved at | 2026-11-14T19:11:35.379298+00:00 |
| Files in this snapshot | 416 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
.github/  (6 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_proposal.yml
  workflows/  (2 files)
    agentscan.yml
    safari.yml
  PULL_REQUEST_TEMPLATE.md
images/  (1 files)
  jasmine-horizontal.svg
lib/  (12 files)
  jasmine-core/  (11 files)
    example/  (8 files)
      … 8 files under this directory
    boot.js
    jasmine-html.js
    jasmine.css
  jasmine-core.js
release_notes/  (96 files)
  1.3.0.md
  1.3.1.md
  2.0.1.md
  2.0.2.md
  2.1.0.md
  2.1.1.md
  2.1.2.md
  2.1.3.md
  2.2.0.md
  2.2.1.md
  2.3.0.md
  2.3.1.md
  2.3.2.md
  2.3.3.md
  2.3.4.md
  2.4.0.md
  2.4.1.md
  2.5.0.md
  2.5.1.md
  2.5.2.md
  2.6.0.md
  2.6.1.md
  2.6.2.md
  2.6.3.md
  … 72 more files
scripts/  (8 files)
  lib/  (1 files)
    buildDistribution.js
  buildDistribution.js
  buildStandaloneDist.js
  run-sauce-browsers
  runSpecsInNode.js
  runSpecsInParallel.js
  start-sauce-connect
  stop-sauce-connect
spec/  (146 files)
  core/  (114 files)
    asymmetric_equality/  (15 files)
      … 15 files under this directory
    integration/  (12 files)
      … 12 files under this directory
    matchers/  (47 files)
      … 47 files under this directory
    AsyncExpectationSpec.js
    CallTrackerSpec.js
    ClockSpec.js
    CompleteOnFirstErrorSkipPolicySpec.js
    ConfigurationSpec.js
    DelayedFunctionSchedulerSpec.js
    DeprecatorSpec.js
    EnvSpec.js
    ExceptionFormatterSpec.js
    ExceptionsSpec.js
    ExpectationFilterChainSpec.js
    ExpectationSpec.js
    GlobalErrorsSpec.js
    MockDateSpec.js
    ParallelReportDispatcherSpec.js
    PrettyPrintSpec.js
    QueueRunnerSpec.js
    ReportDispatcherSpec.js
    RunableResourcesSpec.js
    RunnerSpec.js
    SkipAfterBeforeAllErrorPolicySpec.js
    SpecSpec.js
    SpyRegistrySpec.js
    SpySpec.js
    … 16 more files
  fixtures/  (1 files)
    reset.js
  helpers/  (10 files)
    BrowserFlags.js
    callerFilenameShim.js
    defineJasmineUnderTest.js
    domHelpers.js
    environments.js
    init.js
    integrationMatchers.js
    monkeyPatchingSpecs.js
    nodeDefineJasmineUnderTest.js
    resetEnv.js
  html/  (9 files)
    HtmlReporterV2Spec.js
    HtmlReporterV2UrlsSpec.js
    HtmlSpecFilterV2Spec.js
    PerformanceViewSpec.js
    PrettyPrintHtmlSpec.js
    QueryStringSpec.js
    ResultsNodeSpec.js
    SpyRegistryHtmlSpec.js
    TabBarSpec.js
  javascripts/  (1 files)
    support/  (1 files)
      … 1 files under this directory
  npmPackage/  (2 files)
    npmPackageSpec.js
    resetSpec.js
  performance/  (2 files)
    large_object_test.js
    performance_test.js
  support/  (7 files)
    ci.js
    jasmine-browser-performance.json
    jasmine-browser.js
    jasmine-performance.json
    jasmine-performance.yml
    jasmine.json
    localJasmineBrowser.js
src/  (135 files)
  boot/  (2 files)
    boot.js
    jasmine-core.js
  core/  (110 files)
    asymmetric_equality/  (15 files)
      … 15 files under this directory
    matchers/  (49 files)
      … 49 files under this directory
    CallTracker.js
    Clock.js
    CompleteOnFirstErrorSkipPolicy.js
    Configuration.js
    CurrentRunableTracker.js
    DelayedFunctionScheduler.js
    Deprecator.js
    Env.js
    ExceptionFormatter.js
    Expectation.js
    ExpectationFilterChain.js
    Expector.js
    GlobalErrors.js
    MockDate.js
    NeverSkipPolicy.js
    Order.js
    ParallelReportDispatcher.js
    PrettyPrinter.js
    QueueRunner.js
    ReportDispatcher.js
    RunableResources.js
    Runner.js
    SkipAfterBeforeAllErrorPolicy.js
    Spec.js
    … 22 more files
  html/  (18 files)
    AlertsView.js
    Banner.js
    FailuresView.js
    HtmlReporterV2.js
    HtmlReporterV2Urls.js
    HtmlSpecFilterv2.js
    OverallStatusBar.js
    PerformanceView.js
    QueryString.js
    ResultsNode.js
    ResultsStateBuilder.js
    SummaryTreeView.js
    TabBar.js
    _HTMLReporter.scss
    htmlReporterUtils.js
    jasmine.scss
    requireHtml.js
    requireSuffix.js
  templates/  (2 files)
    example_project_jasmine_tags.html.erb
    version.js.erb
  SpecRunner.html.ejs
  licenseBanner.js.ejs
  version.js
.editorconfig
.gitattributes
.gitignore
.prettierrc
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
RELEASE.md
eslint.config.mjs
package.json
```

## Entry points

- [lib/jasmine-core.js](https://github.com/jasmine/jasmine/blob/69d3743e64763daaae19f228a50c4d72862df1ba/lib/jasmine-core.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| boot package | library | Observed | Groups 2 file(s) under boot package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 12 file(s) under external integrations (observed from repository paths and static analysis). |
| html package | library | Observed | Groups 16 file(s) under html package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 11 file(s) under lib package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 212 file(s) under service / domain layer (observed from repository paths and static analysis). |
| spec package | library | Observed | Groups 27 file(s) under spec package (observed from repository paths and static analysis). |
| version.js package | library | Observed | Groups 1 file(s) under version.js package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_proposal.yml` (config)
- `.github/workflows/agentscan.yml` (ci)
- `.github/workflows/safari.yml` (ci)
- `package.json` (manifest)
- `spec/javascripts/support/jasmine_selenium_runner.yml` (config)
- `spec/support/jasmine-browser-performance.json` (config)
- `spec/support/jasmine-performance.json` (config)
- `spec/support/jasmine-performance.yml` (config)
- `spec/support/jasmine.json` (config)

## Top-level layout

- `spec` — 146 analysed file(s)
- `src` — 135 analysed file(s)
- `release_notes` — 96 analysed file(s)
- `lib` — 12 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `scripts` — 8 analysed file(s)
- `.github` — 6 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `images` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `69d3743e64763daaae19f228a50c4d72862df1ba` is the revision these paths and observations refer to.
