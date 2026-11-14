# Project structure: MarsX-dev/floatui

**Analysed commit:** `70824397a5ca6eca3cff1bee37d8a6972d653860`

**Commit reference:** [70824397a5ca6eca3cff1bee37d8a6972d653860](https://github.com/MarsX-dev/floatui/commit/70824397a5ca6eca3cff1bee37d8a6972d653860)

**Tree at this commit:** [MarsX-dev/floatui@70824397a5ca](https://github.com/MarsX-dev/floatui/tree/70824397a5ca6eca3cff1bee37d8a6972d653860)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | MarsX-dev/floatui |
| Description | Beautiful and responsive UI components and templates for React and Vue (soon) with Tailwind CSS. |
| Stars | 3588 |
| Forks | 362 |
| Licence | Other |
| Language | MDX |
| Default branch | main |
| Analysed commit | `70824397a5ca6eca3cff1bee37d8a6972d653860` |
| Retrieved at | 2026-11-14T19:15:13.081047+00:00 |
| Files in this snapshot | 573 |

## Directory tree

```text
.vscode/  (1 files)
  settings.json
app/  (18 files)
  api/  (1 files)
    subscribe/  (1 files)
      … 1 files under this directory
  blog/  (2 files)
    [slug]/  (1 files)
      … 1 files under this directory
    page.tsx
  components/  (3 files)
    [slug]/  (1 files)
      … 1 files under this directory
    layout.tsx
    page.tsx
  demo/  (1 files)
    page.tsx
  license/  (1 files)
    page.tsx
  privacy-policy/  (1 files)
    page.tsx
  sitemap.xml/  (1 files)
    route.tsx
  templates/  (2 files)
    [slug]/  (1 files)
      … 1 files under this directory
    page.tsx
  customize.css
  layout.tsx
  page.tsx
  prismjs-theme.css
  robots.txt
  tailwind.css
components/  (64 files)
  icons/  (13 files)
    IconAlpinejs.tsx
    IconArrowsexpandLeft.tsx
    IconBxCustomize.tsx
    IconGithub.tsx
    IconHTML.tsx
    IconLoading.tsx
    IconPennibLine.tsx
    IconRadix.tsx
    IconRadixVue.tsx
    IconReact.tsx
    IconSvelte.tsx
    IconVue.tsx
    index.ts
  ui/  (43 files)
    Banner/  (1 files)
      … 1 files under this directory
    BgGradient/  (1 files)
      … 1 files under this directory
    BlogCard/  (1 files)
      … 1 files under this directory
    Brand/  (1 files)
      … 1 files under this directory
    Button/  (1 files)
      … 1 files under this directory
    CTA/  (1 files)
      … 1 files under this directory
    CodeBlockContainer/  (1 files)
      … 1 files under this directory
    CodeSwitchBar/  (1 files)
      … 1 files under this directory
    DemoHeader/  (2 files)
      … 2 files under this directory
    Features/  (2 files)
      … 2 files under this directory
    Footer/  (4 files)
      … 4 files under this directory
    Hero/  (2 files)
      … 2 files under this directory
    LinkItem/  (1 files)
      … 1 files under this directory
    Navbar/  (2 files)
      … 2 files under this directory
    Preview/  (2 files)
      … 2 files under this directory
    PreviewSwitch/  (1 files)
      … 1 files under this directory
    Sidebar/  (2 files)
      … 2 files under this directory
    SupportedFrameworks/  (3 files)
      … 3 files under this directory
    SupportedLibraries/  (1 files)
      … 1 files under this directory
    Tabs/  (1 files)
      … 1 files under this directory
    TechStackSwitch/  (1 files)
      … 1 files under this directory
    TemplateCTA/  (4 files)
      … 4 files under this directory
    TemplateCard/  (1 files)
      … 1 files under this directory
    TemplateTechStackGroup/  (1 files)
      … 1 files under this directory
    Button.tsx
    Input.tsx
    Modal.tsx
    NewsletterModal.tsx
    Pagination.tsx
  BlurBackground.tsx
  HeroBgGradient.tsx
  HighlightCodeSeobot.tsx
  LazyMotionWrapper.tsx
  MDXRemoteClient.tsx
  SyntaxHeighlight.tsx
  UsermavenSetup.tsx
  variants.ts
componentsDB/  (198 files)
  404-pages/  (5 files)
    404-pages-1d62afb9a2ef.mdx
    404-pages-708eee4dee17.mdx
    404-pages-7b5bede66a5a.mdx
    404-pages-c9848c731519.mdx
    404-pages-f1893ab05a18.mdx
  alerts/  (10 files)
    alerts-33daaccc81a4.mdx
    alerts-36e2604247e4.mdx
    alerts-390c5560fd91.mdx
    alerts-3d27dee362d8.mdx
    alerts-55b9ab92ee04.mdx
    alerts-65b5b4c38bb2.mdx
    alerts-8d1a64022159.mdx
    alerts-a978a607c455.mdx
    alerts-e6aaeb7bc81e.mdx
    alerts-f055417b0bad.mdx
  authentication/  (7 files)
    authentication-0279bd4dcc2e.mdx
    authentication-2bb4e0e2d823.mdx
    authentication-855af584e04d.mdx
    authentication-ccedb97166eb.mdx
    authentication-e7cb4f182d2b.mdx
    authentication-fa7eb93bd2dc.mdx
    authentication-fff7c32ba871.mdx
  avatars/  (7 files)
    avatars-4dd84fe1128c.mdx
    avatars-5049f63b8118.mdx
    avatars-607a4a2b5277.mdx
    avatars-b8e20075f87f.mdx
    avatars-ca5a7f080a8c.mdx
    avatars-ef97d419a9e5.mdx
    avatars-fc855c570b20.mdx
  banners/  (5 files)
    banners-11f7f6dccd6e.mdx
    banners-2e2d3671c0e4.mdx
    banners-46041cc55332.mdx
    banners-53081c4f88bd.mdx
    banners-8d9e23203788.mdx
  buttons/  (9 files)
    buttons-5fbbbed09f14.mdx
    buttons-60c1afc75839.mdx
    buttons-69b2beb4ac19.mdx
    buttons-a983b34d398a.mdx
    buttons-aa6606ba23eb.mdx
    buttons-b066c674da1a.mdx
    buttons-b77496133191.mdx
    buttons-e68a4d95ea0b.mdx
    buttons-f6e5363f7c55.mdx
  cards/  (8 files)
    cards-061d2f1b44aa.mdx
    cards-3d8d50b659a2.mdx
    cards-547248cd873c.mdx
    cards-7c3fba8fdac8.mdx
    cards-87c624cfe2b7.mdx
    cards-8ea106d2c788.mdx
    cards-903c1360e7a1.mdx
    cards-c787d27b744d.mdx
  contact-sections/  (6 files)
    contact-sections-003dafb73af4.mdx
    contact-sections-43d51106e45f.mdx
    contact-sections-76753a93c670.mdx
    contact-sections-b12dd074a93c.mdx
    contact-sections-ba7f2ec93e91.mdx
    contact-sections-cdaf2076140b.mdx
  context-menus/  (2 files)
    context-menus-423e9edb1d58.mdx
    context-menus-a6712d74dd3d.mdx
  cta-sections/  (9 files)
    cta-sections-1342b0427082.mdx
    cta-sections-2e249de5a055.mdx
    cta-sections-409aef4b3a69.mdx
    cta-sections-41e14d6153a5.mdx
    cta-sections-636e1d3a29de.mdx
    cta-sections-86d95ad05b9c.mdx
    cta-sections-89d412ecb171.mdx
    cta-sections-92e2a79c2046.mdx
    cta-sections-c7b9c2dbbf6a.mdx
  faqs/  (7 files)
    faqs-356f7ea0f73c.mdx
    faqs-79884cc45412.mdx
    faqs-7c1180404b4e.mdx
    faqs-86cc9726a658.mdx
    faqs-889e74f80cc3.mdx
    faqs-9a15d33ef2b1.mdx
    faqs-b513b3100d76.mdx
  feature-sections/  (8 files)
    feature-sections-213e46f0ea1d.mdx
    feature-sections-2f2324b0f00e.mdx
    feature-sections-7cd43fad37ba.mdx
    feature-sections-833f29c8bf32.mdx
    feature-sections-94f8250449f9.mdx
    feature-sections-afa753ebec53.mdx
    feature-sections-cc6a507c2c59.mdx
    feature-sections-f80a7ff2efcf.mdx
  footers/  (6 files)
    footers-0da45f93945f.mdx
    footers-181aeccbae3c.mdx
    footers-3477ba81914f.mdx
    footers-4f697cf07807.mdx
    footers-7adb1d10aa04.mdx
    footers-c68b86ce5cab.mdx
  heroes/  (8 files)
    heroes-40b102808fb4.mdx
    heroes-6424ed2d84bc.mdx
    heroes-799910ad7f15.mdx
    heroes-88a21442bae9.mdx
    heroes-8cbb7080120b.mdx
    heroes-acaa71156254.mdx
    heroes-ce11e6ea7764.mdx
    heroes-e5fdc83c631d.mdx
  inputs/  (11 files)
    inputs-076325d8e787.mdx
    inputs-0abece2c72f5.mdx
    inputs-65adedb2e30a.mdx
    inputs-7b42ef3d3325.mdx
    inputs-97bcab681cbc.mdx
    inputs-9c0928e9bc52.mdx
    inputs-a3ba8df65622.mdx
    inputs-bf0855c269f3.mdx
    inputs-e9e3f04488a4.mdx
    inputs-f28b45e133a6.mdx
    inputs-ff2bb089cf05.mdx
  logo-grid/  (5 files)
    logo-grid-2edeee98b168.mdx
    logo-grid-332c0905193d.mdx
    logo-grid-3f0796669114.mdx
    logo-grid-b149d44095d0.mdx
    logo-grid-b8ad04c3687b.mdx
  modals/  (5 files)
    modals-20821fae4e94.mdx
    modals-309ee3e4092f.mdx
    modals-7137f8a56e6f.mdx
    modals-f0ec64cd480f.mdx
    modals-f34e78b6c647.mdx
  navbars/  (7 files)
    navbars-36483e9519a4.mdx
    navbars-38e9a45102dd.mdx
    navbars-5ec32b832d4e.mdx
    navbars-9a1c9a6ece9c.mdx
    navbars-b54a69f7bab4.mdx
    navbars-d6a3586b937a.mdx
    navbars-fb7b2b1ac194.mdx
  newsletters/  (6 files)
    newsletters-0f3f45dbf6bd.mdx
    newsletters-17b9b4f5c0d1.mdx
    newsletters-27789200531b.mdx
    newsletters-82b1fb03588f.mdx
    newsletters-c6c50b23117d.mdx
    newsletters-ea1c994cea5c.mdx
  paginations/  (4 files)
    paginations-1311e1782604.mdx
    paginations-1e4d4591c1cb.mdx
    paginations-7ba0a8fc0441.mdx
    paginations-dd626f42a498.mdx
  pricing-sections/  (6 files)
    pricing-sections-12db7f5f43a1.mdx
    pricing-sections-4ebb20d66a92.mdx
    pricing-sections-57658d06d0ae.mdx
    pricing-sections-5a219949cdf6.mdx
    pricing-sections-97d1254e5c48.mdx
    pricing-sections-ef544e8e316c.mdx
  radio-groups/  (4 files)
    radio-groups-10e410e23333.mdx
    radio-groups-2a2ede791219.mdx
    radio-groups-6f7c3873442d.mdx
    radio-groups-da29db262e3a.mdx
  section-headers/  (5 files)
    section-headers-0e48b8f61cbf.mdx
    section-headers-1bb6aac58666.mdx
    section-headers-a50f5cf7b48d.mdx
    section-headers-bc6f81d07d99.mdx
    section-headers-cad019ac8b7d.mdx
  select-menus/  (7 files)
    select-menus-3b23bd8a97e1.mdx
    select-menus-6346a9db37da.mdx
    select-menus-757dbb5bff06.mdx
    select-menus-8f8830d17b53.mdx
    select-menus-97760aa45255.mdx
    select-menus-ad8f8006c239.mdx
    select-menus-c864235a7a0a.mdx
  sidebars/  (4 files)
    sidebars-1f142eb36aba.mdx
    sidebars-8d301e81fb4d.mdx
    sidebars-ad4b5210ef57.mdx
    sidebars-f462b4d034da.mdx
  stats/  (6 files)
    stats-107fcab08c89.mdx
    stats-146359b8ee6f.mdx
    stats-37f2976dd0e8.mdx
    stats-5081ec2639f3.mdx
    stats-7f0b9d26569a.mdx
    stats-aa9fbac873a9.mdx
  steps/  (5 files)
    steps-12ae72a1a7d4.mdx
    steps-79a787b6535e.mdx
    steps-7b010f6574f6.mdx
    steps-a9dfb5212762.mdx
    steps-dd28d0306f17.mdx
  tables/  (8 files)
    tables-263cf08c1c36.mdx
    tables-26d85d4a0cc6.mdx
    tables-4fc343d81b73.mdx
    tables-5304dcf25d65.mdx
    tables-7ac34fe1bc83.mdx
    tables-7f4565159e80.mdx
    tables-9513f502a160.mdx
    tables-ee6597e4652c.mdx
  tabs/  (6 files)
    tabs-47e5f52687cd.mdx
    tabs-519ce1885d98.mdx
    tabs-a5e1caa4ba5a.mdx
    tabs-bb5a5023cf65.mdx
    tabs-edec7e621082.mdx
    tabs-ef72b74a807f.mdx
  team-sections/  (6 files)
    team-sections-5097f1bf7638.mdx
    team-sections-55ff68e2a191.mdx
    team-sections-569a052486c0.mdx
    team-sections-5918c241d485.mdx
    team-sections-59fca7b97734.mdx
    team-sections-eb43deb82099.mdx
  testimonials/  (6 files)
    testimonials-534b038c5538.mdx
    testimonials-720e7cffa4c1.mdx
    testimonials-9bfcf6d81808.mdx
    testimonials-a39a1e4c35c3.mdx
    testimonials-dd1b11b8b66b.mdx
    testimonials-f74dfcd40d23.mdx
content/  (2 files)
  intro.mdx
  license.mdx
demo/  (53 files)
  alerts-33daaccc81a4.mdx
  alerts-36e2604247e4.mdx
  alerts-3d27dee362d8.mdx
  alerts-8d1a64022159.mdx
  authentication-0279bd4dcc2e.mdx
  authentication-2bb4e0e2d823.mdx
  authentication-855af584e04d.mdx
  banners-2e2d3671c0e4.mdx
  banners-46041cc55332.mdx
  banners-53081c4f88bd.mdx
  cards-547248cd873c.mdx
  cards-7c3fba8fdac8.mdx
  cards-8ea106d2c788.mdx
  cards-903c1360e7a1.mdx
  contact-sections-003dafb73af4.mdx
  contact-sections-b12dd074a93c.mdx
  contact-sections-cdaf2076140b.mdx
  footers-0da45f93945f.mdx
  footers-181aeccbae3c.mdx
  heroes-40b102808fb4.mdx
  heroes-8cbb7080120b.mdx
  heroes-acaa71156254.mdx
  heroes-ce11e6ea7764.mdx
  inputs-0abece2c72f5.mdx
  … 29 more files
firebase/  (1 files)
  config.ts
posts/  (1 files)
  getting-started.mdx
previewsComponents/  (198 files)
  FUI404PageWithImage.jsx
  FUI404PageWithListOfItems.jsx
  FUI404PageWithLogo.jsx
  FUIAlertDanger.jsx
  FUIAlertDangerWithDescription.jsx
  FUIAlertDangerWithLink.jsx
  FUIAlertInfo.jsx
  FUIAlertInfoLinear.jsx
  FUIAlertInfoWithLink.jsx
  FUIAlertSuccess.jsx
  FUIAlertSuccessWithLink.jsx
  FUIAlertWarning.jsx
  FUIAlertWarningWithBorder.jsx
  FUIAmountInput.jsx
  FUIAmountInputWithSelectInRight.jsx
  FUIAvatarGroupStacked.jsx
  FUIAvatarGroupStackedWithJoinButton.jsx
  FUIAvatarGroupStackedWithText.jsx
  FUIAvatarWithLinkAndButton.jsx
  FUIAvatars.jsx
  FUIAvatarsWithInfo.jsx
  FUIAvatarsWithNotification.jsx
  FUIBannerCentred.jsx
  FUIBannerCentredWithBadge.jsx
  … 174 more files
public/  (14 files)
  icons/  (4 files)
    nextjs.svg
    reactjs.svg
    tailwind.svg
    vuejs.svg
  images/  (3 files)
    fb-icon.svg
    logo.svg
    tw-icon.svg
  feature-cover.svg
  logo-dark.svg
  logo.svg
  robots.txt
  tailwind.css
  tw-output.css
  up-logo.svg
sections/  (1 files)
  sections.json
styles/  (3 files)
  customize.css
  prismjs-theme.css
  tailwind.css
types/  (1 files)
  types.ts
utils/  (3 files)
  mergeTW.ts
  seobot.ts
  supportedFrameworksJSON.ts
viewport/  (3 files)
  components/  (1 files)
    Viewport.tsx
  template/  (1 files)
    index.ts
  index.tsx
.gitignore
CONTRIBUTING.md
LICENSE.md
README.md
componentsNames.ts
metatag.ts
next-env.d.ts
next.config.js
package.json
postcss.config.js
tailwind.config.js
tsconfig.json
```

## Entry points

- [app/blog/[slug]/page.tsx](https://github.com/MarsX-dev/floatui/blob/70824397a5ca6eca3cff1bee37d8a6972d653860/app/blog/%5Bslug%5D/page.tsx)
- [app/blog/page.tsx](https://github.com/MarsX-dev/floatui/blob/70824397a5ca6eca3cff1bee37d8a6972d653860/app/blog/page.tsx)
- [app/components/[slug]/page.tsx](https://github.com/MarsX-dev/floatui/blob/70824397a5ca6eca3cff1bee37d8a6972d653860/app/components/%5Bslug%5D/page.tsx)
- [app/components/page.tsx](https://github.com/MarsX-dev/floatui/blob/70824397a5ca6eca3cff1bee37d8a6972d653860/app/components/page.tsx)
- [app/demo/page.tsx](https://github.com/MarsX-dev/floatui/blob/70824397a5ca6eca3cff1bee37d8a6972d653860/app/demo/page.tsx)
- [app/license/page.tsx](https://github.com/MarsX-dev/floatui/blob/70824397a5ca6eca3cff1bee37d8a6972d653860/app/license/page.tsx)
- [app/page.tsx](https://github.com/MarsX-dev/floatui/blob/70824397a5ca6eca3cff1bee37d8a6972d653860/app/page.tsx)
- [app/privacy-policy/page.tsx](https://github.com/MarsX-dev/floatui/blob/70824397a5ca6eca3cff1bee37d8a6972d653860/app/privacy-policy/page.tsx)
- [app/templates/[slug]/page.tsx](https://github.com/MarsX-dev/floatui/blob/70824397a5ca6eca3cff1bee37d8a6972d653860/app/templates/%5Bslug%5D/page.tsx)
- [app/templates/page.tsx](https://github.com/MarsX-dev/floatui/blob/70824397a5ca6eca3cff1bee37d8a6972d653860/app/templates/page.tsx)
- [components/icons/index.ts](https://github.com/MarsX-dev/floatui/blob/70824397a5ca6eca3cff1bee37d8a6972d653860/components/icons/index.ts)
- [components/ui/BgGradient/index.tsx](https://github.com/MarsX-dev/floatui/blob/70824397a5ca6eca3cff1bee37d8a6972d653860/components/ui/BgGradient/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| app package | library | Observed | Groups 13 file(s) under app package (observed from repository paths and static analysis). |
| components package | library | Observed | Groups 64 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| firebase package | library | Observed | Groups 1 file(s) under firebase package (observed from repository paths and static analysis). |
| previewsComponents package | library | Observed | Groups 198 file(s) under previewscomponents package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 1 file(s) under types package (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 3 file(s) under utils package (observed from repository paths and static analysis). |
| viewport package | library | Observed | Groups 3 file(s) under viewport package (observed from repository paths and static analysis). |

## Important files

- `.vscode/settings.json` (config)
- `package.json` (manifest)
- `sections/sections.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `componentsDB` — 198 analysed file(s)
- `previewsComponents` — 198 analysed file(s)
- `components` — 64 analysed file(s)
- `demo` — 53 analysed file(s)
- `app` — 18 analysed file(s)
- `public` — 14 analysed file(s)
- `(root files)` — 12 analysed file(s)
- `styles` — 3 analysed file(s)
- `utils` — 3 analysed file(s)
- `viewport` — 3 analysed file(s)
- `content` — 2 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `firebase` — 1 analysed file(s)
- `posts` — 1 analysed file(s)
- `sections` — 1 analysed file(s)
- `types` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `70824397a5ca6eca3cff1bee37d8a6972d653860` is the revision these paths and observations refer to.
