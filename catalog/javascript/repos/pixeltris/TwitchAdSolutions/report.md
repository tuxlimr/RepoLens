# Architecture report: pixeltris/TwitchAdSolutions

> Automated static analysis. **Observed** = directly seen in files/imports/AST; **Inferred** = interpretation from that evidence. Repository code was not executed.

## 1. Repository at a glance

| Item | Value |
| --- | --- |
| Repository | pixeltris/TwitchAdSolutions |
| Description | Not provided |
| Language | JavaScript |
| Stars | 11316 |
| Licence | MIT |
| Analysed commit / branch | c51ef2fe8f667f9dc9216eb550924cf0d732ce27 / master |
| Framework(s) | None detected |
| Files analysed | 10 |
| Components | 3 |

## 2. Architecture in one minute

pixeltris/TwitchAdSolutions. This repository was analysed statically from 10 file(s) (0 Python). Detected technologies (observed from imports/manifests): GitHub Actions. Files are grouped into 3 component(s): strip package, vaft package, video-swap-new package. Findings below distinguish observed facts from inferred interpretation.

## 3. High-level block diagram

```mermaid
flowchart TD
    strip["strip package"]
    vaft["vaft package"]
    video_swap_new["video-swap-new package"]
```

## 4. Main components

### strip package (`strip`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under strip package (observed from repository paths and static analysis).
- **Paths:** `strip/strip.user.js`
- **Evidence:** [strip/strip.user.js](https://github.com/pixeltris/TwitchAdSolutions/blob/c51ef2fe8f667f9dc9216eb550924cf0d732ce27/strip/strip.user.js)

### vaft package (`vaft`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 2 file(s) under vaft package (observed from repository paths and static analysis).
- **Paths:** `vaft/vaft-ublock-origin.js`, `vaft/vaft.user.js`
- **Evidence:** [vaft/vaft-ublock-origin.js](https://github.com/pixeltris/TwitchAdSolutions/blob/c51ef2fe8f667f9dc9216eb550924cf0d732ce27/vaft/vaft-ublock-origin.js); [vaft/vaft.user.js](https://github.com/pixeltris/TwitchAdSolutions/blob/c51ef2fe8f667f9dc9216eb550924cf0d732ce27/vaft/vaft.user.js)

### video-swap-new package (`video_swap_new`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 2 file(s) under video-swap-new package (observed from repository paths and static analysis).
- **Paths:** `video-swap-new/video-swap-new-ublock-origin.js`, `video-swap-new/video-swap-new.user.js`
- **Evidence:** [video-swap-new/video-swap-new-ublock-origin.js](https://github.com/pixeltris/TwitchAdSolutions/blob/c51ef2fe8f667f9dc9216eb550924cf0d732ce27/video-swap-new/video-swap-new-ublock-origin.js); [video-swap-new/video-swap-new.user.js](https://github.com/pixeltris/TwitchAdSolutions/blob/c51ef2fe8f667f9dc9216eb550924cf0d732ce27/video-swap-new/video-swap-new.user.js)

## 5. Execution flow

No entry point was observed; the startup flow below is therefore limited.

Representative flow (derived from observed entry points and the import graph; steps beyond the entry point are **Inferred**):

1. Execution starts at an observed entry point listed above, if present.
2. No internal import relationships between components were observed.

## 6. Project structure

### `(root)`

- `LICENSE` - docs (1095 bytes)
- `README.md` - docs (4728 bytes)
- `full-list.md` - docs (7410 bytes)
- `issues.md` - docs (3277 bytes)

### `.github`

- `.github/workflows/release.yml` - ci, YAML (1005 bytes)

### `strip`

- `strip/strip.user.js` - source, JavaScript (26832 bytes)

### `vaft`

- `vaft/vaft-ublock-origin.js` - source, JavaScript (60183 bytes)
- `vaft/vaft.user.js` - source, JavaScript (60670 bytes)

### `video-swap-new`

- `video-swap-new/video-swap-new-ublock-origin.js` - source, JavaScript (51042 bytes)
- `video-swap-new/video-swap-new.user.js` - source, JavaScript (51556 bytes)

## 7. Key dependencies and integrations

| Name | Category | Status | Confidence | Evidence |
| --- | --- | --- | --- | --- |
| GitHub Actions | ci | Observed | 0.85 | [.github/workflows/release.yml](https://github.com/pixeltris/TwitchAdSolutions/blob/c51ef2fe8f667f9dc9216eb550924cf0d732ce27/.github/workflows/release.yml) |

## 8. Data and state

No database, cache, queue, or persistent-state usage was observed in the analysed files. State handling, if any, may be in-memory or in files that were not analysed.

## 9. Configuration and deployment clues

- `.github/workflows/release.yml` (ci)

## 10. Design observations

- No strong design patterns could be established from the available evidence.

These observations are interpretations (**Inferred**) of the observed structure, not guarantees about runtime design.

## 11. Limitations and unknowns

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.
- The GitHub repository was marked archived at selection time.

## 12. Source references

- [.github/workflows/release.yml](https://github.com/pixeltris/TwitchAdSolutions/blob/c51ef2fe8f667f9dc9216eb550924cf0d732ce27/.github/workflows/release.yml)
- [strip/strip.user.js](https://github.com/pixeltris/TwitchAdSolutions/blob/c51ef2fe8f667f9dc9216eb550924cf0d732ce27/strip/strip.user.js)
- [vaft/vaft-ublock-origin.js](https://github.com/pixeltris/TwitchAdSolutions/blob/c51ef2fe8f667f9dc9216eb550924cf0d732ce27/vaft/vaft-ublock-origin.js)
- [vaft/vaft.user.js](https://github.com/pixeltris/TwitchAdSolutions/blob/c51ef2fe8f667f9dc9216eb550924cf0d732ce27/vaft/vaft.user.js)
- [video-swap-new/video-swap-new-ublock-origin.js](https://github.com/pixeltris/TwitchAdSolutions/blob/c51ef2fe8f667f9dc9216eb550924cf0d732ce27/video-swap-new/video-swap-new-ublock-origin.js)
- [video-swap-new/video-swap-new.user.js](https://github.com/pixeltris/TwitchAdSolutions/blob/c51ef2fe8f667f9dc9216eb550924cf0d732ce27/video-swap-new/video-swap-new.user.js)
