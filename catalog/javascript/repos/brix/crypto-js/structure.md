# Project structure: brix/crypto-js

**Analysed commit:** `ac34a5a584337b33a2e567f50d96819a96ac44bf`

**Commit reference:** [ac34a5a584337b33a2e567f50d96819a96ac44bf](https://github.com/brix/crypto-js/commit/ac34a5a584337b33a2e567f50d96819a96ac44bf)

**Tree at this commit:** [brix/crypto-js@ac34a5a58433](https://github.com/brix/crypto-js/tree/ac34a5a584337b33a2e567f50d96819a96ac44bf)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | brix/crypto-js |
| Description | JavaScript library of crypto standards. |
| Stars | 16398 |
| Forks | 2488 |
| Licence | Other |
| Language | JavaScript |
| Default branch | develop |
| Analysed commit | `ac34a5a584337b33a2e567f50d96819a96ac44bf` |
| Retrieved at | 2026-11-14T19:11:33.037718+00:00 |
| Files in this snapshot | 117 |

## Directory tree

```text
docs/  (1 files)
  QuickStartGuide.wiki
grunt/  (7 files)
  config/  (6 files)
    clean.js
    copy.js
    jshint.js
    jsonlint.js
    modularize.js
    update_json.js
  tasks/  (1 files)
    modularize.js
src/  (35 files)
  aes.js
  blowfish.js
  cipher-core.js
  core.js
  enc-base64.js
  enc-base64url.js
  enc-utf16.js
  evpkdf.js
  format-hex.js
  hmac.js
  lib-typedarrays.js
  md5.js
  mode-cfb.js
  mode-ctr-gladman.js
  mode-ctr.js
  mode-ecb.js
  mode-ofb.js
  pad-ansix923.js
  pad-iso10126.js
  pad-iso97971.js
  pad-nopadding.js
  pad-zeropadding.js
  pbkdf2.js
  rabbit-legacy.js
  … 11 more files
test/  (66 files)
  aes-profile.js
  aes-test.js
  blowfish-test.js
  cipher-test.js
  config-test.js
  des-profile.js
  des-test.js
  enc-base64-test.js
  enc-hex-test.js
  enc-latin1-test.js
  enc-utf16-test.js
  enc-utf8-test.js
  evpkdf-profile.js
  evpkdf-test.js
  format-openssl-test.js
  hmac-md5-profile.js
  hmac-md5-test.js
  hmac-sha224-test.js
  hmac-sha256-test.js
  hmac-sha384-test.js
  hmac-sha512-test.js
  kdf-openssl-test.js
  lib-base-test.js
  lib-cipherparams-test.js
  … 42 more files
.gitignore
.jshintrc
.travis.yml
CONTRIBUTING.md
Gruntfile.js
LICENSE
README.md
package.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| aes.js package | library | Observed | Groups 1 file(s) under aes.js package (observed from repository paths and static analysis). |
| blowfish.js package | library | Observed | Groups 1 file(s) under blowfish.js package (observed from repository paths and static analysis). |
| cipher-core.js package | library | Observed | Groups 1 file(s) under cipher-core.js package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 7 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| core.js package | library | Observed | Groups 1 file(s) under core.js package (observed from repository paths and static analysis). |
| enc-base64.js package | library | Observed | Groups 1 file(s) under enc-base64.js package (observed from repository paths and static analysis). |
| enc-base64url.js package | library | Observed | Groups 1 file(s) under enc-base64url.js package (observed from repository paths and static analysis). |
| enc-utf16.js package | library | Observed | Groups 1 file(s) under enc-utf16.js package (observed from repository paths and static analysis). |
| evpkdf.js package | library | Observed | Groups 1 file(s) under evpkdf.js package (observed from repository paths and static analysis). |
| format-hex.js package | library | Observed | Groups 1 file(s) under format-hex.js package (observed from repository paths and static analysis). |
| grunt package | library | Observed | Groups 1 file(s) under grunt package (observed from repository paths and static analysis). |
| hmac.js package | library | Observed | Groups 1 file(s) under hmac.js package (observed from repository paths and static analysis). |
| lib-typedarrays.js package | library | Observed | Groups 1 file(s) under lib-typedarrays.js package (observed from repository paths and static analysis). |
| md5.js package | library | Observed | Groups 1 file(s) under md5.js package (observed from repository paths and static analysis). |
| mode-cfb.js package | library | Observed | Groups 1 file(s) under mode-cfb.js package (observed from repository paths and static analysis). |
| mode-ctr-gladman.js package | library | Observed | Groups 1 file(s) under mode-ctr-gladman.js package (observed from repository paths and static analysis). |
| mode-ctr.js package | library | Observed | Groups 1 file(s) under mode-ctr.js package (observed from repository paths and static analysis). |
| mode-ecb.js package | library | Observed | Groups 1 file(s) under mode-ecb.js package (observed from repository paths and static analysis). |
| mode-ofb.js package | library | Observed | Groups 1 file(s) under mode-ofb.js package (observed from repository paths and static analysis). |
| pad-ansix923.js package | library | Observed | Groups 1 file(s) under pad-ansix923.js package (observed from repository paths and static analysis). |
| pad-iso10126.js package | library | Observed | Groups 1 file(s) under pad-iso10126.js package (observed from repository paths and static analysis). |
| pad-iso97971.js package | library | Observed | Groups 1 file(s) under pad-iso97971.js package (observed from repository paths and static analysis). |
| pad-nopadding.js package | library | Observed | Groups 1 file(s) under pad-nopadding.js package (observed from repository paths and static analysis). |
| pad-zeropadding.js package | library | Observed | Groups 1 file(s) under pad-zeropadding.js package (observed from repository paths and static analysis). |
| pbkdf2.js package | library | Observed | Groups 1 file(s) under pbkdf2.js package (observed from repository paths and static analysis). |
| rabbit.js package | library | Observed | Groups 1 file(s) under rabbit.js package (observed from repository paths and static analysis). |
| rabbit-legacy.js package | library | Observed | Groups 1 file(s) under rabbit-legacy.js package (observed from repository paths and static analysis). |
| rc4.js package | library | Observed | Groups 1 file(s) under rc4.js package (observed from repository paths and static analysis). |
| ripemd160.js package | library | Observed | Groups 1 file(s) under ripemd160.js package (observed from repository paths and static analysis). |
| sha1.js package | library | Observed | Groups 1 file(s) under sha1.js package (observed from repository paths and static analysis). |
| sha224.js package | library | Observed | Groups 1 file(s) under sha224.js package (observed from repository paths and static analysis). |
| sha256.js package | library | Observed | Groups 1 file(s) under sha256.js package (observed from repository paths and static analysis). |
| sha384.js package | library | Observed | Groups 1 file(s) under sha384.js package (observed from repository paths and static analysis). |
| sha3.js package | library | Observed | Groups 1 file(s) under sha3.js package (observed from repository paths and static analysis). |
| sha512.js package | library | Observed | Groups 1 file(s) under sha512.js package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 66 file(s) under tests (observed from repository paths and static analysis). |
| tripledes.js package | library | Observed | Groups 1 file(s) under tripledes.js package (observed from repository paths and static analysis). |
| x64-core.js package | library | Observed | Groups 1 file(s) under x64-core.js package (observed from repository paths and static analysis). |

## Important files

- `.travis.yml` (ci)
- `package.json` (manifest)

## Top-level layout

- `test` — 66 analysed file(s)
- `src` — 35 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `grunt` — 7 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- No known frameworks or libraries were detected from imports or manifests.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `ac34a5a584337b33a2e567f50d96819a96ac44bf` is the revision these paths and observations refer to.
