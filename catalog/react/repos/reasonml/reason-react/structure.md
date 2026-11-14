# Project structure: reasonml/reason-react

**Analysed commit:** `0206fb41ac67c4ba584409f4eb7d3e501273d431`

**Commit reference:** [0206fb41ac67c4ba584409f4eb7d3e501273d431](https://github.com/reasonml/reason-react/commit/0206fb41ac67c4ba584409f4eb7d3e501273d431)

**Tree at this commit:** [reasonml/reason-react@0206fb41ac67](https://github.com/reasonml/reason-react/tree/0206fb41ac67c4ba584409f4eb7d3e501273d431)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | reasonml/reason-react |
| Description | Reason bindings for ReactJS |
| Stars | 3262 |
| Forks | 344 |
| Licence | MIT |
| Language | Reason |
| Default branch | main |
| Analysed commit | `0206fb41ac67c4ba584409f4eb7d3e501273d431` |
| Retrieved at | 2026-11-14T19:15:26.914508+00:00 |
| Files in this snapshot | 216 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (3 files)
    nix.yml
    opam.yml
    website.yml
.vscode/  (1 files)
  settings.json
demo/  (3 files)
  dune
  index.html
  main.re
docs/  (39 files)
  adding-data-props.md
  clone-element.md
  community.md
  component-as-prop.md
  components.md
  context.md
  custom-hooks.md
  dom.md
  element-type-is-invalid.md
  error-boundaries.md
  event.md
  example-projects.md
  graphql-apollo.md
  i-really-need-feature-x-from-reactjs.md
  i-want-to-create-a-dom-element-without-jsx.md
  im-having-a-type-error.md
  importing-js-into-reason.md
  importing-reason-into-js.md
  installation.md
  intro-example.md
  invalid-prop-name.md
  js-using-reason.md
  jsx.md
  playground.md
  … 15 more files
ppx/  (34 files)
  test/  (31 files)
    component-without-make.t/  (2 files)
      … 2 files under this directory
    component.t/  (2 files)
      … 2 files under this directory
    data-attribute-collisions.t/  (2 files)
      … 2 files under this directory
    data-attributes.t/  (2 files)
      … 2 files under this directory
    external.t/  (2 files)
      … 2 files under this directory
    fragment.t/  (2 files)
      … 2 files under this directory
    functor.t/  (2 files)
      … 2 files under this directory
    lower.t/  (2 files)
      … 2 files under this directory
    record-props-error.t/  (2 files)
      … 2 files under this directory
    record-props.t/  (2 files)
      … 2 files under this directory
    signature-optional.t/  (2 files)
      … 2 files under this directory
    signature.t/  (2 files)
      … 2 files under this directory
    upper.t/  (2 files)
      … 2 files under this directory
    dune
    input.re
    locations-check.t
    ppx.sh
    run-ppx.sh
  dune
  reason_react_ppx.ml
  standalone.ml
src/  (16 files)
  README.md
  React.re
  React.rei
  ReactDOM.re
  ReactDOM.rei
  ReactDOMServer.re
  ReactDOMServer.rei
  ReactDOMServerNode.re
  ReactDOMServerNode.rei
  ReactDOMTestUtils.re
  ReactDOMTestUtils.rei
  ReasonReactErrorBoundary.re
  ReasonReactErrorBoundary.rei
  ReasonReactRouter.re
  ReasonReactRouter.rei
  dune
test/  (46 files)
  blackbox-tests/  (22 files)
    components-destructured-error.t/  (2 files)
      … 2 files under this directory
    data-attributes.t/  (1 files)
      … 1 files under this directory
    dom-props.t/  (2 files)
      … 2 files under this directory
    issue-429.t/  (2 files)
      … 2 files under this directory
    key-as-prop-error.t/  (2 files)
      … 2 files under this directory
    keys.t/  (2 files)
      … 2 files under this directory
    simple.t/  (2 files)
      … 2 files under this directory
    uppercase.t/  (2 files)
      … 2 files under this directory
    dom-props-completion.t
    dom-props-locations.t
    dune
    hover.t
    optional-arg-check.t
    react.t
    useCallback.t
  jest/  (5 files)
    Expect.re
    Jest.re
    Mock.re
    README.md
    dune
  melange-testing-library/  (11 files)
    dom/  (7 files)
      … 7 files under this directory
    react/  (3 files)
      … 3 files under this directory
    README.md
  Form__test.re
  Hooks__test.re
  ReactDOMDataAttributes__test.re
  ReactDOM__test.re
  ReactRouter__test.re
  React__test.re
  Ref__test.re
  dune
website/  (56 files)
  blog/  (16 files)
    2017-06-09-major-release.md
    2017-06-21-015.md
    2017-07-05-021.md
    2017-09-01-reducers.md
    2017-10-02-new-docs-site.md
    2017-11-17-power-children.md
    2018-01-09-subscriptions-send-router.md
    2018-08-06-050.md
    2019-03-12-small-release.md
    2019-04-10-react-hooks.md
    2019-10-18-new-bsb-template.md
    2020-05-05-080-release.md
    2020-06-08-090-release.md
    2021-05-07-rescript-migration.md
    2023-06-11-reborn.md
    2023-09-13-reason-react-ppx.md
  core/  (1 files)
    Footer.js
  i18n/  (1 files)
    en.json
  pages/  (6 files)
    en/  (6 files)
      … 6 files under this directory
  static/  (26 files)
    css/  (3 files)
      … 3 files under this directory
    img/  (19 files)
      … 19 files under this directory
    js/  (3 files)
      … 3 files under this directory
    .nojekyll
  .gitignore
  README.md
  languages.js
  package.json
  sidebars.json
  siteConfig.js
.gitattributes
.gitignore
.npmignore
.ocamlformat
CHANGES.md
CONTRIBUTING.md
LICENSE
Makefile
README.md
crowdin.yaml
dune
dune-project
flake.lock
flake.nix
package.json
reason-react-ppx.opam
reason-react.opam
reason-react.opam.template
```

## Entry points

- [website/pages/en/index.js](https://github.com/reasonml/reason-react/blob/0206fb41ac67c4ba584409f4eb7d3e501273d431/website/pages/en/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 1 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 77 file(s) under tests (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 11 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/nix.yml` (ci)
- `.github/workflows/opam.yml` (ci)
- `.github/workflows/website.yml` (ci)
- `.vscode/settings.json` (config)
- `crowdin.yaml` (config)
- `package.json` (manifest)
- `website/i18n/en.json` (config)
- `website/package.json` (manifest)
- `website/sidebars.json` (config)

## Top-level layout

- `website` — 56 analysed file(s)
- `test` — 46 analysed file(s)
- `docs` — 39 analysed file(s)
- `ppx` — 34 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `src` — 16 analysed file(s)
- `.github` — 3 analysed file(s)
- `demo` — 3 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `0206fb41ac67c4ba584409f4eb7d3e501273d431` is the revision these paths and observations refer to.
