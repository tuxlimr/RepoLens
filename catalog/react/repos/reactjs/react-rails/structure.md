# Project structure: reactjs/react-rails

**Analysed commit:** `e48a3263d6a79e544d7af92df4ebd86e5f27e213`

**Commit reference:** [e48a3263d6a79e544d7af92df4ebd86e5f27e213](https://github.com/reactjs/react-rails/commit/e48a3263d6a79e544d7af92df4ebd86e5f27e213)

**Tree at this commit:** [reactjs/react-rails@e48a3263d6a7](https://github.com/reactjs/react-rails/tree/e48a3263d6a79e544d7af92df4ebd86e5f27e213)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | reactjs/react-rails |
| Description | Integrate React.js with Rails views and controllers, the asset pipeline, or webpacker. |
| Stars | 6776 |
| Forks | 737 |
| Licence | Apache-2.0 |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `e48a3263d6a79e544d7af92df4ebd86e5f27e213` |
| Retrieved at | 2026-11-14T19:14:01.557260+00:00 |
| Files in this snapshot | 252 |

## Directory tree

```text
.github/  (6 files)
  workflows/  (4 files)
    claude-code-review.yml
    claude.yml
    rubocop.yml
    ruby.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
docs/  (9 files)
  common-errors.md
  component-generator.md
  controller-actions.md
  get-started.md
  migrating-from-react-rails-to-react_on_rails.md
  server-side-rendering.md
  ujs.md
  upgrading.md
  view-helper.md
gemfiles/  (12 files)
  base.gemfile
  base.gemfile.lock
  connection_pool_3.gemfile
  connection_pool_3.gemfile.lock
  propshaft.gemfile
  propshaft.gemfile.lock
  shakapacker.gemfile
  shakapacker.gemfile.lock
  sprockets_3.gemfile
  sprockets_3.gemfile.lock
  sprockets_4.gemfile
  sprockets_4.gemfile.lock
lib/  (43 files)
  assets/  (3 files)
    javascripts/  (1 files)
      … 1 files under this directory
    react-source/  (2 files)
      … 2 files under this directory
  generators/  (11 files)
    react/  (2 files)
      … 2 files under this directory
    templates/  (9 files)
      … 9 files under this directory
  react/  (27 files)
    jsx/  (5 files)
      … 5 files under this directory
    rails/  (8 files)
      … 8 files under this directory
    server_rendering/  (11 files)
      … 11 files under this directory
    jsx.rb
    rails.rb
    server_rendering.rb
  react-rails.rb
  react.rb
rakelib/  (1 files)
  create_release.rake
react-builds/  (4 files)
  package.json
  react-browser.js
  react-server.js
  webpack.config.js
react_ujs/  (16 files)
  src/  (13 files)
    events/  (6 files)
      … 6 files under this directory
    getConstructor/  (4 files)
      … 4 files under this directory
    reactDomClient.js
    renderHelpers.js
    supportsRootApi.js
  index.js
  readme.md
  webpack.config.js
test/  (138 files)
  bin/  (1 files)
    create-fake-js-package-managers
  dummy/  (99 files)
    app/  (56 files)
      … 56 files under this directory
    bin/  (6 files)
      … 6 files under this directory
    config/  (25 files)
      … 25 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    log/  (1 files)
      … 1 files under this directory
    public/  (3 files)
      … 3 files under this directory
    .gitignore
    .postcssrc.yml
    README.rdoc
    Rakefile
    babel.config.js
    config.ru
    package.json
  generators/  (6 files)
    coffee_component_generator_test.rb
    component_generator_test.rb
    es6_component_generator_test.rb
    install_generator_sprockets_test.rb
    install_generator_webpacker_test.rb
    ts_es6_component_generator_test.rb
  helper_files/  (3 files)
    TodoListWithUpdates.js
    TodoListWithUpdates.js.jsx
    WithoutSprockets.js
  react/  (22 files)
    jsx/  (2 files)
      … 2 files under this directory
    rails/  (11 files)
      … 11 files under this directory
    server_rendering/  (7 files)
      … 7 files under this directory
    jsx_test.rb
    server_rendering_test.rb
  support/  (3 files)
    propshaft_helpers.rb
    sprockets_helpers.rb
    webpacker_helpers.rb
  react_asset_test.rb
  react_test.rb
  server_rendered_html_test.rb
  test_helper.rb
.bowerrc
.codeclimate.yml
.gitignore
.pryrc
.rubocop.yml
.rubocop_todo.yml
Appraisals
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Gemfile
Gemfile.lock
Guardfile
LICENSE
LintingGemfile
LintingGemfile.lock
README.md
Rakefile
SECURITY.md
VERSIONS.md
check_for_uncommitted_files.sh
package.json
react-rails.gemspec
```

## Entry points

- [react_ujs/index.js](https://github.com/reactjs/react-rails/blob/e48a3263d6a79e544d7af92df4ebd86e5f27e213/react_ujs/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 40 file(s) under lib package (observed from repository paths and static analysis). |
| react-builds package | library | Observed | Groups 3 file(s) under react-builds package (observed from repository paths and static analysis). |
| react_ujs package | library | Observed | Groups 15 file(s) under react_ujs package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 139 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.codeclimate.yml` (config)
- `.github/workflows/claude-code-review.yml` (ci)
- `.github/workflows/claude.yml` (ci)
- `.github/workflows/rubocop.yml` (ci)
- `.github/workflows/ruby.yml` (ci)
- `.rubocop.yml` (config)
- `.rubocop_todo.yml` (config)
- `package.json` (manifest)
- `react-builds/package.json` (manifest)

## Top-level layout

- `test` — 138 analysed file(s)
- `lib` — 43 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `react_ujs` — 16 analysed file(s)
- `gemfiles` — 12 analysed file(s)
- `docs` — 9 analysed file(s)
- `.github` — 6 analysed file(s)
- `react-builds` — 4 analysed file(s)
- `rakelib` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 6 file(s) were skipped during inventory (2 x lockfile excluded; 4 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e48a3263d6a79e544d7af92df4ebd86e5f27e213` is the revision these paths and observations refer to.
