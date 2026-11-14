# Project structure: luongnv89/claude-howto

**Analysed commit:** `5609e68a6ce838579e15fd31ceb6025be08841df`

**Commit reference:** [5609e68a6ce838579e15fd31ceb6025be08841df](https://github.com/luongnv89/claude-howto/commit/5609e68a6ce838579e15fd31ceb6025be08841df)

**Tree at this commit:** [luongnv89/claude-howto@5609e68a6ce8](https://github.com/luongnv89/claude-howto/tree/5609e68a6ce838579e15fd31ceb6025be08841df)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | luongnv89/claude-howto |
| Description | A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value. |
| Stars | 47197 |
| Forks | 5750 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `5609e68a6ce838579e15fd31ceb6025be08841df` |
| Retrieved at | 2026-11-14T19:06:37.662901+00:00 |
| Files in this snapshot | 683 |

## Directory tree

```text
.claude/  (9 files)
  skills/  (9 files)
    lesson-quiz/  (4 files)
      … 4 files under this directory
    self-assessment/  (5 files)
      … 5 files under this directory
.github/  (14 files)
  ISSUE_TEMPLATE/  (5 files)
    bug_report.md
    config.yml
    documentation.md
    feature_request.md
    question.md
  workflows/  (4 files)
    docs-check.yml
    pages.yml
    release.yml
    test.yml
  FUNDING.yml
  SECURITY_REPORTING.md
  TESTING.md
  markdown-link-check-config.json
  pull_request_template.md
01-slash-commands/  (9 files)
  README.md
  commit.md
  doc-refactor.md
  generate-api-docs.md
  optimize.md
  pr.md
  push-all.md
  setup-ci-cd.md
  unit-test-expand.md
02-memory/  (4 files)
  README.md
  directory-api-CLAUDE.md
  personal-CLAUDE.md
  project-CLAUDE.md
03-skills/  (23 files)
  blog-draft/  (3 files)
    templates/  (2 files)
      … 2 files under this directory
    SKILL.md
  brand-voice/  (4 files)
    templates/  (2 files)
      … 2 files under this directory
    SKILL.md
    tone-examples.md
  claude-md/  (1 files)
    SKILL.md
  code-review-specialist/  (5 files)
    scripts/  (2 files)
      … 2 files under this directory
    templates/  (2 files)
      … 2 files under this directory
    SKILL.md
  doc-generator/  (2 files)
    SKILL.md
    generate-docs.py
  refactor/  (6 files)
    references/  (2 files)
      … 2 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    templates/  (1 files)
      … 1 files under this directory
    SKILL.md
  .gitignore
  README.md
04-subagents/  (10 files)
  README.md
  clean-code-reviewer.md
  code-reviewer.md
  data-scientist.md
  debugger.md
  documentation-writer.md
  implementation-agent.md
  performance-optimizer.md
  secure-reviewer.md
  test-engineer.md
05-mcp/  (5 files)
  README.md
  database-mcp.json
  filesystem-mcp.json
  github-mcp.json
  multi-mcp.json
06-hooks/  (12 files)
  README.md
  context-tracker-tiktoken.py
  context-tracker.py
  dependency-check.sh
  format-code.sh
  log-bash.sh
  notify-team.sh
  pre-commit.sh
  pre-tool-check.sh
  security-scan.sh
  session-end.sh
  validate-prompt.sh
07-plugins/  (40 files)
  devops-automation/  (15 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    commands/  (4 files)
      … 4 files under this directory
    hooks/  (3 files)
      … 3 files under this directory
    scripts/  (3 files)
      … 3 files under this directory
    README.md
  documentation/  (13 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    commands/  (4 files)
      … 4 files under this directory
    templates/  (3 files)
      … 3 files under this directory
    .mcp.json
    README.md
  pr-review/  (11 files)
    .claude-plugin/  (1 files)
      … 1 files under this directory
    agents/  (3 files)
      … 3 files under this directory
    commands/  (3 files)
      … 3 files under this directory
    hooks/  (2 files)
      … 2 files under this directory
    .mcp.json
    README.md
  README.md
08-checkpoints/  (2 files)
  README.md
  checkpoint-examples.md
09-advanced-features/  (4 files)
  README.md
  config-examples.json
  planning-mode-examples.md
  setup-auto-mode-permissions.py
10-cli/  (1 files)
  README.md
assets/  (7 files)
  logo/  (7 files)
    favicon.svg
    logo-black.svg
    logo-full.svg
    logo-icon.svg
    logo-mark.svg
    logo-white.svg
    logo-wordmark.svg
docs/  (2 files)
  ROADMAP-20260401.md
  TASKS-20260401.md
fa/  (98 files)
  .github/  (4 files)
    ISSUE_TEMPLATE/  (4 files)
      … 4 files under this directory
  01-slash-commands/  (9 files)
    README.md
    commit.md
    doc-refactor.md
    generate-api-docs.md
    optimize.md
    pr.md
    push-all.md
    setup-ci-cd.md
    unit-test-expand.md
  02-memory/  (4 files)
    README.md
    directory-api-CLAUDE.md
    personal-CLAUDE.md
    project-CLAUDE.md
  03-skills/  (15 files)
    blog-draft/  (3 files)
      … 3 files under this directory
    brand-voice/  (2 files)
      … 2 files under this directory
    claude-md/  (1 files)
      … 1 files under this directory
    code-review-specialist/  (3 files)
      … 3 files under this directory
    doc-generator/  (1 files)
      … 1 files under this directory
    refactor/  (4 files)
      … 4 files under this directory
    README.md
  04-subagents/  (10 files)
    README.md
    clean-code-reviewer.md
    code-reviewer.md
    data-scientist.md
    debugger.md
    documentation-writer.md
    implementation-agent.md
    performance-optimizer.md
    secure-reviewer.md
    test-engineer.md
  05-mcp/  (1 files)
    README.md
  06-hooks/  (1 files)
    README.md
  07-plugins/  (27 files)
    devops-automation/  (8 files)
      … 8 files under this directory
    documentation/  (11 files)
      … 11 files under this directory
    pr-review/  (7 files)
      … 7 files under this directory
    README.md
  08-checkpoints/  (2 files)
    README.md
    checkpoint-examples.md
  09-advanced-features/  (1 files)
    planning-mode-examples.md
  10-cli/  (1 files)
    README.md
  docs/  (2 files)
    ROADMAP-20260401.md
    TASKS-20260401.md
  prompts/  (1 files)
    remotion-video.md
  resources/  (3 files)
    DESIGN-SYSTEM.md
    QUICK-START.md
    README.md
  scripts/  (1 files)
    README.md
  CATALOG.md
  CHANGELOG.md
  CLAUDE.md
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  INDEX.md
  LEARNING-ROADMAP.md
  QUICK_REFERENCE.md
  README.md
  RELEASE_NOTES.md
  SECURITY.md
  STYLE_GUIDE.md
  TRANSLATION_NOTES.md
  claude_concepts_guide.md
  clean-code-rules.md
  resources.md
ja/  (115 files)
  .github/  (7 files)
    ISSUE_TEMPLATE/  (4 files)
      … 4 files under this directory
    SECURITY_REPORTING.md
    TESTING.md
    pull_request_template.md
  01-slash-commands/  (9 files)
    README.md
    commit.md
    doc-refactor.md
    generate-api-docs.md
    optimize.md
    pr.md
    push-all.md
    setup-ci-cd.md
    unit-test-expand.md
  02-memory/  (4 files)
    README.md
    directory-api-CLAUDE.md
    personal-CLAUDE.md
    project-CLAUDE.md
  03-skills/  (15 files)
    blog-draft/  (3 files)
      … 3 files under this directory
    brand-voice/  (2 files)
      … 2 files under this directory
    claude-md/  (1 files)
      … 1 files under this directory
    code-review-specialist/  (3 files)
      … 3 files under this directory
    doc-generator/  (1 files)
      … 1 files under this directory
    refactor/  (4 files)
      … 4 files under this directory
    README.md
  04-subagents/  (10 files)
    README.md
    clean-code-reviewer.md
    code-reviewer.md
    data-scientist.md
    debugger.md
    documentation-writer.md
    implementation-agent.md
    performance-optimizer.md
    secure-reviewer.md
    test-engineer.md
  05-mcp/  (5 files)
    README.md
    database-mcp.json
    filesystem-mcp.json
    github-mcp.json
    multi-mcp.json
  06-hooks/  (10 files)
    README.md
    dependency-check.sh
    format-code.sh
    log-bash.sh
    notify-team.sh
    pre-commit.sh
    pre-tool-check.sh
    security-scan.sh
    session-end.sh
    validate-prompt.sh
  07-plugins/  (27 files)
    devops-automation/  (8 files)
      … 8 files under this directory
    documentation/  (11 files)
      … 11 files under this directory
    pr-review/  (7 files)
      … 7 files under this directory
    README.md
  08-checkpoints/  (2 files)
    README.md
    checkpoint-examples.md
  09-advanced-features/  (2 files)
    README.md
    planning-mode-examples.md
  10-cli/  (1 files)
    README.md
  docs/  (2 files)
    ROADMAP-20260401.md
    TASKS-20260401.md
  prompts/  (1 files)
    remotion-video.md
  resources/  (3 files)
    DESIGN-SYSTEM.md
    QUICK-START.md
    README.md
  scripts/  (1 files)
    README.md
  CATALOG.md
  CHANGELOG.md
  CLAUDE.md
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  INDEX.md
  LEARNING-ROADMAP.md
  QUICK_REFERENCE.md
  README.md
  RELEASE_NOTES.md
  SECURITY.md
  STYLE_GUIDE.md
  TRANSLATION_NOTES.md
  claude_concepts_guide.md
  clean-code-rules.md
  resources.md
ko/  (98 files)
  .github/  (7 files)
    ISSUE_TEMPLATE/  (4 files)
      … 4 files under this directory
    SECURITY_REPORTING.md
    TESTING.md
    pull_request_template.md
  01-slash-commands/  (9 files)
    README.md
    commit.md
    doc-refactor.md
    generate-api-docs.md
    optimize.md
    pr.md
    push-all.md
    setup-ci-cd.md
    unit-test-expand.md
  02-memory/  (4 files)
    README.md
    directory-api-CLAUDE.md
    personal-CLAUDE.md
    project-CLAUDE.md
  03-skills/  (15 files)
    blog-draft/  (3 files)
      … 3 files under this directory
    brand-voice/  (2 files)
      … 2 files under this directory
    claude-md/  (1 files)
      … 1 files under this directory
    code-review-specialist/  (3 files)
      … 3 files under this directory
    doc-generator/  (1 files)
      … 1 files under this directory
    refactor/  (4 files)
      … 4 files under this directory
    README.md
  04-subagents/  (10 files)
    README.md
    clean-code-reviewer.md
    code-reviewer.md
    data-scientist.md
    debugger.md
    documentation-writer.md
    implementation-agent.md
    performance-optimizer.md
    secure-reviewer.md
    test-engineer.md
  05-mcp/  (1 files)
    README.md
  06-hooks/  (1 files)
    README.md
  07-plugins/  (27 files)
    devops-automation/  (8 files)
      … 8 files under this directory
    documentation/  (11 files)
      … 11 files under this directory
    pr-review/  (7 files)
      … 7 files under this directory
    README.md
  08-checkpoints/  (2 files)
    README.md
    checkpoint-examples.md
  09-advanced-features/  (2 files)
    README.md
    planning-mode-examples.md
  10-cli/  (1 files)
    README.md
  resources/  (3 files)
    DESIGN-SYSTEM.md
    QUICK-START.md
    README.md
  scripts/  (1 files)
    README.md
  CATALOG.md
  CHANGELOG.md
  CLAUDE.md
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  INDEX.md
  LEARNING-ROADMAP.md
  QUICK_REFERENCE.md
  README.md
  SECURITY.md
  STYLE_GUIDE.md
  TRANSLATION_NOTES.md
  claude_concepts_guide.md
  clean-code-rules.md
  resources.md
local-progress/  (1 files)
  index.html
prompts/  (1 files)
  remotion-video.md
resources/  (14 files)
  favicons/  (5 files)
    favicon-128.svg
    favicon-16.svg
    favicon-256.svg
    favicon-32.svg
    favicon-64.svg
  icons/  (2 files)
    claude-howto-icon-dark.svg
    claude-howto-icon.svg
  logos/  (2 files)
    claude-howto-logo-dark.svg
    claude-howto-logo.svg
  DESIGN-SYSTEM.md
  INDEX.txt
  MANIFEST.txt
  QUICK-START.md
  README.md
scripts/  (32 files)
  tests/  (9 files)
    __init__.py
    conftest.py
    test_build_epub.py
    test_build_website.py
    test_check_cross_references.py
    test_check_epub_diagrams.py
    test_check_markdown_rendering.py
    test_check_mermaid.py
    test_pele_renderer.py
  website_templates/  (8 files)
    landing.css
    landing.html.j2
    landing.js
    page.html.j2
    roadmap.json
    site.css
    tailwind.config.js
    tailwind.input.css
  README.md
  build_epub.py
  build_website.py
  check_cross_references.py
  check_epub_diagrams.py
  check_links.py
  check_markdown_rendering.py
  check_mermaid.py
  pele_render.mjs
  pele_renderer.py
  pyproject.toml
  requirements-dev.txt
  requirements.txt
  sync_translations.py
  vendor_assets.py
uk/  (134 files)
  01-slash-commands/  (9 files)
    README.md
    commit.md
    doc-refactor.md
    generate-api-docs.md
    optimize.md
    pr.md
    push-all.md
    setup-ci-cd.md
    unit-test-expand.md
  02-memory/  (4 files)
    README.md
    directory-api-CLAUDE.md
    personal-CLAUDE.md
    project-CLAUDE.md
  03-skills/  (23 files)
    blog-draft/  (3 files)
      … 3 files under this directory
    brand-voice/  (4 files)
      … 4 files under this directory
    claude-md/  (1 files)
      … 1 files under this directory
    code-review-specialist/  (5 files)
      … 5 files under this directory
    doc-generator/  (2 files)
      … 2 files under this directory
    refactor/  (6 files)
      … 6 files under this directory
    .gitignore
    README.md
  04-subagents/  (10 files)
    README.md
    clean-code-reviewer.md
    code-reviewer.md
    data-scientist.md
    debugger.md
    documentation-writer.md
    implementation-agent.md
    performance-optimizer.md
    secure-reviewer.md
    test-engineer.md
  05-mcp/  (5 files)
    README.md
    database-mcp.json
    filesystem-mcp.json
    github-mcp.json
    multi-mcp.json
  06-hooks/  (11 files)
    README.md
    context-tracker-tiktoken.py
    context-tracker.py
    dependency-check.sh
    format-code.sh
    log-bash.sh
    notify-team.sh
    pre-commit.sh
    pre-tool-check.sh
    security-scan.sh
    validate-prompt.sh
  07-plugins/  (40 files)
    devops-automation/  (15 files)
      … 15 files under this directory
    documentation/  (13 files)
      … 13 files under this directory
    pr-review/  (11 files)
      … 11 files under this directory
    README.md
  08-checkpoints/  (2 files)
    README.md
    checkpoint-examples.md
  09-advanced-features/  (4 files)
    README.md
    config-examples.json
    planning-mode-examples.md
    setup-auto-mode-permissions.py
  10-cli/  (1 files)
    README.md
  docs/  (2 files)
    ROADMAP-20260401.md
    TASKS-20260401.md
  prompts/  (1 files)
    remotion-video.md
  resources/  (3 files)
    DESIGN-SYSTEM.md
    QUICK-START.md
    README.md
  scripts/  (1 files)
    README.md
  CATALOG.md
  CHANGELOG.md
  CLAUDE.md
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  INDEX.md
  LEARNING-ROADMAP.md
  LICENSE
  QUICK_REFERENCE.md
  README.md
  RELEASE_NOTES.md
  SECURITY.md
  STYLE_GUIDE.md
  TRANSLATION_NOTES.md
  TRANSLATION_QUEUE.md
  claude_concepts_guide.md
  clean-code-rules.md
  resources.md
vi/  (26 files)
  01-slash-commands/  (9 files)
    README.md
    commit.md
    doc-refactor.md
    generate-api-docs.md
    optimize.md
    pr.md
    push-all.md
    setup-ci-cd.md
    unit-test-expand.md
  02-memory/  (4 files)
    README.md
    directory-api-CLAUDE.md
    personal-CLAUDE.md
    project-CLAUDE.md
  03-skills/  (6 files)
    blog-draft/  (1 files)
      … 1 files under this directory
    brand-voice/  (1 files)
      … 1 files under this directory
    claude-md/  (1 files)
      … 1 files under this directory
    code-review-specialist/  (1 files)
      … 1 files under this directory
    refactor/  (1 files)
      … 1 files under this directory
    README.md
  04-subagents/  (7 files)
    README.md
    code-reviewer.md
    debugger.md
    documentation-writer.md
    implementation-agent.md
    secure-reviewer.md
    test-engineer.md
.cspell.json
.gitignore
.idd.yml
.markdownlint.json
.pre-commit-config.yaml
CATALOG.md
CHANGELOG.md
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
INDEX.md
LEARNING-ROADMAP.md
LICENSE
QUICK_REFERENCE.md
README.md
SECURITY.md
STYLE_GUIDE.md
claude-howto-logo.svg
claude_concepts_guide.md
clean-code-rules.md
coverage.xml
resources.md
```

## Entry points

- [03-skills/code-review-specialist/scripts/analyze-metrics.py:30](https://github.com/luongnv89/claude-howto/blob/5609e68a6ce838579e15fd31ceb6025be08841df/03-skills/code-review-specialist/scripts/analyze-metrics.py#L30)
- [03-skills/code-review-specialist/scripts/compare-complexity.py:169](https://github.com/luongnv89/claude-howto/blob/5609e68a6ce838579e15fd31ceb6025be08841df/03-skills/code-review-specialist/scripts/compare-complexity.py#L169)
- [03-skills/doc-generator/generate-docs.py:45](https://github.com/luongnv89/claude-howto/blob/5609e68a6ce838579e15fd31ceb6025be08841df/03-skills/doc-generator/generate-docs.py#L45)
- [03-skills/refactor/scripts/analyze-complexity.py:544](https://github.com/luongnv89/claude-howto/blob/5609e68a6ce838579e15fd31ceb6025be08841df/03-skills/refactor/scripts/analyze-complexity.py#L544)
- [03-skills/refactor/scripts/detect-smells.py:710](https://github.com/luongnv89/claude-howto/blob/5609e68a6ce838579e15fd31ceb6025be08841df/03-skills/refactor/scripts/detect-smells.py#L710)
- [06-hooks/context-tracker-tiktoken.py:148](https://github.com/luongnv89/claude-howto/blob/5609e68a6ce838579e15fd31ceb6025be08841df/06-hooks/context-tracker-tiktoken.py#L148)
- [06-hooks/context-tracker.py:125](https://github.com/luongnv89/claude-howto/blob/5609e68a6ce838579e15fd31ceb6025be08841df/06-hooks/context-tracker.py#L125)
- [09-advanced-features/setup-auto-mode-permissions.py:266](https://github.com/luongnv89/claude-howto/blob/5609e68a6ce838579e15fd31ceb6025be08841df/09-advanced-features/setup-auto-mode-permissions.py#L266)
- [scripts/build_epub.py:1231](https://github.com/luongnv89/claude-howto/blob/5609e68a6ce838579e15fd31ceb6025be08841df/scripts/build_epub.py#L1231)
- [scripts/build_website.py:1215](https://github.com/luongnv89/claude-howto/blob/5609e68a6ce838579e15fd31ceb6025be08841df/scripts/build_website.py#L1215)
- [scripts/check_cross_references.py:133](https://github.com/luongnv89/claude-howto/blob/5609e68a6ce838579e15fd31ceb6025be08841df/scripts/check_cross_references.py#L133)
- [scripts/check_epub_diagrams.py:160](https://github.com/luongnv89/claude-howto/blob/5609e68a6ce838579e15fd31ceb6025be08841df/scripts/check_epub_diagrams.py#L160)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| 06-hooks package | library | Observed | Groups 9 file(s) under 06-hooks package (observed from repository paths and static analysis). |
| 07-plugins package | library | Observed | Groups 6 file(s) under 07-plugins package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 32 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 24 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: APIDocExtractor, BuildState, ChapterCollector, ChapterInfo, CodeSmell, ComplexityAnalyzer… |
| ja package | library | Observed | Groups 9 file(s) under ja package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 5 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: PeleDiagramError, PeleHelperError, PeleResult, PeleUnavailableError. Observed top-level functions:… |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: FakeRenderer, TestBrokenBlocks, TestBuildState, TestBuildWebsite, TestChapterCollector, TestChapterOrder. Ob… |
| uk package | library | Observed | Groups 14 file(s) under uk package (observed from repository paths and static analysis). |

## Important files

- `.cspell.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/markdown-link-check-config.json` (config)
- `.github/workflows/docs-check.yml` (ci)
- `.github/workflows/pages.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/test.yml` (ci)
- `.idd.yml` (config)
- `.markdownlint.json` (config)
- `.pre-commit-config.yaml` (config)
- `05-mcp/database-mcp.json` (config)
- `05-mcp/filesystem-mcp.json` (config)
- `05-mcp/github-mcp.json` (config)
- `05-mcp/multi-mcp.json` (config)
- `07-plugins/devops-automation/.claude-plugin/plugin.json` (config)
- `07-plugins/devops-automation/hooks/hooks.json` (config)
- `07-plugins/documentation/.claude-plugin/plugin.json` (config)
- `07-plugins/documentation/.mcp.json` (config)
- `07-plugins/pr-review/.claude-plugin/plugin.json` (config)
- `07-plugins/pr-review/.mcp.json` (config)
- `07-plugins/pr-review/hooks/hooks.json` (config)
- `09-advanced-features/config-examples.json` (config)
- `ja/05-mcp/database-mcp.json` (config)
- `ja/05-mcp/filesystem-mcp.json` (config)
- `ja/05-mcp/github-mcp.json` (config)
- `ja/05-mcp/multi-mcp.json` (config)
- `scripts/pyproject.toml` (manifest)
- `scripts/requirements-dev.txt` (manifest)
- `scripts/requirements.txt` (manifest)
- `scripts/website_templates/roadmap.json` (config)
- `uk/05-mcp/database-mcp.json` (config)
- `uk/05-mcp/filesystem-mcp.json` (config)
- `uk/05-mcp/github-mcp.json` (config)
- `uk/05-mcp/multi-mcp.json` (config)
- `uk/07-plugins/devops-automation/.claude-plugin/plugin.json` (config)
- `uk/07-plugins/devops-automation/hooks/hooks.json` (config)
- `uk/07-plugins/documentation/.claude-plugin/plugin.json` (config)
- `uk/07-plugins/documentation/.mcp.json` (config)
- `uk/07-plugins/pr-review/.claude-plugin/plugin.json` (config)
- `uk/07-plugins/pr-review/.mcp.json` (config)
- `uk/07-plugins/pr-review/hooks/hooks.json` (config)
- `uk/09-advanced-features/config-examples.json` (config)

## Top-level layout

- `uk` — 134 analysed file(s)
- `ja` — 115 analysed file(s)
- `fa` — 98 analysed file(s)
- `ko` — 98 analysed file(s)
- `07-plugins` — 40 analysed file(s)
- `scripts` — 32 analysed file(s)
- `vi` — 26 analysed file(s)
- `03-skills` — 23 analysed file(s)
- `(root files)` — 22 analysed file(s)
- `.github` — 14 analysed file(s)
- `resources` — 14 analysed file(s)
- `06-hooks` — 12 analysed file(s)
- `04-subagents` — 10 analysed file(s)
- `.claude` — 9 analysed file(s)
- `01-slash-commands` — 9 analysed file(s)
- `assets` — 7 analysed file(s)
- `05-mcp` — 5 analysed file(s)
- `02-memory` — 4 analysed file(s)
- `09-advanced-features` — 4 analysed file(s)
- `08-checkpoints` — 2 analysed file(s)
- `docs` — 2 analysed file(s)
- `10-cli` — 1 analysed file(s)
- `local-progress` — 1 analysed file(s)
- `prompts` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5609e68a6ce838579e15fd31ceb6025be08841df` is the revision these paths and observations refer to.
