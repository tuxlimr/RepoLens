# Project structure: verl-project/verl

**Analysed commit:** `4191e7f910d85d69acb8c45f4840f10faa535165`

**Commit reference:** [4191e7f910d85d69acb8c45f4840f10faa535165](https://github.com/verl-project/verl/commit/4191e7f910d85d69acb8c45f4840f10faa535165)

**Tree at this commit:** [verl-project/verl@4191e7f910d8](https://github.com/verl-project/verl/tree/4191e7f910d85d69acb8c45f4840f10faa535165)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | verl-project/verl |
| Description | verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework  |
| Stars | 24230 |
| Forks | 4909 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `4191e7f910d85d69acb8c45f4840f10faa535165` |
| Retrieved at | 2026-11-14T19:07:39.669298+00:00 |
| Files in this snapshot | 799 |

## Directory tree

```text
.agent/  (3 files)
  skills/  (3 files)
    issue/  (1 files)
      … 1 files under this directory
    pr/  (1 files)
      … 1 files under this directory
    upgrade-deps/  (1 files)
      … 1 files under this directory
.github/  (56 files)
  ISSUE_TEMPLATE/  (3 files)
    bug-report.yml
    config.yml
    feature-request.yml
  workflows/  (50 files)
    README.md
    check-pr-title.yml
    cpu_unit_tests.yml
    doc.yml
    docker-build-ascend-a2.yml
    docker-build-ascend-a3.yml
    docker-build-ascend-a5.yml
    docker-build-ascend-sglang-a2.yml
    docker-build-ascend-sglang-a3.yml
    e2e_ascend.yml
    e2e_ppo_grpo_trainer_trtllm.yml
    e2e_ppo_trainer.yml
    e2e_ppo_trainer_megatron_sglang.yml
    e2e_ppo_trainer_megatron_sglang_2.yml
    e2e_ppo_trainer_megatron_sglang_2_ascend.yml
    e2e_ppo_trainer_megatron_sglang_ascend.yml
    e2e_ppo_trainer_megatron_vllm.yml
    e2e_ppo_trainer_megatron_vllm_2.yml
    e2e_ppo_trainer_megatron_vllm_2_ascend.yml
    e2e_ppo_trainer_megatron_vllm_ascend.yml
    e2e_ppo_trainer_megatron_vllm_rocm.yml
    e2e_ppo_trainer_torchtitan_vllm.yml
    e2e_ppo_trainer_veomni_vllm.yml
    e2e_ppo_trainer_veomni_vllm_ascend.yml
    … 26 more files
  CODEOWNERS
  PULL_REQUEST_TEMPLATE.md
  dependabot.yml
.vscode/  (1 files)
  settings.json
docker/  (76 files)
  ascend/  (28 files)
    patches/  (1 files)
      … 1 files under this directory
    Dockerfile.ascend.sglang_8.3.rc1_a2
    Dockerfile.ascend.sglang_8.3.rc1_a3
    Dockerfile.ascend.sglang_8.5.0_a2
    Dockerfile.ascend.sglang_8.5.0_a3
    Dockerfile.ascend_8.2.rc1_a2
    Dockerfile.ascend_8.2.rc1_a3
    Dockerfile.ascend_8.3.rc1_a2
    Dockerfile.ascend_8.3.rc1_a3
    Dockerfile.ascend_8.5.0_a2
    Dockerfile.ascend_8.5.0_a2_v0.7.1
    Dockerfile.ascend_8.5.0_a3
    Dockerfile.ascend_8.5.0_a3_v0.7.1
    Dockerfile.ascend_8.5.2_a2_qwen3-5
    Dockerfile.ascend_8.5.2_a3_qwen3-5
    Dockerfile.ascend_9.0.0_a2_v0.8.0
    Dockerfile.ascend_9.0.0_a3_v0.8.0
    Dockerfile.ascend_9.1.0_a2
    Dockerfile.ascend_9.1.0_a2_v0.9.1
    Dockerfile.ascend_9.1.0_a3
    Dockerfile.ascend_9.1.0_a3_v0.9.1
    Dockerfile.ascend_9.1.0_a5
    Dockerfile.ascend_9.1.0_a5_v0.9.1
    Dockerfile.ascend_9.2.1_a2
    Dockerfile.ascend_9.2.1_a3
    … 3 more files
  aws/  (2 files)
    Dockerfile.extention.awsefa
    Dockerfile.ngc.vllm0.8.sagemaker
  rocm/  (13 files)
    patches/  (5 files)
      … 5 files under this directory
    Apptainerfile.rocm
    Dockerfile.rocm
    Dockerfile.rocm.deepseek-v4
    Dockerfile.rocm6
    Dockerfile.rocm702
    Dockerfile.rocm_verl-0.3.0.post1
    Dockerfile.rocm_verl-0.4.1
    README.md
  verl0.4-cu124-torch2.6-fa2.7.4/  (8 files)
    Dockerfile.app.sglang.vllm.mcore0.12
    Dockerfile.app.sglang.vllm.mcore0.12.deepep
    Dockerfile.app.sglang.vllm.mcore0.13.preview
    Dockerfile.app.vllm.mcore0.12
    Dockerfile.app.vllm.mcore0.12.deepep
    Dockerfile.app.vllm.mcore0.13.preview
    Dockerfile.base
    README.md
  verl0.5-cu126-torch2.7-fa2.7.4/  (6 files)
    Dockerfile.app.sglang0.4.10.post2.mcore0.13
    Dockerfile.app.sglang0.4.9.post6.mcore0.13
    Dockerfile.app.vllm.mcore0.13
    Dockerfile.app.vllm.mcore0.15
    Dockerfile.base.torch2.7.1
    README.md
  verl0.5-cu126-torch2.7.1-fa2.8.0/  (4 files)
    Dockerfile.app.sglang.mcore0.12
    Dockerfile.app.sglang.mcore0.13.preview
    Dockerfile.base
    README.md
  verl0.5-preview-cu128-torch2.7.1-fa2.8.0/  (3 files)
    Dockerfile.app.sglang.megatron
    Dockerfile.base
    README.md
  verl0.6-cu128-torch2.8.0-fa2.7.4/  (3 files)
    Dockerfile.app.sglang
    Dockerfile.base
    Dockerfile.vllm011.mcore_gpt-oss
  verl0.6.1-experimental/  (2 files)
    Dockerfile.sglang056exp
    Dockerfile.vllm012exp
  xpu/  (1 files)
    Dockerfile.stable.vllm
  Dockerfile.isaaclab230
  Dockerfile.stable.sglang
  Dockerfile.stable.trtllm
  Dockerfile.stable.vllm
  Dockerfile.uv.cu130
  README.md
docs/  (156 files)
  _static/  (3 files)
    js/  (2 files)
      … 2 files under this directory
    custom.css
  advance/  (26 files)
    agent_loop.rst
    async-on-policy-distill.md
    attention_implementation.rst
    checkpoint.rst
    deepseek_v4_integration.rst
    delta_weight_sync.md
    determinism.md
    dpo_extension.rst
    dynamic_context_parallel.rst
    dynamic_schedule.md
    fsdp_extension.rst
    fsdp_turbo_backend.rst
    fully_async.md
    grafana_prometheus.md
    megatron_extension.rst
    megatron_lite_backend.rst
    mtp.md
    one_step_off.md
    placement.rst
    ppo_lora.rst
    reward_loop.rst
    rl_insight.md
    rollout_trace.rst
    rope.rst
    … 2 more files
  algo/  (15 files)
    baseline.md
    dapo.md
    dppo.md
    dro.md
    entropy.md
    gpg.md
    grpo.md
    opd.md
    opo.md
    otb.md
    ppo.md
    rollout_corr.md
    rollout_corr_math.md
    spin.md
    sppo.md
  amd_tutorial/  (3 files)
    amd_quick_start.rst
    amd_vllm_page.rst
    index.rst
  api/  (4 files)
    data.rst
    single_controller.rst
    trainer.rst
    utils.rst
  ascend_tutorial/  (52 files)
    en/  (26 files)
      … 26 files under this directory
    zh/  (25 files)
      … 25 files under this directory
    index.rst
  blog/  (1 files)
    v0.7.md
  contributing/  (1 files)
    editing-agent-instructions.md
  data/  (1 files)
    transfer_queue.md
  examples/  (7 files)
    config.rst
    gsm8k_example.rst
    megatron_fsdp_example.rst
    multi_modal_example.rst
    ppo_code_architecture.rst
    sandbox_fusion_example.rst
    skypilot_examples.rst
  faq/  (1 files)
    faq.rst
  hardware/  (1 files)
    multi_chip_support.rst
  low_precision/  (5 files)
    fp8.md
    mxfp4_qat.md
    mxfp8.md
    nvfp4.md
    qat.md
  perf/  (8 files)
    best_practices.rst
    device_tuning.rst
    dpsk.md
    nsight_profiling.md
    perf_tuning.rst
    rollout_kv_offload.md
    torch_profiling.md
    verl_profiler_system.md
  preparation/  (2 files)
    prepare_data.rst
    reward_function.rst
  sglang_multiturn/  (3 files)
    multiturn.rst
    sandbox_fusion.rst
    search_tool_example.rst
  start/  (6 files)
    agentic_rl.rst
    install.rst
    more_resources.rst
    multinode.rst
    quickstart.rst
    ray_debug_tutorial.rst
  workers/  (7 files)
    automodel_workers.rst
    engine_workers.rst
    model_engine.rst
    ray_trainer.rst
    sglang_worker.rst
    torchtitan_workers.rst
    trtllm_worker.rst
  Makefile
  README.md
  README_vllm0.7.md
  README_vllm0.8.md
  conf.py
  extend_guide.rst
  hybrid_flow.rst
  index.rst
  requirements-docs.txt
  single_controller.rst
examples/  (179 files)
  ascend_extras/  (10 files)
    grpo_trainer/  (7 files)
      … 7 files under this directory
    gspo_trainer/  (1 files)
      … 1 files under this directory
    low_precision/  (1 files)
      … 1 files under this directory
    ppo_trainer/  (1 files)
      … 1 files under this directory
  cispo_trainer/  (2 files)
    README.md
    run_qwen3_8b_fsdp.sh
  data_preprocess/  (16 files)
    aime2024_multiturn_w_tool.py
    dapo_multiturn_w_tool.py
    full_hh_rlhf.py
    geo3k.py
    geo3k_multiturn_w_tool.py
    gsm8k.py
    gsm8k_multiturn_sft.py
    gsm8k_multiturn_w_tool.py
    gsm8k_tool_agent_loop.py
    hellaswag.py
    math_dataset.py
    multiturn.py
    openr1mm.py
    pokemon.py
    preprocess_search_r1_dataset.py
    tinyllava_video_r1.py
  dppo_trainer/  (2 files)
    README.md
    run_qwen3_30b_a3b_megatron.sh
  gdpo_trainer/  (2 files)
    README.md
    run_qwen3_8b_fsdp.sh
  generation/  (1 files)
    run_deepseek_llm_7b.sh
  gmpo_trainer/  (2 files)
    README.md
    run_qwen3_8b_fsdp.sh
  gpg_trainer/  (3 files)
    README.md
    run_qwen3_8b_fsdp.sh
    run_qwen3_8b_megatron.sh
  grpo_trainer/  (48 files)
    README.md
    run_deepseek_v3_671b_megatron.sh
    run_deepseek_v4_flash_megatron.sh
    run_deepseek_v4_flash_megatron_rocm.sh
    run_deepseek_v4_megatron_lite.sh
    run_deepseek_v4_pro_megatron.sh
    run_deepseek_v4_veomni.sh
    run_glm4_1v_9b_fsdp.sh
    run_gpt_oss_20b_fsdp.sh
    run_gpt_oss_20b_veomni.sh
    run_hy_v3_megatron.sh
    run_kimi_k2_6_glm5_1_megatron_lite.sh
    run_minicpm_o_2_6_fsdp.sh
    run_mistral_nemo_12b_skyworkrm_fsdp.sh
    run_moonlight_16b_a3b_megatron.sh
    run_nemotron_nano_v3_30b_a3b_megatron.sh
    run_qwen2-7b_math_megatron_fsdp.sh
    run_qwen2_5_32b_fsdp.sh
    run_qwen2_5_vl_7b_fsdp.sh
    run_qwen2_5_vl_7b_megatron.sh
    run_qwen3_235b_a22b_megatron.sh
    run_qwen3_30b_a3b_fsdp.sh
    run_qwen3_30b_a3b_megatron.sh
    run_qwen3_30b_veomni.sh
    … 24 more files
  gspo_trainer/  (3 files)
    README.md
    run_qwen3_30b_a3b_megatron.sh
    run_qwen3_8b_fsdp.sh
  mtp_trainer/  (4 files)
    README.md
    run_mimo_7b_mtp_fully_async_megatron_multinode.sh
    run_mimo_7b_mtp_megatron.sh
    run_mimo_7b_mtp_rl_vllm_sgl_megatron.sh
  muon/  (1 files)
    README.md
  mxfp4/  (1 files)
    run_qwen3_30b_a3b_megatron.sh
  mxfp8/  (2 files)
    run_qwen3_30b_a3b_megatron.sh
    run_qwen3_8b_megatron.sh
  on_policy_distillation_trainer/  (9 files)
    README.md
    run_qwen3_0.6b_opd_veomni.sh
    run_qwen3_5_2b_fsdp.sh
    run_qwen3_5_4b_fsdp.sh
    run_qwen3_8b_fsdp.sh
    run_qwen3_8b_megatron.sh
    run_qwen3_8b_mopd_fsdp.sh
    run_qwen3_8b_mopd_veomni.sh
    run_qwen3_vl_8b_fsdp.sh
  otb_trainer/  (2 files)
    README.md
    run_qwen3_8b_fsdp.sh
  ppo_trainer/  (3 files)
    README.md
    run_qwen3_8b_fsdp.sh
    run_qwen3_8b_megatron.sh
  prefix_grouper/  (2 files)
    README.md
    run_qwen3_8b_fsdp.sh
  profile/  (5 files)
    README.md
    run_qwen2_5_7b_torch_profile.sh
    run_qwen2_5_vl_7b_torch_memory.sh
    run_qwen3_8b_npu_profile_discrete.sh
    run_qwen3_8b_npu_profile_e2e.sh
  real_nvfp4/  (3 files)
    README.md
    run_qwen3_30b_megatron.sh
    runtime_env.yaml
  reinforce_plus_plus_trainer/  (2 files)
    README.md
    run_qwen3_8b_fsdp.sh
  remax_trainer/  (3 files)
    README.md
    run_qwen2.5_math_7b_sync_fsdp.sh
    run_qwen3_8b_fsdp.sh
  rewards/  (1 files)
    custome_reward_fn/  (1 files)
      … 1 files under this directory
  rloo_trainer/  (2 files)
    README.md
    run_qwen3_8b_fsdp.sh
  rollout_correction/  (4 files)
    run_qwen2_5_0_5b_score_centering_fsdp.sh
    run_qwen2_5_7b_fsdp.sh
    run_qwen2_5_7b_fsdp_multi_rs.sh
    run_qwen3_30b_score_centering_megatron.sh
  router_replay/  (3 files)
    README.md
    run_qwen3_30b_a3b_megatron.sh
    run_qwen3_5_35b_a3b_veomni.sh
  sapo_trainer/  (3 files)
    README.md
    run_qwen3_30b_a3b_fsdp.sh
    run_qwen3_8b_fsdp.sh
  sft/  (15 files)
    gsm8k/  (13 files)
      … 13 files under this directory
    multiturn/  (1 files)
      … 1 files under this directory
    vlm/  (1 files)
      … 1 files under this directory
  tpu/  (8 files)
    grpo/  (6 files)
      … 6 files under this directory
    sft/  (2 files)
      … 2 files under this directory
  tuning/  (8 files)
    lora/  (5 files)
      … 5 files under this directory
    scaling/  (2 files)
      … 2 files under this directory
    README.md
  tutorial/  (8 files)
    agent_loop_get_started/  (2 files)
      … 2 files under this directory
    ray/  (1 files)
      … 1 files under this directory
    skypilot/  (3 files)
      … 3 files under this directory
    slurm/  (1 files)
      … 1 files under this directory
    README.md
  README.md
scripts/  (18 files)
  veomni/  (2 files)
    moe_merge.py
    moe_split.py
  __init__.py
  chat_template_checker.py
  chat_template_mock_trajectories.py
  converter_hf_to_mcore.py
  diagnose.py
  generate_trainer_config.sh
  init_random_model.py
  install_sglang_mcore_npu.sh
  install_vllm_mcore_npu.sh
  install_vllm_sglang_mcore.sh
  legacy_model_merger.py
  megatron_merge_lora.py
  migrate_megatron_checkpoint_layout.py
  print_cfg.py
  rollout_logprob_diff.py
  rollout_viewer.py
tests/  (293 files)
  checkpoint_engine/  (13 files)
    __init__.py
    d2h_checkpoint_engine.py
    test_block_placement.py
    test_correctness_on_gpu.py
    test_correctness_on_npu.py
    test_d2h_checkpoint_engine.py
    test_fsdp_lora_only_checkpoint_on_cpu.py
    test_global_steps_on_cpu.py
    test_sglang_fusion_bucketing_on_cpu.py
    test_sglang_loader.py
    test_sharded_delta.py
    test_special_server_adapter.py
    test_utils.py
  experimental/  (28 files)
    agent_loop/  (15 files)
      … 15 files under this directory
    fully_async_policy/  (2 files)
      … 2 files under this directory
    reward_loop/  (9 files)
      … 9 files under this directory
    vla/  (1 files)
      … 1 files under this directory
    __init__.py
  model_merger/  (3 files)
    test_fsdp_merge_non_dtensor_shards_on_cpu.py
    test_output_validation_on_cpu.py
    test_shard_configuration_on_cpu.py
  models/  (9 files)
    test_engine.py
    test_fsdp_no_padding_on_gpu.py
    test_fused_kernels_ulysses_sp_on_cpu.py
    test_liger_vl_compat.py
    test_model_forward_fused.py
    test_moe_zloss_per_token_loss.py
    test_tiled_mlp_accuracy.py
    test_transformer.py
    test_transformers_ulysses.py
  plugin/  (2 files)
    __init__.py
    test_platform_abstraction.py
  single_controller/  (26 files)
    base/  (1 files)
      … 1 files under this directory
    check_worker_alive/  (1 files)
      … 1 files under this directory
    detached_worker/  (4 files)
      … 4 files under this directory
    __init__.py
    test_auto_padding_on_cpu.py
    test_colocated_workers.py
    test_colocated_workers_fused.py
    test_data_transfer.py
    test_decorator_on_cpu.py
    test_device_agnostic_resources_on_cpu.py
    test_device_mesh_register.py
    test_driverfunc_to_worker.py
    test_fused_workers_on_cpu.py
    test_get_set_dispatch_collect_cpu.py
    test_high_level_scheduling_api.py
    test_nested_worker.py
    test_ray_collectives.py
    test_ray_local_envs_on_cpu.py
    test_ray_utils_on_cpu.py
    test_rvdz.py
    test_split_resource_pool.py
    test_worker_group_basics.py
    test_worker_group_torch.py
  special_distributed/  (15 files)
    README.md
    run_all.sh
    test_fsdp2_cpu_offload_state_dict.py
    test_fsdp2_model_cpu_offload.py
    test_fsdp2_pinned_model_transfer.py
    test_fsdp_ckpt.py
    test_fused_kernels_ulysses_sp.py
    test_mcore_probe_differential.py
    test_megatron_dynamic_cp_features.py
    test_qwen35_linear_attention_ulysses_sp.py
    test_router_replay_empty_pp.py
    test_sglang_delta_loop.py
    test_sharded_delta_gather.py
    test_tensor_dict.py
    test_torch_functional.py
  special_e2e/  (23 files)
    envs/  (4 files)
      … 4 files under this directory
    ppo_trainer/  (3 files)
      … 3 files under this directory
    sft/  (4 files)
      … 4 files under this directory
    README.md
    __init__.py
    check_custom_rwd_fn.py
    check_results.py
    profiler_finish_hook_marker.sh
    run_ppo_trainer_megatron.sh
    run_ppo_trainer_torchtitan.sh
    run_ppo_trainer_veomni.sh
    run_v1_colocate_async_disrm.sh
    run_v1_separate_async.sh
    run_v1_separate_async_ascend.sh
    run_v1_separate_async_opd.sh
  special_npu/  (22 files)
    nightly_ci_ascend/  (11 files)
      … 11 files under this directory
    quick_start/  (4 files)
      … 4 files under this directory
    run_qwen3_06b_grpo_mindspeed.sh
    run_qwen3_06b_ppo.sh
    run_qwen3_30b_grpo_mindspeed.sh
    run_qwen3_5_2b_fsdp_turbo.sh
    run_qwen3_5_35b_grpo_megatron.sh
    run_qwen3_8b_grpo_profiling.sh
    run_qwen3_vl_8b_Instruct_fsdp2_npu.sh
  special_sanity/  (16 files)
    check_api_docs.py
    check_dataproto_usage.py
    check_device_api_usage.py
    check_docs_time_info.py
    check_docstrings.py
    check_example_naming.py
    check_license.py
    check_pr_description.py
    check_pr_title.py
    check_uv_gpu_only.py
    test_check_example_naming.py
    test_config_docs.py
    test_import.py
    type_coverage_check.py
    validate_imported_docs.py
    validate_structure.py
  special_standalone/  (2 files)
    README.md
    test_memory_buffers.py
  tools/  (4 files)
    __init__.py
    _stub_search_tools.py
    test_function_tool_on_cpu.py
    test_mixed_tools_on_cpu.py
  trainer/  (31 files)
    ppo/  (28 files)
      … 28 files under this directory
    __init__.py
    test_constants_ppo_on_cpu.py
    test_multi_trajectories_advantage_on_cpu.py
  utils/  (93 files)
    ckpt/  (4 files)
      … 4 files under this directory
    dataset/  (4 files)
      … 4 files under this directory
    debug/  (1 files)
      … 1 files under this directory
    kernel/  (1 files)
      … 1 files under this directory
    megatron/  (8 files)
      … 8 files under this directory
    qat/  (5 files)
      … 5 files under this directory
    real_nvfp4/  (4 files)
      … 4 files under this directory
    reward_score/  (4 files)
      … 4 files under this directory
    _test_module.py
    test_activation_offload.py
    test_attention_utils.py
    test_audio_input_support_on_cpu.py
    test_bucketed_weight_transfer.py
    test_cann_linear_ce_on_cpu.py
    test_cann_linear_ce_on_npu.py
    test_check_ipc_version_support_on_npu.py
    test_check_profiler_output.py
    test_config_on_cpu.py
    test_config_router_replay_on_cpu.py
    test_continuous_token_check_on_cpu.py
    test_continuous_token_on_cpu.py
    test_dynamic_cp_scheduler.py
    test_experimental_torch_functional_on_cpu.py
    test_flops_counter.py
    test_fs_on_cpu.py
    test_fsdp2_model_transfer_on_cpu.py
    test_fsdp2_peft_wrapping.py
    test_fsdp_lora_merge.py
    test_fsdp_wrap_policy_on_cpu.py
    test_groupwise.py
    test_import_utils_on_cpu.py
    test_linear_cross_entropy.py
    … 38 more files
  README.md
  __init__.py
  kill_github_tests.sh
  test_base_config_on_cpu.py
  test_protocol_on_cpu.py
  test_protocol_v2_on_cpu.py
.dockerignore
.git-blame-ignore-revs
.gitignore
.gitmodules
.pre-commit-config.yaml
.readthedocs.yaml
AGENTS.md
CONTRIBUTING.md
LICENSE
Notice.txt
README.md
manage_envs.py
pyproject.toml
requirements-npu.txt
requirements-test.txt
requirements.txt
setup.py
```

## Entry points

- [manage_envs.py:945](https://github.com/verl-project/verl/blob/4191e7f910d85d69acb8c45f4840f10faa535165/manage_envs.py#L945)
- [scripts/chat_template_checker.py:1140](https://github.com/verl-project/verl/blob/4191e7f910d85d69acb8c45f4840f10faa535165/scripts/chat_template_checker.py#L1140)
- [scripts/converter_hf_to_mcore.py:113](https://github.com/verl-project/verl/blob/4191e7f910d85d69acb8c45f4840f10faa535165/scripts/converter_hf_to_mcore.py#L113)
- [scripts/diagnose.py:286](https://github.com/verl-project/verl/blob/4191e7f910d85d69acb8c45f4840f10faa535165/scripts/diagnose.py#L286)
- [scripts/init_random_model.py:100](https://github.com/verl-project/verl/blob/4191e7f910d85d69acb8c45f4840f10faa535165/scripts/init_random_model.py#L100)
- [scripts/legacy_model_merger.py:807](https://github.com/verl-project/verl/blob/4191e7f910d85d69acb8c45f4840f10faa535165/scripts/legacy_model_merger.py#L807)
- [scripts/megatron_merge_lora.py:126](https://github.com/verl-project/verl/blob/4191e7f910d85d69acb8c45f4840f10faa535165/scripts/megatron_merge_lora.py#L126)
- [scripts/migrate_megatron_checkpoint_layout.py:247](https://github.com/verl-project/verl/blob/4191e7f910d85d69acb8c45f4840f10faa535165/scripts/migrate_megatron_checkpoint_layout.py#L247)
- [scripts/print_cfg.py:34](https://github.com/verl-project/verl/blob/4191e7f910d85d69acb8c45f4840f10faa535165/scripts/print_cfg.py#L34)
- [scripts/rollout_logprob_diff.py:306](https://github.com/verl-project/verl/blob/4191e7f910d85d69acb8c45f4840f10faa535165/scripts/rollout_logprob_diff.py#L306)
- [scripts/rollout_viewer.py:552](https://github.com/verl-project/verl/blob/4191e7f910d85d69acb8c45f4840f10faa535165/scripts/rollout_viewer.py#L552)
- [scripts/veomni/moe_merge.py:116](https://github.com/verl-project/verl/blob/4191e7f910d85d69acb8c45f4840f10faa535165/scripts/veomni/moe_merge.py#L116)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 66 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 13 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Typer. Observed top-level classes: BaseModelMerger, CheckResult, CustomSaveWo… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| scripts package | library | Observed | Groups 6 file(s) under scripts package (observed from repository paths and static analysis). Observed top-level classes: SingleTurnTrajectory, ToolAgentTrajectory, TrajectoryStep, VLSingleTurnTrajectory, VLToolResponseS… |
| Tests | test | Observed | Groups 293 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH verl.trainer.ppo.metric_utils._compute_response_info, PATCH verl.trainer.ppo.metric_utils._compute_response_inf… |

## Important files

- `.dockerignore` (container)
- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/workflows/README.md` (ci)
- `.github/workflows/check-pr-title.yml` (ci)
- `.github/workflows/cpu_unit_tests.yml` (ci)
- `.github/workflows/doc.yml` (ci)
- `.github/workflows/docker-build-ascend-a2.yml` (ci)
- `.github/workflows/docker-build-ascend-a3.yml` (ci)
- `.github/workflows/docker-build-ascend-a5.yml` (ci)
- `.github/workflows/docker-build-ascend-sglang-a2.yml` (ci)
- `.github/workflows/docker-build-ascend-sglang-a3.yml` (ci)
- `.github/workflows/e2e_ascend.yml` (ci)
- `.github/workflows/e2e_ppo_grpo_trainer_trtllm.yml` (ci)
- `.github/workflows/e2e_ppo_trainer.yml` (ci)
- `.github/workflows/e2e_ppo_trainer_megatron_sglang.yml` (ci)
- `.github/workflows/e2e_ppo_trainer_megatron_sglang_2.yml` (ci)
- `.github/workflows/e2e_ppo_trainer_megatron_sglang_2_ascend.yml` (ci)
- `.github/workflows/e2e_ppo_trainer_megatron_sglang_ascend.yml` (ci)
- `.github/workflows/e2e_ppo_trainer_megatron_vllm.yml` (ci)
- `.github/workflows/e2e_ppo_trainer_megatron_vllm_2.yml` (ci)
- `.github/workflows/e2e_ppo_trainer_megatron_vllm_2_ascend.yml` (ci)
- `.github/workflows/e2e_ppo_trainer_megatron_vllm_ascend.yml` (ci)
- `.github/workflows/e2e_ppo_trainer_megatron_vllm_rocm.yml` (ci)
- `.github/workflows/e2e_ppo_trainer_torchtitan_vllm.yml` (ci)
- `.github/workflows/e2e_ppo_trainer_veomni_vllm.yml` (ci)
- `.github/workflows/e2e_ppo_trainer_veomni_vllm_ascend.yml` (ci)
- `.github/workflows/e2e_sft_llm.yml` (ci)
- `.github/workflows/e2e_sft_llm_ascend.yml` (ci)
- `.github/workflows/e2e_sft_vlm.yml` (ci)
- `.github/workflows/e2e_v1_separate_async.yml` (ci)
- `.github/workflows/e2e_v1_separate_async_ascend.yml` (ci)
- `.github/workflows/e2e_v1_separate_async_opd.yml` (ci)
- `.github/workflows/gpu_unit_tests.yml` (ci)
- `.github/workflows/model.yml` (ci)
- `.github/workflows/model_ascend.yml` (ci)
- `.github/workflows/nightly_ascend.yml` (ci)
- `.github/workflows/nightly_ascend_multinode.yml` (ci)
- `.github/workflows/npu_unit_tests.yml` (ci)
- `.github/workflows/pre-commit.yml` (ci)
- `.github/workflows/precommit-autofix.yml` (ci)
- `.github/workflows/reward_model_sglang.yml` (ci)
- `.github/workflows/reward_model_sglang_ascend.yml` (ci)
- `.github/workflows/reward_model_vllm.yml` (ci)
- `.github/workflows/reward_model_vllm_ascend.yml` (ci)
- `.github/workflows/sanity.yml` (ci)
- `.github/workflows/schedule_doc_translate_ascend.yaml` (ci)
- `.github/workflows/scorecard.yml` (ci)
- `.github/workflows/sgl.yml` (ci)
- `.github/workflows/sgl_ascend.yml` (ci)
- `.github/workflows/type-coverage-check.yml` (ci)
- `.github/workflows/vllm.yml` (ci)
- `.github/workflows/vllm_ascend.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `.readthedocs.yaml` (config)
- `.vscode/settings.json` (config)
- `docker/Dockerfile.isaaclab230` (container)
- `docker/Dockerfile.stable.sglang` (container)
- `docker/Dockerfile.stable.trtllm` (container)
- `docker/Dockerfile.stable.vllm` (container)
- `docker/Dockerfile.uv.cu130` (container)
- `docker/ascend/Dockerfile.ascend.sglang_8.3.rc1_a2` (container)
- `docker/ascend/Dockerfile.ascend.sglang_8.3.rc1_a3` (container)
- `docker/ascend/Dockerfile.ascend.sglang_8.5.0_a2` (container)
- `docker/ascend/Dockerfile.ascend.sglang_8.5.0_a3` (container)
- `docker/ascend/Dockerfile.ascend_8.2.rc1_a2` (container)
- `docker/ascend/Dockerfile.ascend_8.2.rc1_a3` (container)
- `docker/ascend/Dockerfile.ascend_8.3.rc1_a2` (container)
- `docker/ascend/Dockerfile.ascend_8.3.rc1_a3` (container)
- `docker/ascend/Dockerfile.ascend_8.5.0_a2` (container)
- `docker/ascend/Dockerfile.ascend_8.5.0_a2_v0.7.1` (container)
- `docker/ascend/Dockerfile.ascend_8.5.0_a3` (container)
- `docker/ascend/Dockerfile.ascend_8.5.0_a3_v0.7.1` (container)
- `docker/ascend/Dockerfile.ascend_8.5.2_a2_qwen3-5` (container)
- `docker/ascend/Dockerfile.ascend_8.5.2_a3_qwen3-5` (container)
- `docker/ascend/Dockerfile.ascend_9.0.0_a2_v0.8.0` (container)
- `docker/ascend/Dockerfile.ascend_9.0.0_a3_v0.8.0` (container)
- `docker/ascend/Dockerfile.ascend_9.1.0_a2` (container)
- `docker/ascend/Dockerfile.ascend_9.1.0_a2_v0.9.1` (container)
- `docker/ascend/Dockerfile.ascend_9.1.0_a3` (container)
- `docker/ascend/Dockerfile.ascend_9.1.0_a3_v0.9.1` (container)
- `docker/ascend/Dockerfile.ascend_9.1.0_a5` (container)
- `docker/ascend/Dockerfile.ascend_9.1.0_a5_v0.9.1` (container)
- `docker/ascend/Dockerfile.ascend_9.2.1_a2` (container)
- `docker/ascend/Dockerfile.ascend_9.2.1_a3` (container)
- `docker/ascend/Dockerfile.ascend_9.2.1_a5` (container)
- `docker/aws/Dockerfile.extention.awsefa` (container)
- `docker/aws/Dockerfile.ngc.vllm0.8.sagemaker` (container)
- `docker/rocm/Dockerfile.rocm` (container)
- `docker/rocm/Dockerfile.rocm.deepseek-v4` (container)
- `docker/rocm/Dockerfile.rocm6` (container)
- `docker/rocm/Dockerfile.rocm702` (container)
- `docker/rocm/Dockerfile.rocm_verl-0.3.0.post1` (container)
- `docker/rocm/Dockerfile.rocm_verl-0.4.1` (container)
- `docker/verl0.4-cu124-torch2.6-fa2.7.4/Dockerfile.app.sglang.vllm.mcore0.12` (container)
- `docker/verl0.4-cu124-torch2.6-fa2.7.4/Dockerfile.app.sglang.vllm.mcore0.12.deepep` (container)
- `docker/verl0.4-cu124-torch2.6-fa2.7.4/Dockerfile.app.sglang.vllm.mcore0.13.preview` (container)
- `docker/verl0.4-cu124-torch2.6-fa2.7.4/Dockerfile.app.vllm.mcore0.12` (container)
- `docker/verl0.4-cu124-torch2.6-fa2.7.4/Dockerfile.app.vllm.mcore0.12.deepep` (container)
- `docker/verl0.4-cu124-torch2.6-fa2.7.4/Dockerfile.app.vllm.mcore0.13.preview` (container)
- `docker/verl0.4-cu124-torch2.6-fa2.7.4/Dockerfile.base` (container)
- `docker/verl0.5-cu126-torch2.7-fa2.7.4/Dockerfile.app.sglang0.4.10.post2.mcore0.13` (container)
- `docker/verl0.5-cu126-torch2.7-fa2.7.4/Dockerfile.app.sglang0.4.9.post6.mcore0.13` (container)
- `docker/verl0.5-cu126-torch2.7-fa2.7.4/Dockerfile.app.vllm.mcore0.13` (container)
- `docker/verl0.5-cu126-torch2.7-fa2.7.4/Dockerfile.app.vllm.mcore0.15` (container)
- `docker/verl0.5-cu126-torch2.7-fa2.7.4/Dockerfile.base.torch2.7.1` (container)
- `docker/verl0.5-cu126-torch2.7.1-fa2.8.0/Dockerfile.app.sglang.mcore0.12` (container)
- `docker/verl0.5-cu126-torch2.7.1-fa2.8.0/Dockerfile.app.sglang.mcore0.13.preview` (container)
- `docker/verl0.5-cu126-torch2.7.1-fa2.8.0/Dockerfile.base` (container)
- `docker/verl0.5-preview-cu128-torch2.7.1-fa2.8.0/Dockerfile.app.sglang.megatron` (container)
- `docker/verl0.5-preview-cu128-torch2.7.1-fa2.8.0/Dockerfile.base` (container)
- `docker/verl0.6-cu128-torch2.8.0-fa2.7.4/Dockerfile.app.sglang` (container)
- `docker/verl0.6-cu128-torch2.8.0-fa2.7.4/Dockerfile.base` (container)
- `docker/verl0.6-cu128-torch2.8.0-fa2.7.4/Dockerfile.vllm011.mcore_gpt-oss` (container)
- `docker/verl0.6.1-experimental/Dockerfile.sglang056exp` (container)
- `docker/verl0.6.1-experimental/Dockerfile.vllm012exp` (container)
- `docker/xpu/Dockerfile.stable.vllm` (container)
- `docs/ascend_tutorial/en/get_start/dockerfile_build_guidance.rst` (container)
- `docs/ascend_tutorial/zh/get_start/dockerfile_build_guidance.rst` (container)
- `docs/requirements-docs.txt` (manifest)
- `examples/real_nvfp4/runtime_env.yaml` (config)
- `examples/tpu/grpo/Dockerfile` (container)
- `examples/tpu/grpo/ray-tpu-v6e-2slice.yaml` (config)
- `examples/tutorial/skypilot/verl-grpo.yaml` (config)
- `examples/tutorial/skypilot/verl-ppo.yaml` (config)
- `pyproject.toml` (manifest)
- `requirements-npu.txt` (manifest)
- `requirements-test.txt` (manifest)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `tests` — 293 analysed file(s)
- `examples` — 179 analysed file(s)
- `docs` — 156 analysed file(s)
- `docker` — 76 analysed file(s)
- `.github` — 56 analysed file(s)
- `scripts` — 18 analysed file(s)
- `(root files)` — 17 analysed file(s)
- `.agent` — 3 analysed file(s)
- `.vscode` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `4191e7f910d85d69acb8c45f4840f10faa535165` is the revision these paths and observations refer to.
