# Project structure: auth0/node-jsonwebtoken

**Analysed commit:** `b924272f29192e12926b5414546f7c5bfcc9579d`

**Commit reference:** [b924272f29192e12926b5414546f7c5bfcc9579d](https://github.com/auth0/node-jsonwebtoken/commit/b924272f29192e12926b5414546f7c5bfcc9579d)

**Tree at this commit:** [auth0/node-jsonwebtoken@b924272f2919](https://github.com/auth0/node-jsonwebtoken/tree/b924272f29192e12926b5414546f7c5bfcc9579d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | auth0/node-jsonwebtoken |
| Description | JsonWebToken implementation for node.js http://self-issued.info/docs/draft-ietf-oauth-json-web-token.html |
| Stars | 18183 |
| Forks | 1294 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `b924272f29192e12926b5414546f7c5bfcc9579d` |
| Retrieved at | 2026-11-14T19:11:22.527161+00:00 |
| Files in this snapshot | 67 |

## Directory tree

```text
.github/  (5 files)
  workflows/  (5 files)
    commitlint.yml
    prepare-release.yml
    release.yml
    sca-scan.yml
    test.yml
.husky/  (1 files)
  commit-msg
bin/  (1 files)
  changelog
lib/  (8 files)
  JsonWebTokenError.js
  NotBeforeError.js
  TokenExpiredError.js
  asymmetricKeyDetailsSupported.js
  psSupported.js
  rsaPssKeyDetailsSupported.js
  timespan.js
  validateAsymmetricKey.js
test/  (35 files)
  .eslintrc.json
  async_sign.tests.js
  buffer.tests.js
  claim-aud.test.js
  claim-exp.test.js
  claim-iat.test.js
  claim-iss.test.js
  claim-jti.test.js
  claim-nbf.test.js
  claim-private.tests.js
  claim-sub.tests.js
  decoding.tests.js
  encoding.tests.js
  expires_format.tests.js
  header-kid.test.js
  invalid_exp.tests.js
  issue_147.tests.js
  issue_304.tests.js
  issue_70.tests.js
  jwt.asymmetric_signing.tests.js
  jwt.hs.tests.js
  jwt.malicious.tests.js
  noTimestamp.tests.js
  non_object_values.tests.js
  … 11 more files
.commitlintrc.json
.editorconfig
.eslintignore
.eslintrc.json
.gitignore
.npmignore
.releaserc.json
CHANGELOG.md
CODEOWNERS
LICENSE
README.md
decode.js
index.js
opslevel.yml
package.json
sign.js
verify.js
```

## Entry points

- [index.js](https://github.com/auth0/node-jsonwebtoken/blob/b924272f29192e12926b5414546f7c5bfcc9579d/index.js)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| lib package | library | Observed | Groups 8 file(s) under lib package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 35 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.commitlintrc.json` (config)
- `.editorconfig` (config)
- `.eslintrc.json` (config)
- `.github/workflows/commitlint.yml` (ci)
- `.github/workflows/prepare-release.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/sca-scan.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.releaserc.json` (config)
- `opslevel.yml` (config)
- `package.json` (manifest)

## Top-level layout

- `test` — 35 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `lib` — 8 analysed file(s)
- `.github` — 5 analysed file(s)
- `.husky` — 1 analysed file(s)
- `bin` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 17 file(s) were skipped during inventory (17 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `b924272f29192e12926b5414546f7c5bfcc9579d` is the revision these paths and observations refer to.
