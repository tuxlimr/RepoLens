# Project structure: defunkt/jquery-pjax

**Analysed commit:** `153262eda33e31119eabb97cd5f14365580a3b35`

**Commit reference:** [153262eda33e31119eabb97cd5f14365580a3b35](https://github.com/defunkt/jquery-pjax/commit/153262eda33e31119eabb97cd5f14365580a3b35)

**Tree at this commit:** [defunkt/jquery-pjax@153262eda33e](https://github.com/defunkt/jquery-pjax/tree/153262eda33e31119eabb97cd5f14365580a3b35)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | defunkt/jquery-pjax |
| Description | pushState + ajax = pjax |
| Stars | 16622 |
| Forks | 1914 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `153262eda33e31119eabb97cd5f14365580a3b35` |
| Retrieved at | 2026-11-14T19:11:31.520093+00:00 |
| Files in this snapshot | 39 |

## Directory tree

```text
script/  (3 files)
  bootstrap
  server
  test
test/  (25 files)
  unit/  (4 files)
    fn_pjax.js
    helpers.js
    pjax.js
    pjax_fallback.js
  views/  (18 files)
    aliens.erb
    anchor.erb
    boom.erb
    boom_sans_pjax.erb
    dinosaurs.erb
    double_title.erb
    empty.erb
    env.erb
    fragment.erb
    hello.erb
    home.erb
    layout.erb
    long.erb
    nested_title.erb
    qunit.erb
    referer.erb
    scripts.erb
    timeout.erb
  app.rb
  evaled.js
  run-qunit.js
.eslintrc
.gitignore
.travis.yml
CONTRIBUTING.md
Gemfile
Gemfile.lock
LICENSE
README.md
bower.json
jquery.pjax.js
package.json
```

## Entry points

- [jquery.pjax.js](https://github.com/defunkt/jquery-pjax/blob/153262eda33e31119eabb97cd5f14365580a3b35/jquery.pjax.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 26 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `bower.json` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 25 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `script` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `153262eda33e31119eabb97cd5f14365580a3b35` is the revision these paths and observations refer to.
