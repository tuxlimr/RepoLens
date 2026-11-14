# Project structure: pyg-team/pytorch_geometric

**Analysed commit:** `d1f2f8642387b6e0563d6aee227c39130746c738`

**Commit reference:** [d1f2f8642387b6e0563d6aee227c39130746c738](https://github.com/pyg-team/pytorch_geometric/commit/d1f2f8642387b6e0563d6aee227c39130746c738)

**Tree at this commit:** [pyg-team/pytorch_geometric@d1f2f8642387](https://github.com/pyg-team/pytorch_geometric/tree/d1f2f8642387b6e0563d6aee227c39130746c738)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | pyg-team/pytorch_geometric |
| Description | Graph Neural Network Library for PyTorch |
| Stars | 24142 |
| Forks | 4102 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `d1f2f8642387b6e0563d6aee227c39130746c738` |
| Retrieved at | 2026-11-14T19:07:41.329553+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (21 files)
  ISSUE_TEMPLATE/  (6 files)
    bug-report.yml
    config.yml
    documentation.yml
    feature-request.yml
    installation.yml
    refactor.yml
  actions/  (1 files)
    setup/  (1 files)
      … 1 files under this directory
  workflows/  (10 files)
    _testing.yml
    auto-merge.yml
    building_nightly.yml
    changelog.yml
    documentation.yml
    examples.yml
    labeler.yml
    linting.yml
    testing.yml
    testing_rag.yml
  CODEOWNERS
  CONTRIBUTING.md
  dependabot.yml
  labeler.yml
benchmark/  (70 files)
  citation/  (13 files)
    README.md
    __init__.py
    appnp.py
    arma.py
    cheb.py
    datasets.py
    gat.py
    gcn.py
    inference.sh
    run.sh
    sgc.py
    statistics.py
    train_eval.py
  inference/  (2 files)
    README.md
    inference_benchmark.py
  kernel/  (19 files)
    README.md
    __init__.py
    asap.py
    datasets.py
    diff_pool.py
    edge_pool.py
    gcn.py
    gin.py
    global_attention.py
    graclus.py
    graph_sage.py
    main.py
    main_performance.py
    sag_pool.py
    set2set.py
    sort_pool.py
    statistics.py
    top_k.py
    train_eval.py
  loader/  (1 files)
    neighbor_loader.py
  multi_gpu/  (4 files)
    training/  (4 files)
      … 4 files under this directory
  points/  (10 files)
    README.md
    __init__.py
    datasets.py
    edge_cnn.py
    mpnn.py
    point_cnn.py
    point_net.py
    spline_cnn.py
    statistics.py
    train_eval.py
  runtime/  (13 files)
    dgl/  (6 files)
      … 6 files under this directory
    README.md
    __init__.py
    gat.py
    gcn.py
    main.py
    rgcn.py
    train.py
  training/  (2 files)
    README.md
    training_benchmark.py
  utils/  (4 files)
    __init__.py
    hetero_gat.py
    hetero_sage.py
    utils.py
  README.md
  setup.py
docker/  (4 files)
  Dockerfile
  Dockerfile.xpu
  README.md
  singularity
docs/  (88 files)
  source/  (85 files)
    _figures/  (12 files)
      … 12 files under this directory
    _static/  (1 files)
      … 1 files under this directory
    _templates/  (5 files)
      … 5 files under this directory
    advanced/  (8 files)
      … 8 files under this directory
    cheatsheet/  (2 files)
      … 2 files under this directory
    external/  (1 files)
      … 1 files under this directory
    get_started/  (2 files)
      … 2 files under this directory
    install/  (2 files)
      … 2 files under this directory
    modules/  (15 files)
      … 15 files under this directory
    notes/  (16 files)
      … 16 files under this directory
    tutorial/  (18 files)
      … 18 files under this directory
    .gitignore
    conf.py
    index.rst
  Makefile
  README.md
  requirements.txt
examples/  (174 files)
  compile/  (2 files)
    gcn.py
    gin.py
  contrib/  (5 files)
    README.md
    pgm_explainer_graph_classification.py
    pgm_explainer_node_classification.py
    rbcd_attack.py
    rbcd_attack_poisoning.py
  cpp/  (4 files)
    CMakeLists.txt
    README.md
    main.cpp
    save_model.py
  distributed/  (11 files)
    graphlearn_for_pytorch/  (5 files)
      … 5 files under this directory
    kuzu/  (4 files)
      … 4 files under this directory
    pyg/  (1 files)
      … 1 files under this directory
    README.md
  explain/  (8 files)
    README.md
    captum_explainer.py
    captum_explainer_hetero_link.py
    gnn_explainer.py
    gnn_explainer_ba_shapes.py
    gnn_explainer_link_pred.py
    graphmask_explainer.py
    mgnan_graph_mutagenicity.py
  hetero/  (14 files)
    README.md
    bipartite_sage.py
    bipartite_sage_unsup.py
    dmgi_unsup.py
    han_imdb.py
    hetero_conv_dblp.py
    hetero_link_pred.py
    hgt_dblp.py
    hierarchical_sage.py
    load_csv.py
    metapath2vec.py
    recommender_system.py
    temporal_link_pred.py
    to_hetero_mag.py
  jit/  (5 files)
    README.md
    film.py
    gat.py
    gcn.py
    gin.py
  llm/  (11 files)
    txt2qa_config/  (2 files)
      … 2 files under this directory
    README.md
    g_retriever.py
    git_mol.py
    glem.py
    molecule_gpt.py
    protein_mpnn.py
    relbench_gretriever.py
    txt2kg_rag.py
    txt2qa.py
  multi_gpu/  (12 files)
    README.md
    distributed_batching.py
    distributed_sampling.py
    distributed_sampling_multinode.py
    distributed_sampling_multinode.sbatch
    distributed_sampling_xpu.py
    mag240m_graphsage.py
    model_parallel.py
    papers100m_gcn.py
    papers100m_gcn_multinode.py
    pcqm4m_ogb.py
    taobao.py
  pytorch_ignite/  (2 files)
    README.md
    gin.py
  pytorch_lightning/  (4 files)
    README.md
    gin.py
    graph_sage.py
    relational_gnn.py
  quiver/  (3 files)
    README.md
    multi_gpu_quiver.py
    single_gpu_quiver.py
  README.md
  agnn.py
  ar_link_pred.py
  argva_node_clustering.py
  arma.py
  attentive_fp.py
  autoencoder.py
  cluster_gcn_ppi.py
  cluster_gcn_reddit.py
  colors_topk_pool.py
  cora.py
  correct_and_smooth.py
  datapipe.py
  dgcnn_classification.py
  dgcnn_segmentation.py
  dir_gnn.py
  dna.py
  egc.py
  equilibrium_median.py
  faust.py
  film.py
  gat.py
  gcn.py
  gcn2_cora.py
  … 69 more files
graphgym/  (49 files)
  configs/  (4 files)
    pyg/  (3 files)
      … 3 files under this directory
    example.yaml
  custom_graphgym/  (26 files)
    act/  (2 files)
      … 2 files under this directory
    config/  (2 files)
      … 2 files under this directory
    encoder/  (2 files)
      … 2 files under this directory
    head/  (2 files)
      … 2 files under this directory
    layer/  (2 files)
      … 2 files under this directory
    loader/  (2 files)
      … 2 files under this directory
    loss/  (2 files)
      … 2 files under this directory
    network/  (2 files)
      … 2 files under this directory
    optimizer/  (2 files)
      … 2 files under this directory
    pooling/  (2 files)
      … 2 files under this directory
    stage/  (2 files)
      … 2 files under this directory
    train/  (2 files)
      … 2 files under this directory
    transform/  (1 files)
      … 1 files under this directory
    __init__.py
  grids/  (2 files)
    pyg/  (1 files)
      … 1 files under this directory
    example.txt
  results/  (9 files)
    example_node_grid_example/  (9 files)
      … 9 files under this directory
  sample/  (2 files)
    dimensions.txt
    dimensionsatt.txt
  agg_batch.py
  configs_gen.py
  main.py
  parallel.sh
  run_batch.sh
  run_single.sh
test/  (385 files)
  contrib/  (4 files)
    explain/  (1 files)
      … 1 files under this directory
    nn/  (2 files)
      … 2 files under this directory
    utils/  (1 files)
      … 1 files under this directory
  data/  (17 files)
    lightning/  (1 files)
      … 1 files under this directory
    test_batch.py
    test_data.py
    test_database.py
    test_datapipes.py
    test_dataset.py
    test_dataset_summary.py
    test_feature_store.py
    test_graph_store.py
    test_hetero_data.py
    test_hypergraph_data.py
    test_inherit.py
    test_on_disk_dataset.py
    test_remote_backend_utils.py
    test_storage.py
    test_temporal.py
    test_view.py
  datasets/  (29 files)
    graph_generator/  (4 files)
      … 4 files under this directory
    motif_generator/  (4 files)
      … 4 files under this directory
    test_ba_shapes.py
    test_bzr.py
    test_elliptic.py
    test_enzymes.py
    test_explainer_dataset.py
    test_fake.py
    test_git_mol_dataset.py
    test_graphland.py
    test_imdb_binary.py
    test_infection_dataset.py
    test_karate.py
    test_medshapenet.py
    test_molecule_gpt_dataset.py
    test_mutag.py
    test_planetoid.py
    test_protein_mpnn_dataset.py
    test_snap_dataset.py
    test_suite_sparse.py
    test_tag_dataset.py
    test_teeth3ds.py
    test_web_qsp_dataset.py
  distributed/  (9 files)
    test_dist_link_neighbor_loader.py
    test_dist_link_neighbor_sampler.py
    test_dist_neighbor_loader.py
    test_dist_neighbor_sampler.py
    test_dist_utils.py
    test_local_feature_store.py
    test_local_graph_store.py
    test_partition.py
    test_rpc.py
  explain/  (17 files)
    algorithm/  (8 files)
      … 8 files under this directory
    metric/  (3 files)
      … 3 files under this directory
    conftest.py
    test_explain_config.py
    test_explainer.py
    test_explanation.py
    test_hetero_explainer.py
    test_hetero_explanation.py
  graphgym/  (5 files)
    example_node.yml
    test_config.py
    test_graphgym.py
    test_logger.py
    test_register.py
  io/  (4 files)
    example1.off
    example2.off
    test_fs.py
    test_off.py
  llm/  (18 files)
    models/  (10 files)
      … 10 files under this directory
    utils/  (4 files)
      … 4 files under this directory
    conftest.py
    test_large_graph_indexer.py
    test_rag_loader.py
    test_txt2qa.py
  loader/  (18 files)
    test_cache.py
    test_cluster.py
    test_dataloader.py
    test_dynamic_batch_sampler.py
    test_graph_saint.py
    test_hgt_loader.py
    test_ibmb_loader.py
    test_imbalanced_sampler.py
    test_link_neighbor_loader.py
    test_mixin.py
    test_neighbor_loader.py
    test_neighbor_sampler.py
    test_prefetch.py
    test_random_node_loader.py
    test_shadow.py
    test_temporal_dataloader.py
    test_utils.py
    test_zip_loader.py
  metrics/  (1 files)
    test_link_pred_metric.py
  nn/  (185 files)
    aggr/  (19 files)
      … 19 files under this directory
    attention/  (3 files)
      … 3 files under this directory
    conv/  (67 files)
      … 67 files under this directory
    dense/  (9 files)
      … 9 files under this directory
    functional/  (2 files)
      … 2 files under this directory
    kge/  (4 files)
      … 4 files under this directory
    models/  (33 files)
      … 33 files under this directory
    norm/  (9 files)
      … 9 files under this directory
    pool/  (19 files)
      … 19 files under this directory
    unpool/  (1 files)
      … 1 files under this directory
    test_compile_basic.py
    test_compile_conv.py
    test_compile_dynamic.py
    test_data_parallel.py
    test_encoding.py
    test_fvcore.py
    test_fx.py
    test_inits.py
    test_model_hub.py
    test_model_summary.py
    test_module_dict.py
    test_parameter_dict.py
    test_reshape.py
    test_resolver.py
    test_sequential.py
    test_to_fixed_size_transformer.py
    test_to_hetero_module.py
    test_to_hetero_transformer.py
    test_to_hetero_with_bases_transformer.py
  profile/  (5 files)
    test_benchmark.py
    test_nvtx.py
    test_profile.py
    test_profile_utils.py
    test_profiler.py
  sampler/  (2 files)
    test_sampler_base.py
    test_sampler_neighbor_sampler.py
  testing/  (1 files)
    test_decorators.py
  transforms/  (54 files)
    test_add_gpse.py
    test_add_metapaths.py
    test_add_positional_encoding.py
    test_add_remaining_self_loops.py
    test_add_self_loops.py
    test_cartesian.py
    test_center.py
    test_compose.py
    test_constant.py
    test_delaunay.py
    test_distance.py
    test_face_to_edge.py
    test_feature_propagation.py
    test_fixed_points.py
    test_gcn_norm.py
    test_gdc.py
    test_generate_mesh_normals.py
    test_grid_sampling.py
    test_half_hop.py
    test_knn_graph.py
    test_laplacian_lambda_max.py
    test_largest_connected_components.py
    test_line_graph.py
    test_linear_transformation.py
    … 30 more files
  conftest.py
  my_config.yaml
  test_config_mixin.py
  test_config_store.py
  test_debug.py
  test_edge_index.py
  test_experimental.py
  test_hash_tensor.py
  test_home.py
  test_index.py
  test_inspector.py
  test_isinstance.py
  test_onnx.py
  test_seed.py
  test_typing.py
  test_warnings.py
.gitignore
.pre-commit-config.yaml
CHANGELOG.md
CITATION.cff
LICENSE
README.md
codecov.yml
pyproject.toml
readthedocs.yml
```

## Entry points

- [benchmark/inference/inference_benchmark.py:298](https://github.com/pyg-team/pytorch_geometric/blob/d1f2f8642387b6e0563d6aee227c39130746c738/benchmark/inference/inference_benchmark.py#L298)
- [benchmark/loader/neighbor_loader.py:106](https://github.com/pyg-team/pytorch_geometric/blob/d1f2f8642387b6e0563d6aee227c39130746c738/benchmark/loader/neighbor_loader.py#L106)
- [benchmark/multi_gpu/training/training_benchmark_cuda.py:26](https://github.com/pyg-team/pytorch_geometric/blob/d1f2f8642387b6e0563d6aee227c39130746c738/benchmark/multi_gpu/training/training_benchmark_cuda.py#L26)
- [benchmark/multi_gpu/training/training_benchmark_xpu.py:40](https://github.com/pyg-team/pytorch_geometric/blob/d1f2f8642387b6e0563d6aee227c39130746c738/benchmark/multi_gpu/training/training_benchmark_xpu.py#L40)
- [benchmark/training/training_benchmark.py:341](https://github.com/pyg-team/pytorch_geometric/blob/d1f2f8642387b6e0563d6aee227c39130746c738/benchmark/training/training_benchmark.py#L341)
- [graphgym/main.py:23](https://github.com/pyg-team/pytorch_geometric/blob/d1f2f8642387b6e0563d6aee227c39130746c738/graphgym/main.py#L23)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| benchmark package | library | Observed | Groups 53 file(s) under benchmark package (observed from repository paths and static analysis). Observed top-level classes: ASAP, Block, DiffPool, EdgePool, GAT, GATConv. Observed top-level functions: create_mask_per_ra… |
| Configuration and deployment | config | Observed | Groups 12 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: set_cfg_example. |
| Application entry point | entrypoint | Observed | Groups 9 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: custom_optimizer, full_batch_inference, get_dist_params, logger, run, run_cuda. |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| graphgym package | library | Observed | Groups 29 file(s) under graphgym package (observed from repository paths and static analysis). Observed top-level classes: ExampleConv1, ExampleConv2, ExampleConv2Layer, ExampleEdgeEncoder, ExampleGNN, ExampleNodeEncode… |
| Tests | test | Observed | Groups 387 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH torch_geometric.profile.nvtx.torch.cuda, PATCH torch_geometric.profile.nvtx.torch.cuda, PATCH torch_geometric.p… |

## Important files

- `.github/ISSUE_TEMPLATE/bug-report.yml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/ISSUE_TEMPLATE/documentation.yml` (config)
- `.github/ISSUE_TEMPLATE/feature-request.yml` (config)
- `.github/ISSUE_TEMPLATE/installation.yml` (config)
- `.github/ISSUE_TEMPLATE/refactor.yml` (config)
- `.github/actions/setup/action.yml` (config)
- `.github/dependabot.yml` (config)
- `.github/labeler.yml` (config)
- `.github/workflows/_testing.yml` (ci)
- `.github/workflows/auto-merge.yml` (ci)
- `.github/workflows/building_nightly.yml` (ci)
- `.github/workflows/changelog.yml` (ci)
- `.github/workflows/documentation.yml` (ci)
- `.github/workflows/examples.yml` (ci)
- `.github/workflows/labeler.yml` (ci)
- `.github/workflows/linting.yml` (ci)
- `.github/workflows/testing.yml` (ci)
- `.github/workflows/testing_rag.yml` (ci)
- `.pre-commit-config.yaml` (config)
- `benchmark/setup.py` (manifest)
- `codecov.yml` (config)
- `docker/Dockerfile` (container)
- `docker/Dockerfile.xpu` (container)
- `docs/requirements.txt` (manifest)
- `examples/distributed/graphlearn_for_pytorch/dist_train_sage_sup_config.yml` (config)
- `examples/llm/txt2qa_config/text_config_nim.yaml` (config)
- `examples/llm/txt2qa_config/text_config_vllm.yaml` (config)
- `graphgym/configs/example.yaml` (config)
- `graphgym/configs/pyg/example_graph.yaml` (config)
- `graphgym/configs/pyg/example_link.yaml` (config)
- `graphgym/configs/pyg/example_node.yaml` (config)
- `pyproject.toml` (manifest)
- `readthedocs.yml` (config)

## Top-level layout

- `test` — 385 analysed file(s)
- `examples` — 174 analysed file(s)
- `docs` — 88 analysed file(s)
- `benchmark` — 70 analysed file(s)
- `graphgym` — 49 analysed file(s)
- `.github` — 21 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `docker` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `d1f2f8642387b6e0563d6aee227c39130746c738` is the revision these paths and observations refer to.
