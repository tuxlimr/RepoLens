# Project structure: pytorch/examples

**Analysed commit:** `acc295dc7b90714f1bf47f06004fc19a7fe235c4`

**Commit reference:** [acc295dc7b90714f1bf47f06004fc19a7fe235c4](https://github.com/pytorch/examples/commit/acc295dc7b90714f1bf47f06004fc19a7fe235c4)

**Tree at this commit:** [pytorch/examples@acc295dc7b90](https://github.com/pytorch/examples/tree/acc295dc7b90714f1bf47f06004fc19a7fe235c4)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pytorch/examples |
| Description | A set of examples around pytorch in Vision, Text, Reinforcement Learning, etc. |
| Stars | 24094 |
| Forks | 9803 |
| Licence | BSD-3-Clause |
| Language | Python |
| Default branch | main |
| Analysed commit | `acc295dc7b90714f1bf47f06004fc19a7fe235c4` |
| Retrieved at | 2026-11-14T19:07:43.633211+00:00 |
| Files in this snapshot | 223 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (3 files)
    bug_template.md
    doc_template.md
    feature_template.md
  PULL_REQUEST_TEMPLATE/  (1 files)
    pull_request_template.md
  workflows/  (4 files)
    doc-build.yml
    main_cpp.yml
    main_distributed.yaml
    main_python.yml
cpp/  (28 files)
  autograd/  (3 files)
    CMakeLists.txt
    README.md
    autograd.cpp
  custom-dataset/  (3 files)
    CMakeLists.txt
    README.md
    custom-dataset.cpp
  dcgan/  (4 files)
    CMakeLists.txt
    README.md
    dcgan.cpp
    display_samples.py
  distributed/  (3 files)
    CMakeLists.txt
    README.md
    dist-mnist.cpp
  mnist/  (3 files)
    CMakeLists.txt
    README.md
    mnist.cpp
  regression/  (3 files)
    CMakeLists.txt
    README.md
    regression.cpp
  tools/  (2 files)
    InstallingOpenCV.md
    download_mnist.py
  transfer-learning/  (6 files)
    CMakeLists.txt
    README.md
    classify.cpp
    convert.py
    main.cpp
    main.h
  .clang-format
dcgan/  (3 files)
  README.md
  main.py
  requirements.txt
distributed/  (78 files)
  FSDP/  (18 files)
    configs/  (3 files)
      … 3 files under this directory
    model_checkpointing/  (2 files)
      … 2 files under this directory
    policies/  (4 files)
      … 4 files under this directory
    utils/  (3 files)
      … 3 files under this directory
    .gitignore
    README.md
    T5_training.py
    download_dataset.sh
    requirements.txt
    summarization_dataset.py
  FSDP2/  (7 files)
    README.md
    checkpoint.py
    example.py
    model.py
    requirements.txt
    run_example.sh
    utils.py
  ddp/  (4 files)
    README.md
    example.py
    requirements.txt
    run_example.sh
  ddp-tutorial-series/  (10 files)
    slurm/  (3 files)
      … 3 files under this directory
    README.md
    datautils.py
    multigpu.py
    multigpu_torchrun.py
    multinode.py
    requirements.txt
    single_gpu.py
  minGPT-ddp/  (11 files)
    mingpt/  (8 files)
      … 8 files under this directory
    README.md
    requirements.txt
    run_example.sh
  rpc/  (20 files)
    batch/  (4 files)
      … 4 files under this directory
    ddp_rpc/  (3 files)
      … 3 files under this directory
    parameter_server/  (3 files)
      … 3 files under this directory
    pipeline/  (3 files)
      … 3 files under this directory
    rl/  (3 files)
      … 3 files under this directory
    rnn/  (4 files)
      … 4 files under this directory
  tensor_parallelism/  (8 files)
    README.md
    fsdp_tp_example.py
    llama2_model.py
    log_utils.py
    requirements.txt
    run_example.sh
    sequence_parallel_example.py
    tensor_parallel_example.py
docs/  (6 files)
  source/  (3 files)
    _static/  (1 files)
      … 1 files under this directory
    conf.py
    index.rst
  Makefile
  make.bat
  requirements.txt
fast_neural_style/  (8 files)
  neural_style/  (5 files)
    __init__.py
    neural_style.py
    transformer_net.py
    utils.py
    vgg.py
  README.md
  download_saved_models.py
  requirements.txt
fx/  (16 files)
  native_interpreter/  (4 files)
    CMakeLists.txt
    README.md
    interpreter.cpp
    use_interpreter.py
  README.md
  custom_tracer.py
  inline_function.py
  invert.py
  module_tracer.py
  primitive_library.py
  profiling_tracer.py
  proxy_based_graph_creation.py
  replace_op.py
  requirements.txt
  subgraph_rewriter_basic_use.py
  wrap_output_dynamically.py
gat/  (3 files)
  README.md
  main.py
  requirements.txt
gcn/  (3 files)
  README.md
  main.py
  requirements.txt
imagenet/  (4 files)
  README.md
  extract_ILSVRC.sh
  main.py
  requirements.txt
language_translation/  (5 files)
  src/  (2 files)
    data.py
    model.py
  README.md
  main.py
  requirements.txt
legacy/  (5 files)
  snli/  (5 files)
    README.md
    model.py
    requirements.txt
    train.py
    util.py
mnist/  (3 files)
  README.md
  main.py
  requirements.txt
mnist_forward_forward/  (3 files)
  README.md
  main.py
  requirements.txt
mnist_hogwild/  (4 files)
  README.md
  main.py
  requirements.txt
  train.py
mnist_rnn/  (3 files)
  README.md
  main.py
  requirements.txt
regression/  (3 files)
  README.md
  main.py
  requirements.txt
reinforcement_learning/  (4 files)
  README.md
  actor_critic.py
  reinforce.py
  requirements.txt
siamese_network/  (3 files)
  README.md
  main.py
  requirements.txt
super_resolution/  (7 files)
  README.md
  data.py
  dataset.py
  main.py
  model.py
  requirements.txt
  super_resolve.py
time_sequence_prediction/  (4 files)
  README.md
  generate_sine_wave.py
  requirements.txt
  train.py
vae/  (4 files)
  results/  (1 files)
    .gitignore
  README.md
  main.py
  requirements.txt
word_language_model/  (7 files)
  data/  (1 files)
    wikitext-2/  (1 files)
      … 1 files under this directory
  README.md
  data.py
  generate.py
  main.py
  model.py
  requirements.txt
.gitignore
CODEOWNERS
CODE_OF_CONDUCT.md
CONTRIBUTING.md
LICENSE
README.md
run_cpp_examples.sh
run_distributed_examples.sh
run_python_examples.sh
runtime.txt
utils.sh
```

## Entry points

- [language_translation/src/data.py:120](https://github.com/pytorch/examples/blob/acc295dc7b90714f1bf47f06004fc19a7fe235c4/language_translation/src/data.py#L120)
- [cpp/tools/download_mnist.py:88](https://github.com/pytorch/examples/blob/acc295dc7b90714f1bf47f06004fc19a7fe235c4/cpp/tools/download_mnist.py#L88)
- [distributed/FSDP/T5_training.py:198](https://github.com/pytorch/examples/blob/acc295dc7b90714f1bf47f06004fc19a7fe235c4/distributed/FSDP/T5_training.py#L198)
- [distributed/FSDP2/example.py:111](https://github.com/pytorch/examples/blob/acc295dc7b90714f1bf47f06004fc19a7fe235c4/distributed/FSDP2/example.py#L111)
- [distributed/ddp-tutorial-series/multigpu.py:95](https://github.com/pytorch/examples/blob/acc295dc7b90714f1bf47f06004fc19a7fe235c4/distributed/ddp-tutorial-series/multigpu.py#L95)
- [distributed/ddp-tutorial-series/multigpu_torchrun.py:103](https://github.com/pytorch/examples/blob/acc295dc7b90714f1bf47f06004fc19a7fe235c4/distributed/ddp-tutorial-series/multigpu_torchrun.py#L103)
- [distributed/ddp-tutorial-series/multinode.py:104](https://github.com/pytorch/examples/blob/acc295dc7b90714f1bf47f06004fc19a7fe235c4/distributed/ddp-tutorial-series/multinode.py#L104)
- [distributed/ddp-tutorial-series/single_gpu.py:73](https://github.com/pytorch/examples/blob/acc295dc7b90714f1bf47f06004fc19a7fe235c4/distributed/ddp-tutorial-series/single_gpu.py#L73)
- [distributed/ddp/example.py:96](https://github.com/pytorch/examples/blob/acc295dc7b90714f1bf47f06004fc19a7fe235c4/distributed/ddp/example.py#L96)
- [distributed/minGPT-ddp/mingpt/main.py:52](https://github.com/pytorch/examples/blob/acc295dc7b90714f1bf47f06004fc19a7fe235c4/distributed/minGPT-ddp/mingpt/main.py#L52)
- [distributed/rpc/batch/parameter_server.py:156](https://github.com/pytorch/examples/blob/acc295dc7b90714f1bf47f06004fc19a7fe235c4/distributed/rpc/batch/parameter_server.py#L156)
- [distributed/rpc/batch/reinforce.py:261](https://github.com/pytorch/examples/blob/acc295dc7b90714f1bf47f06004fc19a7fe235c4/distributed/rpc/batch/reinforce.py#L261)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 35 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: fsdp_config, train_config. |
| Core modules | core | Observed | Groups 4 file(s) under core modules (observed from repository paths and static analysis). |
| cpp package | library | Observed | Groups 11 file(s) under cpp package (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 6 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Attention, Block, Bottle, EmbeddingStem, Encoder, FeedForward. Observed top-level functions: create_opt… |
| distributed package | library | Observed | Groups 28 file(s) under distributed package (observed from repository paths and static analysis). Observed top-level classes: Attention, CharDataset, Checkpointer, DataConfig, Decoder, EmbeddingTable. Observed top-level… |
| Application entry point | entrypoint | Observed | Groups 36 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: APP_MATCHER, Agent, AverageMeter, BatchUpdateParameterServer, Discriminator, DistResNet50… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| fast_neural_style package | library | Observed | Groups 4 file(s) under fast_neural_style package (observed from repository paths and static analysis). Observed top-level classes: ConvLayer, ResidualBlock, TransformerNet, UpsampleConvLayer, Vgg16. Observed top-level f… |
| fx package | library | Observed | Groups 12 file(s) under fx package (observed from repository paths and static analysis). Observed top-level classes: ActivationFunction, Foo, InliningTracer, LowerReluTracer, M, M1. Observed top-level functions: add_inv… |
| imagenet package | library | Observed | Groups 1 file(s) under imagenet package (observed from repository paths and static analysis). |
| legacy package | library | Observed | Groups 2 file(s) under legacy package (observed from repository paths and static analysis). Observed top-level functions: get_args, makedirs. |
| mnist_hogwild package | library | Observed | Groups 1 file(s) under mnist_hogwild package (observed from repository paths and static analysis). Observed top-level functions: test, test_epoch, train, train_epoch. |
| super_resolution package | library | Observed | Groups 3 file(s) under super_resolution package (observed from repository paths and static analysis). Observed top-level classes: DatasetFromFolder. Observed top-level functions: calculate_valid_crop_size, download_bsd3… |
| time_sequence_prediction package | library | Observed | Groups 1 file(s) under time_sequence_prediction package (observed from repository paths and static analysis). |
| word_language_model package | library | Observed | Groups 2 file(s) under word_language_model package (observed from repository paths and static analysis). Observed top-level classes: Corpus, Dictionary. |

## Important files

- `.github/workflows/doc-build.yml` (ci)
- `.github/workflows/main_cpp.yml` (ci)
- `.github/workflows/main_distributed.yaml` (ci)
- `.github/workflows/main_python.yml` (ci)
- `dcgan/requirements.txt` (manifest)
- `distributed/FSDP/requirements.txt` (manifest)
- `distributed/FSDP2/requirements.txt` (manifest)
- `distributed/ddp-tutorial-series/requirements.txt` (manifest)
- `distributed/ddp/requirements.txt` (manifest)
- `distributed/minGPT-ddp/mingpt/gpt2_train_cfg.yaml` (config)
- `distributed/minGPT-ddp/requirements.txt` (manifest)
- `distributed/rpc/batch/requirements.txt` (manifest)
- `distributed/rpc/ddp_rpc/requirements.txt` (manifest)
- `distributed/rpc/parameter_server/requirements.txt` (manifest)
- `distributed/rpc/pipeline/requirements.txt` (manifest)
- `distributed/rpc/rl/requirements.txt` (manifest)
- `distributed/rpc/rnn/requirements.txt` (manifest)
- `distributed/tensor_parallelism/requirements.txt` (manifest)
- `docs/requirements.txt` (manifest)
- `fast_neural_style/requirements.txt` (manifest)
- `fx/requirements.txt` (manifest)
- `gat/requirements.txt` (manifest)
- `gcn/requirements.txt` (manifest)
- `imagenet/requirements.txt` (manifest)
- `language_translation/requirements.txt` (manifest)
- `legacy/snli/requirements.txt` (manifest)
- `mnist/requirements.txt` (manifest)
- `mnist_forward_forward/requirements.txt` (manifest)
- `mnist_hogwild/requirements.txt` (manifest)
- `mnist_rnn/requirements.txt` (manifest)
- `regression/requirements.txt` (manifest)
- `reinforcement_learning/requirements.txt` (manifest)
- `siamese_network/requirements.txt` (manifest)
- `super_resolution/requirements.txt` (manifest)
- `time_sequence_prediction/requirements.txt` (manifest)
- `vae/requirements.txt` (manifest)
- `word_language_model/requirements.txt` (manifest)

## Top-level layout

- `distributed` — 78 analysed file(s)
- `cpp` — 28 analysed file(s)
- `fx` — 16 analysed file(s)
- `(root files)` — 11 analysed file(s)
- `.github` — 8 analysed file(s)
- `fast_neural_style` — 8 analysed file(s)
- `super_resolution` — 7 analysed file(s)
- `word_language_model` — 7 analysed file(s)
- `docs` — 6 analysed file(s)
- `language_translation` — 5 analysed file(s)
- `legacy` — 5 analysed file(s)
- `imagenet` — 4 analysed file(s)
- `mnist_hogwild` — 4 analysed file(s)
- `reinforcement_learning` — 4 analysed file(s)
- `time_sequence_prediction` — 4 analysed file(s)
- `vae` — 4 analysed file(s)
- `dcgan` — 3 analysed file(s)
- `gat` — 3 analysed file(s)
- `gcn` — 3 analysed file(s)
- `mnist` — 3 analysed file(s)
- `mnist_forward_forward` — 3 analysed file(s)
- `mnist_rnn` — 3 analysed file(s)
- `regression` — 3 analysed file(s)
- `siamese_network` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `acc295dc7b90714f1bf47f06004fc19a7fe235c4` is the revision these paths and observations refer to.
