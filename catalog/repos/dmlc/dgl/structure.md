# Project structure: dmlc/dgl

**Analysed commit:** `3d16000b4170fa741ed9e9667f22ba84d3493026`

**Commit reference:** [3d16000b4170fa741ed9e9667f22ba84d3493026](https://github.com/dmlc/dgl/commit/3d16000b4170fa741ed9e9667f22ba84d3493026)

**Tree at this commit:** [dmlc/dgl@3d16000b4170](https://github.com/dmlc/dgl/tree/3d16000b4170fa741ed9e9667f22ba84d3493026)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | dmlc/dgl |
| Description | Python package built to ease deep learning on graph, on top of existing DL frameworks. |
| Stars | 14290 |
| Forks | 3059 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `3d16000b4170fa741ed9e9667f22ba84d3493026` |
| Retrieved at | 2026-11-14T19:09:29.868000+00:00 |
| Files in this snapshot | 793 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (5 files)
    --work-item--dev-only-.md
    bug-report.md
    documentation.md
    feature-request.md
    questions-help-support.md
  workflows/  (2 files)
    lint.yml
    stale.yml
  PULL_REQUEST_TEMPLATE.md
apps/  (1 files)
  life_sci/  (1 files)
    README.md
benchmarks/  (79 files)
  benchmarks/  (65 files)
    api/  (34 files)
      … 34 files under this directory
    kernel/  (5 files)
      … 5 files under this directory
    model_acc/  (8 files)
      … 8 files under this directory
    model_speed/  (11 files)
      … 11 files under this directory
    multigpu/  (4 files)
      … 4 files under this directory
    __init__.py
    rgcn.py
    utils.py
  scripts/  (8 files)
    README.md
    build_dgl_asv.sh
    fix_ram_info.py
    generate_excel.py
    install_dgl_asv.sh
    publish.sh
    replace_branch.py
    torch_gpu_pip.txt
  .gitignore
  Jenkinsfile
  README.md
  asv.conf.json
  run.sh
  task.json
cmake/  (5 files)
  modules/  (2 files)
    CUDA.cmake
    FindMETIS.cmake
  util/  (3 files)
    FindCUDA.cmake
    MshadowUtil.cmake
    Util.cmake
conda/  (7 files)
  dgl/  (7 files)
    README.md
    bld.bat
    build.sh
    conda_build_config.yaml
    meta.yaml
    run_test.bat
    run_test.sh
dgl_sparse/  (30 files)
  include/  (10 files)
    sparse/  (10 files)
      … 10 files under this directory
  src/  (16 files)
    cpu/  (1 files)
      … 1 files under this directory
    elemenwise_op.cc
    matmul.cc
    matmul.h
    matrix_ops.cc
    matrix_ops_impl.h
    python_binding.cc
    reduction.cc
    sddmm.cc
    softmax.cc
    sparse_format.cc
    sparse_matrix.cc
    sparse_matrix_coalesce.cc
    spmm.cc
    spspmm.cc
    utils.h
  CMakeLists.txt
  build.bat
  build.sh
  find_cmake.py
dglgo/  (75 files)
  dglgo/  (52 files)
    apply_pipeline/  (10 files)
      … 10 files under this directory
    cli/  (8 files)
      … 8 files under this directory
    model/  (14 files)
      … 14 files under this directory
    pipeline/  (13 files)
      … 13 files under this directory
    utils/  (6 files)
      … 6 files under this directory
    __init__.py
  recipes/  (18 files)
    __init__.py
    graphpred_hiv_gin.yaml
    graphpred_hiv_pna.yaml
    graphpred_pcba_gin.yaml
    linkpred_citation2_sage.yaml
    linkpred_collab_sage.yaml
    linkpred_cora_sage.yaml
    nodepred-ns_arxiv_gcn.yaml
    nodepred-ns_product_sage.yaml
    nodepred_citeseer_gat.yaml
    nodepred_citeseer_gcn.yaml
    nodepred_citeseer_sage.yaml
    nodepred_cora_gat.yaml
    nodepred_cora_gcn.yaml
    nodepred_cora_sage.yaml
    nodepred_pubmed_gat.yaml
    nodepred_pubmed_gcn.yaml
    nodepred_pubmed_sage.yaml
  tests/  (3 files)
    cfg.yml
    run_test.sh
    test_pipeline.py
  README.md
  setup.py
docker/  (32 files)
  install/  (21 files)
    conda_env/  (10 files)
      … 10 files under this directory
    ubuntu_install_antlr.sh
    ubuntu_install_build.sh
    ubuntu_install_conda.sh
    ubuntu_install_core.sh
    ubuntu_install_java.sh
    ubuntu_install_mxnet_cpu.sh
    ubuntu_install_mxnet_gpu.sh
    ubuntu_install_python.sh
    ubuntu_install_python_package.sh
    ubuntu_install_torch.sh
    ubuntu_install_torch_1.2.0.sh
  pods/  (5 files)
    ci-compile-cpu.yaml
    ci-compile-gpu.yaml
    ci-cpu.yaml
    ci-gpu.yaml
    ci-lint.yaml
  Dockerfile.awscli
  Dockerfile.ci_benchmark
  Dockerfile.ci_cpu
  Dockerfile.ci_gpu
  Dockerfile.ci_lint
  README.md
docs/  (188 files)
  source/  (183 files)
    _static/  (1 files)
      … 1 files under this directory
    _templates/  (2 files)
      … 2 files under this directory
    api/  (21 files)
      … 21 files under this directory
    developer/  (1 files)
      … 1 files under this directory
    features/  (1 files)
      … 1 files under this directory
    graphtransformer/  (3 files)
      … 3 files under this directory
    guide/  (47 files)
      … 47 files under this directory
    guide_cn/  (40 files)
      … 40 files under this directory
    guide_ko/  (43 files)
      … 43 files under this directory
    install/  (1 files)
      … 1 files under this directory
    notebooks/  (6 files)
      … 6 files under this directory
    stochastic_training/  (9 files)
      … 9 files under this directory
    conf.py
    contribute.rst
    env_var.rst
    faq.rst
    gen_dataset_stat.py
    index.rst
    performance.rst
    resources.rst
  .gitignore
  Makefile
  README.md
  clean.sh
  migrate-guide-0.5.md
examples/  (358 files)
  advanced/  (2 files)
    cugraph/  (2 files)
      … 2 files under this directory
  core/  (11 files)
    Graphormer/  (4 files)
      … 4 files under this directory
    gat/  (2 files)
      … 2 files under this directory
    gated_gcn/  (2 files)
      … 2 files under this directory
    graphsage/  (1 files)
      … 1 files under this directory
    rgcn/  (2 files)
      … 2 files under this directory
  distributed/  (8 files)
    graphsage/  (4 files)
      … 4 files under this directory
    rgcn/  (4 files)
      … 4 files under this directory
  graphbolt/  (24 files)
    disk_based_feature/  (2 files)
      … 2 files under this directory
    lightning/  (2 files)
      … 2 files under this directory
    pyg/  (10 files)
      … 10 files under this directory
    quickstart/  (3 files)
      … 3 files under this directory
    rgcn/  (2 files)
      … 2 files under this directory
    sparse/  (1 files)
      … 1 files under this directory
    README.md
    link_prediction.py
    node_classification.py
    temporal_link_prediction.py
  legacy/  (3 files)
    README.md
    link_prediction.py
    node_classification.py
  multigpu/  (4 files)
    graphbolt/  (2 files)
      … 2 files under this directory
    README.md
    node_classification_sage.py
  mxnet/  (54 files)
    appnp/  (2 files)
      … 2 files under this directory
    gat/  (4 files)
      … 4 files under this directory
    gcn/  (5 files)
      … 5 files under this directory
    gin/  (5 files)
      … 5 files under this directory
    graphsage/  (2 files)
      … 2 files under this directory
    monet/  (2 files)
      … 2 files under this directory
    rgcn/  (3 files)
      … 3 files under this directory
    scenegraph/  (22 files)
      … 22 files under this directory
    sgc/  (2 files)
      … 2 files under this directory
    tagcn/  (3 files)
      … 3 files under this directory
    tree_lstm/  (3 files)
      … 3 files under this directory
    README.md
  pytorch/  (251 files)
    GATNE-T/  (9 files)
      … 9 files under this directory
    GNN-FiLM/  (4 files)
      … 4 files under this directory
    NGCF/  (10 files)
      … 10 files under this directory
    P-GNN/  (4 files)
      … 4 files under this directory
    TAHIN/  (5 files)
      … 5 files under this directory
    appnp/  (3 files)
      … 3 files under this directory
    argo/  (5 files)
      … 5 files under this directory
    arma/  (3 files)
      … 3 files under this directory
    bgnn/  (3 files)
      … 3 files under this directory
    bgrl/  (5 files)
      … 5 files under this directory
    capsule/  (6 files)
      … 6 files under this directory
    caregnn/  (6 files)
      … 6 files under this directory
    cluster_gcn/  (2 files)
      … 2 files under this directory
    compGCN/  (7 files)
      … 7 files under this directory
    correct_and_smooth/  (3 files)
      … 3 files under this directory
    dagnn/  (3 files)
      … 3 files under this directory
    deepergcn/  (5 files)
      … 5 files under this directory
    deepwalk/  (1 files)
      … 1 files under this directory
    dgi/  (4 files)
      … 4 files under this directory
    dgmg/  (6 files)
      … 6 files under this directory
    diffpool/  (15 files)
      … 15 files under this directory
    dimenet/  (21 files)
      … 21 files under this directory
    dtgrnn/  (7 files)
      … 7 files under this directory
    eeg-gcnn/  (5 files)
      … 5 files under this directory
    eges/  (6 files)
      … 6 files under this directory
    evolveGCN/  (5 files)
      … 5 files under this directory
    gas/  (6 files)
      … 6 files under this directory
    gat/  (3 files)
      … 3 files under this directory
    gatv2/  (3 files)
      … 3 files under this directory
    gcmc/  (6 files)
      … 6 files under this directory
    gcn/  (2 files)
      … 2 files under this directory
    geniepath/  (4 files)
      … 4 files under this directory
    ggnn/  (8 files)
      … 8 files under this directory
    gin/  (2 files)
      … 2 files under this directory
    gnn_explainer/  (9 files)
      … 9 files under this directory
    grace/  (6 files)
      … 6 files under this directory
    grand/  (3 files)
      … 3 files under this directory
    graph_matching/  (3 files)
      … 3 files under this directory
    graphsage/  (10 files)
      … 10 files under this directory
    graphsaint/  (6 files)
      … 6 files under this directory
    graphsim/  (6 files)
      … 6 files under this directory
    graphwriter/  (9 files)
      … 9 files under this directory
    gxn/  (9 files)
      … 9 files under this directory
    han/  (3 files)
      … 3 files under this directory
  README.md
.clang-format
.gitignore
.gitmodules
.lintrunner.toml
CMakeLists.txt
CONTRIBUTORS.md
Jenkinsfile
LICENSE
NEWS.md
README.md
```

## Entry points

- [benchmarks/benchmarks/multigpu/bench_multigpu_rgcn.py:564](https://github.com/dmlc/dgl/blob/3d16000b4170fa741ed9e9667f22ba84d3493026/benchmarks/benchmarks/multigpu/bench_multigpu_rgcn.py#L564)
- [benchmarks/scripts/replace_branch.py:80](https://github.com/dmlc/dgl/blob/3d16000b4170fa741ed9e9667f22ba84d3493026/benchmarks/scripts/replace_branch.py#L80)
- [dglgo/dglgo/cli/__init__.py:3](https://github.com/dmlc/dgl/blob/3d16000b4170fa741ed9e9667f22ba84d3493026/dglgo/dglgo/cli/__init__.py#L3)
- [dglgo/dglgo/cli/cli.py:12](https://github.com/dmlc/dgl/blob/3d16000b4170fa741ed9e9667f22ba84d3493026/dglgo/dglgo/cli/cli.py#L12)
- [dglgo/dglgo/cli/config_apply_cli.py:6](https://github.com/dmlc/dgl/blob/3d16000b4170fa741ed9e9667f22ba84d3493026/dglgo/dglgo/cli/config_apply_cli.py#L6)
- [dglgo/dglgo/cli/config_cli.py:11](https://github.com/dmlc/dgl/blob/3d16000b4170fa741ed9e9667f22ba84d3493026/dglgo/dglgo/cli/config_cli.py#L11)
- [dglgo/dglgo/cli/export_cli.py:41](https://github.com/dmlc/dgl/blob/3d16000b4170fa741ed9e9667f22ba84d3493026/dglgo/dglgo/cli/export_cli.py#L41)
- [dglgo/dglgo/cli/recipe_cli.py:70](https://github.com/dmlc/dgl/blob/3d16000b4170fa741ed9e9667f22ba84d3493026/dglgo/dglgo/cli/recipe_cli.py#L70)
- [dglgo/dglgo/cli/train_cli.py:28](https://github.com/dmlc/dgl/blob/3d16000b4170fa741ed9e9667f22ba84d3493026/dglgo/dglgo/cli/train_cli.py#L28)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| API layer | api | Observed | Groups 34 file(s) under api layer (observed from repository paths and static analysis). Observed top-level functions: _node2vec, _random_walk, track_time. |
| benchmarks package | library | Observed | Groups 36 file(s) under benchmarks package (observed from repository paths and static analysis). Observed top-level classes: BagOfWords, BagOfWordsPretrained, BaseRGCN, CrossEntropyLoss, EntityClassify, GAT. Observed to… |
| conda package | library | Observed | Groups 2 file(s) under conda package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 40 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| dgl_sparse package | library | Observed | Groups 15 file(s) under dgl_sparse package (observed from repository paths and static analysis). |
| dglgo package | library | Observed | Groups 39 file(s) under dglgo package (observed from repository paths and static analysis). Observed top-level classes: ApplyGraphpredPipeline, ApplyGraphpredPipelineCfg, ApplyNodepredNsPipeline, ApplyNodepredPipeline,… |
| docker package | library | Observed | Groups 11 file(s) under docker package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 9 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Typer. Observed top-level classes: EntityClassify, NeighborSampler. Observed t… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 4 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: ExperimentSpec. Observed top-level functions: get_auc, get_performance, ranklist_by_heapq, ranklist_by_sorte… |

## Important files

- `.github/workflows/lint.yml` (ci)
- `.github/workflows/stale.yml` (ci)
- `.lintrunner.toml` (config)
- `benchmarks/asv.conf.json` (config)
- `benchmarks/task.json` (config)
- `conda/dgl/conda_build_config.yaml` (config)
- `conda/dgl/meta.yaml` (config)
- `dglgo/recipes/graphpred_hiv_gin.yaml` (config)
- `dglgo/recipes/graphpred_hiv_pna.yaml` (config)
- `dglgo/recipes/graphpred_pcba_gin.yaml` (config)
- `dglgo/recipes/linkpred_citation2_sage.yaml` (config)
- `dglgo/recipes/linkpred_collab_sage.yaml` (config)
- `dglgo/recipes/linkpred_cora_sage.yaml` (config)
- `dglgo/recipes/nodepred-ns_arxiv_gcn.yaml` (config)
- `dglgo/recipes/nodepred-ns_product_sage.yaml` (config)
- `dglgo/recipes/nodepred_citeseer_gat.yaml` (config)
- `dglgo/recipes/nodepred_citeseer_gcn.yaml` (config)
- `dglgo/recipes/nodepred_citeseer_sage.yaml` (config)
- `dglgo/recipes/nodepred_cora_gat.yaml` (config)
- `dglgo/recipes/nodepred_cora_gcn.yaml` (config)
- `dglgo/recipes/nodepred_cora_sage.yaml` (config)
- `dglgo/recipes/nodepred_pubmed_gat.yaml` (config)
- `dglgo/recipes/nodepred_pubmed_gcn.yaml` (config)
- `dglgo/recipes/nodepred_pubmed_sage.yaml` (config)
- `dglgo/setup.py` (manifest)
- `docker/Dockerfile.awscli` (container)
- `docker/Dockerfile.ci_benchmark` (container)
- `docker/Dockerfile.ci_cpu` (container)
- `docker/Dockerfile.ci_gpu` (container)
- `docker/Dockerfile.ci_lint` (container)
- `docker/install/conda_env/kg_cpu.yml` (config)
- `docker/install/conda_env/kg_gpu.yml` (config)
- `docker/install/conda_env/mxnet_cpu.yml` (config)
- `docker/install/conda_env/mxnet_gpu.yml` (config)
- `docker/install/conda_env/tensorflow_cpu.yml` (config)
- `docker/install/conda_env/tensorflow_gpu.yml` (config)
- `docker/install/conda_env/torch_cpu.yml` (config)
- `docker/install/conda_env/torch_gpu.yml` (config)
- `docker/pods/ci-compile-cpu.yaml` (config)
- `docker/pods/ci-compile-gpu.yaml` (config)
- `docker/pods/ci-cpu.yaml` (config)
- `docker/pods/ci-gpu.yaml` (config)
- `docker/pods/ci-lint.yaml` (config)
- `examples/pytorch/GATNE-T/requirements.txt` (manifest)
- `examples/pytorch/dimenet/config/convert.yaml` (config)
- `examples/pytorch/dimenet/config/dimenet.yaml` (config)
- `examples/pytorch/dimenet/config/dimenet_pp.yaml` (config)
- `examples/pytorch/gnn_explainer/gnn_subgraph/1/graph.json` (config)
- `examples/pytorch/gnn_explainer/gnn_subgraph/1/model_list.json` (config)
- `examples/pytorch/gnn_explainer/gnn_subgraph/1/subgraph_1.json` (config)
- `examples/pytorch/gnn_explainer/gnn_subgraph/1/subgraph_list.json` (config)
- `examples/pytorch/gnn_explainer/gnn_subgraph/dataset_list.json` (config)

## Top-level layout

- `examples` — 358 analysed file(s)
- `docs` — 188 analysed file(s)
- `benchmarks` — 79 analysed file(s)
- `dglgo` — 75 analysed file(s)
- `docker` — 32 analysed file(s)
- `dgl_sparse` — 30 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `.github` — 8 analysed file(s)
- `conda` — 7 analysed file(s)
- `cmake` — 5 analysed file(s)
- `apps` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 7 file(s) were skipped during inventory (7 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `3d16000b4170fa741ed9e9667f22ba84d3493026` is the revision these paths and observations refer to.
