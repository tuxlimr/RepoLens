# Project structure: vercel-labs/ui

**Analysed commit:** `220c1a0d7278872286a620a8e4ee4210ca46f9bd`

**Commit reference:** [220c1a0d7278872286a620a8e4ee4210ca46f9bd](https://github.com/vercel-labs/ui/commit/220c1a0d7278872286a620a8e4ee4210ca46f9bd)

**Tree at this commit:** [vercel-labs/ui@220c1a0d7278](https://github.com/vercel-labs/ui/tree/220c1a0d7278872286a620a8e4ee4210ca46f9bd)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vercel-labs/ui |
| Description | A library of behaviors for agents to build the next generation of user interfaces. |
| Stars | 4452 |
| Forks | 128 |
| Licence | Apache-2.0 |
| Language | TypeScript |
| Default branch | main |
| Analysed commit | `220c1a0d7278872286a620a8e4ee4210ca46f9bd` |
| Retrieved at | 2026-11-14T19:14:45.824798+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.agents/  (20 files)
  experts/  (15 files)
    react/  (3 files)
      … 3 files under this directory
    solid/  (3 files)
      … 3 files under this directory
    svelte/  (3 files)
      … 3 files under this directory
    vue/  (3 files)
      … 3 files under this directory
    web/  (3 files)
      … 3 files under this directory
  skills/  (5 files)
    ui-sdk-expert-review/  (1 files)
      … 1 files under this directory
    ui-sdk-unslop/  (1 files)
      … 1 files under this directory
    ui-sdk-write-code/  (1 files)
      … 1 files under this directory
    ui-sdk-write-docs/  (1 files)
      … 1 files under this directory
    README.md
.changeset/  (10 files)
  pre/  (5 files)
    button-router-link.md
    confirm-inside-dialog.md
    cookie-duplicate-name.md
    nuxt-dev-one-core.md
    select-trigger-field-server.md
  README.md
  config.json
  listbox-restore-guard.md
  pre.json
  webmcp-improvements.md
.claude/  (6 files)
  agents/  (5 files)
    react-expert.md
    solid-expert.md
    svelte-expert.md
    vue-expert.md
    web-expert.md
  launch.json
.github/  (7 files)
  actions/  (1 files)
    setup/  (1 files)
      … 1 files under this directory
  workflows/  (5 files)
    ci.yml
    nightly.yml
    release.yml
    scheduled-issue.yml
    weekly.yml
  dependabot.yml
apps/  (745 files)
  docs/  (578 files)
    app/  (41 files)
      … 41 files under this directory
    components/  (59 files)
      … 59 files under this directory
    content/  (423 files)
      … 423 files under this directory
    lib/  (38 files)
      … 38 files under this directory
    public/  (6 files)
      … 6 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    AGENTS.md
    next-env.d.ts
    next.config.mjs
    package.json
    postcss.config.mjs
    proxy.test.ts
    proxy.ts
    tsconfig.json
    vercel.json
  playground/  (167 files)
    src/  (163 files)
      … 163 files under this directory
    README.md
    index.html
    package.json
    solid-ssr.ts
.gitignore
.nvmrc
.prettierignore
.prettierrc
AGENTS.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| apps package | library | Observed | Groups 159 file(s) under apps package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 20 file(s) under configuration and deployment (observed from repository paths and static analysis). |

## Important files

- `.changeset/config.json` (config)
- `.changeset/pre.json` (config)
- `.claude/launch.json` (config)
- `.github/actions/setup/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/nightly.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/scheduled-issue.yml` (ci)
- `.github/workflows/weekly.yml` (ci)
- `apps/docs/content/docs/agents/connect-an-agent/meta.json` (config)
- `apps/docs/content/docs/agents/meta.json` (config)
- `apps/docs/content/docs/core/behaviors/meta.json` (config)
- `apps/docs/content/docs/core/meta.json` (config)
- `apps/docs/content/docs/guides/meta.json` (config)
- `apps/docs/content/docs/meta.json` (config)
- `apps/docs/content/docs/react/hooks/meta.json` (config)
- `apps/docs/content/docs/react/meta.json` (config)
- `apps/docs/content/docs/solid/meta.json` (config)
- `apps/docs/content/docs/solid/utilities/meta.json` (config)
- `apps/docs/content/docs/svelte/meta.json` (config)
- `apps/docs/content/docs/svelte/utilities/meta.json` (config)
- `apps/docs/content/docs/vue/meta.json` (config)
- `apps/docs/content/docs/vue/utilities/meta.json` (config)
- `apps/docs/content/docs/web-components/meta.json` (config)
- `apps/docs/content/docs/web-components/utilities/meta.json` (config)
- `apps/docs/package.json` (manifest)
- `apps/docs/tsconfig.json` (config)
- `apps/docs/vercel.json` (config)
- `apps/playground/package.json` (manifest)

## Top-level layout

- `apps` — 745 analysed file(s)
- `.agents` — 20 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.changeset` — 10 analysed file(s)
- `.github` — 7 analysed file(s)
- `.claude` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `220c1a0d7278872286a620a8e4ee4210ca46f9bd` is the revision these paths and observations refer to.
