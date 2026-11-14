# Project structure: facebookresearch/fairseq

**Analysed commit:** `3d262bb25690e4eb2e7d3c1309b1e9c406ca4b99`

**Commit reference:** [3d262bb25690e4eb2e7d3c1309b1e9c406ca4b99](https://github.com/facebookresearch/fairseq/commit/3d262bb25690e4eb2e7d3c1309b1e9c406ca4b99)

**Tree at this commit:** [facebookresearch/fairseq@3d262bb25690](https://github.com/facebookresearch/fairseq/tree/3d262bb25690e4eb2e7d3c1309b1e9c406ca4b99)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | facebookresearch/fairseq |
| Description | Facebook AI Research Sequence-to-Sequence Toolkit written in Python. |
| Stars | 32206 |
| Forks | 6665 |
| Licence | MIT |
| Language | Python |
| Default branch | main |
| Analysed commit | `3d262bb25690e4eb2e7d3c1309b1e9c406ca4b99` |
| Retrieved at | 2026-11-14T19:07:06.990677+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (11 files)
  ISSUE_TEMPLATE/  (4 files)
    bug_report.md
    documentation.md
    feature_request.md
    how-to-question.md
  workflows/  (3 files)
    build.yml
    depreview.yml
    release.yml
  CODEOWNERS
  ISSUE_TEMPLATE.md
  PULL_REQUEST_TEMPLATE.md
  stale.yml
docs/  (18 files)
  Makefile
  command_line_tools.rst
  conf.py
  criterions.rst
  data.rst
  docutils.conf
  getting_started.rst
  hydra_integration.md
  index.rst
  lr_scheduler.rst
  make.bat
  models.rst
  modules.rst
  optim.rst
  overview.rst
  tasks.rst
  tutorial_classifying_names.rst
  tutorial_simple_lstm.rst
examples/  (762 files)
  MMPT/  (126 files)
    mmpt/  (37 files)
      … 37 files under this directory
    mmpt_cli/  (2 files)
      … 2 files under this directory
    projects/  (69 files)
      … 69 files under this directory
    scripts/  (10 files)
      … 10 files under this directory
    .gitignore
    CONFIG.md
    DATASET.md
    README.md
    endtask.md
    locallaunch.py
    pretraining.md
    setup.py
  adaptive_span/  (7 files)
    README.md
    __init__.py
    adagrad_with_grad_clip.py
    adaptive_span_attention.py
    adaptive_span_loss.py
    adaptive_span_model.py
    adaptive_span_model_wrapper.py
  attention_head_selection/  (15 files)
    src/  (14 files)
      … 14 files under this directory
    README.md
  audio_nlp/  (4 files)
    nlu/  (4 files)
      … 4 files under this directory
  backtranslation/  (7 files)
    README.md
    deduplicate_lines.py
    extract_bt_data.py
    prepare-de-monolingual.sh
    prepare-wmt18en2de.sh
    sacrebleu.sh
    tokenized_bleu.sh
  bart/  (4 files)
    README.glue.md
    README.md
    README.summarization.md
    summarize.py
  byte_level_bpe/  (4 files)
    README.md
    get_bitext.py
    get_data.sh
    gru_transformer.py
  camembert/  (1 files)
    README.md
  constrained_decoding/  (3 files)
    README.md
    normalize.py
    tok.py
  conv_seq2seq/  (1 files)
    README.md
  criss/  (9 files)
    mining/  (2 files)
      … 2 files under this directory
    sentence_retrieval/  (2 files)
      … 2 files under this directory
    unsupervised_mt/  (1 files)
      … 1 files under this directory
    README.md
    download_and_preprocess_flores_test.sh
    download_and_preprocess_tatoeba.sh
    save_encoder.py
  cross_lingual_language_model/  (1 files)
    README.md
  data2vec/  (138 files)
    config/  (81 files)
      … 81 files under this directory
    data/  (7 files)
      … 7 files under this directory
    models/  (17 files)
      … 17 files under this directory
    scripts/  (23 files)
      … 23 files under this directory
    tasks/  (7 files)
      … 7 files under this directory
    README.md
    __init__.py
    fb_convert_beit_cp.py
  discriminative_reranking_nmt/  (11 files)
    config/  (1 files)
      … 1 files under this directory
    criterions/  (2 files)
      … 2 files under this directory
    models/  (2 files)
      … 2 files under this directory
    scripts/  (1 files)
      … 1 files under this directory
    tasks/  (2 files)
      … 2 files under this directory
    README.md
    __init__.py
    drnmt_rerank.py
  emotion_conversion/  (19 files)
    emotion_models/  (6 files)
      … 6 files under this directory
    fairseq_models/  (1 files)
      … 1 files under this directory
    preprocess/  (9 files)
      … 9 files under this directory
    README.md
    requirements.txt
    synthesize.py
  fast_noisy_channel/  (5 files)
    README.md
    __init__.py
    noisy_channel_beam_search.py
    noisy_channel_sequence_generator.py
    noisy_channel_translation.py
  flores101/  (1 files)
    README.md
  fully_sharded_data_parallel/  (1 files)
    README.md
  gottbert/  (1 files)
    README.md
  hubert/  (36 files)
    config/  (17 files)
      … 17 files under this directory
    simple_kmeans/  (8 files)
      … 8 files under this directory
    tests/  (8 files)
      … 8 files under this directory
    README.md
    measure_teacher_quality.py
    update_ckpt.py
  joint_alignment_translation/  (2 files)
    README.md
    prepare-wmt18en2de_no_norm_no_escape_no_agressive.sh
  language_model/  (4 files)
    README.adaptive_inputs.md
    README.conv.md
    README.md
    prepare-wikitext-103.sh
  laser/  (6 files)
    laser_src/  (5 files)
      … 5 files under this directory
    README.md
  latent_depth/  (10 files)
    latent_depth_src/  (9 files)
      … 9 files under this directory
    README.md
  layerdrop/  (1 files)
    README.md
  linformer/  (8 files)
    linformer_src/  (7 files)
      … 7 files under this directory
    README.md
  m2m_100/  (14 files)
    process_data/  (3 files)
      … 3 files under this directory
    tokenizers/  (8 files)
      … 8 files under this directory
    README.md
    install_dependecies.sh
    tok.sh
  mbart/  (1 files)
    README.md
  megatron_11b/  (2 files)
    README.md
    detok.py
  mms/  (34 files)
    asr/  (3 files)
      … 3 files under this directory
    data_prep/  (6 files)
      … 6 files under this directory
    lid/  (2 files)
      … 2 files under this directory
    lid_rerank/  (18 files)
      … 18 files under this directory
    misc/  (1 files)
      … 1 files under this directory
    tts/  (1 files)
      … 1 files under this directory
    zero_shot/  (1 files)
      … 1 files under this directory
    MODEL_CARD.md
    README.md
  moe_lm/  (3 files)
    README.md
    data_card.md
    model_card.md
  mr_hubert/  (17 files)
    config/  (13 files)
      … 13 files under this directory
    README.md
    decode.sh
    finetune.sh
    train.sh
  multilingual/  (27 files)
    data_scripts/  (22 files)
      … 22 files under this directory
    ML50_langs.txt
    README.md
    finetune_multilingual_model.sh
    multilingual_fairseq_gen.sh
    train_multilingual_model.sh
  noisychannel/  (9 files)
    README.md
    __init__.py
    rerank.py
    rerank_generate.py
    rerank_options.py
    rerank_score_bw.py
    rerank_score_lm.py
    rerank_tune.py
    rerank_utils.py
  nonautoregressive_translation/  (2 files)
    README.md
    scripts.md
  normformer/  (2 files)
    README.md
    train_lm.sh
  operators/  (5 files)
    alignment_train_cpu.cpp
    alignment_train_cuda.cpp
    alignment_train_cuda.h
    alignment_train_kernel.cu
    utils.h
  paraphraser/  (2 files)
    README.md
    paraphrase.py
  pay_less_attention_paper/  (1 files)
    README.md
  pointer_generator/  (6 files)
    pointer_generator_src/  (2 files)
      … 2 files under this directory
    README.md
    README.xsum.md
    postprocess.py
    preprocess.py
  quant_noise/  (2 files)
    README.md
    transformer_quantization_config.yaml
  roberta/  (36 files)
    commonsense_qa/  (4 files)
      … 4 files under this directory
    config/  (17 files)
      … 17 files under this directory
    fb_multilingual/  (1 files)
      … 1 files under this directory
    wsc/  (5 files)
      … 5 files under this directory
    README.custom_classification.md
    README.glue.md
    README.md
    README.pretraining.md
    README.race.md
    multiprocessing_bpe_encoder.py
    preprocess_GLUE_tasks.sh
    preprocess_RACE.py
    preprocess_RACE.sh
  rxf/  (5 files)
    rxf_src/  (3 files)
      … 3 files under this directory
    README.md
    __init__.py
  scaling_nmt/  (1 files)
    README.md
  shuffled_word_order/  (2 files)
    README.finetuning.md
    README.md
  simultaneous_translation/  (18 files)
    docs/  (2 files)
      … 2 files under this directory
    eval/  (1 files)
      … 1 files under this directory
    models/  (3 files)
      … 3 files under this directory
    modules/  (4 files)
      … 4 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    utils/  (4 files)
      … 4 files under this directory
    README.md
    __init__.py
  speech_recognition/  (39 files)
    criterions/  (3 files)
      … 3 files under this directory
    data/  (5 files)
      … 5 files under this directory
    datasets/  (2 files)
      … 2 files under this directory
    kaldi/  (5 files)
      … 5 files under this directory
    models/  (3 files)
      … 3 files under this directory
    new/  (14 files)
      … 14 files under this directory
    tasks/  (2 files)
      … 2 files under this directory
    utils/  (1 files)
      … 1 files under this directory
    README.md
    __init__.py
    infer.py
    w2l_decoder.py
  speech_synthesis/  (27 files)
    docs/  (3 files)
      … 3 files under this directory
    evaluation/  (5 files)
      … 5 files under this directory
    preprocessing/  (14 files)
      … 14 files under this directory
    README.md
    __init__.py
    data_utils.py
    generate_waveform.py
    utils.py
  speech_text_joint_to_text/  (22 files)
    configs/  (1 files)
      … 1 files under this directory
    criterions/  (4 files)
      … 4 files under this directory
    data/  (1 files)
      … 1 files under this directory
    docs/  (3 files)
      … 3 files under this directory
    models/  (5 files)
      … 5 files under this directory
    scripts/  (2 files)
      … 2 files under this directory
    tasks/  (4 files)
      … 4 files under this directory
    README.md
    __init__.py
  speech_to_speech/  (30 files)
    asr_bleu/  (6 files)
      … 6 files under this directory
    benchmarking/  (8 files)
      … 8 files under this directory
    docs/  (4 files)
      … 4 files under this directory
    preprocessing/  (6 files)
      … 6 files under this directory
    unity/  (3 files)
      … 3 files under this directory
    README.md
    __init__.py
    generate_waveform_from_code.py
  speech_to_text/  (13 files)
    docs/  (5 files)
      … 5 files under this directory
    simultaneous_translation/  (1 files)
      … 1 files under this directory
    README.md
    data_utils.py
    prep_covost_data.py
    prep_librispeech_data.py
    prep_mtedx_data.py
    prep_mustc_data.py
    seg_mustc_data.py
  stories/  (1 files)
    README.md
  textless_nlp/  (14 files)
    dgslm/  (7 files)
      … 7 files under this directory
    gslm/  (7 files)
      … 7 files under this directory
  .gitignore
  __init__.py
.gitignore
.gitmodules
.pre-commit-config.yaml
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
MANIFEST.in
README.md
RELEASE.md
```

## Entry points

No application entry point was observed at this commit.

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 46 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: AlignmentTrainTest, ChunkwiswTestCase, HardMonotonicAttentionTestCase, InfiniteLookbackTestCase, MonotonicA… |

## Important files

- `.github/stale.yml` (config)
- `.github/workflows/build.yml` (ci)
- `.github/workflows/depreview.yml` (ci)
- `.github/workflows/release.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `MANIFEST.in` (manifest)
- `examples/MMPT/projects/mfmmlm.yaml` (config)
- `examples/MMPT/projects/mtm/mmfusionmtm.yaml` (config)
- `examples/MMPT/projects/mtm/vlm.yaml` (config)
- `examples/MMPT/projects/mtm/vlm/coin.yaml` (config)
- `examples/MMPT/projects/mtm/vlm/crosstask.yaml` (config)
- `examples/MMPT/projects/mtm/vlm/how2.yaml` (config)
- `examples/MMPT/projects/mtm/vlm/vtt.yaml` (config)
- `examples/MMPT/projects/mtm/vlm/vttqa.yaml` (config)
- `examples/MMPT/projects/mtm/vlm/youcook.yaml` (config)
- `examples/MMPT/projects/mtm/vlm/youcookcap.yaml` (config)
- `examples/MMPT/projects/retri/videoclip.yaml` (config)
- `examples/MMPT/projects/retri/videoclip/coin_videoclip.yaml` (config)
- `examples/MMPT/projects/retri/videoclip/crosstask_videoclip.yaml` (config)
- `examples/MMPT/projects/retri/videoclip/how2.yaml` (config)
- `examples/MMPT/projects/retri/videoclip/vtt_videoclip.yaml` (config)
- `examples/MMPT/projects/retri/videoclip/vttqa_videoclip.yaml` (config)
- `examples/MMPT/projects/retri/videoclip/youcook_videoclip.yaml` (config)
- `examples/MMPT/projects/retri/videoretri.yaml` (config)
- `examples/MMPT/projects/task/coin.yaml` (config)
- `examples/MMPT/projects/task/coin_videoclip.yaml` (config)
- `examples/MMPT/projects/task/crosstask.yaml` (config)
- `examples/MMPT/projects/task/crosstask_videoclip.yaml` (config)
- `examples/MMPT/projects/task/default.yaml` (config)
- `examples/MMPT/projects/task/ft.yaml` (config)
- `examples/MMPT/projects/task/how2.yaml` (config)
- `examples/MMPT/projects/task/test.yaml` (config)
- `examples/MMPT/projects/task/vtt.yaml` (config)
- `examples/MMPT/projects/task/vtt_videoclip.yaml` (config)
- `examples/MMPT/projects/task/vttqa.yaml` (config)
- `examples/MMPT/projects/task/vttqa_videoclip.yaml` (config)
- `examples/MMPT/projects/task/youcook.yaml` (config)
- `examples/MMPT/projects/task/youcook_videoclip.yaml` (config)
- `examples/MMPT/projects/task/youcookcap.yaml` (config)
- `examples/MMPT/scripts/text_token_extractor/configs/bert-base-uncased.yaml` (config)
- `examples/MMPT/setup.py` (manifest)
- `examples/audio_nlp/nlu/configs/nlu_finetuning.yaml` (config)
- `examples/data2vec/config/audio/classification/base_classification.yaml` (config)
- `examples/data2vec/config/audio/classification/run_config/slurm_1.yaml` (config)
- `examples/data2vec/config/audio/classification/run_config/slurm_1g.yaml` (config)
- `examples/data2vec/config/audio/classification/run_config/slurm_2.yaml` (config)
- `examples/data2vec/config/audio/pretraining/audioset.yaml` (config)
- `examples/data2vec/config/audio/pretraining/base_librispeech.yaml` (config)
- `examples/data2vec/config/audio/pretraining/run_config/local.yaml` (config)
- `examples/data2vec/config/audio/pretraining/run_config/slurm_1.yaml` (config)
- `examples/data2vec/config/audio/pretraining/run_config/slurm_1_aws.yaml` (config)
- `examples/data2vec/config/audio/pretraining/run_config/slurm_2.yaml` (config)
- `examples/data2vec/config/audio/pretraining/run_config/slurm_2_aws.yaml` (config)
- `examples/data2vec/config/audio/pretraining/run_config/slurm_3.yaml` (config)
- `examples/data2vec/config/audio/pretraining/run_config/slurm_4.yaml` (config)
- `examples/data2vec/config/audio/pretraining/run_config/slurm_4_aws.yaml` (config)
- `examples/data2vec/config/audio/pretraining/run_config/slurm_6_aws.yaml` (config)
- `examples/data2vec/config/audio/pretraining/run_config/slurm_8_aws.yaml` (config)
- `examples/data2vec/config/text/pretraining/base.yaml` (config)
- `examples/data2vec/config/text/pretraining/run_config/local.yaml` (config)
- `examples/data2vec/config/text/pretraining/run_config/slurm_1_aws.yaml` (config)
- `examples/data2vec/config/text/pretraining/run_config/slurm_2.yaml` (config)
- `examples/data2vec/config/text/pretraining/run_config/slurm_2_aws.yaml` (config)
- `examples/data2vec/config/text/pretraining/run_config/slurm_3.yaml` (config)
- `examples/data2vec/config/text/pretraining/run_config/slurm_4.yaml` (config)
- `examples/data2vec/config/text/pretraining/run_config/slurm_4_aws.yaml` (config)
- `examples/data2vec/config/text/pretraining/run_config/slurm_8_aws.yaml` (config)
- `examples/data2vec/config/v2/base_audio_only_task.yaml` (config)
- `examples/data2vec/config/v2/base_images_only_task.yaml` (config)
- `examples/data2vec/config/v2/base_text_only_task.yaml` (config)
- `examples/data2vec/config/v2/huge_images14_only_task.yaml` (config)
- `examples/data2vec/config/v2/huge_images_only_task.yaml` (config)
- `examples/data2vec/config/v2/large_audio_only_task.yaml` (config)
- `examples/data2vec/config/v2/large_images_only_task.yaml` (config)
- `examples/data2vec/config/v2/large_text_only_task.yaml` (config)
- `examples/data2vec/config/v2/large_text_only_task_pgrp_1M.yaml` (config)
- `examples/data2vec/config/v2/run_config/local.yaml` (config)
- `examples/data2vec/config/v2/run_config/slurm_1.yaml` (config)
- `examples/data2vec/config/v2/run_config/slurm_1_aws.yaml` (config)
- `examples/data2vec/config/v2/run_config/slurm_2.yaml` (config)
- `examples/data2vec/config/v2/run_config/slurm_2_aws.yaml` (config)
- `examples/data2vec/config/v2/run_config/slurm_3.yaml` (config)
- `examples/data2vec/config/v2/run_config/slurm_4.yaml` (config)
- `examples/data2vec/config/v2/run_config/slurm_4_aws.yaml` (config)
- `examples/data2vec/config/v2/run_config/slurm_6_aws.yaml` (config)
- `examples/data2vec/config/v2/run_config/slurm_8.yaml` (config)
- `examples/data2vec/config/v2/run_config/slurm_8_aws.yaml` (config)
- `examples/data2vec/config/v2/text_finetuning/cola.yaml` (config)
- `examples/data2vec/config/v2/text_finetuning/mnli.yaml` (config)
- `examples/data2vec/config/v2/text_finetuning/mrpc.yaml` (config)
- `examples/data2vec/config/v2/text_finetuning/qnli.yaml` (config)
- `examples/data2vec/config/v2/text_finetuning/qqp.yaml` (config)
- `examples/data2vec/config/v2/text_finetuning/rte.yaml` (config)
- `examples/data2vec/config/v2/text_finetuning/run_config/local.yaml` (config)
- `examples/data2vec/config/v2/text_finetuning/sst_2.yaml` (config)
- `examples/data2vec/config/v2/text_finetuning/sts_b.yaml` (config)
- `examples/data2vec/config/vision/finetuning/imagenet.yaml` (config)
- `examples/data2vec/config/vision/finetuning/mae_imagenet_clean.yaml` (config)
- `examples/data2vec/config/vision/finetuning/mae_imagenet_huge_clean.yaml` (config)
- `examples/data2vec/config/vision/finetuning/mae_imagenet_large_clean.yaml` (config)
- `examples/data2vec/config/vision/finetuning/run_config/local.yaml` (config)
- `examples/data2vec/config/vision/finetuning/run_config/slurm_1.yaml` (config)
- `examples/data2vec/config/vision/finetuning/run_config/slurm_1_aws.yaml` (config)
- `examples/data2vec/config/vision/finetuning/run_config/slurm_2.yaml` (config)
- `examples/data2vec/config/vision/finetuning/run_config/slurm_2_aws.yaml` (config)
- `examples/data2vec/config/vision/finetuning/run_config/slurm_3.yaml` (config)
- `examples/data2vec/config/vision/finetuning/run_config/slurm_4.yaml` (config)
- `examples/data2vec/config/vision/finetuning/run_config/slurm_4_aws.yaml` (config)
- `examples/data2vec/config/vision/finetuning/run_config/slurm_6_aws.yaml` (config)
- `examples/data2vec/config/vision/finetuning/run_config/slurm_8_aws.yaml` (config)
- `examples/data2vec/config/vision/pretraining/base_imagenet.yaml` (config)
- `examples/data2vec/config/vision/pretraining/base_imagenet_d2v1.yaml` (config)
- `examples/data2vec/config/vision/pretraining/base_mae_imagenet.yaml` (config)
- `examples/data2vec/config/vision/pretraining/run_config/local.yaml` (config)
- `examples/data2vec/config/vision/pretraining/run_config/slurm_1.yaml` (config)
- `examples/data2vec/config/vision/pretraining/run_config/slurm_1_aws.yaml` (config)
- `examples/data2vec/config/vision/pretraining/run_config/slurm_2.yaml` (config)
- `examples/data2vec/config/vision/pretraining/run_config/slurm_2_aws.yaml` (config)
- `examples/data2vec/config/vision/pretraining/run_config/slurm_3.yaml` (config)
- `examples/data2vec/config/vision/pretraining/run_config/slurm_4.yaml` (config)
- `examples/data2vec/config/vision/pretraining/run_config/slurm_4_aws.yaml` (config)
- `examples/data2vec/config/vision/pretraining/run_config/slurm_6_aws.yaml` (config)
- `examples/data2vec/config/vision/pretraining/run_config/slurm_8_aws.yaml` (config)
- `examples/discriminative_reranking_nmt/config/deen.yaml` (config)
- `examples/emotion_conversion/emotion_models/duration_predictor.yaml` (config)
- `examples/emotion_conversion/emotion_models/pitch_predictor.yaml` (config)
- `examples/emotion_conversion/requirements.txt` (manifest)
- `examples/hubert/config/decode/ax_sweep/ngram.yaml` (config)
- `examples/hubert/config/decode/ax_sweep/transformer.yaml` (config)
- `examples/hubert/config/decode/infer_fsqlm.yaml` (config)
- `examples/hubert/config/decode/infer_kenlm.yaml` (config)
- `examples/hubert/config/decode/infer_viterbi.yaml` (config)
- `examples/hubert/config/decode/run/submitit_slurm.yaml` (config)
- `examples/hubert/config/decode/run/submitit_slurm_8gpu.yaml` (config)
- `examples/hubert/config/finetune/base_10h.yaml` (config)
- `examples/hubert/config/finetune/ckpt/it1.yaml` (config)
- `examples/hubert/config/finetune/lm/ls_4gram.yaml` (config)
- `examples/hubert/config/finetune/run/submitit_reg.yaml` (config)
- `examples/hubert/config/pretrain/data/iter1.yaml` (config)
- `examples/hubert/config/pretrain/data/iter2.yaml` (config)
- `examples/hubert/config/pretrain/hubert_base_librispeech.yaml` (config)
- `examples/hubert/config/pretrain/hubert_large_librivox.yaml` (config)
- `examples/hubert/config/pretrain/hubert_xlarge_librivox.yaml` (config)
- `examples/hubert/config/pretrain/run/submitit_reg.yaml` (config)
- `examples/mms/asr/config/infer_common.yaml` (config)
- `examples/mms/lid_rerank/requirements.txt` (manifest)
- `examples/mr_hubert/config/decode/infer.yaml` (config)
- `examples/mr_hubert/config/decode/infer_lm.yaml` (config)
- `examples/mr_hubert/config/decode/run/submitit_slurm.yaml` (config)
- `examples/mr_hubert/config/decode/run/submitit_slurm_8gpu.yaml` (config)
- `examples/mr_hubert/config/finetune/base_100h.yaml` (config)
- `examples/mr_hubert/config/finetune/base_100h_large.yaml` (config)
- `examples/mr_hubert/config/finetune/base_10h.yaml` (config)
- `examples/mr_hubert/config/finetune/base_10h_large.yaml` (config)
- `examples/mr_hubert/config/finetune/base_1h.yaml` (config)
- `examples/mr_hubert/config/finetune/base_1h_large.yaml` (config)
- `examples/mr_hubert/config/pretrain/mrhubert_base_librispeech.yaml` (config)
- `examples/mr_hubert/config/pretrain/mrhubert_large_librilight.yaml` (config)
- `examples/mr_hubert/config/pretrain/run/submitit_reg.yaml` (config)
- `examples/quant_noise/transformer_quantization_config.yaml` (config)
- `examples/roberta/config/finetuning/cola.yaml` (config)
- `examples/roberta/config/finetuning/mnli.yaml` (config)
- `examples/roberta/config/finetuning/mrpc.yaml` (config)
- `examples/roberta/config/finetuning/qnli.yaml` (config)
- `examples/roberta/config/finetuning/qqp.yaml` (config)
- `examples/roberta/config/finetuning/rte.yaml` (config)
- `examples/roberta/config/finetuning/run_config/local.yaml` (config)
- `examples/roberta/config/finetuning/run_config/slurm_1g.yaml` (config)
- `examples/roberta/config/finetuning/run_config/slurm_1g_aws.yaml` (config)
- `examples/roberta/config/finetuning/sst_2.yaml` (config)
- `examples/roberta/config/finetuning/sts_b.yaml` (config)
- `examples/roberta/config/pretraining/base.yaml` (config)
- `examples/roberta/config/pretraining/run_config/local.yaml` (config)
- `examples/roberta/config/pretraining/run_config/slurm_2.yaml` (config)
- `examples/roberta/config/pretraining/run_config/slurm_2_aws.yaml` (config)
- `examples/roberta/config/pretraining/run_config/slurm_3.yaml` (config)
- `examples/roberta/config/pretraining/run_config/slurm_4.yaml` (config)
- `examples/speech_recognition/kaldi/config/kaldi_initializer.yaml` (config)
- `examples/speech_recognition/new/conf/hydra/sweeper/ax.yaml` (config)
- `examples/speech_recognition/new/conf/hydra/sweeper/ax_sil.yaml` (config)
- `examples/speech_recognition/new/conf/infer.yaml` (config)
- `examples/speech_recognition/new/conf/run_config/fb_slurm_1.yaml` (config)
- `examples/speech_recognition/new/conf/run_config/fb_slurm_2g.yaml` (config)
- `examples/speech_to_speech/asr_bleu/asr_model_cfgs.json` (config)
- `examples/speech_to_speech/asr_bleu/requirements.txt` (manifest)
- `examples/speech_to_speech/benchmarking/configs/2StageS2ST.yaml` (config)
- `examples/speech_to_speech/benchmarking/configs/3StageS2ST.yaml` (config)
- `examples/speech_to_speech/benchmarking/configs/DirectS2U.yaml` (config)
- `examples/speech_to_speech/benchmarking/configs/S2T.yaml` (config)

## Top-level layout

- `examples` — 762 analysed file(s)
- `docs` — 18 analysed file(s)
- `.github` — 11 analysed file(s)
- `(root files)` — 9 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- No clear application entry point was observed in the analysed files.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `3d262bb25690e4eb2e7d3c1309b1e9c406ca4b99` is the revision these paths and observations refer to.
