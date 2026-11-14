# Project structure: facebookresearch/Detectron

**Analysed commit:** `04155a01a6ea68f22ac27c79a822066457941ece`

**Commit reference:** [04155a01a6ea68f22ac27c79a822066457941ece](https://github.com/facebookresearch/Detectron/commit/04155a01a6ea68f22ac27c79a822066457941ece)

**Tree at this commit:** [facebookresearch/Detectron@04155a01a6ea](https://github.com/facebookresearch/Detectron/tree/04155a01a6ea68f22ac27c79a822066457941ece)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | facebookresearch/Detectron |
| Description | FAIR's research platform for object detection research, implementing popular algorithms like Mask R-CNN and RetinaNet. |
| Stars | 26335 |
| Forks | 5373 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `04155a01a6ea68f22ac27c79a822066457941ece` |
| Retrieved at | 2026-11-14T19:07:23.494798+00:00 |
| Files in this snapshot | 210 |

## Directory tree

```text
.github/  (1 files)
  issue_template.md
cmake/  (7 files)
  legacy/  (6 files)
    Modules/  (1 files)
      … 1 files under this directory
    Cuda.cmake
    Dependencies.cmake
    Summary.cmake
    Utils.cmake
    legacymake.cmake
  Summary.cmake
configs/  (87 files)
  04_2018_gn_baselines/  (7 files)
    e2e_mask_rcnn_R-101-FPN_2x_gn.yaml
    e2e_mask_rcnn_R-101-FPN_3x_gn.yaml
    e2e_mask_rcnn_R-50-FPN_2x_gn.yaml
    e2e_mask_rcnn_R-50-FPN_3x_gn.yaml
    mask_rcnn_R-50-FPN_1x_gn.yaml
    scratch_e2e_mask_rcnn_R-101-FPN_3x_gn.yaml
    scratch_e2e_mask_rcnn_R-50-FPN_3x_gn.yaml
  12_2017_baselines/  (74 files)
    e2e_faster_rcnn_R-101-FPN_1x.yaml
    e2e_faster_rcnn_R-101-FPN_2x.yaml
    e2e_faster_rcnn_R-50-C4_1x.yaml
    e2e_faster_rcnn_R-50-C4_2x.yaml
    e2e_faster_rcnn_R-50-FPN_1x.yaml
    e2e_faster_rcnn_R-50-FPN_2x.yaml
    e2e_faster_rcnn_X-101-32x8d-FPN_1x.yaml
    e2e_faster_rcnn_X-101-32x8d-FPN_2x.yaml
    e2e_faster_rcnn_X-101-64x4d-FPN_1x.yaml
    e2e_faster_rcnn_X-101-64x4d-FPN_2x.yaml
    e2e_keypoint_rcnn_R-101-FPN_1x.yaml
    e2e_keypoint_rcnn_R-101-FPN_s1x.yaml
    e2e_keypoint_rcnn_R-50-FPN_1x.yaml
    e2e_keypoint_rcnn_R-50-FPN_s1x.yaml
    e2e_keypoint_rcnn_X-101-32x8d-FPN_1x.yaml
    e2e_keypoint_rcnn_X-101-32x8d-FPN_s1x.yaml
    e2e_keypoint_rcnn_X-101-64x4d-FPN_1x.yaml
    e2e_keypoint_rcnn_X-101-64x4d-FPN_s1x.yaml
    e2e_mask_rcnn_R-101-FPN_1x.yaml
    e2e_mask_rcnn_R-101-FPN_2x.yaml
    e2e_mask_rcnn_R-50-C4_1x.yaml
    e2e_mask_rcnn_R-50-C4_2x.yaml
    e2e_mask_rcnn_R-50-FPN_1x.yaml
    e2e_mask_rcnn_R-50-FPN_2x.yaml
    … 50 more files
  getting_started/  (4 files)
    tutorial_1gpu_e2e_faster_rcnn_R-50-FPN.yaml
    tutorial_2gpu_e2e_faster_rcnn_R-50-FPN.yaml
    tutorial_4gpu_e2e_faster_rcnn_R-50-FPN.yaml
    tutorial_8gpu_e2e_faster_rcnn_R-50-FPN.yaml
  test_time_aug/  (2 files)
    e2e_mask_rcnn_R-50-FPN_2x.yaml
    keypoint_rcnn_R-50-FPN_1x.yaml
demo/  (1 files)
  NOTICE
detectron/  (86 files)
  core/  (6 files)
    __init__.py
    config.py
    rpn_generator.py
    test.py
    test_engine.py
    test_retinanet.py
  datasets/  (15 files)
    VOCdevkit-matlab-wrapper/  (3 files)
      … 3 files under this directory
    data/  (1 files)
      … 1 files under this directory
    __init__.py
    cityscapes_json_dataset_evaluator.py
    coco_to_cityscapes_id.py
    dataset_catalog.py
    dummy_datasets.py
    json_dataset.py
    json_dataset_evaluator.py
    roidb.py
    task_evaluation.py
    voc_dataset_evaluator.py
    voc_eval.py
  modeling/  (16 files)
    FPN.py
    ResNet.py
    VGG16.py
    VGG_CNN_M_1024.py
    __init__.py
    detector.py
    fast_rcnn_heads.py
    generate_anchors.py
    keypoint_rcnn_heads.py
    mask_rcnn_heads.py
    model_builder.py
    name_compat.py
    optimizer.py
    retinanet_heads.py
    rfcn_heads.py
    rpn_heads.py
  ops/  (7 files)
    __init__.py
    collect_and_distribute_fpn_rpn_proposals.py
    generate_proposal_labels.py
    generate_proposals.py
    zero_even_op.cc
    zero_even_op.cu
    zero_even_op.h
  roi_data/  (9 files)
    __init__.py
    data_utils.py
    fast_rcnn.py
    keypoint_rcnn.py
    loader.py
    mask_rcnn.py
    minibatch.py
    retinanet.py
    rpn.py
  tests/  (9 files)
    data_loader_benchmark.py
    test_batch_permutation_op.py
    test_bbox_transform.py
    test_cfg.py
    test_loader.py
    test_restore_checkpoint.py
    test_smooth_l1_loss_op.py
    test_spatial_narrow_as_op.py
    test_zero_even_op.py
  utils/  (23 files)
    __init__.py
    blob.py
    boxes.py
    c2.py
    collections.py
    colormap.py
    coordinator.py
    cython_bbox.pyx
    cython_nms.pyx
    env.py
    image.py
    io.py
    keypoints.py
    logging.py
    lr_policy.py
    model_convert_utils.py
    net.py
    segms.py
    subprocess.py
    timer.py
    train.py
    training_stats.py
    vis.py
  __init__.py
docker/  (1 files)
  Dockerfile
projects/  (1 files)
  GN/  (1 files)
    README.md
tools/  (12 files)
  convert_cityscapes_to_coco.py
  convert_coco_model_to_cityscapes.py
  convert_pkl_to_pb.py
  convert_selective_search.py
  generate_testdev_from_test.py
  infer.py
  infer_simple.py
  pickle_caffe_blobs.py
  reval.py
  test_net.py
  train_net.py
  visualize_results.py
.gitignore
CMakeLists.txt
CODE_OF_CONDUCT.md
CONTRIBUTING.md
FAQ.md
GETTING_STARTED.md
INSTALL.md
LICENSE
MODEL_ZOO.md
Makefile
NOTICE
README.md
requirements.txt
setup.py
```

## Entry points

- [tools/convert_cityscapes_to_coco.py:212](https://github.com/facebookresearch/Detectron/blob/04155a01a6ea68f22ac27c79a822066457941ece/tools/convert_cityscapes_to_coco.py#L212)
- [tools/convert_coco_model_to_cityscapes.py:119](https://github.com/facebookresearch/Detectron/blob/04155a01a6ea68f22ac27c79a822066457941ece/tools/convert_coco_model_to_cityscapes.py#L119)
- [tools/convert_pkl_to_pb.py:695](https://github.com/facebookresearch/Detectron/blob/04155a01a6ea68f22ac27c79a822066457941ece/tools/convert_pkl_to_pb.py#L695)
- [tools/convert_selective_search.py:35](https://github.com/facebookresearch/Detectron/blob/04155a01a6ea68f22ac27c79a822066457941ece/tools/convert_selective_search.py#L35)
- [tools/generate_testdev_from_test.py:94](https://github.com/facebookresearch/Detectron/blob/04155a01a6ea68f22ac27c79a822066457941ece/tools/generate_testdev_from_test.py#L94)
- [tools/infer.py:193](https://github.com/facebookresearch/Detectron/blob/04155a01a6ea68f22ac27c79a822066457941ece/tools/infer.py#L193)
- [tools/infer_simple.py:181](https://github.com/facebookresearch/Detectron/blob/04155a01a6ea68f22ac27c79a822066457941ece/tools/infer_simple.py#L181)
- [tools/pickle_caffe_blobs.py:215](https://github.com/facebookresearch/Detectron/blob/04155a01a6ea68f22ac27c79a822066457941ece/tools/pickle_caffe_blobs.py#L215)
- [tools/reval.py:105](https://github.com/facebookresearch/Detectron/blob/04155a01a6ea68f22ac27c79a822066457941ece/tools/reval.py#L105)
- [tools/train_net.py:131](https://github.com/facebookresearch/Detectron/blob/04155a01a6ea68f22ac27c79a822066457941ece/tools/train_net.py#L131)
- [tools/visualize_results.py:135](https://github.com/facebookresearch/Detectron/blob/04155a01a6ea68f22ac27c79a822066457941ece/tools/visualize_results.py#L135)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 91 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level functions: _check_and_coerce_cfg_value_type, _decode_cfg_value, _key_is_deprecated, _key_is_r… |
| detectron package | library | Observed | Groups 63 file(s) under detectron package (observed from repository paths and static analysis). Observed top-level classes: AttrDict, CollectAndDistributeFpnRpnProposalsOp, Coordinator, DetectionModelHelper, GeneratePro… |
| Application entry point | entrypoint | Observed | Groups 10 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level functions: _export_to_logfiledb, _get_result_blobs, _prepare_blobs, _save_image_graphs, _save_mode… |
| Service / domain layer | service | Observed | Groups 3 file(s) under service / domain layer (observed from repository paths and static analysis). Observed top-level functions: _add_multilevel_rois_for_test, _get_blobs, _get_rois_blob, _project_im_rois, box_results_… |
| Tests | test | Observed | Groups 13 file(s) under tests (observed from repository paths and static analysis). Observed routes: PATCH detectron.roi_data.loader.get_minibatch_blob_names, PATCH detectron.roi_data.loader.get_minibatch. Observed top-… |

## Important files

- `configs/04_2018_gn_baselines/e2e_mask_rcnn_R-101-FPN_2x_gn.yaml` (config)
- `configs/04_2018_gn_baselines/e2e_mask_rcnn_R-101-FPN_3x_gn.yaml` (config)
- `configs/04_2018_gn_baselines/e2e_mask_rcnn_R-50-FPN_2x_gn.yaml` (config)
- `configs/04_2018_gn_baselines/e2e_mask_rcnn_R-50-FPN_3x_gn.yaml` (config)
- `configs/04_2018_gn_baselines/mask_rcnn_R-50-FPN_1x_gn.yaml` (config)
- `configs/04_2018_gn_baselines/scratch_e2e_mask_rcnn_R-101-FPN_3x_gn.yaml` (config)
- `configs/04_2018_gn_baselines/scratch_e2e_mask_rcnn_R-50-FPN_3x_gn.yaml` (config)
- `configs/12_2017_baselines/e2e_faster_rcnn_R-101-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/e2e_faster_rcnn_R-101-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/e2e_faster_rcnn_R-50-C4_1x.yaml` (config)
- `configs/12_2017_baselines/e2e_faster_rcnn_R-50-C4_2x.yaml` (config)
- `configs/12_2017_baselines/e2e_faster_rcnn_R-50-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/e2e_faster_rcnn_R-50-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/e2e_faster_rcnn_X-101-32x8d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/e2e_faster_rcnn_X-101-32x8d-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/e2e_faster_rcnn_X-101-64x4d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/e2e_faster_rcnn_X-101-64x4d-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/e2e_keypoint_rcnn_R-101-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/e2e_keypoint_rcnn_R-101-FPN_s1x.yaml` (config)
- `configs/12_2017_baselines/e2e_keypoint_rcnn_R-50-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/e2e_keypoint_rcnn_R-50-FPN_s1x.yaml` (config)
- `configs/12_2017_baselines/e2e_keypoint_rcnn_X-101-32x8d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/e2e_keypoint_rcnn_X-101-32x8d-FPN_s1x.yaml` (config)
- `configs/12_2017_baselines/e2e_keypoint_rcnn_X-101-64x4d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/e2e_keypoint_rcnn_X-101-64x4d-FPN_s1x.yaml` (config)
- `configs/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/e2e_mask_rcnn_R-50-C4_1x.yaml` (config)
- `configs/12_2017_baselines/e2e_mask_rcnn_R-50-C4_2x.yaml` (config)
- `configs/12_2017_baselines/e2e_mask_rcnn_R-50-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/e2e_mask_rcnn_R-50-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/e2e_mask_rcnn_X-101-32x8d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/e2e_mask_rcnn_X-101-32x8d-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/e2e_mask_rcnn_X-101-64x4d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/e2e_mask_rcnn_X-101-64x4d-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/e2e_mask_rcnn_X-152-32x8d-FPN-IN5k_1.44x.yaml` (config)
- `configs/12_2017_baselines/fast_rcnn_R-101-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/fast_rcnn_R-101-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/fast_rcnn_R-50-C4_1x.yaml` (config)
- `configs/12_2017_baselines/fast_rcnn_R-50-C4_2x.yaml` (config)
- `configs/12_2017_baselines/fast_rcnn_R-50-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/fast_rcnn_R-50-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/fast_rcnn_X-101-32x8d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/fast_rcnn_X-101-32x8d-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/fast_rcnn_X-101-64x4d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/fast_rcnn_X-101-64x4d-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/keypoint_rcnn_R-101-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/keypoint_rcnn_R-101-FPN_s1x.yaml` (config)
- `configs/12_2017_baselines/keypoint_rcnn_R-50-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/keypoint_rcnn_R-50-FPN_s1x.yaml` (config)
- `configs/12_2017_baselines/keypoint_rcnn_X-101-32x8d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/keypoint_rcnn_X-101-32x8d-FPN_s1x.yaml` (config)
- `configs/12_2017_baselines/keypoint_rcnn_X-101-64x4d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/keypoint_rcnn_X-101-64x4d-FPN_s1x.yaml` (config)
- `configs/12_2017_baselines/mask_rcnn_R-101-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/mask_rcnn_R-101-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/mask_rcnn_R-50-C4_1x.yaml` (config)
- `configs/12_2017_baselines/mask_rcnn_R-50-C4_2x.yaml` (config)
- `configs/12_2017_baselines/mask_rcnn_R-50-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/mask_rcnn_R-50-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/mask_rcnn_X-101-32x8d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/mask_rcnn_X-101-32x8d-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/mask_rcnn_X-101-64x4d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/mask_rcnn_X-101-64x4d-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/retinanet_R-101-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/retinanet_R-101-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/retinanet_R-50-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/retinanet_R-50-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/retinanet_X-101-32x8d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/retinanet_X-101-32x8d-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/retinanet_X-101-64x4d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/retinanet_X-101-64x4d-FPN_2x.yaml` (config)
- `configs/12_2017_baselines/rpn_R-101-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/rpn_R-50-C4_1x.yaml` (config)
- `configs/12_2017_baselines/rpn_R-50-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/rpn_X-101-32x8d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/rpn_X-101-64x4d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/rpn_person_only_R-101-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/rpn_person_only_R-50-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/rpn_person_only_X-101-32x8d-FPN_1x.yaml` (config)
- `configs/12_2017_baselines/rpn_person_only_X-101-64x4d-FPN_1x.yaml` (config)
- `configs/getting_started/tutorial_1gpu_e2e_faster_rcnn_R-50-FPN.yaml` (config)
- `configs/getting_started/tutorial_2gpu_e2e_faster_rcnn_R-50-FPN.yaml` (config)
- `configs/getting_started/tutorial_4gpu_e2e_faster_rcnn_R-50-FPN.yaml` (config)
- `configs/getting_started/tutorial_8gpu_e2e_faster_rcnn_R-50-FPN.yaml` (config)
- `configs/test_time_aug/e2e_mask_rcnn_R-50-FPN_2x.yaml` (config)
- `configs/test_time_aug/keypoint_rcnn_R-50-FPN_1x.yaml` (config)
- `docker/Dockerfile` (container)
- `requirements.txt` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `configs` — 87 analysed file(s)
- `detectron` — 86 analysed file(s)
- `(root files)` — 14 analysed file(s)
- `tools` — 12 analysed file(s)
- `cmake` — 7 analysed file(s)
- `.github` — 1 analysed file(s)
- `demo` — 1 analysed file(s)
- `docker` — 1 analysed file(s)
- `projects` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.
- The GitHub repository was marked archived at selection time.

Commit `04155a01a6ea68f22ac27c79a822066457941ece` is the revision these paths and observations refer to.
