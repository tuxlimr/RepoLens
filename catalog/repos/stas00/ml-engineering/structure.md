# Project structure: stas00/ml-engineering

**Analysed commit:** `fbe87165bd90a697b158dd056fdb4703a0b85350`

**Commit reference:** [fbe87165bd90a697b158dd056fdb4703a0b85350](https://github.com/stas00/ml-engineering/commit/fbe87165bd90a697b158dd056fdb4703a0b85350)

**Tree at this commit:** [stas00/ml-engineering@fbe87165bd90](https://github.com/stas00/ml-engineering/tree/fbe87165bd90a697b158dd056fdb4703a0b85350)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | stas00/ml-engineering |
| Description | Machine Learning Engineering Open Book |
| Stars | 19713 |
| Forks | 1304 |
| Licence | CC-BY-SA-4.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `fbe87165bd90a697b158dd056fdb4703a0b85350` |
| Retrieved at | 2026-11-14T19:08:10.770366+00:00 |
| Files in this snapshot | 127 |

## Directory tree

```text
compute/  (10 files)
  accelerator/  (7 files)
    amd/  (2 files)
      … 2 files under this directory
    benchmarks/  (3 files)
      … 3 files under this directory
    nvidia/  (1 files)
      … 1 files under this directory
    README.md
  cpu/  (1 files)
    README.md
  cpu-memory/  (1 files)
    README.md
  README.md
courses/  (2 files)
  lesson-learned/  (2 files)
    README.md
    lesson-learned-cover.prompt
debug/  (29 files)
  code/  (9 files)
    collective_mismatch.py
    collective_mismatch_analyze.py
    kernel_oob.cu
    kernel_oob.py
    kernel_oob_gdb.py
    kernel_oob_prebuilt.py
    kernel_race.cu
    kernel_race.py
    see-mem-usage.py
  tiny-scripts/  (11 files)
    README.md
    c4-en-10k.py
    cm4-synthetic-testing.py
    fsmt-make-super-tiny-model.py
    general-pmd-ds-unpack.py
    general-pmd-synthetic-testing.py
    idefics-make-tiny-model.py
    m4-ds-unpack.py
    mt5-make-tiny-model.py
    openwebtext-10k.py
    oscar-en-10k.py
  NicerTrace.py
  README.md
  make-tiny-models-tokenizers-datasets.md
  nccl-performance-debug.md
  tools.md
  torch-distributed-gpu-test.py
  torch-distributed-hanging-solutions.md
  underflow_overflow.md
  underflow_overflow.py
inference/  (1 files)
  README.md
insights/  (9 files)
  when-to-upgrade-gpus/  (7 files)
    README.md
    bench_decompose.py
    bench_flash_attn.py
    benchmark.py
    install.sh
    plot_results.py
    run_sweep.sh
  ai-battlefield.md
  how-to-choose-cloud-provider.md
model-parallelism/  (1 files)
  README.md
network/  (10 files)
  benchmarks/  (7 files)
    README.md
    all_gather_object_vs_all_gather.py
    all_gather_object_vs_all_reduce.py
    all_reduce_bench.py
    all_reduce_latency_comp.py
    torch-dist-bench-pyxis.sbatch
    torch-dist-bench.py
  debug/  (1 files)
    README.md
  README.md
  comms.md
orchestration/  (15 files)
  kubernetes/  (1 files)
    README.md
  slurm/  (13 files)
    launchers/  (5 files)
      … 5 files under this directory
    README.md
    admin.md
    cron-daily.slurm
    cron-hourly.slurm
    example.slurm
    performance.md
    undrain-good-nodes.sh
    users.md
  README.md
resources/  (1 files)
  README.md
skills/  (3 files)
  evaluate-cluster/  (1 files)
    SKILL.md
  ml-engineering/  (1 files)
    SKILL.md
  README.md
stabs/  (2 files)
  README.md
  incoming.md
storage/  (4 files)
  README.md
  fio-json-extract.py
  fio-scan
  mmap-io-bench.py
testing/  (2 files)
  README.md
  testing_utils.py
training/  (30 files)
  checkpoints/  (3 files)
    README.md
    torch-checkpoint-convert-to-bf16
    torch-checkpoint-shrink.py
  fault-tolerance/  (5 files)
    README.md
    fs-watchdog.py
    fs-watchdog.slurm
    slurm-status.py
    slurm-status.slurm
  instabilities/  (2 files)
    README.md
    training-loss-patterns.md
  model-parallelism/  (1 files)
    README.md
  performance/  (9 files)
    benchmarks/  (7 files)
      … 7 files under this directory
    distributed/  (1 files)
      … 1 files under this directory
    README.md
  reproducibility/  (1 files)
    README.md
  tools/  (3 files)
    main_process_first.py
    multi-gpu-non-interleaved-print.py
    printflock.py
  README.md
  datasets.md
  dtype.md
  emulate-multi-node.md
  hparams.md
  re-train-hub-models.md
.gitignore
LICENSE-CC-BY-SA
Makefile
README.md
SKILL.md
chapters-md.txt
contributors.md
todo.md
```

## Entry points

- [compute/accelerator/benchmarks/mamf-finder-all-gpus.py:364](https://github.com/stas00/ml-engineering/blob/fbe87165bd90a697b158dd056fdb4703a0b85350/compute/accelerator/benchmarks/mamf-finder-all-gpus.py#L364)
- [compute/accelerator/benchmarks/mamf-finder.py:1983](https://github.com/stas00/ml-engineering/blob/fbe87165bd90a697b158dd056fdb4703a0b85350/compute/accelerator/benchmarks/mamf-finder.py#L1983)
- [debug/NicerTrace.py:201](https://github.com/stas00/ml-engineering/blob/fbe87165bd90a697b158dd056fdb4703a0b85350/debug/NicerTrace.py#L201)
- [debug/code/see-mem-usage.py:126](https://github.com/stas00/ml-engineering/blob/fbe87165bd90a697b158dd056fdb4703a0b85350/debug/code/see-mem-usage.py#L126)
- [insights/when-to-upgrade-gpus/bench_decompose.py:208](https://github.com/stas00/ml-engineering/blob/fbe87165bd90a697b158dd056fdb4703a0b85350/insights/when-to-upgrade-gpus/bench_decompose.py#L208)
- [insights/when-to-upgrade-gpus/benchmark.py:224](https://github.com/stas00/ml-engineering/blob/fbe87165bd90a697b158dd056fdb4703a0b85350/insights/when-to-upgrade-gpus/benchmark.py#L224)
- [network/benchmarks/all_reduce_latency_comp.py:91](https://github.com/stas00/ml-engineering/blob/fbe87165bd90a697b158dd056fdb4703a0b85350/network/benchmarks/all_reduce_latency_comp.py#L91)
- [network/benchmarks/torch-dist-bench.py:1020](https://github.com/stas00/ml-engineering/blob/fbe87165bd90a697b158dd056fdb4703a0b85350/network/benchmarks/torch-dist-bench.py#L1020)
- [training/checkpoints/torch-checkpoint-shrink.py:81](https://github.com/stas00/ml-engineering/blob/fbe87165bd90a697b158dd056fdb4703a0b85350/training/checkpoints/torch-checkpoint-shrink.py#L81)
- [training/fault-tolerance/fs-watchdog.py:183](https://github.com/stas00/ml-engineering/blob/fbe87165bd90a697b158dd056fdb4703a0b85350/training/fault-tolerance/fs-watchdog.py#L183)
- [training/fault-tolerance/slurm-status.py:179](https://github.com/stas00/ml-engineering/blob/fbe87165bd90a697b158dd056fdb4703a0b85350/training/fault-tolerance/slurm-status.py#L179)
- [training/performance/benchmarks/numa/numa-set-pynvml.py:48](https://github.com/stas00/ml-engineering/blob/fbe87165bd90a697b158dd056fdb4703a0b85350/training/performance/benchmarks/numa/numa-set-pynvml.py#L48)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Data layer | data | Observed | Groups 2 file(s) under data layer (observed from repository paths and static analysis). Observed top-level functions: drop_page_cache. |
| debug package | library | Observed | Groups 18 file(s) under debug package (observed from repository paths and static analysis). Observed top-level classes: C4En10k, CM4Synthetic, DebugOption, DebugUnderflowOverflow, ExplicitEnum, GeneralPMDSynthetic. Obse… |
| Application entry point | entrypoint | Observed | Groups 16 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AMDArch, Arch, CudaLikeArch, FakeTelemetry, HPUArch, MPSArch. Observed top-level function… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| insights package | library | Observed | Groups 4 file(s) under insights package (observed from repository paths and static analysis). Observed top-level functions: bench. |
| network package | library | Observed | Groups 3 file(s) under network package (observed from repository paths and static analysis). Observed top-level functions: all_gather, all_gather_object, all_reduce. |
| orchestration package | library | Observed | Groups 1 file(s) under orchestration package (observed from repository paths and static analysis). |
| testing package | library | Observed | Groups 1 file(s) under testing package (observed from repository paths and static analysis). Observed top-level classes: CaptureLogger, CaptureStd, CaptureStderr, CaptureStdout, TestCasePlus, _RunOutput. Observed top-le… |
| training package | library | Observed | Groups 6 file(s) under training package (observed from repository paths and static analysis). Observed top-level classes: MyDataset. Observed top-level functions: benchmark_bmm, printflock. |

## Important files

No manifest, config, CI, or container files were observed in the analysed set.

## Top-level layout

- `training` — 30 analysed file(s)
- `debug` — 29 analysed file(s)
- `orchestration` — 15 analysed file(s)
- `compute` — 10 analysed file(s)
- `network` — 10 analysed file(s)
- `insights` — 9 analysed file(s)
- `(root files)` — 8 analysed file(s)
- `storage` — 4 analysed file(s)
- `skills` — 3 analysed file(s)
- `courses` — 2 analysed file(s)
- `stabs` — 2 analysed file(s)
- `testing` — 2 analysed file(s)
- `inference` — 1 analysed file(s)
- `model-parallelism` — 1 analysed file(s)
- `resources` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- 20 file(s) were skipped during inventory (20 x vendored/generated directory excluded).
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `fbe87165bd90a697b158dd056fdb4703a0b85350` is the revision these paths and observations refer to.
