# Project structure: gulpjs/gulp

**Analysed commit:** `61f22dc11bb14234b555253095fa1d224ce0eab1`

**Commit reference:** [61f22dc11bb14234b555253095fa1d224ce0eab1](https://github.com/gulpjs/gulp/commit/61f22dc11bb14234b555253095fa1d224ce0eab1)

**Tree at this commit:** [gulpjs/gulp@61f22dc11bb1](https://github.com/gulpjs/gulp/tree/61f22dc11bb14234b555253095fa1d224ce0eab1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | gulpjs/gulp |
| Description | A toolkit to automate & enhance your workflow |
| Stars | 32915 |
| Forks | 4124 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `61f22dc11bb14234b555253095fa1d224ce0eab1` |
| Retrieved at | 2026-11-14T19:10:44.696112+00:00 |
| Files in this snapshot | 93 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    dev.yml
    release.yml
  SECURITY.md
bin/  (1 files)
  gulp.js
docs/  (63 files)
  advanced/  (1 files)
    creating-custom-registries.md
  api/  (15 files)
    README.md
    concepts.md
    dest.md
    last-run.md
    parallel.md
    registry.md
    series.md
    src.md
    symlink.md
    task.md
    tree.md
    vinyl-iscustomprop.md
    vinyl-isvinyl.md
    vinyl.md
    watch.md
  getting-started/  (9 files)
    1-quick-start.md
    2-javascript-and-gulpfiles.md
    3-creating-tasks.md
    4-async-completion.md
    5-working-with-files.md
    6-explaining-globs.md
    7-using-plugins.md
    8-watching-files.md
    README.md
  recipes/  (25 files)
    README.md
    automate-releases.md
    browserify-multiple-destination.md
    browserify-transforms.md
    browserify-uglify-sourcemap.md
    browserify-with-globs.md
    combining-streams-to-handle-errors.md
    cron-task.md
    delete-files-folder.md
    fast-browserify-builds-with-watchify.md
    handling-the-delete-event-on-watch.md
    incremental-builds-with-concatenate.md
    maintain-directory-structure-while-globbing.md
    make-stream-from-buffer.md
    minified-and-non-minified.md
    minimal-browsersync-setup-with-gulp4.md
    mocha-test-runner-with-gulp.md
    pass-arguments-from-cli.md
    rollup-with-rollup-stream.md
    run-grunt-tasks-from-gulp.md
    running-task-steps-per-folder.md
    server-with-livereload-and-css-injection.md
    sharing-streams-with-stream-factories.md
    templating-with-swig-and-yaml-front-matter.md
    … 1 more files
  support/  (1 files)
    for-enterprise.md
  why-use-pump/  (1 files)
    README.md
  writing-a-plugin/  (6 files)
    README.md
    dealing-with-streams.md
    guidelines.md
    recommended-modules.md
    testing.md
    using-buffers.md
  CLI.md
  FAQ.md
  README.md
  documentation-missing.md
  getting-started.md
test/  (12 files)
  fixtures/  (7 files)
    copy/  (1 files)
      … 1 files under this directory
    gulpfiles/  (2 files)
      … 2 files under this directory
    stuff/  (2 files)
      … 2 files under this directory
    test/  (1 files)
      … 1 files under this directory
    test.coffee
  .gitkeep
  dest.js
  index.test.js
  src.js
  watch.js
.editorconfig
.eslintrc
.gitattributes
.gitignore
.prettierignore
.tidelift.yml
CHANGELOG.md
CONTRIBUTING.md
EXPENSE_POLICY.md
LICENSE
README.md
index.js
index.mjs
package.json
```

## Entry points

- [index.js](https://github.com/gulpjs/gulp/blob/61f22dc11bb14234b555253095fa1d224ce0eab1/index.js)
- [bin/gulp.js](https://github.com/gulpjs/gulp/blob/61f22dc11bb14234b555253095fa1d224ce0eab1/bin/gulp.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 12 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/workflows/dev.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.tidelift.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `docs` — 63 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `test` — 12 analysed file(s)
- `.github` — 3 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `61f22dc11bb14234b555253095fa1d224ce0eab1` is the revision these paths and observations refer to.
