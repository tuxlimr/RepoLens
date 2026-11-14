# Project structure: guillaumemeyer/watermarks-remover

**Analysed commit:** `5a62be6338d2812372b1da440e55c82922f97d53`

**Commit reference:** [5a62be6338d2812372b1da440e55c82922f97d53](https://github.com/guillaumemeyer/watermarks-remover/commit/5a62be6338d2812372b1da440e55c82922f97d53)

**Tree at this commit:** [guillaumemeyer/watermarks-remover@5a62be6338d2](https://github.com/guillaumemeyer/watermarks-remover/tree/5a62be6338d2812372b1da440e55c82922f97d53)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | guillaumemeyer/watermarks-remover |
| Description | A privacy-first app that strips AI watermarks from content you own. |
| Stars | 27419 |
| Forks | 3106 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `5a62be6338d2812372b1da440e55c82922f97d53` |
| Retrieved at | 2026-11-14T19:07:20.653472+00:00 |
| Files in this snapshot | 295 |

## Directory tree

```text
.claude-plugin/  (2 files)
  marketplace.json
  plugin.json
.github/  (9 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_report.md
    feature_request.md
    release_suggestion.md
  workflows/  (3 files)
    ci.yml
    codeql.yml
    release-images.yml
  CODEOWNERS
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
benchmarks/  (100 files)
  corpus/  (8 files)
    cloud-computing.txt
    coffee-brewing.txt
    hiking-checklist.txt
    nutrition-myths.txt
    open-source-licenses.txt
    renewable-energy.txt
    small-biz-finance.txt
    venice-history.txt
  corpus-large/  (30 files)
    beekeeping.txt
    bicycle-maintenance.txt
    birdwatching.txt
    bookbinding.txt
    budget-travel.txt
    car-maintenance.txt
    cheese-making.txt
    cloud-computing.txt
    coffee-brewing.txt
    dog-training.txt
    emergency-preparedness.txt
    film-photography.txt
    fish-keeping.txt
    hiking-checklist.txt
    home-internet-setup.txt
    home-pest-control.txt
    nutrition-myths.txt
    ocean-plastics.txt
    open-source-licenses.txt
    pottery-basics.txt
    remote-work.txt
    renewable-energy.txt
    sleep-hygiene.txt
    small-biz-finance.txt
    … 6 more files
  corpus-polish/  (58 files)
    additional/  (3 files)
      … 3 files under this directory
    excluded-numeric/  (4 files)
      … 4 files under this directory
    01_chmura-obliczeniowa.txt
    02_parzenie-kawy.txt
    03_przygotowanie-do-wedrowki.txt
    04_mity-zywieniowe.txt
    05_licencje-otwartego-oprogramowania.txt
    06_energia-odnawialna.txt
    07_finanse-malej-firmy.txt
    08_historia-wenecji.txt
    09_brak-skladnika-w-piekarni.txt
    10_naprawa-starej-kuchni.txt
    11_zimowe-zapasy.txt
    12_podroz-bez-bagazu.txt
    13_opieka-nad-ogrodem.txt
    14_pomoc-w-schronisku.txt
    15_nauka-pracy-w-sklepie.txt
    16_przygotowanie-szkolnego-festynu.txt
    17_awaria-w-pensjonacie.txt
    18_rodzinny-posilek.txt
    19_pakowanie-przed-przeprowadzka.txt
    20_zakup-roweru.txt
    21_badanie-psa.txt
    22_planowanie-podrozy.txt
    23_poszukiwanie-turysty.txt
    24_spacer-z-psem.txt
    … 27 more files
  providers/  (1 files)
    deepseek.json
  README.md
  benchmark-full.sh
  benchmark-smoke.sh
config/  (1 files)
  clean_strategy.json
docs/  (5 files)
  plans/  (1 files)
    ideas/  (1 files)
      … 1 files under this directory
  deepseek-benchmark.md
  frontmatter-scanning.md
  synthid-text-benchmark.md
  windows-autostart.md
hooks/  (2 files)
  hooks.json
  run_hook.js
integrations/  (1 files)
  cursor/  (1 files)
    clean-user-facing-text.mdc
service/  (52 files)
  scripts/  (46 files)
    audit_dir.py
    audit_lib.py
    audit_website.py
    av_meta.py
    bench_deepseek_smoke.py
    bench_synthid_text.py
    check_staged.py
    clean_audio.py
    clean_ctrlregen.py
    clean_file.py
    clean_image.py
    clean_staged.py
    clean_text.py
    clean_video.py
    common.py
    container_meta.py
    detect_gumbel.py
    detect_text_watermark.py
    format_dispatch.py
    hook_written_file.py
    humanize_pass.py
    image_meta.py
    inspect_file.py
    inspect_image.py
    … 22 more files
  .dockerignore
  Dockerfile
  Dockerfile.ctrlregen
  Dockerfile.markdiffusion
  Dockerfile.markllm
  Dockerfile.synthid
skills/  (17 files)
  clean-user-facing-text/  (10 files)
    references/  (4 files)
      … 4 files under this directory
    scripts/  (5 files)
      … 5 files under this directory
    SKILL.md
  remove-ai-marks/  (7 files)
    references/  (6 files)
      … 6 files under this directory
    SKILL.md
stealer/  (6 files)
  README.md
  __init__.py
  download_prompts.py
  scorer.py
  steal.py
  tokens.py
tests/  (82 files)
  fixtures/  (6 files)
    sample_ai.html
    sample_ai.md
    sample_meta.svg
    sample_watermarked.txt
    stylometry_ai_sample.txt
    stylometry_human_sample.txt
  conftest.py
  test_ai_generator_hints.py
  test_audit.py
  test_audit_sarif_and_concurrency.py
  test_av_meta.py
  test_avif_heic.py
  test_backup_preserved.py
  test_bench_deepseek_smoke.py
  test_bench_synthid_text.py
  test_binary_guard.py
  test_c2patool_report.py
  test_capabilities_tooling.py
  test_child_console_windows.py
  test_clean_audio.py
  test_clean_file_clean_exit.py
  test_clean_file_quiet.py
  test_clean_image.py
  test_clean_options_normalize_spaces.py
  test_clean_strategy.py
  test_clean_text.py
  test_clean_video.py
  test_container_meta.py
  test_ctrlregen_clean.py
  test_detect_endpoint.py
  … 52 more files
.coderabbit.yaml
.dockerignore
.env.example
.gitignore
.pre-commit-hooks.yaml
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
Makefile
README.md
SECURITY.md
compose-check.sh
compose.yaml
install-skill.sh
install_skill.py
pytest.ini
requirements-dev.txt
ruff.toml
```

## Entry points

- [install_skill.py:449](https://github.com/guillaumemeyer/watermarks-remover/blob/5a62be6338d2812372b1da440e55c82922f97d53/install_skill.py#L449)
- [service/scripts/audit_dir.py:167](https://github.com/guillaumemeyer/watermarks-remover/blob/5a62be6338d2812372b1da440e55c82922f97d53/service/scripts/audit_dir.py#L167)
- [service/scripts/audit_website.py:662](https://github.com/guillaumemeyer/watermarks-remover/blob/5a62be6338d2812372b1da440e55c82922f97d53/service/scripts/audit_website.py#L662)
- [service/scripts/bench_deepseek_smoke.py:214](https://github.com/guillaumemeyer/watermarks-remover/blob/5a62be6338d2812372b1da440e55c82922f97d53/service/scripts/bench_deepseek_smoke.py#L214)
- [service/scripts/bench_synthid_text.py:3827](https://github.com/guillaumemeyer/watermarks-remover/blob/5a62be6338d2812372b1da440e55c82922f97d53/service/scripts/bench_synthid_text.py#L3827)
- [service/scripts/check_staged.py:84](https://github.com/guillaumemeyer/watermarks-remover/blob/5a62be6338d2812372b1da440e55c82922f97d53/service/scripts/check_staged.py#L84)
- [service/scripts/clean_audio.py:310](https://github.com/guillaumemeyer/watermarks-remover/blob/5a62be6338d2812372b1da440e55c82922f97d53/service/scripts/clean_audio.py#L310)
- [service/scripts/clean_ctrlregen.py:211](https://github.com/guillaumemeyer/watermarks-remover/blob/5a62be6338d2812372b1da440e55c82922f97d53/service/scripts/clean_ctrlregen.py#L211)
- [service/scripts/clean_file.py:291](https://github.com/guillaumemeyer/watermarks-remover/blob/5a62be6338d2812372b1da440e55c82922f97d53/service/scripts/clean_file.py#L291)
- [service/scripts/clean_image.py:209](https://github.com/guillaumemeyer/watermarks-remover/blob/5a62be6338d2812372b1da440e55c82922f97d53/service/scripts/clean_image.py#L209)
- [service/scripts/clean_staged.py:186](https://github.com/guillaumemeyer/watermarks-remover/blob/5a62be6338d2812372b1da440e55c82922f97d53/service/scripts/clean_staged.py#L186)
- [service/scripts/clean_text.py:97](https://github.com/guillaumemeyer/watermarks-remover/blob/5a62be6338d2812372b1da440e55c82922f97d53/service/scripts/clean_text.py#L97)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmarks package | library | Observed | Groups 2 file(s) under benchmarks package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 18 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 31 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Benchmark, Handler, HumanLikeness, MarkLLMWorker, MarkerMatch, SemanticEmbedder. Observed… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| hooks package | library | Observed | Groups 1 file(s) under hooks package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 14 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AVInspectReport, CharHit, ClaudeTextDetector, ContainerInspectReport, GumbelTextDetector,… |
| skills package | library | Observed | Groups 2 file(s) under skills package (observed from repository paths and static analysis). Observed top-level classes: CharHit, TextInspectReport. Observed top-level functions: _char_label, _configure_stdio, _decide, _… |
| stealer package | library | Observed | Groups 3 file(s) under stealer package (observed from repository paths and static analysis). Observed top-level functions: _prob, apply_delta, build_scorer, context_key, count_ngrams, default_tokenize. |
| Tests | test | Observed | Groups 82 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestSvgSecurityHardening, _Completed, _FakeBench, _FakeMarkLLM, _FakeOpener, _FakeResp. Observed top-level… |

## Important files

- `.claude-plugin/marketplace.json` (config)
- `.claude-plugin/plugin.json` (config)
- `.coderabbit.yaml` (config)
- `.dockerignore` (container)
- `.env.example` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/ci.yml` (ci)
- `.github/workflows/codeql.yml` (ci)
- `.github/workflows/release-images.yml` (ci)
- `.pre-commit-hooks.yaml` (config)
- `benchmarks/providers/deepseek.json` (config)
- `compose.yaml` (container)
- `config/clean_strategy.json` (config)
- `hooks/hooks.json` (config)
- `pytest.ini` (config)
- `requirements-dev.txt` (manifest)
- `ruff.toml` (config)
- `service/.dockerignore` (container)
- `service/Dockerfile` (container)
- `service/Dockerfile.ctrlregen` (container)
- `service/Dockerfile.markdiffusion` (container)
- `service/Dockerfile.markllm` (container)
- `service/Dockerfile.synthid` (container)
- `service/scripts/requirements-ctrlregen.txt` (manifest)
- `service/scripts/requirements-markdiffusion.txt` (manifest)
- `service/scripts/requirements-markllm.txt` (manifest)
- `service/scripts/requirements-semantic.txt` (manifest)
- `service/scripts/requirements-synthid-scorer.txt` (manifest)

## Top-level layout

- `benchmarks` — 100 analysed file(s)
- `tests` — 82 analysed file(s)
- `service` — 52 analysed file(s)
- `(root files)` — 18 analysed file(s)
- `skills` — 17 analysed file(s)
- `.github` — 9 analysed file(s)
- `stealer` — 6 analysed file(s)
- `docs` — 5 analysed file(s)
- `.claude-plugin` — 2 analysed file(s)
- `hooks` — 2 analysed file(s)
- `config` — 1 analysed file(s)
- `integrations` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5a62be6338d2812372b1da440e55c82922f97d53` is the revision these paths and observations refer to.
