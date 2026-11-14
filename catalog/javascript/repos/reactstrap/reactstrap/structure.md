# Project structure: reactstrap/reactstrap

**Analysed commit:** `090bc1eeb19bcc269970151d330c6bc03f731635`

**Commit reference:** [090bc1eeb19bcc269970151d330c6bc03f731635](https://github.com/reactstrap/reactstrap/commit/090bc1eeb19bcc269970151d330c6bc03f731635)

**Tree at this commit:** [reactstrap/reactstrap@090bc1eeb19b](https://github.com/reactstrap/reactstrap/tree/090bc1eeb19bcc269970151d330c6bc03f731635)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | reactstrap/reactstrap |
| Description | Simple React Bootstrap 5 components |
| Stars | 10510 |
| Forks | 1276 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `090bc1eeb19bcc269970151d330c6bc03f731635` |
| Retrieved at | 2026-11-14T19:12:38.016862+00:00 |
| Files in this snapshot | 605 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (1 files)
    bug-report.md
  workflows/  (4 files)
    coverage.yml
    docs.yml
    release-please.yml
    test.yml
  FUNDING.yml
  dependabot.yml
.storybook/  (6 files)
  main.cjs
  manager-head.html
  manager.cjs
  preview-head.html
  preview.cjs
  webpack.config.cjs
__mocks__/  (2 files)
  .eslintrc
  react-popper.js
config-overrides/  (2 files)
  index.cjs
  package.json
scripts/  (2 files)
  docs
  tag_release
src/  (198 files)
  __tests__/  (90 files)
    .eslintrc
    Accordion.spec.js
    AccordionBody.spec.js
    AccordionHeader.spec.js
    AccordionItem.spec.js
    Alert.spec.js
    Badge.spec.js
    Breadcrumb.spec.js
    BreadcrumbList.spec.js
    Button.spec.js
    ButtonDropdown.spec.js
    ButtonGroup.spec.js
    ButtonToggle.spec.js
    ButtonToolbar.spec.js
    Card.spec.js
    CardBody.spec.js
    CardColumns.spec.js
    CardDeck.spec.js
    CardFooter.spec.js
    CardGroup.spec.js
    CardHeader.spec.js
    CardImg.spec.js
    CardImgOverlay.spec.js
    CardLink.spec.js
    … 66 more files
  Accordion.js
  AccordionBody.js
  AccordionContext.js
  AccordionHeader.js
  AccordionItem.js
  Alert.js
  Badge.js
  Breadcrumb.js
  BreadcrumbItem.js
  Button.js
  ButtonDropdown.js
  ButtonGroup.js
  ButtonToggle.js
  ButtonToolbar.js
  Card.js
  CardBody.js
  CardColumns.js
  CardDeck.js
  CardFooter.js
  CardGroup.js
  CardHeader.js
  CardImg.js
  CardImgOverlay.js
  CardLink.js
  … 84 more files
static/  (2 files)
  logo-white.svg
  logo.svg
stories/  (274 files)
  examples/  (239 files)
    Accordion/  (8 files)
      … 8 files under this directory
    Alert/  (9 files)
      … 9 files under this directory
    Badge/  (7 files)
      … 7 files under this directory
    Breadcrump/  (3 files)
      … 3 files under this directory
    Button/  (7 files)
      … 7 files under this directory
    ButtonGroup/  (10 files)
      … 10 files under this directory
    Card/  (16 files)
      … 16 files under this directory
    Carousel/  (6 files)
      … 6 files under this directory
    CloseButton/  (4 files)
      … 4 files under this directory
    Collapse/  (7 files)
      … 7 files under this directory
    Dropdown/  (12 files)
      … 12 files under this directory
    Form/  (15 files)
      … 15 files under this directory
    InputGroup/  (6 files)
      … 6 files under this directory
    List/  (4 files)
      … 4 files under this directory
    ListGroup/  (11 files)
      … 11 files under this directory
    Modal/  (21 files)
      … 21 files under this directory
    Nav/  (9 files)
      … 9 files under this directory
    Navbar/  (6 files)
      … 6 files under this directory
    Offcanvas/  (3 files)
      … 3 files under this directory
    Pagination/  (5 files)
      … 5 files under this directory
    Placeholder/  (5 files)
      … 5 files under this directory
    Popover/  (6 files)
      … 6 files under this directory
    Progress/  (9 files)
      … 9 files under this directory
    Spinner/  (8 files)
      … 8 files under this directory
    Table/  (10 files)
      … 10 files under this directory
    Tooltip/  (9 files)
      … 9 files under this directory
    ButtonDropdown.js
    ButtonDropdownMulti.js
    ButtonDropdownMultiSplit.js
    ButtonDropdownUncontrolled.js
    Clearfix.js
    Color.js
    ContainerResponsive.js
    Fade.js
    FadeProps.js
    Layout.js
    LayoutProps.js
    LayoutRowCols.js
    Media.js
    MediaAlignment.js
    MediaList.js
    MediaNested.js
    Props.js
    Toast.js
    ToastDismiss.js
    ToastHeaderIcon.js
    ToastProps.js
    UncontrolledAccordion.js
    options.js
  themes/  (2 files)
    Themes.stories.mdx
    index.js
  .eslintrc.json
  Accordion.stories.js
  Alert.stories.js
  Badge.stories.js
  Breadcrumb.stories.js
  Button.stories.js
  ButtonGroup.stories.js
  Card.stories.js
  Carousel.stories.js
  CloseButton.stories.js
  Collapse.stories.js
  Dropdown.stories.js
  Fade.stories.js
  Forms.stories.js
  GitHub.stories.mdx
  Index.stories.mdx
  InputGroup.stories.js
  Layout.stories.js
  List.stories.js
  ListGroup.stories.js
  Modal.stories.js
  Nav.stories.js
  Navbar.stories.js
  Offcanvas.stories.js
  … 9 more files
types/  (94 files)
  lib/  (90 files)
    Accordion.d.ts
    AccordionBody.d.ts
    AccordionHeader.d.ts
    AccordionItem.d.ts
    Alert.d.ts
    Badge.d.ts
    Breadcrumb.d.ts
    BreadcrumbItem.d.ts
    Button.d.ts
    ButtonDropdown.d.ts
    ButtonGroup.d.ts
    ButtonToggle.d.ts
    ButtonToolbar.d.ts
    Card.d.ts
    CardBody.d.ts
    CardColumns.d.ts
    CardDeck.d.ts
    CardFooter.d.ts
    CardGroup.d.ts
    CardHeader.d.ts
    CardImg.d.ts
    CardImgOverlay.d.ts
    CardLink.d.ts
    CardSubtitle.d.ts
    … 66 more files
  index.d.ts
  reactstrap-tests.tsx
  tsconfig.json
  tslint.json
.eslintignore
.eslintrc.json
.gitignore
.nvmrc
.prettierrc.json
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
ISSUE_TEMPLATE.md
LICENSE
PULL_REQUEST_TEMPLATE.md
README.md
SECURITY.md
babel.build.config.cjs
babel.config.cjs
babel.esm.config.cjs
jest.config.js
package.json
```

## Entry points

- [config-overrides/index.cjs](https://github.com/reactstrap/reactstrap/blob/090bc1eeb19bcc269970151d330c6bc03f731635/config-overrides/index.cjs)
- [src/index.js](https://github.com/reactstrap/reactstrap/blob/090bc1eeb19bcc269970151d330c6bc03f731635/src/index.js)
- [stories/themes/index.js](https://github.com/reactstrap/reactstrap/blob/090bc1eeb19bcc269970151d330c6bc03f731635/stories/themes/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Accordion.js package | library | Observed | Groups 1 file(s) under accordion.js package (observed from repository paths and static analysis). |
| AccordionBody.js package | library | Observed | Groups 1 file(s) under accordionbody.js package (observed from repository paths and static analysis). |
| AccordionContext.js package | library | Observed | Groups 1 file(s) under accordioncontext.js package (observed from repository paths and static analysis). |
| AccordionHeader.js package | library | Observed | Groups 1 file(s) under accordionheader.js package (observed from repository paths and static analysis). |
| AccordionItem.js package | library | Observed | Groups 1 file(s) under accordionitem.js package (observed from repository paths and static analysis). |
| Alert.js package | library | Observed | Groups 1 file(s) under alert.js package (observed from repository paths and static analysis). |
| Badge.js package | library | Observed | Groups 1 file(s) under badge.js package (observed from repository paths and static analysis). |
| Breadcrumb.js package | library | Observed | Groups 1 file(s) under breadcrumb.js package (observed from repository paths and static analysis). |
| BreadcrumbItem.js package | library | Observed | Groups 1 file(s) under breadcrumbitem.js package (observed from repository paths and static analysis). |
| Button.js package | library | Observed | Groups 1 file(s) under button.js package (observed from repository paths and static analysis). |
| ButtonDropdown.js package | library | Observed | Groups 1 file(s) under buttondropdown.js package (observed from repository paths and static analysis). |
| ButtonGroup.js package | library | Observed | Groups 1 file(s) under buttongroup.js package (observed from repository paths and static analysis). |
| ButtonToggle.js package | library | Observed | Groups 1 file(s) under buttontoggle.js package (observed from repository paths and static analysis). |
| ButtonToolbar.js package | library | Observed | Groups 1 file(s) under buttontoolbar.js package (observed from repository paths and static analysis). |
| Card.js package | library | Observed | Groups 1 file(s) under card.js package (observed from repository paths and static analysis). |
| CardBody.js package | library | Observed | Groups 1 file(s) under cardbody.js package (observed from repository paths and static analysis). |
| CardColumns.js package | library | Observed | Groups 1 file(s) under cardcolumns.js package (observed from repository paths and static analysis). |
| CardDeck.js package | library | Observed | Groups 1 file(s) under carddeck.js package (observed from repository paths and static analysis). |
| CardFooter.js package | library | Observed | Groups 1 file(s) under cardfooter.js package (observed from repository paths and static analysis). |
| CardGroup.js package | library | Observed | Groups 1 file(s) under cardgroup.js package (observed from repository paths and static analysis). |
| CardHeader.js package | library | Observed | Groups 1 file(s) under cardheader.js package (observed from repository paths and static analysis). |
| CardImg.js package | library | Observed | Groups 1 file(s) under cardimg.js package (observed from repository paths and static analysis). |
| CardImgOverlay.js package | library | Observed | Groups 1 file(s) under cardimgoverlay.js package (observed from repository paths and static analysis). |
| CardLink.js package | library | Observed | Groups 1 file(s) under cardlink.js package (observed from repository paths and static analysis). |
| CardSubtitle.js package | library | Observed | Groups 1 file(s) under cardsubtitle.js package (observed from repository paths and static analysis). |
| CardText.js package | library | Observed | Groups 1 file(s) under cardtext.js package (observed from repository paths and static analysis). |
| CardTitle.js package | library | Observed | Groups 1 file(s) under cardtitle.js package (observed from repository paths and static analysis). |
| Carousel.js package | library | Observed | Groups 1 file(s) under carousel.js package (observed from repository paths and static analysis). |
| CarouselCaption.js package | library | Observed | Groups 1 file(s) under carouselcaption.js package (observed from repository paths and static analysis). |
| CarouselContext.js package | library | Observed | Groups 1 file(s) under carouselcontext.js package (observed from repository paths and static analysis). |
| CarouselControl.js package | library | Observed | Groups 1 file(s) under carouselcontrol.js package (observed from repository paths and static analysis). |
| CarouselIndicators.js package | library | Observed | Groups 1 file(s) under carouselindicators.js package (observed from repository paths and static analysis). |
| CarouselItem.js package | library | Observed | Groups 1 file(s) under carouselitem.js package (observed from repository paths and static analysis). |
| CloseButton.js package | library | Observed | Groups 1 file(s) under closebutton.js package (observed from repository paths and static analysis). |
| Col.js package | library | Observed | Groups 1 file(s) under col.js package (observed from repository paths and static analysis). |
| Collapse.js package | library | Observed | Groups 1 file(s) under collapse.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| config-overrides package | library | Observed | Groups 1 file(s) under config-overrides package (observed from repository paths and static analysis). |
| Container.js package | library | Observed | Groups 1 file(s) under container.js package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| Dropdown.js package | library | Observed | Groups 1 file(s) under dropdown.js package (observed from repository paths and static analysis). |
| DropdownContext.js package | library | Observed | Groups 1 file(s) under dropdowncontext.js package (observed from repository paths and static analysis). |
| DropdownItem.js package | library | Observed | Groups 1 file(s) under dropdownitem.js package (observed from repository paths and static analysis). |
| DropdownMenu.js package | library | Observed | Groups 1 file(s) under dropdownmenu.js package (observed from repository paths and static analysis). |
| DropdownToggle.js package | library | Observed | Groups 1 file(s) under dropdowntoggle.js package (observed from repository paths and static analysis). |
| Fade.js package | library | Observed | Groups 1 file(s) under fade.js package (observed from repository paths and static analysis). |
| Form.js package | library | Observed | Groups 1 file(s) under form.js package (observed from repository paths and static analysis). |
| FormFeedback.js package | library | Observed | Groups 1 file(s) under formfeedback.js package (observed from repository paths and static analysis). |
| FormGroup.js package | library | Observed | Groups 1 file(s) under formgroup.js package (observed from repository paths and static analysis). |
| FormText.js package | library | Observed | Groups 1 file(s) under formtext.js package (observed from repository paths and static analysis). |
| index.js package | library | Observed | Groups 1 file(s) under index.js package (observed from repository paths and static analysis). |
| Input.js package | library | Observed | Groups 1 file(s) under input.js package (observed from repository paths and static analysis). |
| InputGroup.js package | library | Observed | Groups 1 file(s) under inputgroup.js package (observed from repository paths and static analysis). |
| InputGroupContext.js package | library | Observed | Groups 1 file(s) under inputgroupcontext.js package (observed from repository paths and static analysis). |
| InputGroupText.js package | library | Observed | Groups 1 file(s) under inputgrouptext.js package (observed from repository paths and static analysis). |
| Label.js package | library | Observed | Groups 1 file(s) under label.js package (observed from repository paths and static analysis). |
| List.js package | library | Observed | Groups 1 file(s) under list.js package (observed from repository paths and static analysis). |
| ListGroup.js package | library | Observed | Groups 1 file(s) under listgroup.js package (observed from repository paths and static analysis). |
| ListGroupItem.js package | library | Observed | Groups 1 file(s) under listgroupitem.js package (observed from repository paths and static analysis). |
| ListGroupItemHeading.js package | library | Observed | Groups 1 file(s) under listgroupitemheading.js package (observed from repository paths and static analysis). |
| ListGroupItemText.js package | library | Observed | Groups 1 file(s) under listgroupitemtext.js package (observed from repository paths and static analysis). |
| ListInlineItem.js package | library | Observed | Groups 1 file(s) under listinlineitem.js package (observed from repository paths and static analysis). |
| Media.js package | library | Observed | Groups 1 file(s) under media.js package (observed from repository paths and static analysis). |
| __mocks__ package | library | Observed | Groups 1 file(s) under __mocks__ package (observed from repository paths and static analysis). |
| Modal.js package | library | Observed | Groups 1 file(s) under modal.js package (observed from repository paths and static analysis). |
| ModalBody.js package | library | Observed | Groups 1 file(s) under modalbody.js package (observed from repository paths and static analysis). |
| ModalFooter.js package | library | Observed | Groups 1 file(s) under modalfooter.js package (observed from repository paths and static analysis). |
| ModalHeader.js package | library | Observed | Groups 1 file(s) under modalheader.js package (observed from repository paths and static analysis). |
| Nav.js package | library | Observed | Groups 1 file(s) under nav.js package (observed from repository paths and static analysis). |
| Navbar.js package | library | Observed | Groups 1 file(s) under navbar.js package (observed from repository paths and static analysis). |
| NavbarBrand.js package | library | Observed | Groups 1 file(s) under navbarbrand.js package (observed from repository paths and static analysis). |
| NavbarText.js package | library | Observed | Groups 1 file(s) under navbartext.js package (observed from repository paths and static analysis). |
| NavbarToggler.js package | library | Observed | Groups 1 file(s) under navbartoggler.js package (observed from repository paths and static analysis). |
| NavItem.js package | library | Observed | Groups 1 file(s) under navitem.js package (observed from repository paths and static analysis). |
| NavLink.js package | library | Observed | Groups 1 file(s) under navlink.js package (observed from repository paths and static analysis). |
| Offcanvas.js package | library | Observed | Groups 1 file(s) under offcanvas.js package (observed from repository paths and static analysis). |
| OffcanvasBody.js package | library | Observed | Groups 1 file(s) under offcanvasbody.js package (observed from repository paths and static analysis). |
| OffcanvasHeader.js package | library | Observed | Groups 1 file(s) under offcanvasheader.js package (observed from repository paths and static analysis). |
| Pagination.js package | library | Observed | Groups 1 file(s) under pagination.js package (observed from repository paths and static analysis). |
| PaginationItem.js package | library | Observed | Groups 1 file(s) under paginationitem.js package (observed from repository paths and static analysis). |
| PaginationLink.js package | library | Observed | Groups 1 file(s) under paginationlink.js package (observed from repository paths and static analysis). |
| Placeholder.js package | library | Observed | Groups 1 file(s) under placeholder.js package (observed from repository paths and static analysis). |
| PlaceholderButton.js package | library | Observed | Groups 1 file(s) under placeholderbutton.js package (observed from repository paths and static analysis). |
| polyfill.js package | library | Observed | Groups 1 file(s) under polyfill.js package (observed from repository paths and static analysis). |
| Popover.js package | library | Observed | Groups 1 file(s) under popover.js package (observed from repository paths and static analysis). |
| PopoverBody.js package | library | Observed | Groups 1 file(s) under popoverbody.js package (observed from repository paths and static analysis). |
| PopoverHeader.js package | library | Observed | Groups 1 file(s) under popoverheader.js package (observed from repository paths and static analysis). |
| PopperContent.js package | library | Observed | Groups 1 file(s) under poppercontent.js package (observed from repository paths and static analysis). |
| PopperTargetHelper.js package | library | Observed | Groups 1 file(s) under poppertargethelper.js package (observed from repository paths and static analysis). |
| Portal.js package | library | Observed | Groups 1 file(s) under portal.js package (observed from repository paths and static analysis). |
| Progress.js package | library | Observed | Groups 1 file(s) under progress.js package (observed from repository paths and static analysis). |
| Row.js package | library | Observed | Groups 1 file(s) under row.js package (observed from repository paths and static analysis). |
| Spinner.js package | library | Observed | Groups 1 file(s) under spinner.js package (observed from repository paths and static analysis). |
| stories package | library | Observed | Groups 269 file(s) under stories package (observed from repository paths and static analysis). |
| TabContent.js package | library | Observed | Groups 1 file(s) under tabcontent.js package (observed from repository paths and static analysis). |
| TabContext.js package | library | Observed | Groups 1 file(s) under tabcontext.js package (observed from repository paths and static analysis). |
| Table.js package | library | Observed | Groups 1 file(s) under table.js package (observed from repository paths and static analysis). |
| TabPane.js package | library | Observed | Groups 1 file(s) under tabpane.js package (observed from repository paths and static analysis). |
| __tests__ package | library | Observed | Groups 89 file(s) under __tests__ package (observed from repository paths and static analysis). |
| testUtils.js package | library | Observed | Groups 1 file(s) under testutils.js package (observed from repository paths and static analysis). |
| Toast.js package | library | Observed | Groups 1 file(s) under toast.js package (observed from repository paths and static analysis). |
| ToastBody.js package | library | Observed | Groups 1 file(s) under toastbody.js package (observed from repository paths and static analysis). |
| ToastHeader.js package | library | Observed | Groups 1 file(s) under toastheader.js package (observed from repository paths and static analysis). |
| Tooltip.js package | library | Observed | Groups 1 file(s) under tooltip.js package (observed from repository paths and static analysis). |
| TooltipPopoverWrapper.js package | library | Observed | Groups 1 file(s) under tooltippopoverwrapper.js package (observed from repository paths and static analysis). |
| types package | library | Observed | Groups 92 file(s) under types package (observed from repository paths and static analysis). |
| UncontrolledAccordion.js package | library | Observed | Groups 1 file(s) under uncontrolledaccordion.js package (observed from repository paths and static analysis). |
| UncontrolledAlert.js package | library | Observed | Groups 1 file(s) under uncontrolledalert.js package (observed from repository paths and static analysis). |
| UncontrolledButtonDropdown.js package | library | Observed | Groups 1 file(s) under uncontrolledbuttondropdown.js package (observed from repository paths and static analysis). |
| UncontrolledCarousel.js package | library | Observed | Groups 1 file(s) under uncontrolledcarousel.js package (observed from repository paths and static analysis). |
| UncontrolledCollapse.js package | library | Observed | Groups 1 file(s) under uncontrolledcollapse.js package (observed from repository paths and static analysis). |
| UncontrolledDropdown.js package | library | Observed | Groups 1 file(s) under uncontrolleddropdown.js package (observed from repository paths and static analysis). |
| UncontrolledPopover.js package | library | Observed | Groups 1 file(s) under uncontrolledpopover.js package (observed from repository paths and static analysis). |
| UncontrolledTooltip.js package | library | Observed | Groups 1 file(s) under uncontrolledtooltip.js package (observed from repository paths and static analysis). |
| utils.js package | library | Observed | Groups 1 file(s) under utils.js package (observed from repository paths and static analysis). |

## Important files

- `.eslintrc.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/coverage.yml` (ci)
- `.github/workflows/docs.yml` (ci)
- `.github/workflows/release-please.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.prettierrc.json` (config)
- `config-overrides/package.json` (manifest)
- `package.json` (manifest)
- `stories/.eslintrc.json` (config)
- `types/tsconfig.json` (config)
- `types/tslint.json` (config)

## Top-level layout

- `stories` — 274 analysed file(s)
- `src` — 198 analysed file(s)
- `types` — 94 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `.github` — 7 analysed file(s)
- `.storybook` — 6 analysed file(s)
- `__mocks__` — 2 analysed file(s)
- `config-overrides` — 2 analysed file(s)
- `scripts` — 2 analysed file(s)
- `static` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `090bc1eeb19bcc269970151d330c6bc03f731635` is the revision these paths and observations refer to.
