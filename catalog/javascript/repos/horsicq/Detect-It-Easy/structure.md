# Project structure: horsicq/Detect-It-Easy

**Analysed commit:** `ed70c31e6a5e9655d1d94e717b9378ecc8019fed`

**Commit reference:** [ed70c31e6a5e9655d1d94e717b9378ecc8019fed](https://github.com/horsicq/Detect-It-Easy/commit/ed70c31e6a5e9655d1d94e717b9378ecc8019fed)

**Tree at this commit:** [horsicq/Detect-It-Easy@ed70c31e6a5e](https://github.com/horsicq/Detect-It-Easy/tree/ed70c31e6a5e9655d1d94e717b9378ecc8019fed)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | horsicq/Detect-It-Easy |
| Description | Program for determining types of files for Windows, Linux and MacOS. |
| Stars | 11950 |
| Forks | 1000 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `ed70c31e6a5e9655d1d94e717b9378ecc8019fed` |
| Retrieved at | 2026-11-14T19:12:12.882491+00:00 |
| Files in this snapshot | 447 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (4 files)
    create_beta.yml
    db-release.yml
    format-js.yml
    update_db.yml
  FUNDING.yml
autotools/  (48 files)
  dbcompiler/  (46 files)
    node_licenses/  (41 files)
      … 41 files under this directory
    node_modules_clean.cmd
    node_modules_clean.sh
    package.json
    task.js
    worker.js
  dbupdater/  (1 files)
    task.py
  partner/  (1 files)
    CONFIG
db/  (385 files)
  .vscode/  (2 files)
    about.txt
    settings.json
  APK/  (53 files)
    _APK.0.sg
    _init
    library_IL2CPP.4.sg
    library_SandHook.4.sg
    library_UnicomSDK.4.sg
    library_Unity.4.sg
    package_PackageName.1.sg
    packer_Kony.2.sg
    protector_APKProtect.2.sg
    protector_APKProtector.2.sg
    protector_AlibabaProtection.2.sg
    protector_AndroidRepublic.2.sg
    protector_AppGuard.2.sg
    protector_AppSolid.2.sg
    protector_BaiduProtection.2.sg
    protector_BangBangReinforcement.2.sg
    protector_BangcleProtection.2.sg
    protector_DXShield.2.sg
    protector_DexProtector.2.sg
    protector_DingXiangReinforcement.2.sg
    protector_EasyShield.2.sg
    protector_ExTrus_AppDefence.2.sg
    protector_Gemalto.2.sg
    protector_Hdus-Wjus.2.sg
    … 29 more files
  Amiga/  (99 files)
    _Amiga.0.sg
    _init
    compiler_ABasic.4.sg
    compiler_AMOS_Basic.4.sg
    compiler_Absoft_AC_Basic.4.sg
    compiler_Absoft_Fortran.4.sg
    compiler_AmigaBasic.4.sg
    compiler_Amiga_E.4.sg
    compiler_Aztec_C.4.sg
    compiler_Blitz_BASIC.4.sg
    compiler_DICE_C.4.sg
    compiler_Free_Pascal.4.sg
    compiler_GFA-Basic.4.sg
    compiler_GNU_C.4.sg
    compiler_HiSoft_Basic.4.sg
    compiler_JForth.4.sg
    compiler_Lattice_C.4.sg
    compiler_Maxon_C++.4.sg
    compiler_Multi-Forth.4.sg
    compiler_Oberon-A.4.sg
    compiler_PureBasic.4.sg
    compiler_Storm_C.4.sg
    compiler_VBCC.4.sg
    cruncher_AMOS_Compiler_Cruncher.1.sg
    … 75 more files
  Archive/  (2 files)
    _Archive.0.sg
    _init
  AtariST/  (2 files)
    _AtariST.0.sg
    _init
  Binary/  (226 files)
    Certificate_cert.WinAuth.1.sg
    ROM_1.sg
    __MiniBatchHeuristic_By_DosX.7.sg
    __MiniExtensionsHeuristic_By_DosX.7.sg
    __MiniJavaScriptHeuristic_By_DosX.7.sg
    __MiniVsProjMalwareHeuristic_by_DosX.7.sg
    _init
    archive_7z.1.sg
    archive_ACE.1.sg
    archive_ANC-Cruncher.1.sg
    archive_AR.1.sg
    archive_ARC.1.sg
    archive_ARCV4.1.sg
    archive_ARJ.1.sg
    archive_ASAR.1.sg
    archive_ASD.1.sg
    archive_Apple_Hardware_Test_LOC.1.sg
    archive_Audials_CMP.1.sg
    archive_BCSAR.1.sg
    archive_BZip.1.sg
    archive_Birdies.1.sg
    archive_Build_GRP.1.sg
    archive_CCA.1.sg
    archive_CFL3.1.sg
    … 202 more files
  ACE
.gitattributes
.gitignore
.prettierrc
CODE-FORMATTING.md
CONTRIBUTING.md
Dockerfile
LICENSE
README.md
changelog.txt
```

## Entry points

- [autotools/dbupdater/task.py:30](https://github.com/horsicq/Detect-It-Easy/blob/ed70c31e6a5e9655d1d94e717b9378ecc8019fed/autotools/dbupdater/task.py#L30)
- [autotools/dbcompiler/task.js](https://github.com/horsicq/Detect-It-Easy/blob/ed70c31e6a5e9655d1d94e717b9378ecc8019fed/autotools/dbcompiler/task.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| autotools package | library | Observed | Groups 3 file(s) under autotools package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: count_signatures. |

## Important files

- `.github/FUNDING.yml` (config)
- `.github/workflows/create_beta.yml` (ci)
- `.github/workflows/db-release.yml` (ci)
- `.github/workflows/format-js.yml` (ci)
- `.github/workflows/update_db.yml` (ci)
- `Dockerfile` (container)
- `autotools/dbcompiler/package.json` (manifest)
- `db/.vscode/settings.json` (config)

## Top-level layout

- `db` — 385 analysed file(s)
- `autotools` — 48 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 5 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 353 file(s) were skipped during inventory (1 x lockfile excluded; 352 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `ed70c31e6a5e9655d1d94e717b9378ecc8019fed` is the revision these paths and observations refer to.
