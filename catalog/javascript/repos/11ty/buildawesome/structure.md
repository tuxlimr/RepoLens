# Project structure: 11ty/buildawesome

**Analysed commit:** `3079645e6c43e5c27b486bbf58faf132f34ab4b0`

**Commit reference:** [3079645e6c43e5c27b486bbf58faf132f34ab4b0](https://github.com/11ty/buildawesome/commit/3079645e6c43e5c27b486bbf58faf132f34ab4b0)

**Tree at this commit:** [11ty/buildawesome@3079645e6c43](https://github.com/11ty/buildawesome/tree/3079645e6c43e5c27b486bbf58faf132f34ab4b0)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | 11ty/buildawesome |
| Description | A simpler site generator. Transforms a directory of templates (of varying types) into HTML. |
| Stars | 20040 |
| Forks | 595 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `3079645e6c43e5c27b486bbf58faf132f34ab4b0` |
| Retrieved at | 2026-11-14T19:11:15.670587+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (9 files)
  ISSUE_TEMPLATE/  (2 files)
    config.yml
    possible-bug.yml
  workflows/  (4 files)
    ci.yml
    codeql.yml
    release.yml
    scorecard.yml
  CODEOWNERS
  dependabot.yml
  opencollective.yml
docs/  (4 files)
  coverage.md
  coverage.njk
  eleventy.coverage.js
  release-instructions.md
packages/  (23 files)
  browser/  (16 files)
    src/  (8 files)
      … 8 files under this directory
    test/  (3 files)
      … 3 files under this directory
    README.md
    generate-bundle.js
    package.json
    update-package-json.js
    vitest.config.js
  build-awesome/  (7 files)
    src/  (3 files)
      … 3 files under this directory
    cmd.js
    package.json
    tsconfig.json
    update-package-json.js
scripts/  (3 files)
  prune-types.js
  release-dryrun.sh
  release.sh
src/  (158 files)
  Adapters/  (16 files)
    Engines/  (6 files)
      … 6 files under this directory
    Packages/  (8 files)
      … 8 files under this directory
    getDefaultConfig.core.js
    getDefaultConfig.js
  Benchmark/  (3 files)
    Benchmark.js
    BenchmarkGroup.js
    BenchmarkManager.js
  Data/  (8 files)
    ComputedData.js
    ComputedDataTemplateString.js
    ConfigurationGlobalData.js
    GlobalDataReads.js
    InternalReads.js
    ResolveConfigurationData.js
    Signals.js
    TemplateData.js
  Engines/  (10 files)
    FrontMatter/  (1 files)
      … 1 files under this directory
    Util/  (1 files)
      … 1 files under this directory
    Custom.js
    Html.js
    JavaScript.js
    Liquid.js
    Markdown.js
    Nunjucks.js
    TemplateEngine.js
    TemplateEngineManager.js
  Errors/  (7 files)
    BaseError.js
    DuplicatePermalinkOutputError.js
    ErrorHandler.js
    ErrorUtil.js
    TemplateContentPrematureUseError.js
    TemplateContentUnrenderedTemplateError.js
    UsingCircularTemplateContentReferenceError.js
  Filters/  (5 files)
    GetCollectionItem.js
    GetCollectionItemIndex.js
    GetLocaleCollectionItem.js
    GetParentDirectory.js
    Url.js
  Plugins/  (8 files)
    HtmlBasePlugin.js
    HtmlRelativeCopyPlugin.js
    I18nPlugin.js
    IdAttributePlugin.js
    InputPathToUrl.js
    Pagination.js
    PreserveClosingTagsPlugin.js
    RenderPlugin.js
  Reporters/  (1 files)
    NdjsonReporter.js
  Util/  (66 files)
    Objects/  (5 files)
      … 5 files under this directory
    PostHtml/  (1 files)
      … 1 files under this directory
    TypeScript/  (1 files)
      … 1 files under this directory
    ArrayUtil.js
    AsyncEventEmitter.js
    Compatibility.js
    ConsoleLogger.js
    DateParse.js
    DebugLogUtil.js
    DirContains.js
    EnvironmentVars.cjs
    EsmResolver.js
    EsmResolverPortAdapter.core.js
    EsmResolverPortAdapter.js
    ExistsCache.js
    FilePathUtil.js
    FileSize.js
    FileSystemUtilities.js
    GetJavaScriptData.js
    Git.js
    GlobMatcher.client.js
    GlobMatcher.js
    GlobRemap.js
    HtmlRelativeCopy.js
    HtmlTransformer.js
    ImportAsFunction.js
    ImportJsonSync.js
    … 35 more files
  Core.js
  CoreFs.js
  CoreMinimal.js
  ExtensionMap.js
  FileSystemSearch.js
  Files.js
  GlobalDependencyMap.js
  LayoutCache.js
  Serve.js
  Template.js
  TemplateBehavior.js
  TemplateCollection.js
  TemplateConfig.js
  TemplateContent.js
  TemplateFileSlug.js
  TemplateGlob.js
  TemplateLayout.js
  TemplateLayoutPathResolver.js
  TemplateMap.js
  TemplatePassthrough.js
  TemplatePassthroughManager.js
  TemplatePermalink.js
  TemplatePipeline.js
  TemplatePreprocessors.js
  … 10 more files
test/  (589 files)
  Util/  (2 files)
    normalizeNewLines.js
    normalizeSeparators.js
  _generated/  (1 files)
    .gitignore
  _issues/  (35 files)
    0/  (3 files)
      … 3 files under this directory
    2100/  (4 files)
      … 4 files under this directory
    2250/  (4 files)
      … 4 files under this directory
    2823/  (3 files)
      … 3 files under this directory
    3697/  (3 files)
      … 3 files under this directory
    3809/  (3 files)
      … 3 files under this directory
    3853/  (1 files)
      … 1 files under this directory
    3854/  (3 files)
      … 3 files under this directory
    3896/  (4 files)
      … 4 files under this directory
    3932/  (3 files)
      … 3 files under this directory
    975/  (4 files)
      … 4 files under this directory
  file-system-search/  (1 files)
    file.txt
  noop/  (1 files)
    .gitkeep
  noop2/  (1 files)
    .gitkeep
  proxy-pagination-globaldata/  (4 files)
    _data/  (1 files)
      … 1 files under this directory
    tmpl.liquid
    tmpl2.njk
    tmpl4.11ty.js
  slugify-filter/  (7 files)
    comma.njk
    multibyte.njk
    slug-number.njk
    slug-options.njk
    slugify-number.njk
    slugify-options.njk
    test.njk
  stubs/  (135 files)
    _data/  (7 files)
      … 7 files under this directory
    _includes/  (37 files)
      … 37 files under this directory
    _layouts/  (1 files)
      … 1 files under this directory
    add-extension/  (2 files)
      … 2 files under this directory
    cfg-cli-sync/  (3 files)
      … 3 files under this directory
    cfg-directories-export/  (2 files)
      … 2 files under this directory
    cfg-directories-export-cjs/  (2 files)
      … 2 files under this directory
    cmd-help-processing/  (1 files)
      … 1 files under this directory
    collection/  (10 files)
      … 10 files under this directory
    collection-layout/  (3 files)
      … 3 files under this directory
    collection-slug/  (2 files)
      … 2 files under this directory
    collection-template/  (3 files)
      … 3 files under this directory
    collection2/  (2 files)
      … 2 files under this directory
    component/  (5 files)
      … 5 files under this directory
    component-async/  (3 files)
      … 3 files under this directory
    custom-frontmatter/  (7 files)
      … 7 files under this directory
    data-cascade/  (2 files)
      … 2 files under this directory
    datafiledoesnotexist/  (1 files)
      … 1 files under this directory
    dates/  (7 files)
      … 7 files under this directory
    .eleventyignore
    2016-02-01-permalinkdate.liquid
    broken-config.cjs
    buffer.11ty.cjs
    class-async-data-fn.11ty.cjs
    class-async-filter.11ty.cjs
    class-async.11ty.cjs
    class-buffer.11ty.cjs
    class-data-filter.11ty.cjs
    class-data-fn-filter.11ty.cjs
    class-data-fn-shorthand.11ty.cjs
    class-data-fn.11ty.cjs
    class-data-permalink-async-fn.11ty.cjs
    class-data-permalink-buffer.11ty.cjs
    class-data-permalink-fn-buffer.11ty.cjs
    class-data-permalink-fn-filter.11ty.cjs
    class-data-permalink-fn.11ty.cjs
    class-data-permalink.11ty.cjs
    class-data.11ty.cjs
    class-filter.11ty.cjs
    class-fns-has-page.11ty.cjs
    class-fns.11ty.cjs
    class-norender.11ty.cjs
    class-with-dep-upstream.js
    … 11 more files
  stubs--to/  (2 files)
    test.md
    test2.liquid
  stubs-1206/  (2 files)
    page1.njk
    page2.njk
  stubs-1242/  (3 files)
    _data/  (2 files)
      … 2 files under this directory
    empty.md
  stubs-1325/  (2 files)
    test.11ty.js
    test.js
  stubs-142/  (1 files)
    index.njk
  stubs-1691/  (3 files)
    _data/  (1 files)
      … 1 files under this directory
    template.data.txt
    template.njk
  stubs-2109/  (1 files)
    _data/  (1 files)
      … 1 files under this directory
  stubs-2145/  (2 files)
    _includes/  (1 files)
      … 1 files under this directory
    test.njk
  stubs-2167/  (1 files)
    paginated.njk
  stubs-2224/  (1 files)
    index.njk
  stubs-2258/  (4 files)
    _includes/  (2 files)
      … 2 files under this directory
    eleventy.config.cjs
    style.scss
  stubs-2258-2830-skip-layouts/  (3 files)
    _includes/  (1 files)
      … 1 files under this directory
    eleventy.config.cjs
    style.scss
  stubs-2261/  (3 files)
    _includes/  (1 files)
      … 1 files under this directory
    eleventy.config.js
    index.njk
  stubs-2367/  (3 files)
    _includes/  (1 files)
      … 1 files under this directory
    templateWithLiquidShortcodeMultipleArguments-template2.liquid
    templateWithLiquidShortcodeMultipleArguments.liquid
  stubs-2602/  (1 files)
    index.njk
  stubs-2634/  (4 files)
    computed/  (1 files)
      … 1 files under this directory
    fallback/  (1 files)
      … 1 files under this directory
    plain/  (1 files)
      … 1 files under this directory
    subtitle/  (1 files)
      … 1 files under this directory
  stubs-2753/  (3 files)
    _data/  (1 files)
      … 1 files under this directory
    page1.njk
    page2.njk
  stubs-2790/  (1 files)
    page.11ty.cjs
  stubs-2851/  (2 files)
    content.njk
    paginated.njk
  stubs-3013/  (12 files)
    html/  (3 files)
      … 3 files under this directory
    liquid/  (3 files)
      … 3 files under this directory
    md/  (3 files)
      … 3 files under this directory
    njk/  (3 files)
      … 3 files under this directory
  stubs-3285/  (1 files)
    src/  (1 files)
      … 1 files under this directory
  stubs-3356/  (1 files)
    .gitkeep
  stubs-337/  (2 files)
    data/  (1 files)
      … 1 files under this directory
    src/  (1 files)
      … 1 files under this directory
  stubs-3543/  (1 files)
    assets/  (1 files)
      … 1 files under this directory
  stubs-3807/  (5 files)
    _layouts/  (2 files)
      … 2 files under this directory
    Issue3807test.js
    eleventy.config.js
    index.md
  stubs-3810/  (3 files)
    _includes/  (1 files)
      … 1 files under this directory
    eleventy.config.js
    index.md
  stubs-3824/  (5 files)
    _includes/  (2 files)
      … 2 files under this directory
    eleventy.config.js
    index.11ty.tsx
    tsconfig-3824.json
  stubs-403/  (3 files)
    _includes/  (1 files)
      … 1 files under this directory
    .eleventyignore
    template.liquid
  stubs-408-sass/  (2 files)
    _code.scss
    style.scss
  stubs-413/  (1 files)
    date-frontmatter.md
  stubs-4311/  (2 files)
    sub/  (2 files)
      … 2 files under this directory
  stubs-434/  (2 files)
    _includes/  (2 files)
      … 2 files under this directory
  stubs-445/  (4 files)
    _includes/  (1 files)
      … 1 files under this directory
    blog/  (2 files)
      … 2 files under this directory
    with-layout.njk
  stubs-475/  (2 files)
    _includes/  (1 files)
      … 1 files under this directory
    transform-layout/  (1 files)
      … 1 files under this directory
  stubs-630/  (18 files)
    _data/  (11 files)
      … 11 files under this directory
    component-yaml/  (7 files)
      … 7 files under this directory
  stubs-670/  (2 files)
    content.njk
    index.njk
  stubs-919/  (3 files)
    test.data.cjs
    test.njk
    test2.njk
  stubs-absolute/  (1 files)
    test.md
  stubs-addglobaldata/  (1 files)
    test.liquid
  stubs-addglobaldata-noop/  (1 files)
    test.txt
  stubs-autocopy/  (1 files)
    .gitkeep
  stubs-base/  (1 files)
    index.njk
  stubs-base-case-sens/  (1 files)
    index.njk
  stubs-circular-layout/  (4 files)
    _includes/  (4 files)
      … 4 files under this directory
  stubs-computed-array/  (1 files)
    test.liquid
  stubs-computed-collections/  (2 files)
    collections.njk
    dog.njk
  stubs-computed-collections-filter/  (2 files)
    collections.njk
    dog.njk
  stubs-computed-dirdata/  (3 files)
    dir/  (3 files)
      … 3 files under this directory
  stubs-computed-global/  (2 files)
    _data/  (1 files)
      … 1 files under this directory
    intermix.njk
  stubs-computed-pagination/  (2 files)
    child.11ty.cjs
    paginated.njk
  stubs-computed-symbolparse/  (2 files)
    test.liquid
    test.njk
  stubs-custom-extension/  (1 files)
    test.js1
  stubs-data-cascade/  (12 files)
    global-versus-layout/  (3 files)
      … 3 files under this directory
    layout-data-files/  (3 files)
      … 3 files under this directory
    layout-versus-dirdatafile/  (3 files)
      … 3 files under this directory
    layout-versus-tmpldatafile/  (3 files)
      … 3 files under this directory
  stubs-data-esm/  (2 files)
    _data/  (2 files)
      … 2 files under this directory
  stubs-dependency-tree/  (3 files)
    child.cjs
    grandchild.cjs
    index.cjs
  stubs-empty/  (1 files)
    .gitkeep
  stubs-empty-json-data/  (1 files)
    _data/  (1 files)
      … 1 files under this directory
  stubs-fancyjs/  (2 files)
    test.11ty.tsx
    test.mdx
  stubs-freeze/  (3 files)
    eleventy/  (1 files)
      … 1 files under this directory
    eleventy-fn/  (1 files)
      … 1 files under this directory
    page/  (1 files)
      … 1 files under this directory
  stubs-global-data-config-api/  (1 files)
    empty.txt
  stubs-global-data-config-api-nested/  (1 files)
    _data/  (1 files)
      … 1 files under this directory
  stubs-i18n/  (4 files)
    en/  (1 files)
      … 1 files under this directory
    en-us/  (1 files)
      … 1 files under this directory
    es/  (1 files)
      … 1 files under this directory
    non-lang-file.njk
  stubs-img-transform/  (4 files)
    ignored.md
    missing-alt.md
    multiple.md
    single.md
  stubs-incremental/  (3 files)
    layout-chain/  (3 files)
      … 3 files under this directory
  stubs-layout-cache/  (4 files)
    _includes/  (2 files)
      … 2 files under this directory
    test.liquid
    test.njk
  stubs-layouts-event/  (4 files)
    _includes/  (3 files)
      … 3 files under this directory
    page.md
  stubs-njk-async/  (1 files)
    _includes/  (1 files)
      … 1 files under this directory
  stubs-pagination-computed-quotes/  (2 files)
    post.liquid
    test.liquid
  stubs-pagination-computed-quotes-njk/  (2 files)
    post.njk
    test.njk
  stubs-pathtourl/  (4 files)
    css.njk
    filter.njk
    tmpl.njk
    transform.njk
  stubs-render-plugin/  (35 files)
    _includes/  (6 files)
      … 6 files under this directory
    11tyjs-file-override.njk
    11tyjs-file.njk
    11tyjs.liquid
    bad-data.njk
    capture-liquid-set.njk
    capture-liquid.njk
    capture-njk.liquid
    data-no-templatelang.liquid
    false.liquid
    liquid-direct.njk
    liquid-eleventy.njk
    liquid-global.njk
    liquid-md.11ty.cjs
    liquid-md.liquid
    liquid-page.liquid
    liquid-page.njk
    liquid.njk
    md.liquid
    njk-eleventy.liquid
    njk-file-not-exist.liquid
    njk-file.liquid
    njk-file.njk
    njk-page.liquid
    nunjucks-frontmatter.njk
    … 5 more files
  stubs-types/  (12 files)
    core-options.ts
    define-config.cjs
    define-config.js
    import-type-root.ts
    import-type-subpath.ts
    jsdoc-import-default.js
    jsdoc-import-tag.js
    jsdoc-param-default.cjs
    jsdoc-param-default.js
    jsdoc-param-root.js
    satisfies.ts
    tsconfig.json
  stubs-virtual/  (2 files)
    .gitkeep
    eleventy.config.js
  stubs-virtual-nowrite/  (1 files)
    .gitkeep
  ArrayUtilTest.js
  BenchmarkTest.js
  BundlePluginTest.js
  CompatibilityTest.js
  ComputedDataTemplateStringTest.js
  ComputedDataTest.js
  ConsoleLoggerTest.js
  ContentPipelineTest.js
  CoreTest-ComputedData.js
  CoreTest-CustomDateParsing.js
  CoreTest-PageData.js
  CoreTest-Preprocessors.js
  CoreTest-Shortcodes.js
  CoreTest-VirtualTemplates.js
  CoreTest.js
  CoreWatchOutputHashesTest.js
  DebugLogUtilTest.js
  DefineConfigTest.js
  DependencyGraphTest.js
  DirContainsTest.js
  EleventyAddGlobalDataTest.js
  EleventyImgTransformTest.js
  EleventyMarkdownTest.js
  EleventyNunjucksTest.js
  … 138 more files
.editorconfig
.git-blame-ignore-revs
.gitignore
.npmignore
.nvmrc
.prettierignore
.prettierrc.json
CODE_OF_CONDUCT.md
LICENSE
README.md
SECURITY.md
cmd.cjs
eslint.config.js
package.json
```

## Entry points

- [src/Core.js](https://github.com/11ty/buildawesome/blob/3079645e6c43e5c27b486bbf58faf132f34ab4b0/src/Core.js)
- [cmd.cjs](https://github.com/11ty/buildawesome/blob/3079645e6c43e5c27b486bbf58faf132f34ab4b0/cmd.cjs)
- [packages/build-awesome/cmd.js](https://github.com/11ty/buildawesome/blob/3079645e6c43e5c27b486bbf58faf132f34ab4b0/packages/build-awesome/cmd.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Benchmark package | library | Observed | Groups 3 file(s) under benchmark package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Core.js package | library | Observed | Groups 1 file(s) under core.js package (observed from repository paths and static analysis). |
| CoreFs.js package | library | Observed | Groups 1 file(s) under corefs.js package (observed from repository paths and static analysis). |
| CoreMinimal.js package | library | Observed | Groups 1 file(s) under coreminimal.js package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 8 file(s) under data layer (observed from repository paths and static analysis). |
| defaultConfig.js package | library | Observed | Groups 1 file(s) under defaultconfig.js package (observed from repository paths and static analysis). |
| defaultConfigExtended.client.js package | library | Observed | Groups 1 file(s) under defaultconfigextended.client.js package (observed from repository paths and static analysis). |
| defaultConfigExtended.js package | library | Observed | Groups 1 file(s) under defaultconfigextended.js package (observed from repository paths and static analysis). |
| Engines package | library | Observed | Groups 10 file(s) under engines package (observed from repository paths and static analysis). |
| Errors package | library | Observed | Groups 7 file(s) under errors package (observed from repository paths and static analysis). |
| ExtensionMap.js package | library | Observed | Groups 1 file(s) under extensionmap.js package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 16 file(s) under external integrations (observed from repository paths and static analysis). |
| Files.js package | library | Observed | Groups 1 file(s) under files.js package (observed from repository paths and static analysis). |
| FileSystemSearch.js package | library | Observed | Groups 1 file(s) under filesystemsearch.js package (observed from repository paths and static analysis). |
| Filters package | library | Observed | Groups 5 file(s) under filters package (observed from repository paths and static analysis). |
| GlobalDependencyMap.js package | library | Observed | Groups 1 file(s) under globaldependencymap.js package (observed from repository paths and static analysis). |
| LayoutCache.js package | library | Observed | Groups 1 file(s) under layoutcache.js package (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 16 file(s) under packages package (observed from repository paths and static analysis). |
| Plugins package | library | Observed | Groups 8 file(s) under plugins package (observed from repository paths and static analysis). |
| Reporters package | library | Observed | Groups 1 file(s) under reporters package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| Serve.js package | library | Observed | Groups 1 file(s) under serve.js package (observed from repository paths and static analysis). |
| Template.js package | library | Observed | Groups 1 file(s) under template.js package (observed from repository paths and static analysis). |
| TemplateBehavior.js package | library | Observed | Groups 1 file(s) under templatebehavior.js package (observed from repository paths and static analysis). |
| TemplateCollection.js package | library | Observed | Groups 1 file(s) under templatecollection.js package (observed from repository paths and static analysis). |
| TemplateConfig.js package | library | Observed | Groups 1 file(s) under templateconfig.js package (observed from repository paths and static analysis). |
| TemplateContent.js package | library | Observed | Groups 1 file(s) under templatecontent.js package (observed from repository paths and static analysis). |
| TemplateFileSlug.js package | library | Observed | Groups 1 file(s) under templatefileslug.js package (observed from repository paths and static analysis). |
| TemplateGlob.js package | library | Observed | Groups 1 file(s) under templateglob.js package (observed from repository paths and static analysis). |
| TemplateLayout.js package | library | Observed | Groups 1 file(s) under templatelayout.js package (observed from repository paths and static analysis). |
| TemplateLayoutPathResolver.js package | library | Observed | Groups 1 file(s) under templatelayoutpathresolver.js package (observed from repository paths and static analysis). |
| TemplateMap.js package | library | Observed | Groups 1 file(s) under templatemap.js package (observed from repository paths and static analysis). |
| TemplatePassthrough.js package | library | Observed | Groups 1 file(s) under templatepassthrough.js package (observed from repository paths and static analysis). |
| TemplatePassthroughManager.js package | library | Observed | Groups 1 file(s) under templatepassthroughmanager.js package (observed from repository paths and static analysis). |
| TemplatePermalink.js package | library | Observed | Groups 1 file(s) under templatepermalink.js package (observed from repository paths and static analysis). |
| TemplatePipeline.js package | library | Observed | Groups 1 file(s) under templatepipeline.js package (observed from repository paths and static analysis). |
| TemplatePreprocessors.js package | library | Observed | Groups 1 file(s) under templatepreprocessors.js package (observed from repository paths and static analysis). |
| TemplateRender.js package | library | Observed | Groups 1 file(s) under templaterender.js package (observed from repository paths and static analysis). |
| TemplateWriter.js package | library | Observed | Groups 1 file(s) under templatewriter.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 592 file(s) under tests (observed from repository paths and static analysis). |
| UserConfig.js package | library | Observed | Groups 1 file(s) under userconfig.js package (observed from repository paths and static analysis). |
| UserConfigExtended.ts package | library | Observed | Groups 1 file(s) under userconfigextended.ts package (observed from repository paths and static analysis). |
| Util package | library | Observed | Groups 65 file(s) under util package (observed from repository paths and static analysis). |
| Watch.js package | library | Observed | Groups 1 file(s) under watch.js package (observed from repository paths and static analysis). |
| WatchQueue.js package | library | Observed | Groups 1 file(s) under watchqueue.js package (observed from repository paths and static analysis). |
| WatchTargets.js package | library | Observed | Groups 1 file(s) under watchtargets.js package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/possible-bug.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/opencollective.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/scorecard.yml` (ci)
- `.prettierrc.json` (config)
- `package.json` (manifest)
- `packages/browser/package.json` (manifest)
- `packages/build-awesome/package.json` (manifest)
- `packages/build-awesome/tsconfig.json` (config)

## Top-level layout

- `test` — 589 analysed file(s)
- `src` — 158 analysed file(s)
- `packages` — 23 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `.github` — 9 analysed file(s)
- `docs` — 4 analysed file(s)
- `scripts` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3079645e6c43e5c27b486bbf58faf132f34ab4b0` is the revision these paths and observations refer to.
