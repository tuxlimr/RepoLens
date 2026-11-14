# Project structure: shader-effects-inc/shaders

**Analysed commit:** `1f71d113ee17c23d77e95ee46a98c3f4fcbef75a`

**Commit reference:** [1f71d113ee17c23d77e95ee46a98c3f4fcbef75a](https://github.com/shader-effects-inc/shaders/commit/1f71d113ee17c23d77e95ee46a98c3f4fcbef75a)

**Tree at this commit:** [shader-effects-inc/shaders@1f71d113ee17](https://github.com/shader-effects-inc/shaders/tree/1f71d113ee17c23d77e95ee46a98c3f4fcbef75a)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | shader-effects-inc/shaders |
| Description | WebGPU components for React, Vue, Svelte, Solid, JS & Framer |
| Stars | 5940 |
| Forks | 279 |
| Licence | MIT |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `1f71d113ee17c23d77e95ee46a98c3f4fcbef75a` |
| Retrieved at | 2026-11-14T19:14:11.520251+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (6 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.yml
    config.yml
    feature_request.yml
  workflows/  (2 files)
    release.yml
    test.yml
  PULL_REQUEST_TEMPLATE.md
packages/  (785 files)
  core/  (785 files)
    docs/  (46 files)
      … 46 files under this directory
    scripts/  (5 files)
      … 5 files under this directory
    src/  (732 files)
      … 732 files under this directory
    eslint.config.mjs
    package.json
.gitignore
CHANGELOG.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
changelog.config.mjs
package.json
```

## Entry points

- [packages/core/src/index.ts](https://github.com/shader-effects-inc/shaders/blob/1f71d113ee17c23d77e95ee46a98c3f4fcbef75a/packages/core/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 520 file(s) under service / domain layer (observed from repository paths and static analysis). |

## Important files

- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `package.json` (manifest)
- `packages/core/package.json` (manifest)

## Top-level layout

- `packages` — 785 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1f71d113ee17c23d77e95ee46a98c3f4fcbef75a` is the revision these paths and observations refer to.
