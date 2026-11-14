# Project structure: davidsandberg/facenet

**Analysed commit:** `096ed770f163957c1e56efa7feeb194773920f6e`

**Commit reference:** [096ed770f163957c1e56efa7feeb194773920f6e](https://github.com/davidsandberg/facenet/commit/096ed770f163957c1e56efa7feeb194773920f6e)

**Tree at this commit:** [davidsandberg/facenet@096ed770f163](https://github.com/davidsandberg/facenet/tree/096ed770f163957c1e56efa7feeb194773920f6e)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | davidsandberg/facenet |
| Description | Face recognition using Tensorflow |
| Stars | 14364 |
| Forks | 4766 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `096ed770f163957c1e56efa7feeb194773920f6e` |
| Retrieved at | 2026-11-14T19:09:27.399498+00:00 |
| Files in this snapshot | 91 |

## Directory tree

```text
contributed/  (8 files)
  __init__.py
  batch_represent.py
  cluster.py
  clustering.py
  export_embeddings.py
  face.py
  predict.py
  real_time_face_recognition.py
data/  (5 files)
  learning_rate_retrain_tripletloss.txt
  learning_rate_schedule_classifier_casia.txt
  learning_rate_schedule_classifier_msceleb.txt
  learning_rate_schedule_classifier_vggface2.txt
  pairs.txt
src/  (29 files)
  align/  (3 files)
    __init__.py
    align_dataset_mtcnn.py
    detect_face.py
  generative/  (9 files)
    models/  (5 files)
      … 5 files under this directory
    __init__.py
    calculate_attribute_vectors.py
    modify_attribute.py
    train_vae.py
  models/  (5 files)
    __init__.py
    dummy.py
    inception_resnet_v1.py
    inception_resnet_v2.py
    squeezenet.py
  __init__.py
  calculate_filtering_metrics.py
  classifier.py
  compare.py
  decode_msceleb_dataset.py
  download_and_extract.py
  facenet.py
  freeze_graph.py
  lfw.py
  train_softmax.py
  train_tripletloss.py
  validate_on_lfw.py
test/  (5 files)
  batch_norm_test.py
  center_loss_test.py
  restore_test.py
  train_test.py
  triplet_loss_test.py
tmp/  (34 files)
  __init__.py
  align_dataset.m
  align_dataset.py
  align_dlib.py
  cacd2000_split_identities.py
  dataset_read_speed.py
  deepdream.py
  detect_face_v1.m
  detect_face_v2.m
  download_vgg_face_dataset.py
  funnel_dataset.py
  invariance_test.txt
  mnist_center_loss.py
  mnist_noise_labels.py
  mtcnn.py
  mtcnn_test.py
  mtcnn_test_pnet_dbg.py
  network.py
  nn2.py
  nn3.py
  nn4.py
  nn4_small2_v1.py
  random_test.py
  rename_casia_directories.py
  … 10 more files
util/  (1 files)
  plot_learning_curves.m
.gitignore
.project
.pydevproject
.pylintrc
.travis.yml
LICENSE.md
README.md
__init__.py
requirements.txt
```

## Entry points

- [src/align/align_dataset_mtcnn.py:158](https://github.com/davidsandberg/facenet/blob/096ed770f163957c1e56efa7feeb194773920f6e/src/align/align_dataset_mtcnn.py#L158)
- [src/calculate_filtering_metrics.py:127](https://github.com/davidsandberg/facenet/blob/096ed770f163957c1e56efa7feeb194773920f6e/src/calculate_filtering_metrics.py#L127)
- [src/classifier.py:169](https://github.com/davidsandberg/facenet/blob/096ed770f163957c1e56efa7feeb194773920f6e/src/classifier.py#L169)
- [src/compare.py:129](https://github.com/davidsandberg/facenet/blob/096ed770f163957c1e56efa7feeb194773920f6e/src/compare.py#L129)
- [src/decode_msceleb_dataset.py:78](https://github.com/davidsandberg/facenet/blob/096ed770f163957c1e56efa7feeb194773920f6e/src/decode_msceleb_dataset.py#L78)
- [src/freeze_graph.py:102](https://github.com/davidsandberg/facenet/blob/096ed770f163957c1e56efa7feeb194773920f6e/src/freeze_graph.py#L102)
- [src/generative/calculate_attribute_vectors.py:199](https://github.com/davidsandberg/facenet/blob/096ed770f163957c1e56efa7feeb194773920f6e/src/generative/calculate_attribute_vectors.py#L199)
- [src/generative/modify_attribute.py:141](https://github.com/davidsandberg/facenet/blob/096ed770f163957c1e56efa7feeb194773920f6e/src/generative/modify_attribute.py#L141)
- [src/generative/train_vae.py:283](https://github.com/davidsandberg/facenet/blob/096ed770f163957c1e56efa7feeb194773920f6e/src/generative/train_vae.py#L283)
- [src/train_softmax.py:579](https://github.com/davidsandberg/facenet/blob/096ed770f163957c1e56efa7feeb194773920f6e/src/train_softmax.py#L579)
- [src/train_tripletloss.py:485](https://github.com/davidsandberg/facenet/blob/096ed770f163957c1e56efa7feeb194773920f6e/src/train_tripletloss.py#L485)
- [src/validate_on_lfw.py:163](https://github.com/davidsandberg/facenet/blob/096ed770f163957c1e56efa7feeb194773920f6e/src/validate_on_lfw.py#L163)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| align package | library | Observed | Groups 2 file(s) under align package (observed from repository paths and static analysis). Observed top-level classes: Network, ONet, PNet, RNet. Observed top-level functions: bbreg, bulk_detect_face, create_mtcnn, dete… |
| Configuration and deployment | config | Observed | Groups 1 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| contributed package | library | Observed | Groups 2 file(s) under contributed package (observed from repository paths and static analysis). Observed top-level classes: Detection, Encoder, Face, Identifier, Recognition. |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 10 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: Vae. Observed top-level functions: block17, block35, block8, conv2d_block, expand, fire_module. |
| download_and_extract.py package | library | Observed | Groups 1 file(s) under download_and_extract.py package (observed from repository paths and static analysis). Observed top-level functions: download_and_extract_file, download_file_from_google_drive, get_confirm_token, s… |
| Application entry point | entrypoint | Observed | Groups 29 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: T, TemporaryDirectory, _chinese_whispers, add_overlays, align_data, cluster_facial_enco… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| facenet.py package | library | Observed | Groups 1 file(s) under facenet.py package (observed from repository paths and static analysis). Observed top-level classes: ImageClass. Observed top-level functions: _add_loss_summaries, calculate_accuracy, calculate_ro… |
| generative package | library | Observed | Groups 1 file(s) under generative package (observed from repository paths and static analysis). |
| __init__.py package | library | Observed | Groups 1 file(s) under __init__.py package (observed from repository paths and static analysis). |
| lfw.py package | library | Observed | Groups 1 file(s) under lfw.py package (observed from repository paths and static analysis). Observed top-level functions: add_extension, evaluate, get_paths, read_pairs. |
| Tests | test | Observed | Groups 11 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: BatchNormTest, CenterLossTest, DemuxEmbeddingsTest, TrainTest. Observed top-level functions: _affine, _conv… |
| tmp package | library | Observed | Groups 13 file(s) under tmp package (observed from repository paths and static analysis). Observed top-level classes: AlignDlib. Observed top-level functions: affine, apool, batch_norm, conv, inception, inference. |

## Important files

- `.travis.yml` (ci)
- `requirements.txt` (manifest)

## Top-level layout

- `tmp` — 34 analysed file(s)
- `src` — 29 analysed file(s)
- `(root files)` — 9 analysed file(s)
- `contributed` — 8 analysed file(s)
- `data` — 5 analysed file(s)
- `test` — 5 analysed file(s)
- `util` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `096ed770f163957c1e56efa7feeb194773920f6e` is the revision these paths and observations refer to.
