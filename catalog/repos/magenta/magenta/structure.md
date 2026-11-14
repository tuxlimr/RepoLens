# Project structure: magenta/magenta

**Analysed commit:** `c15687ebd1c1cc12658cd468c737d3c24c02b918`

**Commit reference:** [c15687ebd1c1cc12658cd468c737d3c24c02b918](https://github.com/magenta/magenta/commit/c15687ebd1c1cc12658cd468c737d3c24c02b918)

**Tree at this commit:** [magenta/magenta@c15687ebd1c1](https://github.com/magenta/magenta/tree/c15687ebd1c1cc12658cd468c737d3c24c02b918)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | magenta/magenta |
| Description | Magenta: Music and Art Generation with Machine Intelligence |
| Stars | 19785 |
| Forks | 3757 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `c15687ebd1c1cc12658cd468c737d3c24c02b918` |
| Retrieved at | 2026-11-14T19:08:08.086168+00:00 |
| Files in this snapshot | 388 |

## Directory tree

```text
.github/  (1 files)
  workflows/  (1 files)
    build.yml
demos/  (1 files)
  README.md
magenta/  (377 files)
  common/  (12 files)
    __init__.py
    beam_search.py
    beam_search_test.py
    concurrency.py
    concurrency_test.py
    nade.py
    nade_test.py
    sequence_example_lib.py
    state_util.py
    state_util_test.py
    testing_lib.py
    tf_utils.py
  contrib/  (7 files)
    __init__.py
    cudnn_rnn.py
    rnn.py
    rnn_test.py
    seq2seq.py
    seq2seq_test.py
    training.py
  interfaces/  (8 files)
    midi/  (7 files)
      … 7 files under this directory
    __init__.py
  js/  (1 files)
    README.md
  models/  (288 files)
    arbitrary_image_stylization/  (15 files)
      … 15 files under this directory
    coconet/  (23 files)
      … 23 files under this directory
    drums_rnn/  (10 files)
      … 10 files under this directory
    gansynth/  (22 files)
      … 22 files under this directory
    image_stylization/  (14 files)
      … 14 files under this directory
    improv_rnn/  (10 files)
      … 10 files under this directory
    latent_transfer/  (27 files)
      … 27 files under this directory
    melody_rnn/  (10 files)
      … 10 files under this directory
    music_vae/  (16 files)
      … 16 files under this directory
    nsynth/  (19 files)
      … 19 files under this directory
    onsets_frames_transcription/  (37 files)
      … 37 files under this directory
    performance_rnn/  (8 files)
      … 8 files under this directory
    piano_genie/  (9 files)
      … 9 files under this directory
    pianoroll_rnn_nade/  (9 files)
      … 9 files under this directory
    polyphony_rnn/  (13 files)
      … 13 files under this directory
    rl_tuner/  (8 files)
      … 8 files under this directory
    score2perf/  (11 files)
      … 11 files under this directory
    shared/  (9 files)
      … 9 files under this directory
    sketch_rnn/  (8 files)
      … 8 files under this directory
    svg_vae/  (8 files)
      … 8 files under this directory
    README.md
    __init__.py
  music/  (1 files)
    __init__.py
  pipelines/  (25 files)
    README.md
    __init__.py
    chord_pipelines.py
    chord_pipelines_test.py
    dag_pipeline.py
    dag_pipeline_test.py
    drum_pipelines.py
    drum_pipelines_test.py
    event_sequence_pipeline.py
    lead_sheet_pipelines.py
    lead_sheet_pipelines_test.py
    melody_pipelines.py
    melody_pipelines_test.py
    note_sequence_pipelines.py
    note_sequence_pipelines_test.py
    performance_pipeline.py
    performance_pipeline_test.py
    pianoroll_pipeline.py
    pianoroll_pipeline_test.py
    pipeline.py
    pipeline_test.py
    pipelines_common.py
    pipelines_common_test.py
    statistics.py
    … 1 more files
  reviews/  (7 files)
    GAN.md
    README.md
    draw.md
    pixelrnn.md
    rnnrbm.md
    styletransfer.md
    summary_generation_sequences.md
  scripts/  (6 files)
    README.md
    __init__.py
    abc_compare.py
    convert_dir_to_note_sequences.py
    convert_dir_to_note_sequences_test.py
    unpack_bundle.py
  tensor2tensor/  (7 files)
    __init__.py
    models.py
    problems.py
    problems_datagen.py
    t2t_datagen.py
    t2t_decoder.py
    t2t_trainer.py
  tools/  (1 files)
    magenta-install.sh
  video/  (12 files)
    next_frame_prediction_pix2pix/  (4 files)
      … 4 files under this directory
    tools/  (7 files)
      … 7 files under this directory
    __init__.py
  __init__.py
  version.py
.gitignore
.isort.cfg
.pylintrc
AUTHORS
LICENSE
README.md
conftest.py
setup.cfg
setup.py
```

## Entry points

- [magenta/common/beam_search_test.py:89](https://github.com/magenta/magenta/blob/c15687ebd1c1cc12658cd468c737d3c24c02b918/magenta/common/beam_search_test.py#L89)
- [magenta/common/concurrency_test.py:53](https://github.com/magenta/magenta/blob/c15687ebd1c1cc12658cd468c737d3c24c02b918/magenta/common/concurrency_test.py#L53)
- [magenta/common/nade_test.py:59](https://github.com/magenta/magenta/blob/c15687ebd1c1cc12658cd468c737d3c24c02b918/magenta/common/nade_test.py#L59)
- [magenta/common/state_util_test.py:78](https://github.com/magenta/magenta/blob/c15687ebd1c1cc12658cd468c737d3c24c02b918/magenta/common/state_util_test.py#L78)
- [magenta/contrib/rnn_test.py:954](https://github.com/magenta/magenta/blob/c15687ebd1c1cc12658cd468c737d3c24c02b918/magenta/contrib/rnn_test.py#L954)
- [magenta/contrib/seq2seq_test.py:558](https://github.com/magenta/magenta/blob/c15687ebd1c1cc12658cd468c737d3c24c02b918/magenta/contrib/seq2seq_test.py#L558)
- [magenta/interfaces/midi/magenta_midi.py:393](https://github.com/magenta/magenta/blob/c15687ebd1c1cc12658cd468c737d3c24c02b918/magenta/interfaces/midi/magenta_midi.py#L393)
- [magenta/interfaces/midi/midi_clock.py:78](https://github.com/magenta/magenta/blob/c15687ebd1c1cc12658cd468c737d3c24c02b918/magenta/interfaces/midi/midi_clock.py#L78)
- [magenta/interfaces/midi/midi_hub_test.py:710](https://github.com/magenta/magenta/blob/c15687ebd1c1cc12658cd468c737d3c24c02b918/magenta/interfaces/midi/midi_hub_test.py#L710)
- [magenta/models/arbitrary_image_stylization/arbitrary_image_stylization_convert_tflite.py:473](https://github.com/magenta/magenta/blob/c15687ebd1c1cc12658cd468c737d3c24c02b918/magenta/models/arbitrary_image_stylization/arbitrary_image_stylization_convert_tflite.py#L473)
- [magenta/models/arbitrary_image_stylization/arbitrary_image_stylization_distill_mobilenet.py:188](https://github.com/magenta/magenta/blob/c15687ebd1c1cc12658cd468c737d3c24c02b918/magenta/models/arbitrary_image_stylization/arbitrary_image_stylization_distill_mobilenet.py#L188)
- [magenta/models/arbitrary_image_stylization/arbitrary_image_stylization_evaluate.py:134](https://github.com/magenta/magenta/blob/c15687ebd1c1cc12658cd468c737d3c24c02b918/magenta/models/arbitrary_image_stylization/arbitrary_image_stylization_evaluate.py#L134)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 2 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 171 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AbsoluteMelody2PerfProblem, AggregateMean, AncestralSampler, Architecture, AudioRecorder, AudioTimeou… |
| Application entry point | entrypoint | Observed | Groups 78 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: AgibbsStrategy, AudioChunk, AudioQueue, BachUpsamplingStrategy, BaseStrategy, CCMapper. O… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| magenta package | library | Observed | Groups 45 file(s) under magenta package (observed from repository paths and static analysis). Observed top-level classes: AttentionCellWrapper, BadInputOrOutputError, BadTopologyError, BaseDecoder, BasicDecoder, BasicDe… |
| Tests | test | Observed | Groups 47 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BaseConditionedOneHotDataTest, BaseDataTest, BaseOneHotDataTest, BasicDecoderTest, BeamSearchTest, ChordPip… |

## Important files

- `.github/workflows/build.yml` (ci)
- `.isort.cfg` (config)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `magenta` — 377 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `.github` — 1 analysed file(s)
- `demos` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `c15687ebd1c1cc12658cd468c737d3c24c02b918` is the revision these paths and observations refer to.
