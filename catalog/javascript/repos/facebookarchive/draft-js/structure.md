# Project structure: facebookarchive/draft-js

**Analysed commit:** `afdb5c3177c13fd26cb0abbdc439488f3e21b73b`

**Commit reference:** [afdb5c3177c13fd26cb0abbdc439488f3e21b73b](https://github.com/facebookarchive/draft-js/commit/afdb5c3177c13fd26cb0abbdc439488f3e21b73b)

**Tree at this commit:** [facebookarchive/draft-js@afdb5c3177c1](https://github.com/facebookarchive/draft-js/tree/afdb5c3177c13fd26cb0abbdc439488f3e21b73b)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | facebookarchive/draft-js |
| Description | A React framework for building text editors. |
| Stars | 22550 |
| Forks | 2586 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `afdb5c3177c13fd26cb0abbdc439488f3e21b73b` |
| Retrieved at | 2026-11-14T19:11:08.115020+00:00 |
| Files in this snapshot | 440 |

## Directory tree

```text
.dependabot/  (1 files)
  config.yml
.github/  (3 files)
  workflows/  (1 files)
    ci.yml
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
docs/  (30 files)
  APIReference-APIMigration.md
  APIReference-AtomicBlockUtils.md
  APIReference-CharacterMetadata.md
  APIReference-CompositeDecorator.md
  APIReference-ContentBlock.md
  APIReference-ContentState.md
  APIReference-Data-Conversion.md
  APIReference-Editor.md
  APIReference-EditorChangeType.md
  APIReference-EditorState.md
  APIReference-Entity.md
  APIReference-KeyBindingUtil.md
  APIReference-Modifier.md
  APIReference-RichUtils.md
  APIReference-SelectionState.md
  Advanced-Topics-Block-Components.md
  Advanced-Topics-Block-Styling.md
  Advanced-Topics-Custom-Block-Render.md
  Advanced-Topics-Decorators.md
  Advanced-Topics-EditorState-Race-Conditions.md
  Advanced-Topics-Entities.md
  Advanced-Topics-Inline-Styles.md
  Advanced-Topics-Issues-and-Pitfalls.md
  Advanced-Topics-Key-Bindings.md
  … 6 more files
examples/  (43 files)
  draft-0-10-0/  (43 files)
    color/  (1 files)
      … 1 files under this directory
    convertFromHTML/  (1 files)
      … 1 files under this directory
    entity/  (1 files)
      … 1 files under this directory
    iframe/  (1 files)
      … 1 files under this directory
    link/  (1 files)
      … 1 files under this directory
    media/  (1 files)
      … 1 files under this directory
    plaintext/  (1 files)
      … 1 files under this directory
    playground/  (14 files)
      … 14 files under this directory
    rich/  (2 files)
      … 2 files under this directory
    tex/  (12 files)
      … 12 files under this directory
    tweet/  (1 files)
      … 1 files under this directory
    universal/  (7 files)
      … 7 files under this directory
meta/  (42 files)
  meeting-notes/  (41 files)
    2017-02-10-weekly-meeting.md
    2017-02-17-weekly-meeting.md
    2017-02-24-weekly-meeting.md
    2017-03-10-weekly-meeting.md
    2017-03-17-weekly-meeting.md
    2017-03-24-weekly-meeting.md
    2017-03-31-weekly-meeting.md
    2017-04-14-weekly-meeting.md
    2017-04-21-weekly-meeting.md
    2017-04-28-weekly-meeting.md
    2017-05-05-weekly-meeting.md
    2017-05-19-weekly-meeting.md
    2017-05-26-weekly-meeting.md
    2017-06-02-weekly-meeting.md
    2017-07-07-weekly-meeting.md
    2017-07-14-weekly-meeting.md
    2017-07-21-weekly-meeting.md
    2017-07-28-weekly-meeting.md
    2017-08-04-weekly-meeting.md
    2017-08-11-weekly-meeting.md
    2017-08-18-weekly-meeting.md
    2017-09-01-weekly-meeting.md
    2017-09-08-weekly-meeting.md
    2017-09-15-weekly-meeting.md
    … 17 more files
  roadmaps/  (1 files)
    2017-h1.md
scripts/  (4 files)
  jest/  (3 files)
    hasteImpl.js
    preprocessor.js
    shims.js
  module-map.js
src/  (289 files)
  __mocks__/  (1 files)
    generateRandomKey.js
  component/  (114 files)
    base/  (10 files)
      … 10 files under this directory
    contents/  (16 files)
      … 16 files under this directory
    handlers/  (41 files)
      … 41 files under this directory
    selection/  (22 files)
      … 22 files under this directory
    utils/  (25 files)
      … 25 files under this directory
  flowlib/  (1 files)
    window.js
  model/  (163 files)
    constants/  (6 files)
      … 6 files under this directory
    decorators/  (5 files)
      … 5 files under this directory
    encoding/  (32 files)
      … 32 files under this directory
    entity/  (11 files)
      … 11 files under this directory
    immutable/  (39 files)
      … 39 files under this directory
    keys/  (2 files)
      … 2 files under this directory
    modifier/  (21 files)
      … 21 files under this directory
    paste/  (5 files)
      … 5 files under this directory
    transaction/  (42 files)
      … 42 files under this directory
  stubs/  (5 files)
    ComposedEntityMutability.js
    DraftEditorContents.react.js
    DraftEffects.js
    DraftJsDebugLogging.js
    gkx.js
  util/  (2 files)
    getOwnObjectValues.js
    uuid.js
  .flowconfig
  Draft.js
  NonASCIIStringSnapshotSerializer.js
website/  (14 files)
  src/  (7 files)
    components/  (4 files)
      … 4 files under this directory
    css/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
  static/  (2 files)
    img/  (1 files)
      … 1 files under this directory
    CNAME
  .gitignore
  README.md
  docusaurus.config.js
  package.json
  sidebars.js
.alexignore
.alexrc.js
.eslintignore
.eslintrc.js
.gitignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
LICENSE-examples
README.md
gulpfile.js
package.json
prettier.config.js
```

## Entry points

- [examples/draft-0-10-0/universal/index.js](https://github.com/facebookarchive/draft-js/blob/afdb5c3177c13fd26cb0abbdc439488f3e21b73b/examples/draft-0-10-0/universal/index.js)
- [website/src/pages/index.js](https://github.com/facebookarchive/draft-js/blob/afdb5c3177c13fd26cb0abbdc439488f3e21b73b/website/src/pages/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 38 file(s) under api layer (observed from repository paths and static analysis). |
| component package | library | Observed | Groups 62 file(s) under component package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Draft.js package | library | Observed | Groups 1 file(s) under draft.js package (observed from repository paths and static analysis). |
| flowlib package | library | Observed | Groups 1 file(s) under flowlib package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 1 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| model package | library | Observed | Groups 125 file(s) under model package (observed from repository paths and static analysis). |
| NonASCIIStringSnapshotSerializer.js package | library | Observed | Groups 1 file(s) under nonasciistringsnapshotserializer.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). |
| stubs package | library | Observed | Groups 5 file(s) under stubs package (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 2 file(s) under util package (observed from repository paths and static analysis). |
| website package | library | Observed | Groups 4 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.dependabot/config.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `examples/draft-0-10-0/playground/package.json` (manifest)
- `examples/draft-0-10-0/playground/public/manifest.json` (config)
- `examples/draft-0-10-0/tex/package.json` (manifest)
- `examples/draft-0-10-0/universal/package.json` (manifest)
- `package.json` (manifest)
- `website/package.json` (manifest)

## Top-level layout

- `src` — 289 analysed file(s)
- `examples` — 43 analysed file(s)
- `meta` — 42 analysed file(s)
- `docs` — 30 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `website` — 14 analysed file(s)
- `scripts` — 4 analysed file(s)
- `.github` — 3 analysed file(s)
- `.dependabot` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (1 x likely secret file excluded; 1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `afdb5c3177c13fd26cb0abbdc439488f3e21b73b` is the revision these paths and observations refer to.
