# Project structure: LAION-AI/Open-Assistant

**Analysed commit:** `f1e6ed9526f5817531f3ab85441a40b3671ddccb`

**Commit reference:** [f1e6ed9526f5817531f3ab85441a40b3671ddccb](https://github.com/LAION-AI/Open-Assistant/commit/f1e6ed9526f5817531f3ab85441a40b3671ddccb)

**Tree at this commit:** [LAION-AI/Open-Assistant@f1e6ed9526f5](https://github.com/LAION-AI/Open-Assistant/tree/f1e6ed9526f5817531f3ab85441a40b3671ddccb)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | LAION-AI/Open-Assistant |
| Description | OpenAssistant is a chat-based assistant that understands tasks, can interact with third-party systems, and retrieve information dynamically to do so. |
| Stars | 37351 |
| Forks | 3257 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `f1e6ed9526f5817531f3ab85441a40b3671ddccb` |
| Retrieved at | 2026-11-14T19:06:48.530013+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.devcontainer/  (7 files)
  backend-dev/  (2 files)
    devcontainer.json
    post_create_command.sh
  frontend-dev/  (2 files)
    devcontainer.json
    post_create_command.sh
  README.md
  devcontainer.json
  post_create_command.sh
.github/  (12 files)
  workflows/  (11 files)
    build-frontend.yaml
    build-postgres.yaml
    deploy-docs-site.yaml
    deploy-to-node.yaml
    docker-build.yaml
    pre-commit.yaml
    production-deploy.yaml
    production2-deploy.yaml
    release.yaml
    test-api-contract.yaml
    test-e2e.yaml
  dependabot.yml
.vscode/  (3 files)
  extensions.json
  launch.json
  settings.json
ansible/  (10 files)
  inference/  (4 files)
    deploy-server.yaml
    deploy-worker.yaml
    redis.conf
    test.inventory.ini
  .gitignore
  README.md
  deploy-to-node.yaml
  pgbackrest.conf
  redis.conf
  test.inventory.ini
assets/  (3 files)
  logo.svg
  logo_mono.svg
  open assistant hexagon sticker EN.svg
backend/  (134 files)
  alembic/  (52 files)
    versions/  (49 files)
      … 49 files under this directory
    README
    env.py
    script.py.mako
  oasst_backend/  (65 files)
    api/  (18 files)
      … 18 files under this directory
    models/  (19 files)
      … 19 files under this directory
    schemas/  (4 files)
      … 4 files under this directory
    utils/  (11 files)
      … 11 files under this directory
    __init__.py
    auth.py
    cached_stats_repository.py
    celery_worker.py
    config.py
    database.py
    journal_writer.py
    prompt_repository.py
    scheduled_tasks.py
    task_repository.py
    tree_manager.py
    user_repository.py
    user_stats_repository.py
  test_data/  (2 files)
    generic/  (1 files)
      … 1 files under this directory
    realistic/  (1 files)
      … 1 files under this directory
  tests/  (3 files)
    __init__.py
    test_settings.py
    test_tree_manager_config.py
  .env.example
  .gitignore
  README.md
  alembic.ini
  export.py
  import.py
  main.py
  requirements.txt
  requirements_worker.txt
  rerank.py
  sql_snippets.md
  update_message_attributes.py
copilot/  (5 files)
  api/  (1 files)
    manifest.yml
  environments/  (1 files)
    staging/  (1 files)
      … 1 files under this directory
  web/  (1 files)
    manifest.yml
  .workspace
  README.md
data/  (116 files)
  datasets/  (114 files)
    TSSB-3M/  (4 files)
      … 4 files under this directory
    bart_searchgpt_wiki_nlp_augment/  (8 files)
      … 8 files under this directory
    biostars_qa/  (3 files)
      … 3 files under this directory
    cmu_wiki_qa/  (3 files)
      … 3 files under this directory
    cocktail_recipes/  (1 files)
      … 1 files under this directory
    codet_humaneval_mbpp/  (3 files)
      … 3 files under this directory
    fa-isna-news/  (1 files)
      … 1 files under this directory
    fa-wikipedia/  (1 files)
      … 1 files under this directory
    fd_dialogue/  (1 files)
      … 1 files under this directory
    grade_school_math_instructions/  (1 files)
      … 1 files under this directory
    gutenberg/  (3 files)
      … 3 files under this directory
    iapp_wiki_qa_squad/  (4 files)
      … 4 files under this directory
    instructional_codesearchnet_python/  (3 files)
      … 3 files under this directory
    logicreference_OA/  (3 files)
      … 3 files under this directory
    mt_note_generation/  (5 files)
      … 5 files under this directory
    nsfw_selfharm_reddit/  (7 files)
      … 7 files under this directory
    oa_dolly_15k/  (2 files)
      … 2 files under this directory
    oa_leet10k/  (2 files)
      … 2 files under this directory
    oa_stackexchange/  (7 files)
      … 7 files under this directory
    poetry_instruction/  (3 files)
      … 3 files under this directory
    prosocial_confessions/  (2 files)
      … 2 files under this directory
    reasoning_bg_oa/  (2 files)
      … 2 files under this directory
    reasoning_gsm_qna_oa/  (2 files)
      … 2 files under this directory
    recipes/  (2 files)
      … 2 files under this directory
    safety_directory/  (4 files)
      … 4 files under this directory
    semantics_ws_qna_oa/  (3 files)
      … 3 files under this directory
    soda_synthetic_dialogue/  (5 files)
      … 5 files under this directory
    tatoeba_mt_qna_oa/  (5 files)
      … 5 files under this directory
    tell_a_joke/  (1 files)
      … 1 files under this directory
    tlcv2.0_oa/  (2 files)
      … 2 files under this directory
    tv_dialogue/  (3 files)
      … 3 files under this directory
    ubuntu_dialogue_qa/  (3 files)
      … 3 files under this directory
    youtube_subs_howto100M/  (5 files)
      … 5 files under this directory
    zhihu-kol/  (8 files)
      … 8 files under this directory
    README.md
    __init__.py
  __init__.py
  dev-requirements.txt
deploy/  (13 files)
  dev-node/  (4 files)
    nginx/  (4 files)
      … 4 files under this directory
  prod-node/  (4 files)
    nginx/  (4 files)
      … 4 files under this directory
  prod2-node/  (4 files)
    nginx/  (4 files)
      … 4 files under this directory
  README.md
discord-bots/  (75 files)
  oa-bot-js/  (38 files)
    src/  (32 files)
      … 32 files under this directory
    .env.sample
    .gitignore
    README.md
    docker-compose.yml
    package.json
    tsconfig.json
  oa-bot-py/  (37 files)
    bot/  (15 files)
      … 15 files under this directory
    templates/  (17 files)
      … 17 files under this directory
    .env.example
    .gitignore
    README.md
    message_templates.py
    requirements.txt
docker/  (23 files)
  grafana/  (4 files)
    dashboards/  (2 files)
      … 2 files under this directory
    datasources/  (1 files)
      … 1 files under this directory
    README.md
  inference/  (6 files)
    Dockerfile.safety
    Dockerfile.server
    Dockerfile.worker
    Dockerfile.worker-full
    Dockerfile.worker-hf
    Dockerfile.worker-standalone
  netdata/  (4 files)
    go.d/  (3 files)
      … 3 files under this directory
    README.md
  oasst-postgres/  (2 files)
    Dockerfile
    backup_pg_to_s3.sh
  prometheus/  (2 files)
    README.md
    prometheus.yml
  Dockerfile.backend
  Dockerfile.backend-worker
  Dockerfile.discord-bot
  Dockerfile.model-training
  Dockerfile.website
docs/  (54 files)
  blog/  (9 files)
    2023-02-24-open-assistant-inference-backend-development-hands-on-coding/  (1 files)
      … 1 files under this directory
    2023-04-06-open-assistant-first-models-are-here/  (1 files)
      … 1 files under this directory
    2023-04-10-open-assistant-livestream-just-chatting/  (1 files)
      … 1 files under this directory
    2023-04-15-open-assistant-released/  (1 files)
      … 1 files under this directory
    2023-04-21-open-assistant-storms-youtube/  (1 files)
      … 1 files under this directory
    2023-10-25-open-assistant-is-completed/  (1 files)
      … 1 files under this directory
    2023-02-05-we-need-your-help.mdx
    2023-02-11-architecture.md
    authors.yml
  docs/  (31 files)
    api/  (2 files)
      … 2 files under this directory
    architecture/  (2 files)
      … 2 files under this directory
    data/  (5 files)
      … 5 files under this directory
    guides/  (5 files)
      … 5 files under this directory
    plugins/  (4 files)
      … 4 files under this directory
    presentations/  (1 files)
      … 1 files under this directory
    research/  (4 files)
      … 4 files under this directory
    tasks/  (6 files)
      … 6 files under this directory
    faq.md
    intro.md
  src/  (5 files)
    components/  (2 files)
      … 2 files under this directory
    css/  (1 files)
      … 1 files under this directory
    pages/  (2 files)
      … 2 files under this directory
  static/  (2 files)
    img/  (1 files)
      … 1 files under this directory
    .nojekyll
  .gitignore
  .yarnrc.yml
  README.md
  babel.config.js
  docusaurus.config.js
  package.json
  sidebars.js
inference/  (89 files)
  safety/  (5 files)
    README.md
    main.py
    requirements.txt
    safety_main.sh
    settings.py
  server/  (54 files)
    alembic/  (13 files)
      … 13 files under this directory
    oasst_inference_server/  (35 files)
      … 35 files under this directory
    README.md
    alembic.ini
    export.py
    main.py
    requirements.txt
    server_main.sh
  tests/  (1 files)
    locust/  (1 files)
      … 1 files under this directory
  text-client/  (3 files)
    __main__.py
    requirements.txt
    text_client_utils.py
  worker/  (23 files)
    README.md
    __main__.py
    basic_hf_server.py
    chat_chain.py
    chat_chain_prompts.py
    chat_chain_utils.py
    download_model.py
    download_model_hf.py
    get_model_config_prop.py
    hf_langchain_inference.py
    hf_stopping.py
    hf_streamer.py
    interface.py
    openapi_parser.py
    requirements-hf.txt
    requirements.txt
    run_worker_container.sh
    settings.py
    utils.py
    work.py
    worker_full_main.sh
    worker_hf_main.sh
    worker_standalone_main.sh
  .gitignore
  README.md
  full-dev-setup.sh
model/  (117 files)
  model_eval/  (29 files)
    manual/  (18 files)
      … 18 files under this directory
    sample_results/  (4 files)
      … 4 files under this directory
    README.md
    __init__.py
    eval_datasets.py
    eval_rm.py
    rejection_sampling.py
    sampling_score.py
    utils.py
  model_training/  (77 files)
    configs/  (15 files)
      … 15 files under this directory
    custom_datasets/  (16 files)
      … 16 files under this directory
    models/  (11 files)
      … 11 files under this directory
    tests/  (14 files)
      … 14 files under this directory
    tools/  (6 files)
      … 6 files under this directory
    utils/  (4 files)
      … 4 files under this directory
    .gitignore
    README.md
    __init__.py
    check_dataset_appearances.py
    check_dataset_counts.py
    efficiency_utils.py
    metrics.py
    to_triton.py
    trainer_rl.py
    trainer_rm.py
    trainer_sft.py
  pretokenizer/  (7 files)
    configs/  (1 files)
      … 1 files under this directory
    README.md
    create_hf_tokenizer_config.py
    indexed_dataset.py
    pretokenize.py
    requirements.txt
    tokenizer.py
  .gitignore
  MESSAGE_AND_TOKEN_FORMAT.md
  README.md
  pyproject.toml
notebooks/  (42 files)
  TSSB-3M-bugs-dataset/  (2 files)
    TSSB-3M-bugs_dataset.ipynb
    TSSB-3M-bugs_dataset.md
  closed-book-qa/  (2 files)
    Closed Book QA Generator.ipynb
    README.md
  data-augmentation/  (26 files)
    anthropic/  (3 files)
      … 3 files under this directory
    changemyview-builder/  (2 files)
      … 2 files under this directory
    essay-instructions/  (2 files)
      … 2 files under this directory
    essay-revision/  (2 files)
      … 2 files under this directory
    hippocorpus/  (2 files)
      … 2 files under this directory
    movie-descriptions/  (2 files)
      … 2 files under this directory
    movie-dialogs/  (2 files)
      … 2 files under this directory
    stackexchange-builder/  (2 files)
      … 2 files under this directory
    unified-qa/  (2 files)
      … 2 files under this directory
    wikidata-qa/  (3 files)
      … 3 files under this directory
    writing-prompt/  (3 files)
      … 3 files under this directory
    README.md
  detoxify-evaluation/  (1 files)
    README.md
  diverse/  (2 files)
    README.md
    diverse.ipynb
  example/  (4 files)
    data/  (1 files)
      … 1 files under this directory
    README.md
    example.ipynb
    requirements.txt
  openassistant-oasst1/  (2 files)
    README.md
    getting-started.ipynb
  openbugger/  (2 files)
    README.md
    openbugger_example.ipynb
  README.md
oasst-data/  (12 files)
  examples/  (5 files)
    clean_dataset.py
    filter_messages.py
    filter_trees.py
    split_dataset.py
    tree_to_messages.py
  oasst_data/  (5 files)
    __init__.py
    reader.py
    schemas.py
    traversal.py
    writer.py
  README.md
  pyproject.toml
oasst-shared/  (13 files)
  oasst_shared/  (9 files)
    exceptions/  (2 files)
      … 2 files under this directory
    schemas/  (3 files)
      … 3 files under this directory
    __init__.py
    api_client.py
    model_configs.py
    utils.py
  tests/  (2 files)
    __init__.py
    test_oasst_api_client.py
  README.md
  pyproject.toml
safety/  (1 files)
  README.md
scripts/  (28 files)
  backend-development/  (8 files)
    README.md
    run-local-no-limit.sh
    run-local.sh
    start-docker.sh
    start-mock-server.sh
    start-worker.sh
    stop-mock-server.sh
    stop-worker.sh
  data-collection/  (4 files)
    twitter/  (4 files)
      … 4 files under this directory
  data_augment/  (1 files)
    data_augment.py
  discord/  (2 files)
    stats.py
    verify-lobby.py
  frontend-development/  (4 files)
    README.md
    find-missing-locales.py
    run-bot-local.sh
    run-contract-test.sh
  oasst-shared-development/  (1 files)
    test.sh
  postprocessing/  (7 files)
    importance_selection.py
    infogain_selector.py
    ranking_disagreement.py
    rankings.py
    regex_pii_detector.py
    scoring.py
    task_schedule.py
  xor-codec/  (1 files)
    xor_codec.py
text-frontend/  (3 files)
  __main__.py
  auto_main.py
  requirements.txt
website/  (26 files)
  .storybook/  (3 files)
    decorators.js
    main.js
    preview.js
  cypress/  (14 files)
    components/  (1 files)
      … 1 files under this directory
    contract/  (1 files)
      … 1 files under this directory
    e2e/  (6 files)
      … 6 files under this directory
    fixtures/  (1 files)
      … 1 files under this directory
    support/  (4 files)
      … 4 files under this directory
    README.md
  cypress-visual-screenshots/  (1 files)
    baseline/  (1 files)
      … 1 files under this directory
  .eslintrc.json
  .gitignore
  .nvmrc
  .prettierignore
  .prettierrc.json
  README.md
  cypress.config.contract.js
  cypress.config.js
.dockerignore
.gitattributes
.gitignore
.pre-commit-config.yaml
.python-version
CODEOWNERS
CONTRIBUTING.md
LICENSE
README.md
docker-compose.yaml
inlang.config.js
pyproject.toml
redis.conf
```

## Entry points

- [backend/export.py:452](https://github.com/LAION-AI/Open-Assistant/blob/f1e6ed9526f5817531f3ab85441a40b3671ddccb/backend/export.py#L452)
- [backend/import.py:201](https://github.com/LAION-AI/Open-Assistant/blob/f1e6ed9526f5817531f3ab85441a40b3671ddccb/backend/import.py#L201)
- [backend/main.py:35](https://github.com/LAION-AI/Open-Assistant/blob/f1e6ed9526f5817531f3ab85441a40b3671ddccb/backend/main.py#L35)
- [backend/oasst_backend/cached_stats_repository.py:96](https://github.com/LAION-AI/Open-Assistant/blob/f1e6ed9526f5817531f3ab85441a40b3671ddccb/backend/oasst_backend/cached_stats_repository.py#L96)
- [backend/oasst_backend/celery_worker.py:11](https://github.com/LAION-AI/Open-Assistant/blob/f1e6ed9526f5817531f3ab85441a40b3671ddccb/backend/oasst_backend/celery_worker.py#L11)
- [backend/oasst_backend/tree_manager.py:1798](https://github.com/LAION-AI/Open-Assistant/blob/f1e6ed9526f5817531f3ab85441a40b3671ddccb/backend/oasst_backend/tree_manager.py#L1798)
- [backend/oasst_backend/user_stats_repository.py:649](https://github.com/LAION-AI/Open-Assistant/blob/f1e6ed9526f5817531f3ab85441a40b3671ddccb/backend/oasst_backend/user_stats_repository.py#L649)
- [backend/oasst_backend/utils/language_classification.py:102](https://github.com/LAION-AI/Open-Assistant/blob/f1e6ed9526f5817531f3ab85441a40b3671ddccb/backend/oasst_backend/utils/language_classification.py#L102)
- [backend/oasst_backend/utils/message_tree_topic_modeling.py:83](https://github.com/LAION-AI/Open-Assistant/blob/f1e6ed9526f5817531f3ab85441a40b3671ddccb/backend/oasst_backend/utils/message_tree_topic_modeling.py#L83)
- [backend/oasst_backend/utils/ranking.py:132](https://github.com/LAION-AI/Open-Assistant/blob/f1e6ed9526f5817531f3ab85441a40b3671ddccb/backend/oasst_backend/utils/ranking.py#L132)
- [backend/rerank.py:77](https://github.com/LAION-AI/Open-Assistant/blob/f1e6ed9526f5817531f3ab85441a40b3671ddccb/backend/rerank.py#L77)
- [backend/update_message_attributes.py:90](https://github.com/LAION-AI/Open-Assistant/blob/f1e6ed9526f5817531f3ab85441a40b3671ddccb/backend/update_message_attributes.py#L90)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 27 file(s) under api layer (observed from repository paths and static analysis). Observed routes: POST /api_client, GET /backend_settings/full, GET /backend_settings/public, POST /purge_user/{user_id}, POST /purg… |
| backend package | library | Observed | Groups 66 file(s) under backend package (observed from repository paths and static analysis). Observed top-level classes: CommitMode, HfClassificationModel, HfEmbeddingModel, HfUrl, HuggingFaceAPI, JournalEvent. Observe… |
| Configuration and deployment | config | Observed | Groups 107 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: Settings, TreeManagerConfiguration. Observed top-level functions: split_keys_string. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 67 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Account, ApiClient, AssistantReplyPayload, CachedStats, DataProcess, DbChat. Observed top-level functi… |
| deploy package | library | Observed | Groups 6 file(s) under deploy package (observed from repository paths and static analysis). |
| discord-bots package | library | Observed | Groups 40 file(s) under discord-bots package (observed from repository paths and static analysis). Observed top-level classes: AssistantReplyHandler, InitialPromptHandler, LabelAssistantReplyHandler, LabelModal, LabelPr… |
| docker package | library | Observed | Groups 1 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 86 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Celery, FastAPI, Typer. Observed routes: POST /safety, GET /health, GET /icon… |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: OasstApiClient, TaskType. Observed top-level functions: downgrade, upgrade. |
| inference package | library | Observed | Groups 43 file(s) under inference package (observed from repository paths and static analysis). Observed top-level classes: ChatListRead, ChatRead, ChatRepository, ChatUpdateRequest, CreateAssistantMessageRequest, Creat… |
| model package | library | Observed | Groups 27 file(s) under model package (observed from repository paths and static analysis). Observed top-level classes: AbstractTokenizer, AlpacaBaseDataset, AlpacaGpt4, AnthropicRLHF, AugmentedOA, CrossEntropyLoss. Obs… |
| oasst-data package | library | Observed | Groups 4 file(s) under oasst-data package (observed from repository paths and static analysis). Observed top-level functions: convert_hf_message, default_serializer, open_jsonl_read, open_jsonl_write, read_dataset_messa… |
| oasst-shared package | library | Observed | Groups 8 file(s) under oasst-shared package (observed from repository paths and static analysis). Observed top-level classes: AbstractLabelTask, AbstractRatingTask, Account, AllCachedStatsResponse, Anonymizer, Assistant… |
| scripts package | library | Observed | Groups 14 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: ConversationTree, ConversationTreeNode, PIIDetector, Settings. Observed top-level functions: on_r… |
| Tests | test | Observed | Groups 22 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ChatUser, MockClientSession, ModalView, RatingView, SelectRating, TaskModal. Observed top-level functions:… |
| website package | library | Observed | Groups 16 file(s) under website package (observed from repository paths and static analysis). |

## Important files

- `.devcontainer/backend-dev/devcontainer.json` (config)
- `.devcontainer/devcontainer.json` (config)
- `.devcontainer/frontend-dev/devcontainer.json` (config)
- `.dockerignore` (container)
- `.github/dependabot.yml` (config)
- `.github/workflows/build-frontend.yaml` (ci)
- `.github/workflows/build-postgres.yaml` (ci)
- `.github/workflows/deploy-docs-site.yaml` (ci)
- `.github/workflows/deploy-to-node.yaml` (ci)
- `.github/workflows/docker-build.yaml` (ci)
- `.github/workflows/pre-commit.yaml` (ci)
- `.github/workflows/production-deploy.yaml` (ci)
- `.github/workflows/production2-deploy.yaml` (ci)
- `.github/workflows/release.yaml` (ci)
- `.github/workflows/test-api-contract.yaml` (ci)
- `.github/workflows/test-e2e.yaml` (ci)
- `.pre-commit-config.yaml` (config)
- `.vscode/extensions.json` (config)
- `.vscode/launch.json` (config)
- `.vscode/settings.json` (config)
- `ansible/deploy-to-node.yaml` (config)
- `ansible/inference/deploy-server.yaml` (config)
- `ansible/inference/deploy-worker.yaml` (config)
- `ansible/inference/test.inventory.ini` (config)
- `ansible/test.inventory.ini` (config)
- `backend/.env.example` (config)
- `backend/alembic.ini` (config)
- `backend/requirements.txt` (manifest)
- `backend/requirements_worker.txt` (manifest)
- `backend/test_data/realistic/realistic_seed_data.json` (config)
- `copilot/api/manifest.yml` (config)
- `copilot/environments/staging/manifest.yml` (config)
- `copilot/web/manifest.yml` (config)
- `data/datasets/biostars_qa/requirements.txt` (manifest)
- `data/datasets/cmu_wiki_qa/requirements.txt` (manifest)
- `data/datasets/gutenberg/requirements.txt` (manifest)
- `data/datasets/iapp_wiki_qa_squad/requirements.txt` (manifest)
- `data/datasets/logicreference_OA/requirements.txt` (manifest)
- `data/datasets/poetry_instruction/requirements.txt` (manifest)
- `data/datasets/safety_directory/emergency_infos/wikipedia_emergency_info.json` (config)
- `data/datasets/tv_dialogue/requirements.txt` (manifest)
- `data/datasets/ubuntu_dialogue_qa/requirements.txt` (manifest)
- `data/datasets/youtube_subs_howto100M/requirements.txt` (manifest)
- `data/datasets/zhihu-kol/requirements.txt` (manifest)
- `deploy/dev-node/nginx/docker-compose.yaml` (container)
- `deploy/prod-node/nginx/docker-compose.yaml` (container)
- `deploy/prod2-node/nginx/docker-compose.yaml` (container)
- `discord-bots/oa-bot-js/.env.sample` (config)
- `discord-bots/oa-bot-js/docker-compose.yml` (container)
- `discord-bots/oa-bot-js/package.json` (manifest)
- `discord-bots/oa-bot-js/tsconfig.json` (config)
- `discord-bots/oa-bot-py/.env.example` (config)
- `discord-bots/oa-bot-py/requirements.txt` (manifest)
- `docker-compose.yaml` (container)
- `docker/Dockerfile.backend` (container)
- `docker/Dockerfile.backend-worker` (container)
- `docker/Dockerfile.discord-bot` (container)
- `docker/Dockerfile.model-training` (container)
- `docker/Dockerfile.website` (container)
- `docker/grafana/dashboards/dashboard.yaml` (config)
- `docker/grafana/dashboards/fastapi-backend.json` (config)
- `docker/grafana/datasources/datasource.yml` (config)
- `docker/inference/Dockerfile.safety` (container)
- `docker/inference/Dockerfile.server` (container)
- `docker/inference/Dockerfile.worker` (container)
- `docker/inference/Dockerfile.worker-full` (container)
- `docker/inference/Dockerfile.worker-hf` (container)
- `docker/inference/Dockerfile.worker-standalone` (container)
- `docker/oasst-postgres/Dockerfile` (container)
- `docker/prometheus/prometheus.yml` (config)
- `docs/.yarnrc.yml` (config)
- `docs/blog/authors.yml` (config)
- `docs/docs/api/backend-openapi.json` (config)
- `docs/docs/api/inference-openapi.json` (config)
- `docs/package.json` (manifest)
- `inference/safety/requirements.txt` (manifest)
- `inference/server/alembic.ini` (config)
- `inference/server/oasst_inference_server/plugins/gale_pleaser/ai-plugin.json` (config)
- `inference/server/oasst_inference_server/plugins/gale_roaster/ai-plugin.json` (config)
- `inference/server/oasst_inference_server/plugins/web_retriever/ai-plugin.json` (config)
- `inference/server/requirements.txt` (manifest)
- `inference/text-client/requirements.txt` (manifest)
- `inference/worker/requirements-hf.txt` (manifest)
- `inference/worker/requirements.txt` (manifest)
- `model/model_eval/manual/config/default.json` (config)
- `model/model_eval/manual/config/default_rallio.json` (config)
- `model/model_eval/manual/config/noprefix.json` (config)
- `model/model_eval/manual/config/noprefix2.json` (config)
- `model/model_eval/manual/config/noprefix2_profile.json` (config)
- `model/model_eval/manual/config/synth.json` (config)
- `model/model_eval/manual/config/synth2.json` (config)
- `model/model_eval/manual/config/synth2_gale_prefix.json` (config)
- `model/model_eval/manual/config/synth2_rallio_original.json` (config)
- `model/model_eval/manual/config/synth_rallio.json` (config)
- `model/model_eval/manual/config/system_profile.json` (config)
- `model/model_eval/manual/config/system_profile2.json` (config)
- `model/model_eval/manual/requirements.txt` (manifest)
- `model/model_eval/sample_results/comparison.json` (config)
- `model/model_eval/sample_results/rejected_samples.json` (config)
- `model/model_eval/sample_results/selected_samples.json` (config)
- `model/model_eval/sample_results/theblackcat102-pythia-12b-deduped-sft.json` (config)
- `model/model_training/configs/accelerate_config.yaml` (config)
- `model/model_training/configs/config.yaml` (config)
- `model/model_training/configs/config_rl.yaml` (config)
- `model/model_training/configs/config_rm.yaml` (config)
- `model/model_training/configs/deepspeed_rl.json` (config)
- `model/model_training/configs/deepspeed_rl_zero3.json` (config)
- `model/model_training/configs/ppo_config.yaml` (config)
- `model/model_training/configs/zero3_config_falcon.json` (config)
- `model/model_training/configs/zero3_config_pretrain.json` (config)
- `model/model_training/configs/zero3_config_sft.json` (config)
- `model/model_training/configs/zero_config.json` (config)
- `model/model_training/configs/zero_config_pretrain.json` (config)
- `model/model_training/configs/zero_config_sft_65b.json` (config)
- `model/pretokenizer/configs/pretokenize.yaml` (config)
- `model/pretokenizer/requirements.txt` (manifest)
- `model/pyproject.toml` (manifest)
- `notebooks/data-augmentation/wikidata-qa/requirements.txt` (manifest)
- `notebooks/example/requirements.txt` (manifest)
- `oasst-data/pyproject.toml` (manifest)
- `oasst-shared/pyproject.toml` (manifest)
- `pyproject.toml` (manifest)
- `scripts/data-collection/twitter/requirements.txt` (manifest)
- `text-frontend/requirements.txt` (manifest)
- `website/.eslintrc.json` (config)
- `website/.prettierrc.json` (config)
- `website/cypress/fixtures/example.json` (config)

## Top-level layout

- `backend` — 134 analysed file(s)
- `model` — 117 analysed file(s)
- `data` — 116 analysed file(s)
- `inference` — 89 analysed file(s)
- `discord-bots` — 75 analysed file(s)
- `docs` — 54 analysed file(s)
- `notebooks` — 42 analysed file(s)
- `scripts` — 28 analysed file(s)
- `website` — 26 analysed file(s)
- `docker` — 23 analysed file(s)
- `(root files)` — 13 analysed file(s)
- `deploy` — 13 analysed file(s)
- `oasst-shared` — 13 analysed file(s)
- `.github` — 12 analysed file(s)
- `oasst-data` — 12 analysed file(s)
- `ansible` — 10 analysed file(s)
- `.devcontainer` — 7 analysed file(s)
- `copilot` — 5 analysed file(s)
- `.vscode` — 3 analysed file(s)
- `assets` — 3 analysed file(s)
- `text-frontend` — 3 analysed file(s)
- `safety` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `f1e6ed9526f5817531f3ab85441a40b3671ddccb` is the revision these paths and observations refer to.
