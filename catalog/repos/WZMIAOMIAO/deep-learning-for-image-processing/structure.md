# Project structure: WZMIAOMIAO/deep-learning-for-image-processing

**Analysed commit:** `1ec3fe6f374fc9969973a61f819de25658595afa`

**Commit reference:** [1ec3fe6f374fc9969973a61f819de25658595afa](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/commit/1ec3fe6f374fc9969973a61f819de25658595afa)

**Tree at this commit:** [WZMIAOMIAO/deep-learning-for-image-processing@1ec3fe6f374f](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/tree/1ec3fe6f374fc9969973a61f819de25658595afa)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | WZMIAOMIAO/deep-learning-for-image-processing |
| Description | deep learning for image processing including classification and object-detection etc. |
| Stars | 26451 |
| Forks | 8151 |
| Licence | GPL-3.0 |
| Language | Python |
| Default branch | master |
| Analysed commit | `1ec3fe6f374fc9969973a61f819de25658595afa` |
| Retrieved at | 2026-11-14T19:07:26.390674+00:00 |
| Files in this snapshot | 594 |

## Directory tree

```text
.github/  (1 files)
  ISSUE_TEMPLATE/  (1 files)
    issue-template.md
article_link/  (1 files)
  README.md
course_ppt/  (1 files)
  README.md
data_set/  (2 files)
  README.md
  split_data.py
deploying_service/  (35 files)
  deploying_pytorch/  (30 files)
    convert_onnx_cls/  (3 files)
      … 3 files under this directory
    convert_openvino/  (17 files)
      … 17 files under this directory
    convert_tensorrt/  (5 files)
      … 5 files under this directory
    pytorch_flask_service/  (5 files)
      … 5 files under this directory
  pruning_model_pytorch/  (5 files)
    class_indices.json
    main.py
    model.py
    predict.py
    train.py
others_project/  (23 files)
  draw_dilated_conv/  (1 files)
    main.py
  kmeans_anchors/  (4 files)
    main.py
    plot_kmeans.py
    read_voc.py
    yolo_kmeans.py
  openvinotest/  (6 files)
    openvino_cls_test/  (6 files)
      … 6 files under this directory
  readPbFile/  (6 files)
    export/  (1 files)
      … 1 files under this directory
    test_images/  (1 files)
      … 1 files under this directory
    README.md
    pascal_label_map.pbtxt
    readPb.py
    using_function.py
  textcnnKeras/  (4 files)
    dataGenerator.py
    data_link.txt
    main.py
    models.py
  trans_widerface_to_xml/  (2 files)
    create_xml.py
    main.py
pytorch_classification/  (142 files)
  ConfusionMatrix/  (3 files)
    class_indices.json
    main.py
    model.py
  ConvNeXt/  (6 files)
    README.md
    model.py
    my_dataset.py
    predict.py
    train.py
    utils.py
  MobileViT/  (9 files)
    README.md
    model.py
    model_config.py
    my_dataset.py
    predict.py
    train.py
    transformer.py
    unfold_test.py
    utils.py
  Test10_regnet/  (7 files)
    README.md
    model.py
    my_dataset.py
    predict.py
    pretrain_weights.py
    train.py
    utils.py
  Test11_efficientnetV2/  (8 files)
    README.md
    class_indices.json
    model.py
    my_dataset.py
    predict.py
    train.py
    trans_effv2_weights.py
    utils.py
  Test1_official_demo/  (3 files)
    model.py
    predict.py
    train.py
  Test2_alexnet/  (4 files)
    class_indices.json
    model.py
    predict.py
    train.py
  Test3_vggnet/  (4 files)
    class_indices.json
    model.py
    predict.py
    train.py
  Test4_googlenet/  (4 files)
    class_indices.json
    model.py
    predict.py
    train.py
  Test5_resnet/  (7 files)
    README.md
    batch_predict.py
    class_indices.json
    load_weights.py
    model.py
    predict.py
    train.py
  Test6_mobilenet/  (5 files)
    class_indices.json
    model_v2.py
    model_v3.py
    predict.py
    train.py
  Test7_shufflenet/  (7 files)
    README.md
    class_indices.json
    model.py
    my_dataset.py
    predict.py
    train.py
    utils.py
  Test8_densenet/  (6 files)
    README.md
    model.py
    my_dataset.py
    predict.py
    train.py
    utils.py
  Test9_efficientNet/  (8 files)
    README.md
    model.py
    my_dataset.py
    predict.py
    requirements.txt
    train.py
    trans_weights_to_pytorch.py
    utils.py
  analyze_weights_featuremap/  (4 files)
    alexnet_model.py
    analyze_feature_map.py
    analyze_kernel_weight.py
    resnet_model.py
  custom_dataset/  (3 files)
    main.py
    my_dataset.py
    utils.py
  grad_cam/  (8 files)
    README.md
    imagenet1k_classes.txt
    main_cnn.py
    main_swin.py
    main_vit.py
    swin_model.py
    utils.py
    vit_model.py
  mini_imagenet/  (10 files)
    multi_train_utils/  (3 files)
      … 3 files under this directory
    README.md
    imagenet_class_index.json
    model.py
    my_dataset.py
    restructure_csv.py
    train_multi_gpu_using_launch.py
    train_single_gpu.py
  model_complexity/  (3 files)
    main.py
    model.py
    utils.py
  swin_transformer/  (8 files)
    README.md
    create_confusion_matrix.py
    model.py
    my_dataset.py
    predict.py
    select_incorrect_samples.py
    train.py
    utils.py
  tensorboard_test/  (6 files)
    data_utils.py
    model.py
    my_dataset.py
    requirements.txt
    train.py
    train_eval_utils.py
  train_multi_GPU/  (11 files)
    multi_train_utils/  (2 files)
      … 2 files under this directory
    README.md
    model.py
    my_dataset.py
    plot_results.py
    requirements.txt
    train_multi_gpu_using_launch.py
    train_multi_gpu_using_spawn.py
    train_single_gpu.py
    utils.py
  vision_transformer/  (7 files)
    README.md
    flops.py
    my_dataset.py
    predict.py
    train.py
    utils.py
    vit_model.py
  README.md
pytorch_keypoint/  (35 files)
  DeepPose/  (15 files)
    train_utils/  (4 files)
      … 4 files under this directory
    README.md
    datasets.py
    export_onnx.py
    model.py
    predict.py
    requirements.txt
    train.py
    train_multi_GPU.py
    transforms.py
    utils.py
    wflw_horizontal_flip_indices.py
  HRNet/  (20 files)
    model/  (2 files)
      … 2 files under this directory
    train_utils/  (7 files)
      … 7 files under this directory
    README.md
    draw_utils.py
    my_dataset_coco.py
    person_keypoints.json
    plot_curve.py
    predict.py
    requirements.txt
    train.py
    train_multi_GPU.py
    transforms.py
    validation.py
pytorch_object_detection/  (181 files)
  faster_rcnn/  (35 files)
    backbone/  (5 files)
      … 5 files under this directory
    network_files/  (8 files)
      … 8 files under this directory
    train_utils/  (6 files)
      … 6 files under this directory
    README.md
    change_backbone_with_fpn.py
    change_backbone_without_fpn.py
    draw_box_utils.py
    my_dataset.py
    pascal_voc_classes.json
    plot_curve.py
    predict.py
    record_mAP.txt
    requirements.txt
    split_data.py
    train_mobilenetv2.py
    train_multi_GPU.py
    train_res50_fpn.py
    transforms.py
    validation.py
  mask_rcnn/  (33 files)
    backbone/  (3 files)
      … 3 files under this directory
    network_files/  (9 files)
      … 9 files under this directory
    train_utils/  (6 files)
      … 6 files under this directory
    README.md
    coco91_indices.json
    det_results20220406-141544.txt
    draw_box_utils.py
    my_dataset_coco.py
    my_dataset_voc.py
    pascal_voc_indices.json
    plot_curve.py
    predict.py
    requirements.txt
    seg_results20220406-141544.txt
    train.py
    train_multi_GPU.py
    transforms.py
    validation.py
  retinaNet/  (29 files)
    backbone/  (3 files)
      … 3 files under this directory
    network_files/  (8 files)
      … 8 files under this directory
    train_utils/  (6 files)
      … 6 files under this directory
    README.md
    draw_box_utils.py
    my_dataset.py
    pascal_voc_classes.json
    plot_curve.py
    predict.py
    requirements.txt
    results20210421-142632.txt
    train.py
    train_multi_GPU.py
    transforms.py
    validation.py
  ssd/  (22 files)
    src/  (4 files)
      … 4 files under this directory
    train_utils/  (6 files)
      … 6 files under this directory
    README.md
    draw_box_utils.py
    my_dataset.py
    pascal_voc_classes.json
    plot_curve.py
    predict_test.py
    record_mAP.txt
    requirements.txt
    train_multi_GPU.py
    train_ssd300.py
    transforms.py
    validation.py
  train_coco_dataset/  (33 files)
    backbone/  (6 files)
      … 6 files under this directory
    network_files/  (8 files)
      … 8 files under this directory
    train_utils/  (5 files)
      … 5 files under this directory
    README.md
    change_backbone_with_fpn.py
    coco91_indices.json
    compute_receptive_field.py
    draw_box_utils.py
    my_dataset.py
    plot_curve.py
    predict.py
    requirements.txt
    results20220408-201436.txt
    train.py
    train_multi_GPU.py
    transforms.py
    validation.py
  yolov3_spp/  (29 files)
    build_utils/  (7 files)
      … 7 files under this directory
    cfg/  (2 files)
      … 2 files under this directory
    data/  (1 files)
      … 1 files under this directory
    train_utils/  (6 files)
      … 6 files under this directory
    README.md
    calculate_dataset.py
    draw_box_utils.py
    export_onnx.py
    load_onnx_test.py
    models.py
    predict_test.py
    requirements.txt
    results20210515-152935.txt
    train.py
    train_multi_GPU.py
    trans_voc2yolo.py
    validation.py
pytorch_segmentation/  (87 files)
  deeplab_v3/  (19 files)
    src/  (4 files)
      … 4 files under this directory
    train_utils/  (3 files)
      … 3 files under this directory
    README.md
    get_palette.py
    my_dataset.py
    palette.json
    pascal_voc_classes.json
    predict.py
    requirements.txt
    results20211027-104607.txt
    train.py
    train_multi_GPU.py
    transforms.py
    validation.py
  fcn/  (18 files)
    src/  (3 files)
      … 3 files under this directory
    train_utils/  (3 files)
      … 3 files under this directory
    README.md
    get_palette.py
    my_dataset.py
    palette.json
    pascal_voc_classes.json
    predict.py
    requirements.txt
    results20210918-122740.txt
    train.py
    train_multi_GPU.py
    transforms.py
    validation.py
  lraspp/  (18 files)
    src/  (3 files)
      … 3 files under this directory
    train_utils/  (3 files)
      … 3 files under this directory
    README.md
    get_palette.py
    my_dataset.py
    palette.json
    pascal_voc_classes.json
    predict.py
    requirements.txt
    results20211028-105233.txt
    train.py
    train_multi_GPU.py
    transforms.py
    validation.py
  u2net/  (15 files)
    src/  (2 files)
      … 2 files under this directory
    train_utils/  (3 files)
      … 3 files under this directory
    README.md
    convert_weight.py
    my_dataset.py
    predict.py
    requirements.txt
    results20220723-123632.txt
    train.py
    train_multi_GPU.py
    transforms.py
    validation.py
  unet/  (17 files)
    src/  (4 files)
      … 4 files under this directory
    train_utils/  (4 files)
      … 4 files under this directory
    README.md
    compute_mean_std.py
    my_dataset.py
    predict.py
    requirements.txt
    results20220109-165837.txt
    train.py
    train_multi_GPU.py
    transforms.py
tensorflow_classification/  (82 files)
  ConfusionMatrix/  (3 files)
    class_indices.json
    main.py
    model.py
  ConvNeXt/  (5 files)
    model.py
    predict.py
    train.py
    trans_weights.py
    utils.py
  Test11_efficientnetV2/  (5 files)
    model.py
    predict.py
    train.py
    trans_weights.py
    utils.py
  Test1_official_demo/  (2 files)
    model.py
    train.py
  Test2_alexnet/  (7 files)
    class_indices.json
    fine_train_alexnet.py
    model.py
    predict.py
    read_pth.py
    train.py
    trainGPU.py
  Test3_vgg/  (7 files)
    class_indices.json
    fine_train_vgg16.py
    model.py
    predict.py
    read_ckpt.py
    train.py
    trainGPU.py
  Test4_goolenet/  (8 files)
    class_indices.json
    model.py
    model_add_bn.py
    predict.py
    read_pth.py
    train.py
    trainGPU.py
    train_add_bn.py
  Test5_resnet/  (9 files)
    batch_predict.py
    class_indices.json
    model.py
    predict.py
    read_ckpt.py
    read_h5.py
    subclassed_model.py
    train.py
    trainGPU.py
  Test6_mobilenet/  (9 files)
    model_v2.py
    model_v3.py
    predict.py
    read_ckpt.py
    trainGPU_mobilenet_v2.py
    train_mobilenet_v2.py
    train_mobilenet_v3.py
    trans_v3_weights.py
    utils.py
  Test7_shuffleNet/  (5 files)
    model.py
    predict.py
    train.py
    trans_weights.py
    utils.py
  Test9_efficientNet/  (4 files)
    model.py
    predict.py
    train.py
    utils.py
  analyze_weights_featuremap/  (3 files)
    alexnet_model.py
    analyze_feature_map.py
    analyze_kernel_weight.py
  custom_dataset/  (2 files)
    train_fit.py
    utils.py
  swin_transformer/  (5 files)
    model.py
    predict.py
    train.py
    trans_weights.py
    utils.py
  tensorboard_test/  (2 files)
    train_fit.py
    train_not_fit.py
  vision_transformer/  (5 files)
    predict.py
    train.py
    trans_weights.py
    utils.py
    vit_model.py
  README.md
.gitignore
LICENSE
README.md
summary_problem.md
```

## Entry points

- [pytorch_segmentation/u2net/src/model.py:225](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/u2net/src/model.py#L225)
- [data_set/split_data.py:66](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/data_set/split_data.py#L66)
- [deploying_service/deploying_pytorch/convert_onnx_cls/main.py:78](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_onnx_cls/main.py#L78)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_fps.py:125](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_fps.py#L125)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_onnx_and_ir.py:64](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_onnx_and_ir.py#L64)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/convert_pytorch2onnx.py:55](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/convert_pytorch2onnx.py#L55)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/quantization_int8.py:83](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/quantization_int8.py#L83)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_fps.py:120](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_fps.py#L120)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_onnx_and_ir.py:60](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_onnx_and_ir.py#L60)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/evaluation.py:43](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/evaluation.py#L43)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/predict.py:49](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/predict.py#L49)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/quantization_int8.py:101](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/quantization_int8.py#L101)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| Configuration and deployment | config | Observed | Groups 53 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 36 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AlexNet, AlexNet_v2, BasicBlock, BasicConv2d, BasicLayer, Block. Observed top-level functions: AlexNet… |
| deploying_service package | library | Observed | Groups 7 file(s) under deploying_service package (observed from repository paths and static analysis). Observed top-level classes: Accuracy, EvalCOCOMetric, MAPMetric, MyDataLoader, MyDataSet. Observed top-level functio… |
| Application entry point | entrypoint | Observed | Groups 186 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /predict, ROUTE /. Observed top-level classes:… |
| External integrations | external | Inferred | Groups 0 file(s) under external integrations (observed from repository paths and static analysis). |
| others_project package | library | Observed | Groups 7 file(s) under others_project package (observed from repository paths and static analysis). Observed top-level classes: VOCDataSet, XMLGenerator. Observed top-level functions: content2idList, convert_type, creat… |
| pytorch_classification package | library | Observed | Groups 45 file(s) under pytorch_classification package (observed from repository paths and static analysis). Observed top-level classes: ActivationsAndGradients, AlexNet, Attention, BasicBlock, BasicLayer, Block. Observ… |
| pytorch_keypoint package | library | Observed | Groups 18 file(s) under pytorch_keypoint package (observed from repository paths and static analysis). Observed top-level classes: AffineTransform, BasicBlock, Bottleneck, Compose, EvalCOCOMetric, GroupedBatchSampler. O… |
| pytorch_object_detection package | library | Observed | Groups 117 file(s) under pytorch_object_detection package (observed from repository paths and static analysis). Observed top-level classes: AnchorsGenerator, AssignGTtoDefaultBox, Backbone, BackboneWithFPN, BalancedPosi… |
| pytorch_segmentation package | library | Observed | Groups 43 file(s) under pytorch_segmentation package (observed from repository paths and static analysis). Observed top-level classes: ASPP, ASPPConv, ASPPPooling, Bottleneck, CenterCrop, Compose. Observed top-level fun… |
| tensorflow_classification package | library | Observed | Groups 20 file(s) under tensorflow_classification package (observed from repository paths and static analysis). Observed top-level classes: AlexNet_v2, Attention, BasicBlock, Block, Bottleneck, ConcatClassTokenAddPosEmb… |
| Tests | test | Observed | Groups 5 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: bboxes_iou, check_path_exist, clip_coords, create_model, main, my_self. |

## Important files

- `deploying_service/deploying_pytorch/convert_onnx_cls/class_indices.json` (config)
- `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/requirements.txt` (manifest)
- `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/requirements.txt` (manifest)
- `deploying_service/deploying_pytorch/pytorch_flask_service/class_indices.json` (config)
- `deploying_service/deploying_pytorch/pytorch_flask_service/requirements.txt` (manifest)
- `deploying_service/pruning_model_pytorch/class_indices.json` (config)
- `others_project/openvinotest/openvino_cls_test/class_indices.json` (config)
- `pytorch_classification/ConfusionMatrix/class_indices.json` (config)
- `pytorch_classification/Test11_efficientnetV2/class_indices.json` (config)
- `pytorch_classification/Test2_alexnet/class_indices.json` (config)
- `pytorch_classification/Test3_vggnet/class_indices.json` (config)
- `pytorch_classification/Test4_googlenet/class_indices.json` (config)
- `pytorch_classification/Test5_resnet/class_indices.json` (config)
- `pytorch_classification/Test6_mobilenet/class_indices.json` (config)
- `pytorch_classification/Test7_shufflenet/class_indices.json` (config)
- `pytorch_classification/Test9_efficientNet/requirements.txt` (manifest)
- `pytorch_classification/mini_imagenet/imagenet_class_index.json` (config)
- `pytorch_classification/tensorboard_test/requirements.txt` (manifest)
- `pytorch_classification/train_multi_GPU/requirements.txt` (manifest)
- `pytorch_keypoint/DeepPose/requirements.txt` (manifest)
- `pytorch_keypoint/HRNet/person_keypoints.json` (config)
- `pytorch_keypoint/HRNet/requirements.txt` (manifest)
- `pytorch_object_detection/faster_rcnn/pascal_voc_classes.json` (config)
- `pytorch_object_detection/faster_rcnn/requirements.txt` (manifest)
- `pytorch_object_detection/mask_rcnn/coco91_indices.json` (config)
- `pytorch_object_detection/mask_rcnn/pascal_voc_indices.json` (config)
- `pytorch_object_detection/mask_rcnn/requirements.txt` (manifest)
- `pytorch_object_detection/retinaNet/pascal_voc_classes.json` (config)
- `pytorch_object_detection/retinaNet/requirements.txt` (manifest)
- `pytorch_object_detection/ssd/pascal_voc_classes.json` (config)
- `pytorch_object_detection/ssd/requirements.txt` (manifest)
- `pytorch_object_detection/train_coco_dataset/coco91_indices.json` (config)
- `pytorch_object_detection/train_coco_dataset/requirements.txt` (manifest)
- `pytorch_object_detection/yolov3_spp/cfg/hyp.yaml` (config)
- `pytorch_object_detection/yolov3_spp/cfg/yolov3-spp.cfg` (config)
- `pytorch_object_detection/yolov3_spp/data/pascal_voc_classes.json` (config)
- `pytorch_object_detection/yolov3_spp/requirements.txt` (manifest)
- `pytorch_segmentation/deeplab_v3/palette.json` (config)
- `pytorch_segmentation/deeplab_v3/pascal_voc_classes.json` (config)
- `pytorch_segmentation/deeplab_v3/requirements.txt` (manifest)
- `pytorch_segmentation/fcn/palette.json` (config)
- `pytorch_segmentation/fcn/pascal_voc_classes.json` (config)
- `pytorch_segmentation/fcn/requirements.txt` (manifest)
- `pytorch_segmentation/lraspp/palette.json` (config)
- `pytorch_segmentation/lraspp/pascal_voc_classes.json` (config)
- `pytorch_segmentation/lraspp/requirements.txt` (manifest)
- `pytorch_segmentation/u2net/requirements.txt` (manifest)
- `pytorch_segmentation/unet/requirements.txt` (manifest)
- `tensorflow_classification/ConfusionMatrix/class_indices.json` (config)
- `tensorflow_classification/Test2_alexnet/class_indices.json` (config)
- `tensorflow_classification/Test3_vgg/class_indices.json` (config)
- `tensorflow_classification/Test4_goolenet/class_indices.json` (config)
- `tensorflow_classification/Test5_resnet/class_indices.json` (config)

## Top-level layout

- `pytorch_object_detection` — 181 analysed file(s)
- `pytorch_classification` — 142 analysed file(s)
- `pytorch_segmentation` — 87 analysed file(s)
- `tensorflow_classification` — 82 analysed file(s)
- `deploying_service` — 35 analysed file(s)
- `pytorch_keypoint` — 35 analysed file(s)
- `others_project` — 23 analysed file(s)
- `(root files)` — 4 analysed file(s)
- `data_set` — 2 analysed file(s)
- `.github` — 1 analysed file(s)
- `article_link` — 1 analysed file(s)
- `course_ppt` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `1ec3fe6f374fc9969973a61f819de25658595afa` is the revision these paths and observations refer to.
