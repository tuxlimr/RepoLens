# Project structure: mantinedev/ui.mantine.dev

**Analysed commit:** `963b955c5cef4bcc6008d40a0431e46ef771c254`

**Commit reference:** [963b955c5cef4bcc6008d40a0431e46ef771c254](https://github.com/mantinedev/ui.mantine.dev/commit/963b955c5cef4bcc6008d40a0431e46ef771c254)

**Tree at this commit:** [mantinedev/ui.mantine.dev@963b955c5cef](https://github.com/mantinedev/ui.mantine.dev/tree/963b955c5cef4bcc6008d40a0431e46ef771c254)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | mantinedev/ui.mantine.dev |
| Description | Mantine UI website and components |
| Stars | 3946 |
| Forks | 366 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `963b955c5cef4bcc6008d40a0431e46ef771c254` |
| Retrieved at | 2026-11-14T19:14:57.613289+00:00 |
| Files in this snapshot | 732 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    npm_test.yml
.storybook/  (3 files)
  main.ts
  preview-head.html
  preview.tsx
.vscode/  (1 files)
  settings.json
components/  (32 files)
  CategoryHeader/  (2 files)
    CategoryHeader.module.css
    CategoryHeader.tsx
  CategoryPage/  (1 files)
    CategoryPage.tsx
  ChangelogPage/  (2 files)
    ChangelogPage.module.css
    ChangelogPage.tsx
  ComponentCanvas/  (4 files)
    CanvasHeader/  (2 files)
      … 2 files under this directory
    ComponentCanvas.module.css
    ComponentCanvas.tsx
  ComponentPage/  (1 files)
    ComponentPage.tsx
  ComponentPreview/  (1 files)
    ComponentPreview.tsx
  ComponentPreviewControls/  (1 files)
    ComponentPreviewControls.tsx
  GaScript/  (2 files)
    GaScript.tsx
    index.ts
  HomePage/  (8 files)
    Banner/  (3 files)
      … 3 files under this directory
    CategoriesList/  (2 files)
      … 2 files under this directory
    CategoryCard/  (2 files)
      … 2 files under this directory
    HomePage.tsx
  HotKeysHandler/  (2 files)
    HotKeysHandler.tsx
    index.ts
  PageHead/  (2 files)
    PageHead.tsx
    index.ts
  Search/  (2 files)
    Search.tsx
    index.ts
  Shell/  (3 files)
    Shell.module.css
    Shell.tsx
    index.ts
  StoryWrapper/  (1 files)
    StoryWrapper.tsx
data/  (53 files)
  images/  (49 files)
    authentication-dark.svg
    authentication-light.svg
    banners-dark.svg
    banners-light.svg
    buttons-dark.svg
    buttons-light.svg
    cards-dark.svg
    cards-light.svg
    carousels-dark.svg
    carousels-light.svg
    color-scheme-dark.svg
    color-scheme-light.svg
    comments-dark.svg
    comments-light.svg
    contact-dark.svg
    contact-light.svg
    dnd-dark.svg
    dnd-light.svg
    dropzones-dark.svg
    dropzones-light.svg
    error-pages-dark.svg
    error-pages-light.svg
    faq-dark.svg
    faq-light.svg
    … 25 more files
  categories.ts
  components.ts
  index.ts
  types.ts
lib/  (617 files)
  ActionToggle/  (5 files)
    ActionToggle.module.css
    ActionToggle.story.tsx
    ActionToggle.test.tsx
    ActionToggle.tsx
    attributes.json
  ActionsGrid/  (5 files)
    ActionsGrid.module.css
    ActionsGrid.story.tsx
    ActionsGrid.test.tsx
    ActionsGrid.tsx
    attributes.json
  ArticleCard/  (5 files)
    ArticleCard.module.css
    ArticleCard.story.tsx
    ArticleCard.test.tsx
    ArticleCard.tsx
    attributes.json
  ArticleCardFooter/  (5 files)
    ArticleCardFooter.module.css
    ArticleCardFooter.story.tsx
    ArticleCardFooter.test.tsx
    ArticleCardFooter.tsx
    attributes.json
  ArticleCardImage/  (5 files)
    ArticleCardImage.module.css
    ArticleCardImage.story.tsx
    ArticleCardImage.test.tsx
    ArticleCardImage.tsx
    attributes.json
  ArticleCardVertical/  (5 files)
    ArticleCardVertical.module.css
    ArticleCardVertical.story.tsx
    ArticleCardVertical.test.tsx
    ArticleCardVertical.tsx
    attributes.json
  ArticlesCardsGrid/  (5 files)
    ArticlesCardsGrid.module.css
    ArticlesCardsGrid.story.tsx
    ArticlesCardsGrid.test.tsx
    ArticlesCardsGrid.tsx
    attributes.json
  AuthenticationForm/  (6 files)
    AuthenticationForm.story.tsx
    AuthenticationForm.test.tsx
    AuthenticationForm.tsx
    GoogleButton.tsx
    TwitterButton.tsx
    attributes.json
  AuthenticationImage/  (5 files)
    AuthenticationImage.module.css
    AuthenticationImage.story.tsx
    AuthenticationImage.test.tsx
    AuthenticationImage.tsx
    attributes.json
  AuthenticationTitle/  (5 files)
    AuthenticationTitle.module.css
    AuthenticationTitle.story.tsx
    AuthenticationTitle.test.tsx
    AuthenticationTitle.tsx
    attributes.json
  AutocompleteLoading/  (4 files)
    AutocompleteLoading.story.tsx
    AutocompleteLoading.test.tsx
    AutocompleteLoading.tsx
    attributes.json
  BadgeCard/  (5 files)
    BadgeCard.module.css
    BadgeCard.story.tsx
    BadgeCard.test.tsx
    BadgeCard.tsx
    attributes.json
  ButtonCopy/  (4 files)
    ButtonCopy.story.tsx
    ButtonCopy.test.tsx
    ButtonCopy.tsx
    attributes.json
  ButtonMenu/  (4 files)
    ButtonMenu.story.tsx
    ButtonMenu.test.tsx
    ButtonMenu.tsx
    attributes.json
  ButtonProgress/  (5 files)
    ButtonProgress.module.css
    ButtonProgress.story.tsx
    ButtonProgress.test.tsx
    ButtonProgress.tsx
    attributes.json
  CardGradient/  (5 files)
    CardGradient.module.css
    CardGradient.story.tsx
    CardGradient.test.tsx
    CardGradient.tsx
    attributes.json
  CardWithStats/  (5 files)
    CardWithStats.module.css
    CardWithStats.story.tsx
    CardWithStats.test.tsx
    CardWithStats.tsx
    attributes.json
  CardsCarousel/  (5 files)
    CardsCarousel.module.css
    CardsCarousel.story.tsx
    CardsCarousel.test.tsx
    CardsCarousel.tsx
    attributes.json
  CarouselCard/  (5 files)
    CarouselCard.module.css
    CarouselCard.story.tsx
    CarouselCard.test.tsx
    CarouselCard.tsx
    attributes.json
  CheckboxCard/  (5 files)
    CheckboxCard.module.css
    CheckboxCard.story.tsx
    CheckboxCard.test.tsx
    CheckboxCard.tsx
    attributes.json
  CommentHtml/  (5 files)
    CommentHtml.module.css
    CommentHtml.story.tsx
    CommentHtml.test.tsx
    CommentHtml.tsx
    attributes.json
  CommentSimple/  (4 files)
    CommentSimple.story.tsx
    CommentSimple.test.tsx
    CommentSimple.tsx
    attributes.json
  ContactUs/  (7 files)
    ContactIcons.module.css
    ContactIcons.tsx
    ContactUs.module.css
    ContactUs.story.tsx
    ContactUs.test.tsx
    ContactUs.tsx
    attributes.json
  ContainedInputs/  (5 files)
    ContainedInput.module.css
    ContainedInputs.story.tsx
    ContainedInputs.test.tsx
    ContainedInputs.tsx
    attributes.json
  CookiesBanner/  (4 files)
    CookiesBanner.story.tsx
    CookiesBanner.test.tsx
    CookiesBanner.tsx
    attributes.json
  CurrencyInput/  (4 files)
    CurrencyInput.story.tsx
    CurrencyInput.test.tsx
    CurrencyInput.tsx
    attributes.json
  CustomSwitch/  (5 files)
    CustomSwitch.module.css
    CustomSwitch.story.tsx
    CustomSwitch.test.tsx
    CustomSwitch.tsx
    attributes.json
  DndList/  (5 files)
    DndList.module.css
    DndList.story.tsx
    DndList.test.tsx
    DndList.tsx
    attributes.json
  DndListHandle/  (5 files)
    DndListHandle.module.css
    DndListHandle.story.tsx
    DndListHandle.test.tsx
    DndListHandle.tsx
    attributes.json
  DndTable/  (5 files)
    DndTable.module.css
    DndTable.story.tsx
    DndTable.test.tsx
    DndTable.tsx
    attributes.json
  DoubleHeader/  (5 files)
    DoubleHeader.module.css
    DoubleHeader.story.tsx
    DoubleHeader.test.tsx
    DoubleHeader.tsx
    attributes.json
  DoubleNavbar/  (5 files)
    DoubleNavbar.module.css
    DoubleNavbar.story.tsx
    DoubleNavbar.test.tsx
    DoubleNavbar.tsx
    attributes.json
  DropzoneButton/  (5 files)
    DropzoneButton.module.css
    DropzoneButton.story.tsx
    DropzoneButton.test.tsx
    DropzoneButton.tsx
    attributes.json
  EmailBanner/  (6 files)
    EmailBanner.module.css
    EmailBanner.story.tsx
    EmailBanner.test.tsx
    EmailBanner.tsx
    attributes.json
    image.svg
  FaqSimple/  (5 files)
    FaqSimple.module.css
    FaqSimple.story.tsx
    FaqSimple.test.tsx
    FaqSimple.tsx
    attributes.json
  FaqWithBg/  (5 files)
    FaqWithBg.module.css
    FaqWithBg.story.tsx
    FaqWithBg.test.tsx
    FaqWithBg.tsx
    attributes.json
  FaqWithHeader/  (7 files)
    ContactIcons.module.css
    ContactIcons.tsx
    FaqWithHeader.module.css
    FaqWithHeader.story.tsx
    FaqWithHeader.test.tsx
    FaqWithHeader.tsx
    attributes.json
  FaqWithImage/  (6 files)
    FaqWithImage.module.css
    FaqWithImage.story.tsx
    FaqWithImage.test.tsx
    FaqWithImage.tsx
    attributes.json
    image.svg
  FeaturesAsymmetrical/  (5 files)
    FeaturesAsymmetrical.module.css
    FeaturesAsymmetrical.story.tsx
    FeaturesAsymmetrical.test.tsx
    FeaturesAsymmetrical.tsx
    attributes.json
  FeaturesCard/  (5 files)
    FeaturesCard.module.css
    FeaturesCard.story.tsx
    FeaturesCard.test.tsx
    FeaturesCard.tsx
    attributes.json
  FeaturesCards/  (5 files)
    FeaturesCards.module.css
    FeaturesCards.story.tsx
    FeaturesCards.test.tsx
    FeaturesCards.tsx
    attributes.json
  FeaturesGrid/  (5 files)
    FeaturesGrid.module.css
    FeaturesGrid.story.tsx
    FeaturesGrid.test.tsx
    FeaturesGrid.tsx
    attributes.json
  FeaturesImages/  (10 files)
    images/  (5 files)
      … 5 files under this directory
    FeaturesImages.module.css
    FeaturesImages.story.tsx
    FeaturesImages.test.tsx
    FeaturesImages.tsx
    attributes.json
  FeaturesTitle/  (5 files)
    FeaturesTitle.module.css
    FeaturesTitle.story.tsx
    FeaturesTitle.test.tsx
    FeaturesTitle.tsx
    attributes.json
  FloatingLabelInput/  (5 files)
    FloatingLabelInput.module.css
    FloatingLabelInput.story.tsx
    FloatingLabelInput.test.tsx
    FloatingLabelInput.tsx
    attributes.json
  FooterCentered/  (5 files)
    FooterCentered.module.css
    FooterCentered.story.tsx
    FooterCentered.test.tsx
    FooterCentered.tsx
    attributes.json
  FooterLinks/  (5 files)
    FooterLinks.module.css
    FooterLinks.story.tsx
    FooterLinks.test.tsx
    FooterLinks.tsx
    attributes.json
  FooterSimple/  (5 files)
    FooterSimple.module.css
    FooterSimple.story.tsx
    FooterSimple.test.tsx
    FooterSimple.tsx
    attributes.json
  FooterSocial/  (5 files)
    FooterSocial.module.css
    FooterSocial.story.tsx
    FooterSocial.test.tsx
    FooterSocial.tsx
    attributes.json
  ForgotPassword/  (5 files)
    ForgotPassword.module.css
    ForgotPassword.story.tsx
    ForgotPassword.test.tsx
    ForgotPassword.tsx
    attributes.json
  ForgotPasswordInput/  (4 files)
    ForgotPasswordInput.story.tsx
    ForgotPasswordInput.test.tsx
    ForgotPasswordInput.tsx
    attributes.json
  GetInTouch/  (8 files)
    ContactIcons.module.css
    ContactIcons.tsx
    GetInTouch.module.css
    GetInTouch.story.tsx
    GetInTouch.test.tsx
    GetInTouch.tsx
    attributes.json
    bg.svg
  GetInTouchSimple/  (4 files)
    GetInTouchSimple.story.tsx
    GetInTouchSimple.test.tsx
    GetInTouchSimple.tsx
    attributes.json
  GradientSegmentedControl/  (5 files)
    GradientSegmentedControl.module.css
    GradientSegmentedControl.story.tsx
    GradientSegmentedControl.test.tsx
    GradientSegmentedControl.tsx
    attributes.json
  GridAsymmetrical/  (4 files)
    GridAsymmetrical.story.tsx
    GridAsymmetrical.test.tsx
    GridAsymmetrical.tsx
    attributes.json
  HeaderMegaMenu/  (5 files)
    HeaderMegaMenu.module.css
    HeaderMegaMenu.story.tsx
    HeaderMegaMenu.test.tsx
    HeaderMegaMenu.tsx
    attributes.json
  HeaderMenu/  (5 files)
    HeaderMenu.module.css
    HeaderMenu.story.tsx
    HeaderMenu.test.tsx
    HeaderMenu.tsx
    attributes.json
  HeaderSearch/  (5 files)
    HeaderSearch.module.css
    HeaderSearch.story.tsx
    HeaderSearch.test.tsx
    HeaderSearch.tsx
    attributes.json
  HeaderSimple/  (5 files)
    HeaderSimple.module.css
    HeaderSimple.story.tsx
    HeaderSimple.test.tsx
    HeaderSimple.tsx
    attributes.json
  HeaderTabs/  (5 files)
    HeaderTabs.module.css
    HeaderTabs.story.tsx
    HeaderTabs.test.tsx
    HeaderTabs.tsx
    attributes.json
  HeroBullets/  (6 files)
    HeroBullets.module.css
    HeroBullets.story.tsx
    HeroBullets.test.tsx
    HeroBullets.tsx
    attributes.json
    image.svg
  HeroContentLeft/  (5 files)
    HeroContentLeft.module.css
    HeroContentLeft.story.tsx
    HeroContentLeft.test.tsx
    HeroContentLeft.tsx
    attributes.json
  HeroImageBackground/  (5 files)
    HeroImageBackground.module.css
    HeroImageBackground.story.tsx
    HeroImageBackground.test.tsx
    HeroImageBackground.tsx
    attributes.json
  HeroImageRight/  (5 files)
    HeroImageRight.module.css
    HeroImageRight.story.tsx
    HeroImageRight.test.tsx
    HeroImageRight.tsx
    attributes.json
  HeroText/  (6 files)
    Dots.tsx
    HeroText.module.css
    HeroText.story.tsx
    HeroText.test.tsx
    HeroText.tsx
    attributes.json
  HeroTitle/  (5 files)
    HeroTitle.module.css
    HeroTitle.story.tsx
    HeroTitle.test.tsx
    HeroTitle.tsx
    attributes.json
  ImageActionBanner/  (5 files)
    ImageActionBanner.module.css
    ImageActionBanner.story.tsx
    ImageActionBanner.test.tsx
    ImageActionBanner.tsx
    attributes.json
  ImageCard/  (5 files)
    ImageCard.module.css
    ImageCard.story.tsx
    ImageCard.test.tsx
    ImageCard.tsx
    attributes.json
  ImageCheckboxes/  (6 files)
    icons/  (1 files)
      … 1 files under this directory
    ImageCheckboxes.module.css
    ImageCheckboxes.story.tsx
    ImageCheckboxes.test.tsx
    ImageCheckboxes.tsx
    attributes.json
  InputTooltip/  (4 files)
    InputTooltip.story.tsx
    InputTooltip.test.tsx
    InputTooltip.tsx
    attributes.json
  InputValidation/  (5 files)
    InputValidation.module.css
    InputValidation.story.tsx
    InputValidation.test.tsx
    InputValidation.tsx
    attributes.json
  InputWithButton/  (4 files)
    InputWithButton.story.tsx
    InputWithButton.test.tsx
    InputWithButton.tsx
    attributes.json
  LanguagePicker/  (6 files)
    images/  (1 files)
      … 1 files under this directory
    LanguagePicker.module.css
    LanguagePicker.story.tsx
    LanguagePicker.test.tsx
    LanguagePicker.tsx
    attributes.json
  LeadGrid/  (4 files)
    LeadGrid.story.tsx
    LeadGrid.test.tsx
    LeadGrid.tsx
    attributes.json
  NavbarLinksGroup/  (5 files)
    NavbarLinksGroup.module.css
    NavbarLinksGroup.story.tsx
    NavbarLinksGroup.test.tsx
    NavbarLinksGroup.tsx
    attributes.json
  NavbarMinimal/  (5 files)
    NavbarMinimal.module.css
    NavbarMinimal.story.tsx
    NavbarMinimal.test.tsx
    NavbarMinimal.tsx
    attributes.json
  NavbarMinimalColored/  (5 files)
    NavbarMinimalColored.module.css
    NavbarMinimalColored.story.tsx
    NavbarMinimalColored.test.tsx
    NavbarMinimalColored.tsx
    attributes.json
  NavbarNested/  (6 files)
    Logo.tsx
    NavbarNested.module.css
    NavbarNested.story.tsx
    NavbarNested.test.tsx
    NavbarNested.tsx
    attributes.json
  NavbarSearch/  (5 files)
    NavbarSearch.module.css
    NavbarSearch.story.tsx
    NavbarSearch.test.tsx
    NavbarSearch.tsx
    attributes.json
  NavbarSegmented/  (5 files)
    NavbarSegmented.module.css
    NavbarSegmented.story.tsx
    NavbarSegmented.test.tsx
    NavbarSegmented.tsx
    attributes.json
  NavbarSimple/  (5 files)
    NavbarSimple.module.css
    NavbarSimple.story.tsx
    NavbarSimple.test.tsx
    NavbarSimple.tsx
    attributes.json
  NavbarSimpleColored/  (5 files)
    NavbarSimpleColored.module.css
    NavbarSimpleColored.story.tsx
    NavbarSimpleColored.test.tsx
    NavbarSimpleColored.tsx
    attributes.json
  NotFoundImage/  (6 files)
    NotFoundImage.module.css
    NotFoundImage.story.tsx
    NotFoundImage.test.tsx
    NotFoundImage.tsx
    attributes.json
    image.svg
  NotFoundTitle/  (5 files)
    NotFoundTitle.module.css
    NotFoundTitle.story.tsx
    NotFoundTitle.test.tsx
    NotFoundTitle.tsx
    attributes.json
  NothingFoundBackground/  (6 files)
    Illustration.tsx
    NothingFoundBackground.module.css
    NothingFoundBackground.story.tsx
    NothingFoundBackground.test.tsx
    NothingFoundBackground.tsx
    attributes.json
  PasswordStrength/  (4 files)
    PasswordStrength.story.tsx
    PasswordStrength.test.tsx
    PasswordStrength.tsx
    attributes.json
  ProgressCard/  (4 files)
    ProgressCard.story.tsx
    ProgressCard.test.tsx
    ProgressCard.tsx
    attributes.json
  ProgressCardColored/  (5 files)
    ProgressCardColored.module.css
    ProgressCardColored.story.tsx
    ProgressCardColored.test.tsx
    ProgressCardColored.tsx
    attributes.json
  ServerError/  (5 files)
    ServerError.module.css
    ServerError.story.tsx
    ServerError.test.tsx
    ServerError.tsx
    attributes.json
  ServerOverload/  (6 files)
    Illustration.tsx
    ServerOverload.module.css
    ServerOverload.story.tsx
    ServerOverload.test.tsx
    ServerOverload.tsx
    attributes.json
  SliderHover/  (4 files)
    SliderHover.story.tsx
    SliderHover.test.tsx
    SliderHover.tsx
    attributes.json
  SliderIcon/  (4 files)
    SliderIcon.story.tsx
    SliderIcon.test.tsx
    SliderIcon.tsx
    attributes.json
  SliderInput/  (5 files)
    SliderInput.module.css
    SliderInput.story.tsx
    SliderInput.test.tsx
    SliderInput.tsx
    attributes.json
  SliderLabel/  (5 files)
    SliderLabel.module.css
    SliderLabel.story.tsx
    SliderLabel.test.tsx
    SliderLabel.tsx
    attributes.json
  SliderMarks/  (5 files)
    SliderMarks.module.css
    SliderMarks.story.tsx
    SliderMarks.test.tsx
    SliderMarks.tsx
    attributes.json
  SliderWhite/  (5 files)
    SliderWhite.module.css
    SliderWhite.story.tsx
    SliderWhite.test.tsx
    SliderWhite.tsx
    attributes.json
  SocialButtons/  (7 files)
    FacebookIcon.tsx
    GoogleIcon.tsx
    SocialButtons.module.css
    SocialButtons.story.tsx
    SocialButtons.test.tsx
    SocialButtons.tsx
    attributes.json
  SplitButton/  (5 files)
    SplitButton.module.css
    SplitButton.story.tsx
    SplitButton.test.tsx
    SplitButton.tsx
    attributes.json
  StatsCard/  (5 files)
    StatsCard.module.css
    StatsCard.story.tsx
    StatsCard.test.tsx
    StatsCard.tsx
    attributes.json
  StatsControls/  (5 files)
    StatsControls.module.css
    StatsControls.story.tsx
    StatsControls.test.tsx
    StatsControls.tsx
    attributes.json
  StatsGrid/  (5 files)
    StatsGrid.module.css
    StatsGrid.story.tsx
    StatsGrid.test.tsx
    StatsGrid.tsx
    attributes.json
  StatsGridIcons/  (5 files)
    StatsGridIcons.module.css
    StatsGridIcons.story.tsx
    StatsGridIcons.test.tsx
    StatsGridIcons.tsx
    attributes.json
  StatsGroup/  (5 files)
    StatsGroup.module.css
    StatsGroup.story.tsx
    StatsGroup.test.tsx
    StatsGroup.tsx
    attributes.json
  StatsRing/  (4 files)
    StatsRing.story.tsx
    StatsRing.test.tsx
    StatsRing.tsx
    attributes.json
  StatsRingCard/  (5 files)
    StatsRingCard.module.css
    StatsRingCard.story.tsx
    StatsRingCard.test.tsx
    StatsRingCard.tsx
    attributes.json
  StatsSegments/  (5 files)
    StatsSegments.module.css
    StatsSegments.story.tsx
    StatsSegments.test.tsx
    StatsSegments.tsx
    attributes.json
  Subgrid/  (4 files)
    Subgrid.story.tsx
    Subgrid.test.tsx
    Subgrid.tsx
    attributes.json
  SwitchesCard/  (5 files)
    SwitchesCard.module.css
    SwitchesCard.story.tsx
    SwitchesCard.test.tsx
    SwitchesCard.tsx
    attributes.json
  TableOfContents/  (5 files)
    TableOfContents.module.css
    TableOfContents.story.tsx
    TableOfContents.test.tsx
    TableOfContents.tsx
    attributes.json
  TableOfContentsFloating/  (5 files)
    TableOfContentsFloating.module.css
    TableOfContentsFloating.story.tsx
    TableOfContentsFloating.test.tsx
    TableOfContentsFloating.tsx
    attributes.json
  TableReviews/  (5 files)
    TableReviews.module.css
    TableReviews.story.tsx
    TableReviews.test.tsx
    TableReviews.tsx
    attributes.json
  TableScrollArea/  (5 files)
    TableScrollArea.module.css
    TableScrollArea.story.tsx
    TableScrollArea.test.tsx
    TableScrollArea.tsx
    attributes.json
  TableSelection/  (5 files)
    TableSelection.module.css
    TableSelection.story.tsx
    TableSelection.test.tsx
    TableSelection.tsx
    attributes.json
  TableSort/  (5 files)
    TableSort.module.css
    TableSort.story.tsx
    TableSort.test.tsx
    TableSort.tsx
    attributes.json
  TaskCard/  (4 files)
    TaskCard.story.tsx
    TaskCard.test.tsx
    TaskCard.tsx
    attributes.json
  UserButton/  (5 files)
    UserButton.module.css
    UserButton.story.tsx
    UserButton.test.tsx
    UserButton.tsx
    attributes.json
  UserCardImage/  (5 files)
    UserCardImage.module.css
    UserCardImage.story.tsx
    UserCardImage.test.tsx
    UserCardImage.tsx
    attributes.json
  UserInfoAction/  (4 files)
    UserInfoAction.story.tsx
    UserInfoAction.test.tsx
    UserInfoAction.tsx
    attributes.json
  UserInfoIcons/  (5 files)
    UserInfoIcons.module.css
    UserInfoIcons.story.tsx
    UserInfoIcons.test.tsx
    UserInfoIcons.tsx
    attributes.json
  UserMenu/  (4 files)
    UserMenu.story.tsx
    UserMenu.test.tsx
    UserMenu.tsx
    attributes.json
  UsersRolesTable/  (4 files)
    UsersRolesTable.story.tsx
    UsersRolesTable.test.tsx
    UsersRolesTable.tsx
    attributes.json
  UsersStack/  (4 files)
    UsersStack.story.tsx
    UsersStack.test.tsx
    UsersStack.tsx
    attributes.json
  UsersTable/  (4 files)
    UsersTable.story.tsx
    UsersTable.test.tsx
    UsersTable.tsx
    attributes.json
  index.ts
pages/  (6 files)
  category/  (1 files)
    [category].tsx
  changelog/  (1 files)
    [changelog].tsx
  component/  (1 files)
    [component].tsx
  _app.tsx
  _document.tsx
  index.tsx
public/  (1 files)
  favicon.svg
test-utils/  (3 files)
  axe.ts
  index.ts
  render.tsx
.gitignore
.nvmrc
.oxlintrc.json
.yarnrc.yml
LICENCE
README.md
global.d.ts
jest.config.js
jest.setup.js
next.config.mjs
oxfmt.config.mjs
package.json
postcss.config.cjs
renovate.json
tsconfig.json
```

## Entry points

- [.storybook/main.ts](https://github.com/mantinedev/ui.mantine.dev/blob/963b955c5cef4bcc6008d40a0431e46ef771c254/.storybook/main.ts)
- [components/GaScript/index.ts](https://github.com/mantinedev/ui.mantine.dev/blob/963b955c5cef4bcc6008d40a0431e46ef771c254/components/GaScript/index.ts)
- [components/HotKeysHandler/index.ts](https://github.com/mantinedev/ui.mantine.dev/blob/963b955c5cef4bcc6008d40a0431e46ef771c254/components/HotKeysHandler/index.ts)
- [components/PageHead/index.ts](https://github.com/mantinedev/ui.mantine.dev/blob/963b955c5cef4bcc6008d40a0431e46ef771c254/components/PageHead/index.ts)
- [components/Search/index.ts](https://github.com/mantinedev/ui.mantine.dev/blob/963b955c5cef4bcc6008d40a0431e46ef771c254/components/Search/index.ts)
- [components/Shell/index.ts](https://github.com/mantinedev/ui.mantine.dev/blob/963b955c5cef4bcc6008d40a0431e46ef771c254/components/Shell/index.ts)
- [data/images/index.ts](https://github.com/mantinedev/ui.mantine.dev/blob/963b955c5cef4bcc6008d40a0431e46ef771c254/data/images/index.ts)
- [data/index.ts](https://github.com/mantinedev/ui.mantine.dev/blob/963b955c5cef4bcc6008d40a0431e46ef771c254/data/index.ts)
- [lib/FeaturesImages/images/index.ts](https://github.com/mantinedev/ui.mantine.dev/blob/963b955c5cef4bcc6008d40a0431e46ef771c254/lib/FeaturesImages/images/index.ts)
- [lib/ImageCheckboxes/icons/index.ts](https://github.com/mantinedev/ui.mantine.dev/blob/963b955c5cef4bcc6008d40a0431e46ef771c254/lib/ImageCheckboxes/icons/index.ts)
- [lib/LanguagePicker/images/index.ts](https://github.com/mantinedev/ui.mantine.dev/blob/963b955c5cef4bcc6008d40a0431e46ef771c254/lib/LanguagePicker/images/index.ts)
- [lib/index.ts](https://github.com/mantinedev/ui.mantine.dev/blob/963b955c5cef4bcc6008d40a0431e46ef771c254/lib/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| components package | library | Observed | Groups 24 file(s) under components package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 126 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 6 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 5 file(s) under data layer (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 384 file(s) under lib package (observed from repository paths and static analysis). |
| pages package | library | Observed | Groups 6 file(s) under pages package (observed from repository paths and static analysis). |
| test-utils package | library | Observed | Groups 3 file(s) under test-utils package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/npm_test.yml` (ci)
- `.oxlintrc.json` (config)
- `.vscode/settings.json` (config)
- `.yarnrc.yml` (config)
- `lib/ActionToggle/attributes.json` (config)
- `lib/ActionsGrid/attributes.json` (config)
- `lib/ArticleCard/attributes.json` (config)
- `lib/ArticleCardFooter/attributes.json` (config)
- `lib/ArticleCardImage/attributes.json` (config)
- `lib/ArticleCardVertical/attributes.json` (config)
- `lib/ArticlesCardsGrid/attributes.json` (config)
- `lib/AuthenticationForm/attributes.json` (config)
- `lib/AuthenticationImage/attributes.json` (config)
- `lib/AuthenticationTitle/attributes.json` (config)
- `lib/AutocompleteLoading/attributes.json` (config)
- `lib/BadgeCard/attributes.json` (config)
- `lib/ButtonCopy/attributes.json` (config)
- `lib/ButtonMenu/attributes.json` (config)
- `lib/ButtonProgress/attributes.json` (config)
- `lib/CardGradient/attributes.json` (config)
- `lib/CardWithStats/attributes.json` (config)
- `lib/CardsCarousel/attributes.json` (config)
- `lib/CarouselCard/attributes.json` (config)
- `lib/CheckboxCard/attributes.json` (config)
- `lib/CommentHtml/attributes.json` (config)
- `lib/CommentSimple/attributes.json` (config)
- `lib/ContactUs/attributes.json` (config)
- `lib/ContainedInputs/attributes.json` (config)
- `lib/CookiesBanner/attributes.json` (config)
- `lib/CurrencyInput/attributes.json` (config)
- `lib/CustomSwitch/attributes.json` (config)
- `lib/DndList/attributes.json` (config)
- `lib/DndListHandle/attributes.json` (config)
- `lib/DndTable/attributes.json` (config)
- `lib/DoubleHeader/attributes.json` (config)
- `lib/DoubleNavbar/attributes.json` (config)
- `lib/DropzoneButton/attributes.json` (config)
- `lib/EmailBanner/attributes.json` (config)
- `lib/FaqSimple/attributes.json` (config)
- `lib/FaqWithBg/attributes.json` (config)
- `lib/FaqWithHeader/attributes.json` (config)
- `lib/FaqWithImage/attributes.json` (config)
- `lib/FeaturesAsymmetrical/attributes.json` (config)
- `lib/FeaturesCard/attributes.json` (config)
- `lib/FeaturesCards/attributes.json` (config)
- `lib/FeaturesGrid/attributes.json` (config)
- `lib/FeaturesImages/attributes.json` (config)
- `lib/FeaturesTitle/attributes.json` (config)
- `lib/FloatingLabelInput/attributes.json` (config)
- `lib/FooterCentered/attributes.json` (config)
- `lib/FooterLinks/attributes.json` (config)
- `lib/FooterSimple/attributes.json` (config)
- `lib/FooterSocial/attributes.json` (config)
- `lib/ForgotPassword/attributes.json` (config)
- `lib/ForgotPasswordInput/attributes.json` (config)
- `lib/GetInTouch/attributes.json` (config)
- `lib/GetInTouchSimple/attributes.json` (config)
- `lib/GradientSegmentedControl/attributes.json` (config)
- `lib/GridAsymmetrical/attributes.json` (config)
- `lib/HeaderMegaMenu/attributes.json` (config)
- `lib/HeaderMenu/attributes.json` (config)
- `lib/HeaderSearch/attributes.json` (config)
- `lib/HeaderSimple/attributes.json` (config)
- `lib/HeaderTabs/attributes.json` (config)
- `lib/HeroBullets/attributes.json` (config)
- `lib/HeroContentLeft/attributes.json` (config)
- `lib/HeroImageBackground/attributes.json` (config)
- `lib/HeroImageRight/attributes.json` (config)
- `lib/HeroText/attributes.json` (config)
- `lib/HeroTitle/attributes.json` (config)
- `lib/ImageActionBanner/attributes.json` (config)
- `lib/ImageCard/attributes.json` (config)
- `lib/ImageCheckboxes/attributes.json` (config)
- `lib/InputTooltip/attributes.json` (config)
- `lib/InputValidation/attributes.json` (config)
- `lib/InputWithButton/attributes.json` (config)
- `lib/LanguagePicker/attributes.json` (config)
- `lib/LeadGrid/attributes.json` (config)
- `lib/NavbarLinksGroup/attributes.json` (config)
- `lib/NavbarMinimal/attributes.json` (config)
- `lib/NavbarMinimalColored/attributes.json` (config)
- `lib/NavbarNested/attributes.json` (config)
- `lib/NavbarSearch/attributes.json` (config)
- `lib/NavbarSegmented/attributes.json` (config)
- `lib/NavbarSimple/attributes.json` (config)
- `lib/NavbarSimpleColored/attributes.json` (config)
- `lib/NotFoundImage/attributes.json` (config)
- `lib/NotFoundTitle/attributes.json` (config)
- `lib/NothingFoundBackground/attributes.json` (config)
- `lib/PasswordStrength/attributes.json` (config)
- `lib/ProgressCard/attributes.json` (config)
- `lib/ProgressCardColored/attributes.json` (config)
- `lib/ServerError/attributes.json` (config)
- `lib/ServerOverload/attributes.json` (config)
- `lib/SliderHover/attributes.json` (config)
- `lib/SliderIcon/attributes.json` (config)
- `lib/SliderInput/attributes.json` (config)
- `lib/SliderLabel/attributes.json` (config)
- `lib/SliderMarks/attributes.json` (config)
- `lib/SliderWhite/attributes.json` (config)
- `lib/SocialButtons/attributes.json` (config)
- `lib/SplitButton/attributes.json` (config)
- `lib/StatsCard/attributes.json` (config)
- `lib/StatsControls/attributes.json` (config)
- `lib/StatsGrid/attributes.json` (config)
- `lib/StatsGridIcons/attributes.json` (config)
- `lib/StatsGroup/attributes.json` (config)
- `lib/StatsRing/attributes.json` (config)
- `lib/StatsRingCard/attributes.json` (config)
- `lib/StatsSegments/attributes.json` (config)
- `lib/Subgrid/attributes.json` (config)
- `lib/SwitchesCard/attributes.json` (config)
- `lib/TableOfContents/attributes.json` (config)
- `lib/TableOfContentsFloating/attributes.json` (config)
- `lib/TableReviews/attributes.json` (config)
- `lib/TableScrollArea/attributes.json` (config)
- `lib/TableSelection/attributes.json` (config)
- `lib/TableSort/attributes.json` (config)
- `lib/TaskCard/attributes.json` (config)
- `lib/UserButton/attributes.json` (config)
- `lib/UserCardImage/attributes.json` (config)
- `lib/UserInfoAction/attributes.json` (config)
- `lib/UserInfoIcons/attributes.json` (config)
- `lib/UserMenu/attributes.json` (config)
- `lib/UsersRolesTable/attributes.json` (config)
- `lib/UsersStack/attributes.json` (config)
- `lib/UsersTable/attributes.json` (config)
- `package.json` (manifest)
- `renovate.json` (config)
- `tsconfig.json` (config)

## Top-level layout

- `lib` — 617 analysed file(s)
- `data` — 53 analysed file(s)
- `components` — 32 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `pages` — 6 analysed file(s)
- `.storybook` — 3 analysed file(s)
- `test-utils` — 3 analysed file(s)
- `.github` — 1 analysed file(s)
- `.vscode` — 1 analysed file(s)
- `public` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `963b955c5cef4bcc6008d40a0431e46ef771c254` is the revision these paths and observations refer to.
