# Project structure: yargs/yargs

**Analysed commit:** `f444858808bc11e9910fc5ed0d0322dc40d5638e`

**Commit reference:** [f444858808bc11e9910fc5ed0d0322dc40d5638e](https://github.com/yargs/yargs/commit/f444858808bc11e9910fc5ed0d0322dc40d5638e)

**Tree at this commit:** [yargs/yargs@f444858808bc](https://github.com/yargs/yargs/tree/f444858808bc11e9910fc5ed0d0322dc40d5638e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | yargs/yargs |
| Description |  yargs the modern, pirate-themed successor to optimist. |
| Stars | 11508 |
| Forks | 1063 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `f444858808bc11e9910fc5ed0d0322dc40d5638e` |
| Retrieved at | 2026-11-14T19:12:17.634043+00:00 |
| Files in this snapshot | 173 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (2 files)
    ci.yaml
    release-please.yml
  FUNDING.yml
docs/  (7 files)
  advanced.md
  api.md
  browser.md
  examples.md
  release-policy.md
  tricks.md
  typescript.md
example/  (28 files)
  cmds/  (4 files)
    remote_cmds/  (2 files)
      … 2 files under this directory
    init.mjs
    remote.mjs
  bool.cjs
  boolean_double.cjs
  boolean_single.cjs
  command_hierarchy.mjs
  complex.mjs
  count.mjs
  default_hash.mjs
  default_singles.mjs
  demand_count.mjs
  divide.mjs
  help.mjs
  implies.mjs
  implies_hash.mjs
  line_count.mjs
  line_count_options.mjs
  line_count_wrap.mjs
  nested.mjs
  nonopt.mjs
  requires_arg.mjs
  short.mjs
  string.mjs
  usage-options.mjs
  xup.mjs
  yargs.html
helpers/  (2 files)
  helpers.mjs
  package.json
lib/  (23 files)
  platform-shims/  (3 files)
    browser.mjs
    deno.ts
    esm.mjs
  typings/  (2 files)
    common-types.ts
    yargs-parser-types.ts
  utils/  (8 files)
    apply-extends.ts
    is-promise.ts
    levenshtein.ts
    maybe-async-result.ts
    obj-filter.ts
    process-argv.ts
    set-blocking.ts
    which-module.ts
  argsert.ts
  command.ts
  completion-templates.ts
  completion.ts
  middleware.ts
  parse-command.ts
  usage.ts
  validation.ts
  yargs-factory.ts
  yerror.ts
locales/  (29 files)
  be.json
  cs.json
  de.json
  en.json
  es.json
  fi.json
  fr.json
  he.json
  hi.json
  hu.json
  id.json
  it.json
  ja.json
  ka.json
  ko.json
  nb.json
  nl.json
  nn.json
  pirate.json
  pl.json
  pt.json
  pt_BR.json
  ru.json
  th.json
  … 5 more files
test/  (59 files)
  deno/  (2 files)
    platform-shim.test.ts
    yargs.test.ts
  esm/  (9 files)
    fixtures/  (6 files)
      … 6 files under this directory
    helpers.mjs
    platform-shim-test.mjs
    yargs-test.mjs
  fixtures/  (33 files)
    broken-json/  (1 files)
      … 1 files under this directory
    cmddir/  (5 files)
      … 5 files under this directory
    cmddir_cyclic/  (1 files)
      … 1 files under this directory
    cmddir_noname/  (1 files)
      … 1 files under this directory
    esm-command/  (4 files)
      … 4 files under this directory
    extends/  (10 files)
      … 10 files under this directory
    bin.js
    command-module.js
    command.js
    config.json
    issue-497.js
    no-extension
    no-require-main.js
    normal-bin.js
    opt-assignment-and-positional-command-arg.js
    package.json
    symlink-bin.js
  helpers/  (1 files)
    utils.mjs
  argsert.mjs
  before.mjs
  command.mjs
  completion.mjs
  helpers.mjs
  integration.mjs
  is-promise.mjs
  middleware.mjs
  obj-filter.mjs
  parse-command.mjs
  parser.mjs
  usage.mjs
  validation.mjs
  yargs.mjs
.eslintignore
.eslintrc.json
.gitattributes
.gitignore
.nycrc
.prettierrc.cjs
AI_POLICY.md
CHANGELOG.md
CODE_OF_CONDUCT.md
LICENSE
README.md
SECURITY.md
browser.d.ts
browser.mjs
contributing.md
deno-types.ts
deno.ts
index.mjs
package.json
renovate.json
tsconfig.json
tsconfig.test.json
```

## Entry points

- [index.mjs](https://github.com/yargs/yargs/blob/f444858808bc11e9910fc5ed0d0322dc40d5638e/index.mjs)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 34 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| helpers package | library | Observed | Groups 1 file(s) under helpers package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 23 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 59 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/workflows/ci.yaml` (ci)
- `.github/workflows/release-please.yml` (ci)
- `helpers/package.json` (manifest)
- `locales/be.json` (config)
- `locales/cs.json` (config)
- `locales/de.json` (config)
- `locales/en.json` (config)
- `locales/es.json` (config)
- `locales/fi.json` (config)
- `locales/fr.json` (config)
- `locales/he.json` (config)
- `locales/hi.json` (config)
- `locales/hu.json` (config)
- `locales/id.json` (config)
- `locales/it.json` (config)
- `locales/ja.json` (config)
- `locales/ka.json` (config)
- `locales/ko.json` (config)
- `locales/nb.json` (config)
- `locales/nl.json` (config)
- `locales/nn.json` (config)
- `locales/pirate.json` (config)
- `locales/pl.json` (config)
- `locales/pt.json` (config)
- `locales/pt_BR.json` (config)
- `locales/ru.json` (config)
- `locales/th.json` (config)
- `locales/tr.json` (config)
- `locales/uk_UA.json` (config)
- `locales/uz.json` (config)
- `locales/zh_CN.json` (config)
- `locales/zh_TW.json` (config)
- `package.json` (manifest)
- `renovate.json` (config)
- `tsconfig.json` (config)
- `tsconfig.test.json` (config)

## Top-level layout

- `test` — 59 analysed file(s)
- `locales` — 29 analysed file(s)
- `example` — 28 analysed file(s)
- `lib` — 23 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `docs` — 7 analysed file(s)
- `.github` — 3 analysed file(s)
- `helpers` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `f444858808bc11e9910fc5ed0d0322dc40d5638e` is the revision these paths and observations refer to.
