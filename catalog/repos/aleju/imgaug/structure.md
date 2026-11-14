# Project structure: aleju/imgaug

**Analysed commit:** `0101108d4fed06bc5056c4a03e2bcb0216dac326`

**Commit reference:** [0101108d4fed06bc5056c4a03e2bcb0216dac326](https://github.com/aleju/imgaug/commit/0101108d4fed06bc5056c4a03e2bcb0216dac326)

**Tree at this commit:** [aleju/imgaug@0101108d4fed](https://github.com/aleju/imgaug/tree/0101108d4fed06bc5056c4a03e2bcb0216dac326)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | aleju/imgaug |
| Description | Image augmentation for machine learning experiments. |
| Stars | 14739 |
| Forks | 2445 |
| Licence | MIT |
| Language | Python |
| Default branch | master |
| Analysed commit | `0101108d4fed06bc5056c4a03e2bcb0216dac326` |
| Retrieved at | 2026-11-14T19:09:17.574385+00:00 |
| Files in this snapshot | 283 |

## Directory tree

```text
.github/  (3 files)
  workflows/  (3 files)
    build_wheels.yml
    test_master.yml
    test_pull_requests.yml
changelogs/  (119 files)
  0.3.0/  (2 files)
    v0.3.0.cleaned.md
    v0.3.0.uncleaned.md
  0.4.0/  (80 files)
    added/  (32 files)
      … 32 files under this directory
    changed/  (8 files)
      … 8 files under this directory
    deprecated/  (2 files)
      … 2 files under this directory
    fixed/  (25 files)
      … 25 files under this directory
    refactored/  (2 files)
      … 2 files under this directory
    renamed/  (1 files)
      … 1 files under this directory
    20191003_reworked_aug_methods.md
    20191016_pooling_affects_maps.md
    20191026_reworked_quantization.md
    20191027_improve_invert.md
    20191111_pickleable.md
    20191113_iterable_augmentables.md
    20191610_crop_and_pad.md
    20191610_perspective_transform.md
    20200107_improved_blending.md
    20200126_python38.md
  master/  (33 files)
    changed/  (2 files)
      … 2 files under this directory
    fixed/  (10 files)
      … 10 files under this directory
    improved/  (18 files)
      … 18 files under this directory
    refactored/  (2 files)
      … 2 files under this directory
    20200206_data_module.md
  v0.2.8.summary.md
  v0.2.9.summary.md
  v0.3.0.summary.md
  v0.4.0.summary.md
checks/  (67 files)
  README.md
  check_add_to_hue_and_saturation.py
  check_affine.py
  check_affinecv2.py
  check_average_blur.py
  check_background_augmentation.py
  check_bb_augmentation.py
  check_bilateral_blur.py
  check_blendalphasegmapclassids.py
  check_blendalphasomecolors.py
  check_brightness.py
  check_canny.py
  check_cartoon.py
  check_channel_shuffle.py
  check_clouds.py
  check_color_temperature.py
  check_contrast.py
  check_crop_and_pad.py
  check_cutout.py
  check_deprecation_warning.py
  check_directed_edge_detect.py
  check_elastic_transformation.py
  check_fast_snowy_landscape.py
  check_fixed_size.py
  … 43 more files
imgaug/  (44 files)
  augmentables/  (11 files)
    __init__.py
    base.py
    batches.py
    bbs.py
    heatmaps.py
    kps.py
    lines.py
    normalization.py
    polys.py
    segmaps.py
    utils.py
  augmenters/  (18 files)
    __init__.py
    artistic.py
    base.py
    blend.py
    blur.py
    collections.py
    color.py
    contrast.py
    convolutional.py
    debug.py
    edges.py
    flip.py
    imgcorruptlike.py
    overlay.py
    pillike.py
    pooling.py
    segmentation.py
    weather.py
  external/  (5 files)
    README.md
    __init__.py
    opensimplex.py
    poly_point_isect_py2py3.py
    poly_point_isect_py3.py.bak
  __init__.py
  data.py
  dtypes.py
  imgaug.py
  multicore.py
  parameters.py
  quokka_annotations.json
  random.py
  testutils.py
  validation.py
test/  (35 files)
  augmentables/  (9 files)
    test_batches.py
    test_bbs.py
    test_heatmaps.py
    test_kps.py
    test_lines.py
    test_normalization.py
    test_polys.py
    test_segmaps.py
    test_utils.py
  augmenters/  (17 files)
    test_artistic.py
    test_blend.py
    test_blur.py
    test_collections.py
    test_color.py
    test_contrast.py
    test_convolutional.py
    test_debug.py
    test_edges.py
    test_flip.py
    test_imgcorruptlike.py
    test_mixed_files.py
    test_overlay.py
    test_pillike.py
    test_pooling.py
    test_segmentation.py
    test_weather.py
  requirements.txt
  run_doctests.sh
  run_tests.sh
  test_data.py
  test_dtypes.py
  test_imgaug.py
  test_multicore.py
  test_parameters.py
  test_random.py
.codacy.yml
.gitignore
.pylintrc
.travis.yml
CHANGELOG.md
LICENSE
MANIFEST.in
README.md
bandit.yml
codecov.yml
pytest.ini
readthedocs.yml
requirements.txt
setup.cfg
setup.py
```

## Entry points

- [checks/check_add_to_hue_and_saturation.py:41](https://github.com/aleju/imgaug/blob/0101108d4fed06bc5056c4a03e2bcb0216dac326/checks/check_add_to_hue_and_saturation.py#L41)
- [checks/check_affine.py:129](https://github.com/aleju/imgaug/blob/0101108d4fed06bc5056c4a03e2bcb0216dac326/checks/check_affine.py#L129)
- [checks/check_affinecv2.py:91](https://github.com/aleju/imgaug/blob/0101108d4fed06bc5056c4a03e2bcb0216dac326/checks/check_affinecv2.py#L91)
- [checks/check_average_blur.py:49](https://github.com/aleju/imgaug/blob/0101108d4fed06bc5056c4a03e2bcb0216dac326/checks/check_average_blur.py#L49)
- [checks/check_background_augmentation.py:305](https://github.com/aleju/imgaug/blob/0101108d4fed06bc5056c4a03e2bcb0216dac326/checks/check_background_augmentation.py#L305)
- [checks/check_bb_augmentation.py:56](https://github.com/aleju/imgaug/blob/0101108d4fed06bc5056c4a03e2bcb0216dac326/checks/check_bb_augmentation.py#L56)
- [checks/check_bilateral_blur.py:54](https://github.com/aleju/imgaug/blob/0101108d4fed06bc5056c4a03e2bcb0216dac326/checks/check_bilateral_blur.py#L54)
- [checks/check_blendalphasegmapclassids.py:34](https://github.com/aleju/imgaug/blob/0101108d4fed06bc5056c4a03e2bcb0216dac326/checks/check_blendalphasegmapclassids.py#L34)
- [checks/check_blendalphasomecolors.py:44](https://github.com/aleju/imgaug/blob/0101108d4fed06bc5056c4a03e2bcb0216dac326/checks/check_blendalphasomecolors.py#L44)
- [checks/check_brightness.py:37](https://github.com/aleju/imgaug/blob/0101108d4fed06bc5056c4a03e2bcb0216dac326/checks/check_brightness.py#L37)
- [checks/check_canny.py:38](https://github.com/aleju/imgaug/blob/0101108d4fed06bc5056c4a03e2bcb0216dac326/checks/check_canny.py#L38)
- [checks/check_cartoon.py:73](https://github.com/aleju/imgaug/blob/0101108d4fed06bc5056c4a03e2bcb0216dac326/checks/check_cartoon.py#L73)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 9 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: check_alternative_installation, get_install_requirements. |
| Application entry point | entrypoint | Observed | Groups 66 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Dummy1, Dummy2, Dummy3, ElasticTransformationCv2, ElasticTransformationScipy, PoolWithMar… |
| External integrations | external | Observed | Groups 3 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: Event, EventQueue, Node, OpenSimplex, RBTree, SweepLine. Observed top-level functions: dot_v… |
| imgaug package | library | Observed | Groups 38 file(s) under imgaug package (observed from repository paths and static analysis). Observed top-level classes: Absolute, Add, AddToBrightness, AddToHue, AddToHueAndSaturation, AddToSaturation. Observed top-lev… |
| Tests | test | Observed | Groups 35 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH imgaug.augmentables.bbs._LabelOnImageDrawer, PATCH imgaug.augmentables.bbs._LabelOnImageDrawer, PATCH imgaug.aug… |

## Important files

- `.codacy.yml` (config)
- `.github/workflows/build_wheels.yml` (ci)
- `.github/workflows/test_master.yml` (ci)
- `.github/workflows/test_pull_requests.yml` (ci)
- `.travis.yml` (ci)
- `MANIFEST.in` (manifest)
- `bandit.yml` (config)
- `codecov.yml` (config)
- `imgaug/quokka_annotations.json` (config)
- `pytest.ini` (config)
- `readthedocs.yml` (config)
- `requirements.txt` (manifest)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `changelogs` — 119 analysed file(s)
- `checks` — 67 analysed file(s)
- `imgaug` — 44 analysed file(s)
- `test` — 35 analysed file(s)
- `(root files)` — 15 analysed file(s)
- `.github` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `0101108d4fed06bc5056c4a03e2bcb0216dac326` is the revision these paths and observations refer to.
