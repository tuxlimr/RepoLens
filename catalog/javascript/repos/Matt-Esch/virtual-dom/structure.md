# Project structure: Matt-Esch/virtual-dom

**Analysed commit:** `947ecf92b67d25bb693a0f625fa8e90c099887d5`

**Commit reference:** [947ecf92b67d25bb693a0f625fa8e90c099887d5](https://github.com/Matt-Esch/virtual-dom/commit/947ecf92b67d25bb693a0f625fa8e90c099887d5)

**Tree at this commit:** [Matt-Esch/virtual-dom@947ecf92b67d](https://github.com/Matt-Esch/virtual-dom/tree/947ecf92b67d25bb693a0f625fa8e90c099887d5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Matt-Esch/virtual-dom |
| Description | A Virtual DOM and diffing algorithm |
| Stars | 11820 |
| Forks | 762 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `947ecf92b67d25bb693a0f625fa8e90c099887d5` |
| Retrieved at | 2026-11-14T19:12:14.278412+00:00 |
| Files in this snapshot | 80 |

## Directory tree

```text
docs/  (8 files)
  README.md
  css-animations.md
  faq.md
  hooks.md
  thunk.md
  vnode.md
  vtext.md
  widget.md
test/  (15 files)
  lib/  (4 files)
    assert-childNodes-from-array.js
    assert-equal-dom.js
    nodes-from-array.js
    patch-count.js
  attributes.js
  hook.js
  index.js
  keys.js
  main.js
  nested-properties.js
  non-string.js
  sort.js
  style.js
  thunk.js
  undefined-properties.js
vdom/  (11 files)
  test/  (4 files)
    dom-index.js
    index.js
    patch-index.js
    patch-op-index.js
  README.md
  apply-properties.js
  create-element.js
  dom-index.js
  patch-op.js
  patch.js
  update-widget.js
virtual-hyperscript/  (14 files)
  hooks/  (4 files)
    attribute-hook.js
    ev-hook.js
    focus-hook.js
    soft-set-hook.js
  test/  (5 files)
    attribute-hook.js
    ev-hook.js
    h.js
    index.js
    svg.js
  README.md
  index.js
  parse-tag.js
  svg-attribute-namespace.js
  svg.js
vnode/  (12 files)
  test/  (2 files)
    handle-thunk.js
    index.js
  handle-thunk.js
  is-thunk.js
  is-vhook.js
  is-vnode.js
  is-vtext.js
  is-widget.js
  version.js
  vnode.js
  vpatch.js
  vtext.js
vtree/  (5 files)
  test/  (2 files)
    diff-props.js
    index.js
  README.md
  diff-props.js
  diff.js
.editorconfig
.gitignore
.jshintrc
.travis.yml
.zuul.yml
CHANGELOG.md
LICENSE
README.md
create-element.js
diff.js
docs.jsig
h.js
index.js
package.json
patch.js
```

## Entry points

- [index.js](https://github.com/Matt-Esch/virtual-dom/blob/947ecf92b67d25bb693a0f625fa8e90c099887d5/index.js)
- [virtual-hyperscript/index.js](https://github.com/Matt-Esch/virtual-dom/blob/947ecf92b67d25bb693a0f625fa8e90c099887d5/virtual-hyperscript/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 28 file(s) under tests (observed from repository paths and static analysis). |
| vdom package | library | Observed | Groups 6 file(s) under vdom package (observed from repository paths and static analysis). |
| virtual-hyperscript package | library | Observed | Groups 8 file(s) under virtual-hyperscript package (observed from repository paths and static analysis). |
| vnode package | library | Observed | Groups 10 file(s) under vnode package (observed from repository paths and static analysis). |
| vtree package | library | Observed | Groups 2 file(s) under vtree package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.travis.yml` (ci)
- `.zuul.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `(root files)` — 15 analysed file(s)
- `test` — 15 analysed file(s)
- `virtual-hyperscript` — 14 analysed file(s)
- `vnode` — 12 analysed file(s)
- `vdom` — 11 analysed file(s)
- `docs` — 8 analysed file(s)
- `vtree` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `947ecf92b67d25bb693a0f625fa8e90c099887d5` is the revision these paths and observations refer to.
