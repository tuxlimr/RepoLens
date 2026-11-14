# Project structure: coreyhaines31/marketingskills

**Analysed commit:** `1f837447b20bb6f0e72d87b80ece1c221c362c7d`

**Commit reference:** [1f837447b20bb6f0e72d87b80ece1c221c362c7d](https://github.com/coreyhaines31/marketingskills/commit/1f837447b20bb6f0e72d87b80ece1c221c362c7d)

**Tree at this commit:** [coreyhaines31/marketingskills@1f837447b20b](https://github.com/coreyhaines31/marketingskills/tree/1f837447b20bb6f0e72d87b80ece1c221c362c7d)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | coreyhaines31/marketingskills |
| Description | Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering. |
| Stars | 60299 |
| Forks | 8803 |
| Licence | MIT |
| Language | JavaScript |
| Default branch | main |
| Analysed commit | `1f837447b20bb6f0e72d87b80ece1c221c362c7d` |
| Retrieved at | 2026-11-14T19:10:36.314733+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.agents/  (1 files)
  plugins/  (1 files)
    marketplace.json
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.codex-plugin/  (1 files)
  plugin.json
.github/  (13 files)
  ISSUE_TEMPLATE/  (2 files)
    config.yml
    skill-request.yml
  PULL_REQUEST_TEMPLATE/  (3 files)
    documentation.md
    new-skill.md
    skill-update.md
  scripts/  (1 files)
    sync-skills.js
  workflows/  (6 files)
    check-versions.yml
    regression-tests.yml
    release.yml
    skill-packaging.yml
    sync-skills.yml
    validate-skill.yml
  FUNDING.yml
docs/  (1 files)
  skill-release-packaging.md
evals/  (6 files)
  triggers/  (6 files)
    README.md
    heldout.json
    heldout2.json
    heldout3.json
    heldout4.json
    prompts.json
scripts/  (5 files)
  check-versions.mjs
  claude-web-descriptions.json
  package_skills.py
  sync-partners.mjs
  trigger-eval.mjs
skills/  (460 files)
  ab-testing/  (4 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  ad-creative/  (14 files)
    assets/  (1 files)
      … 1 files under this directory
    evals/  (1 files)
      … 1 files under this directory
    references/  (11 files)
      … 11 files under this directory
    SKILL.md
  ads/  (18 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (16 files)
      … 16 files under this directory
    SKILL.md
  ai-seo/  (17 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (15 files)
      … 15 files under this directory
    SKILL.md
  analytics/  (5 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    SKILL.md
  aso/  (7 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  attribution/  (6 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (4 files)
      … 4 files under this directory
    SKILL.md
  churn-prevention/  (4 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  co-marketing/  (3 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
  cold-email/  (12 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (10 files)
      … 10 files under this directory
    SKILL.md
  community-marketing/  (3 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
  competitor-profiling/  (4 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  competitors/  (4 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  content-strategy/  (4 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  conversion-tracking/  (75 files)
    assets/  (62 files)
      … 62 files under this directory
    evals/  (1 files)
      … 1 files under this directory
    references/  (9 files)
      … 9 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    SKILL.md
  copy-editing/  (5 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    SKILL.md
  copywriting/  (5 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    SKILL.md
  cro/  (4 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  customer-research/  (4 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  directory-submissions/  (7 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  emails/  (5 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    SKILL.md
  events/  (6 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (4 files)
      … 4 files under this directory
    SKILL.md
  free-tools/  (4 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  image/  (3 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
  influencer-marketing/  (6 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (4 files)
      … 4 files under this directory
    SKILL.md
  launch/  (4 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  lead-magnets/  (7 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  link-building/  (5 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    SKILL.md
  marketing-council/  (15 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (13 files)
      … 13 files under this directory
    SKILL.md
  marketing-ideas/  (4 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  marketing-loops/  (9 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (7 files)
      … 7 files under this directory
    SKILL.md
  marketing-plan/  (16 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (14 files)
      … 14 files under this directory
    SKILL.md
  marketing-psychology/  (2 files)
    evals/  (1 files)
      … 1 files under this directory
    SKILL.md
  offers/  (10 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (8 files)
      … 8 files under this directory
    SKILL.md
  onboarding/  (5 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (3 files)
      … 3 files under this directory
    SKILL.md
  paywalls/  (4 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  popups/  (2 files)
    evals/  (1 files)
      … 1 files under this directory
    SKILL.md
  pricing/  (6 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (4 files)
      … 4 files under this directory
    SKILL.md
  product-marketing/  (3 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
  programmatic-seo/  (4 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (2 files)
      … 2 files under this directory
    SKILL.md
  prospecting/  (12 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (10 files)
      … 10 files under this directory
    SKILL.md
  public-relations/  (10 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (8 files)
      … 8 files under this directory
    SKILL.md
  referrals/  (9 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (7 files)
      … 7 files under this directory
    SKILL.md
  reverse-engineer-marketing/  (45 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (42 files)
      … 42 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    SKILL.md
  revops/  (7 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (5 files)
      … 5 files under this directory
    SKILL.md
  sales-enablement/  (8 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (6 files)
      … 6 files under this directory
    SKILL.md
  schema/  (3 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (1 files)
      … 1 files under this directory
    SKILL.md
  seo-audit/  (9 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (7 files)
      … 7 files under this directory
    SKILL.md
  signup/  (2 files)
    evals/  (1 files)
      … 1 files under this directory
    SKILL.md
  site-architecture/  (6 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (4 files)
      … 4 files under this directory
    SKILL.md
  sms/  (6 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (4 files)
      … 4 files under this directory
    SKILL.md
  social/  (12 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (10 files)
      … 10 files under this directory
    SKILL.md
  video/  (6 files)
    evals/  (1 files)
      … 1 files under this directory
    references/  (4 files)
      … 4 files under this directory
    SKILL.md
tests/  (152 files)
  assets/  (4 files)
    conversion-tracking-formidable-forms.test.cjs
    conversion-tracking-generic-ajax-form.test.cjs
    conversion-tracking-thank-you-page.test.cjs
    creative-review-images.test.cjs
  clis/  (138 files)
    activecampaign-contact-fields.test.cjs
    adobe-report-suites.test.cjs
    ahrefs-link-reports.test.cjs
    ahrefs-reports.test.cjs
    airops-public-api.test.cjs
    amplitude-device-identity.test.cjs
    amplitude-export.test.cjs
    amplitude-json-shapes.test.cjs
    amplitude-retention-events.test.cjs
    amplitude-user-activity.test.cjs
    apollo-employee-ranges.test.cjs
    apollo-enrichment.test.cjs
    beehiiv-post-content.test.cjs
    beehiiv-update.test.cjs
    brevo-contact-suppression.test.cjs
    buffer-publish-flags.test.cjs
    calendly-webhooks.test.cjs
    cloro-requests.test.cjs
    close-collection-pagination.test.cjs
    close-opportunity-status.test.cjs
    close-opportunity-value.test.cjs
    crossbeam-overlaps.test.cjs
    customer-io-suppression.test.cjs
    customerio-identifiers.test.cjs
    … 114 more files
  fixtures/  (8 files)
    invalid/  (8 files)
      … 8 files under this directory
  run-regression.sh
  test_skill_packaging.py
tools/  (152 files)
  aisa/  (4 files)
    evals/  (2 files)
      … 2 files under this directory
    README.md
    coverage-map.md
  clis/  (68 files)
    README.md
    activecampaign.js
    adobe-analytics.js
    ahrefs.js
    airops.js
    amplitude.js
    apollo.js
    beehiiv.js
    brevo.js
    buffer.js
    calendly.js
    clay.js
    clearbit.js
    cloro.js
    close.js
    coupler.js
    crossbeam.js
    customer-io.js
    dataforseo.js
    demio.js
    dub.js
    exa.js
    firecrawl.js
    g2.js
    … 44 more files
  composio/  (2 files)
    README.md
    marketing-tools.md
  integrations/  (75 files)
    activecampaign.md
    admakeai.md
    adobe-analytics.md
    agentaos.md
    ahrefs.md
    airops.md
    aisa.md
    amplitude.md
    apify.md
    apollo.md
    attentive.md
    attio.md
    audiencetap.md
    beehiiv.md
    brevo.md
    browserbase.md
    buffer.md
    calendly.md
    clay.md
    clearbit.md
    cloro.md
    close.md
    cogny.md
    composio.md
    … 51 more files
  PARTNERS.md
  REGISTRY.md
  SETUP.md
.gitignore
AGENTS.md
CONTRIBUTING.md
LICENSE
README.md
VERSIONS.md
partners.json
```

## Entry points

- [scripts/package_skills.py:223](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/scripts/package_skills.py#L223)
- [skills/conversion-tracking/scripts/build_recipe.py:222](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/conversion-tracking/scripts/build_recipe.py#L222)
- [skills/conversion-tracking/scripts/check_recipes.py:88](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/conversion-tracking/scripts/check_recipes.py#L88)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 94 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 3 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: build, expected_html, fail, git, html_param, js_escape. |
| scripts package | library | Observed | Groups 3 file(s) under scripts package (observed from repository paths and static analysis). |
| skills package | library | Observed | Groups 27 file(s) under skills package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 152 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: PackagingTests. |
| tools package | library | Observed | Groups 67 file(s) under tools package (observed from repository paths and static analysis). |

## Important files

- `.agents/plugins/marketplace.json` (config)
- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.codex-plugin/plugin.json` (config)
- `.github/FUNDING.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/skill-request.yml` (config)
- `.github/workflows/check-versions.yml` (ci)
- `.github/workflows/regression-tests.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.github/workflows/skill-packaging.yml` (ci)
- `.github/workflows/sync-skills.yml` (ci)
- `.github/workflows/validate-skill.yml` (ci)
- `evals/triggers/heldout.json` (config)
- `evals/triggers/heldout2.json` (config)
- `evals/triggers/heldout3.json` (config)
- `evals/triggers/heldout4.json` (config)
- `evals/triggers/prompts.json` (config)
- `partners.json` (config)
- `scripts/claude-web-descriptions.json` (config)
- `skills/ab-testing/evals/evals.json` (config)
- `skills/ad-creative/evals/evals.json` (config)
- `skills/ads/evals/evals.json` (config)
- `skills/ai-seo/evals/evals.json` (config)
- `skills/analytics/evals/evals.json` (config)
- `skills/aso/evals/evals.json` (config)
- `skills/attribution/evals/evals.json` (config)
- `skills/churn-prevention/evals/evals.json` (config)
- `skills/co-marketing/evals/evals.json` (config)
- `skills/cold-email/evals/evals.json` (config)
- `skills/community-marketing/evals/evals.json` (config)
- `skills/competitor-profiling/evals/evals.json` (config)
- `skills/competitors/evals/evals.json` (config)
- `skills/content-strategy/evals/evals.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-acuity-scheduling.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-cal-com.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-calendly.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-contact-form-7.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-divi-forms.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-elementor-forms.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-file-download.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-fluent-forms.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-formidable-forms.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-forminator.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-framer-forms.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-generic-ajax-form.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-gravity-forms.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-hubspot-forms.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-jotform.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-ninja-forms.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-phone-click.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-squarespace-forms.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-tally.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-thank-you-page.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-typeform.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-webflow-forms.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-wix-forms.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-wix-scheduling.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-wpforms.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/detect/detect-ws-form.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/event-map.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/send/ga4.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/send/google-ads.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/send/linkedin.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/send/meta.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/send/microsoft.json` (config)
- `skills/conversion-tracking/assets/gtm-recipes/send/tiktok.json` (config)
- `skills/conversion-tracking/evals/evals.json` (config)
- `skills/copy-editing/evals/evals.json` (config)
- `skills/copywriting/evals/evals.json` (config)
- `skills/cro/evals/evals.json` (config)
- `skills/customer-research/evals/evals.json` (config)
- `skills/directory-submissions/evals/evals.json` (config)
- `skills/emails/evals/evals.json` (config)
- `skills/events/evals/evals.json` (config)
- `skills/free-tools/evals/evals.json` (config)
- `skills/image/evals/evals.json` (config)
- `skills/influencer-marketing/evals/evals.json` (config)
- `skills/launch/evals/evals.json` (config)
- `skills/lead-magnets/evals/evals.json` (config)
- `skills/link-building/evals/evals.json` (config)
- `skills/marketing-council/evals/evals.json` (config)
- `skills/marketing-ideas/evals/evals.json` (config)
- `skills/marketing-loops/evals/evals.json` (config)
- `skills/marketing-plan/evals/evals.json` (config)
- `skills/marketing-psychology/evals/evals.json` (config)
- `skills/offers/evals/evals.json` (config)
- `skills/onboarding/evals/evals.json` (config)
- `skills/paywalls/evals/evals.json` (config)
- `skills/popups/evals/evals.json` (config)
- `skills/pricing/evals/evals.json` (config)
- `skills/product-marketing/evals/evals.json` (config)
- `skills/programmatic-seo/evals/evals.json` (config)
- `skills/prospecting/evals/evals.json` (config)
- `skills/public-relations/evals/evals.json` (config)
- `skills/referrals/evals/evals.json` (config)
- `skills/reverse-engineer-marketing/evals/evals.json` (config)
- `skills/revops/evals/evals.json` (config)
- `skills/sales-enablement/evals/evals.json` (config)
- `skills/schema/evals/evals.json` (config)
- `skills/seo-audit/evals/evals.json` (config)
- `skills/signup/evals/evals.json` (config)
- `skills/site-architecture/evals/evals.json` (config)
- `skills/sms/evals/evals.json` (config)
- `skills/social/evals/evals.json` (config)
- `skills/video/evals/evals.json` (config)
- `tools/aisa/evals/evals.json` (config)

## Top-level layout

- `skills` — 460 analysed file(s)
- `tests` — 152 analysed file(s)
- `tools` — 152 analysed file(s)
- `.github` — 13 analysed file(s)
- `(root files)` — 7 analysed file(s)
- `evals` — 6 analysed file(s)
- `scripts` — 5 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `.agents` — 1 analysed file(s)
- `.codex-plugin` — 1 analysed file(s)
- `docs` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `1f837447b20bb6f0e72d87b80ece1c221c362c7d` is the revision these paths and observations refer to.
