# Project structure: tensorflow/tensor2tensor

**Analysed commit:** `bafdc1b67730430d38d6ab802cbd51f9d053ba2e`

**Commit reference:** [bafdc1b67730430d38d6ab802cbd51f9d053ba2e](https://github.com/tensorflow/tensor2tensor/commit/bafdc1b67730430d38d6ab802cbd51f9d053ba2e)

**Tree at this commit:** [tensorflow/tensor2tensor@bafdc1b67730](https://github.com/tensorflow/tensor2tensor/tree/bafdc1b67730430d38d6ab802cbd51f9d053ba2e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | tensorflow/tensor2tensor |
| Description | Library of deep learning models and datasets designed to make deep learning more accessible and accelerate ML research. |
| Stars | 17471 |
| Forks | 3829 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `bafdc1b67730430d38d6ab802cbd51f9d053ba2e` |
| Retrieved at | 2026-11-14T19:08:31.531398+00:00 |
| Files in this snapshot | 545 |

## Directory tree

```text
docs/  (10 files)
  tutorials/  (1 files)
    asr_with_transformer.md
  cloud_mlengine.md
  cloud_tpu.md
  distributed_training.md
  index.md
  multi_problem.md
  new_model.md
  new_problem.md
  overview.md
  walkthrough.md
oss_scripts/  (4 files)
  oss_integration_test.sh
  oss_pip_install.sh
  oss_release.sh
  oss_tests.sh
tensor2tensor/  (520 files)
  bin/  (25 files)
    __init__.py
    build_vocab.py
    make_tf_configs.py
    t2t-avg-all
    t2t-bleu
    t2t-datagen
    t2t-decoder
    t2t-eval
    t2t-exporter
    t2t-insights-server
    t2t-make-tf-configs
    t2t-query-server
    t2t-trainer
    t2t-translate-all
    t2t_attack.py
    t2t_avg_all.py
    t2t_bleu.py
    t2t_datagen.py
    t2t_decoder.py
    t2t_distill.py
    t2t_eval.py
    t2t_prune.py
    t2t_trainer.py
    t2t_trainer_test.py
    … 1 more files
  data_generators/  (164 files)
    ops/  (8 files)
      … 8 files under this directory
    test_data/  (5 files)
      … 5 files under this directory
    wikifact/  (1 files)
      … 1 files under this directory
    wikisum/  (16 files)
      … 16 files under this directory
    README.md
    __init__.py
    algorithmic.py
    algorithmic_math.py
    algorithmic_math_deepmind.py
    algorithmic_math_test.py
    algorithmic_math_two_variables.py
    algorithmic_test.py
    all_problems.py
    allen_brain.py
    allen_brain_test.py
    audio.py
    audio_encoder.py
    audio_test.py
    babi_qa.py
    bair_robot_pushing.py
    celeba.py
    celeba_test.py
    celebahq.py
    cifar.py
    cipher.py
    cleaner_en_xx.py
    cnn_dailymail.py
    cola.py
    … 110 more files
  envs/  (20 files)
    __init__.py
    env_problem.py
    env_problem_utils.py
    env_problem_utils_test.py
    gym_env_problem.py
    gym_env_problem_test.py
    gym_spaces_utils.py
    gym_spaces_utils_test.py
    mujoco_problems.py
    mujoco_problems_test.py
    rendered_env_problem.py
    rendered_env_problem_test.py
    tic_tac_toe_env.py
    tic_tac_toe_env_problem.py
    tic_tac_toe_env_problem_test.py
    tic_tac_toe_env_test.py
    time_step.py
    time_step_test.py
    trajectory.py
    trajectory_test.py
  insights/  (30 files)
    polymer/  (23 files)
      … 23 files under this directory
    README.md
    __init__.py
    graph.py
    insight_configuration.proto
    query_processor.py
    server.py
    transformer_model.py
  layers/  (30 files)
    __init__.py
    area_attention.py
    area_attention_test.py
    common_attention_test.py
    common_audio.py
    common_hparams.py
    common_image_attention.py
    common_image_attention_test.py
    common_layers.py
    common_layers_test.py
    common_video.py
    common_video_test.py
    discretization.py
    discretization_test.py
    latent_layers.py
    latent_layers_test.py
    message_passing_attention.py
    modalities.py
    modalities_test.py
    ngram.py
    ngram_test.py
    transformer_glow_layers.py
    transformer_glow_layers_ops.py
    transformer_glow_layers_ops_test.py
    … 6 more files
  metrics/  (3 files)
    __init__.py
    video_conditional_fvd.py
    video_conditional_fvd_test.py
  models/  (118 files)
    neural_architecture_search/  (6 files)
      … 6 files under this directory
    research/  (47 files)
      … 47 files under this directory
    video/  (28 files)
      … 28 files under this directory
    README.md
    __init__.py
    basic.py
    basic_test.py
    bytenet.py
    bytenet_test.py
    distillation.py
    evolved_transformer.py
    evolved_transformer_test.py
    image_transformer.py
    image_transformer_2d.py
    image_transformer_2d_test.py
    image_transformer_test.py
    lstm.py
    lstm_test.py
    mtf_image_transformer.py
    mtf_image_transformer_test.py
    mtf_resnet.py
    mtf_transformer.py
    mtf_transformer2.py
    mtf_transformer_test.py
    neural_assistant.py
    neural_gpu.py
    neural_gpu_test.py
    … 13 more files
  notebooks/  (3 files)
    Transformer_translate.ipynb
    asr_transformer.ipynb
    t2t_problem.ipynb
  rl/  (34 files)
    envs/  (6 files)
      … 6 files under this directory
    README.md
    __init__.py
    batch_dqn_agent_test.py
    batch_runner_test.py
    datagen_with_agent.py
    dopamine_connector.py
    evaluator.py
    evaluator_test.py
    gym_utils.py
    gym_utils_test.py
    player.py
    player_utils.py
    policy_learner.py
    ppo.py
    ppo_learner.py
    restarter.py
    restarter_test.py
    rl_utils.py
    trainer_model_based.py
    trainer_model_based_agent_only.py
    trainer_model_based_params.py
    trainer_model_based_recurrent_test.py
    trainer_model_based_stochastic_test.py
    trainer_model_based_sv2p_test.py
    … 4 more files
  serving/  (5 files)
    README.md
    __init__.py
    export.py
    query.py
    serving_utils.py
  test_data/  (7 files)
    example_usr_dir/  (3 files)
      … 3 files under this directory
    transformer_test_ckpt/  (3 files)
      … 3 files under this directory
    vocab.translate_ende_wmt8k.8192.subwords
  utils/  (71 files)
    video/  (2 files)
      … 2 files under this directory
    __init__.py
    adafactor.py
    adafactor_test.py
    adv_attack_utils.py
    avg_checkpoints.py
    beam_search.py
    beam_search_test.py
    bleu_hook.py
    bleu_hook_test.py
    checkpoint_compatibility_test.py
    cloud_mlengine.py
    compute_video_metrics.py
    contrib.py
    data_reader.py
    data_reader_test.py
    decoding.py
    devices.py
    diet.py
    diet_test.py
    expert_utils.py
    expert_utils_test.py
    flags.py
    get_cnndm_rouge.sh
    get_ende_bleu.sh
    … 45 more files
  visualization/  (6 files)
    TransformerVisualization.ipynb
    __init__.py
    attention.js
    attention.py
    visualization.py
    visualization_test.py
  __init__.py
  problems.py
  problems_colab.py
  problems_test.py
.gitignore
.travis.yml
AUTHORS
CONTRIBUTING.md
ISSUE_TEMPLATE.md
LICENSE
README.md
floyd.yml
floyd_requirements.txt
pylintrc
setup.py
```

## Entry points

- [tensor2tensor/bin/build_vocab.py:70](https://github.com/tensorflow/tensor2tensor/blob/bafdc1b67730430d38d6ab802cbd51f9d053ba2e/tensor2tensor/bin/build_vocab.py#L70)
- [tensor2tensor/bin/make_tf_configs.py:109](https://github.com/tensorflow/tensor2tensor/blob/bafdc1b67730430d38d6ab802cbd51f9d053ba2e/tensor2tensor/bin/make_tf_configs.py#L109)
- [tensor2tensor/bin/t2t_attack.py:279](https://github.com/tensorflow/tensor2tensor/blob/bafdc1b67730430d38d6ab802cbd51f9d053ba2e/tensor2tensor/bin/t2t_attack.py#L279)
- [tensor2tensor/bin/t2t_avg_all.py:113](https://github.com/tensorflow/tensor2tensor/blob/bafdc1b67730430d38d6ab802cbd51f9d053ba2e/tensor2tensor/bin/t2t_avg_all.py#L113)
- [tensor2tensor/bin/t2t_bleu.py:173](https://github.com/tensorflow/tensor2tensor/blob/bafdc1b67730430d38d6ab802cbd51f9d053ba2e/tensor2tensor/bin/t2t_bleu.py#L173)
- [tensor2tensor/bin/t2t_datagen.py:304](https://github.com/tensorflow/tensor2tensor/blob/bafdc1b67730430d38d6ab802cbd51f9d053ba2e/tensor2tensor/bin/t2t_datagen.py#L304)
- [tensor2tensor/bin/t2t_decoder.py:213](https://github.com/tensorflow/tensor2tensor/blob/bafdc1b67730430d38d6ab802cbd51f9d053ba2e/tensor2tensor/bin/t2t_decoder.py#L213)
- [tensor2tensor/bin/t2t_distill.py:187](https://github.com/tensorflow/tensor2tensor/blob/bafdc1b67730430d38d6ab802cbd51f9d053ba2e/tensor2tensor/bin/t2t_distill.py#L187)
- [tensor2tensor/bin/t2t_eval.py:63](https://github.com/tensorflow/tensor2tensor/blob/bafdc1b67730430d38d6ab802cbd51f9d053ba2e/tensor2tensor/bin/t2t_eval.py#L63)
- [tensor2tensor/bin/t2t_prune.py:117](https://github.com/tensorflow/tensor2tensor/blob/bafdc1b67730430d38d6ab802cbd51f9d053ba2e/tensor2tensor/bin/t2t_prune.py#L117)
- [tensor2tensor/bin/t2t_trainer.py:425](https://github.com/tensorflow/tensor2tensor/blob/bafdc1b67730430d38d6ab802cbd51f9d053ba2e/tensor2tensor/bin/t2t_trainer.py#L425)
- [tensor2tensor/bin/t2t_trainer_test.py:46](https://github.com/tensorflow/tensor2tensor/blob/bafdc1b67730430d38d6ab802cbd51f9d053ba2e/tensor2tensor/bin/t2t_trainer_test.py#L46)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 5 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 78 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AbstractGAN, AddCombiner, Aligned, AttendToEncoderLayerBase, AttendToEncoderTopDownLayer, AttentionLM.… |
| Application entry point | entrypoint | Observed | Groups 38 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed top-level classes: DebugFrontendApplication, NextFrameGlowTes… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| oss_scripts package | library | Observed | Groups 4 file(s) under oss_scripts package (observed from repository paths and static analysis). |
| tensor2tensor package | library | Observed | Groups 223 file(s) under tensor2tensor package (observed from repository paths and static analysis). Observed top-level classes: ActionDiscretizeWrapper, AdafactorOptimizer, AlgorithmicAdditionBinary40, AlgorithmicAddit… |
| Tests | test | Observed | Groups 127 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH tensor2tensor.data_generators.paraphrase_ms_coco.ParaphraseGenerationProblem.prepare_data, PATCH tensor2tensor.… |

## Important files

- `.travis.yml` (ci)
- `floyd.yml` (config)
- `setup.py` (manifest)
- `tensor2tensor/insights/polymer/bower.json` (config)
- `tensor2tensor/test_data/example_usr_dir/requirements.txt` (manifest)
- `tensor2tensor/test_data/transformer_test_ckpt/hparams.json` (config)

## Top-level layout

- `tensor2tensor` — 520 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `docs` — 10 analysed file(s)
- `oss_scripts` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `bafdc1b67730430d38d6ab802cbd51f9d053ba2e` is the revision these paths and observations refer to.
