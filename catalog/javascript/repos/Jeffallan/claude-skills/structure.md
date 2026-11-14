# Project structure: Jeffallan/claude-skills

**Analysed commit:** `078a25cc5bfd8011459be7b91d004e900c1d02d3`

**Commit reference:** [078a25cc5bfd8011459be7b91d004e900c1d02d3](https://github.com/Jeffallan/claude-skills/commit/078a25cc5bfd8011459be7b91d004e900c1d02d3)

**Tree at this commit:** [Jeffallan/claude-skills@078a25cc5bfd](https://github.com/Jeffallan/claude-skills/tree/078a25cc5bfd8011459be7b91d004e900c1d02d3)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | Jeffallan/claude-skills |
| Description | 67 Specialized Skills for Full-Stack Developers. Transform Claude Code into your expert pair programmer. |
| Stars | 12361 |
| Forks | 1186 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `078a25cc5bfd8011459be7b91d004e900c1d02d3` |
| Retrieved at | 2026-11-14T19:12:06.074336+00:00 |
| Files in this snapshot | 590 |

## Directory tree

```text
.astro/  (4 files)
  content-assets.mjs
  content-modules.mjs
  content.d.ts
  types.d.ts
.claude/  (5 files)
  old-commands/  (5 files)
    legacy/  (5 files)
      … 5 files under this directory
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.github/  (10 files)
  ISSUE_TEMPLATE/  (2 files)
    claude-issue.yml
    new-skill.yml
  workflows/  (7 files)
    ci.yml
    docs-deploy.yml
    docs-site.yml
    handbook-update.yml
    publish-plugin.yml
    release.yml
    validate.yml
  dependabot.yml
assets/  (2 files)
  capture-screenshot.js
  social-preview.html
commands/  (23 files)
  intake/  (3 files)
    capture-behavior.yaml
    create-system-description.yaml
    document-codebase.yaml
  project/  (17 files)
    discovery/  (6 files)
      … 6 files under this directory
    execution/  (4 files)
      … 4 files under this directory
    planning/  (4 files)
      … 4 files under this directory
    retrospectives/  (3 files)
      … 3 files under this directory
  common-ground.md
  common-ground.yaml
  workflow-manifest.yaml
docs/  (32 files)
  ideas/  (4 files)
    audit-primary-docs.md
    audit-skill-consistency.md
    audit-workflow-docs.md
    documentation-site.md
  prompts/  (1 files)
    discovery-for-feature-forge.md
  skill-ideas/  (2 files)
    tarot.md
    the-fool.md
  workflow/  (18 files)
    common-ground.md
    discovery-approve.md
    discovery-create.md
    discovery-phase.md
    discovery-synthesize.md
    execution-complete-ticket.md
    execution-execute-ticket.md
    execution-phase.md
    intake-capture-behavior.md
    intake-create-system-description.md
    intake-document-codebase.md
    intake-phase.md
    planning-epic-plan.md
    planning-impl-plan.md
    planning-phase.md
    retrospective-complete-epic.md
    retrospective-phase.md
    workflow-definition-schema.md
  ATLASSIAN_MCP_SETUP.md
  COMMON_GROUND.md
  SUPPORTED_AGENTS.md
  WORKFLOW_COMMANDS.md
  local_skill_development.md
  v0.5.0-narrative.md
  v0.5.0-plan.md
references/  (3 files)
  common-ground/  (3 files)
    assumption-classification.md
    file-management.md
    reasoning-graph.md
research/  (4 files)
  GITHUB_ISSUE_TREE.md
  SKILL_TRIGGER_LOGS.md
  superpowers.md
  superpowers_research_findings.md
scripts/  (4 files)
  build-plugin-dist.sh
  migrate-frontmatter.py
  test-build-plugin-dist.sh
  test-makefile.sh
site/  (40 files)
  public/  (2 files)
    .gitignore
    robots.txt
  scripts/  (1 files)
    sync-content.mjs
  src/  (33 files)
    components/  (26 files)
      … 26 files under this directory
    content/  (2 files)
      … 2 files under this directory
    pages/  (1 files)
      … 1 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    content.config.ts
    middleware.ts
    routeData.ts
  .prettierrc
  astro.config.mjs
  package.json
  tsconfig.json
skills/  (438 files)
  angular-architect/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  api-designer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  architecture-designer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  atlassian-mcp/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  chaos-engineer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  cli-developer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  cloud-architect/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  code-documenter/  (9 files)
    references/  (8 files)
      … 8 files under this directory
    SKILL.md
  code-reviewer/  (7 files)
    references/  (6 files)
      … 6 files under this directory
    SKILL.md
  cpp-pro/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  csharp-developer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  database-optimizer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  debugging-wizard/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  devops-engineer/  (10 files)
    references/  (9 files)
      … 9 files under this directory
    SKILL.md
  django-expert/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  django-storages-s3/  (5 files)
    references/  (4 files)
      … 4 files under this directory
    SKILL.md
  dotnet-core-expert/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  embedded-systems/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  fastapi-expert/  (7 files)
    references/  (6 files)
      … 6 files under this directory
    SKILL.md
  feature-forge/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  fine-tuning-expert/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  flutter-expert/  (7 files)
    references/  (6 files)
      … 6 files under this directory
    SKILL.md
  fullstack-guardian/  (11 files)
    references/  (10 files)
      … 10 files under this directory
    SKILL.md
  game-developer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  golang-pro/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  graphql-architect/  (7 files)
    references/  (6 files)
      … 6 files under this directory
    SKILL.md
  java-architect/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  javascript-pro/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  kotlin-specialist/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  kubernetes-specialist/  (12 files)
    references/  (11 files)
      … 11 files under this directory
    SKILL.md
  laravel-specialist/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  legacy-modernizer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  mcp-developer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  microservices-architect/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  ml-pipeline/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  monitoring-expert/  (9 files)
    references/  (8 files)
      … 8 files under this directory
    SKILL.md
  nestjs-expert/  (7 files)
    references/  (6 files)
      … 6 files under this directory
    SKILL.md
  nextjs-developer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  pandas-pro/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  php-pro/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  playwright-expert/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  postgres-pro/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  prompt-engineer/  (7 files)
    references/  (6 files)
      … 6 files under this directory
    SKILL.md
  python-pro/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  rag-architect/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  rails-expert/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  react-expert/  (8 files)
    references/  (7 files)
      … 7 files under this directory
    SKILL.md
  react-native-expert/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  rust-engineer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  salesforce-developer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  secure-code-guardian/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  security-reviewer/  (7 files)
    references/  (6 files)
      … 6 files under this directory
    SKILL.md
  shopify-expert/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  spark-engineer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  spec-miner/  (5 files)
    references/  (4 files)
      … 4 files under this directory
    SKILL.md
  spring-boot-engineer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  sql-pro/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  sre-engineer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  swift-expert/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  terraform-engineer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  test-master/  (11 files)
    references/  (10 files)
      … 10 files under this directory
    SKILL.md
  the-fool/  (7 files)
    references/  (6 files)
      … 6 files under this directory
    SKILL.md
  typescript-pro/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  vue-expert/  (8 files)
    references/  (7 files)
      … 7 files under this directory
    SKILL.md
  vue-expert-js/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  websocket-engineer/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  wordpress-pro/  (6 files)
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
specs/  (2 files)
  sidecar-mods.spec.md
  v050-roadmap-consolidation.spec.md
.copier-answers.yml
.editorconfig
.git-blame-ignore-revs
.gitignore
.pre-commit-config.yaml
.prettierignore
.prettierrc
CHANGELOG.md
CLAUDE.md
CONTRIBUTING.md
LICENSE
MODELCLAUDE.md
Makefile
QUICKSTART.md
README.md
ROADMAP.md
SKILLS_GUIDE.md
pyproject.toml
pyrightconfig.json
ruff.toml
version.json
```

## Entry points

- [scripts/migrate-frontmatter.py:481](https://github.com/Jeffallan/claude-skills/blob/078a25cc5bfd8011459be7b91d004e900c1d02d3/scripts/migrate-frontmatter.py#L481)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| assets package | library | Observed | Groups 1 file(s) under assets package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 21 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 1 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: add_related_skills_to_frontmatter, build_new_frontmatter, extract_related_skills, main,… |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| site package | library | Observed | Groups 16 file(s) under site package (observed from repository paths and static analysis). |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.copier-answers.yml` (config)
- `.editorconfig` (config)
- `.github/ISSUE_TEMPLATE/claude-issue.yml` (config)
- `.github/ISSUE_TEMPLATE/new-skill.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/docs-deploy.yml` (ci)
- `.github/workflows/docs-site.yml` (ci)
- `.github/workflows/handbook-update.yml` (ci)
- `.github/workflows/publish-plugin.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/validate.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `commands/common-ground.yaml` (config)
- `commands/intake/capture-behavior.yaml` (config)
- `commands/intake/create-system-description.yaml` (config)
- `commands/intake/document-codebase.yaml` (config)
- `commands/project/discovery/approve.yaml` (config)
- `commands/project/discovery/create.yaml` (config)
- `commands/project/discovery/synthesize.yaml` (config)
- `commands/project/execution/complete-ticket.yaml` (config)
- `commands/project/execution/execute-ticket.yaml` (config)
- `commands/project/planning/epic-plan.yaml` (config)
- `commands/project/planning/impl-plan.yaml` (config)
- `commands/project/retrospectives/complete-epic.yaml` (config)
- `commands/workflow-manifest.yaml` (config)
- `pyproject.toml` (manifest)
- `pyrightconfig.json` (config)
- `ruff.toml` (config)
- `site/package.json` (manifest)
- `site/src/components/site-footer/profile.json` (config)
- `site/src/components/site-nav/sites.json` (config)
- `site/tsconfig.json` (config)
- `version.json` (config)

## Top-level layout

- `skills` — 438 analysed file(s)
- `site` — 40 analysed file(s)
- `docs` — 32 analysed file(s)
- `commands` — 23 analysed file(s)
- `(root files)` — 21 analysed file(s)
- `.github` — 10 analysed file(s)
- `.claude` — 5 analysed file(s)
- `.astro` — 4 analysed file(s)
- `research` — 4 analysed file(s)
- `scripts` — 4 analysed file(s)
- `references` — 3 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `assets` — 2 analysed file(s)
- `specs` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `078a25cc5bfd8011459be7b91d004e900c1d02d3` is the revision these paths and observations refer to.
