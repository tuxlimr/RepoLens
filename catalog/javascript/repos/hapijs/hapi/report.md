# Architecture report: hapijs/hapi

> Automated static analysis. **Observed** = directly seen in files/imports/AST; **Inferred** = interpretation from that evidence. Repository code was not executed.

## 1. Repository at a glance

| Item | Value |
| --- | --- |
| Repository | hapijs/hapi |
| Description | The Simple, Secure Framework Developers Trust |
| Language | JavaScript |
| Stars | 14798 |
| Licence | Other |
| Analysed commit / branch | f2837a006535a6fbbcf33692067c1bd497ba8124 / master |
| Framework(s) | None detected |
| Files analysed | 70 |
| Components | 3 |

## 2. Architecture in one minute

hapijs/hapi - The Simple, Secure Framework Developers Trust. This repository was analysed statically from 70 file(s) (0 Python). Detected technologies (observed from imports/manifests): GitHub Actions, TypeScript. Files are grouped into 3 component(s): Configuration and deployment, lib package, Tests. Findings below distinguish observed facts from inferred interpretation.

## 3. High-level block diagram

```mermaid
flowchart TD
    subgraph config_group
        config["Configuration and deployment"]
    end
    subgraph library_group
        lib["lib package"]
    end
    subgraph test_group
        tests["Tests"]
    end
```

## 4. Main components

### Configuration and deployment (`config`)

- **Kind:** config
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis).
- **Paths:** `package.json`
- **Evidence:** [package.json](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/package.json)

### lib package (`lib`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 38 file(s) under lib package (observed from repository paths and static analysis).
- **Paths:** `lib/auth.js`, `lib/compression.js`, `lib/config.js`, `lib/core.js`, `lib/cors.js`, `lib/ext.js`, `lib/handler.js`, `lib/headers.js`, `lib/index.d.ts`, `lib/index.js`, `lib/methods.js`, `lib/request.js`, `lib/response.js`, `lib/route.js`, `lib/security.js`, `lib/server.js`, `lib/streams.js`, `lib/toolkit.js`, `lib/transmit.js`, `lib/types/index.d.ts`, `lib/types/plugin.d.ts`, `lib/types/request.d.ts`, `lib/types/response.d.ts`, `lib/types/route.d.ts`, `lib/types/server/auth.d.ts`, `lib/types/server/cache.d.ts`, `lib/types/server/encoders.d.ts`, `lib/types/server/events.d.ts`, `lib/types/server/ext.d.ts`, `lib/types/server/index.d.ts`, `lib/types/server/info.d.ts`, `lib/types/server/inject.d.ts`, `lib/types/server/methods.d.ts`, `lib/types/server/options.d.ts`, `lib/types/server/server.d.ts`, `lib/types/server/state.d.ts`, `lib/types/utils.d.ts`, `lib/validation.js`
- **Evidence:** [lib/auth.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/auth.js); [lib/compression.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/compression.js); [lib/config.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/config.js); [lib/core.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/core.js); [lib/cors.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/cors.js); [lib/ext.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/ext.js); [lib/handler.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/handler.js); [lib/headers.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/headers.js)

### Tests (`tests`)

- **Kind:** test
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 24 file(s) under tests (observed from repository paths and static analysis).
- **Paths:** `test/.hidden`, `test/auth.js`, `test/common.js`, `test/core.js`, `test/cors.js`, `test/file/note.txt`, `test/handler.js`, `test/headers.js`, `test/index.js`, `test/methods.js`, `test/payload.js`, `test/request.js`, `test/response.js`, `test/route.js`, `test/security.js`, `test/server.js`, `test/state.js`, `test/templates/invalid.html`, `test/templates/plugin/test.html`, `test/templates/test.html`, `test/toolkit.js`, `test/transmit.js`, `test/types/index.ts`, `test/validation.js`
- **Evidence:** [test/.hidden](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/.hidden); [test/auth.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/auth.js); [test/common.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/common.js); [test/core.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/core.js); [test/cors.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/cors.js); [test/file/note.txt](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/file/note.txt); [test/handler.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/handler.js); [test/headers.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/headers.js)

## 5. Execution flow

**Observed** entry point(s):

- [lib/index.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/index.js)
- [lib/server.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/server.js)

Representative flow (derived from observed entry points and the import graph; steps beyond the entry point are **Inferred**):

1. Execution starts at an observed entry point listed above, if present.
2. No internal import relationships between components were observed.

## 6. Project structure

### `(root)`

- `.gitignore` - other (108 bytes)
- `API.md` - docs (197919 bytes)
- `LICENSE.md` - docs (1556 bytes)
- `README.md` - docs (1123 bytes)
- `SPONSORS.md` - docs (691 bytes)
- `package.json` - manifest (1697 bytes)
- `typescript.md` - docs (23312 bytes)

### `.github`

- `.github/workflows/ci-module.yml` - ci, YAML (216 bytes)

### `lib`

- `lib/auth.js` - source, JavaScript (16596 bytes)
- `lib/compression.js` - source, JavaScript (3242 bytes)
- `lib/config.js` - source, JavaScript (15506 bytes)
- `lib/core.js` - source, JavaScript (22167 bytes)
- `lib/cors.js` - source, JavaScript (5409 bytes)
- `lib/ext.js` - source, JavaScript (2301 bytes)
- `lib/handler.js` - source, JavaScript (3928 bytes)
- `lib/headers.js` - source, JavaScript (5027 bytes)
- `lib/index.d.ts` - source, TypeScript (25 bytes)
- `lib/index.js` - source, JavaScript (128 bytes)
- `lib/methods.js` - source, JavaScript (3579 bytes)
- `lib/request.js` - source, JavaScript (25209 bytes)
- `lib/response.js` - source, JavaScript (18984 bytes)
- `lib/route.js` - source, JavaScript (14004 bytes)
- `lib/security.js` - source, JavaScript (2419 bytes)
- `lib/server.js` - source, JavaScript (19122 bytes)
- `lib/streams.js` - source, JavaScript (1326 bytes)
- `lib/toolkit.js` - source, JavaScript (6664 bytes)
- `lib/transmit.js` - source, JavaScript (9923 bytes)
- `lib/types/index.d.ts` - source, TypeScript (629 bytes)
- `lib/types/plugin.d.ts` - source, TypeScript (11150 bytes)
- `lib/types/request.d.ts` - source, TypeScript (23840 bytes)
- `lib/types/response.d.ts` - source, TypeScript (27791 bytes)
- `lib/types/route.d.ts` - source, TypeScript (55405 bytes)
- `lib/types/server/auth.d.ts` - source, TypeScript (9765 bytes)
- `lib/types/server/cache.d.ts` - source, TypeScript (5706 bytes)
- `lib/types/server/encoders.d.ts` - source, TypeScript (533 bytes)
- `lib/types/server/events.d.ts` - source, TypeScript (12509 bytes)
- `lib/types/server/ext.d.ts` - source, TypeScript (10498 bytes)
- `lib/types/server/index.d.ts` - source, TypeScript (281 bytes)
- `lib/types/server/info.d.ts` - source, TypeScript (1752 bytes)
- `lib/types/server/inject.d.ts` - source, TypeScript (5389 bytes)
- `lib/types/server/methods.d.ts` - source, TypeScript (4098 bytes)
- `lib/types/server/options.d.ts` - source, TypeScript (12963 bytes)
- `lib/types/server/server.d.ts` - source, TypeScript (44740 bytes)
- `lib/types/server/state.d.ts` - source, TypeScript (3237 bytes)
- `lib/types/utils.d.ts` - source, TypeScript (5130 bytes)
- `lib/validation.js` - source, JavaScript (6529 bytes)

### `test`

- `test/.hidden` - test (7 bytes)
- `test/auth.js` - test, JavaScript (76641 bytes)
- `test/common.js` - test, JavaScript (908 bytes)
- `test/core.js` - test, JavaScript (84468 bytes)
- `test/cors.js` - test, JavaScript (30172 bytes)
- `test/file/note.txt` - test (4 bytes)
- `test/handler.js` - test, JavaScript (19440 bytes)
- `test/headers.js` - test, JavaScript (24825 bytes)
- `test/index.js` - test, JavaScript (530 bytes)
- `test/methods.js` - test, JavaScript (21864 bytes)
- `test/payload.js` - test, JavaScript (35980 bytes)
- `test/request.js` - test, JavaScript (98628 bytes)
- `test/response.js` - test, JavaScript (50335 bytes)
- `test/route.js` - test, JavaScript (28892 bytes)
- `test/security.js` - test, JavaScript (2933 bytes)
- `test/server.js` - test, JavaScript (96327 bytes)
- `test/state.js` - test, JavaScript (13891 bytes)
- `test/templates/invalid.html` - test (34 bytes)
- `test/templates/plugin/test.html` - test (20 bytes)
- `test/templates/test.html` - test (38 bytes)
- `test/toolkit.js` - test, JavaScript (21503 bytes)
- `test/transmit.js` - test, JavaScript (83278 bytes)
- `test/types/index.ts` - test, TypeScript (17835 bytes)
- `test/validation.js` - test, JavaScript (59028 bytes)

## 7. Key dependencies and integrations

| Name | Category | Status | Confidence | Evidence |
| --- | --- | --- | --- | --- |
| GitHub Actions | ci | Observed | 0.85 | [.github/workflows/ci-module.yml](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/.github/workflows/ci-module.yml) |
| TypeScript | tooling | Observed | 0.85 | [package.json:58](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/package.json#L58) |

## 8. Data and state

No database, cache, queue, or persistent-state usage was observed in the analysed files. State handling, if any, may be in-memory or in files that were not analysed.

## 9. Configuration and deployment clues

- `.github/workflows/ci-module.yml` (ci)
- `package.json` (manifest)

## 10. Design observations

- Tests are present alongside source code (Observed from test file paths).

These observations are interpretations (**Inferred**) of the observed structure, not guarantees about runtime design.

## 11. Limitations and unknowns

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

## 12. Source references

- [.github/workflows/ci-module.yml](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/.github/workflows/ci-module.yml)
- [lib/auth.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/auth.js)
- [lib/compression.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/compression.js)
- [lib/config.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/config.js)
- [lib/core.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/core.js)
- [lib/cors.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/cors.js)
- [lib/ext.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/ext.js)
- [lib/handler.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/handler.js)
- [lib/headers.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/headers.js)
- [lib/index.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/index.js)
- [lib/server.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/lib/server.js)
- [package.json](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/package.json)
- [package.json:58](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/package.json#L58)
- [test/.hidden](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/.hidden)
- [test/auth.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/auth.js)
- [test/common.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/common.js)
- [test/core.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/core.js)
- [test/cors.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/cors.js)
- [test/file/note.txt](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/file/note.txt)
- [test/handler.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/handler.js)
- [test/headers.js](https://github.com/hapijs/hapi/blob/f2837a006535a6fbbcf33692067c1bd497ba8124/test/headers.js)
