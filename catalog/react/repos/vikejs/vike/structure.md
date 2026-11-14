# Project structure: vikejs/vike

**Analysed commit:** `50a93575b1ee6c6e37516e7f89a75b664ab7f0da`

**Commit reference:** [50a93575b1ee6c6e37516e7f89a75b664ab7f0da](https://github.com/vikejs/vike/commit/50a93575b1ee6c6e37516e7f89a75b664ab7f0da)

**Tree at this commit:** [vikejs/vike@50a93575b1ee](https://github.com/vikejs/vike/tree/50a93575b1ee6c6e37516e7f89a75b664ab7f0da)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vikejs/vike |
| Description | (Replaces Next.js/Nuxt) 🔨 Build mission-critical applications with stability and development freedom. |
| Stars | 5839 |
| Forks | 398 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `50a93575b1ee6c6e37516e7f89a75b664ab7f0da` |
| Retrieved at | 2026-11-14T19:14:13.453534+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.github/  (44 files)
  ISSUE_TEMPLATE/  (4 files)
    bug.yml
    config.yml
    feature.yml
    polish.yaml
  workflows/  (38 files)
    ci/  (6 files)
      … 6 files under this directory
    sync-github-releases/  (25 files)
      … 25 files under this directory
    ci.yml
    dependabot-automerge.yml
    discord-notification.yml
    format-check.yml
    lint-check.yml
    sync-github-releases.yml
    website-deploy.yml
  FUNDING.yml
  dependabot.yml
docs/  (526 files)
  assets/  (21 files)
    choices-icons/  (12 files)
      … 12 files under this directory
    icons/  (6 files)
      … 6 files under this directory
    logo/  (3 files)
      … 3 files under this directory
  components/  (37 files)
    brands/  (7 files)
      … 7 files under this directory
    Advanced.mdx
    CommunityNote.tsx
    ConfigSpec.css
    ConfigSpec.tsx
    CustomIntegrationWarning.tsx
    DefaultRouting.mdx
    DeprecatedServer.mdx
    Example.tsx
    ExtraWidth.tsx
    Figure.tsx
    HtmlAndClientNote.mdx
    IntegrationHelp.tsx
    JustAMiddlewareLink.tsx
    OnlyHtmlNote.mdx
    RecommendationRouterLibraries.tsx
    ServerJsRecommendation.mdx
    ServerStep.mdx
    StaticSsrIntro.mdx
    TeamQuote.css
    TeamQuote.tsx
    TreeShaking.tsx
    UiFrameworkExtension.tsx
    UseScaffolder.tsx
    UseVikeExtensionUiFramework.tsx
    … 6 more files
  pages/  (445 files)
    AuthJS/  (2 files)
      … 2 files under this directory
    ClientOnly/  (1 files)
      … 1 files under this directory
    Head/  (1 files)
      … 1 files under this directory
    Layout/  (1 files)
      … 1 files under this directory
    Loading/  (3 files)
      … 3 files under this directory
    MDXEditor/  (1 files)
      … 1 files under this directory
    NODE_ENV/  (1 files)
      … 1 files under this directory
    PM2/  (1 files)
      … 1 files under this directory
    Page/  (1 files)
      … 1 files under this directory
    Page-client/  (1 files)
      … 1 files under this directory
    Page-server/  (1 files)
      … 1 files under this directory
    RPC/  (1 files)
      … 1 files under this directory
    RenderErrorPage/  (1 files)
      … 1 files under this directory
    SSR-vs-SPA/  (1 files)
      … 1 files under this directory
    Wrapper/  (1 files)
      … 1 files under this directory
    abort/  (1 files)
      … 1 files under this directory
    active-links/  (1 files)
      … 1 files under this directory
    add/  (1 files)
      … 1 files under this directory
    ai/  (1 files)
      … 1 files under this directory
    angular/  (1 files)
      … 1 files under this directory
    antd/  (1 files)
      … 1 files under this directory
    api/  (1 files)
      … 1 files under this directory
    api-routes/  (1 files)
      … 1 files under this directory
    apollo-graphql/  (1 files)
      … 1 files under this directory
    auth/  (1 files)
      … 1 files under this directory
    aws/  (1 files)
      … 1 files under this directory
    banner/  (10 files)
      … 10 files under this directory
    base-url/  (1 files)
      … 1 files under this directory
    blog/  (6 files)
      … 6 files under this directory
    bodyAttributes/  (1 files)
      … 1 files under this directory
    bodyHtmlBegin/  (1 files)
      … 1 files under this directory
    bodyHtmlEnd/  (1 files)
      … 1 files under this directory
    bootstrap/  (1 files)
      … 1 files under this directory
    broken-npm-package/  (1 files)
      … 1 files under this directory
    build-your-own-framework/  (1 files)
      … 1 files under this directory
    chakra/  (1 files)
      … 1 files under this directory
    cli/  (1 files)
      … 1 files under this directory
    client/  (1 files)
      … 1 files under this directory
    client-routing/  (1 files)
      … 1 files under this directory
    client-runtime-duplicated/  (1 files)
      … 1 files under this directory
    client-runtimes-conflict/  (1 files)
      … 1 files under this directory
    clientHooks/  (1 files)
      … 1 files under this directory
    clientOnly-helper/  (1 files)
      … 1 files under this directory
    clientRouting/  (1 files)
      … 1 files under this directory
    cloudflare/  (2 files)
      … 2 files under this directory
    cloudflare-pages/  (1 files)
      … 1 files under this directory
    common-issues/  (1 files)
      … 1 files under this directory
    compiled/  (1 files)
      … 1 files under this directory
    config/  (1 files)
      … 1 files under this directory
    consulting/  (1 files)
      … 1 files under this directory
    createDevMiddleware/  (1 files)
      … 1 files under this directory
    createPageRenderer/  (1 files)
      … 1 files under this directory
    csp/  (1 files)
      … 1 files under this directory
    css-in-js/  (1 files)
      … 1 files under this directory
    daisyui/  (1 files)
      … 1 files under this directory
    data/  (1 files)
      … 1 files under this directory
    data-fetching/  (1 files)
      … 1 files under this directory
    debug/  (1 files)
      … 1 files under this directory
    deno/  (1 files)
      … 1 files under this directory
    deploy-sync/  (1 files)
      … 1 files under this directory
    description/  (1 files)
      … 1 files under this directory
    disableAutoFullBuild/  (1 files)
      … 1 files under this directory
    doNotPrerender/  (1 files)
      … 1 files under this directory
    docker/  (1 files)
      … 1 files under this directory
    dot-page-dot-client-dot-js/  (2 files)
      … 2 files under this directory
    dot-page-dot-js/  (2 files)
      … 2 files under this directory
    dot-page-dot-route-dot-js/  (2 files)
      … 2 files under this directory
    dot-page-dot-server-dot-js/  (2 files)
      … 2 files under this directory
    edgeone-pages/  (1 files)
      … 1 files under this directory
    effector/  (1 files)
      … 1 files under this directory
    eject/  (1 files)
      … 1 files under this directory
    element-plus/  (1 files)
      … 1 files under this directory
    env/  (1 files)
      … 1 files under this directory
    error/  (2 files)
      … 2 files under this directory
    error-page/  (1 files)
      … 1 files under this directory
    error-tracking/  (1 files)
      … 1 files under this directory
    escapeInject/  (1 files)
      … 1 files under this directory
    exports/  (1 files)
      … 1 files under this directory
    express/  (1 files)
      … 1 files under this directory
    extends/  (1 files)
      … 1 files under this directory
    extension-vs-custom/  (1 files)
      … 1 files under this directory
    extensions/  (1 files)
      … 1 files under this directory
    faq/  (1 files)
      … 1 files under this directory
    fastify/  (1 files)
      … 1 files under this directory
    favicon/  (1 files)
      … 1 files under this directory
    file-env/  (1 files)
      … 1 files under this directory
    file-structure/  (1 files)
      … 1 files under this directory
    filesystem-routing/  (1 files)
      … 1 files under this directory
    filesystemRoutingRoot/  (1 files)
      … 1 files under this directory
    firebase/  (1 files)
      … 1 files under this directory
    force/  (1 files)
      … 1 files under this directory
    free/  (2 files)
      … 2 files under this directory
    getGlobalContext/  (1 files)
      … 1 files under this directory
    getPageContext/  (1 files)
      … 1 files under this directory
    getPageContextClient/  (1 files)
      … 1 files under this directory
    getVikeConfig/  (1 files)
      … 1 files under this directory
    github-pages/  (1 files)
      … 1 files under this directory
    globalContext/  (1 files)
      … 1 files under this directory
    glossary/  (1 files)
      … 1 files under this directory
    graphql/  (1 files)
      … 1 files under this directory
    grommet/  (1 files)
      … 1 files under this directory
    grpc/  (1 files)
      … 1 files under this directory
    guard/  (1 files)
      … 1 files under this directory
    h3/  (1 files)
      … 1 files under this directory
    hapi/  (1 files)
      … 1 files under this directory
    hattip/  (1 files)
      … 1 files under this directory
    head-manual/  (1 files)
      … 1 files under this directory
    head-tags/  (3 files)
      … 3 files under this directory
    headHtmlBegin/  (1 files)
      … 1 files under this directory
    headHtmlEnd/  (1 files)
      … 1 files under this directory
    headers/  (1 files)
      … 1 files under this directory
    headersResponse/  (1 files)
      … 1 files under this directory
    hints/  (1 files)
      … 1 files under this directory
    hono/  (1 files)
      … 1 files under this directory
    hooks/  (3 files)
      … 3 files under this directory
    hooksTimeout/  (1 files)
      … 1 files under this directory
    host/  (1 files)
      … 1 files under this directory
    htmlAttributes/  (1 files)
      … 1 files under this directory
    hydration/  (1 files)
      … 1 files under this directory
    hydration-mismatch/  (1 files)
      … 1 files under this directory
    hydrationCanBeAborted/  (1 files)
      … 1 files under this directory
    i18n/  (1 files)
      … 1 files under this directory
    image/  (1 files)
      … 1 files under this directory
    img/  (1 files)
      … 1 files under this directory
    importBuild-dot-cjs/  (2 files)
      … 2 files under this directory
    importBuild-dot-js/  (2 files)
      … 2 files under this directory
    includeAssetsImportedByServer/  (1 files)
      … 1 files under this directory
    index/  (84 files)
      … 84 files under this directory
    injectAssets/  (1 files)
      … 1 files under this directory
    injectFilter/  (1 files)
      … 1 files under this directory
    injectScriptsAt/  (1 files)
      … 1 files under this directory
    integration/  (1 files)
      … 1 files under this directory
    keepScrollPosition/  (1 files)
      … 1 files under this directory
    koa/  (1 files)
      … 1 files under this directory
    lang/  (1 files)
      … 1 files under this directory
    languages/  (1 files)
      … 1 files under this directory
    lazy-transpiling/  (1 files)
      … 1 files under this directory
    license/  (2 files)
      … 2 files under this directory
    lingui/  (1 files)
      … 1 files under this directory
    managed-hosts/  (1 files)
      … 1 files under this directory
    mantine/  (1 files)
      … 1 files under this directory
    markdown/  (1 files)
      … 1 files under this directory
    meta/  (1 files)
      … 1 files under this directory
    middleware/  (1 files)
      … 1 files under this directory
    migration/  (13 files)
      … 13 files under this directory
    mode/  (1 files)
      … 1 files under this directory
    modifyUrl/  (1 files)
      … 1 files under this directory
    mui/  (1 files)
      … 1 files under this directory
    multiple-renderer/  (1 files)
      … 1 files under this directory
    naive-ui/  (1 files)
      … 1 files under this directory
    navigate/  (1 files)
      … 1 files under this directory
    netlify/  (1 files)
      … 1 files under this directory
    new/  (5 files)
      … 5 files under this directory
    nextjs/  (1 files)
      … 1 files under this directory
    nextui/  (1 files)
      … 1 files under this directory
    nginx/  (1 files)
      … 1 files under this directory
    nitro/  (1 files)
      … 1 files under this directory
    no-side-exports/  (1 files)
      … 1 files under this directory
    onAfterRenderClient/  (1 files)
      … 1 files under this directory
    onAfterRenderHtml/  (1 files)
      … 1 files under this directory
    onBeforePrerenderStart/  (1 files)
      … 1 files under this directory
    onBeforeRender/  (1 files)
      … 1 files under this directory
    onBeforeRender-multiple/  (1 files)
      … 1 files under this directory
    onBeforeRenderClient/  (1 files)
      … 1 files under this directory
    onBeforeRenderHtml/  (1 files)
      … 1 files under this directory
    onBeforeRoute/  (1 files)
      … 1 files under this directory
    onCreateApp/  (1 files)
      … 1 files under this directory
    onCreateGlobalContext/  (1 files)
      … 1 files under this directory
    onCreatePageContext/  (1 files)
      … 1 files under this directory
    onData/  (1 files)
      … 1 files under this directory
    onError/  (1 files)
      … 1 files under this directory
    onHookCall/  (1 files)
      … 1 files under this directory
    onHydrationEnd/  (1 files)
      … 1 files under this directory
    onPageTransitionEnd/  (1 files)
      … 1 files under this directory
    onPageTransitionStart/  (1 files)
      … 1 files under this directory
    onPrerenderStart/  (1 files)
      … 1 files under this directory
    onRenderClient/  (1 files)
      … 1 files under this directory
    onRenderHtml/  (1 files)
      … 1 files under this directory
    pageContext/  (1 files)
      … 1 files under this directory
    pageContext-json/  (2 files)
      … 2 files under this directory
    pageContext-manipulation/  (1 files)
      … 1 files under this directory
    panda-css/  (1 files)
      … 1 files under this directory
    passToClient/  (1 files)
      … 1 files under this directory
    path-aliases/  (1 files)
      … 1 files under this directory
    payload/  (1 files)
      … 1 files under this directory
    photon/  (1 files)
      … 1 files under this directory
    pinia/  (1 files)
      … 1 files under this directory
    port/  (1 files)
      … 1 files under this directory
    pre-rendering/  (2 files)
      … 2 files under this directory
    preact/  (1 files)
      … 1 files under this directory
    precompress/  (1 files)
      … 1 files under this directory
    prefetch/  (1 files)
      … 1 files under this directory
    prefetchStaticAssets/  (1 files)
      … 1 files under this directory
    preloading/  (1 files)
      … 1 files under this directory
    prerender/  (1 files)
      … 1 files under this directory
    press/  (2 files)
      … 2 files under this directory
    pricing/  (7 files)
      … 7 files under this directory
    primereact/  (1 files)
      … 1 files under this directory
    pullstate/  (1 files)
      … 1 files under this directory
    react/  (1 files)
      … 1 files under this directory
    react-router/  (1 files)
      … 1 files under this directory
    react-setting/  (1 files)
      … 1 files under this directory
    react-tour/  (1 files)
      … 1 files under this directory
    reactStrictMode/  (1 files)
      … 1 files under this directory
    redirect/  (1 files)
      … 1 files under this directory
    redirects/  (1 files)
      … 1 files under this directory
    redux/  (1 files)
      … 1 files under this directory
    relay/  (1 files)
      … 1 files under this directory
    releases/  (4 files)
      … 4 files under this directory
    reload/  (1 files)
      … 1 files under this directory
    render/  (1 files)
      … 1 files under this directory
    render-client/  (1 files)
      … 1 files under this directory
    render-hook/  (1 files)
      … 1 files under this directory
    render-modes/  (1 files)
      … 1 files under this directory
    renderPage/  (1 files)
      … 1 files under this directory
    require/  (1 files)
      … 1 files under this directory
    root/  (1 files)
      … 1 files under this directory
    rootAttributes/  (1 files)
      … 1 files under this directory
    route/  (1 files)
      … 1 files under this directory
    route-function/  (1 files)
      … 1 files under this directory
    route-string/  (1 files)
      … 1 files under this directory
    routing/  (1 files)
      … 1 files under this directory
    routing-precedence/  (1 files)
      … 1 files under this directory
    ruby-on-rails/  (1 files)
      … 1 files under this directory
    sass/  (1 files)
      … 1 files under this directory
    self-host/  (1 files)
      … 1 files under this directory
    server/  (1 files)
      … 1 files under this directory
    server-routing/  (1 files)
      … 1 files under this directory
    server-routing-vs-client-routing/  (1 files)
      … 1 files under this directory
    serverEntry/  (1 files)
      … 1 files under this directory
    settings/  (1 files)
      … 1 files under this directory
    socket-io/  (1 files)
      … 1 files under this directory
    solid/  (1 files)
      … 1 files under this directory
    spa/  (1 files)
      … 1 files under this directory
    ssr/  (1 files)
      … 1 files under this directory
    start/  (2 files)
      … 2 files under this directory
    static-directory/  (1 files)
      … 1 files under this directory
    static-hosts/  (1 files)
      … 1 files under this directory
    store/  (1 files)
      … 1 files under this directory
    storybook/  (1 files)
      … 1 files under this directory
    stream/  (1 files)
      … 1 files under this directory
    streaming/  (1 files)
      … 1 files under this directory
    styled-components/  (1 files)
      … 1 files under this directory
    styled-jsx/  (1 files)
      … 1 files under this directory
    svelte/  (1 files)
      … 1 files under this directory
    tRPC/  (1 files)
      … 1 files under this directory
    tailwind-css/  (1 files)
      … 1 files under this directory
    tanstack-query/  (1 files)
      … 1 files under this directory
    tanstack-router/  (1 files)
      … 1 files under this directory
    tauri/  (1 files)
      … 1 files under this directory
    team/  (5 files)
      … 5 files under this directory
    telefunc/  (1 files)
      … 1 files under this directory
    title/  (1 files)
      … 1 files under this directory
    tools/  (1 files)
      … 1 files under this directory
    tour/  (1 files)
      … 1 files under this directory
    typescript/  (1 files)
      … 1 files under this directory
    ui-frameworks/  (1 files)
      … 1 files under this directory
    url-normalization/  (1 files)
      … 1 files under this directory
    urql/  (1 files)
      … 1 files under this directory
    use-cases/  (1 files)
      … 1 files under this directory
    useConfig/  (1 files)
      … 1 files under this directory
    useData/  (1 files)
      … 1 files under this directory
    useHydrated/  (1 files)
      … 1 files under this directory
    usePageContext/  (1 files)
      … 1 files under this directory
    vanjs/  (1 files)
      … 1 files under this directory
    vercel/  (1 files)
      … 1 files under this directory
    versioning/  (1 files)
      … 1 files under this directory
    viewport/  (1 files)
      … 1 files under this directory
    vike-app/  (2 files)
      … 2 files under this directory
    vike-photon/  (6 files)
      … 6 files under this directory
    vike-react/  (1 files)
      … 1 files under this directory
    vike-server/  (1 files)
      … 1 files under this directory
    vike-solid/  (1 files)
      … 1 files under this directory
    vike-vue/  (1 files)
      … 1 files under this directory
    vite-plugin/  (1 files)
      … 1 files under this directory
    vitest/  (1 files)
      … 1 files under this directory
    vue/  (1 files)
      … 1 files under this directory
    vue-i18n/  (1 files)
      … 1 files under this directory
    vue-query/  (1 files)
      … 1 files under this directory
    vue-router/  (1 files)
      … 1 files under this directory
    vue-setting/  (1 files)
      … 1 files under this directory
    vue-tour/  (1 files)
      … 1 files under this directory
    vuetify/  (1 files)
      … 1 files under this directory
    vuex/  (1 files)
      … 1 files under this directory
    warning/  (4 files)
      … 4 files under this directory
    what-is-SSR-and-SPA/  (1 files)
      … 1 files under this directory
    why/  (1 files)
      … 1 files under this directory
    why-the-v1-design/  (1 files)
      … 1 files under this directory
    wsl/  (1 files)
      … 1 files under this directory
  public/  (4 files)
    .nojekyll
    CNAME
    favicon.svg
    llms.txt
  utils/  (1 files)
    checkType.ts
  vite-plugins/  (2 files)
    skillCodeBlockPlugin.ts
    teamJsonPlugin.ts
  +config.ts
  +docpress.tsx
  +redirects.ts
  .gitignore
  .test-dev.test.ts
  .test-e2e.json
  .test-preview.test.ts
  .testRun.ts
  CONTRIBUTING.md
  README.md
  TopNavigation.tsx
  headings.ts
  links.ts
  package.json
  tsconfig.json
  vite.config.ts
examples/  (220 files)
  auth/  (27 files)
    components/  (2 files)
      … 2 files under this directory
    layouts/  (2 files)
      … 2 files under this directory
    pages/  (11 files)
      … 11 files under this directory
    server/  (3 files)
      … 3 files under this directory
    .gitignore
    .test-dev.test.ts
    .test-e2e.json
    .test-prod.test.ts
    .testRun.ts
    README.md
    package.json
    tsconfig.json
    vite.config.ts
  base-url/  (18 files)
    components/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    public/  (1 files)
      … 1 files under this directory
    renderer/  (6 files)
      … 6 files under this directory
    .gitignore
    .test-dev.test.ts
    .test-e2e.json
    .test-preview.test.ts
    .testRun.ts
    README.md
    package.json
    vite.config.js
  base-url-cdn/  (19 files)
    pages/  (2 files)
      … 2 files under this directory
    public/  (1 files)
      … 1 files under this directory
    renderer/  (6 files)
      … 6 files under this directory
    server/  (4 files)
      … 4 files under this directory
    .gitignore
    .test-e2e.json
    .test.ts
    README.md
    package.json
    vite.config.js
  base-url-server/  (21 files)
    components/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    public/  (1 files)
      … 1 files under this directory
    renderer/  (6 files)
      … 6 files under this directory
    server/  (4 files)
      … 4 files under this directory
    .gitignore
    .test-e2e.json
    .test.ts
    README.md
    base.js
    package.json
    vite.config.js
  cloudflare-workers-react/  (21 files)
    pages/  (5 files)
      … 5 files under this directory
    renderer/  (4 files)
      … 4 files under this directory
    worker/  (3 files)
      … 3 files under this directory
    .gitignore
    .test-dev.test.ts
    .test-e2e.json
    .test-wrangler.test.ts
    README.md
    package.json
    tsconfig.json
    vite.config.js
    wrangler.jsonc
  cloudflare-workers-react-full/  (25 files)
    components/  (1 files)
      … 1 files under this directory
    dev-server/  (2 files)
      … 2 files under this directory
    pages/  (3 files)
      … 3 files under this directory
    renderer/  (7 files)
      … 7 files under this directory
    worker/  (3 files)
      … 3 files under this directory
    .gitignore
    .test-dev.test.ts
    .test-e2e.json
    .test-wrangler.test.ts
    .testRun.ts
    README.md
    package.json
    vite.config.ts
    wrangler.jsonc
  cloudflare-workers-vue/  (19 files)
    pages/  (3 files)
      … 3 files under this directory
    renderer/  (5 files)
      … 5 files under this directory
    worker/  (3 files)
      … 3 files under this directory
    .gitignore
    .test-dev.test.ts
    .test-e2e.json
    .test-wrangler.test.ts
    README.md
    package.json
    vite.config.js
    wrangler.jsonc
  custom-preload/  (18 files)
    pages/  (5 files)
      … 5 files under this directory
    renderer/  (6 files)
      … 6 files under this directory
    .gitignore
    .test-e2e.json
    .test-preview.test.ts
    .testRun.ts
    README.md
    package.json
    vite.config.js
  file-structure-domain-driven/  (22 files)
    (marketing)/  (2 files)
      … 2 files under this directory
    auth/  (2 files)
      … 2 files under this directory
    product/  (5 files)
      … 5 files under this directory
    renderer/  (5 files)
      … 5 files under this directory
    .gitignore
    .test-dev.test.ts
    .test-e2e.json
    .test-preview.test.ts
    .testRun.ts
    README.md
    package.json
    vite.config.js
  html-fragments/  (11 files)
    index/  (2 files)
      … 2 files under this directory
    .gitignore
    .test-dev.test.ts
    .test-e2e.json
    .test-preview.test.ts
    .testRun.ts
    README.md
    package.json
    tsconfig.json
    vite.config.js
  i18n/  (18 files)
    components/  (2 files)
      … 2 files under this directory
    locales/  (5 files)
      … 5 files under this directory
    pages/  (4 files)
      … 4 files under this directory
    .gitignore
    .test-dev.test.ts
    .test-e2e.json
    .test-preview.test.ts
    .testRun.ts
    README.md
    package.json
  README.md
.gitignore
.ignore
.prettierrc
AGENTS.md
CLAUDE.md
CONTRIBUTING.md
LICENSE.md
README.md
biome.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/bug.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature.yml` (config)
- `.github/ISSUE_TEMPLATE/polish.yaml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/ci/.gitignore` (ci)
- `.github/workflows/ci/package.json` (ci)
- `.github/workflows/ci/prepare.spec.ts` (ci)
- `.github/workflows/ci/prepare.ts` (ci)
- `.github/workflows/ci/tsconfig.json` (ci)
- `.github/workflows/ci/vitest.config.ts` (ci)
- `.github/workflows/dependabot-automerge.yml` (ci)
- `.github/workflows/discord-notification.yml` (ci)
- `.github/workflows/format-check.yml` (ci)
- `.github/workflows/lint-check.yml` (ci)
- `.github/workflows/sync-github-releases.yml` (ci)
- `.github/workflows/sync-github-releases/README.md` (ci)
- `.github/workflows/sync-github-releases/delete-all.ts` (ci)
- `.github/workflows/sync-github-releases/package.json` (ci)
- `.github/workflows/sync-github-releases/sync.ts` (ci)
- `.github/workflows/sync-github-releases/sync/apply-release-plan.spec.ts` (ci)
- `.github/workflows/sync-github-releases/sync/apply-release-plan.ts` (ci)
- `.github/workflows/sync-github-releases/sync/release-plan.spec.ts` (ci)
- `.github/workflows/sync-github-releases/sync/release-plan.ts` (ci)
- `.github/workflows/sync-github-releases/sync/sync-package.spec.ts` (ci)
- `.github/workflows/sync-github-releases/sync/sync-package.ts` (ci)
- `.github/workflows/sync-github-releases/sync/tag-scheme.spec.ts` (ci)
- `.github/workflows/sync-github-releases/sync/tag-scheme.ts` (ci)
- `.github/workflows/sync-github-releases/tsconfig.json` (ci)
- `.github/workflows/sync-github-releases/utils/changelog-spec-fixtures/changelog-telefunc.md` (ci)
- `.github/workflows/sync-github-releases/utils/changelog-spec-fixtures/changelog-vike-react.md` (ci)
- `.github/workflows/sync-github-releases/utils/changelog-spec-fixtures/changelog-vike-solid.md` (ci)
- `.github/workflows/sync-github-releases/utils/changelog-spec-fixtures/changelog-vike-vue.md` (ci)
- `.github/workflows/sync-github-releases/utils/changelog-spec-fixtures/changelog-vike.md` (ci)
- `.github/workflows/sync-github-releases/utils/changelog.spec.ts` (ci)
- `.github/workflows/sync-github-releases/utils/changelog.ts` (ci)
- `.github/workflows/sync-github-releases/utils/git.spec.ts` (ci)
- `.github/workflows/sync-github-releases/utils/git.ts` (ci)
- `.github/workflows/sync-github-releases/utils/github-env.ts` (ci)
- `.github/workflows/sync-github-releases/utils/github.spec.ts` (ci)
- `.github/workflows/sync-github-releases/utils/github.ts` (ci)
- `.github/workflows/website-deploy.yml` (ci)
- `biome.json` (config)
- `docs/.test-e2e.json` (config)
- `docs/package.json` (manifest)
- `docs/pages/index/sections/Flexibility/_Editor/Tree/files/treeReact.json` (config)
- `docs/tsconfig.json` (config)
- `examples/auth/.test-e2e.json` (config)
- `examples/auth/package.json` (manifest)
- `examples/auth/tsconfig.json` (config)
- `examples/base-url-cdn/.test-e2e.json` (config)
- `examples/base-url-cdn/package.json` (manifest)
- `examples/base-url-cdn/public/manifest.json` (config)
- `examples/base-url-server/.test-e2e.json` (config)
- `examples/base-url-server/package.json` (manifest)
- `examples/base-url-server/public/manifest.json` (config)
- `examples/base-url/.test-e2e.json` (config)
- `examples/base-url/package.json` (manifest)
- `examples/base-url/public/manifest.json` (config)
- `examples/cloudflare-workers-react-full/.test-e2e.json` (config)
- `examples/cloudflare-workers-react-full/package.json` (manifest)
- `examples/cloudflare-workers-react/.test-e2e.json` (config)
- `examples/cloudflare-workers-react/package.json` (manifest)
- `examples/cloudflare-workers-react/tsconfig.json` (config)
- `examples/cloudflare-workers-vue/.test-e2e.json` (config)
- `examples/cloudflare-workers-vue/package.json` (manifest)
- `examples/custom-preload/.test-e2e.json` (config)
- `examples/custom-preload/package.json` (manifest)
- `examples/file-structure-domain-driven/.test-e2e.json` (config)
- `examples/file-structure-domain-driven/package.json` (manifest)
- `examples/html-fragments/.test-e2e.json` (config)
- `examples/html-fragments/package.json` (manifest)
- `examples/html-fragments/tsconfig.json` (config)
- `examples/i18n/.test-e2e.json` (config)
- `examples/i18n/package.json` (manifest)

## Top-level layout

- `docs` — 526 analysed file(s)
- `examples` — 220 analysed file(s)
- `.github` — 44 analysed file(s)
- `(root files)` — 9 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `50a93575b1ee6c6e37516e7f89a75b664ab7f0da` is the revision these paths and observations refer to.
