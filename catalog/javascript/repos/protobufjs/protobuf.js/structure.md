# Project structure: protobufjs/protobuf.js

**Analysed commit:** `798b4c942cca81a7ae0a2694f28ecd2985d386c9`

**Commit reference:** [798b4c942cca81a7ae0a2694f28ecd2985d386c9](https://github.com/protobufjs/protobuf.js/commit/798b4c942cca81a7ae0a2694f28ecd2985d386c9)

**Tree at this commit:** [protobufjs/protobuf.js@798b4c942cca](https://github.com/protobufjs/protobuf.js/tree/798b4c942cca81a7ae0a2694f28ecd2985d386c9)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | protobufjs/protobuf.js |
| Description | High-performance Protocol Buffers for JavaScript and TypeScript. Conformant through Edition 2026, and unusually versatile. No protoc required. |
| Stars | 10608 |
| Forks | 1855 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `798b4c942cca81a7ae0a2694f28ecd2985d386c9` |
| Retrieved at | 2026-11-14T19:12:36.350135+00:00 |
| Files in this snapshot | 361 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (2 files)
    config.yml
    issue.yml
  actions/  (1 files)
    conformance/  (1 files)
      … 1 files under this directory
  workflows/  (2 files)
    release.yaml
    test.yml
  FUNDING.yml
bench/  (25 files)
  cases/  (10 files)
    buf-perf/  (3 files)
      … 3 files under this directory
    common/  (3 files)
      … 3 files under this directory
    vector-tile/  (3 files)
      … 3 files under this directory
    support.js
  generated/  (1 files)
    .gitignore
  results/  (7 files)
    decode-dark.svg
    decode-light.svg
    decode.svg
    encode-dark.svg
    encode-light.svg
    encode.svg
    latest.json
  README.md
  generate.js
  index.js
  package.json
  prof.js
  report.js
  suite.js
cli/  (40 files)
  bin/  (3 files)
    pbjs
    pbts
    protoc-gen-pbjs
  lib/  (11 files)
    catharsis/  (5 files)
      … 5 files under this directory
    tsd-jsdoc/  (5 files)
      … 5 files under this directory
    tsd-jsdoc.json
  targets/  (7 files)
    json-module.js
    json.js
    proto.js
    proto2.js
    proto3.js
    static-module.js
    static.js
  wrappers/  (6 files)
    amd.js
    closure.js
    commonjs.js
    default.js
    es6.js
    esm.js
  CHANGELOG.md
  LICENSE
  README.md
  index.d.ts
  index.js
  package.json
  pbjs.d.ts
  pbjs.js
  pbts.d.ts
  pbts.js
  protoc-gen-pbjs.d.ts
  protoc-gen-pbjs.js
  util.js
config/  (2 files)
  jsdoc.json
  tslint.json
examples/  (5 files)
  custom-get-set.js
  grpc-service.js
  reader-writer.js
  streaming-rpc.js
  traverse-types.js
ext/  (16 files)
  debug/  (2 files)
    README.md
    index.js
  descriptor/  (3 files)
    README.md
    index.d.ts
    index.js
  README.md
  descriptor.d.ts
  descriptor.generated.d.ts
  descriptor.js
  protojson.LICENSE
  protojson.d.ts
  protojson.generated.d.ts
  protojson.js
  textformat.d.ts
  textformat.generated.d.ts
  textformat.js
google/  (18 files)
  api/  (4 files)
    annotations.json
    annotations.proto
    http.json
    http.proto
  protobuf/  (12 files)
    compiler/  (2 files)
      … 2 files under this directory
    api.json
    api.proto
    descriptor.json
    descriptor.proto
    json_enumvalue_options.json
    json_enumvalue_options.proto
    source_context.json
    source_context.proto
    type.json
    type.proto
  LICENSE
  README.md
lib/  (7 files)
  deep-equal/  (5 files)
    lib/  (2 files)
      … 2 files under this directory
    LICENSE
    README.md
    index.js
  prelude.js
  tape-adapter.js
scripts/  (5 files)
  bundle.js
  gencommons.js
  gentests.js
  gulpfile.js
  pages.js
src/  (54 files)
  rpc/  (1 files)
    service.js
  util/  (22 files)
    aspromise.d.ts
    aspromise.js
    base64.d.ts
    base64.js
    codegen.d.ts
    codegen.js
    eventemitter.d.ts
    eventemitter.js
    fetch.d.ts
    fetch.js
    float.d.ts
    float.js
    fs.js
    longbits.js
    minimal.js
    path.d.ts
    path.js
    patterns.js
    pool.d.ts
    pool.js
    utf8.d.ts
    utf8.js
  common.js
  converter.js
  decoder.js
  encoder.js
  enum.js
  field.js
  index-light.js
  index-minimal.js
  index.js
  mapfield.js
  message.js
  method.js
  namespace.js
  object.js
  oneof.js
  parse.js
  reader.js
  reader_buffer.js
  root.js
  roots.js
  rpc.js
  service.js
  tokenize.js
  type.js
  … 7 more files
tests/  (161 files)
  conformance/  (6 files)
    .gitignore
    check.js
    generate.js
    report.js
    summary.js
    testee.js
  data/  (62 files)
    cli/  (9 files)
      … 9 files under this directory
    google/  (2 files)
      … 2 files under this directory
    mapbox/  (4 files)
      … 4 files under this directory
    util_fetch/  (1 files)
      … 1 files under this directory
    util_utf8/  (2 files)
      … 2 files under this directory
    badimport.proto
    comment_serialization.proto
    comments-alternate-parse.proto
    comments.d.ts
    comments.js
    comments.proto
    common-custom.proto
    common.json
    common.proto
    convert.d.ts
    convert.js
    convert.proto
    enum-semantics.d.ts
    enum-semantics.js
    enum-semantics.proto
    feature-resolution.proto
    import-option-bad.proto
    invalid-lookup.proto
    invalid.json
    invalid.proto
    issue936.proto
    options_test.proto
    package.d.ts
    package.js
    … 20 more files
  helpers/  (1 files)
    cli.js
  node/  (3 files)
    api_load-sync.js
    comp_loaders.js
    override-mistake.js
  split/  (2 files)
    root.js
    test.proto
  README.md
  api_Class.js
  api_common.js
  api_converters.js
  api_decoder_bounds.js
  api_descriptor.js
  api_enum.js
  api_field.js
  api_inheritance.js
  api_longbits.js
  api_mapfield.js
  api_namespace.js
  api_object.js
  api_oneof.js
  api_protojson.js
  api_reader-writer-reuse.js
  api_reader_packed.js
  api_root-deferred.js
  api_root-expose.js
  api_root.js
  api_service-rpc-streaming.js
  api_service-rpc.js
  api_service.js
  api_textformat.js
  … 63 more files
.gitattributes
.gitignore
.gitmodules
.release-please-manifest.json
CHANGELOG.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
eslint.config.cjs
index.d.ts
index.js
light.d.ts
light.js
minimal.d.ts
minimal.js
package.json
pbjs.svg
release-please-config.json
renovate.json
tsconfig.json
tsconfig.test-types.json
```

## Entry points

- [cli/index.js](https://github.com/protobufjs/protobuf.js/blob/798b4c942cca81a7ae0a2694f28ecd2985d386c9/cli/index.js)
- [cli/bin/pbjs](https://github.com/protobufjs/protobuf.js/blob/798b4c942cca81a7ae0a2694f28ecd2985d386c9/cli/bin/pbjs)
- [cli/bin/pbts](https://github.com/protobufjs/protobuf.js/blob/798b4c942cca81a7ae0a2694f28ecd2985d386c9/cli/bin/pbts)
- [cli/bin/protoc-gen-pbjs](https://github.com/protobufjs/protobuf.js/blob/798b4c942cca81a7ae0a2694f28ecd2985d386c9/cli/bin/protoc-gen-pbjs)
- [index.js](https://github.com/protobufjs/protobuf.js/blob/798b4c942cca81a7ae0a2694f28ecd2985d386c9/index.js)
- [bench/cases/buf-perf/index.js](https://github.com/protobufjs/protobuf.js/blob/798b4c942cca81a7ae0a2694f28ecd2985d386c9/bench/cases/buf-perf/index.js)
- [bench/cases/common/index.js](https://github.com/protobufjs/protobuf.js/blob/798b4c942cca81a7ae0a2694f28ecd2985d386c9/bench/cases/common/index.js)
- [bench/cases/vector-tile/index.js](https://github.com/protobufjs/protobuf.js/blob/798b4c942cca81a7ae0a2694f28ecd2985d386c9/bench/cases/vector-tile/index.js)
- [bench/index.js](https://github.com/protobufjs/protobuf.js/blob/798b4c942cca81a7ae0a2694f28ecd2985d386c9/bench/index.js)
- [ext/debug/index.js](https://github.com/protobufjs/protobuf.js/blob/798b4c942cca81a7ae0a2694f28ecd2985d386c9/ext/debug/index.js)
- [ext/descriptor/index.js](https://github.com/protobufjs/protobuf.js/blob/798b4c942cca81a7ae0a2694f28ecd2985d386c9/ext/descriptor/index.js)
- [lib/deep-equal/index.js](https://github.com/protobufjs/protobuf.js/blob/798b4c942cca81a7ae0a2694f28ecd2985d386c9/lib/deep-equal/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| bench package | library | Observed | Groups 9 file(s) under bench package (observed from repository paths and static analysis). |
| cli package | library | Observed | Groups 28 file(s) under cli package (observed from repository paths and static analysis). |
| common.js package | library | Observed | Groups 1 file(s) under common.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 20 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| converter.js package | library | Observed | Groups 1 file(s) under converter.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 7 file(s) under core modules (observed from repository paths and static analysis). |
| decoder.js package | library | Observed | Groups 1 file(s) under decoder.js package (observed from repository paths and static analysis). |
| encoder.js package | library | Observed | Groups 1 file(s) under encoder.js package (observed from repository paths and static analysis). |
| enum.js package | library | Observed | Groups 1 file(s) under enum.js package (observed from repository paths and static analysis). |
| ext package | library | Observed | Groups 12 file(s) under ext package (observed from repository paths and static analysis). |
| field.js package | library | Observed | Groups 1 file(s) under field.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| index-light.js package | library | Observed | Groups 1 file(s) under index-light.js package (observed from repository paths and static analysis). |
| index-minimal.js package | library | Observed | Groups 1 file(s) under index-minimal.js package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 5 file(s) under lib package (observed from repository paths and static analysis). |
| mapfield.js package | library | Observed | Groups 1 file(s) under mapfield.js package (observed from repository paths and static analysis). |
| message.js package | library | Observed | Groups 1 file(s) under message.js package (observed from repository paths and static analysis). |
| method.js package | library | Observed | Groups 1 file(s) under method.js package (observed from repository paths and static analysis). |
| namespace.js package | library | Observed | Groups 1 file(s) under namespace.js package (observed from repository paths and static analysis). |
| object.js package | library | Observed | Groups 1 file(s) under object.js package (observed from repository paths and static analysis). |
| oneof.js package | library | Observed | Groups 1 file(s) under oneof.js package (observed from repository paths and static analysis). |
| parse.js package | library | Observed | Groups 1 file(s) under parse.js package (observed from repository paths and static analysis). |
| reader_buffer.js package | library | Observed | Groups 1 file(s) under reader_buffer.js package (observed from repository paths and static analysis). |
| reader.js package | library | Observed | Groups 1 file(s) under reader.js package (observed from repository paths and static analysis). |
| root.js package | library | Observed | Groups 1 file(s) under root.js package (observed from repository paths and static analysis). |
| roots.js package | library | Observed | Groups 1 file(s) under roots.js package (observed from repository paths and static analysis). |
| rpc package | library | Observed | Groups 1 file(s) under rpc package (observed from repository paths and static analysis). |
| rpc.js package | library | Observed | Groups 1 file(s) under rpc.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). |
| service.js package | library | Observed | Groups 1 file(s) under service.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 161 file(s) under tests (observed from repository paths and static analysis). |
| tokenize.js package | library | Observed | Groups 1 file(s) under tokenize.js package (observed from repository paths and static analysis). |
| type.js package | library | Observed | Groups 1 file(s) under type.js package (observed from repository paths and static analysis). |
| types.js package | library | Observed | Groups 1 file(s) under types.js package (observed from repository paths and static analysis). |
| typescript.js package | library | Observed | Groups 1 file(s) under typescript.js package (observed from repository paths and static analysis). |
| util package | library | Observed | Groups 22 file(s) under util package (observed from repository paths and static analysis). |
| util.js package | library | Observed | Groups 1 file(s) under util.js package (observed from repository paths and static analysis). |
| verifier.js package | library | Observed | Groups 1 file(s) under verifier.js package (observed from repository paths and static analysis). |
| wrappers.js package | library | Observed | Groups 1 file(s) under wrappers.js package (observed from repository paths and static analysis). |
| writer_buffer.js package | library | Observed | Groups 1 file(s) under writer_buffer.js package (observed from repository paths and static analysis). |
| writer.js package | library | Observed | Groups 1 file(s) under writer.js package (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/issue.yml` (config)
- `.github/actions/conformance/action.yml` (config)
- `.github/workflows/release.yaml` (ci)
- `.github/workflows/test.yml` (ci)
- `.release-please-manifest.json` (config)
- `bench/cases/common/bench.json` (config)
- `bench/package.json` (manifest)
- `bench/results/latest.json` (config)
- `cli/lib/tsd-jsdoc.json` (config)
- `cli/package.json` (manifest)
- `config/jsdoc.json` (config)
- `config/tslint.json` (config)
- `google/api/annotations.json` (config)
- `google/api/http.json` (config)
- `google/protobuf/api.json` (config)
- `google/protobuf/compiler/plugin.json` (config)
- `google/protobuf/descriptor.json` (config)
- `google/protobuf/json_enumvalue_options.json` (config)
- `google/protobuf/source_context.json` (config)
- `google/protobuf/type.json` (config)
- `package.json` (manifest)
- `release-please-config.json` (config)
- `renovate.json` (config)
- `tsconfig.json` (config)
- `tsconfig.test-types.json` (config)

## Top-level layout

- `tests` — 161 analysed file(s)
- `src` — 54 analysed file(s)
- `cli` — 40 analysed file(s)
- `bench` — 25 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `google` — 18 analysed file(s)
- `ext` — 16 analysed file(s)
- `lib` — 7 analysed file(s)
- `.github` — 6 analysed file(s)
- `examples` — 5 analysed file(s)
- `scripts` — 5 analysed file(s)
- `config` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `798b4c942cca81a7ae0a2694f28ecd2985d386c9` is the revision these paths and observations refer to.
