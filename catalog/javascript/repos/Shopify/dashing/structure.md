# Project structure: Shopify/dashing

**Analysed commit:** `bc1c106e42d52d3bfc042cba7bb0181d09413068`

**Commit reference:** [bc1c106e42d52d3bfc042cba7bb0181d09413068](https://github.com/Shopify/dashing/commit/bc1c106e42d52d3bfc042cba7bb0181d09413068)

**Tree at this commit:** [Shopify/dashing@bc1c106e42d5](https://github.com/Shopify/dashing/tree/bc1c106e42d52d3bfc042cba7bb0181d09413068)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Shopify/dashing |
| Description | The exceptionally handsome dashboard framework in Ruby and Coffeescript. |
| Stars | 10893 |
| Forks | 1143 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `bc1c106e42d52d3bfc042cba7bb0181d09413068` |
| Retrieved at | 2026-11-14T19:12:29.184491+00:00 |
| Files in this snapshot | 73 |

## Directory tree

```text
bin/  (1 files)
  dashing
javascripts/  (4 files)
  batman.jquery.js
  dashing.coffee
  es5-shim.js
  jquery.js
lib/  (4 files)
  dashing/  (3 files)
    app.rb
    cli.rb
    downloader.rb
  dashing.rb
templates/  (51 files)
  dashboard/  (1 files)
    %name%.erb.tt
  job/  (1 files)
    %name%.rb
  project/  (46 files)
    assets/  (6 files)
      … 6 files under this directory
    dashboards/  (3 files)
      … 3 files under this directory
    jobs/  (4 files)
      … 4 files under this directory
    lib/  (1 files)
      … 1 files under this directory
    public/  (1 files)
      … 1 files under this directory
    widgets/  (27 files)
      … 27 files under this directory
    .gitignore
    Gemfile
    README.md
    config.ru
  widget/  (3 files)
    %name%/  (3 files)
      … 3 files under this directory
test/  (4 files)
  app_test.rb
  cli_test.rb
  downloader_test.rb
  test_helper.rb
.gitignore
.travis.yml
CONTRIBUTING.md
Gemfile
MIT-LICENSE
README.md
Rakefile
dashing.gemspec
shipit.rubygems.yml
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| javascripts package | library | Observed | Groups 3 file(s) under javascripts package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 4 file(s) under lib package (observed from repository paths and static analysis). |
| templates package | library | Observed | Groups 7 file(s) under templates package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `shipit.rubygems.yml` (config)

## Top-level layout

- `templates` — 51 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `javascripts` — 4 analysed file(s)
- `lib` — 4 analysed file(s)
- `test` — 4 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x generated/minified file excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `bc1c106e42d52d3bfc042cba7bb0181d09413068` is the revision these paths and observations refer to.
