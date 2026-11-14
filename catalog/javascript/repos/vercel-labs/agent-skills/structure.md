# Project structure: vercel-labs/agent-skills

**Analysed commit:** `1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62`

**Commit reference:** [1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62](https://github.com/vercel-labs/agent-skills/commit/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62)

**Tree at this commit:** [vercel-labs/agent-skills@1a2c79d4e6c4](https://github.com/vercel-labs/agent-skills/tree/1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | vercel-labs/agent-skills |
| Description | Vercel's official collection of agent skills |
| Stars | 34058 |
| Forks | 2970 |
| Licence | Not detected |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62` |
| Retrieved at | 2026-11-14T19:10:44.183549+00:00 |
| Files in this snapshot | 427 |

## Directory tree

```text
.github/  (2 files)
  workflows/  (2 files)
    agent-skills-discovery.yml
    react-best-practices-ci.yml
packages/  (118 files)
  react-best-practices-build/  (11 files)
    src/  (7 files)
      … 7 files under this directory
    .gitignore
    package.json
    test-cases.json
    tsconfig.json
  vercel-optimize-tests/  (107 files)
    test/  (106 files)
      … 106 files under this directory
    package.json
scripts/  (1 files)
  build-discovery-index.mjs
skills/  (301 files)
  composition-patterns/  (14 files)
    rules/  (10 files)
      … 10 files under this directory
    AGENTS.md
    README.md
    SKILL.md
    metadata.json
  deploy-to-vercel/  (1 files)
    SKILL.md
  react-best-practices/  (76 files)
    rules/  (72 files)
      … 72 files under this directory
    AGENTS.md
    README.md
    SKILL.md
    metadata.json
  react-native-skills/  (42 files)
    rules/  (38 files)
      … 38 files under this directory
    AGENTS.md
    README.md
    SKILL.md
    metadata.json
  react-view-transitions/  (9 files)
    references/  (5 files)
      … 5 files under this directory
    AGENTS.md
    README.md
    SKILL.md
    metadata.json
  vercel-cli-with-tokens/  (1 files)
    SKILL.md
  vercel-optimize/  (156 files)
    lib/  (75 files)
      … 75 files under this directory
    references/  (61 files)
      … 61 files under this directory
    scripts/  (15 files)
      … 15 files under this directory
    AGENTS.md
    CONTRIBUTING.md
    README.md
    SKILL.md
    metadata.json
  web-design-guidelines/  (1 files)
    SKILL.md
  writing-guidelines/  (1 files)
    SKILL.md
.gitignore
AGENTS.md
README.md
package.json
skills.sh.json
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| packages package | library | Observed | Groups 7 file(s) under packages package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 1 file(s) under scripts package (observed from repository paths and static analysis). |
| skills package | library | Observed | Groups 90 file(s) under skills package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 106 file(s) under tests (observed from repository paths and static analysis). |

## Important files

- `.github/workflows/agent-skills-discovery.yml` (ci)
- `.github/workflows/react-best-practices-ci.yml` (ci)
- `package.json` (manifest)
- `packages/react-best-practices-build/package.json` (manifest)
- `packages/react-best-practices-build/test-cases.json` (config)
- `packages/react-best-practices-build/tsconfig.json` (config)
- `packages/vercel-optimize-tests/package.json` (manifest)
- `skills.sh.json` (config)
- `skills/composition-patterns/metadata.json` (config)
- `skills/react-best-practices/metadata.json` (config)
- `skills/react-native-skills/metadata.json` (config)
- `skills/react-view-transitions/metadata.json` (config)
- `skills/vercel-optimize/metadata.json` (config)
- `skills/vercel-optimize/references/docs-library.json` (config)

## Top-level layout

- `skills` — 301 analysed file(s)
- `packages` — 118 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `.github` — 2 analysed file(s)
- `scripts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- JavaScript and TypeScript files were inventoried from paths and package manifests. They were not parsed with a full language AST, and repository code was not executed.

Commit `1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62` is the revision these paths and observations refer to.
