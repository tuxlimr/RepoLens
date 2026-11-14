# Project structure: riot/riot

**Analysed commit:** `e46e3bbf962b2bfad672de199c67bcc4147e430b`

**Commit reference:** [e46e3bbf962b2bfad672de199c67bcc4147e430b](https://github.com/riot/riot/commit/e46e3bbf962b2bfad672de199c67bcc4147e430b)

**Tree at this commit:** [riot/riot@e46e3bbf962b](https://github.com/riot/riot/tree/e46e3bbf962b2bfad672de199c67bcc4147e430b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | riot/riot |
| Description | Simple and elegant component-based UI library |
| Stars | 14925 |
| Forks | 953 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `e46e3bbf962b2bfad672de199c67bcc4147e430b` |
| Retrieved at | 2026-11-14T19:11:42.134135+00:00 |
| Files in this snapshot | 162 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (1 files)
    test.yml
  CONTRIBUTING.md
  FUNDING.yml
  PULL_REQUEST_TEMPLATE.md
.qlty/  (1 files)
  qlty.toml
src/  (45 files)
  api/  (12 files)
    __.js
    component.js
    create-pure-component.js
    install.js
    mount.js
    pure.js
    register.js
    uninstall.js
    unmount.js
    unregister.js
    version.js
    with-types.js
  compiler/  (10 files)
    compile-from-string.js
    compile-from-url.js
    compile.js
    component-with-slots.js
    define-window-riot-global-registry.js
    evaluate.js
    global-registry.js
    inject.js
    mount-with-slots.js
    transpile.js
  core/  (18 files)
    add-css-hook.js
    bind-dom-node-to-component-instance.js
    component-dom-selectors.js
    component-lifecycle-methods.js
    component-template-factory.js
    compute-component-state.js
    compute-initial-props.js
    create-attribute-bindings.js
    create-component-from-wrapper.js
    create-core-api-methods.js
    create-pure-component.js
    css-manager.js
    instantiate-component.js
    manage-component-lifecycle.js
    mocked-template-interface.js
    mount-component.js
    pure-component-api.js
    run-plugins.js
  utils/  (3 files)
    create-runtime-slots.js
    dom.js
    get-root-computed-attribute-names.js
  riot+compiler.js
  riot.js
test/  (96 files)
  components/  (72 files)
    child.riot
    comments-and-expressions.riot
    component-with-getters.riot
    conditional-select-option.riot
    conditional-slot-parent.riot
    conditional-slot.riot
    custom-tag-ref-attribute.riot
    dashed-attribute-child.riot
    dashed-attribute-parent.riot
    default-content-slot.riot
    each-and-spread-attribute.riot
    each-custom-children-components.riot
    each-root-attributes.riot
    expression-parts.riot
    global-components.riot
    hmr-child-parent.riot
    hmr-child-v1.riot
    hmr-child-v2.riot
    invalid-pure-css-component.riot
    invalid-pure-html-component.riot
    issue-2895-child.riot
    issue-2895-parent.riot
    issue-2978-child.riot
    issue-2978-parent.riot
    … 48 more files
  e2e/  (4 files)
    index.html
    index.js
    rollup.config.js
    test.e2e.js
  specs/  (9 files)
    compiler.spec.js
    components-registration.spec.js
    components-rendering.spec.js
    hot-reload.spec.js
    lifecycle-events.spec.js
    plugins-api.spec.js
    public-api.spec.js
    slots.spec.js
    state-and-props.spec.js
  typing/  (8 files)
    autobound-methods-type-inference.ts
    component-function-export.spec.ts
    component-object-export.spec.ts
    public-api.spec.ts
    pure-component.ts
    shims-riot.d.ts
    with-types-infer.ts
    wrapper-template-get-component-return-type.ts
  setup.js
  tsconfig.json
  utils.js
.gitignore
.prettierignore
.prettierrc.js
AWESOME.md
CODE_OF_CONDUCT.md
LICENSE.txt
Makefile
README.md
eslint.config.js
package.json
riot.d.ts
riot.js
rollup.config.js
wdio.conf.js
```

## Entry points

- [riot.js](https://github.com/riot/riot/blob/e46e3bbf962b2bfad672de199c67bcc4147e430b/riot.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 12 file(s) under api layer (observed from repository paths and static analysis). |
| compiler package | library | Observed | Groups 10 file(s) under compiler package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| riot+compiler.js package | library | Observed | Groups 1 file(s) under riot+compiler.js package (observed from repository paths and static analysis). |
| riot.js package | library | Observed | Groups 1 file(s) under riot.js package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 18 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 96 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 3 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/test.yml` (ci)
- `.qlty/qlty.toml` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 96 analysed file(s)
- `src` — 45 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 6 analysed file(s)
- `.qlty` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e46e3bbf962b2bfad672de199c67bcc4147e430b` is the revision these paths and observations refer to.
