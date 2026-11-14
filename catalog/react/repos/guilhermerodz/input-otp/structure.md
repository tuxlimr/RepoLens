# Project structure: guilhermerodz/input-otp

**Analysed commit:** `cf81845e59ff43c5885c66b4755085a36f071cc1`

**Commit reference:** [cf81845e59ff43c5885c66b4755085a36f071cc1](https://github.com/guilhermerodz/input-otp/commit/cf81845e59ff43c5885c66b4755085a36f071cc1)

**Tree at this commit:** [guilhermerodz/input-otp@cf81845e59ff](https://github.com/guilhermerodz/input-otp/tree/cf81845e59ff43c5885c66b4755085a36f071cc1)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | guilhermerodz/input-otp |
| Description | One time passcode Input. Accessible & unstyled. |
| Stars | 3275 |
| Forks | 91 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | master |
| Analysed commit | `cf81845e59ff43c5885c66b4755085a36f071cc1` |
| Retrieved at | 2026-11-14T19:15:26.692230+00:00 |
| Files in this snapshot | 346 |

## Directory tree

```text
.agents/  (124 files)
  skills/  (124 files)
    impeccable/  (124 files)
      … 124 files under this directory
.claude/  (1 files)
  launch.json
.codex/  (1 files)
  hooks.json
.github/  (5 files)
  ISSUE_TEMPLATE/  (3 files)
    bad-design-choice.md
    bug-report.md
    feature_request.md
  workflows/  (2 files)
    playwright.yml
    release.yml
apps/  (193 files)
  playground/  (32 files)
    public/  (2 files)
      … 2 files under this directory
    src/  (21 files)
      … 21 files under this directory
    .eslintrc.json
    .gitignore
    README.md
    next.config.mjs
    package.json
    playwright.config.ts
    postcss.config.js
    tailwind.config.ts
    tsconfig.json
  website/  (161 files)
    public/  (23 files)
      … 23 files under this directory
    src/  (127 files)
      … 127 files under this directory
    .eslintrc.json
    .gitignore
    HANDOFF.md
    README.md
    components.json
    next.config.mjs
    package.json
    postcss.config.js
    tailwind.config.ts
    tsconfig.json
    vercel.json
packages/  (10 files)
  input-otp/  (10 files)
    src/  (7 files)
      … 7 files under this directory
    package.json
    tsconfig.json
    tsup.config.ts
scripts/  (1 files)
  release.mjs
.editorconfig
.eslintignore
.gitignore
CHANGELOG.md
CLAUDE.md
LICENSE
README.md
RELEASING.md
package.json
pnpm-workspace.yaml
turbo.json
```

## Entry points

- [packages/input-otp/src/index.ts](https://github.com/guilhermerodz/input-otp/blob/cf81845e59ff43c5885c66b4755085a36f071cc1/packages/input-otp/src/index.ts)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 1 file(s) under api layer (observed from repository paths and static analysis). |
| apps package | library | Observed | Groups 122 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 14 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 8 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 10 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.agents/skills/impeccable/agents/impeccable_asset_producer.toml` (config)
- `.agents/skills/impeccable/agents/impeccable_finish_reviewer.toml` (config)
- `.agents/skills/impeccable/agents/impeccable_manual_edit_applier.toml` (config)
- `.agents/skills/impeccable/agents/openai.yaml` (config)
- `.agents/skills/impeccable/scripts/command-metadata.json` (config)
- `.claude/launch.json` (config)
- `.codex/hooks.json` (config)
- `.editorconfig` (config)
- `.github/workflows/playwright.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `apps/playground/.eslintrc.json` (config)
- `apps/playground/package.json` (manifest)
- `apps/playground/tsconfig.json` (config)
- `apps/website/.eslintrc.json` (config)
- `apps/website/components.json` (config)
- `apps/website/package.json` (manifest)
- `apps/website/tsconfig.json` (config)
- `apps/website/vercel.json` (config)
- `package.json` (manifest)
- `packages/input-otp/package.json` (manifest)
- `packages/input-otp/tsconfig.json` (config)
- `pnpm-workspace.yaml` (config)
- `turbo.json` (config)

## Top-level layout

- `apps` — 193 analysed file(s)
- `.agents` — 124 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `packages` — 10 analysed file(s)
- `.github` — 5 analysed file(s)
- `.claude` — 1 analysed file(s)
- `.codex` — 1 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `cf81845e59ff43c5885c66b4755085a36f071cc1` is the revision these paths and observations refer to.
