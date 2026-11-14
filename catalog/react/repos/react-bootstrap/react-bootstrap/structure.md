# Project structure: react-bootstrap/react-bootstrap

**Analysed commit:** `3291c5bed8c4ec287e7bc5cf3a980984cfedbb6a`

**Commit reference:** [3291c5bed8c4ec287e7bc5cf3a980984cfedbb6a](https://github.com/react-bootstrap/react-bootstrap/commit/3291c5bed8c4ec287e7bc5cf3a980984cfedbb6a)

**Tree at this commit:** [react-bootstrap/react-bootstrap@3291c5bed8c4](https://github.com/react-bootstrap/react-bootstrap/tree/3291c5bed8c4ec287e7bc5cf3a980984cfedbb6a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | react-bootstrap/react-bootstrap |
| Description | Bootstrap components built with React |
| Stars | 22613 |
| Forks | 3565 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | master |
| Analysed commit | `3291c5bed8c4ec287e7bc5cf3a980984cfedbb6a` |
| Retrieved at | 2026-11-14T19:13:07.750303+00:00 |
| Files in this snapshot | 630 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    feature_request.yml
  workflows/  (1 files)
    ci.yml
.husky/  (1 files)
  pre-commit
scripts/  (3 files)
  buildDist.ts
  dist.webpack.config.js
  tsconfig.json
src/  (147 files)
  internal/  (1 files)
    warning.ts
  AbstractModalHeader.tsx
  Accordion.tsx
  AccordionBody.tsx
  AccordionButton.tsx
  AccordionCollapse.tsx
  AccordionContext.ts
  AccordionHeader.tsx
  AccordionItem.tsx
  AccordionItemContext.ts
  Alert.tsx
  AlertHeading.tsx
  AlertLink.tsx
  Anchor.tsx
  Badge.tsx
  BootstrapModalManager.tsx
  Breadcrumb.tsx
  BreadcrumbItem.tsx
  Button.tsx
  ButtonGroup.tsx
  ButtonToolbar.tsx
  Card.tsx
  CardBody.tsx
  CardFooter.tsx
  CardGroup.tsx
  … 122 more files
test/  (88 files)
  AccordionButtonSpec.tsx
  AccordionHeaderSpec.tsx
  AccordionSpec.tsx
  AlertSpec.tsx
  BadgeSpec.tsx
  BootstrapModalManagerSpec.ts
  BreadcrumbItemSpec.tsx
  BreadcrumbSpec.tsx
  ButtonGroupSpec.tsx
  ButtonSpec.tsx
  ButtonToolbarSpec.tsx
  CardImgSpec.tsx
  CardSpec.tsx
  CarouselCaptionSpec.tsx
  CarouselSpec.tsx
  CloseButtonSpec.tsx
  ColSpec.tsx
  CollapseSpec.tsx
  ContainerSpec.tsx
  DropdownButtonSpec.tsx
  DropdownItemSpec.tsx
  DropdownMenuSpec.tsx
  DropdownSpec.tsx
  DropdownToggleSpec.tsx
  … 64 more files
tests/  (1 files)
  simple-types-test.tsx
www/  (367 files)
  docs/  (316 files)
    components/  (26 files)
      … 26 files under this directory
    examples/  (260 files)
      … 260 files under this directory
    forms/  (11 files)
      … 11 files under this directory
    getting-started/  (7 files)
      … 7 files under this directory
    layout/  (4 files)
      … 4 files under this directory
    migrating/  (3 files)
      … 3 files under this directory
    utilities/  (4 files)
      … 4 files under this directory
    about.mdx
  plugins/  (4 files)
    bootstrap-metadata-plugin.ts
    react-docgen-plugin.ts
    react-resolver-plugin.ts
    webpack-plugin.ts
  src/  (34 files)
    components/  (14 files)
      … 14 files under this directory
    css/  (4 files)
      … 4 files under this directory
    hooks/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
    theme/  (13 files)
      … 13 files under this directory
  static/  (6 files)
    img/  (5 files)
      … 5 files under this directory
    .nojekyll
  .gitignore
  README.md
  babel.config.js
  docusaurus.config.ts
  package.json
  sidebars.ts
  tsconfig.json
.babelrc.js
.editorconfig
.gitattributes
.gitignore
.nvmrc
CHANGELOG-pre1.md
CHANGELOG.md
CONTRIBUTING.md
LICENSE
MAINTAINING.md
README.md
codecov.yml
eslint.config.mjs
manual_releases.md
package.json
renovate.json
tsconfig.json
vitest.config.mts
vitest.setup.ts
vitest.shims.d.ts
```

## Entry points

- [src/index.tsx](https://github.com/react-bootstrap/react-bootstrap/blob/3291c5bed8c4ec287e7bc5cf3a980984cfedbb6a/src/index.tsx)
- [www/src/pages/index.tsx](https://github.com/react-bootstrap/react-bootstrap/blob/3291c5bed8c4ec287e7bc5cf3a980984cfedbb6a/www/src/pages/index.tsx)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| AbstractModalHeader.tsx package | library | Observed | Groups 1 file(s) under abstractmodalheader.tsx package (observed from repository paths and static analysis). |
| Accordion.tsx package | library | Observed | Groups 1 file(s) under accordion.tsx package (observed from repository paths and static analysis). |
| AccordionBody.tsx package | library | Observed | Groups 1 file(s) under accordionbody.tsx package (observed from repository paths and static analysis). |
| AccordionButton.tsx package | library | Observed | Groups 1 file(s) under accordionbutton.tsx package (observed from repository paths and static analysis). |
| AccordionCollapse.tsx package | library | Observed | Groups 1 file(s) under accordioncollapse.tsx package (observed from repository paths and static analysis). |
| AccordionContext.ts package | library | Observed | Groups 1 file(s) under accordioncontext.ts package (observed from repository paths and static analysis). |
| AccordionHeader.tsx package | library | Observed | Groups 1 file(s) under accordionheader.tsx package (observed from repository paths and static analysis). |
| AccordionItem.tsx package | library | Observed | Groups 1 file(s) under accordionitem.tsx package (observed from repository paths and static analysis). |
| AccordionItemContext.ts package | library | Observed | Groups 1 file(s) under accordionitemcontext.ts package (observed from repository paths and static analysis). |
| Alert.tsx package | library | Observed | Groups 1 file(s) under alert.tsx package (observed from repository paths and static analysis). |
| AlertHeading.tsx package | library | Observed | Groups 1 file(s) under alertheading.tsx package (observed from repository paths and static analysis). |
| AlertLink.tsx package | library | Observed | Groups 1 file(s) under alertlink.tsx package (observed from repository paths and static analysis). |
| Anchor.tsx package | library | Observed | Groups 1 file(s) under anchor.tsx package (observed from repository paths and static analysis). |
| Badge.tsx package | library | Observed | Groups 1 file(s) under badge.tsx package (observed from repository paths and static analysis). |
| BootstrapModalManager.tsx package | library | Observed | Groups 1 file(s) under bootstrapmodalmanager.tsx package (observed from repository paths and static analysis). |
| Breadcrumb.tsx package | library | Observed | Groups 1 file(s) under breadcrumb.tsx package (observed from repository paths and static analysis). |
| BreadcrumbItem.tsx package | library | Observed | Groups 1 file(s) under breadcrumbitem.tsx package (observed from repository paths and static analysis). |
| Button.tsx package | library | Observed | Groups 1 file(s) under button.tsx package (observed from repository paths and static analysis). |
| ButtonGroup.tsx package | library | Observed | Groups 1 file(s) under buttongroup.tsx package (observed from repository paths and static analysis). |
| ButtonToolbar.tsx package | library | Observed | Groups 1 file(s) under buttontoolbar.tsx package (observed from repository paths and static analysis). |
| Card.tsx package | library | Observed | Groups 1 file(s) under card.tsx package (observed from repository paths and static analysis). |
| CardBody.tsx package | library | Observed | Groups 1 file(s) under cardbody.tsx package (observed from repository paths and static analysis). |
| CardFooter.tsx package | library | Observed | Groups 1 file(s) under cardfooter.tsx package (observed from repository paths and static analysis). |
| CardGroup.tsx package | library | Observed | Groups 1 file(s) under cardgroup.tsx package (observed from repository paths and static analysis). |
| CardHeader.tsx package | library | Observed | Groups 1 file(s) under cardheader.tsx package (observed from repository paths and static analysis). |
| CardHeaderContext.tsx package | library | Observed | Groups 1 file(s) under cardheadercontext.tsx package (observed from repository paths and static analysis). |
| CardImg.tsx package | library | Observed | Groups 1 file(s) under cardimg.tsx package (observed from repository paths and static analysis). |
| CardImgOverlay.tsx package | library | Observed | Groups 1 file(s) under cardimgoverlay.tsx package (observed from repository paths and static analysis). |
| CardLink.tsx package | library | Observed | Groups 1 file(s) under cardlink.tsx package (observed from repository paths and static analysis). |
| CardSubtitle.tsx package | library | Observed | Groups 1 file(s) under cardsubtitle.tsx package (observed from repository paths and static analysis). |
| CardText.tsx package | library | Observed | Groups 1 file(s) under cardtext.tsx package (observed from repository paths and static analysis). |
| CardTitle.tsx package | library | Observed | Groups 1 file(s) under cardtitle.tsx package (observed from repository paths and static analysis). |
| Carousel.tsx package | library | Observed | Groups 1 file(s) under carousel.tsx package (observed from repository paths and static analysis). |
| CarouselCaption.tsx package | library | Observed | Groups 1 file(s) under carouselcaption.tsx package (observed from repository paths and static analysis). |
| CarouselItem.tsx package | library | Observed | Groups 1 file(s) under carouselitem.tsx package (observed from repository paths and static analysis). |
| CloseButton.tsx package | library | Observed | Groups 1 file(s) under closebutton.tsx package (observed from repository paths and static analysis). |
| Col.tsx package | library | Observed | Groups 1 file(s) under col.tsx package (observed from repository paths and static analysis). |
| Collapse.tsx package | library | Observed | Groups 1 file(s) under collapse.tsx package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 13 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Container.tsx package | library | Observed | Groups 1 file(s) under container.tsx package (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| createChainedFunction.tsx package | library | Observed | Groups 1 file(s) under createchainedfunction.tsx package (observed from repository paths and static analysis). |
| createUtilityClasses.ts package | library | Observed | Groups 1 file(s) under createutilityclasses.ts package (observed from repository paths and static analysis). |
| createWithBsPrefix.tsx package | library | Observed | Groups 1 file(s) under createwithbsprefix.tsx package (observed from repository paths and static analysis). |
| divWithClassName.tsx package | library | Observed | Groups 1 file(s) under divwithclassname.tsx package (observed from repository paths and static analysis). |
| Dropdown.tsx package | library | Observed | Groups 1 file(s) under dropdown.tsx package (observed from repository paths and static analysis). |
| DropdownButton.tsx package | library | Observed | Groups 1 file(s) under dropdownbutton.tsx package (observed from repository paths and static analysis). |
| DropdownContext.ts package | library | Observed | Groups 1 file(s) under dropdowncontext.ts package (observed from repository paths and static analysis). |
| DropdownDivider.tsx package | library | Observed | Groups 1 file(s) under dropdowndivider.tsx package (observed from repository paths and static analysis). |
| DropdownHeader.tsx package | library | Observed | Groups 1 file(s) under dropdownheader.tsx package (observed from repository paths and static analysis). |
| DropdownItem.tsx package | library | Observed | Groups 1 file(s) under dropdownitem.tsx package (observed from repository paths and static analysis). |
| DropdownItemText.tsx package | library | Observed | Groups 1 file(s) under dropdownitemtext.tsx package (observed from repository paths and static analysis). |
| DropdownMenu.tsx package | library | Observed | Groups 1 file(s) under dropdownmenu.tsx package (observed from repository paths and static analysis). |
| DropdownToggle.tsx package | library | Observed | Groups 1 file(s) under dropdowntoggle.tsx package (observed from repository paths and static analysis). |
| ElementChildren.tsx package | library | Observed | Groups 1 file(s) under elementchildren.tsx package (observed from repository paths and static analysis). |
| Fade.tsx package | library | Observed | Groups 1 file(s) under fade.tsx package (observed from repository paths and static analysis). |
| Feedback.tsx package | library | Observed | Groups 1 file(s) under feedback.tsx package (observed from repository paths and static analysis). |
| Figure.tsx package | library | Observed | Groups 1 file(s) under figure.tsx package (observed from repository paths and static analysis). |
| FigureCaption.tsx package | library | Observed | Groups 1 file(s) under figurecaption.tsx package (observed from repository paths and static analysis). |
| FigureImage.tsx package | library | Observed | Groups 1 file(s) under figureimage.tsx package (observed from repository paths and static analysis). |
| FloatingLabel.tsx package | library | Observed | Groups 1 file(s) under floatinglabel.tsx package (observed from repository paths and static analysis). |
| Form.tsx package | library | Observed | Groups 1 file(s) under form.tsx package (observed from repository paths and static analysis). |
| FormCheck.tsx package | library | Observed | Groups 1 file(s) under formcheck.tsx package (observed from repository paths and static analysis). |
| FormCheckInput.tsx package | library | Observed | Groups 1 file(s) under formcheckinput.tsx package (observed from repository paths and static analysis). |
| FormCheckLabel.tsx package | library | Observed | Groups 1 file(s) under formchecklabel.tsx package (observed from repository paths and static analysis). |
| FormContext.tsx package | library | Observed | Groups 1 file(s) under formcontext.tsx package (observed from repository paths and static analysis). |
| FormControl.tsx package | library | Observed | Groups 1 file(s) under formcontrol.tsx package (observed from repository paths and static analysis). |
| FormFloating.tsx package | library | Observed | Groups 1 file(s) under formfloating.tsx package (observed from repository paths and static analysis). |
| FormGroup.tsx package | library | Observed | Groups 1 file(s) under formgroup.tsx package (observed from repository paths and static analysis). |
| FormLabel.tsx package | library | Observed | Groups 1 file(s) under formlabel.tsx package (observed from repository paths and static analysis). |
| FormRange.tsx package | library | Observed | Groups 1 file(s) under formrange.tsx package (observed from repository paths and static analysis). |
| FormSelect.tsx package | library | Observed | Groups 1 file(s) under formselect.tsx package (observed from repository paths and static analysis). |
| FormText.tsx package | library | Observed | Groups 1 file(s) under formtext.tsx package (observed from repository paths and static analysis). |
| getInitialPopperStyles.ts package | library | Observed | Groups 1 file(s) under getinitialpopperstyles.ts package (observed from repository paths and static analysis). |
| getTabTransitionComponent.ts package | library | Observed | Groups 1 file(s) under gettabtransitioncomponent.ts package (observed from repository paths and static analysis). |
| helpers.ts package | library | Observed | Groups 1 file(s) under helpers.ts package (observed from repository paths and static analysis). |
| Image.tsx package | library | Observed | Groups 1 file(s) under image.tsx package (observed from repository paths and static analysis). |
| index.tsx package | library | Observed | Groups 1 file(s) under index.tsx package (observed from repository paths and static analysis). |
| InputGroup.tsx package | library | Observed | Groups 1 file(s) under inputgroup.tsx package (observed from repository paths and static analysis). |
| InputGroupContext.tsx package | library | Observed | Groups 1 file(s) under inputgroupcontext.tsx package (observed from repository paths and static analysis). |
| InputGroupText.tsx package | library | Observed | Groups 1 file(s) under inputgrouptext.tsx package (observed from repository paths and static analysis). |
| internal package | library | Observed | Groups 1 file(s) under internal package (observed from repository paths and static analysis). |
| ListGroup.tsx package | library | Observed | Groups 1 file(s) under listgroup.tsx package (observed from repository paths and static analysis). |
| ListGroupItem.tsx package | library | Observed | Groups 1 file(s) under listgroupitem.tsx package (observed from repository paths and static analysis). |
| Modal.tsx package | library | Observed | Groups 1 file(s) under modal.tsx package (observed from repository paths and static analysis). |
| ModalBody.tsx package | library | Observed | Groups 1 file(s) under modalbody.tsx package (observed from repository paths and static analysis). |
| ModalContext.tsx package | library | Observed | Groups 1 file(s) under modalcontext.tsx package (observed from repository paths and static analysis). |
| ModalDialog.tsx package | library | Observed | Groups 1 file(s) under modaldialog.tsx package (observed from repository paths and static analysis). |
| ModalFooter.tsx package | library | Observed | Groups 1 file(s) under modalfooter.tsx package (observed from repository paths and static analysis). |
| ModalHeader.tsx package | library | Observed | Groups 1 file(s) under modalheader.tsx package (observed from repository paths and static analysis). |
| ModalTitle.tsx package | library | Observed | Groups 1 file(s) under modaltitle.tsx package (observed from repository paths and static analysis). |
| Nav.tsx package | library | Observed | Groups 1 file(s) under nav.tsx package (observed from repository paths and static analysis). |
| Navbar.tsx package | library | Observed | Groups 1 file(s) under navbar.tsx package (observed from repository paths and static analysis). |
| NavbarBrand.tsx package | library | Observed | Groups 1 file(s) under navbarbrand.tsx package (observed from repository paths and static analysis). |
| NavbarCollapse.tsx package | library | Observed | Groups 1 file(s) under navbarcollapse.tsx package (observed from repository paths and static analysis). |
| NavbarContext.tsx package | library | Observed | Groups 1 file(s) under navbarcontext.tsx package (observed from repository paths and static analysis). |
| NavbarOffcanvas.tsx package | library | Observed | Groups 1 file(s) under navbaroffcanvas.tsx package (observed from repository paths and static analysis). |
| NavbarText.tsx package | library | Observed | Groups 1 file(s) under navbartext.tsx package (observed from repository paths and static analysis). |
| NavbarToggle.tsx package | library | Observed | Groups 1 file(s) under navbartoggle.tsx package (observed from repository paths and static analysis). |
| NavContext.tsx package | library | Observed | Groups 1 file(s) under navcontext.tsx package (observed from repository paths and static analysis). |
| NavDropdown.tsx package | library | Observed | Groups 1 file(s) under navdropdown.tsx package (observed from repository paths and static analysis). |
| NavItem.tsx package | library | Observed | Groups 1 file(s) under navitem.tsx package (observed from repository paths and static analysis). |
| NavLink.tsx package | library | Observed | Groups 1 file(s) under navlink.tsx package (observed from repository paths and static analysis). |
| Offcanvas.tsx package | library | Observed | Groups 1 file(s) under offcanvas.tsx package (observed from repository paths and static analysis). |
| OffcanvasBody.tsx package | library | Observed | Groups 1 file(s) under offcanvasbody.tsx package (observed from repository paths and static analysis). |
| OffcanvasHeader.tsx package | library | Observed | Groups 1 file(s) under offcanvasheader.tsx package (observed from repository paths and static analysis). |
| OffcanvasTitle.tsx package | library | Observed | Groups 1 file(s) under offcanvastitle.tsx package (observed from repository paths and static analysis). |
| OffcanvasToggling.tsx package | library | Observed | Groups 1 file(s) under offcanvastoggling.tsx package (observed from repository paths and static analysis). |
| Overlay.tsx package | library | Observed | Groups 1 file(s) under overlay.tsx package (observed from repository paths and static analysis). |
| OverlayTrigger.tsx package | library | Observed | Groups 1 file(s) under overlaytrigger.tsx package (observed from repository paths and static analysis). |
| PageItem.tsx package | library | Observed | Groups 1 file(s) under pageitem.tsx package (observed from repository paths and static analysis). |
| Pagination.tsx package | library | Observed | Groups 1 file(s) under pagination.tsx package (observed from repository paths and static analysis). |
| Placeholder.tsx package | library | Observed | Groups 1 file(s) under placeholder.tsx package (observed from repository paths and static analysis). |
| PlaceholderButton.tsx package | library | Observed | Groups 1 file(s) under placeholderbutton.tsx package (observed from repository paths and static analysis). |
| Popover.tsx package | library | Observed | Groups 1 file(s) under popover.tsx package (observed from repository paths and static analysis). |
| PopoverBody.tsx package | library | Observed | Groups 1 file(s) under popoverbody.tsx package (observed from repository paths and static analysis). |
| PopoverHeader.tsx package | library | Observed | Groups 1 file(s) under popoverheader.tsx package (observed from repository paths and static analysis). |
| ProgressBar.tsx package | library | Observed | Groups 1 file(s) under progressbar.tsx package (observed from repository paths and static analysis). |
| Ratio.tsx package | library | Observed | Groups 1 file(s) under ratio.tsx package (observed from repository paths and static analysis). |
| Row.tsx package | library | Observed | Groups 1 file(s) under row.tsx package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Spinner.tsx package | library | Observed | Groups 1 file(s) under spinner.tsx package (observed from repository paths and static analysis). |
| SplitButton.tsx package | library | Observed | Groups 1 file(s) under splitbutton.tsx package (observed from repository paths and static analysis). |
| Stack.tsx package | library | Observed | Groups 1 file(s) under stack.tsx package (observed from repository paths and static analysis). |
| Switch.tsx package | library | Observed | Groups 1 file(s) under switch.tsx package (observed from repository paths and static analysis). |
| Tab.tsx package | library | Observed | Groups 1 file(s) under tab.tsx package (observed from repository paths and static analysis). |
| TabContainer.tsx package | library | Observed | Groups 1 file(s) under tabcontainer.tsx package (observed from repository paths and static analysis). |
| TabContent.tsx package | library | Observed | Groups 1 file(s) under tabcontent.tsx package (observed from repository paths and static analysis). |
| Table.tsx package | library | Observed | Groups 1 file(s) under table.tsx package (observed from repository paths and static analysis). |
| TabPane.tsx package | library | Observed | Groups 1 file(s) under tabpane.tsx package (observed from repository paths and static analysis). |
| Tabs.tsx package | library | Observed | Groups 1 file(s) under tabs.tsx package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 89 file(s) under tests (observed from repository paths and static analysis). |
| ThemeProvider.tsx package | library | Observed | Groups 1 file(s) under themeprovider.tsx package (observed from repository paths and static analysis). |
| Toast.tsx package | library | Observed | Groups 1 file(s) under toast.tsx package (observed from repository paths and static analysis). |
| ToastBody.tsx package | library | Observed | Groups 1 file(s) under toastbody.tsx package (observed from repository paths and static analysis). |
| ToastContainer.tsx package | library | Observed | Groups 1 file(s) under toastcontainer.tsx package (observed from repository paths and static analysis). |
| ToastContext.tsx package | library | Observed | Groups 1 file(s) under toastcontext.tsx package (observed from repository paths and static analysis). |
| ToastFade.tsx package | library | Observed | Groups 1 file(s) under toastfade.tsx package (observed from repository paths and static analysis). |
| ToastHeader.tsx package | library | Observed | Groups 1 file(s) under toastheader.tsx package (observed from repository paths and static analysis). |
| ToggleButton.tsx package | library | Observed | Groups 1 file(s) under togglebutton.tsx package (observed from repository paths and static analysis). |
| ToggleButtonGroup.tsx package | library | Observed | Groups 1 file(s) under togglebuttongroup.tsx package (observed from repository paths and static analysis). |
| Tooltip.tsx package | library | Observed | Groups 1 file(s) under tooltip.tsx package (observed from repository paths and static analysis). |
| transitionEndListener.ts package | library | Observed | Groups 1 file(s) under transitionendlistener.ts package (observed from repository paths and static analysis). |
| TransitionWrapper.tsx package | library | Observed | Groups 1 file(s) under transitionwrapper.tsx package (observed from repository paths and static analysis). |
| triggerBrowserReflow.tsx package | library | Observed | Groups 1 file(s) under triggerbrowserreflow.tsx package (observed from repository paths and static analysis). |
| types.tsx package | library | Observed | Groups 1 file(s) under types.tsx package (observed from repository paths and static analysis). |
| useAccordionButton.ts package | library | Observed | Groups 1 file(s) under useaccordionbutton.ts package (observed from repository paths and static analysis). |
| useCol.ts package | library | Observed | Groups 1 file(s) under usecol.ts package (observed from repository paths and static analysis). |
| useOverlayOffset.tsx package | library | Observed | Groups 1 file(s) under useoverlayoffset.tsx package (observed from repository paths and static analysis). |
| usePlaceholder.ts package | library | Observed | Groups 1 file(s) under useplaceholder.ts package (observed from repository paths and static analysis). |
| useWrappedRefWithWarning.tsx package | library | Observed | Groups 1 file(s) under usewrappedrefwithwarning.tsx package (observed from repository paths and static analysis). |
| www package | library | Observed | Groups 32 file(s) under www package (observed from repository paths and static analysis). |

## Important files

- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `codecov.yml` (config)
- `package.json` (manifest)
- `renovate.json` (config)
- `scripts/tsconfig.json` (config)
- `tsconfig.json` (config)
- `www/docs/components/_category_.json` (config)
- `www/docs/forms/_category_.json` (config)
- `www/docs/getting-started/_category_.json` (config)
- `www/docs/layout/_category_.json` (config)
- `www/docs/migrating/_category_.json` (config)
- `www/docs/utilities/_category_.json` (config)
- `www/package.json` (manifest)
- `www/tsconfig.json` (config)

## Top-level layout

- `www` — 367 analysed file(s)
- `src` — 147 analysed file(s)
- `test` — 88 analysed file(s)
- `(root files)` — 20 analysed file(s)
- `.github` — 3 analysed file(s)
- `scripts` — 3 analysed file(s)
- `.husky` — 1 analysed file(s)
- `tests` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `3291c5bed8c4ec287e7bc5cf3a980984cfedbb6a` is the revision these paths and observations refer to.
