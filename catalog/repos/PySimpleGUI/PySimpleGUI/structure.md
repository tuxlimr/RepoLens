# Project structure: PySimpleGUI/PySimpleGUI

**Analysed commit:** `00de5ab857f56014294cb0a5c725a96d32eb7af6`

**Commit reference:** [00de5ab857f56014294cb0a5c725a96d32eb7af6](https://github.com/PySimpleGUI/PySimpleGUI/commit/00de5ab857f56014294cb0a5c725a96d32eb7af6)

**Tree at this commit:** [PySimpleGUI/PySimpleGUI@00de5ab857f5](https://github.com/PySimpleGUI/PySimpleGUI/tree/00de5ab857f56014294cb0a5c725a96d32eb7af6)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | PySimpleGUI/PySimpleGUI |
| Description | Python GUIs for Humans! Create any GUI simple or complicated in a way that's intuitive.  Launched in 2018. NEW for 2026 - the LGPL3 Version 6.  Transforms tkinter, Qt, WxPython, and Remi into a simple, intuitive, and fun experience for both hobbyists and expert users.  |
| Stars | 13820 |
| Forks | 1816 |
| Licence | LGPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `00de5ab857f56014294cb0a5c725a96d32eb7af6` |
| Retrieved at | 2026-11-14T19:09:42.987077+00:00 |
| Files in this snapshot | 352 |

## Directory tree

```text
.github/  (4 files)
  ISSUE_TEMPLATE/  (2 files)
    config.yml
    issue-form---must-fill-in-this-form-with-every-new-issue-submitted.md
  PULL_REQUEST_TEMPLATE/  (1 files)
    pull_request_template.md
  workflows/  (1 files)
    close_prs.yml
DemoPrograms/  (338 files)
  Browser_START_HERE_Demo_Programs_Browser.py
  Demo_All_Elements.py
  Demo_All_Elements_Simple.py
  Demo_Animated_GIFs.py
  Demo_Animated_GIFs_Using_PIL.py
  Demo_Auto_Save_Window_Position.py
  Demo_Bar_Chart.py
  Demo_Base64_Image_Encoder.py
  Demo_Base64_Single_Image_Encoder.py
  Demo_Borderless_Window.py
  Demo_Button_Can_Button_Images.py
  Demo_Button_Click.py
  Demo_Button_Events_From_Browse.py
  Demo_Button_Func_Calls.py
  Demo_Button_Simulated_With_Highlighting_Using_Bind.py
  Demo_Button_States.py
  Demo_Button_Toggle.py
  Demo_Button_Toggle2.py
  Demo_Button_Toggle_Simple_Graphic.py
  Demo_Buttons_Base64_Simple.py
  Demo_Buttons_Base64_User_Settings.py
  Demo_Buttons_Mac.py
  Demo_Buttons_Nice_Graphics.py
  Demo_Buttons_Realtime.py
  … 314 more files
PySimpleGUI/  (4 files)
  CONTRIBUTING.md
  LICENSE.txt
  __init__.py
  __main__.py
.gitignore
CONTRIBUTING.md
LICENSE.txt
README.md
requirements.txt
setup.py
```

## Entry points

- [DemoPrograms/Browser_START_HERE_Demo_Programs_Browser.py:1106](https://github.com/PySimpleGUI/PySimpleGUI/blob/00de5ab857f56014294cb0a5c725a96d32eb7af6/DemoPrograms/Browser_START_HERE_Demo_Programs_Browser.py#L1106)
- [DemoPrograms/Demo_All_Elements.py:160](https://github.com/PySimpleGUI/PySimpleGUI/blob/00de5ab857f56014294cb0a5c725a96d32eb7af6/DemoPrograms/Demo_All_Elements.py#L160)
- [DemoPrograms/Demo_Auto_Save_Window_Position.py:45](https://github.com/PySimpleGUI/PySimpleGUI/blob/00de5ab857f56014294cb0a5c725a96d32eb7af6/DemoPrograms/Demo_Auto_Save_Window_Position.py#L45)
- [DemoPrograms/Demo_Base64_Image_Encoder.py:42](https://github.com/PySimpleGUI/PySimpleGUI/blob/00de5ab857f56014294cb0a5c725a96d32eb7af6/DemoPrograms/Demo_Base64_Image_Encoder.py#L42)
- [DemoPrograms/Demo_Base64_Single_Image_Encoder.py:39](https://github.com/PySimpleGUI/PySimpleGUI/blob/00de5ab857f56014294cb0a5c725a96d32eb7af6/DemoPrograms/Demo_Base64_Single_Image_Encoder.py#L39)
- [DemoPrograms/Demo_Button_Can_Button_Images.py:44](https://github.com/PySimpleGUI/PySimpleGUI/blob/00de5ab857f56014294cb0a5c725a96d32eb7af6/DemoPrograms/Demo_Button_Can_Button_Images.py#L44)
- [DemoPrograms/Demo_Button_Simulated_With_Highlighting_Using_Bind.py:80](https://github.com/PySimpleGUI/PySimpleGUI/blob/00de5ab857f56014294cb0a5c725a96d32eb7af6/DemoPrograms/Demo_Button_Simulated_With_Highlighting_Using_Bind.py#L80)
- [DemoPrograms/Demo_Button_Toggle.py:38](https://github.com/PySimpleGUI/PySimpleGUI/blob/00de5ab857f56014294cb0a5c725a96d32eb7af6/DemoPrograms/Demo_Button_Toggle.py#L38)
- [DemoPrograms/Demo_Button_Toggle2.py:107](https://github.com/PySimpleGUI/PySimpleGUI/blob/00de5ab857f56014294cb0a5c725a96d32eb7af6/DemoPrograms/Demo_Button_Toggle2.py#L107)
- [DemoPrograms/Demo_Button_Toggle_Simple_Graphic.py:34](https://github.com/PySimpleGUI/PySimpleGUI/blob/00de5ab857f56014294cb0a5c725a96d32eb7af6/DemoPrograms/Demo_Button_Toggle_Simple_Graphic.py#L34)
- [DemoPrograms/Demo_Buttons_Base64_User_Settings.py:82](https://github.com/PySimpleGUI/PySimpleGUI/blob/00de5ab857f56014294cb0a5c725a96d32eb7af6/DemoPrograms/Demo_Buttons_Base64_User_Settings.py#L82)
- [DemoPrograms/Demo_Buttons_Nice_Graphics.py:86](https://github.com/PySimpleGUI/PySimpleGUI/blob/00de5ab857f56014294cb0a5c725a96d32eb7af6/DemoPrograms/Demo_Buttons_Nice_Graphics.py#L86)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: readme. |
| DemoPrograms package | library | Observed | Groups 175 file(s) under demoprograms package (observed from repository paths and static analysis). Observed top-level classes: Ball, Item, Playfield, SampleGUI, Toolbar. Observed top-level functions: ArtistBoxplot2, Ax… |
| Application entry point | entrypoint | Observed | Groups 162 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Group. Observed top-level classes: Ball, BtnInfo, DashGraph, G, GUI, Gauge.… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| PySimpleGUI package | library | Observed | Groups 1 file(s) under pysimplegui package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/close_prs.yml` (ci)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `DemoPrograms` — 338 analysed file(s)
- `(root files)` — 6 analysed file(s)
- `.github` — 4 analysed file(s)
- `PySimpleGUI` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `00de5ab857f56014294cb0a5c725a96d32eb7af6` is the revision these paths and observations refer to.
