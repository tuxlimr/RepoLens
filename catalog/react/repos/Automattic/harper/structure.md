# Project structure: Automattic/harper

**Analysed commit:** `4270327e92ecdfd25a8da4fdeb51f6998d5d5443`

**Commit reference:** [4270327e92ecdfd25a8da4fdeb51f6998d5d5443](https://github.com/Automattic/harper/commit/4270327e92ecdfd25a8da4fdeb51f6998d5d5443)

**Tree at this commit:** [Automattic/harper@4270327e92ec](https://github.com/Automattic/harper/tree/4270327e92ecdfd25a8da4fdeb51f6998d5d5443)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Automattic/harper |
| Description | Offline, privacy-first grammar checker. Fast, open-source, Rust-powered |
| Stars | 17706 |
| Forks | 832 |
| Licence | Apache-2.0 |
| Language | Rust |
| Default branch | master |
| Analysed commit | `4270327e92ecdfd25a8da4fdeb51f6998d5d5443` |
| Retrieved at | 2026-11-14T19:13:15.454130+00:00 |
| Files in this snapshot | 798 |

## Directory tree

```text
.buildkite/  (9 files)
  commands/  (7 files)
    build-desktop-windows.ps1
    build-desktop.sh
    release-desktop-windows.sh
    sign-windows.cjs
    sign-windows.test.cjs
    upload-release.cjs
    upload-release.test.cjs
  pipeline.yml
  shared-pipeline-vars
.bundle/  (1 files)
  config
.github/  (16 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.md
    report-false-negative.md
    report-false-positive.md
    report-grammatical-error.md
    suggest-a-feature.md
  scripts/  (1 files)
    apt-install.sh
  workflows/  (8 files)
    binaries.yml
    build_web.yml
    chrome_plugin.yml
    desktop_windows.yml
    just_checks.yml
    stale.yml
    vscode_plugin.yml
    wp_plugin.yml
  dependabot.yml
  pull_request_template.md
.vscode/  (1 files)
  extensions.json
fastlane/  (2 files)
  Fastfile
  Matchfile
fuzz/  (8 files)
  fuzz_targets/  (5 files)
    fuzz_harper_comment.rs
    fuzz_harper_core_markdown.rs
    fuzz_harper_html.rs
    fuzz_harper_literate_haskell.rs
    fuzz_harper_typst.rs
  .gitignore
  Cargo.toml
  README.md
harper-asciidoc/  (7 files)
  src/  (1 files)
    lib.rs
  tests/  (5 files)
    test_sources/  (4 files)
      … 4 files under this directory
    asciidoc_tests.rs
  Cargo.toml
harper-brill/  (3 files)
  src/  (1 files)
    lib.rs
  Cargo.toml
  trained_chunker_model.json
harper-cli/  (12 files)
  src/  (8 files)
    input/  (2 files)
      … 2 files under this directory
    annotate.rs
    input.rs
    lint.rs
    lint_engine.rs
    lint_reporter.rs
    main.rs
  tests/  (2 files)
    no_color.rs
    output_format.rs
  Cargo.toml
  README.md
harper-comments/  (58 files)
  src/  (10 files)
    comment_parsers/  (7 files)
      … 7 files under this directory
    comment_parser.rs
    lib.rs
    masker.rs
  tests/  (46 files)
    language_support_sources/  (45 files)
      … 45 files under this directory
    language_support.rs
  Cargo.toml
  README.md
harper-core/  (655 files)
  benches/  (6 files)
    misspelled_words/  (3 files)
      … 3 files under this directory
    essay.md
    parse_essay.rs
    spellcheck.rs
  examples/  (1 files)
    alloc_profile.rs
  src/  (637 files)
    dict_word_metadata/  (1 files)
      … 1 files under this directory
    expr/  (24 files)
      … 24 files under this directory
    ignored_lints/  (2 files)
      … 2 files under this directory
    lexing/  (4 files)
      … 4 files under this directory
    linting/  (592 files)
      … 592 files under this directory
    case.rs
    char_ext.rs
    char_string.rs
    currency.rs
    dict_word_metadata.rs
    dict_word_metadata_orthography.rs
    document.rs
    edit_distance.rs
    fat_token.rs
    indefinite_article.rs
    irregular_nouns.rs
    irregular_verbs.rs
    language_detection.rs
    lib.rs
  Cargo.toml
  README.md
  annotations.json
  build.rs
  clippy.toml
  default_config.json
  expr_linter_skeleton.rs
  expr_linter_skeleton_commented.rs
  irregular_nouns.json
  irregular_verbs.json
  proper_noun_rules.json
.dockerignore
.editorconfig
.envrc
.gitattributes
.gitignore
.node-version
.nvmrc
.ruby-version
.xcode-version
AGENTS.md
AGENT_POLICY.md
ARCHITECTURE.md
COMPARISON.md
CONTRIBUTING.md
Cargo.toml
Dockerfile
Gemfile
Gemfile.lock
LICENSE
README.md
biome.json
demo.md
docker-compose.dev.yml
docker-compose.yml
… 2 more files
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 18 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| fuzz package | library | Observed | Groups 5 file(s) under fuzz package (observed from repository paths and static analysis). |
| harper-asciidoc package | library | Observed | Groups 1 file(s) under harper-asciidoc package (observed from repository paths and static analysis). |
| harper-brill package | library | Observed | Groups 1 file(s) under harper-brill package (observed from repository paths and static analysis). |
| harper-cli package | library | Observed | Groups 8 file(s) under harper-cli package (observed from repository paths and static analysis). |
| harper-comments package | library | Observed | Groups 10 file(s) under harper-comments package (observed from repository paths and static analysis). |
| harper-core package | library | Observed | Groups 459 file(s) under harper-core package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 53 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.buildkite/pipeline.yml` (config)
- `.dockerignore` (container)
- `.editorconfig` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/binaries.yml` (ci)
- `.github/workflows/build_web.yml` (ci)
- `.github/workflows/chrome_plugin.yml` (ci)
- `.github/workflows/desktop_windows.yml` (ci)
- `.github/workflows/just_checks.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.github/workflows/vscode_plugin.yml` (ci)
- `.github/workflows/wp_plugin.yml` (ci)
- `.vscode/extensions.json` (config)
- `Cargo.toml` (manifest)
- `Dockerfile` (container)
- `biome.json` (config)
- `docker-compose.dev.yml` (config)
- `docker-compose.yml` (container)
- `fuzz/Cargo.toml` (manifest)
- `harper-asciidoc/Cargo.toml` (manifest)
- `harper-brill/Cargo.toml` (manifest)
- `harper-brill/trained_chunker_model.json` (config)
- `harper-cli/Cargo.toml` (manifest)
- `harper-comments/Cargo.toml` (manifest)
- `harper-core/Cargo.toml` (manifest)
- `harper-core/annotations.json` (config)
- `harper-core/clippy.toml` (config)
- `harper-core/default_config.json` (config)
- `harper-core/irregular_nouns.json` (config)
- `harper-core/irregular_verbs.json` (config)
- `harper-core/proper_noun_rules.json` (config)

## Top-level layout

- `harper-core` — 655 analysed file(s)
- `harper-comments` — 58 analysed file(s)
- `(root files)` — 26 analysed file(s)
- `.github` — 16 analysed file(s)
- `harper-cli` — 12 analysed file(s)
- `.buildkite` — 9 analysed file(s)
- `fuzz` — 8 analysed file(s)
- `harper-asciidoc` — 7 analysed file(s)
- `harper-brill` — 3 analysed file(s)
- `fastlane` — 2 analysed file(s)
- `.bundle` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `4270327e92ecdfd25a8da4fdeb51f6998d5d5443` is the revision these paths and observations refer to.
