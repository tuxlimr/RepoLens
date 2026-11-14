# Project structure: Stuk/jszip

**Analysed commit:** `609d95f4098a11507160cd101e0b181cfad6a582`

**Commit reference:** [609d95f4098a11507160cd101e0b181cfad6a582](https://github.com/Stuk/jszip/commit/609d95f4098a11507160cd101e0b181cfad6a582)

**Tree at this commit:** [Stuk/jszip@609d95f4098a](https://github.com/Stuk/jszip/tree/609d95f4098a11507160cd101e0b181cfad6a582)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Stuk/jszip |
| Description | Create, read and edit .zip files with Javascript |
| Stars | 10398 |
| Forks | 1338 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `609d95f4098a11507160cd101e0b181cfad6a582` |
| Retrieved at | 2026-11-14T19:12:40.938032+00:00 |
| Files in this snapshot | 140 |

## Directory tree

```text
.github/  (4 files)
  actions/  (1 files)
    setup/  (1 files)
      … 1 files under this directory
  workflows/  (2 files)
    benchmark.yml
    main.yml
  FUNDING.yml
docs/  (3 files)
  APPNOTE.TXT
  ZIP spec.txt
  references.txt
documentation/  (55 files)
  _layouts/  (1 files)
    default.html
  api_jszip/  (17 files)
    constructor.md
    external.md
    file_data.md
    file_name.md
    file_regex.md
    filter.md
    folder_name.md
    folder_regex.md
    for_each.md
    generate_async.md
    generate_internal_stream.md
    generate_node_stream.md
    load_async.md
    load_async_object.md
    remove.md
    support.md
    version.md
  api_streamhelper/  (4 files)
    accumulate.md
    on.md
    pause.md
    resume.md
  api_zipobject/  (3 files)
    async.md
    internal_stream.md
    node_stream.md
  css/  (2 files)
    main.css
    pygments.css
  examples/  (17 files)
    download-zip-file.inc/  (4 files)
      … 4 files under this directory
    downloader.inc/  (3 files)
      … 3 files under this directory
    get-binary-files-ajax.inc/  (4 files)
      … 4 files under this directory
    read-local-file-api.inc/  (2 files)
      … 2 files under this directory
    download-zip-file.html
    downloader.html
    get-binary-files-ajax.html
    read-local-file-api.html
  howto/  (2 files)
    read_zip.md
    write_zip.md
  .eslintrc.js
  api_jszip.md
  api_streamhelper.md
  api_zipobject.md
  contributing.md
  examples.md
  faq.md
  limitations.md
  upgrade_guide.md
lib/  (36 files)
  generate/  (2 files)
    ZipFileWorker.js
    index.js
  nodejs/  (2 files)
    NodejsStreamInputAdapter.js
    NodejsStreamOutputAdapter.js
  reader/  (6 files)
    ArrayReader.js
    DataReader.js
    NodeBufferReader.js
    StringReader.js
    Uint8ArrayReader.js
    readerFor.js
  stream/  (6 files)
    ConvertWorker.js
    Crc32Probe.js
    DataLengthProbe.js
    DataWorker.js
    GenericWorker.js
    StreamHelper.js
  base64.js
  compressedObject.js
  compressions.js
  crc32.js
  defaults.js
  external.js
  flate.js
  index.js
  license_header.js
  load.js
  nodejsUtils.js
  object.js
  readable-stream-browser.js
  signature.js
  support.js
  utf8.js
  utils.js
  zipEntries.js
  zipEntry.js
  zipObject.js
test/  (25 files)
  asserts/  (14 files)
    constructor.js
    delete.js
    deprecated.js
    external.js
    file.js
    filter.js
    foreach.js
    generate.js
    load.js
    permissions.js
    stream.js
    unicode.js
    utils.js
    version.js
  benchmark/  (4 files)
    .eslintrc.js
    benchmark.js
    index.html
    node.js
  browser/  (1 files)
    cross-realm.js
  helpers/  (3 files)
    browser-test-utils.js
    node-test-utils.js
    test-utils.js
  .eslintrc.js
  index.html
  run.js
.codeclimate.yml
.editorconfig
.eslintrc.js
.gitignore
.npmignore
CHANGES.md
Gruntfile.js
LICENSE.markdown
README.markdown
_config.yml
bower.json
component.json
index.d.ts
index.html
package.json
sponsors.md
tsconfig.json
```

## Entry points

- [lib/generate/index.js](https://github.com/Stuk/jszip/blob/609d95f4098a11507160cd101e0b181cfad6a582/lib/generate/index.js)
- [lib/index.js](https://github.com/Stuk/jszip/blob/609d95f4098a11507160cd101e0b181cfad6a582/lib/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| documentation package | library | Observed | Groups 8 file(s) under documentation package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 36 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 25 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.codeclimate.yml` (config)
- `.editorconfig` (config)
- `.github/FUNDING.yml` (config)
- `.github/actions/setup/action.yml` (config)
- `.github/workflows/benchmark.yml` (ci)
- `.github/workflows/main.yml` (ci)
- `_config.yml` (config)
- `bower.json` (config)
- `component.json` (config)
- `package.json` (manifest)
- `tsconfig.json` (config)

## Top-level layout

- `documentation` — 55 analysed file(s)
- `lib` — 36 analysed file(s)
- `test` — 25 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.github` — 4 analysed file(s)
- `docs` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `609d95f4098a11507160cd101e0b181cfad6a582` is the revision these paths and observations refer to.
