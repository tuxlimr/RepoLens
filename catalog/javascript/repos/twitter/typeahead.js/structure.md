# Project structure: twitter/typeahead.js

**Analysed commit:** `588440f66559714280628a4f9799f0c4eb880a4a`

**Commit reference:** [588440f66559714280628a4f9799f0c4eb880a4a](https://github.com/twitter/typeahead.js/commit/588440f66559714280628a4f9799f0c4eb880a4a)

**Tree at this commit:** [twitter/typeahead.js@588440f66559](https://github.com/twitter/typeahead.js/tree/588440f66559714280628a4f9799f0c4eb880a4a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | twitter/typeahead.js |
| Description | typeahead.js is a fast and fully-featured autocomplete library |
| Stars | 16410 |
| Forks | 3089 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `588440f66559714280628a4f9799f0c4eb880a4a` |
| Retrieved at | 2026-11-14T19:11:32.548127+00:00 |
| Files in this snapshot | 63 |

## Directory tree

```text
doc/  (3 files)
  migration/  (1 files)
    0.10.0.md
  bloodhound.md
  jquery_typeahead.md
src/  (21 files)
  bloodhound/  (10 files)
    bloodhound.js
    lru_cache.js
    options_parser.js
    persistent_storage.js
    prefetch.js
    remote.js
    search_index.js
    tokenizers.js
    transport.js
    version.js
  common/  (1 files)
    utils.js
  typeahead/  (10 files)
    dataset.js
    default_menu.js
    event_bus.js
    event_emitter.js
    highlight.js
    input.js
    menu.js
    plugin.js
    typeahead.js
    www.js
test/  (26 files)
  bloodhound/  (9 files)
    bloodhound_spec.js
    lru_cache_spec.js
    options_parser_spec.js
    persistent_storage_spec.js
    prefetch_spec.js
    remote_spec.js
    search_index_spec.js
    tokenizers_spec.js
    transport_spec.js
  fixtures/  (3 files)
    ajax_responses.js
    data.js
    html.js
  helpers/  (1 files)
    typeahead_mocks.js
  integration/  (2 files)
    test.html
    test.js
  typeahead/  (9 files)
    dataset_spec.js
    default_results_spec.js
    event_bus_spec.js
    event_emitter_spec.js
    highlight_spec.js
    input_spec.js
    plugin_spec.js
    results_spec.js
    typeahead_spec.js
  ci
  playground.html
.gitignore
.jshintrc
.travis.yml
CHANGELOG.md
CONTRIBUTING.md
Gruntfile.js
LICENSE
README.md
bower.json
composer.json
karma.conf.js
package.json
typeahead.js.jquery.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bloodhound package | library | Observed | Groups 10 file(s) under bloodhound package (observed from repository paths and static analysis). |
| common package | library | Observed | Groups 1 file(s) under common package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 26 file(s) under tests (observed from repository paths and static analysis). |
| typeahead package | library | Observed | Groups 10 file(s) under typeahead package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `bower.json` (config)
- `composer.json` (config)
- `package.json` (manifest)
- `typeahead.js.jquery.json` (config)

## Top-level layout

- `test` — 26 analysed file(s)
- `src` — 21 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `doc` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 3 file(s) were skipped during inventory (3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `588440f66559714280628a4f9799f0c4eb880a4a` is the revision these paths and observations refer to.
