# Project structure: svc-develop-team/so-vits-svc

**Analysed commit:** `730930d337d171479eadf305f96cbed4bb393e77`

**Commit reference:** [730930d337d171479eadf305f96cbed4bb393e77](https://github.com/svc-develop-team/so-vits-svc/commit/730930d337d171479eadf305f96cbed4bb393e77)

**Tree at this commit:** [svc-develop-team/so-vits-svc@730930d337d1](https://github.com/svc-develop-team/so-vits-svc/tree/730930d337d171479eadf305f96cbed4bb393e77)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | svc-develop-team/so-vits-svc |
| Description | SoftVC VITS Singing Voice Conversion |
| Stars | 28037 |
| Forks | 5007 |
| Licence | AGPL-3.0 |
| Language | Python |
| Default branch | 4.1-Stable |
| Analysed commit | `730930d337d171479eadf305f96cbed4bb393e77` |
| Retrieved at | 2026-11-14T19:07:17.648191+00:00 |
| Files in this snapshot | 160 |

## Directory tree

```text
.github/  (8 files)
  ISSUE_TEMPLATE/  (6 files)
    ask_for_help.yaml
    ask_for_help_en_US.yaml
    bug_report.yaml
    bug_report_en_US.yaml
    config.yml
    default.md
  workflows/  (2 files)
    reviewdog.yml
    ruff.yml
cluster/  (3 files)
  __init__.py
  kmeans.py
  train_cluster.py
configs/  (2 files)
  config.json
  diffusion.yaml
configs_template/  (3 files)
  config_template.json
  config_tiny_template.json
  diffusion_template.yaml
dataset_raw/  (1 files)
  wav_structure.txt
diffusion/  (16 files)
  logger/  (3 files)
    __init__.py
    saver.py
    utils.py
  __init__.py
  data_loaders.py
  diffusion.py
  diffusion_onnx.py
  dpm_solver_pytorch.py
  how to export onnx.md
  infer_gt_mel.py
  onnx_export.py
  solver.py
  uni_pc.py
  unit2mel.py
  vocoder.py
  wavenet.py
edgetts/  (2 files)
  tts.py
  tts_voices.py
filelists/  (3 files)
  test.txt
  train.txt
  val.txt
inference/  (4 files)
  __init__.py
  infer_tool.py
  infer_tool_grad.py
  slicer.py
logs/  (2 files)
  44k/  (2 files)
    diffusion/  (1 files)
      … 1 files under this directory
    put_pretrained_model_here
modules/  (29 files)
  F0Predictor/  (21 files)
    fcpe/  (4 files)
      … 4 files under this directory
    rmvpe/  (8 files)
      … 8 files under this directory
    CrepeF0Predictor.py
    DioF0Predictor.py
    F0Predictor.py
    FCPEF0Predictor.py
    HarvestF0Predictor.py
    PMF0Predictor.py
    RMVPEF0Predictor.py
    __init__.py
    crepe.py
  DSConv.py
  __init__.py
  attentions.py
  commons.py
  enhancer.py
  losses.py
  mel_processing.py
  modules.py
onnxexport/  (2 files)
  model_onnx.py
  model_onnx_speaker_mix.py
pretrain/  (4 files)
  nsf_hifigan/  (1 files)
    put_nsf_hifigan_ckpt_here
  __init__.py
  meta.py
  put_hubert_ckpt_here
raw/  (1 files)
  put_raw_wav_here
trained/  (1 files)
  put_trained_checkpoints_here
vdecoder/  (17 files)
  hifigan/  (4 files)
    env.py
    models.py
    nvSTFT.py
    utils.py
  hifiganwithsnake/  (8 files)
    alias/  (4 files)
      … 4 files under this directory
    env.py
    models.py
    nvSTFT.py
    utils.py
  nsf_hifigan/  (4 files)
    env.py
    models.py
    nvSTFT.py
    utils.py
  __init__.py
vencoder/  (33 files)
  dphubert/  (7 files)
    utils/  (2 files)
      … 2 files under this directory
    __init__.py
    components.py
    hardconcrete.py
    model.py
    pruning_utils.py
  hubert/  (3 files)
    __init__.py
    hubert_model.py
    hubert_model_onnx.py
  wavlm/  (2 files)
    WavLM.py
    modules.py
  whisper/  (6 files)
    __init__.py
    audio.py
    decoding.py
    model.py
    tokenizer.py
    utils.py
  CNHubertLarge.py
  ContentVec256L12_Onnx.py
  ContentVec256L9.py
  ContentVec256L9_Onnx.py
  ContentVec768L12.py
  ContentVec768L12_Onnx.py
  ContentVec768L9_Onnx.py
  DPHubert.py
  HubertSoft.py
  HubertSoft_Onnx.py
  WavLMBasePlus.py
  WhisperPPG.py
  WhisperPPGLarge.py
  __init__.py
  encoder.py
.gitattributes
.gitignore
.ruff.toml
LICENSE
README.md
README_zh_CN.md
compress_model.py
data_utils.py
export_index_for_onnx.py
flask_api.py
flask_api_full_song.py
inference_main.py
models.py
onnx_export.py
onnx_export_old.py
preprocess_flist_config.py
preprocess_hubert_f0.py
requirements.txt
requirements_onnx_encoder.txt
requirements_win.txt
resample.py
sovits4_for_colab.ipynb
spkmix.py
train.py
… 5 more files
```

## Entry points

- [cluster/train_cluster.py:54](https://github.com/svc-develop-team/so-vits-svc/blob/730930d337d171479eadf305f96cbed4bb393e77/cluster/train_cluster.py#L54)
- [compress_model.py:51](https://github.com/svc-develop-team/so-vits-svc/blob/730930d337d171479eadf305f96cbed4bb393e77/compress_model.py#L51)
- [diffusion/onnx_export.py:224](https://github.com/svc-develop-team/so-vits-svc/blob/730930d337d171479eadf305f96cbed4bb393e77/diffusion/onnx_export.py#L224)
- [edgetts/tts.py:38](https://github.com/svc-develop-team/so-vits-svc/blob/730930d337d171479eadf305f96cbed4bb393e77/edgetts/tts.py#L38)
- [flask_api.py:12](https://github.com/svc-develop-team/so-vits-svc/blob/730930d337d171479eadf305f96cbed4bb393e77/flask_api.py#L12)
- [flask_api_full_song.py:9](https://github.com/svc-develop-team/so-vits-svc/blob/730930d337d171479eadf305f96cbed4bb393e77/flask_api_full_song.py#L9)
- [inference_main.py:154](https://github.com/svc-develop-team/so-vits-svc/blob/730930d337d171479eadf305f96cbed4bb393e77/inference_main.py#L154)
- [onnx_export.py:140](https://github.com/svc-develop-team/so-vits-svc/blob/730930d337d171479eadf305f96cbed4bb393e77/onnx_export.py#L140)
- [onnx_export_old.py:55](https://github.com/svc-develop-team/so-vits-svc/blob/730930d337d171479eadf305f96cbed4bb393e77/onnx_export_old.py#L55)
- [preprocess_flist_config.py:28](https://github.com/svc-develop-team/so-vits-svc/blob/730930d337d171479eadf305f96cbed4bb393e77/preprocess_flist_config.py#L28)
- [preprocess_hubert_f0.py:130](https://github.com/svc-develop-team/so-vits-svc/blob/730930d337d171479eadf305f96cbed4bb393e77/preprocess_hubert_f0.py#L130)
- [resample.py:88](https://github.com/svc-develop-team/so-vits-svc/blob/730930d337d171479eadf305f96cbed4bb393e77/resample.py#L88)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| cluster package | library | Observed | Groups 2 file(s) under cluster package (observed from repository paths and static analysis). Observed top-level classes: KMeansGPU. Observed top-level functions: _kpp, get_center, get_cluster_center_result, get_cluster_… |
| Configuration and deployment | config | Observed | Groups 8 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 5 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: HParams, InferHParams, TextAudioCollate, TextAudioSpeakerLoader, Volume_Extractor. Observed top-level… |
| Data layer | data | Observed | Groups 8 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AudioEncoder, Conv1d, DiscriminatorP, DiscriminatorS, DotDict, E2E. Observed top-level functions: _init… |
| diffusion package | library | Observed | Groups 14 file(s) under diffusion package (observed from repository paths and static analysis). Observed top-level classes: AfterDiffusion, AudioDataset, Conv1d, DPM_Solver, DiffGtMel, DiffNet. Observed top-level functi… |
| edgetts package | library | Observed | Groups 1 file(s) under edgetts package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 16 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /voiceChangeModel, ROUTE /wav2wav. Observed top… |
| inference package | library | Observed | Groups 4 file(s) under inference package (observed from repository paths and static analysis). Observed top-level classes: F0FilterException, RealTimeVC, Slicer, Svc, VitsSvc. Observed top-level functions: chunks2audio,… |
| modules package | library | Observed | Groups 27 file(s) under modules package (observed from repository paths and static analysis). Observed top-level classes: BasePitchExtractor, BiGRU, BiLSTM, ConformerConvModule, ConvBlockRes, ConvReluNorm. Observed top-… |
| onnxexport package | library | Observed | Groups 2 file(s) under onnxexport package (observed from repository paths and static analysis). Observed top-level classes: DiscriminatorP, DiscriminatorS, Encoder, F0Decoder, ResidualCouplingBlock, SynthesizerTrn. |
| pretrain package | library | Observed | Groups 2 file(s) under pretrain package (observed from repository paths and static analysis). Observed top-level functions: download_dict, get_speech_encoder. |
| vdecoder package | library | Observed | Groups 14 file(s) under vdecoder package (observed from repository paths and static analysis). Observed top-level classes: Activation1d, AttrDict, DownSample1d, LowPassFilter1d, Mish, STFT. Observed top-level functions:… |
| vencoder package | library | Observed | Groups 31 file(s) under vencoder package (observed from repository paths and static analysis). Observed top-level classes: ApplyTimestampRules, BeamSearchDecoder, CNHubertLarge, ContentVec256L12_Onnx, ContentVec256L9, C… |

## Important files

- `.github/ISSUE_TEMPLATE/ask_for_help.yaml` (config)
- `.github/ISSUE_TEMPLATE/ask_for_help_en_US.yaml` (config)
- `.github/ISSUE_TEMPLATE/bug_report.yaml` (config)
- `.github/ISSUE_TEMPLATE/bug_report_en_US.yaml` (config)
- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/workflows/reviewdog.yml` (ci)
- `.github/workflows/ruff.yml` (ci)
- `.ruff.toml` (config)
- `configs/config.json` (config)
- `configs/diffusion.yaml` (config)
- `configs_template/config_template.json` (config)
- `configs_template/config_tiny_template.json` (config)
- `configs_template/diffusion_template.yaml` (config)
- `requirements.txt` (manifest)
- `requirements_onnx_encoder.txt` (manifest)
- `requirements_win.txt` (manifest)

## Top-level layout

- `vencoder` — 33 analysed file(s)
- `(root files)` — 29 analysed file(s)
- `modules` — 29 analysed file(s)
- `vdecoder` — 17 analysed file(s)
- `diffusion` — 16 analysed file(s)
- `.github` — 8 analysed file(s)
- `inference` — 4 analysed file(s)
- `pretrain` — 4 analysed file(s)
- `cluster` — 3 analysed file(s)
- `configs_template` — 3 analysed file(s)
- `filelists` — 3 analysed file(s)
- `configs` — 2 analysed file(s)
- `edgetts` — 2 analysed file(s)
- `logs` — 2 analysed file(s)
- `onnxexport` — 2 analysed file(s)
- `dataset_raw` — 1 analysed file(s)
- `raw` — 1 analysed file(s)
- `trained` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `730930d337d171479eadf305f96cbed4bb393e77` is the revision these paths and observations refer to.
