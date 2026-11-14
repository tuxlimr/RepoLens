# Project structure: facebookresearch/detectron2

**Analysed commit:** `247691a1c292654867deb35cabb27f18d75a1363`

**Commit reference:** [247691a1c292654867deb35cabb27f18d75a1363](https://github.com/facebookresearch/detectron2/commit/247691a1c292654867deb35cabb27f18d75a1363)

**Tree at this commit:** [facebookresearch/detectron2@247691a1c292](https://github.com/facebookresearch/detectron2/tree/247691a1c292654867deb35cabb27f18d75a1363)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | facebookresearch/detectron2 |
| Description | Detectron2 is a platform for object detection, segmentation and other visual recognition tasks. |
| Stars | 34984 |
| Forks | 7939 |
| Licence | Apache-2.0 |
| Language | Python |
| Default branch | main |
| Analysed commit | `247691a1c292654867deb35cabb27f18d75a1363` |
| Retrieved at | 2026-11-14T19:06:57.201935+00:00 |
| Files in this snapshot | 800 |

## Directory tree

```text
.github/  (24 files)
  ISSUE_TEMPLATE/  (5 files)
    bugs.md
    config.yml
    documentation.md
    feature-request.md
    unexpected-problems-bugs.md
  actions/  (8 files)
    install_detectron2/  (1 files)
      … 1 files under this directory
    install_detectron2_win/  (1 files)
      … 1 files under this directory
    install_linux_dep/  (1 files)
      … 1 files under this directory
    install_linux_gpu_dep/  (1 files)
      … 1 files under this directory
    install_windows_dep/  (1 files)
      … 1 files under this directory
    run_unittests/  (1 files)
      … 1 files under this directory
    run_unittests_win/  (1 files)
      … 1 files under this directory
    uninstall_tests/  (1 files)
      … 1 files under this directory
  workflows/  (5 files)
    check-template.yml
    levenshtein.js
    needs-reply.yml
    remove-needs-reply.yml
    workflow.yml
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  Detectron2-Logo-Horz.svg
  ISSUE_TEMPLATE.md
  import-tests.sh
  pull_request_template.md
configs/  (133 files)
  COCO-Detection/  (18 files)
    fast_rcnn_R_50_FPN_1x.yaml
    faster_rcnn_R_101_C4_3x.yaml
    faster_rcnn_R_101_DC5_3x.yaml
    faster_rcnn_R_101_FPN_3x.yaml
    faster_rcnn_R_50_C4_1x.yaml
    faster_rcnn_R_50_C4_3x.yaml
    faster_rcnn_R_50_DC5_1x.yaml
    faster_rcnn_R_50_DC5_3x.yaml
    faster_rcnn_R_50_FPN_1x.yaml
    faster_rcnn_R_50_FPN_3x.yaml
    faster_rcnn_X_101_32x8d_FPN_3x.yaml
    fcos_R_50_FPN_1x.py
    retinanet_R_101_FPN_3x.yaml
    retinanet_R_50_FPN_1x.py
    retinanet_R_50_FPN_1x.yaml
    retinanet_R_50_FPN_3x.yaml
    rpn_R_50_C4_1x.yaml
    rpn_R_50_FPN_1x.yaml
  COCO-InstanceSegmentation/  (15 files)
    mask_rcnn_R_101_C4_3x.yaml
    mask_rcnn_R_101_DC5_3x.yaml
    mask_rcnn_R_101_FPN_3x.yaml
    mask_rcnn_R_50_C4_1x.py
    mask_rcnn_R_50_C4_1x.yaml
    mask_rcnn_R_50_C4_3x.yaml
    mask_rcnn_R_50_DC5_1x.yaml
    mask_rcnn_R_50_DC5_3x.yaml
    mask_rcnn_R_50_FPN_1x.py
    mask_rcnn_R_50_FPN_1x.yaml
    mask_rcnn_R_50_FPN_1x_giou.yaml
    mask_rcnn_R_50_FPN_3x.yaml
    mask_rcnn_X_101_32x8d_FPN_3x.yaml
    mask_rcnn_regnetx_4gf_dds_fpn_1x.py
    mask_rcnn_regnety_4gf_dds_fpn_1x.py
  COCO-Keypoints/  (6 files)
    Base-Keypoint-RCNN-FPN.yaml
    keypoint_rcnn_R_101_FPN_3x.yaml
    keypoint_rcnn_R_50_FPN_1x.py
    keypoint_rcnn_R_50_FPN_1x.yaml
    keypoint_rcnn_R_50_FPN_3x.yaml
    keypoint_rcnn_X_101_32x8d_FPN_3x.yaml
  COCO-PanopticSegmentation/  (5 files)
    Base-Panoptic-FPN.yaml
    panoptic_fpn_R_101_3x.yaml
    panoptic_fpn_R_50_1x.py
    panoptic_fpn_R_50_1x.yaml
    panoptic_fpn_R_50_3x.yaml
  Cityscapes/  (1 files)
    mask_rcnn_R_50_FPN.yaml
  Detectron1-Comparisons/  (4 files)
    README.md
    faster_rcnn_R_50_FPN_noaug_1x.yaml
    keypoint_rcnn_R_50_FPN_1x.yaml
    mask_rcnn_R_50_FPN_noaug_1x.yaml
  LVISv0.5-InstanceSegmentation/  (3 files)
    mask_rcnn_R_101_FPN_1x.yaml
    mask_rcnn_R_50_FPN_1x.yaml
    mask_rcnn_X_101_32x8d_FPN_1x.yaml
  LVISv1-InstanceSegmentation/  (3 files)
    mask_rcnn_R_101_FPN_1x.yaml
    mask_rcnn_R_50_FPN_1x.yaml
    mask_rcnn_X_101_32x8d_FPN_1x.yaml
  Misc/  (15 files)
    cascade_mask_rcnn_R_50_FPN_1x.yaml
    cascade_mask_rcnn_R_50_FPN_3x.yaml
    cascade_mask_rcnn_X_152_32x8d_FPN_IN5k_gn_dconv.yaml
    mask_rcnn_R_50_FPN_1x_cls_agnostic.yaml
    mask_rcnn_R_50_FPN_1x_dconv_c3-c5.yaml
    mask_rcnn_R_50_FPN_3x_dconv_c3-c5.yaml
    mask_rcnn_R_50_FPN_3x_gn.yaml
    mask_rcnn_R_50_FPN_3x_syncbn.yaml
    mmdet_mask_rcnn_R_50_FPN_1x.py
    panoptic_fpn_R_101_dconv_cascade_gn_3x.yaml
    scratch_mask_rcnn_R_50_FPN_3x_gn.yaml
    scratch_mask_rcnn_R_50_FPN_9x_gn.yaml
    scratch_mask_rcnn_R_50_FPN_9x_syncbn.yaml
    semantic_R_50_FPN_1x.yaml
    torchvision_imagenet_R_50.py
  PascalVOC-Detection/  (2 files)
    faster_rcnn_R_50_C4.yaml
    faster_rcnn_R_50_FPN.yaml
  common/  (16 files)
    data/  (4 files)
      … 4 files under this directory
    models/  (8 files)
      … 8 files under this directory
    README.md
    coco_schedule.py
    optim.py
    train.py
  new_baselines/  (13 files)
    mask_rcnn_R_101_FPN_100ep_LSJ.py
    mask_rcnn_R_101_FPN_200ep_LSJ.py
    mask_rcnn_R_101_FPN_400ep_LSJ.py
    mask_rcnn_R_50_FPN_100ep_LSJ.py
    mask_rcnn_R_50_FPN_200ep_LSJ.py
    mask_rcnn_R_50_FPN_400ep_LSJ.py
    mask_rcnn_R_50_FPN_50ep_LSJ.py
    mask_rcnn_regnetx_4gf_dds_FPN_100ep_LSJ.py
    mask_rcnn_regnetx_4gf_dds_FPN_200ep_LSJ.py
    mask_rcnn_regnetx_4gf_dds_FPN_400ep_LSJ.py
    mask_rcnn_regnety_4gf_dds_FPN_100ep_LSJ.py
    mask_rcnn_regnety_4gf_dds_FPN_200ep_LSJ.py
    mask_rcnn_regnety_4gf_dds_FPN_400ep_LSJ.py
  quick_schedules/  (28 files)
    README.md
    cascade_mask_rcnn_R_50_FPN_inference_acc_test.yaml
    cascade_mask_rcnn_R_50_FPN_instant_test.yaml
    fast_rcnn_R_50_FPN_inference_acc_test.yaml
    fast_rcnn_R_50_FPN_instant_test.yaml
    keypoint_rcnn_R_50_FPN_inference_acc_test.yaml
    keypoint_rcnn_R_50_FPN_instant_test.yaml
    keypoint_rcnn_R_50_FPN_normalized_training_acc_test.yaml
    keypoint_rcnn_R_50_FPN_training_acc_test.yaml
    mask_rcnn_R_50_C4_GCV_instant_test.yaml
    mask_rcnn_R_50_C4_inference_acc_test.yaml
    mask_rcnn_R_50_C4_instant_test.yaml
    mask_rcnn_R_50_C4_training_acc_test.yaml
    mask_rcnn_R_50_DC5_inference_acc_test.yaml
    mask_rcnn_R_50_FPN_inference_acc_test.yaml
    mask_rcnn_R_50_FPN_instant_test.yaml
    mask_rcnn_R_50_FPN_pred_boxes_training_acc_test.yaml
    mask_rcnn_R_50_FPN_training_acc_test.yaml
    panoptic_fpn_R_50_inference_acc_test.yaml
    panoptic_fpn_R_50_instant_test.yaml
    panoptic_fpn_R_50_training_acc_test.yaml
    retinanet_R_50_FPN_inference_acc_test.yaml
    retinanet_R_50_FPN_instant_test.yaml
    rpn_R_50_FPN_inference_acc_test.yaml
    … 4 more files
  Base-RCNN-C4.yaml
  Base-RCNN-DilatedC5.yaml
  Base-RCNN-FPN.yaml
  Base-RetinaNet.yaml
datasets/  (5 files)
  README.md
  prepare_ade20k_sem_seg.py
  prepare_cocofied_lvis.py
  prepare_for_tests.sh
  prepare_panoptic_fpn.py
demo/  (3 files)
  README.md
  demo.py
  predictor.py
detectron2/  (176 files)
  checkpoint/  (4 files)
    __init__.py
    c2_model_loading.py
    catalog.py
    detection_checkpoint.py
  config/  (6 files)
    __init__.py
    compat.py
    config.py
    defaults.py
    instantiate.py
    lazy.py
  data/  (26 files)
    datasets/  (12 files)
      … 12 files under this directory
    samplers/  (3 files)
      … 3 files under this directory
    transforms/  (4 files)
      … 4 files under this directory
    __init__.py
    benchmark.py
    build.py
    catalog.py
    common.py
    dataset_mapper.py
    detection_utils.py
  engine/  (5 files)
    __init__.py
    defaults.py
    hooks.py
    launch.py
    train_loop.py
  evaluation/  (11 files)
    __init__.py
    cityscapes_evaluation.py
    coco_evaluation.py
    evaluator.py
    fast_eval_api.py
    lvis_evaluation.py
    panoptic_evaluation.py
    pascal_voc_evaluation.py
    rotated_coco_evaluation.py
    sem_seg_evaluation.py
    testing.py
  export/  (12 files)
    README.md
    __init__.py
    api.py
    c10.py
    caffe2_export.py
    caffe2_inference.py
    caffe2_modeling.py
    caffe2_patch.py
    flatten.py
    shared.py
    torchscript.py
    torchscript_patch.py
  layers/  (31 files)
    csrc/  (18 files)
      … 18 files under this directory
    __init__.py
    aspp.py
    batch_norm.py
    blocks.py
    deform_conv.py
    losses.py
    mask_ops.py
    nms.py
    roi_align.py
    roi_align_rotated.py
    rotated_boxes.py
    shape_spec.py
    wrappers.py
  model_zoo/  (2 files)
    __init__.py
    model_zoo.py
  modeling/  (40 files)
    backbone/  (10 files)
      … 10 files under this directory
    meta_arch/  (8 files)
      … 8 files under this directory
    proposal_generator/  (5 files)
      … 5 files under this directory
    roi_heads/  (8 files)
      … 8 files under this directory
    __init__.py
    anchor_generator.py
    box_regression.py
    matcher.py
    mmdet_wrapper.py
    poolers.py
    postprocessing.py
    sampling.py
    test_time_augmentation.py
  projects/  (2 files)
    README.md
    __init__.py
  solver/  (3 files)
    __init__.py
    build.py
    lr_scheduler.py
  structures/  (7 files)
    __init__.py
    boxes.py
    image_list.py
    instances.py
    keypoints.py
    masks.py
    rotated_boxes.py
  tracking/  (7 files)
    __init__.py
    base_tracker.py
    bbox_iou_tracker.py
    hungarian_tracker.py
    iou_weighted_hungarian_bbox_iou_tracker.py
    utils.py
    vanilla_hungarian_bbox_iou_tracker.py
  utils/  (19 files)
    README.md
    __init__.py
    analysis.py
    collect_env.py
    colormap.py
    comm.py
    develop.py
    env.py
    events.py
    file_io.py
    logger.py
    memory.py
    registry.py
    serialize.py
    testing.py
    torch_version_utils.py
    tracing.py
    video_visualizer.py
    visualizer.py
  __init__.py
dev/  (11 files)
  packaging/  (6 files)
    README.md
    build_all_wheels.sh
    build_wheel.sh
    gen_install_table.py
    gen_wheel_index.sh
    pkg_helpers.bash
  README.md
  linter.sh
  parse_results.sh
  run_inference_tests.sh
  run_instant_tests.sh
docker/  (4 files)
  Dockerfile
  README.md
  deploy.Dockerfile
  docker-compose.yml
docs/  (39 files)
  _static/  (1 files)
    css/  (1 files)
      … 1 files under this directory
  modules/  (15 files)
    checkpoint.rst
    config.rst
    data.rst
    data_transforms.rst
    engine.rst
    evaluation.rst
    export.rst
    fvcore.rst
    index.rst
    layers.rst
    model_zoo.rst
    modeling.rst
    solver.rst
    structures.rst
    utils.rst
  notes/  (4 files)
    benchmarks.md
    changelog.md
    compatibility.md
    index.rst
  tutorials/  (13 files)
    README.md
    augmentation.md
    configs.md
    data_loading.md
    datasets.md
    deployment.md
    evaluation.md
    extend.md
    index.rst
    lazyconfigs.md
    models.md
    training.md
    write-models.md
  .gitignore
  Makefile
  README.md
  conf.py
  index.rst
  requirements.txt
projects/  (335 files)
  DeepLab/  (12 files)
    configs/  (3 files)
      … 3 files under this directory
    deeplab/  (7 files)
      … 7 files under this directory
    README.md
    train_net.py
  DensePose/  (206 files)
    configs/  (61 files)
      … 61 files under this directory
    densepose/  (114 files)
      … 114 files under this directory
    dev/  (3 files)
      … 3 files under this directory
    doc/  (10 files)
      … 10 files under this directory
    tests/  (13 files)
      … 13 files under this directory
    README.md
    apply_net.py
    query_db.py
    setup.py
    train_net.py
  MViTv2/  (10 files)
    configs/  (9 files)
      … 9 files under this directory
    README.md
  Panoptic-DeepLab/  (12 files)
    configs/  (4 files)
      … 4 files under this directory
    panoptic_deeplab/  (6 files)
      … 6 files under this directory
    README.md
    train_net.py
  PointRend/  (21 files)
    configs/  (11 files)
      … 11 files under this directory
    point_rend/  (8 files)
      … 8 files under this directory
    README.md
    train_net.py
  PointSup/  (13 files)
    configs/  (3 files)
      … 3 files under this directory
    point_sup/  (7 files)
      … 7 files under this directory
    tools/  (1 files)
      … 1 files under this directory
    README.md
    train_net.py
  Rethinking-BatchNorm/  (8 files)
    configs/  (6 files)
      … 6 files under this directory
    README.md
    retinanet-eval-domain-specific.py
  TensorMask/  (16 files)
    configs/  (3 files)
      … 3 files under this directory
    tensormask/  (8 files)
      … 8 files under this directory
    tests/  (2 files)
      … 2 files under this directory
    README.md
    setup.py
    train_net.py
  TridentNet/  (12 files)
    configs/  (4 files)
      … 4 files under this directory
    tridentnet/  (6 files)
      … 6 files under this directory
    README.md
    train_net.py
  ViTDet/  (24 files)
    configs/  (23 files)
      … 23 files under this directory
    README.md
  README.md
tests/  (60 files)
  config/  (9 files)
    dir1/  (5 files)
      … 5 files under this directory
    root_cfg.py
    test_instantiate_config.py
    test_lazy_config.py
    test_yacs_config.py
  data/  (8 files)
    __init__.py
    test_coco.py
    test_coco_evaluation.py
    test_dataset.py
    test_detection_utils.py
    test_rotation_transform.py
    test_sampler.py
    test_transforms.py
  export/  (1 files)
    test_c10.py
  layers/  (9 files)
    __init__.py
    test_blocks.py
    test_deformable.py
    test_losses.py
    test_mask_ops.py
    test_nms.py
    test_nms_rotated.py
    test_roi_align.py
    test_roi_align_rotated.py
  modeling/  (11 files)
    __init__.py
    test_anchor_generator.py
    test_backbone.py
    test_box2box_transform.py
    test_fast_rcnn.py
    test_matcher.py
    test_mmdet.py
    test_model_e2e.py
    test_roi_heads.py
    test_roi_pooler.py
    test_rpn.py
  structures/  (7 files)
    __init__.py
    test_boxes.py
    test_imagelist.py
    test_instances.py
    test_keypoints.py
    test_masks.py
    test_rotated_boxes.py
  README.md
  __init__.py
  test_checkpoint.py
  test_engine.py
  test_events.py
  test_export_caffe2.py
  test_export_onnx.py
  test_export_torchscript.py
  test_model_analysis.py
  test_model_zoo.py
  test_packaging.py
  test_registry.py
  test_scheduler.py
  test_solver.py
  test_visualizer.py
.clang-format
.flake8
.gitignore
GETTING_STARTED.md
INSTALL.md
LICENSE
MODEL_ZOO.md
README.md
setup.cfg
setup.py
```

## Entry points

- [datasets/prepare_ade20k_sem_seg.py:18](https://github.com/facebookresearch/detectron2/blob/247691a1c292654867deb35cabb27f18d75a1363/datasets/prepare_ade20k_sem_seg.py#L18)
- [datasets/prepare_cocofied_lvis.py:169](https://github.com/facebookresearch/detectron2/blob/247691a1c292654867deb35cabb27f18d75a1363/datasets/prepare_cocofied_lvis.py#L169)
- [datasets/prepare_panoptic_fpn.py:80](https://github.com/facebookresearch/detectron2/blob/247691a1c292654867deb35cabb27f18d75a1363/datasets/prepare_panoptic_fpn.py#L80)
- [demo/demo.py:193](https://github.com/facebookresearch/detectron2/blob/247691a1c292654867deb35cabb27f18d75a1363/demo/demo.py#L193)
- [detectron2/data/datasets/cityscapes.py:336](https://github.com/facebookresearch/detectron2/blob/247691a1c292654867deb35cabb27f18d75a1363/detectron2/data/datasets/cityscapes.py#L336)
- [detectron2/data/datasets/coco.py:555](https://github.com/facebookresearch/detectron2/blob/247691a1c292654867deb35cabb27f18d75a1363/detectron2/data/datasets/coco.py#L555)
- [detectron2/data/datasets/coco_panoptic.py:193](https://github.com/facebookresearch/detectron2/blob/247691a1c292654867deb35cabb27f18d75a1363/detectron2/data/datasets/coco_panoptic.py#L193)
- [detectron2/data/datasets/lvis.py:249](https://github.com/facebookresearch/detectron2/blob/247691a1c292654867deb35cabb27f18d75a1363/detectron2/data/datasets/lvis.py#L249)
- [detectron2/evaluation/panoptic_evaluation.py:180](https://github.com/facebookresearch/detectron2/blob/247691a1c292654867deb35cabb27f18d75a1363/detectron2/evaluation/panoptic_evaluation.py#L180)
- [detectron2/utils/collect_env.py:262](https://github.com/facebookresearch/detectron2/blob/247691a1c292654867deb35cabb27f18d75a1363/detectron2/utils/collect_env.py#L262)
- [detectron2/utils/colormap.py:145](https://github.com/facebookresearch/detectron2/blob/247691a1c292654867deb35cabb27f18d75a1363/detectron2/utils/colormap.py#L145)
- [dev/packaging/gen_install_table.py:32](https://github.com/facebookresearch/detectron2/blob/247691a1c292654867deb35cabb27f18d75a1363/dev/packaging/gen_install_table.py#L32)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 264 file(s) under configuration and deployment (observed from repository paths and static analysis). Observed top-level classes: BatchNormBatchStat, CfgNode, ClassificationAcc, ClassificationNet, ConverterV1, Con… |
| Data layer | data | Observed | Groups 63 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AspectRatioGroupedDataset, AugInput, Augmentation, AugmentationList, CocoDatasetInfo, ColorTransform.… |
| datasets package | library | Observed | Groups 1 file(s) under datasets package (observed from repository paths and static analysis). |
| demo package | library | Observed | Groups 1 file(s) under demo package (observed from repository paths and static analysis). Observed top-level classes: AsyncPredictor, VisualizationDemo. |
| detectron2 package | library | Observed | Groups 129 file(s) under detectron2 package (observed from repository paths and static analysis). Observed top-level classes: AMPTrainer, ASPP, AnyNet, AnyStage, Attention, AutogradProfiler. Observed top-level functions… |
| dev package | library | Observed | Groups 7 file(s) under dev package (observed from repository paths and static analysis). |
| Application entry point | entrypoint | Observed | Groups 23 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Action, COCOPanopticEvaluator, DumpAction, EntrywiseAction, InferenceAction, PrintAction.… |
| External integrations | external | Observed | Groups 1 file(s) under external integrations (observed from repository paths and static analysis). Observed top-level classes: COCOeval_opt. |
| projects package | library | Observed | Groups 119 file(s) under projects package (observed from repository paths and static analysis). Observed top-level classes: ASPP, ASPPConv, ASPPPooling, AllEntrySelector, AnnotationsAccumulator, BaseConverter. Observed… |
| Tests | test | Observed | Groups 77 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: A, DatasetMapperTTA, DeformableTest, DensePoseDatasetMapperTTA, DensePoseGeneralizedRCNNWithTTA, DensePoseR… |

## Important files

- `.github/ISSUE_TEMPLATE/config.yml` (config)
- `.github/actions/install_detectron2/action.yml` (config)
- `.github/actions/install_detectron2_win/action.yml` (config)
- `.github/actions/install_linux_dep/action.yml` (config)
- `.github/actions/install_linux_gpu_dep/action.yml` (config)
- `.github/actions/install_windows_dep/action.yml` (config)
- `.github/actions/run_unittests/action.yml` (config)
- `.github/actions/run_unittests_win/action.yml` (config)
- `.github/actions/uninstall_tests/action.yml` (config)
- `.github/workflows/check-template.yml` (ci)
- `.github/workflows/levenshtein.js` (ci)
- `.github/workflows/needs-reply.yml` (ci)
- `.github/workflows/remove-needs-reply.yml` (ci)
- `.github/workflows/workflow.yml` (ci)
- `configs/Base-RCNN-C4.yaml` (config)
- `configs/Base-RCNN-DilatedC5.yaml` (config)
- `configs/Base-RCNN-FPN.yaml` (config)
- `configs/Base-RetinaNet.yaml` (config)
- `configs/COCO-Detection/fast_rcnn_R_50_FPN_1x.yaml` (config)
- `configs/COCO-Detection/faster_rcnn_R_101_C4_3x.yaml` (config)
- `configs/COCO-Detection/faster_rcnn_R_101_DC5_3x.yaml` (config)
- `configs/COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml` (config)
- `configs/COCO-Detection/faster_rcnn_R_50_C4_1x.yaml` (config)
- `configs/COCO-Detection/faster_rcnn_R_50_C4_3x.yaml` (config)
- `configs/COCO-Detection/faster_rcnn_R_50_DC5_1x.yaml` (config)
- `configs/COCO-Detection/faster_rcnn_R_50_DC5_3x.yaml` (config)
- `configs/COCO-Detection/faster_rcnn_R_50_FPN_1x.yaml` (config)
- `configs/COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml` (config)
- `configs/COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x.yaml` (config)
- `configs/COCO-Detection/retinanet_R_101_FPN_3x.yaml` (config)
- `configs/COCO-Detection/retinanet_R_50_FPN_1x.yaml` (config)
- `configs/COCO-Detection/retinanet_R_50_FPN_3x.yaml` (config)
- `configs/COCO-Detection/rpn_R_50_C4_1x.yaml` (config)
- `configs/COCO-Detection/rpn_R_50_FPN_1x.yaml` (config)
- `configs/COCO-InstanceSegmentation/mask_rcnn_R_101_C4_3x.yaml` (config)
- `configs/COCO-InstanceSegmentation/mask_rcnn_R_101_DC5_3x.yaml` (config)
- `configs/COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x.yaml` (config)
- `configs/COCO-InstanceSegmentation/mask_rcnn_R_50_C4_1x.yaml` (config)
- `configs/COCO-InstanceSegmentation/mask_rcnn_R_50_C4_3x.yaml` (config)
- `configs/COCO-InstanceSegmentation/mask_rcnn_R_50_DC5_1x.yaml` (config)
- `configs/COCO-InstanceSegmentation/mask_rcnn_R_50_DC5_3x.yaml` (config)
- `configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.yaml` (config)
- `configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x_giou.yaml` (config)
- `configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml` (config)
- `configs/COCO-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_3x.yaml` (config)
- `configs/COCO-Keypoints/Base-Keypoint-RCNN-FPN.yaml` (config)
- `configs/COCO-Keypoints/keypoint_rcnn_R_101_FPN_3x.yaml` (config)
- `configs/COCO-Keypoints/keypoint_rcnn_R_50_FPN_1x.yaml` (config)
- `configs/COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml` (config)
- `configs/COCO-Keypoints/keypoint_rcnn_X_101_32x8d_FPN_3x.yaml` (config)
- `configs/COCO-PanopticSegmentation/Base-Panoptic-FPN.yaml` (config)
- `configs/COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml` (config)
- `configs/COCO-PanopticSegmentation/panoptic_fpn_R_50_1x.yaml` (config)
- `configs/COCO-PanopticSegmentation/panoptic_fpn_R_50_3x.yaml` (config)
- `configs/Cityscapes/mask_rcnn_R_50_FPN.yaml` (config)
- `configs/Detectron1-Comparisons/faster_rcnn_R_50_FPN_noaug_1x.yaml` (config)
- `configs/Detectron1-Comparisons/keypoint_rcnn_R_50_FPN_1x.yaml` (config)
- `configs/Detectron1-Comparisons/mask_rcnn_R_50_FPN_noaug_1x.yaml` (config)
- `configs/LVISv0.5-InstanceSegmentation/mask_rcnn_R_101_FPN_1x.yaml` (config)
- `configs/LVISv0.5-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.yaml` (config)
- `configs/LVISv0.5-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_1x.yaml` (config)
- `configs/LVISv1-InstanceSegmentation/mask_rcnn_R_101_FPN_1x.yaml` (config)
- `configs/LVISv1-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.yaml` (config)
- `configs/LVISv1-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_1x.yaml` (config)
- `configs/Misc/cascade_mask_rcnn_R_50_FPN_1x.yaml` (config)
- `configs/Misc/cascade_mask_rcnn_R_50_FPN_3x.yaml` (config)
- `configs/Misc/cascade_mask_rcnn_X_152_32x8d_FPN_IN5k_gn_dconv.yaml` (config)
- `configs/Misc/mask_rcnn_R_50_FPN_1x_cls_agnostic.yaml` (config)
- `configs/Misc/mask_rcnn_R_50_FPN_1x_dconv_c3-c5.yaml` (config)
- `configs/Misc/mask_rcnn_R_50_FPN_3x_dconv_c3-c5.yaml` (config)
- `configs/Misc/mask_rcnn_R_50_FPN_3x_gn.yaml` (config)
- `configs/Misc/mask_rcnn_R_50_FPN_3x_syncbn.yaml` (config)
- `configs/Misc/panoptic_fpn_R_101_dconv_cascade_gn_3x.yaml` (config)
- `configs/Misc/scratch_mask_rcnn_R_50_FPN_3x_gn.yaml` (config)
- `configs/Misc/scratch_mask_rcnn_R_50_FPN_9x_gn.yaml` (config)
- `configs/Misc/scratch_mask_rcnn_R_50_FPN_9x_syncbn.yaml` (config)
- `configs/Misc/semantic_R_50_FPN_1x.yaml` (config)
- `configs/PascalVOC-Detection/faster_rcnn_R_50_C4.yaml` (config)
- `configs/PascalVOC-Detection/faster_rcnn_R_50_FPN.yaml` (config)
- `configs/quick_schedules/cascade_mask_rcnn_R_50_FPN_inference_acc_test.yaml` (config)
- `configs/quick_schedules/cascade_mask_rcnn_R_50_FPN_instant_test.yaml` (config)
- `configs/quick_schedules/fast_rcnn_R_50_FPN_inference_acc_test.yaml` (config)
- `configs/quick_schedules/fast_rcnn_R_50_FPN_instant_test.yaml` (config)
- `configs/quick_schedules/keypoint_rcnn_R_50_FPN_inference_acc_test.yaml` (config)
- `configs/quick_schedules/keypoint_rcnn_R_50_FPN_instant_test.yaml` (config)
- `configs/quick_schedules/keypoint_rcnn_R_50_FPN_normalized_training_acc_test.yaml` (config)
- `configs/quick_schedules/keypoint_rcnn_R_50_FPN_training_acc_test.yaml` (config)
- `configs/quick_schedules/mask_rcnn_R_50_C4_GCV_instant_test.yaml` (config)
- `configs/quick_schedules/mask_rcnn_R_50_C4_inference_acc_test.yaml` (config)
- `configs/quick_schedules/mask_rcnn_R_50_C4_instant_test.yaml` (config)
- `configs/quick_schedules/mask_rcnn_R_50_C4_training_acc_test.yaml` (config)
- `configs/quick_schedules/mask_rcnn_R_50_DC5_inference_acc_test.yaml` (config)
- `configs/quick_schedules/mask_rcnn_R_50_FPN_inference_acc_test.yaml` (config)
- `configs/quick_schedules/mask_rcnn_R_50_FPN_instant_test.yaml` (config)
- `configs/quick_schedules/mask_rcnn_R_50_FPN_pred_boxes_training_acc_test.yaml` (config)
- `configs/quick_schedules/mask_rcnn_R_50_FPN_training_acc_test.yaml` (config)
- `configs/quick_schedules/panoptic_fpn_R_50_inference_acc_test.yaml` (config)
- `configs/quick_schedules/panoptic_fpn_R_50_instant_test.yaml` (config)
- `configs/quick_schedules/panoptic_fpn_R_50_training_acc_test.yaml` (config)
- `configs/quick_schedules/retinanet_R_50_FPN_inference_acc_test.yaml` (config)
- `configs/quick_schedules/retinanet_R_50_FPN_instant_test.yaml` (config)
- `configs/quick_schedules/rpn_R_50_FPN_inference_acc_test.yaml` (config)
- `configs/quick_schedules/rpn_R_50_FPN_instant_test.yaml` (config)
- `configs/quick_schedules/semantic_R_50_FPN_inference_acc_test.yaml` (config)
- `configs/quick_schedules/semantic_R_50_FPN_instant_test.yaml` (config)
- `configs/quick_schedules/semantic_R_50_FPN_training_acc_test.yaml` (config)
- `docker/Dockerfile` (container)
- `docker/docker-compose.yml` (container)
- `docs/requirements.txt` (manifest)
- `projects/DeepLab/configs/Cityscapes-SemanticSegmentation/Base-DeepLabV3-OS16-Semantic.yaml` (config)
- `projects/DeepLab/configs/Cityscapes-SemanticSegmentation/deeplab_v3_R_103_os16_mg124_poly_90k_bs16.yaml` (config)
- `projects/DeepLab/configs/Cityscapes-SemanticSegmentation/deeplab_v3_plus_R_103_os16_mg124_poly_90k_bs16.yaml` (config)
- `projects/DensePose/configs/Base-DensePose-RCNN-FPN.yaml` (config)
- `projects/DensePose/configs/HRNet/densepose_rcnn_HRFPN_HRNet_w32_s1x.yaml` (config)
- `projects/DensePose/configs/HRNet/densepose_rcnn_HRFPN_HRNet_w40_s1x.yaml` (config)
- `projects/DensePose/configs/HRNet/densepose_rcnn_HRFPN_HRNet_w48_s1x.yaml` (config)
- `projects/DensePose/configs/cse/Base-DensePose-RCNN-FPN-Human.yaml` (config)
- `projects/DensePose/configs/cse/Base-DensePose-RCNN-FPN.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_101_FPN_DL_s1x.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_101_FPN_DL_soft_s1x.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_101_FPN_s1x.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_101_FPN_soft_s1x.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_50_FPN_DL_s1x.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_50_FPN_DL_soft_s1x.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_50_FPN_s1x.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_50_FPN_soft_animals_CA_finetune_16k.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_50_FPN_soft_animals_CA_finetune_4k.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_50_FPN_soft_animals_I0_finetune_16k.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_50_FPN_soft_animals_I0_finetune_i2m_16k.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_50_FPN_soft_animals_I0_finetune_m2m_16k.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_50_FPN_soft_animals_finetune_16k.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_50_FPN_soft_animals_finetune_4k.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_50_FPN_soft_animals_finetune_maskonly_24k.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_50_FPN_soft_chimps_finetune_4k.yaml` (config)
- `projects/DensePose/configs/cse/densepose_rcnn_R_50_FPN_soft_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_101_FPN_DL_WC1M_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_101_FPN_DL_WC1_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_101_FPN_DL_WC2M_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_101_FPN_DL_WC2_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_101_FPN_DL_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_101_FPN_WC1M_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_101_FPN_WC1_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_101_FPN_WC2M_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_101_FPN_WC2_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_101_FPN_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_101_FPN_s1x_legacy.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_50_FPN_DL_WC1M_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_50_FPN_DL_WC1_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_50_FPN_DL_WC2M_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_50_FPN_DL_WC2_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_50_FPN_DL_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_50_FPN_WC1M_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_50_FPN_WC1_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_50_FPN_WC2M_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_50_FPN_WC2_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_50_FPN_s1x.yaml` (config)
- `projects/DensePose/configs/densepose_rcnn_R_50_FPN_s1x_legacy.yaml` (config)
- `projects/DensePose/configs/evolution/Base-RCNN-FPN-Atop10P_CA.yaml` (config)
- `projects/DensePose/configs/evolution/densepose_R_50_FPN_DL_WC1M_3x_Atop10P_CA.yaml` (config)
- `projects/DensePose/configs/evolution/densepose_R_50_FPN_DL_WC1M_3x_Atop10P_CA_B_coarsesegm.yaml` (config)
- `projects/DensePose/configs/evolution/densepose_R_50_FPN_DL_WC1M_3x_Atop10P_CA_B_finesegm.yaml` (config)
- `projects/DensePose/configs/evolution/densepose_R_50_FPN_DL_WC1M_3x_Atop10P_CA_B_uniform.yaml` (config)
- `projects/DensePose/configs/evolution/densepose_R_50_FPN_DL_WC1M_3x_Atop10P_CA_B_uv.yaml` (config)
- `projects/DensePose/configs/quick_schedules/cse/densepose_rcnn_R_50_FPN_DL_instant_test.yaml` (config)
- `projects/DensePose/configs/quick_schedules/cse/densepose_rcnn_R_50_FPN_soft_animals_finetune_instant_test.yaml` (config)
- `projects/DensePose/configs/quick_schedules/densepose_rcnn_HRFPN_HRNet_w32_instant_test.yaml` (config)
- `projects/DensePose/configs/quick_schedules/densepose_rcnn_R_50_FPN_DL_instant_test.yaml` (config)
- `projects/DensePose/configs/quick_schedules/densepose_rcnn_R_50_FPN_TTA_inference_acc_test.yaml` (config)
- `projects/DensePose/configs/quick_schedules/densepose_rcnn_R_50_FPN_WC1_instant_test.yaml` (config)
- `projects/DensePose/configs/quick_schedules/densepose_rcnn_R_50_FPN_WC2_instant_test.yaml` (config)
- `projects/DensePose/configs/quick_schedules/densepose_rcnn_R_50_FPN_inference_acc_test.yaml` (config)
- `projects/DensePose/configs/quick_schedules/densepose_rcnn_R_50_FPN_instant_test.yaml` (config)
- `projects/DensePose/configs/quick_schedules/densepose_rcnn_R_50_FPN_training_acc_test.yaml` (config)
- `projects/DensePose/setup.py` (manifest)
- `projects/Panoptic-DeepLab/configs/COCO-PanopticSegmentation/panoptic_deeplab_R_52_os16_mg124_poly_200k_bs64_crop_640_640_coco_dsconv.yaml` (config)
- `projects/Panoptic-DeepLab/configs/Cityscapes-PanopticSegmentation/Base-PanopticDeepLab-OS16.yaml` (config)
- `projects/Panoptic-DeepLab/configs/Cityscapes-PanopticSegmentation/panoptic_deeplab_R_52_os16_mg124_poly_90k_bs32_crop_512_1024.yaml` (config)
- `projects/Panoptic-DeepLab/configs/Cityscapes-PanopticSegmentation/panoptic_deeplab_R_52_os16_mg124_poly_90k_bs32_crop_512_1024_dsconv.yaml` (config)
- `projects/PointRend/configs/InstanceSegmentation/Base-Implicit-PointRend.yaml` (config)
- `projects/PointRend/configs/InstanceSegmentation/Base-PointRend-RCNN-FPN.yaml` (config)
- `projects/PointRend/configs/InstanceSegmentation/implicit_pointrend_R_50_FPN_1x_coco.yaml` (config)
- `projects/PointRend/configs/InstanceSegmentation/implicit_pointrend_R_50_FPN_3x_coco.yaml` (config)
- `projects/PointRend/configs/InstanceSegmentation/pointrend_rcnn_R_101_FPN_3x_coco.yaml` (config)
- `projects/PointRend/configs/InstanceSegmentation/pointrend_rcnn_R_50_FPN_1x_cityscapes.yaml` (config)
- `projects/PointRend/configs/InstanceSegmentation/pointrend_rcnn_R_50_FPN_1x_coco.yaml` (config)
- `projects/PointRend/configs/InstanceSegmentation/pointrend_rcnn_R_50_FPN_3x_coco.yaml` (config)
- `projects/PointRend/configs/InstanceSegmentation/pointrend_rcnn_X_101_32x8d_FPN_3x_coco.yaml` (config)
- `projects/PointRend/configs/SemanticSegmentation/Base-PointRend-Semantic-FPN.yaml` (config)
- `projects/PointRend/configs/SemanticSegmentation/pointrend_semantic_R_101_FPN_1x_cityscapes.yaml` (config)
- `projects/PointSup/configs/implicit_pointrend_R_50_FPN_3x_point_sup_point_aug_coco.yaml` (config)
- `projects/PointSup/configs/mask_rcnn_R_50_FPN_3x_point_sup_coco.yaml` (config)
- `projects/PointSup/configs/mask_rcnn_R_50_FPN_3x_point_sup_point_aug_coco.yaml` (config)
- `projects/TensorMask/configs/Base-TensorMask.yaml` (config)
- `projects/TensorMask/configs/tensormask_R_50_FPN_1x.yaml` (config)
- `projects/TensorMask/configs/tensormask_R_50_FPN_6x.yaml` (config)
- `projects/TensorMask/setup.py` (manifest)
- `projects/TridentNet/configs/Base-TridentNet-Fast-C4.yaml` (config)
- `projects/TridentNet/configs/tridentnet_fast_R_101_C4_3x.yaml` (config)
- `projects/TridentNet/configs/tridentnet_fast_R_50_C4_1x.yaml` (config)
- `projects/TridentNet/configs/tridentnet_fast_R_50_C4_3x.yaml` (config)
- `setup.cfg` (manifest)
- `setup.py` (manifest)

## Top-level layout

- `projects` — 335 analysed file(s)
- `detectron2` — 176 analysed file(s)
- `configs` — 133 analysed file(s)
- `tests` — 60 analysed file(s)
- `docs` — 39 analysed file(s)
- `.github` — 24 analysed file(s)
- `dev` — 11 analysed file(s)
- `(root files)` — 10 analysed file(s)
- `datasets` — 5 analysed file(s)
- `docker` — 4 analysed file(s)
- `demo` — 3 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `247691a1c292654867deb35cabb27f18d75a1363` is the revision these paths and observations refer to.
