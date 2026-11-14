# Project structure: JacksonTian/fks

**Analysed commit:** `54722627d64b3b8918f4f4cf73752d3675dae99e`

**Commit reference:** [54722627d64b3b8918f4f4cf73752d3675dae99e](https://github.com/JacksonTian/fks/commit/54722627d64b3b8918f4f4cf73752d3675dae99e)

**Tree at this commit:** [JacksonTian/fks@54722627d64b](https://github.com/JacksonTian/fks/tree/54722627d64b3b8918f4f4cf73752d3675dae99e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | JacksonTian/fks |
| Description | 前端技能汇总 Frontend Knowledge Structure |
| Stars | 17900 |
| Forks | 4474 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `54722627d64b3b8918f4f4cf73752d3675dae99e` |
| Retrieved at | 2026-11-14T19:11:23.532337+00:00 |
| Files in this snapshot | 332 |

## Directory tree

```text
bin/  (1 files)
  generate.js
fks_chart/  (326 files)
  bower_components/  (321 files)
    angular/  (5 files)
      … 5 files under this directory
    angular-marked/  (9 files)
      … 9 files under this directory
    d3/  (7 files)
      … 7 files under this directory
    jquery/  (84 files)
      … 84 files under this directory
    marked/  (216 files)
      … 216 files under this directory
  css/  (1 files)
    style.css
  data/  (1 files)
    front-end.json
  js/  (1 files)
    app.js
  bower.json
  index.html
.gitignore
Makefile
README.en.md
README.md
package.json
```

## Entry points

- [fks_chart/bower_components/angular-marked/angular-marked.js](https://github.com/JacksonTian/fks/blob/54722627d64b3b8918f4f4cf73752d3675dae99e/fks_chart/bower_components/angular-marked/angular-marked.js)
- [fks_chart/bower_components/marked/lib/marked.js](https://github.com/JacksonTian/fks/blob/54722627d64b3b8918f4f4cf73752d3675dae99e/fks_chart/bower_components/marked/lib/marked.js)
- [fks_chart/bower_components/marked/bin/marked](https://github.com/JacksonTian/fks/blob/54722627d64b3b8918f4f4cf73752d3675dae99e/fks_chart/bower_components/marked/bin/marked)
- [fks_chart/bower_components/marked/index.js](https://github.com/JacksonTian/fks/blob/54722627d64b3b8918f4f4cf73752d3675dae99e/fks_chart/bower_components/marked/index.js)
- [fks_chart/js/app.js](https://github.com/JacksonTian/fks/blob/54722627d64b3b8918f4f4cf73752d3675dae99e/fks_chart/js/app.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bin package | library | Observed | Groups 1 file(s) under bin package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 18 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). |
| fks_chart package | library | Observed | Groups 78 file(s) under fks_chart package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 5 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 201 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `fks_chart/bower.json` (config)
- `fks_chart/bower_components/angular-marked/.bower.json` (config)
- `fks_chart/bower_components/angular-marked/bower.json` (config)
- `fks_chart/bower_components/angular-marked/package.json` (manifest)
- `fks_chart/bower_components/angular/.bower.json` (config)
- `fks_chart/bower_components/angular/bower.json` (config)
- `fks_chart/bower_components/angular/package.json` (manifest)
- `fks_chart/bower_components/d3/.bower.json` (config)
- `fks_chart/bower_components/d3/bower.json` (config)
- `fks_chart/bower_components/d3/composer.json` (config)
- `fks_chart/bower_components/jquery/.bower.json` (config)
- `fks_chart/bower_components/jquery/bower.json` (config)
- `fks_chart/bower_components/marked/.bower.json` (config)
- `fks_chart/bower_components/marked/.travis.yml` (ci)
- `fks_chart/bower_components/marked/component.json` (config)
- `fks_chart/bower_components/marked/package.json` (manifest)
- `fks_chart/data/front-end.json` (config)
- `package.json` (manifest)

## Top-level layout

- `fks_chart` — 326 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x generated/minified file excluded; 1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `54722627d64b3b8918f4f4cf73752d3675dae99e` is the revision these paths and observations refer to.
