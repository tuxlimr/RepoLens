# Project structure: microsoft/Bringing-Old-Photos-Back-to-Life

**Analysed commit:** `33875eccf4ebcd3665cf38cc56f3a0ce563d3a9c`

**Commit reference:** [33875eccf4ebcd3665cf38cc56f3a0ce563d3a9c](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life/commit/33875eccf4ebcd3665cf38cc56f3a0ce563d3a9c)

**Tree at this commit:** [microsoft/Bringing-Old-Photos-Back-to-Life@33875eccf4eb](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life/tree/33875eccf4ebcd3665cf38cc56f3a0ce563d3a9c)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | microsoft/Bringing-Old-Photos-Back-to-Life |
| Description | Bringing Old Photo Back to Life (CVPR 2020 oral) |
| Stars | 15691 |
| Forks | 2081 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `33875eccf4ebcd3665cf38cc56f3a0ce563d3a9c` |
| Retrieved at | 2026-11-14T19:09:00.680177+00:00 |
| Files in this snapshot | 75 |

## Directory tree

```text
Face_Detection/  (4 files)
  align_warp_back_multiple_dlib.py
  align_warp_back_multiple_dlib_HR.py
  detect_all_dlib.py
  detect_all_dlib_HR.py
Face_Enhancement/  (23 files)
  data/  (6 files)
    __init__.py
    base_dataset.py
    custom_dataset.py
    face_dataset.py
    image_folder.py
    pix2pix_dataset.py
  models/  (8 files)
    networks/  (6 files)
      … 6 files under this directory
    __init__.py
    pix2pix_model.py
  options/  (3 files)
    __init__.py
    base_options.py
    test_options.py
  util/  (4 files)
    __init__.py
    iter_counter.py
    util.py
    visualizer.py
  requirements.txt
  test_face.py
Global/  (34 files)
  data/  (9 files)
    Create_Bigfile.py
    Load_Bigfile.py
    __init__.py
    base_data_loader.py
    base_dataset.py
    custom_dataset_data_loader.py
    data_loader.py
    image_folder.py
    online_dataset_for_old_photos.py
  detection_models/  (3 files)
    __init__.py
    antialiasing.py
    networks.py
  detection_util/  (1 files)
    util.py
  models/  (8 files)
    NonLocal_feature_mapping_model.py
    __init__.py
    base_model.py
    mapping_model.py
    models.py
    networks.py
    pix2pixHD_model.py
    pix2pixHD_model_DA.py
  options/  (4 files)
    __init__.py
    base_options.py
    test_options.py
    train_options.py
  util/  (4 files)
    __init__.py
    image_pool.py
    util.py
    visualizer.py
  detection.py
  test.py
  train_domain_A.py
  train_domain_B.py
  train_mapping.py
.gitignore
CODE_OF_CONDUCT.md
Dockerfile
GUI.py
LICENSE
README.md
SECURITY.md
ansible.yaml
cog.yaml
download-weights
kubernetes-pod.yml
predict.py
requirements.txt
run.py
```

## Entry points

- [Face_Detection/align_warp_back_multiple_dlib.py:347](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life/blob/33875eccf4ebcd3665cf38cc56f3a0ce563d3a9c/Face_Detection/align_warp_back_multiple_dlib.py#L347)
- [Face_Detection/align_warp_back_multiple_dlib_HR.py:347](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life/blob/33875eccf4ebcd3665cf38cc56f3a0ce563d3a9c/Face_Detection/align_warp_back_multiple_dlib_HR.py#L347)
- [Face_Detection/detect_all_dlib.py:130](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life/blob/33875eccf4ebcd3665cf38cc56f3a0ce563d3a9c/Face_Detection/detect_all_dlib.py#L130)
- [Face_Detection/detect_all_dlib_HR.py:130](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life/blob/33875eccf4ebcd3665cf38cc56f3a0ce563d3a9c/Face_Detection/detect_all_dlib_HR.py#L130)
- [Global/detection.py:168](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life/blob/33875eccf4ebcd3665cf38cc56f3a0ce563d3a9c/Global/detection.py#L168)
- [Global/detection_models/networks.py:301](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life/blob/33875eccf4ebcd3665cf38cc56f3a0ce563d3a9c/Global/detection_models/networks.py#L301)
- [Global/test.py:95](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life/blob/33875eccf4ebcd3665cf38cc56f3a0ce563d3a9c/Global/test.py#L95)
- [run.py:17](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life/blob/33875eccf4ebcd3665cf38cc56f3a0ce563d3a9c/run.py#L17)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 6 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 2 file(s) under core modules (observed from repository paths and static analysis). Observed top-level classes: Predictor. Observed top-level functions: clean_folder, modify. |
| Data layer | data | Observed | Groups 31 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: BaseDataLoader, BaseDataset, BaseModel, BaseNetwork, BigFileMemoryLoader, ConvEncoder. Observed top-le… |
| Application entry point | entrypoint | Observed | Groups 8 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: UNet, UNetConvBlock, UNetUpBlock, UnetGenerator, UnetSkipConnectionBlock. Observed top-lev… |
| Face_Enhancement package | library | Observed | Groups 6 file(s) under face_enhancement package (observed from repository paths and static analysis). Observed top-level classes: BaseOptions, Colorize, IterationCounter, Visualizer. Observed top-level functions: atoi,… |
| Global package | library | Observed | Groups 13 file(s) under global package (observed from repository paths and static analysis). Observed top-level classes: BaseOptions, Downsample, ImagePool, Timer, TrainOptions, Visualizer. Observed top-level functions:… |
| Tests | test | Observed | Groups 3 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: TestOptions. |

## Important files

- `Dockerfile` (container)
- `Face_Enhancement/requirements.txt` (manifest)
- `ansible.yaml` (config)
- `cog.yaml` (config)
- `kubernetes-pod.yml` (config)
- `requirements.txt` (manifest)

## Top-level layout

- `Global` — 34 analysed file(s)
- `Face_Enhancement` — 23 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `Face_Detection` — 4 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `33875eccf4ebcd3665cf38cc56f3a0ce563d3a9c` is the revision these paths and observations refer to.
