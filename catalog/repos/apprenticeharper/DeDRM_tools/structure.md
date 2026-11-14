# Project structure: apprenticeharper/DeDRM_tools

**Analysed commit:** `776f146ca00d11b24575f4fd6e8202df30a2b7ea`

**Commit reference:** [776f146ca00d11b24575f4fd6e8202df30a2b7ea](https://github.com/apprenticeharper/DeDRM_tools/commit/776f146ca00d11b24575f4fd6e8202df30a2b7ea)

**Tree at this commit:** [apprenticeharper/DeDRM_tools@776f146ca00d](https://github.com/apprenticeharper/DeDRM_tools/tree/776f146ca00d11b24575f4fd6e8202df30a2b7ea)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | apprenticeharper/DeDRM_tools |
| Description | DeDRM tools for ebooks |
| Stars | 15404 |
| Forks | 1715 |
| Licence | Not detected |
| Language | Python |
| Default branch | master |
| Analysed commit | `776f146ca00d11b24575f4fd6e8202df30a2b7ea` |
| Retrieved at | 2026-11-14T19:09:02.880261+00:00 |
| Files in this snapshot | 103 |

## Directory tree

```text
.github/  (3 files)
  ISSUE_TEMPLATE/  (1 files)
    QUESTION.md
  workflows/  (2 files)
    Format.yaml
    Lint.yaml
DeDRM_plugin/  (52 files)
  DeDRM_Adobe Digital Editions Key_Help.htm
  DeDRM_Barnes and Noble Key_Help.htm
  DeDRM_EInk Kindle Serial Number_Help.htm
  DeDRM_Help.htm
  DeDRM_Kindle for Android Key_Help.htm
  DeDRM_Kindle for Mac and PC Key_Help.htm
  DeDRM_Mobipocket PID_Help.htm
  DeDRM_eReader Key_Help.htm
  __init__.py
  activitybar.py
  adobekey.py
  aescbc.py
  alfcrypto.py
  androidkindlekey.py
  argv_utils.py
  askfolder_ed.py
  config.py
  convert2xml.py
  epubtest.py
  erdr2pml.py
  flatxml2html.py
  flatxml2svg.py
  genbook.py
  ignobleepub.py
  … 28 more files
Obok_plugin/  (18 files)
  obok/  (3 files)
    __init__.py
    legacy_obok.py
    obok.py
  translations/  (7 files)
    ar.po
    de.po
    default.po
    es.po
    nl.po
    pt.po
    sv.po
  __init__.py
  action.py
  common_utils.py
  config.py
  dialogs.py
  obok_dedrm_Help.htm
  plugin-import-name-obok_dedrm.txt
  utilities.py
Other_Tools/  (22 files)
  B_and_N_Download_Helper/  (2 files)
    BN-Dload.user.js
    BN-Dload.user_ReadMe.txt
  DRM_Key_Scripts/  (7 files)
    Adobe_Digital_Editions/  (1 files)
      … 1 files under this directory
    Barnes_and_Noble_ePubs/  (3 files)
      … 3 files under this directory
    Kindle_for_Android/  (1 files)
      … 1 files under this directory
    Kindle_for_Mac_and_PC/  (1 files)
      … 1 files under this directory
    Kindle_for_iOS/  (1 files)
      … 1 files under this directory
  Kindle_for_Android_Patches/  (8 files)
    kindle_version_3.0.1.70/  (2 files)
      … 2 files under this directory
    kindle_version_3.7.0.108/  (2 files)
      … 2 files under this directory
    kindle_version_4.0.2.1/  (1 files)
      … 1 files under this directory
    kindle_version_4.8.1.10/  (2 files)
      … 2 files under this directory
    A_Patching_Experience.txt
  Kobo/  (1 files)
    obok.py
  Rocket_ebooks/  (1 files)
    rebhack_ReadMe.txt
  Scuolabook_DRM/  (1 files)
    Scuolabook_ReadMe.txt
  Tetrachroma_FileOpen_ineptpdf/  (2 files)
    ineptpdf_8.4.51.pyw
    ineptpdf_8.4.51_ReadMe.txt
.gitignore
CALIBRE_CLI_INSTRUCTIONS.md
DeDRM_plugin_ReadMe.txt
FAQs.md
README.md
ReadMe_Overview.txt
make_release.py
obok_plugin_ReadMe.txt
```

## Entry points

- [DeDRM_plugin/adobekey.py:584](https://github.com/apprenticeharper/DeDRM_tools/blob/776f146ca00d11b24575f4fd6e8202df30a2b7ea/DeDRM_plugin/adobekey.py#L584)
- [DeDRM_plugin/androidkindlekey.py:463](https://github.com/apprenticeharper/DeDRM_tools/blob/776f146ca00d11b24575f4fd6e8202df30a2b7ea/DeDRM_plugin/androidkindlekey.py#L463)
- [DeDRM_plugin/convert2xml.py:895](https://github.com/apprenticeharper/DeDRM_tools/blob/776f146ca00d11b24575f4fd6e8202df30a2b7ea/DeDRM_plugin/convert2xml.py#L895)
- [DeDRM_plugin/epubtest.py:207](https://github.com/apprenticeharper/DeDRM_tools/blob/776f146ca00d11b24575f4fd6e8202df30a2b7ea/DeDRM_plugin/epubtest.py#L207)
- [DeDRM_plugin/erdr2pml.py:587](https://github.com/apprenticeharper/DeDRM_tools/blob/776f146ca00d11b24575f4fd6e8202df30a2b7ea/DeDRM_plugin/erdr2pml.py#L587)
- [DeDRM_plugin/genbook.py:732](https://github.com/apprenticeharper/DeDRM_tools/blob/776f146ca00d11b24575f4fd6e8202df30a2b7ea/DeDRM_plugin/genbook.py#L732)
- [DeDRM_plugin/ignobleepub.py:438](https://github.com/apprenticeharper/DeDRM_tools/blob/776f146ca00d11b24575f4fd6e8202df30a2b7ea/DeDRM_plugin/ignobleepub.py#L438)
- [DeDRM_plugin/ignoblekey.py:331](https://github.com/apprenticeharper/DeDRM_tools/blob/776f146ca00d11b24575f4fd6e8202df30a2b7ea/DeDRM_plugin/ignoblekey.py#L331)
- [DeDRM_plugin/ignoblekeyfetch.py:251](https://github.com/apprenticeharper/DeDRM_tools/blob/776f146ca00d11b24575f4fd6e8202df30a2b7ea/DeDRM_plugin/ignoblekeyfetch.py#L251)
- [DeDRM_plugin/ignoblekeygen.py:327](https://github.com/apprenticeharper/DeDRM_tools/blob/776f146ca00d11b24575f4fd6e8202df30a2b7ea/DeDRM_plugin/ignoblekeygen.py#L327)
- [DeDRM_plugin/ignoblepdf.py:2161](https://github.com/apprenticeharper/DeDRM_tools/blob/776f146ca00d11b24575f4fd6e8202df30a2b7ea/DeDRM_plugin/ignoblepdf.py#L2161)
- [DeDRM_plugin/ineptepub.py:597](https://github.com/apprenticeharper/DeDRM_tools/blob/776f146ca00d11b24575f4fd6e8202df30a2b7ea/DeDRM_plugin/ineptepub.py#L597)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AddAdeptDialog, AddAndroidDialog, AddBandNKeyDialog, AddEReaderDialog, AddKindleDialo… |
| DeDRM_plugin package | library | Observed | Groups 22 file(s) under dedrm_plugin package (observed from repository paths and static analysis). Observed top-level classes: AES, AES_CBC, ActivityBar, BROWSEINFO, BadKeySizeError, BinaryIonParser. Observed top-level… |
| Application entry point | entrypoint | Observed | Groups 23 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: ADEPTError, AndroidObfuscation, AndroidObfuscationV2, BadZipfile, Decryptor, Dictionary.… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Obok_plugin package | library | Observed | Groups 7 file(s) under obok_plugin package (observed from repository paths and static analysis). Observed top-level classes: AddEpubFormatsProgressDialog, AuthorTableWidgetItem, BookListTableWidget, CheckableTableWidget… |
| Other_Tools package | library | Observed | Groups 1 file(s) under other_tools package (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/Format.yaml` (ci)
- `.github/workflows/Lint.yaml` (ci)

## Top-level layout

- `DeDRM_plugin` — 52 analysed file(s)
- `Other_Tools` — 22 analysed file(s)
- `Obok_plugin` — 18 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `776f146ca00d11b24575f4fd6e8202df30a2b7ea` is the revision these paths and observations refer to.
