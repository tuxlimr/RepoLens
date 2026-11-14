# Project structure: aiming-lab/AutoResearchClaw

**Analysed commit:** `be4ba4755bf1b52220f25e13b2293b5956590070`

**Commit reference:** [be4ba4755bf1b52220f25e13b2293b5956590070](https://github.com/aiming-lab/AutoResearchClaw/commit/be4ba4755bf1b52220f25e13b2293b5956590070)

**Tree at this commit:** [aiming-lab/AutoResearchClaw@be4ba4755bf1](https://github.com/aiming-lab/AutoResearchClaw/tree/be4ba4755bf1b52220f25e13b2293b5956590070)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | aiming-lab/AutoResearchClaw |
| Description | Fully autonomous & self-evolving research from idea to paper. Chat an Idea. Get a Paper. 🦞 |
| Stars | 14875 |
| Forks | 1714 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `be4ba4755bf1b52220f25e13b2293b5956590070` |
| Retrieved at | 2026-11-14T19:09:14.012518+00:00 |
| Files in this snapshot | 727 |

## Directory tree

```text
.claude/  (9 files)
  skills/  (9 files)
    a-evolve/  (1 files)
      … 1 files under this directory
    biology-biopython/  (1 files)
      … 1 files under this directory
    chemistry-rdkit/  (1 files)
      … 1 files under this directory
    hypothesis-formulation/  (1 files)
      … 1 files under this directory
    literature-search/  (1 files)
      … 1 files under this directory
    researchclaw/  (1 files)
      … 1 files under this directory
    scientific-visualization/  (1 files)
      … 1 files under this directory
    scientific-writing/  (1 files)
      … 1 files under this directory
    statistical-reporting/  (1 files)
      … 1 files under this directory
docs/  (20 files)
  examples/  (1 files)
    medical_observational_demo.md
  showcase/  (1 files)
    SHOWCASE.md
  CHANGELOG_ANTHROPIC_ADAPTER.md
  CODE_REVIEW_2026-07-03.md
  DOMAIN_INTEGRATION_GUIDE.md
  HITL_GUIDE.md
  README_AR.md
  README_CN.md
  README_DE.md
  README_ES.md
  README_FR.md
  README_JA.md
  README_KO.md
  README_PT.md
  README_RU.md
  TESTER_GUIDE.md
  TESTER_GUIDE_CN.md
  TESTER_GUIDE_JA.md
  debate_engine.md
  integration-guide.md
experiments/  (176 files)
  arc_bench/  (176 files)
    baseline/  (33 files)
      … 33 files under this directory
    config/  (120 files)
      … 120 files under this directory
    scripts/  (20 files)
      … 20 files under this directory
    EXPERIMENT_DESIGN.md
    README.md
    RUN_GUIDE.md
external/  (31 files)
  agents/  (31 files)
    Biology-Agent/  (13 files)
      … 13 files under this directory
    ColliderAgent/  (1 files)
      … 1 files under this directory
    stat_research_agent/  (16 files)
      … 16 files under this directory
    README.md
frontend-legacy/  (13 files)
  src/  (11 files)
    components/  (7 files)
      … 7 files under this directory
    services/  (2 files)
      … 2 files under this directory
    styles/  (1 files)
      … 1 files under this directory
    app.js
  index.html
  package.json
researchclaw/  (354 files)
  agents/  (24 files)
    benchmark_agent/  (6 files)
      … 6 files under this directory
    code_searcher/  (6 files)
      … 6 files under this directory
    figure_agent/  (10 files)
      … 10 files under this directory
    __init__.py
    base.py
  assessor/  (5 files)
    __init__.py
    comparator.py
    rubrics.py
    scorer.py
    venue_recommender.py
  calendar/  (5 files)
    data/  (1 files)
      … 1 files under this directory
    __init__.py
    deadlines.py
    planner.py
    reminder.py
  collaboration/  (5 files)
    __init__.py
    dedup.py
    publisher.py
    repository.py
    subscriber.py
  copilot/  (5 files)
    __init__.py
    branching.py
    controller.py
    feedback.py
    modes.py
  dashboard/  (4 files)
    __init__.py
    broadcaster.py
    collector.py
    metrics.py
  data/  (10 files)
    framework_docs/  (5 files)
      … 5 files under this directory
    __init__.py
    benchmark_knowledge.yaml
    dataset_registry.yaml
    docker_profiles.yaml
    seminal_papers.yaml
  docker/  (8 files)
    Dockerfile
    Dockerfile.biology
    Dockerfile.chemistry
    Dockerfile.economics
    Dockerfile.generic
    Dockerfile.math
    Dockerfile.physics
    entrypoint.sh
  domains/  (48 files)
    adapters/  (13 files)
      … 13 files under this directory
    profiles/  (30 files)
      … 30 files under this directory
    __init__.py
    deploy.py
    detector.py
    experiment_schema.py
    prompt_adapter.py
  experiment/  (19 files)
    evaluators/  (2 files)
      … 2 files under this directory
    __init__.py
    agentic_sandbox.py
    biology_agent_sandbox.py
    code_agent.py
    colab_sandbox.py
    collider_agent_sandbox.py
    docker_sandbox.py
    factory.py
    git_manager.py
    harness_template.py
    metrics.py
    runner.py
    sandbox.py
    ssh_sandbox.py
    stat_agent_sandbox.py
    validator.py
    visualize.py
  feedback/  (1 files)
    FEEDBACK_ANALYSIS_PROMPT.md
  hitl/  (35 files)
    adapters/  (5 files)
      … 5 files under this directory
    tui/  (3 files)
      … 3 files under this directory
    workshops/  (4 files)
      … 4 files under this directory
    __init__.py
    branching.py
    chat.py
    checksums.py
    claim_verifier.py
    collaboration.py
    config.py
    context_manager.py
    cost_guard.py
    diff_view.py
    editor.py
    escalation.py
    file_wait.py
    hooks.py
    intervention.py
    learning.py
    notify.py
    presets.py
    quality_predictor.py
    session.py
    smart_pause.py
    store.py
    summarizer.py
  knowledge/  (8 files)
    graph/  (6 files)
      … 6 files under this directory
    __init__.py
    base.py
  literature/  (10 files)
    __init__.py
    arxiv_client.py
    cache.py
    models.py
    novelty.py
    openalex_client.py
    search.py
    semantic_scholar.py
    trends.py
    verify.py
  llm/  (4 files)
    __init__.py
    acp_client.py
    anthropic_adapter.py
    client.py
  mcp/  (6 files)
    __init__.py
    client.py
    registry.py
    server.py
    tools.py
    transport.py
  memory/  (8 files)
    __init__.py
    decay.py
    embeddings.py
    experiment_memory.py
    ideation_memory.py
    retriever.py
    store.py
    writing_memory.py
  metaclaw_bridge/  (7 files)
    __init__.py
    config.py
    lesson_to_skill.py
    prm_gate.py
    session.py
    skill_feedback.py
    stage_skill_map.py
  overleaf/  (5 files)
    __init__.py
    conflict.py
    formatter.py
    sync.py
    watcher.py
  pipeline/  (26 files)
    stage_impls/  (10 files)
      … 10 files under this directory
    __init__.py
    _domain.py
    _helpers.py
    code_agent.py
    contracts.py
    debate.py
    executor.py
    experiment_diagnosis.py
    experiment_repair.py
    opencode_bridge.py
    paper_verifier.py
    requirements_judge.py
    runner.py
    stages.py
    tournament.py
    verified_registry.py
  project/  (5 files)
    __init__.py
    idea_pool.py
    manager.py
    models.py
    scheduler.py
  prompts/  (6 files)
    __init__.py
    biology.py
    hep.py
    manager.py
    ml.py
    shared.py
  server/  (16 files)
    dialog/  (4 files)
      … 4 files under this directory
    middleware/  (2 files)
      … 2 files under this directory
    routes/  (5 files)
      … 5 files under this directory
    websocket/  (3 files)
      … 3 files under this directory
    __init__.py
    app.py
  servers/  (7 files)
    __init__.py
    cloud_executor.py
    dispatcher.py
    monitor.py
    registry.py
    slurm_executor.py
    ssh_executor.py
  skills/  (26 files)
    builtin/  (21 files)
      … 21 files under this directory
    __init__.py
    loader.py
    matcher.py
    registry.py
    schema.py
  templates/  (15 files)
    styles/  (10 files)
      … 10 files under this directory
    __init__.py
    compiler.py
    conference.py
    converter.py
    results_table_builder.py
  trends/  (6 files)
    __init__.py
    auto_topic.py
    daily_digest.py
    feeds.py
    opportunity_finder.py
    trend_analyzer.py
  utils/  (3 files)
    __init__.py
    sanitize.py
    thinking_tags.py
  voice/  (4 files)
    __init__.py
    commands.py
    synthesizer.py
    transcriber.py
  web/  (7 files)
    __init__.py
    _ssrf.py
    agent.py
    crawler.py
    pdf_extractor.py
    scholar.py
    search.py
  wizard/  (4 files)
    __init__.py
    quickstart.py
    templates.py
    validator.py
  __init__.py
  __main__.py
  adapters.py
  cli.py
  config.py
  evolution.py
  evolution_aevolve.py
  hardware.py
  health.py
  quality.py
  report.py
  writing_guide.py
scripts/  (6 files)
  metaclaw_start.sh
  plot_iteration_showcase.py
  test_beast_mode_e2e.py
  test_code_agent_live.py
  test_code_agent_sandbox.py
  test_codegen_v2.py
tests/  (101 files)
  test_metaclaw_bridge/  (7 files)
    __init__.py
    test_config.py
    test_lesson_to_skill.py
    test_prm_gate.py
    test_session.py
    test_skill_feedback.py
    test_stage_skill_map.py
  __init__.py
  conftest.py
  e2e_docker_sandbox.py
  e2e_real_llm.py
  test_anthropic.py
  test_assessor.py
  test_atlascloud_provider.py
  test_benchmark_agent.py
  test_calendar.py
  test_cli.py
  test_code_agent.py
  test_code_searcher.py
  test_collaboration.py
  test_compiler.py
  test_convergence_evaluator.py
  test_copilot.py
  test_debate_engine.py
  test_decision_agent.py
  test_domain_detector.py
  test_entry_point_validation.py
  test_evolution_aevolve.py
  test_experiment_diagnosis.py
  test_experiment_repair.py
  test_experiment_schema.py
  … 70 more files
website/  (6 files)
  features.html
  getting-started.html
  index.html
  papers.html
  pipeline.html
  style.css
.gitignore
CONTRIBUTING.md
LICENSE
README.md
RESEARCHCLAW_AGENTS.md
RESEARCHCLAW_CLAUDE.md
config.researchclaw.example.yaml
prompts.default.yaml
pyproject.toml
run_hep_pipeline.sh
sentinel.sh
```

## Entry points

- [experiments/arc_bench/baseline/adapters/_aide_runner.py:153](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/experiments/arc_bench/baseline/adapters/_aide_runner.py#L153)
- [experiments/arc_bench/scripts/_inject_p_requirements.py:229](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/experiments/arc_bench/scripts/_inject_p_requirements.py#L229)
- [experiments/arc_bench/scripts/_rename_t_to_ml.py:156](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/experiments/arc_bench/scripts/_rename_t_to_ml.py#L156)
- [experiments/arc_bench/scripts/evaluate.py:191](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/experiments/arc_bench/scripts/evaluate.py#L191)
- [experiments/arc_bench/scripts/hitl_suggestor.py:251](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/experiments/arc_bench/scripts/hitl_suggestor.py#L251)
- [experiments/arc_bench/scripts/judge.py:1115](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/experiments/arc_bench/scripts/judge.py#L1115)
- [experiments/arc_bench/scripts/judge_manual.py:152](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/experiments/arc_bench/scripts/judge_manual.py#L152)
- [experiments/arc_bench/scripts/judge_results_only.py:234](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/experiments/arc_bench/scripts/judge_results_only.py#L234)
- [experiments/arc_bench/scripts/make_manifests.py:287](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/experiments/arc_bench/scripts/make_manifests.py#L287)
- [experiments/arc_bench/scripts/prepare_run.py:222](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/experiments/arc_bench/scripts/prepare_run.py#L222)
- [experiments/arc_bench/scripts/run_ais_v2.py:747](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/experiments/arc_bench/scripts/run_ais_v2.py#L747)
- [experiments/arc_bench/scripts/run_baseline.py:291](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/experiments/arc_bench/scripts/run_baseline.py#L291)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 5 file(s) under api layer (observed from repository paths and static analysis). Observed routes: POST /pipeline/start, POST /pipeline/stop, GET /pipeline/status, GET /pipeline/stages, GET /runs. Observed top-leve… |
| Configuration and deployment | config | Observed | Groups 191 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: AcpConfig, AgenticConfig, BenchmarkAgentConfig, BiologyAgentConfig, CalendarConfig,… |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Author, Idea, Paper, Project. Observed top-level functions: _load_all, detect_frameworks, load_framewor… |
| Application entry point | entrypoint | Observed | Groups 19 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via FastAPI. Observed top-level classes: ResearchClawMCPServer. Observed top-leve… |
| experiments package | library | Observed | Groups 6 file(s) under experiments package (observed from repository paths and static analysis). |
| External integrations | external | Observed | Groups 30 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: ACPClient, ACPConfig, AIScientistV2Adapter, AgentLabAdapter, AideAdapter, BiologyMetabolicP… |
| frontend-legacy package | library | Observed | Groups 8 file(s) under frontend-legacy package (observed from repository paths and static analysis). |
| researchclaw package | library | Observed | Groups 237 file(s) under researchclaw package (observed from repository paths and static analysis). Observed top-level classes: AcquirerAgent, AdapterBundle, AgentOrchestrator, AgentStepResult, AgenticResult, AgenticSan… |
| scripts package | library | Observed | Groups 2 file(s) under scripts package (observed from repository paths and static analysis). |
| Service / domain layer | service | Observed | Groups 2 file(s) under service / domain layer (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 105 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH researchclaw.templates.compiler.subprocess.run, PATCH researchclaw.templates.compiler.subprocess.run, PATCH res… |

## Important files

- `config.researchclaw.example.yaml` (config)
- `experiments/arc_bench/baseline/interventions/T01.json` (config)
- `experiments/arc_bench/baseline/interventions/T02.json` (config)
- `experiments/arc_bench/baseline/interventions/T03.json` (config)
- `experiments/arc_bench/baseline/interventions/T04.json` (config)
- `experiments/arc_bench/baseline/interventions/T05.json` (config)
- `experiments/arc_bench/baseline/interventions/T06.json` (config)
- `experiments/arc_bench/baseline/interventions/T07.json` (config)
- `experiments/arc_bench/baseline/interventions/T08.json` (config)
- `experiments/arc_bench/baseline/interventions/T09.json` (config)
- `experiments/arc_bench/baseline/interventions/T10.json` (config)
- `experiments/arc_bench/baseline/interventions/T11.json` (config)
- `experiments/arc_bench/baseline/interventions/T12.json` (config)
- `experiments/arc_bench/baseline/interventions/T13.json` (config)
- `experiments/arc_bench/baseline/interventions/T14.json` (config)
- `experiments/arc_bench/baseline/interventions/T15.json` (config)
- `experiments/arc_bench/baseline/interventions/T16.json` (config)
- `experiments/arc_bench/baseline/interventions/T17.json` (config)
- `experiments/arc_bench/baseline/interventions/T18.json` (config)
- `experiments/arc_bench/baseline/interventions/T19.json` (config)
- `experiments/arc_bench/baseline/interventions/T20.json` (config)
- `experiments/arc_bench/baseline/interventions/T21.json` (config)
- `experiments/arc_bench/baseline/interventions/T22.json` (config)
- `experiments/arc_bench/baseline/interventions/T23.json` (config)
- `experiments/arc_bench/baseline/interventions/T24.json` (config)
- `experiments/arc_bench/baseline/interventions/T25.json` (config)
- `experiments/arc_bench/config/_meta_paper_quality.json` (config)
- `experiments/arc_bench/config/base_config.yaml` (config)
- `experiments/arc_bench/config/biology/manifests/B01.yaml` (config)
- `experiments/arc_bench/config/biology/manifests/B02.yaml` (config)
- `experiments/arc_bench/config/biology/manifests/B03.yaml` (config)
- `experiments/arc_bench/config/biology/manifests/B04.yaml` (config)
- `experiments/arc_bench/config/biology/manifests/B05.yaml` (config)
- `experiments/arc_bench/config/biology/manifests/B06.yaml` (config)
- `experiments/arc_bench/config/biology/manifests/B07.yaml` (config)
- `experiments/arc_bench/config/biology/rubrics/B01.json` (config)
- `experiments/arc_bench/config/biology/rubrics/B02.json` (config)
- `experiments/arc_bench/config/biology/rubrics/B03.json` (config)
- `experiments/arc_bench/config/biology/rubrics/B04.json` (config)
- `experiments/arc_bench/config/biology/rubrics/B05.json` (config)
- `experiments/arc_bench/config/biology/rubrics/B06.json` (config)
- `experiments/arc_bench/config/biology/rubrics/B07.json` (config)
- `experiments/arc_bench/config/biology/topics.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML01.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML02.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML03.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML04.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML05.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML06.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML07.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML08.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML09.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML10.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML11.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML12.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML13.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML14.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML15.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML16.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML17.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML18.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML19.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML20.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML21.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML22.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML23.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML24.yaml` (config)
- `experiments/arc_bench/config/ml/manifests/ML25.yaml` (config)
- `experiments/arc_bench/config/ml/rubrics/ML01.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML02.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML03.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML04.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML05.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML06.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML07.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML08.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML09.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML10.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML11.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML12.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML13.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML14.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML15.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML16.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML17.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML18.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML19.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML20.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML21.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML22.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML23.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML24.json` (config)
- `experiments/arc_bench/config/ml/rubrics/ML25.json` (config)
- `experiments/arc_bench/config/ml/topics.yaml` (config)
- `experiments/arc_bench/config/physics/manifests/P01.yaml` (config)
- `experiments/arc_bench/config/physics/manifests/P02.yaml` (config)
- `experiments/arc_bench/config/physics/manifests/P03.yaml` (config)
- `experiments/arc_bench/config/physics/manifests/P04.yaml` (config)
- `experiments/arc_bench/config/physics/manifests/P05.yaml` (config)
- `experiments/arc_bench/config/physics/manifests/P06.yaml` (config)
- `experiments/arc_bench/config/physics/manifests/P07.yaml` (config)
- `experiments/arc_bench/config/physics/manifests/P08.yaml` (config)
- `experiments/arc_bench/config/physics/manifests/P09.yaml` (config)
- `experiments/arc_bench/config/physics/manifests/P10.yaml` (config)
- `experiments/arc_bench/config/physics/rubrics/P01.json` (config)
- `experiments/arc_bench/config/physics/rubrics/P02.json` (config)
- `experiments/arc_bench/config/physics/rubrics/P03.json` (config)
- `experiments/arc_bench/config/physics/rubrics/P04.json` (config)
- `experiments/arc_bench/config/physics/rubrics/P05.json` (config)
- `experiments/arc_bench/config/physics/rubrics/P06.json` (config)
- `experiments/arc_bench/config/physics/rubrics/P07.json` (config)
- `experiments/arc_bench/config/physics/rubrics/P08.json` (config)
- `experiments/arc_bench/config/physics/rubrics/P09.json` (config)
- `experiments/arc_bench/config/physics/rubrics/P10.json` (config)
- `experiments/arc_bench/config/physics/topics.yaml` (config)
- `experiments/arc_bench/config/quantum/manifests/Q01.yaml` (config)
- `experiments/arc_bench/config/quantum/manifests/Q02.yaml` (config)
- `experiments/arc_bench/config/quantum/manifests/Q03.yaml` (config)
- `experiments/arc_bench/config/quantum/manifests/Q04.yaml` (config)
- `experiments/arc_bench/config/quantum/manifests/Q05.yaml` (config)
- `experiments/arc_bench/config/quantum/manifests/Q06.yaml` (config)
- `experiments/arc_bench/config/quantum/manifests/Q07.yaml` (config)
- `experiments/arc_bench/config/quantum/manifests/Q08.yaml` (config)
- `experiments/arc_bench/config/quantum/manifests/Q09.yaml` (config)
- `experiments/arc_bench/config/quantum/manifests/Q10.yaml` (config)
- `experiments/arc_bench/config/quantum/rubrics/Q01.json` (config)
- `experiments/arc_bench/config/quantum/rubrics/Q02.json` (config)
- `experiments/arc_bench/config/quantum/rubrics/Q03.json` (config)
- `experiments/arc_bench/config/quantum/rubrics/Q04.json` (config)
- `experiments/arc_bench/config/quantum/rubrics/Q05.json` (config)
- `experiments/arc_bench/config/quantum/rubrics/Q06.json` (config)
- `experiments/arc_bench/config/quantum/rubrics/Q07.json` (config)
- `experiments/arc_bench/config/quantum/rubrics/Q08.json` (config)
- `experiments/arc_bench/config/quantum/rubrics/Q09.json` (config)
- `experiments/arc_bench/config/quantum/rubrics/Q10.json` (config)
- `experiments/arc_bench/config/quantum/topics.yaml` (config)
- `experiments/arc_bench/config/statistics/manifests/S01.yaml` (config)
- `experiments/arc_bench/config/statistics/manifests/S02.yaml` (config)
- `experiments/arc_bench/config/statistics/manifests/S03.yaml` (config)
- `experiments/arc_bench/config/statistics/rubrics/S01.json` (config)
- `experiments/arc_bench/config/statistics/rubrics/S02.json` (config)
- `experiments/arc_bench/config/statistics/rubrics/S03.json` (config)
- `experiments/arc_bench/config/statistics/topics.yaml` (config)
- `frontend-legacy/package.json` (manifest)
- `prompts.default.yaml` (config)
- `pyproject.toml` (manifest)
- `researchclaw/calendar/data/conferences.yaml` (config)
- `researchclaw/data/benchmark_knowledge.yaml` (config)
- `researchclaw/data/dataset_registry.yaml` (config)
- `researchclaw/data/docker_profiles.yaml` (config)
- `researchclaw/data/seminal_papers.yaml` (config)
- `researchclaw/docker/Dockerfile` (container)
- `researchclaw/docker/Dockerfile.biology` (container)
- `researchclaw/docker/Dockerfile.chemistry` (container)
- `researchclaw/docker/Dockerfile.economics` (container)
- `researchclaw/docker/Dockerfile.generic` (container)
- `researchclaw/docker/Dockerfile.math` (container)
- `researchclaw/docker/Dockerfile.physics` (container)
- `researchclaw/domains/profiles/_generic.yaml` (config)
- `researchclaw/domains/profiles/biology_genomics.yaml` (config)
- `researchclaw/domains/profiles/biology_metabolic.yaml` (config)
- `researchclaw/domains/profiles/biology_protein.yaml` (config)
- `researchclaw/domains/profiles/biology_singlecell.yaml` (config)
- `researchclaw/domains/profiles/chemistry_molprop.yaml` (config)
- `researchclaw/domains/profiles/chemistry_qm.yaml` (config)
- `researchclaw/domains/profiles/clinical_sleep.yaml` (config)
- `researchclaw/domains/profiles/economics_empirical.yaml` (config)
- `researchclaw/domains/profiles/hep_ph.yaml` (config)
- `researchclaw/domains/profiles/mathematics_numerical.yaml` (config)
- `researchclaw/domains/profiles/mathematics_optimization.yaml` (config)
- `researchclaw/domains/profiles/medical_observational.yaml` (config)
- `researchclaw/domains/profiles/ml_compression.yaml` (config)
- `researchclaw/domains/profiles/ml_generative.yaml` (config)
- `researchclaw/domains/profiles/ml_generic.yaml` (config)
- `researchclaw/domains/profiles/ml_graph.yaml` (config)
- `researchclaw/domains/profiles/ml_nlp.yaml` (config)
- `researchclaw/domains/profiles/ml_rl.yaml` (config)
- `researchclaw/domains/profiles/ml_tabular.yaml` (config)
- `researchclaw/domains/profiles/ml_vision.yaml` (config)
- `researchclaw/domains/profiles/neuroscience_computational.yaml` (config)
- `researchclaw/domains/profiles/neuroscience_imaging.yaml` (config)
- `researchclaw/domains/profiles/physics_pde.yaml` (config)
- `researchclaw/domains/profiles/physics_quantum.yaml` (config)
- `researchclaw/domains/profiles/physics_simulation.yaml` (config)
- `researchclaw/domains/profiles/robotics_control.yaml` (config)
- `researchclaw/domains/profiles/security_detection.yaml` (config)
- `researchclaw/domains/profiles/statistics_general.yaml` (config)

## Top-level layout

- `researchclaw` — 354 analysed file(s)
- `experiments` — 176 analysed file(s)
- `tests` — 101 analysed file(s)
- `external` — 31 analysed file(s)
- `docs` — 20 analysed file(s)
- `frontend-legacy` — 13 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.claude` — 9 analysed file(s)
- `scripts` — 6 analysed file(s)
- `website` — 6 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `be4ba4755bf1b52220f25e13b2293b5956590070` is the revision these paths and observations refer to.
