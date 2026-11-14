# Project structure: nondanee/UnblockNeteaseMusic

**Analysed commit:** `b8d5f4b4fe59cef9c021b99f3cf2606d99fa4790`

**Commit reference:** [b8d5f4b4fe59cef9c021b99f3cf2606d99fa4790](https://github.com/nondanee/UnblockNeteaseMusic/commit/b8d5f4b4fe59cef9c021b99f3cf2606d99fa4790)

**Tree at this commit:** [nondanee/UnblockNeteaseMusic@b8d5f4b4fe59](https://github.com/nondanee/UnblockNeteaseMusic/tree/b8d5f4b4fe59cef9c021b99f3cf2606d99fa4790)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nondanee/UnblockNeteaseMusic |
| Description | Revive unavailable songs for Netease Cloud Music |
| Stars | 17326 |
| Forks | 2431 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `b8d5f4b4fe59cef9c021b99f3cf2606d99fa4790` |
| Retrieved at | 2026-11-14T19:11:27.999102+00:00 |
| Files in this snapshot | 46 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    publish.yml
src/  (32 files)
  browser/  (9 files)
    README.md
    background.html
    background.js
    convert.js
    crypto.js
    inject.js
    manifest.json
    request.js
    script.js
  provider/  (13 files)
    baidu.js
    find.js
    insure.js
    joox.js
    kugou.js
    kuwo.js
    match.js
    migu.js
    netease.js
    qq.js
    select.js
    xiami.js
    youtube.js
  app.js
  bridge.js
  cache.js
  cli.js
  crypto.js
  hook.js
  kwDES.js
  request.js
  server.js
  sni.js
.dockerignore
.gitignore
.npmignore
Dockerfile
LICENSE
README.md
app.js
bridge.js
ca.crt
docker-compose.yml
endpoint.worker.js
package.json
server.crt
```

## Entry points

- [src/provider/match.js](https://github.com/nondanee/UnblockNeteaseMusic/blob/b8d5f4b4fe59cef9c021b99f3cf2606d99fa4790/src/provider/match.js)
- [app.js](https://github.com/nondanee/UnblockNeteaseMusic/blob/b8d5f4b4fe59cef9c021b99f3cf2606d99fa4790/app.js)
- [src/app.js](https://github.com/nondanee/UnblockNeteaseMusic/blob/b8d5f4b4fe59cef9c021b99f3cf2606d99fa4790/src/app.js)
- [src/server.js](https://github.com/nondanee/UnblockNeteaseMusic/blob/b8d5f4b4fe59cef9c021b99f3cf2606d99fa4790/src/server.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| app.js package | library | Observed | Groups 1 file(s) under app.js package (observed from repository paths and static analysis). |
| bridge.js package | library | Observed | Groups 1 file(s) under bridge.js package (observed from repository paths and static analysis). |
| browser package | library | Observed | Groups 6 file(s) under browser package (observed from repository paths and static analysis). |
| cache.js package | library | Observed | Groups 1 file(s) under cache.js package (observed from repository paths and static analysis). |
| cli.js package | library | Observed | Groups 1 file(s) under cli.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 4 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 3 file(s) under core modules (observed from repository paths and static analysis). |
| crypto.js package | library | Observed | Groups 1 file(s) under crypto.js package (observed from repository paths and static analysis). |
| hook.js package | library | Observed | Groups 1 file(s) under hook.js package (observed from repository paths and static analysis). |
| kwDES.js package | library | Observed | Groups 1 file(s) under kwdes.js package (observed from repository paths and static analysis). |
| provider package | library | Observed | Groups 13 file(s) under provider package (observed from repository paths and static analysis). |
| request.js package | library | Observed | Groups 1 file(s) under request.js package (observed from repository paths and static analysis). |
| server.js package | library | Observed | Groups 1 file(s) under server.js package (observed from repository paths and static analysis). |
| sni.js package | library | Observed | Groups 1 file(s) under sni.js package (observed from repository paths and static analysis). |

## Important files

- `.dockerignore` (container)
- `.github/workflows/publish.yml` (ci)
- `Dockerfile` (container)
- `docker-compose.yml` (container)
- `package.json` (manifest)
- `src/browser/manifest.json` (config)

## Top-level layout

- `src` — 32 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `.github` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b8d5f4b4fe59cef9c021b99f3cf2606d99fa4790` is the revision these paths and observations refer to.
