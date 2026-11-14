# Project structure: nextlevelbuilder/ui-ux-pro-max-skill

**Analysed commit:** `d643997c82e94742dd3bee43210b0198e8bbba3d`

**Commit reference:** [d643997c82e94742dd3bee43210b0198e8bbba3d](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/commit/d643997c82e94742dd3bee43210b0198e8bbba3d)

**Tree at this commit:** [nextlevelbuilder/ui-ux-pro-max-skill@d643997c82e9](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/d643997c82e94742dd3bee43210b0198e8bbba3d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | nextlevelbuilder/ui-ux-pro-max-skill |
| Description | An AI skill that provides design intelligence for building professional UI/UX across multiple platforms. |
| Stars | 149450 |
| Forks | 15801 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `d643997c82e94742dd3bee43210b0198e8bbba3d` |
| Retrieved at | 2026-11-14T19:06:03.788430+00:00 |
| Files in this snapshot | 639 |

## Directory tree

```text
.claude/  (207 files)
  skills/  (207 files)
    banner-design/  (2 files)
      … 2 files under this directory
    brand/  (18 files)
      … 18 files under this directory
    design/  (38 files)
      … 38 files under this directory
    design-system/  (28 files)
      … 28 files under this directory
    slides/  (6 files)
      … 6 files under this directory
    ui-styling/  (43 files)
      … 43 files under this directory
    ui-ux-pro-max/  (72 files)
      … 72 files under this directory
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.github/  (9 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.yml
    feature_request.yml
  workflows/  (6 files)
    bump-versions.yml
    check-asset-sync.yml
    refresh-catalogs.yml
    release.yml
    smoke-stacks.yml
    tests.yml
  PULL_REQUEST_TEMPLATE.md
cli/  (234 files)
  assets/  (204 files)
    data/  (36 files)
      … 36 files under this directory
    scripts/  (33 files)
      … 33 files under this directory
    skills/  (108 files)
      … 108 files under this directory
    templates/  (27 files)
      … 27 files under this directory
  scripts/  (3 files)
    build.mjs
    run-python.mjs
    sync-assets.mjs
  src/  (11 files)
    commands/  (4 files)
      … 4 files under this directory
    types/  (1 files)
      … 1 files under this directory
    utils/  (5 files)
      … 5 files under this directory
    index.ts
  tests/  (9 files)
    e2e/  (9 files)
      … 9 files under this directory
  .gitignore
  .npmignore
  README.md
  bun.lock
  package.json
  playwright.config.ts
  tsconfig.json
docs/  (7 files)
  journals/  (4 files)
    260812-1844-search-data-quality-planning.md
    260813-0816-phase-6-accessibility-refresh.md
    260813-1622-phase-7-web-stack-freshness.md
    260813-1800-search-data-overhaul-completion.md
  INSTALL.md
  ime-composition.md
  三个 data-scripts-templates 的区别.md
gallery/  (33 files)
  app/  (4 files)
    globals.css
    layout.tsx
    page.tsx
    providers.tsx
  components/  (15 files)
    CodeSnippet.tsx
    ColorPalette.tsx
    DarkModeToggle.tsx
    ExpandableSection.tsx
    FilterBar.tsx
    GalleryGrid.tsx
    InteractiveChecklist.tsx
    MetadataBadges.tsx
    PhoneMockup.tsx
    SearchInput.tsx
    StyleCard.tsx
    StyleDetailModal.tsx
    StylePreview.tsx
    UIControlsShowcase.tsx
    metadata-badges.test.tsx
  lib/  (6 files)
    colorExtractor.ts
    cssGenerator.ts
    filterStyles.ts
    parseStyles.test.ts
    parseStyles.ts
    types.ts
  .gitignore
  next-env.d.ts
  next.config.js
  package.json
  postcss.config.js
  tailwind.config.ts
  tsconfig.json
  tsconfig.test.json
preview/  (1 files)
  xiaomaomi-app.html
projects/  (3 files)
  healthcare-dashboard/  (1 files)
    index.html
  portfolio-dark/  (1 files)
    index.html
  saas-landing/  (1 files)
    index.html
scripts/  (11 files)
  tests/  (1 files)
    test_community_docs.py
  evaluate-relevance.py
  generate-catalog-summary.py
  refresh-google-fonts.py
  refresh-icon-catalog.py
  relevance_metrics.py
  smoke-domains.sh
  smoke-stacks.sh
  sync-release-version.mjs
  validate-agent-guide.py
  validate-csv.py
src/  (96 files)
  ui-ux-pro-max/  (96 files)
    data/  (36 files)
      … 36 files under this directory
    scripts/  (33 files)
      … 33 files under this directory
    templates/  (27 files)
      … 27 files under this directory
stack/  (18 files)
  .claude/  (4 files)
    agents/  (1 files)
      … 1 files under this directory
    commands/  (2 files)
      … 2 files under this directory
    settings.json
  .github/  (1 files)
    workflows/  (1 files)
      … 1 files under this directory
  docs/  (3 files)
    SETUP.md
    STACK.md
    WORKFLOW.md
  examples/  (3 files)
    juniper-audit/  (3 files)
      … 3 files under this directory
  scripts/  (2 files)
    design-audit.mjs
    setup.sh
  .gitignore
  .mcp.json
  CLAUDE.md
  README.md
  package.json
.gitattributes
.gitignore
.releaserc.json
CLAUDE.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.az.md
README.fa.md
README.fr.md
README.id.md
README.ja.md
README.ko.md
README.md
README.vi.md
README.zh.md
SECURITY.md
skill.json
```

## Entry points

- [src/ui-ux-pro-max/scripts/design_system.py:1657](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/d643997c82e94742dd3bee43210b0198e8bbba3d/src/ui-ux-pro-max/scripts/design_system.py#L1657)
- [src/ui-ux-pro-max/scripts/search.py:103](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/d643997c82e94742dd3bee43210b0198e8bbba3d/src/ui-ux-pro-max/scripts/search.py#L103)
- [src/ui-ux-pro-max/scripts/validate_data.py:1094](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/d643997c82e94742dd3bee43210b0198e8bbba3d/src/ui-ux-pro-max/scripts/validate_data.py#L1094)
- [.claude/skills/design-system/scripts/fetch-background.py:338](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/d643997c82e94742dd3bee43210b0198e8bbba3d/.claude/skills/design-system/scripts/fetch-background.py#L338)
- [.claude/skills/design-system/scripts/generate-slide.py:769](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/d643997c82e94742dd3bee43210b0198e8bbba3d/.claude/skills/design-system/scripts/generate-slide.py#L769)
- [.claude/skills/design-system/scripts/html-token-validator.py:358](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/d643997c82e94742dd3bee43210b0198e8bbba3d/.claude/skills/design-system/scripts/html-token-validator.py#L358)
- [.claude/skills/design-system/scripts/search-slides.py:227](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/d643997c82e94742dd3bee43210b0198e8bbba3d/.claude/skills/design-system/scripts/search-slides.py#L227)
- [.claude/skills/design-system/scripts/slide-token-validator.py:34](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/d643997c82e94742dd3bee43210b0198e8bbba3d/.claude/skills/design-system/scripts/slide-token-validator.py#L34)
- [.claude/skills/design/scripts/cip/generate.py:503](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/d643997c82e94742dd3bee43210b0198e8bbba3d/.claude/skills/design/scripts/cip/generate.py#L503)
- [.claude/skills/design/scripts/cip/render-html.py:423](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/d643997c82e94742dd3bee43210b0198e8bbba3d/.claude/skills/design/scripts/cip/render-html.py#L423)
- [.claude/skills/design/scripts/cip/search.py:126](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/d643997c82e94742dd3bee43210b0198e8bbba3d/.claude/skills/design/scripts/cip/search.py#L126)
- [.claude/skills/design/scripts/icon/generate.py:534](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/d643997c82e94742dd3bee43210b0198e8bbba3d/.claude/skills/design/scripts/icon/generate.py#L534)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cli package | library | Observed | Groups 27 file(s) under cli package (observed from repository paths and static analysis). Observed top-level classes: BM25. Observed top-level functions: _contains_phrase, _domain_keywords, _exact_match_diagnostic, _exa… |
| Configuration and deployment | config | Observed | Groups 67 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 25 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: DesignSystemGenerator, ShadcnInstaller, TailwindConfigGenerator, ValidationResult, _SafeR… |
| gallery package | library | Observed | Groups 28 file(s) under gallery package (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 4 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level functions: _check_rules, check_thresholds, grades_for_results, ndcg_at_k, precision_at_k, reciprocal_rank. |
| stack package | library | Observed | Groups 2 file(s) under stack package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 114 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH subprocess.run, PATCH subprocess.run, PATCH subprocess.run, PATCH subprocess.run, PATCH subprocess.run. Observe… |
| ui-ux-pro-max package | library | Observed | Groups 2 file(s) under ui-ux-pro-max package (observed from repository paths and static analysis). Observed top-level classes: BM25. Observed top-level functions: _contains_phrase, _domain_keywords, _exact_match_diagnos… |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.claude/skills/design-system/templates/design-tokens-starter.json` (config)
- `.claude/skills/ui-styling/scripts/requirements.txt` (manifest)
- `.claude/skills/ui-ux-pro-max/data/catalog-summary.json` (config)
- `.claude/skills/ui-ux-pro-max/data/data-provenance.json` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yml` (config)
- `.github/ISSUE_TEMPLATE/feature_request.yml` (config)
- `.github/workflows/bump-versions.yml` (ci)
- `.github/workflows/check-asset-sync.yml` (ci)
- `.github/workflows/refresh-catalogs.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/smoke-stacks.yml` (ci)
- `.github/workflows/tests.yml` (ci)
- `.releaserc.json` (config)
- `cli/assets/data/catalog-summary.json` (config)
- `cli/assets/data/data-provenance.json` (config)
- `cli/assets/skills/design-system/templates/design-tokens-starter.json` (config)
- `cli/assets/skills/ui-styling/scripts/requirements.txt` (manifest)
- `cli/assets/templates/platforms/agent.json` (config)
- `cli/assets/templates/platforms/amazonq.json` (config)
- `cli/assets/templates/platforms/augment.json` (config)
- `cli/assets/templates/platforms/autoclaw.json` (config)
- `cli/assets/templates/platforms/claude.json` (config)
- `cli/assets/templates/platforms/codebuddy.json` (config)
- `cli/assets/templates/platforms/codewhale.json` (config)
- `cli/assets/templates/platforms/codex.json` (config)
- `cli/assets/templates/platforms/continue.json` (config)
- `cli/assets/templates/platforms/copilot.json` (config)
- `cli/assets/templates/platforms/cursor.json` (config)
- `cli/assets/templates/platforms/droid.json` (config)
- `cli/assets/templates/platforms/gemini.json` (config)
- `cli/assets/templates/platforms/kilocode.json` (config)
- `cli/assets/templates/platforms/kimi.json` (config)
- `cli/assets/templates/platforms/kiro.json` (config)
- `cli/assets/templates/platforms/openclaw.json` (config)
- `cli/assets/templates/platforms/opencode.json` (config)
- `cli/assets/templates/platforms/qoder.json` (config)
- `cli/assets/templates/platforms/roocode.json` (config)
- `cli/assets/templates/platforms/trae.json` (config)
- `cli/assets/templates/platforms/universal.json` (config)
- `cli/assets/templates/platforms/warp.json` (config)
- `cli/assets/templates/platforms/windsurf.json` (config)
- `cli/assets/templates/platforms/zcode.json` (config)
- `cli/package.json` (manifest)
- `cli/tsconfig.json` (config)
- `gallery/package.json` (manifest)
- `gallery/tsconfig.json` (config)
- `gallery/tsconfig.test.json` (config)
- `skill.json` (config)
- `src/ui-ux-pro-max/data/catalog-summary.json` (config)
- `src/ui-ux-pro-max/data/data-provenance.json` (config)
- `src/ui-ux-pro-max/templates/platforms/agent.json` (config)
- `src/ui-ux-pro-max/templates/platforms/amazonq.json` (config)
- `src/ui-ux-pro-max/templates/platforms/augment.json` (config)
- `src/ui-ux-pro-max/templates/platforms/autoclaw.json` (config)
- `src/ui-ux-pro-max/templates/platforms/claude.json` (config)
- `src/ui-ux-pro-max/templates/platforms/codebuddy.json` (config)
- `src/ui-ux-pro-max/templates/platforms/codewhale.json` (config)
- `src/ui-ux-pro-max/templates/platforms/codex.json` (config)
- `src/ui-ux-pro-max/templates/platforms/continue.json` (config)
- `src/ui-ux-pro-max/templates/platforms/copilot.json` (config)
- `src/ui-ux-pro-max/templates/platforms/cursor.json` (config)
- `src/ui-ux-pro-max/templates/platforms/droid.json` (config)
- `src/ui-ux-pro-max/templates/platforms/gemini.json` (config)
- `src/ui-ux-pro-max/templates/platforms/kilocode.json` (config)
- `src/ui-ux-pro-max/templates/platforms/kimi.json` (config)
- `src/ui-ux-pro-max/templates/platforms/kiro.json` (config)
- `src/ui-ux-pro-max/templates/platforms/openclaw.json` (config)
- `src/ui-ux-pro-max/templates/platforms/opencode.json` (config)
- `src/ui-ux-pro-max/templates/platforms/qoder.json` (config)
- `src/ui-ux-pro-max/templates/platforms/roocode.json` (config)
- `src/ui-ux-pro-max/templates/platforms/trae.json` (config)
- `src/ui-ux-pro-max/templates/platforms/universal.json` (config)
- `src/ui-ux-pro-max/templates/platforms/warp.json` (config)
- `src/ui-ux-pro-max/templates/platforms/windsurf.json` (config)
- `src/ui-ux-pro-max/templates/platforms/zcode.json` (config)
- `stack/.claude/settings.json` (config)
- `stack/.github/workflows/design-review.yml` (ci)
- `stack/.mcp.json` (config)
- `stack/examples/juniper-audit/report.json` (config)
- `stack/package.json` (manifest)

## Top-level layout

- `cli` — 234 analysed file(s)
- `.claude` — 207 analysed file(s)
- `src` — 96 analysed file(s)
- `gallery` — 33 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `stack` — 18 analysed file(s)
- `scripts` — 11 analysed file(s)
- `.github` — 9 analysed file(s)
- `docs` — 7 analysed file(s)
- `projects` — 3 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `preview` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 2 file(s) were skipped during inventory (2 x lockfile excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `d643997c82e94742dd3bee43210b0198e8bbba3d` is the revision these paths and observations refer to.
