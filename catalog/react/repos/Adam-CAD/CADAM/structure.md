# Project structure: Adam-CAD/CADAM

**Analysed commit:** `e339e3ad85601bb1e23a5ff9c7f33b51ddf602f5`

**Commit reference:** [e339e3ad85601bb1e23a5ff9c7f33b51ddf602f5](https://github.com/Adam-CAD/CADAM/commit/e339e3ad85601bb1e23a5ff9c7f33b51ddf602f5)

**Tree at this commit:** [Adam-CAD/CADAM@e339e3ad8560](https://github.com/Adam-CAD/CADAM/tree/e339e3ad85601bb1e23a5ff9c7f33b51ddf602f5)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Adam-CAD/CADAM |
| Description | CADAM is the open source text-to-CAD web application |
| Stars | 5427 |
| Forks | 670 |
| Licence | GPL-3.0 |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `e339e3ad85601bb1e23a5ff9c7f33b51ddf602f5` |
| Retrieved at | 2026-11-14T19:14:20.962522+00:00 |
| Files in this snapshot | 334 |

## Directory tree

```text
.cursor/  (7 files)
  rules/  (7 files)
    backend-architecture.mdc
    code-style.mdc
    database-workflow.mdc
    deployment-restrictions.mdc
    frontend-architecture.mdc
    project-overview.mdc
    typescript-workflow.mdc
.husky/  (1 files)
  pre-commit
benchmarks/  (28 files)
  01-twisted-hex-vase.md
  01-twisted-hex-vase.scad
  02-knurled-control-knob.md
  02-knurled-control-knob.scad
  03-hex-bolt-and-nut.md
  03-hex-bolt-and-nut.scad
  04-honeycomb-bracket.md
  04-honeycomb-bracket.scad
  05-naca-airfoil-wing.md
  05-naca-airfoil-wing.scad
  06-threaded-jar-and-lid.md
  06-threaded-jar-and-lid.scad
  07-bevel-gear-drive.md
  07-bevel-gear-drive.scad
  08-centrifugal-impeller.md
  08-centrifugal-impeller.scad
  09-herringbone-planetary-gearbox.md
  09-herringbone-planetary-gearbox.scad
  10-radial-aircraft-engine.md
  10-radial-aircraft-engine.scad
  11-turbofan-jet-engine.md
  11-turbofan-jet-engine.scad
  12-axial-turbine-blisk.md
  12-axial-turbine-blisk.scad
  … 4 more files
public/  (7 files)
  adam-logo-full.svg
  adam-logo-pink.svg
  adam-logo.svg
  cadam-icon.svg
  cadam-logo.svg
  fusion.svg
  solidworks.svg
scripts/  (1 files)
  load-prod-snapshot.mjs
shared/  (11 files)
  Tree.ts
  chatAi.ts
  database.ts
  imageRefs.ts
  models.ts
  parametricParts.test.ts
  parametricParts.ts
  parseParameters.ts
  suggestions.test.ts
  suggestions.ts
  types.ts
src/  (241 files)
  assets/  (1 files)
    adam-loading.json
  components/  (110 files)
    ai-elements/  (2 files)
      … 2 files under this directory
    auth/  (4 files)
      … 4 files under this directory
    chat/  (12 files)
      … 12 files under this directory
    history/  (3 files)
      … 3 files under this directory
    icons/  (8 files)
      … 8 files under this directory
    parameter/  (5 files)
      … 5 files under this directory
    ui/  (49 files)
      … 49 files under this directory
    viewer/  (15 files)
      … 15 files under this directory
    ConditionalWrapper.tsx
    CreditsButton.tsx
    FreePlanTrialPill.tsx
    ImageViewer.tsx
    Layout.tsx
    LimitReachedMessage.tsx
    LowPromptsWarningMessage.tsx
    ModelSelector.tsx
    NewProductBanner.tsx
    ProviderLogo.tsx
    Sidebar.tsx
    TextAreaChat.tsx
  config/  (2 files)
    billing.ts
    plan-features.ts
  constants/  (2 files)
    meshConstants.ts
    spinnerVerbs.ts
  contexts/  (8 files)
    AuthContext.tsx
    AuthProvider.tsx
    BlobContext.tsx
    ConversationContext.tsx
    LayoutContext.ts
    MeshFilesContext.tsx
    PostHogProvider.tsx
    SelectedItemsContext.tsx
  hooks/  (16 files)
    use-toast.ts
    useBillingProducts.ts
    useCachedAiChat.ts
    useGlbPreview.ts
    useImageData.ts
    useIsMobile.ts
    useItemSelection.ts
    useLoadingProgress.tsx
    useMediaQuery.ts
    useMeshData.ts
    useModelChange.ts
    useOpenSCAD.ts
    usePreview.ts
    useRequestCancellation.ts
    useSharedSpinnerVerb.ts
    useTokenPacks.ts
  lib/  (8 files)
    OpenSCADError.ts
    WorkspaceFile.ts
    aiMessages.ts
    libraries.ts
    posthog.ts
    ssoAuth.ts
    supabase.ts
    utils.ts
  routes/  (31 files)
    _layout/  (8 files)
      … 8 files under this directory
    api/  (12 files)
      … 12 files under this directory
    __root.tsx
    _layout.tsx
    assets.$.ts
    confirm-email.tsx
    privacy-policy.tsx
    reset-password.tsx
    signin.tsx
    signup-email.tsx
    signup.tsx
    terms-of-service.tsx
    update-password.tsx
  server/  (17 files)
    aiChat.ts
    anthropic.ts
    api.ts
    billingClient.ts
    chatToolPersistence.test.ts
    chatToolPersistence.ts
    deleteUserTeardown.ts
    env.ts
    falWebhook.ts
    imageGen.ts
    mesh.ts
    messageUtils.ts
    modelCapabilities.test.ts
    modelCapabilities.ts
    parseParameter.ts
    serverLog.ts
    supabaseClient.ts
  services/  (5 files)
    api.ts
    conversationService.ts
    messageService.ts
    profileService.ts
    subscriptionService.ts
  types/  (1 files)
    misc.ts
  utils/  (14 files)
    adamLogoVertices.ts
    coloredOffMesh.ts
    downloadUtils.ts
    dxfUtils.ts
    file-utils.ts
    meshPrintProcessUtils.ts
    meshUtils.ts
    offParser.ts
    parameterUtils.ts
    points.frag
    points.vert
    quantize.frag
    shareUtils.ts
    textureExtraction.ts
  views/  (15 files)
    ConversationView.tsx
    EditorView.tsx
    EmailConfirmation.tsx
    ErrorView.tsx
    HistoryView.tsx
    PrivacyPolicyView.tsx
    PromptView.tsx
    ResetPasswordView.tsx
    SettingsView.tsx
    ShareView.tsx
    SignInView.tsx
    SignUpEmailView.tsx
    SignUpView.tsx
    TermsOfServiceView.tsx
    UpdatePasswordView.tsx
  worker/  (5 files)
    openSCAD.ts
    toolWorker.ts
    types.ts
    worker.ts
    workerError.ts
  App.tsx
  client.tsx
  index.css
  routeTree.gen.ts
  router.tsx
  vite-env.d.ts
supabase/  (21 files)
  migrations/  (7 files)
    20250830041942_initialize.sql.sql
    20260302193359_schema_update.sql
    20260303204633_token_payments.sql
    20260419120000_fix_free_tier_token_reset.sql
    20260420000000_unschedule_free_tier_cron.sql
    20260429225347_drop_local_billing_schema.sql
    20260518000000_parametric_ai_sdk_parts.sql
  schemas/  (10 files)
    conversations.sql
    images.sql
    meshes.sql
    messages.sql
    previews.sql
    profile.sql
    prompts.sql
    storage_policies.sql
    triggers.sql
    types.sql
  .gitignore
  config.toml
  deno.json
  seed.sql
.gitignore
.prettierignore
.prettierrc
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
components.json
eslint.config.js
package.json
postcss.config.js
tailwind.config.js
tsconfig.app.json
tsconfig.json
tsconfig.node.json
vercel.json
vite.config.ts
```

## Entry points

- [src/App.tsx](https://github.com/Adam-CAD/CADAM/blob/e339e3ad85601bb1e23a5ff9c7f33b51ddf602f5/src/App.tsx)
- [src/routes/_layout/index.tsx](https://github.com/Adam-CAD/CADAM/blob/e339e3ad85601bb1e23a5ff9c7f33b51ddf602f5/src/routes/_layout/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 46 file(s) under api layer (observed from repository paths and static analysis). |
| App.tsx package | library | Observed | Groups 1 file(s) under app.tsx package (observed from repository paths and static analysis). |
| benchmarks package | library | Observed | Groups 1 file(s) under benchmarks package (observed from repository paths and static analysis). |
| client.tsx package | library | Observed | Groups 1 file(s) under client.tsx package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 109 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 11 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| constants package | library | Observed | Groups 2 file(s) under constants package (observed from repository paths and static analysis). |
| contexts package | library | Observed | Groups 8 file(s) under contexts package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 16 file(s) under hooks package (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 8 file(s) under lib package (observed from repository paths and static analysis). |
| router.tsx package | library | Observed | Groups 1 file(s) under router.tsx package (observed from repository paths and static analysis). |
| routeTree.gen.ts package | library | Observed | Groups 1 file(s) under routetree.gen.ts package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| server package | library | Observed | Groups 17 file(s) under server package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 5 file(s) under service / domain layer (observed from repository paths and static analysis). |
| shared package | library | Observed | Groups 11 file(s) under shared package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 11 file(s) under utils package (observed from repository paths and static analysis). |
| vite-env.d.ts package | library | Observed | Groups 1 file(s) under vite-env.d.ts package (observed from repository paths and static analysis). |
| worker package | library | Observed | Groups 5 file(s) under worker package (observed from repository paths and static analysis). |

## Important files

- `components.json` (config)
- `package.json` (manifest)
- `src/assets/adam-loading.json` (config)
- `supabase/config.toml` (config)
- `supabase/deno.json` (config)
- `tsconfig.app.json` (config)
- `tsconfig.json` (config)
- `tsconfig.node.json` (config)
- `vercel.json` (config)

## Top-level layout

- `src` — 241 analysed file(s)
- `benchmarks` — 28 analysed file(s)
- `supabase` — 21 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `shared` — 11 analysed file(s)
- `.cursor` — 7 analysed file(s)
- `public` — 7 analysed file(s)
- `.husky` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 5 file(s) were skipped during inventory (2 x likely secret file excluded; 3 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e339e3ad85601bb1e23a5ff9c7f33b51ddf602f5` is the revision these paths and observations refer to.
