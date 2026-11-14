# Project structure: novnc/noVNC

**Analysed commit:** `e8b5024d4603587b29ffede4fbd28b1fa2939829`

**Commit reference:** [e8b5024d4603587b29ffede4fbd28b1fa2939829](https://github.com/novnc/noVNC/commit/e8b5024d4603587b29ffede4fbd28b1fa2939829)

**Tree at this commit:** [novnc/noVNC@e8b5024d4603](https://github.com/novnc/noVNC/tree/e8b5024d4603587b29ffede4fbd28b1fa2939829)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | novnc/noVNC |
| Description | VNC client web application |
| Stars | 14206 |
| Forks | 2705 |
| Licence | Other |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `e8b5024d4603587b29ffede4fbd28b1fa2939829` |
| Retrieved at | 2026-11-14T19:11:45.979923+00:00 |
| Files in this snapshot | 192 |

## Directory tree

```text
.github/  (7 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    config.yml
    feature_request.md
  workflows/  (4 files)
    deploy.yml
    lint.yml
    test.yml
    translate.yml
app/  (54 files)
  images/  (26 files)
    icons/  (5 files)
      … 5 files under this directory
    alt.svg
    clipboard.svg
    connect.svg
    ctrl.svg
    ctrlaltdel.svg
    disconnect.svg
    drag.svg
    error.svg
    esc.svg
    expander.svg
    fullscreen.svg
    handle.svg
    handle_bg.svg
    info.svg
    keyboard.svg
    power.svg
    settings.svg
    tab.svg
    toggleextrakeys.svg
    warning.svg
    windows.svg
  locale/  (19 files)
    README
    cs.json
    de.json
    el.json
    es.json
    fr.json
    hu.json
    it.json
    ja.json
    ko.json
    nl.json
    pl.json
    pt_BR.json
    ru.json
    sv.json
    tr.json
    uk.json
    zh_CN.json
    zh_TW.json
  sounds/  (1 files)
    CREDITS
  styles/  (3 files)
    base.css
    constants.css
    input.css
  error-handler.js
  localization.js
  ui.js
  wakelock.js
  webutil.js
core/  (43 files)
  crypto/  (7 files)
    aes.js
    bigint.js
    crypto.js
    des.js
    dh.js
    md5.js
    rsa.js
  decoders/  (10 files)
    copyrect.js
    h264.js
    hextile.js
    jpeg.js
    raw.js
    rre.js
    tight.js
    tightpng.js
    zlib.js
    zrle.js
  input/  (9 files)
    domkeytable.js
    fixedkeys.js
    gesturehandler.js
    keyboard.js
    keysym.js
    keysymdef.js
    util.js
    vkeys.js
    xtscancodes.js
  util/  (8 files)
    browser.js
    cursor.js
    element.js
    events.js
    eventtarget.js
    int.js
    logging.js
    strings.js
  base64.js
  clipboard.js
  deflator.js
  display.js
  encodings.js
  inflator.js
  ra2.js
  rfb.js
  websock.js
docs/  (13 files)
  API-internal.md
  API.md
  EMBEDDING.md
  LIBRARY.md
  LICENSE.BSD-2-Clause
  LICENSE.BSD-3-Clause
  LICENSE.MPL-2.0
  LICENSE.OFL-1.1
  flash_policy.txt
  links
  notes
  novnc_proxy.1
  rfb_notes
po/  (23 files)
  Makefile
  cs.po
  de.po
  el.po
  es.po
  fr.po
  hr.po
  hu.po
  it.po
  ja.po
  ko.po
  nl.po
  noVNC.pot
  pl.po
  po2js
  pt_BR.po
  ru.po
  sv.po
  tr.po
  uk.po
  xgettext-html
  zh_CN.po
  zh_TW.po
snap/  (3 files)
  hooks/  (1 files)
    configure
  local/  (1 files)
    svc_wrapper.sh
  snapcraft.yaml
tests/  (30 files)
  assertions.js
  fake.websocket.js
  playback-ui.js
  playback.js
  test.base64.js
  test.browser.js
  test.clipboard.js
  test.copyrect.js
  test.deflator.js
  test.display.js
  test.gesturehandler.js
  test.h264.js
  test.helper.js
  test.hextile.js
  test.inflator.js
  test.int.js
  test.jpeg.js
  test.keyboard.js
  test.localization.js
  test.raw.js
  test.rre.js
  test.tight.js
  test.tightpng.js
  test.util.js
  … 6 more files
utils/  (6 files)
  README.md
  b64-to-binary.pl
  genkeysymdef.js
  novnc_proxy
  u2x11
  validate
.gitignore
.gitmodules
AI_POLICY.md
AUTHORS
LICENSE.txt
README.md
defaults.json
eslint.config.mjs
karma.conf.cjs
mandatory.json
package.json
vnc.html
vnc_lite.html
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app package | library | Observed | Groups 5 file(s) under app package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 22 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 43 file(s) under service / domain layer (observed from repository paths and static analysis). |
| snap package | library | Observed | Groups 1 file(s) under snap package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 30 file(s) under tests (observed from repository paths and static analysis). |
| utils package | library | Observed | Groups 1 file(s) under utils package (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/deploy.yml` (ci)
- `.github/workflows/lint.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.github/workflows/translate.yml` (ci)
- `app/locale/cs.json` (config)
- `app/locale/de.json` (config)
- `app/locale/el.json` (config)
- `app/locale/es.json` (config)
- `app/locale/fr.json` (config)
- `app/locale/hu.json` (config)
- `app/locale/it.json` (config)
- `app/locale/ja.json` (config)
- `app/locale/ko.json` (config)
- `app/locale/nl.json` (config)
- `app/locale/pl.json` (config)
- `app/locale/pt_BR.json` (config)
- `app/locale/ru.json` (config)
- `app/locale/sv.json` (config)
- `app/locale/tr.json` (config)
- `app/locale/uk.json` (config)
- `app/locale/zh_CN.json` (config)
- `app/locale/zh_TW.json` (config)
- `defaults.json` (config)
- `mandatory.json` (config)
- `package.json` (manifest)
- `snap/snapcraft.yaml` (config)

## Top-level layout

- `app` — 54 analysed file(s)
- `core` — 43 analysed file(s)
- `tests` — 30 analysed file(s)
- `po` — 23 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `docs` — 13 analysed file(s)
- `.github` — 7 analysed file(s)
- `utils` — 6 analysed file(s)
- `snap` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 14 file(s) were skipped during inventory (14 x vendored/generated directory excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `e8b5024d4603587b29ffede4fbd28b1fa2939829` is the revision these paths and observations refer to.
