# Project structure: facebookarchive/prepack

**Analysed commit:** `5beedbe85bd5b9d2de1264abafbb3b76f8584297`

**Commit reference:** [5beedbe85bd5b9d2de1264abafbb3b76f8584297](https://github.com/facebookarchive/prepack/commit/5beedbe85bd5b9d2de1264abafbb3b76f8584297)

**Tree at this commit:** [facebookarchive/prepack@5beedbe85bd5](https://github.com/facebookarchive/prepack/tree/5beedbe85bd5b9d2de1264abafbb3b76f8584297)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | facebookarchive/prepack |
| Description | A JavaScript bundle optimizer. |
| Stars | 14086 |
| Forks | 409 |
| Licence | Other |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `5beedbe85bd5b9d2de1264abafbb3b76f8584297` |
| Retrieved at | 2026-11-14T19:11:47.133462+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.circleci/  (1 files)
  config.yml
assets/  (5 files)
  PrepackLogo.svg
  PrepackLogoAlt.svg
  PrepackLogoWithText.svg
  PrepackLogoWithTextAlt.svg
  PrepackLogoWithTextOnDark.svg
bin/  (2 files)
  prepack-repl.js
  prepack.js
fb-www/  (1 files)
  README.md
flow-libs/  (2 files)
  vscode-debugadapter.js.flow
  vscode-debugprotocol.js.flow
flow-typed/  (70 files)
  npm/  (70 files)
    @babel/  (18 files)
      … 18 files under this directory
    babel-cli_vx.x.x.js
    babel-core_vx.x.x.js
    babel-eslint_vx.x.x.js
    babel-generator_vx.x.x.js
    babel-helper-function-name_vx.x.x.js
    babel-helper-get-function-arity_vx.x.x.js
    babel-jest_vx.x.x.js
    babel-plugin-jest-hoist_vx.x.x.js
    babel-plugin-transform-class-properties_vx.x.x.js
    babel-plugin-transform-object-rest-spread_vx.x.x.js
    babel-preset-es2015_vx.x.x.js
    babel-preset-react_vx.x.x.js
    babel-template_vx.x.x.js
    babel-traverse_vx.x.x.js
    babel-types_vx.x.x.js
    babylon_vx.x.x.js
    chalk_v1.x.x.js
    eslint-config-kittens_vx.x.x.js
    eslint-plugin-babel_vx.x.x.js
    eslint-plugin-flow-header_vx.x.x.js
    eslint-plugin-flowtype_vx.x.x.js
    eslint-plugin-header_vx.x.x.js
    eslint-plugin-prettier_vx.x.x.js
    eslint_vx.x.x.js
    … 28 more files
fuzzer/  (10 files)
  src/  (7 files)
    execute.js
    gen.js
    overnight.js
    property.js
    report.js
    sample.js
    test.js
  .eslintrc
  .gitignore
  package.json
scripts/  (18 files)
  .eslintrc
  debug-fb-www.js
  detect_bad_deps.js
  generate-sourcemaps-test.js
  instrumentor.js
  lint-config.js
  multi-runner.js
  prettier.js
  publish-gh-pages.sh
  test-error-handler.js
  test-internal-react.js
  test-internal.js
  test-runner.js
  test-sourcemaps.sh
  test-std-in.sh
  test262-filters.yml
  test262-runner.js
  test262.js
src/  (332 files)
  debugger/  (23 files)
    adapter/  (2 files)
      … 2 files under this directory
    common/  (8 files)
      … 8 files under this directory
    mock-ui/  (3 files)
      … 3 files under this directory
    server/  (10 files)
      … 10 files under this directory
  domains/  (3 files)
    TypesDomain.js
    ValuesDomain.js
    index.js
  evaluators/  (57 files)
    ArrayExpression.js
    ArrowFunctionExpression.js
    AssignmentExpression.js
    AwaitExpression.js
    BinaryExpression.js
    BlockStatement.js
    BooleanLiteral.js
    BreakStatement.js
    CallExpression.js
    CatchClause.js
    ClassDeclaration.js
    ClassExpression.js
    ConditionalExpression.js
    ContinueStatement.js
    Directive.js
    DirectiveLiteral.js
    DoExpression.js
    DoWhileStatement.js
    EmptyStatement.js
    ExpressionStatement.js
    File.js
    ForInStatement.js
    ForOfStatement.js
    ForStatement.js
    … 33 more files
  intrinsics/  (111 files)
    common/  (1 files)
      … 1 files under this directory
    dom/  (4 files)
      … 4 files under this directory
    ecma262/  (93 files)
      … 93 files under this directory
    fb-www/  (7 files)
      … 7 files under this directory
    prepack/  (4 files)
      … 4 files under this directory
    react-native/  (1 files)
      … 1 files under this directory
    index.js
  methods/  (28 files)
    abstract.js
    arraybuffer.js
    call.js
    construct.js
    create.js
    date.js
    destructuring.js
    environment.js
    function.js
    generator.js
    get.js
    has.js
    hash.js
    index.js
    integerindexed.js
    integrity.js
    is.js
    iterator.js
    join.js
    json.js
    own.js
    promise.js
    properties.js
    proxy.js
    … 4 more files
  react/  (15 files)
    experimental-server-rendering/  (3 files)
      … 3 files under this directory
    ReactElementSet.js
    ReactEquivalenceSet.js
    ReactPropsSet.js
    branching.js
    components.js
    elements.js
    errors.js
    hoisting.js
    jsx.js
    optimizing.js
    reconcilation.js
    utils.js
  serializer/  (25 files)
    Emitter.js
    GeneratorTree.js
    LazyObjectsSerializer.js
    LoggingTracer.js
    Referentializer.js
    ResidualFunctionInitializers.js
    ResidualFunctionInstantiator.js
    ResidualFunctions.js
    ResidualHeapGraphGenerator.js
    ResidualHeapRefCounter.js
    ResidualHeapSerializer.js
    ResidualHeapValueIdentifiers.js
    ResidualHeapVisitor.js
    ResidualOperationSerializer.js
    ResidualOptimizedFunctions.js
    ResidualReactElementSerializer.js
    ResidualReactElementVisitor.js
    factorify.js
    functions.js
    index.js
    serializer.js
    statistics.js
    types.js
    utils.js
    … 1 more files
  utils/  (26 files)
    ConcreteModelConverter.js
    DebugReproManager.js
    DebugReproPackager.js
    HeapInspector.js
    JSONTokenizer.js
    NameGenerator.js
    PreludeGenerator.js
    ShapeInformation.js
    SourceMapManager.js
    TextPrinter.js
    babelhelpers.js
    errors.js
    flow.js
    generator.js
    internalizer.js
    json.js
    leak.js
    logger.js
    modules.js
    native-to-interp.js
    parse.js
    paths.js
    reachability.js
    simplifier.js
    … 2 more files
  values/  (24 files)
    AbstractObjectValue.js
    AbstractValue.js
    ArgumentsExotic.js
    ArrayValue.js
    BooleanValue.js
    BoundFunctionValue.js
    ConcreteValue.js
    ECMAScriptFunctionValue.js
    ECMAScriptSourceFunctionValue.js
    EmptyValue.js
    FunctionValue.js
    IntegerIndexedExotic.js
    NativeFunctionValue.js
    NullValue.js
    NumberValue.js
    ObjectValue.js
    PrimitiveValue.js
    ProxyValue.js
    StringExotic.js
    StringValue.js
    SymbolValue.js
    UndefinedValue.js
    Value.js
    index.js
  benchmarker.js
  completions.js
  construct_realm.js
  descriptors.js
  environment.js
  errors.js
  globals.js
  initialize-singletons.js
  invariant.js
  options.js
  prepack-cli.js
  prepack-node.js
  prepack-options.js
  prepack-standalone.js
  realm.js
  repl-cli.js
  singletons.js
  statistics.js
  types.js
  utils.js
test/  (344 files)
  error-handler/  (42 files)
    EmptyBuiltInArrayCycle.js
    EmptyBuiltInPropsCycle.js
    FinalObjectCannotBeMutated.js
    InstantRenderArrayOps3.js
    ModifiedObjectPropertyLimitation.js
    PropertyAttributeConflict.js
    Set.js
    abstract-value-check-dup-name-string.js
    bad-functions.js
    binaryExpression.js
    call.js
    call2.js
    class.js
    conditional-return.js
    forInStatement.js
    forOfStatement.js
    in1.js
    in2.js
    instanceof.js
    member.js
    member2.js
    object-assign.js
    objectExpression.js
    objectExpression2.js
    … 18 more files
  react/  (250 files)
    AssignSpread/  (19 files)
      … 19 files under this directory
    ClassComponents/  (15 files)
      … 15 files under this directory
    FBMocks/  (30 files)
      … 30 files under this directory
    FactoryComponents/  (2 files)
      … 2 files under this directory
    FirstRenderOnly/  (24 files)
      … 24 files under this directory
    FunctionalComponents/  (89 files)
      … 89 files under this directory
    ReactDOM/  (1 files)
      … 1 files under this directory
    ReactNative/  (2 files)
      … 2 files under this directory
    Reconciliation/  (26 files)
      … 26 files under this directory
    RenderProps/  (14 files)
      … 14 files under this directory
    ServerRendering/  (3 files)
      … 3 files under this directory
    Throw/  (2 files)
      … 2 files under this directory
    __snapshots__/  (10 files)
      … 10 files under this directory
    AssignSpread-test.js
    ClassComponents-test.js
    FBMocks-test.js
    FactoryComponents-test.js
    FirstRenderOnly-test.js
    FunctionalComponents-test.js
    ReactDOM-test.js
    ReactNative-test.js
    Reconciliation-test.js
    RenderProps-test.js
    ServerRendering-test.js
    Throw-test.js
    setupReactTests.js
  serializer/  (52 files)
    abstract/  (52 files)
      … 52 files under this directory
.eslintignore
.eslintrc
.flowconfig
.gitignore
.gitmodules
.prettierrc
.watchmanconfig
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
PATENTS
README.md
babel.config.js
package.json
```

## Entry points

- [bin/prepack.js](https://github.com/facebookarchive/prepack/blob/5beedbe85bd5b9d2de1264abafbb3b76f8584297/bin/prepack.js)
- [bin/prepack-repl.js](https://github.com/facebookarchive/prepack/blob/5beedbe85bd5b9d2de1264abafbb3b76f8584297/bin/prepack-repl.js)
- [src/domains/index.js](https://github.com/facebookarchive/prepack/blob/5beedbe85bd5b9d2de1264abafbb3b76f8584297/src/domains/index.js)
- [src/evaluators/index.js](https://github.com/facebookarchive/prepack/blob/5beedbe85bd5b9d2de1264abafbb3b76f8584297/src/evaluators/index.js)
- [src/intrinsics/index.js](https://github.com/facebookarchive/prepack/blob/5beedbe85bd5b9d2de1264abafbb3b76f8584297/src/intrinsics/index.js)
- [src/methods/index.js](https://github.com/facebookarchive/prepack/blob/5beedbe85bd5b9d2de1264abafbb3b76f8584297/src/methods/index.js)
- [src/serializer/index.js](https://github.com/facebookarchive/prepack/blob/5beedbe85bd5b9d2de1264abafbb3b76f8584297/src/serializer/index.js)
- [src/values/index.js](https://github.com/facebookarchive/prepack/blob/5beedbe85bd5b9d2de1264abafbb3b76f8584297/src/values/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarker.js package | library | Observed | Groups 1 file(s) under benchmarker.js package (observed from repository paths and static analysis). |
| bin package | library | Observed | Groups 2 file(s) under bin package (observed from repository paths and static analysis). |
| completions.js package | library | Observed | Groups 1 file(s) under completions.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| construct_realm.js package | library | Observed | Groups 1 file(s) under construct_realm.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Inferred | Groups 0 file(s) under data layer (observed from repository paths and static analysis). |
| debugger package | library | Observed | Groups 23 file(s) under debugger package (observed from repository paths and static analysis). |
| descriptors.js package | library | Observed | Groups 1 file(s) under descriptors.js package (observed from repository paths and static analysis). |
| domains package | library | Observed | Groups 3 file(s) under domains package (observed from repository paths and static analysis). |
| environment.js package | library | Observed | Groups 1 file(s) under environment.js package (observed from repository paths and static analysis). |
| errors.js package | library | Observed | Groups 1 file(s) under errors.js package (observed from repository paths and static analysis). |
| evaluators package | library | Observed | Groups 57 file(s) under evaluators package (observed from repository paths and static analysis). |
| flow-typed package | library | Observed | Groups 70 file(s) under flow-typed package (observed from repository paths and static analysis). |
| fuzzer package | library | Observed | Groups 7 file(s) under fuzzer package (observed from repository paths and static analysis). |
| globals.js package | library | Observed | Groups 1 file(s) under globals.js package (observed from repository paths and static analysis). |
| initialize-singletons.js package | library | Observed | Groups 1 file(s) under initialize-singletons.js package (observed from repository paths and static analysis). |
| intrinsics package | library | Observed | Groups 111 file(s) under intrinsics package (observed from repository paths and static analysis). |
| invariant.js package | library | Observed | Groups 1 file(s) under invariant.js package (observed from repository paths and static analysis). |
| methods package | library | Observed | Groups 28 file(s) under methods package (observed from repository paths and static analysis). |
| options.js package | library | Observed | Groups 1 file(s) under options.js package (observed from repository paths and static analysis). |
| prepack-cli.js package | library | Observed | Groups 1 file(s) under prepack-cli.js package (observed from repository paths and static analysis). |
| prepack-node.js package | library | Observed | Groups 1 file(s) under prepack-node.js package (observed from repository paths and static analysis). |
| prepack-options.js package | library | Observed | Groups 1 file(s) under prepack-options.js package (observed from repository paths and static analysis). |
| prepack-standalone.js package | library | Observed | Groups 1 file(s) under prepack-standalone.js package (observed from repository paths and static analysis). |
| react package | library | Observed | Groups 15 file(s) under react package (observed from repository paths and static analysis). |
| realm.js package | library | Observed | Groups 1 file(s) under realm.js package (observed from repository paths and static analysis). |
| repl-cli.js package | library | Observed | Groups 1 file(s) under repl-cli.js package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 16 file(s) under scripts package (observed from repository paths and static analysis). |
| serializer package | library | Observed | Groups 25 file(s) under serializer package (observed from repository paths and static analysis). |
| singletons.js package | library | Observed | Groups 1 file(s) under singletons.js package (observed from repository paths and static analysis). |
| statistics.js package | library | Observed | Groups 1 file(s) under statistics.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 344 file(s) under tests (observed from repository paths and static analysis). |
| types.js package | library | Observed | Groups 1 file(s) under types.js package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 26 file(s) under utils package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |
| values package | library | Observed | Groups 24 file(s) under values package (observed from repository paths and static analysis). |

## Important files

- `.circleci/config.yml` (ci)
- `fuzzer/package.json` (manifest)
- `package.json` (manifest)
- `scripts/test262-filters.yml` (config)

## Top-level layout

- `test` — 344 analysed file(s)
- `src` — 332 analysed file(s)
- `flow-typed` — 70 analysed file(s)
- `scripts` — 18 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `fuzzer` — 10 analysed file(s)
- `assets` — 5 analysed file(s)
- `bin` — 2 analysed file(s)
- `flow-libs` — 2 analysed file(s)
- `.circleci` — 1 analysed file(s)
- `fb-www` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

Commit `5beedbe85bd5b9d2de1264abafbb3b76f8584297` is the revision these paths and observations refer to.
