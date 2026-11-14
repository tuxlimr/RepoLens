# Project structure: horovod/horovod

**Analysed commit:** `369fe98d228e40c374e21a65fb2028e2a78bd0dc`

**Commit reference:** [369fe98d228e40c374e21a65fb2028e2a78bd0dc](https://github.com/horovod/horovod/commit/369fe98d228e40c374e21a65fb2028e2a78bd0dc)

**Tree at this commit:** [horovod/horovod@369fe98d228e](https://github.com/horovod/horovod/tree/369fe98d228e40c374e21a65fb2028e2a78bd0dc)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | horovod/horovod |
| Description | Distributed training framework for TensorFlow, Keras, PyTorch, and Apache MXNet. |
| Stars | 14674 |
| Forks | 2226 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `369fe98d228e40c374e21a65fb2028e2a78bd0dc` |
| Retrieved at | 2026-11-14T19:09:20.747801+00:00 |
| Files in this snapshot | 494 |

## Directory tree

```text
.buildkite/  (2 files)
  gen-pipeline.sh
  get_changed_code_files.py
.github/  (11 files)
  ISSUE_TEMPLATE/  (2 files)
    bug_report.md
    feature_request.md
  workflows/  (3 files)
    ci-results.yaml
    codeql-analysis.yml
    upload-pypi.yml
  dependabot.yml
  gen-workflow-ci.py
  get-changed-code-files.py
  pull_request_template.md
  requirements.txt
  timeout-and-retry.sh
cmake/  (9 files)
  Modules/  (6 files)
    FindMxnet.cmake
    FindNCCL.cmake
    FindNVTX.cmake
    FindPytorch.cmake
    FindROCM.cmake
    FindTensorflow.cmake
  upstream/  (1 files)
    FindCUDAToolkit.cmake
  Utilities.cmake
  build_utils.py
docker/  (15 files)
  helm/  (10 files)
    templates/  (7 files)
      … 7 files under this directory
    Chart.yaml
    README.md
    values.yaml
  horovod/  (1 files)
    Dockerfile
  horovod-cpu/  (1 files)
    Dockerfile
  horovod-nvtabular/  (1 files)
    Dockerfile
  horovod-ray/  (1 files)
    Dockerfile
  README.md
docs/  (62 files)
  _static/  (2 files)
    .empty
    custom.css
  _templates/  (1 files)
    .empty
  Makefile
  adasum_user_guide.rst
  adasum_user_guide_include.rst
  api.rst
  autotune.rst
  autotune_include.rst
  benchmarks.rst
  benchmarks_include.rst
  concepts.rst
  concepts_include.rst
  conda.rst
  conda_include.rst
  conf.py
  contributors.rst
  contributors_include.rst
  docker.rst
  docker_include.rst
  elastic.rst
  elastic_include.rst
  gpus.rst
  gpus_include.rst
  hyperparameter_search.rst
  hyperparameter_search_include.rst
  index.rst
  … 35 more files
examples/  (45 files)
  adasum/  (2 files)
    adasum_bench.ipynb
    adasum_small_model.py
  elastic/  (7 files)
    pytorch/  (3 files)
      … 3 files under this directory
    tensorflow/  (1 files)
      … 1 files under this directory
    tensorflow2/  (3 files)
      … 3 files under this directory
  keras/  (3 files)
    keras_imagenet_resnet50.py
    keras_mnist.py
    keras_mnist_advanced.py
  mxnet/  (3 files)
    mxnet2_mnist.py
    mxnet_imagenet_resnet50.py
    mxnet_mnist.py
  pytorch/  (4 files)
    pytorch_imagenet_resnet50.py
    pytorch_lightning_mnist.py
    pytorch_mnist.py
    pytorch_synthetic_benchmark.py
  ray/  (3 files)
    basic_ray_elastic.py
    pytorch_ray_elastic.py
    tensorflow2_mnist_ray.py
  spark/  (10 files)
    keras/  (6 files)
      … 6 files under this directory
    pytorch/  (3 files)
      … 3 files under this directory
    tensorflow2/  (1 files)
      … 1 files under this directory
  tensorflow/  (6 files)
    tensorflow_keras_mnist.py
    tensorflow_mnist.py
    tensorflow_mnist_eager.py
    tensorflow_mnist_estimator.py
    tensorflow_synthetic_benchmark.py
    tensorflow_word2vec.py
  tensorflow2/  (7 files)
    tensorflow2_keras_mnist.py
    tensorflow2_keras_synthetic_benchmark.py
    tensorflow2_mnist.py
    tensorflow2_mnist_data_service.py
    tensorflow2_mnist_data_service_train_fn_compute_side_dispatcher.py
    tensorflow2_mnist_data_service_train_fn_training_side_dispatcher.py
    tensorflow2_synthetic_benchmark.py
horovod/  (266 files)
  _keras/  (3 files)
    __init__.py
    callbacks.py
    elastic.py
  common/  (97 files)
    gloo/  (9 files)
      … 9 files under this directory
    mpi/  (6 files)
      … 6 files under this directory
    ops/  (34 files)
      … 34 files under this directory
    optim/  (4 files)
      … 4 files under this directory
    utils/  (2 files)
      … 2 files under this directory
    wire/  (2 files)
      … 2 files under this directory
    __init__.py
    basics.py
    common.cc
    common.h
    controller.cc
    controller.h
    elastic.py
    exceptions.py
    fusion_buffer_manager.cc
    fusion_buffer_manager.h
    global_state.h
    group_table.cc
    group_table.h
    half.cc
    half.h
    hashes.h
    logging.cc
    logging.h
    message.cc
    message.h
    nvtx_op_range.cc
    nvtx_op_range.h
    operations.cc
    operations.h
    … 16 more files
  data/  (2 files)
    __init__.py
    data_loader_base.py
  keras/  (3 files)
    __init__.py
    callbacks.py
    elastic.py
  mxnet/  (14 files)
    CMakeLists.txt
    __init__.py
    adapter.cc
    adapter.h
    compression.py
    cuda_util.cc
    cuda_util.h
    functions.py
    mpi_ops.cc
    mpi_ops.h
    mpi_ops.py
    tensor_util.cc
    tensor_util.h
    util.h
  ray/  (10 files)
    __init__.py
    adapter.py
    driver_service.py
    elastic.py
    elastic_v2.py
    ray_logger.py
    runner.py
    strategy.py
    utils.py
    worker.py
  runner/  (46 files)
    common/  (17 files)
      … 17 files under this directory
    driver/  (2 files)
      … 2 files under this directory
    elastic/  (8 files)
      … 8 files under this directory
    http/  (3 files)
      … 3 files under this directory
    task/  (2 files)
      … 2 files under this directory
    util/  (7 files)
      … 7 files under this directory
    __init__.py
    gloo_run.py
    js_run.py
    launch.py
    mpi_run.py
    run_task.py
    task_fn.py
  spark/  (51 files)
    common/  (11 files)
      … 11 files under this directory
    data_loaders/  (2 files)
      … 2 files under this directory
    driver/  (7 files)
      … 7 files under this directory
    keras/  (8 files)
      … 8 files under this directory
    lightning/  (6 files)
      … 6 files under this directory
    task/  (5 files)
      … 5 files under this directory
    tensorflow/  (2 files)
      … 2 files under this directory
    torch/  (5 files)
      … 5 files under this directory
    __init__.py
    conf.py
    gloo_run.py
    mpi_run.py
    runner.py
  tensorflow/  (20 files)
    data/  (3 files)
      … 3 files under this directory
    keras/  (3 files)
      … 3 files under this directory
    CMakeLists.txt
    __init__.py
    compression.py
    custom_call_config.fbs
    custom_call_config_generated.h
    elastic.py
    functions.py
    gradient_aggregation.py
    gradient_aggregation_eager.py
    mpi_ops.cc
    mpi_ops.py
    sync_batch_norm.py
    util.py
    xla_mpi_ops.cc
  torch/  (19 files)
    elastic/  (3 files)
      … 3 files under this directory
    CMakeLists.txt
    __init__.py
    adapter_v2.cc
    adapter_v2.h
    compression.py
    cuda_util.cc
    cuda_util.h
    functions.py
    handle_manager.cc
    handle_manager.h
    mpi_ops.py
    mpi_ops_v2.cc
    optimizer.py
    ready_event.cc
    ready_event.h
    sync_batch_norm.py
  __init__.py
test/  (61 files)
  integration/  (20 files)
    data/  (4 files)
      … 4 files under this directory
    elastic_common.py
    elastic_spark_common.py
    test_elastic_spark_tensorflow.py
    test_elastic_spark_tensorflow2.py
    test_elastic_spark_torch.py
    test_elastic_tensorflow.py
    test_elastic_tensorflow2.py
    test_elastic_tensorflow_keras.py
    test_elastic_torch.py
    test_interactiverun.py
    test_spark.py
    test_spark_keras.py
    test_spark_lightning.py
    test_spark_torch.py
    test_stall.py
    test_static_run.py
  parallel/  (20 files)
    base_test_mxnet.py
    base_test_tensorflow.py
    test_adasum_pytorch.py
    test_adasum_tensorflow.py
    test_common.py
    test_compute_worker.py
    test_keras.py
    test_mxnet1.py
    test_mxnet2.py
    test_process_sets_multi_comm.py
    test_process_sets_static.py
    test_tensorflow2_keras.py
    test_tensorflow2_keras_process_sets.py
    test_tensorflow_keras.py
    test_tensorflow_process_sets.py
    test_tensorflow_process_sets_dynamic.py
    test_timeline.py
    test_torch.py
    test_xla.py
    test_xla_process_sets.py
  single/  (18 files)
    data/  (5 files)
      … 5 files under this directory
    test_buildkite.py
    test_compute_service.py
    test_elastic_discovery.py
    test_elastic_driver.py
    test_elastic_run.py
    test_ray.py
    test_ray_elastic.py
    test_ray_elastic_v2.py
    test_run.py
    test_service.py
    test_task_service.py
    test_torch_elastic.py
    test_util.py
  utils/  (2 files)
    common.py
    spark_common.py
  conftest.py
.clang-format
.gitignore
.gitmodules
.readthedocs.yaml
CHANGELOG.md
CMakeLists.txt
CODE_OF_CONDUCT.md
CONTRIBUTING.md
Dockerfile.test.cpu
Dockerfile.test.gpu
GOVERNANCE.md
Jenkinsfile.ppc64le
LICENSE
MANIFEST.in
NOTICE
README.rst
SECURITY.md
assert-package-versions.sh
docker-compose.test.yml
horovod.exp
horovod.lds
setup.cfg
setup.py
```

## Entry points

- [.buildkite/get_changed_code_files.py:50](https://github.com/horovod/horovod/blob/369fe98d228e40c374e21a65fb2028e2a78bd0dc/.buildkite/get_changed_code_files.py#L50)
- [.github/gen-workflow-ci.py:835](https://github.com/horovod/horovod/blob/369fe98d228e40c374e21a65fb2028e2a78bd0dc/.github/gen-workflow-ci.py#L835)
- [.github/get-changed-code-files.py:50](https://github.com/horovod/horovod/blob/369fe98d228e40c374e21a65fb2028e2a78bd0dc/.github/get-changed-code-files.py#L50)
- [horovod/runner/launch.py](https://github.com/horovod/horovod/blob/369fe98d228e40c374e21a65fb2028e2a78bd0dc/horovod/runner/launch.py)
- [horovod/runner/run_task.py:34](https://github.com/horovod/horovod/blob/369fe98d228e40c374e21a65fb2028e2a78bd0dc/horovod/runner/run_task.py#L34)
- [horovod/runner/task_fn.py:56](https://github.com/horovod/horovod/blob/369fe98d228e40c374e21a65fb2028e2a78bd0dc/horovod/runner/task_fn.py#L56)
- [horovod/spark/driver/mpirun_rsh.py:23](https://github.com/horovod/horovod/blob/369fe98d228e40c374e21a65fb2028e2a78bd0dc/horovod/spark/driver/mpirun_rsh.py#L23)
- [horovod/spark/task/gloo_exec_fn.py:26](https://github.com/horovod/horovod/blob/369fe98d228e40c374e21a65fb2028e2a78bd0dc/horovod/spark/task/gloo_exec_fn.py#L26)
- [horovod/spark/task/mpirun_exec_fn.py:48](https://github.com/horovod/horovod/blob/369fe98d228e40c374e21a65fb2028e2a78bd0dc/horovod/spark/task/mpirun_exec_fn.py#L48)
- [horovod/spark/tensorflow/compute_worker.py:28](https://github.com/horovod/horovod/blob/369fe98d228e40c374e21a65fb2028e2a78bd0dc/horovod/spark/tensorflow/compute_worker.py#L28)
- [horovod/tensorflow/data/compute_worker.py:64](https://github.com/horovod/horovod/blob/369fe98d228e40c374e21a65fb2028e2a78bd0dc/horovod/tensorflow/data/compute_worker.py#L64)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cmake package | library | Observed | Groups 1 file(s) under cmake package (observed from repository paths and static analysis). Observed top-level functions: get_nvcc_bin, get_nvcc_flags, is_mx_cuda, is_mx_dnn, is_mx_mkldnn, is_mx_onednn. |
| Configuration and deployment | config | Observed | Groups 19 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BaseSettings, CMakeExtension, ElasticSettings, Settings, custom_build_ext. Observed… |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 4 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AsyncDataLoaderMixin, BaseDataLoader, TfDataServiceConfig. Observed top-level functions: compute_worker… |
| Application entry point | entrypoint | Observed | Groups 8 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _check_all_hosts_ssh_successful, _is_elastic, _launch_job, _run, _run_elastic, _run_stat… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level functions: put_data_into_kvstore, read_data_from_kvstore. |
| horovod package | library | Observed | Groups 181 file(s) under horovod package (observed from repository paths and static analysis). Observed top-level classes: AbstractFilesystemStore, AckResponse, AckStreamResponse, Adapter, Backend, BaseHorovodWorker. Ob… |
| Service / domain layer | service | Observed | Groups 9 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level classes: AbortCommandRequest, AllTaskAddressesRequest, AllTaskAddressesResponse, BasicDriverClient,… |
| Tests | test | Observed | Groups 61 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH horovod.runner.elastic.driver.DISCOVER_HOSTS_FREQUENCY_SECS, PATCH horovod.runner.gloo_run._get_min_start_hosts,… |

## Important files

- `.github/dependabot.yml` (config)
- `.github/requirements.txt` (manifest)
- `.github/workflows/ci-results.yaml` (ci)
- `.github/workflows/codeql-analysis.yml` (ci)
- `.github/workflows/upload-pypi.yml` (ci)
- `.readthedocs.yaml` (config)
- `Dockerfile.test.cpu` (container)
- `Dockerfile.test.gpu` (container)
- `MANIFEST.in` (manifest)
- `docker-compose.test.yml` (config)
- `docker/helm/Chart.yaml` (config)
- `docker/helm/templates/config.yaml` (config)
- `docker/helm/templates/job-service.yaml` (config)
- `docker/helm/templates/job.yaml` (config)
- `docker/helm/templates/statefulset-service.yaml` (config)
- `docker/helm/templates/statefulset.yaml` (config)
- `docker/helm/values.yaml` (config)
- `docker/horovod-cpu/Dockerfile` (container)
- `docker/horovod-nvtabular/Dockerfile` (container)
- `docker/horovod-ray/Dockerfile` (container)
- `docker/horovod/Dockerfile` (container)
- `docs/requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `horovod` — 266 analysed file(s)
- `docs` — 62 analysed file(s)
- `test` — 61 analysed file(s)
- `examples` — 45 analysed file(s)
- `(root files)` — 23 analysed file(s)
- `docker` — 15 analysed file(s)
- `.github` — 11 analysed file(s)
- `cmake` — 9 analysed file(s)
- `.buildkite` — 2 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 1 file(s) were skipped during inventory (1 x likely secret file excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `369fe98d228e40c374e21a65fb2028e2a78bd0dc` is the revision these paths and observations refer to.
