# Architecture report: WZMIAOMIAO/deep-learning-for-image-processing

> Automated static analysis. **Observed** = directly seen in files/imports/AST; **Inferred** = interpretation from that evidence. Repository code was not executed.

## 1. Repository at a glance

| Item | Value |
| --- | --- |
| Repository | WZMIAOMIAO/deep-learning-for-image-processing |
| Description | deep learning for image processing including classification and object-detection etc. |
| Language | Python |
| Stars | 26451 |
| Licence | GPL-3.0 |
| Analysed commit / branch | 1ec3fe6f374fc9969973a61f819de25658595afa / master |
| Framework(s) | Flask |
| Files analysed | 594 |
| Components | 12 |

## 2. Architecture in one minute

WZMIAOMIAO/deep-learning-for-image-processing - deep learning for image processing including classification and object-detection etc.. This repository was analysed statically from 594 file(s) (484 Python). Detected technologies (observed from imports/manifests): Flask, NumPy, pandas, requests. Files are grouped into 12 component(s): Configuration and deployment, Data layer, deploying_service package, Application entry point, External integrations, others_project package, pytorch_classification package, pytorch_keypoint package. Observed entry point(s): data_set/split_data.py, deploying_service/deploying_pytorch/convert_onnx_cls/main.py, deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_fps.py. Findings below distinguish observed facts from inferred interpretation.

## 3. High-level block diagram

```mermaid
flowchart TD
    subgraph config_group
        config["Configuration and deployment"]
    end
    subgraph data_group
        data_layer["Data layer"]
    end
    subgraph entrypoint_group
        entrypoint["Application entry point"]
    end
    subgraph external_group
        external_integrations["External integrations"]
    end
    subgraph library_group
        deploying_service["deploying_service package"]
        others_project["others_project package"]
        pytorch_classification["pytorch_classification package"]
        pytorch_keypoint["pytorch_keypoint package"]
        pytorch_object_detection["pytorch_object_detection package"]
        pytorch_segmentation["pytorch_segmentation package"]
        tensorflow_classification["tensorflow_classification package"]
    end
    subgraph test_group
        tests["Tests"]
    end
    entrypoint -->|imports| external_integrations
    entrypoint -->|imports| pytorch_keypoint
    pytorch_keypoint -->|imports| entrypoint
```

## 4. Main components

### Configuration and deployment (`config`)

- **Kind:** config
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 53 file(s) under configuration and deployment (observed from repository paths and static analysis).
- **Paths:** `deploying_service/deploying_pytorch/convert_onnx_cls/class_indices.json`, `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/requirements.txt`, `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/requirements.txt`, `deploying_service/deploying_pytorch/pytorch_flask_service/class_indices.json`, `deploying_service/deploying_pytorch/pytorch_flask_service/requirements.txt`, `deploying_service/pruning_model_pytorch/class_indices.json`, `others_project/openvinotest/openvino_cls_test/class_indices.json`, `pytorch_classification/ConfusionMatrix/class_indices.json`, `pytorch_classification/Test11_efficientnetV2/class_indices.json`, `pytorch_classification/Test2_alexnet/class_indices.json`, `pytorch_classification/Test3_vggnet/class_indices.json`, `pytorch_classification/Test4_googlenet/class_indices.json`, `pytorch_classification/Test5_resnet/class_indices.json`, `pytorch_classification/Test6_mobilenet/class_indices.json`, `pytorch_classification/Test7_shufflenet/class_indices.json`, `pytorch_classification/Test9_efficientNet/requirements.txt`, `pytorch_classification/mini_imagenet/imagenet_class_index.json`, `pytorch_classification/tensorboard_test/requirements.txt`, `pytorch_classification/train_multi_GPU/requirements.txt`, `pytorch_keypoint/DeepPose/requirements.txt`, `pytorch_keypoint/HRNet/person_keypoints.json`, `pytorch_keypoint/HRNet/requirements.txt`, `pytorch_object_detection/faster_rcnn/pascal_voc_classes.json`, `pytorch_object_detection/faster_rcnn/requirements.txt`, `pytorch_object_detection/mask_rcnn/coco91_indices.json`, `pytorch_object_detection/mask_rcnn/pascal_voc_indices.json`, `pytorch_object_detection/mask_rcnn/requirements.txt`, `pytorch_object_detection/retinaNet/pascal_voc_classes.json`, `pytorch_object_detection/retinaNet/requirements.txt`, `pytorch_object_detection/ssd/pascal_voc_classes.json`, `pytorch_object_detection/ssd/requirements.txt`, `pytorch_object_detection/train_coco_dataset/coco91_indices.json`, `pytorch_object_detection/train_coco_dataset/requirements.txt`, `pytorch_object_detection/yolov3_spp/cfg/hyp.yaml`, `pytorch_object_detection/yolov3_spp/cfg/yolov3-spp.cfg`, `pytorch_object_detection/yolov3_spp/data/pascal_voc_classes.json`, `pytorch_object_detection/yolov3_spp/requirements.txt`, `pytorch_segmentation/deeplab_v3/palette.json`, `pytorch_segmentation/deeplab_v3/pascal_voc_classes.json`, `pytorch_segmentation/deeplab_v3/requirements.txt`, `pytorch_segmentation/fcn/palette.json`, `pytorch_segmentation/fcn/pascal_voc_classes.json`, `pytorch_segmentation/fcn/requirements.txt`, `pytorch_segmentation/lraspp/palette.json`, `pytorch_segmentation/lraspp/pascal_voc_classes.json`, `pytorch_segmentation/lraspp/requirements.txt`, `pytorch_segmentation/u2net/requirements.txt`, `pytorch_segmentation/unet/requirements.txt`, `tensorflow_classification/ConfusionMatrix/class_indices.json`, `tensorflow_classification/Test2_alexnet/class_indices.json`, `tensorflow_classification/Test3_vgg/class_indices.json`, `tensorflow_classification/Test4_goolenet/class_indices.json`, `tensorflow_classification/Test5_resnet/class_indices.json`
- **Evidence:** [deploying_service/deploying_pytorch/convert_onnx_cls/class_indices.json](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_onnx_cls/class_indices.json); [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/requirements.txt](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/requirements.txt); [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/requirements.txt](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/requirements.txt); [deploying_service/deploying_pytorch/pytorch_flask_service/class_indices.json](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/pytorch_flask_service/class_indices.json); [deploying_service/deploying_pytorch/pytorch_flask_service/requirements.txt](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/pytorch_flask_service/requirements.txt); [deploying_service/pruning_model_pytorch/class_indices.json](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/pruning_model_pytorch/class_indices.json); [others_project/openvinotest/openvino_cls_test/class_indices.json](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/openvinotest/openvino_cls_test/class_indices.json); [pytorch_classification/ConfusionMatrix/class_indices.json](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/ConfusionMatrix/class_indices.json)

### Data layer (`data_layer`)

- **Kind:** data
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 36 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AlexNet, AlexNet_v2, BasicBlock, BasicConv2d, BasicLayer, Block. Observed top-level functions: AlexNet_v1, GoogLeNet, MobileNetV2, VGG, _make_divisible, _make_layer.
- **Paths:** `deploying_service/deploying_pytorch/convert_onnx_cls/model.py`, `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/model.py`, `deploying_service/deploying_pytorch/pytorch_flask_service/model.py`, `deploying_service/pruning_model_pytorch/model.py`, `others_project/openvinotest/openvino_cls_test/model.py`, `others_project/textcnnKeras/models.py`, `pytorch_classification/ConfusionMatrix/model.py`, `pytorch_classification/ConvNeXt/model.py`, `pytorch_classification/MobileViT/model.py`, `pytorch_classification/Test10_regnet/model.py`, `pytorch_classification/Test11_efficientnetV2/model.py`, `pytorch_classification/Test1_official_demo/model.py`, `pytorch_classification/Test2_alexnet/model.py`, `pytorch_classification/Test3_vggnet/model.py`, `pytorch_classification/Test4_googlenet/model.py`, `pytorch_classification/Test5_resnet/model.py`, `pytorch_classification/Test7_shufflenet/model.py`, `pytorch_classification/Test8_densenet/model.py`, `pytorch_classification/Test9_efficientNet/model.py`, `pytorch_classification/mini_imagenet/model.py`, `pytorch_classification/model_complexity/model.py`, `pytorch_classification/swin_transformer/model.py`, `pytorch_classification/tensorboard_test/model.py`, `pytorch_classification/train_multi_GPU/model.py`, `pytorch_object_detection/yolov3_spp/models.py`, `tensorflow_classification/ConfusionMatrix/model.py`, `tensorflow_classification/ConvNeXt/model.py`, `tensorflow_classification/Test11_efficientnetV2/model.py`, `tensorflow_classification/Test1_official_demo/model.py`, `tensorflow_classification/Test2_alexnet/model.py`, `tensorflow_classification/Test3_vgg/model.py`, `tensorflow_classification/Test4_goolenet/model.py`, `tensorflow_classification/Test5_resnet/model.py`, `tensorflow_classification/Test7_shuffleNet/model.py`, `tensorflow_classification/Test9_efficientNet/model.py`, `tensorflow_classification/swin_transformer/model.py`
- **Evidence:** [deploying_service/deploying_pytorch/convert_onnx_cls/model.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_onnx_cls/model.py#L5); [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/model.py:9](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/model.py#L9); [deploying_service/deploying_pytorch/pytorch_flask_service/model.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/pytorch_flask_service/model.py#L5); [deploying_service/pruning_model_pytorch/model.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/pruning_model_pytorch/model.py#L5); [others_project/openvinotest/openvino_cls_test/model.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/openvinotest/openvino_cls_test/model.py#L5); [others_project/textcnnKeras/models.py:4](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/textcnnKeras/models.py#L4); [pytorch_classification/ConfusionMatrix/model.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/ConfusionMatrix/model.py#L5); [pytorch_classification/ConvNeXt/model.py:11](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/ConvNeXt/model.py#L11)

### deploying_service package (`deploying_service`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 7 file(s) under deploying_service package (observed from repository paths and static analysis). Observed top-level classes: Accuracy, EvalCOCOMetric, MAPMetric, MyDataLoader, MyDataSet. Observed top-level functions: _coco_remove_images_without_annotations, box_iou, clip_coords, draw_masks, draw_objs, draw_text.
- **Paths:** `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/utils.py`, `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/draw_box_utils.py`, `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/utils.py`, `deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/my_dataset.py`, `deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/utils.py`, `deploying_service/pruning_model_pytorch/predict.py`, `deploying_service/pruning_model_pytorch/train.py`
- **Evidence:** [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/utils.py:11](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/utils.py#L11); [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/draw_box_utils.py:34](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/draw_box_utils.py#L34); [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/utils.py:27](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/utils.py#L27); [deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/my_dataset.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/my_dataset.py#L6); [deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/utils.py:11](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/utils.py#L11); [deploying_service/pruning_model_pytorch/predict.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/pruning_model_pytorch/predict.py); [deploying_service/pruning_model_pytorch/train.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/pruning_model_pytorch/train.py)

### Application entry point (`entrypoint`)

- **Kind:** entrypoint
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 186 file(s) under application entry point (observed from repository paths and static analysis). Observed application object created via Flask. Observed routes: ROUTE /predict, ROUTE /. Observed top-level classes: CocoDetection, CocoKeypoint, ConfusionMatrix, ConvBNReLU, DUTSDataset, DownConvBNReLU. Observed top-level functions: AlexNet_pytorch, anchor_fitness, calculate_data_txt, calculate_split_info, cat_list, change_and_create_cfg_file.
- **Paths:** `data_set/split_data.py`, `deploying_service/deploying_pytorch/convert_onnx_cls/main.py`, `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_fps.py`, `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_onnx_and_ir.py`, `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/convert_pytorch2onnx.py`, `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/quantization_int8.py`, `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_fps.py`, `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_onnx_and_ir.py`, `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/evaluation.py`, `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/predict.py`, `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/quantization_int8.py`, `deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/compare_onnx_and_trt.py`, `deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/convert_pytorch2onnx.py`, `deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/quantization.py`, `deploying_service/deploying_pytorch/pytorch_flask_service/main.py`, `deploying_service/pruning_model_pytorch/main.py`, `others_project/draw_dilated_conv/main.py`, `others_project/kmeans_anchors/main.py`, `others_project/kmeans_anchors/plot_kmeans.py`, `others_project/openvinotest/openvino_cls_test/float32vsint8.py`, `others_project/openvinotest/openvino_cls_test/main.py`, `others_project/textcnnKeras/main.py`, `others_project/trans_widerface_to_xml/main.py`, `pytorch_classification/ConfusionMatrix/main.py`, `pytorch_classification/ConvNeXt/predict.py`, `pytorch_classification/ConvNeXt/train.py`, `pytorch_classification/MobileViT/predict.py`, `pytorch_classification/MobileViT/train.py`, `pytorch_classification/Test10_regnet/predict.py`, `pytorch_classification/Test10_regnet/pretrain_weights.py`, `pytorch_classification/Test10_regnet/train.py`, `pytorch_classification/Test11_efficientnetV2/predict.py`, `pytorch_classification/Test11_efficientnetV2/train.py`, `pytorch_classification/Test11_efficientnetV2/trans_effv2_weights.py`, `pytorch_classification/Test1_official_demo/predict.py`, `pytorch_classification/Test1_official_demo/train.py`, `pytorch_classification/Test2_alexnet/predict.py`, `pytorch_classification/Test2_alexnet/train.py`, `pytorch_classification/Test3_vggnet/predict.py`, `pytorch_classification/Test3_vggnet/train.py`, `pytorch_classification/Test4_googlenet/predict.py`, `pytorch_classification/Test4_googlenet/train.py`, `pytorch_classification/Test5_resnet/batch_predict.py`, `pytorch_classification/Test5_resnet/load_weights.py`, `pytorch_classification/Test5_resnet/predict.py`, `pytorch_classification/Test5_resnet/train.py`, `pytorch_classification/Test6_mobilenet/predict.py`, `pytorch_classification/Test6_mobilenet/train.py`, `pytorch_classification/Test7_shufflenet/predict.py`, `pytorch_classification/Test7_shufflenet/train.py`, `pytorch_classification/Test8_densenet/predict.py`, `pytorch_classification/Test8_densenet/train.py`, `pytorch_classification/Test9_efficientNet/predict.py`, `pytorch_classification/Test9_efficientNet/train.py`, `pytorch_classification/Test9_efficientNet/trans_weights_to_pytorch.py`, `pytorch_classification/custom_dataset/main.py`, `pytorch_classification/grad_cam/main_cnn.py`, `pytorch_classification/grad_cam/main_swin.py`, `pytorch_classification/grad_cam/main_vit.py`, `pytorch_classification/mini_imagenet/restructure_csv.py`, `pytorch_classification/mini_imagenet/train_multi_gpu_using_launch.py`, `pytorch_classification/mini_imagenet/train_single_gpu.py`, `pytorch_classification/model_complexity/main.py`, `pytorch_classification/swin_transformer/create_confusion_matrix.py`, `pytorch_classification/swin_transformer/predict.py`, `pytorch_classification/swin_transformer/select_incorrect_samples.py`, `pytorch_classification/swin_transformer/train.py`, `pytorch_classification/tensorboard_test/train.py`, `pytorch_classification/train_multi_GPU/train_multi_gpu_using_launch.py`, `pytorch_classification/train_multi_GPU/train_multi_gpu_using_spawn.py`, `pytorch_classification/train_multi_GPU/train_single_gpu.py`, `pytorch_classification/vision_transformer/flops.py`, `pytorch_classification/vision_transformer/predict.py`, `pytorch_classification/vision_transformer/train.py`, `pytorch_keypoint/DeepPose/datasets.py`, `pytorch_keypoint/DeepPose/export_onnx.py`, `pytorch_keypoint/DeepPose/model.py`, `pytorch_keypoint/DeepPose/predict.py`, `pytorch_keypoint/DeepPose/train.py`, `pytorch_keypoint/DeepPose/train_multi_GPU.py`, `pytorch_keypoint/DeepPose/train_utils/metrics.py`, `pytorch_keypoint/HRNet/my_dataset_coco.py`, `pytorch_keypoint/HRNet/predict.py`, `pytorch_keypoint/HRNet/train.py`, `pytorch_keypoint/HRNet/train_multi_GPU.py`, `pytorch_keypoint/HRNet/validation.py`, `pytorch_object_detection/faster_rcnn/change_backbone_with_fpn.py`, `pytorch_object_detection/faster_rcnn/change_backbone_without_fpn.py`, `pytorch_object_detection/faster_rcnn/predict.py`, `pytorch_object_detection/faster_rcnn/split_data.py`, `pytorch_object_detection/faster_rcnn/train_mobilenetv2.py`, `pytorch_object_detection/faster_rcnn/train_multi_GPU.py`, `pytorch_object_detection/faster_rcnn/train_res50_fpn.py`, `pytorch_object_detection/faster_rcnn/validation.py`, `pytorch_object_detection/mask_rcnn/my_dataset_coco.py`, `pytorch_object_detection/mask_rcnn/my_dataset_voc.py`, `pytorch_object_detection/mask_rcnn/predict.py`, `pytorch_object_detection/mask_rcnn/train.py`, `pytorch_object_detection/mask_rcnn/train_multi_GPU.py`, `pytorch_object_detection/mask_rcnn/validation.py`, `pytorch_object_detection/retinaNet/predict.py`, `pytorch_object_detection/retinaNet/train.py`, `pytorch_object_detection/retinaNet/train_multi_GPU.py`, `pytorch_object_detection/retinaNet/validation.py`, `pytorch_object_detection/ssd/train_multi_GPU.py`, `pytorch_object_detection/ssd/train_ssd300.py`, `pytorch_object_detection/ssd/validation.py`, `pytorch_object_detection/train_coco_dataset/change_backbone_with_fpn.py`, `pytorch_object_detection/train_coco_dataset/predict.py`, `pytorch_object_detection/train_coco_dataset/train.py`, `pytorch_object_detection/train_coco_dataset/train_multi_GPU.py`, `pytorch_object_detection/train_coco_dataset/validation.py`, `pytorch_object_detection/yolov3_spp/calculate_dataset.py`, `pytorch_object_detection/yolov3_spp/export_onnx.py`, `pytorch_object_detection/yolov3_spp/train.py`, `pytorch_object_detection/yolov3_spp/train_multi_GPU.py`, `pytorch_object_detection/yolov3_spp/trans_voc2yolo.py`, `pytorch_object_detection/yolov3_spp/validation.py`, `pytorch_segmentation/deeplab_v3/predict.py`, `pytorch_segmentation/deeplab_v3/train.py`, `pytorch_segmentation/deeplab_v3/train_multi_GPU.py`, `pytorch_segmentation/deeplab_v3/validation.py`, `pytorch_segmentation/fcn/predict.py`, `pytorch_segmentation/fcn/train.py`, `pytorch_segmentation/fcn/train_multi_GPU.py`, `pytorch_segmentation/fcn/validation.py`, `pytorch_segmentation/lraspp/predict.py`, `pytorch_segmentation/lraspp/train.py`, `pytorch_segmentation/lraspp/train_multi_GPU.py`, `pytorch_segmentation/lraspp/validation.py`, `pytorch_segmentation/u2net/convert_weight.py`, `pytorch_segmentation/u2net/my_dataset.py`, `pytorch_segmentation/u2net/predict.py`, `pytorch_segmentation/u2net/src/model.py`, `pytorch_segmentation/u2net/train.py`, `pytorch_segmentation/u2net/train_multi_GPU.py`, `pytorch_segmentation/u2net/validation.py`, `pytorch_segmentation/unet/compute_mean_std.py`, `pytorch_segmentation/unet/predict.py`, `pytorch_segmentation/unet/train.py`, `pytorch_segmentation/unet/train_multi_GPU.py`, `tensorflow_classification/ConfusionMatrix/main.py`, `tensorflow_classification/ConvNeXt/predict.py`, `tensorflow_classification/ConvNeXt/train.py`, `tensorflow_classification/ConvNeXt/trans_weights.py`, `tensorflow_classification/Test11_efficientnetV2/predict.py`, `tensorflow_classification/Test11_efficientnetV2/train.py`, `tensorflow_classification/Test11_efficientnetV2/trans_weights.py`, `tensorflow_classification/Test1_official_demo/train.py`, `tensorflow_classification/Test2_alexnet/fine_train_alexnet.py`, `tensorflow_classification/Test2_alexnet/predict.py`, `tensorflow_classification/Test2_alexnet/train.py`, `tensorflow_classification/Test2_alexnet/trainGPU.py`, `tensorflow_classification/Test3_vgg/fine_train_vgg16.py`, `tensorflow_classification/Test3_vgg/predict.py`, `tensorflow_classification/Test3_vgg/train.py`, `tensorflow_classification/Test3_vgg/trainGPU.py`, `tensorflow_classification/Test4_goolenet/predict.py`, `tensorflow_classification/Test4_goolenet/train.py`, `tensorflow_classification/Test4_goolenet/trainGPU.py`, `tensorflow_classification/Test4_goolenet/train_add_bn.py`, `tensorflow_classification/Test5_resnet/batch_predict.py`, `tensorflow_classification/Test5_resnet/predict.py`, `tensorflow_classification/Test5_resnet/read_ckpt.py`, `tensorflow_classification/Test5_resnet/train.py`, `tensorflow_classification/Test5_resnet/trainGPU.py`, `tensorflow_classification/Test6_mobilenet/predict.py`, `tensorflow_classification/Test6_mobilenet/read_ckpt.py`, `tensorflow_classification/Test6_mobilenet/trainGPU_mobilenet_v2.py`, `tensorflow_classification/Test6_mobilenet/train_mobilenet_v2.py`, `tensorflow_classification/Test6_mobilenet/train_mobilenet_v3.py`, `tensorflow_classification/Test6_mobilenet/trans_v3_weights.py`, `tensorflow_classification/Test7_shuffleNet/predict.py`, `tensorflow_classification/Test7_shuffleNet/train.py`, `tensorflow_classification/Test7_shuffleNet/trans_weights.py`, `tensorflow_classification/Test9_efficientNet/predict.py`, `tensorflow_classification/Test9_efficientNet/train.py`, `tensorflow_classification/custom_dataset/train_fit.py`, `tensorflow_classification/swin_transformer/predict.py`, `tensorflow_classification/swin_transformer/train.py`, `tensorflow_classification/swin_transformer/trans_weights.py`, `tensorflow_classification/tensorboard_test/train_fit.py`, `tensorflow_classification/tensorboard_test/train_not_fit.py`, `tensorflow_classification/vision_transformer/predict.py`, `tensorflow_classification/vision_transformer/train.py`, `tensorflow_classification/vision_transformer/trans_weights.py`
- **Evidence:** [data_set/split_data.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/data_set/split_data.py#L6); [deploying_service/deploying_pytorch/convert_onnx_cls/main.py:13](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_onnx_cls/main.py#L13); [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_fps.py:10](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_fps.py#L10); [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_onnx_and_ir.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_onnx_and_ir.py#L6); [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/convert_pytorch2onnx.py:11](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/convert_pytorch2onnx.py#L11); [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/quantization_int8.py:9](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/quantization_int8.py#L9); [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_fps.py:9](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_fps.py#L9); [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_onnx_and_ir.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_onnx_and_ir.py#L6)

### External integrations (`external_integrations`)

- **Kind:** external
- **Status:** Inferred
- **Confidence:** 0.70
- **Responsibility:** Groups 0 file(s) under external integrations (observed from repository paths and static analysis).
- **Evidence:** [pytorch_classification/Test10_regnet/pretrain_weights.py:1](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/Test10_regnet/pretrain_weights.py#L1)

### others_project package (`others_project`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 7 file(s) under others_project package (observed from repository paths and static analysis). Observed top-level classes: VOCDataSet, XMLGenerator. Observed top-level functions: content2idList, convert_type, create_pascal_voc_xml, create_xml_test, draw_box, draw_text.
- **Paths:** `others_project/kmeans_anchors/read_voc.py`, `others_project/kmeans_anchors/yolo_kmeans.py`, `others_project/openvinotest/openvino_cls_test/create_imagenet_annotation.py`, `others_project/readPbFile/readPb.py`, `others_project/readPbFile/using_function.py`, `others_project/textcnnKeras/dataGenerator.py`, `others_project/trans_widerface_to_xml/create_xml.py`
- **Evidence:** [others_project/kmeans_anchors/read_voc.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/kmeans_anchors/read_voc.py#L6); [others_project/kmeans_anchors/yolo_kmeans.py:4](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/kmeans_anchors/yolo_kmeans.py#L4); [others_project/openvinotest/openvino_cls_test/create_imagenet_annotation.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/openvinotest/openvino_cls_test/create_imagenet_annotation.py); [others_project/readPbFile/readPb.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/readPbFile/readPb.py); [others_project/readPbFile/using_function.py:37](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/readPbFile/using_function.py#L37); [others_project/textcnnKeras/dataGenerator.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/textcnnKeras/dataGenerator.py#L6); [others_project/trans_widerface_to_xml/create_xml.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/trans_widerface_to_xml/create_xml.py#L6)

### pytorch_classification package (`pytorch_classification`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 45 file(s) under pytorch_classification package (observed from repository paths and static analysis). Observed top-level classes: ActivationsAndGradients, AlexNet, Attention, BasicBlock, BasicLayer, Block. Observed top-level functions: _init_vit_weights, _make_divisible, center_crop_img, cleanup, conv2d_cx, create_lr_scheduler.
- **Paths:** `pytorch_classification/ConvNeXt/my_dataset.py`, `pytorch_classification/ConvNeXt/utils.py`, `pytorch_classification/MobileViT/model_config.py`, `pytorch_classification/MobileViT/my_dataset.py`, `pytorch_classification/MobileViT/transformer.py`, `pytorch_classification/MobileViT/utils.py`, `pytorch_classification/Test10_regnet/my_dataset.py`, `pytorch_classification/Test10_regnet/utils.py`, `pytorch_classification/Test11_efficientnetV2/my_dataset.py`, `pytorch_classification/Test11_efficientnetV2/utils.py`, `pytorch_classification/Test6_mobilenet/model_v2.py`, `pytorch_classification/Test6_mobilenet/model_v3.py`, `pytorch_classification/Test7_shufflenet/my_dataset.py`, `pytorch_classification/Test7_shufflenet/utils.py`, `pytorch_classification/Test8_densenet/my_dataset.py`, `pytorch_classification/Test8_densenet/utils.py`, `pytorch_classification/Test9_efficientNet/my_dataset.py`, `pytorch_classification/Test9_efficientNet/utils.py`, `pytorch_classification/analyze_weights_featuremap/alexnet_model.py`, `pytorch_classification/analyze_weights_featuremap/analyze_feature_map.py`, `pytorch_classification/analyze_weights_featuremap/analyze_kernel_weight.py`, `pytorch_classification/analyze_weights_featuremap/resnet_model.py`, `pytorch_classification/custom_dataset/my_dataset.py`, `pytorch_classification/custom_dataset/utils.py`, `pytorch_classification/grad_cam/swin_model.py`, `pytorch_classification/grad_cam/utils.py`, `pytorch_classification/grad_cam/vit_model.py`, `pytorch_classification/mini_imagenet/multi_train_utils/__init__.py`, `pytorch_classification/mini_imagenet/multi_train_utils/distributed_utils.py`, `pytorch_classification/mini_imagenet/multi_train_utils/train_eval_utils.py`, `pytorch_classification/mini_imagenet/my_dataset.py`, `pytorch_classification/model_complexity/utils.py`, `pytorch_classification/swin_transformer/my_dataset.py`, `pytorch_classification/swin_transformer/utils.py`, `pytorch_classification/tensorboard_test/data_utils.py`, `pytorch_classification/tensorboard_test/my_dataset.py`, `pytorch_classification/tensorboard_test/train_eval_utils.py`, `pytorch_classification/train_multi_GPU/multi_train_utils/distributed_utils.py`, `pytorch_classification/train_multi_GPU/multi_train_utils/train_eval_utils.py`, `pytorch_classification/train_multi_GPU/my_dataset.py`, `pytorch_classification/train_multi_GPU/plot_results.py`, `pytorch_classification/train_multi_GPU/utils.py`, `pytorch_classification/vision_transformer/my_dataset.py`, `pytorch_classification/vision_transformer/utils.py`, `pytorch_classification/vision_transformer/vit_model.py`
- **Evidence:** [pytorch_classification/ConvNeXt/my_dataset.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/ConvNeXt/my_dataset.py#L6); [pytorch_classification/ConvNeXt/utils.py:14](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/ConvNeXt/utils.py#L14); [pytorch_classification/MobileViT/model_config.py:1](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/MobileViT/model_config.py#L1); [pytorch_classification/MobileViT/my_dataset.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/MobileViT/my_dataset.py#L6); [pytorch_classification/MobileViT/transformer.py:8](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/MobileViT/transformer.py#L8); [pytorch_classification/MobileViT/utils.py:13](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/MobileViT/utils.py#L13); [pytorch_classification/Test10_regnet/my_dataset.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/Test10_regnet/my_dataset.py#L6); [pytorch_classification/Test10_regnet/utils.py:13](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/Test10_regnet/utils.py#L13)

### pytorch_keypoint package (`pytorch_keypoint`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 18 file(s) under pytorch_keypoint package (observed from repository paths and static analysis). Observed top-level classes: AffineTransform, BasicBlock, Bottleneck, Compose, EvalCOCOMetric, GroupedBatchSampler. Observed top-level functions: _compute_aspect_ratios_coco_dataset, _compute_aspect_ratios_custom_dataset, _compute_aspect_ratios_slow, _compute_aspect_ratios_subset_dataset, _compute_aspect_ratios_voc_dataset, _quantize.
- **Paths:** `pytorch_keypoint/DeepPose/train_utils/distributed_utils.py`, `pytorch_keypoint/DeepPose/train_utils/losses.py`, `pytorch_keypoint/DeepPose/train_utils/train_eval_utils.py`, `pytorch_keypoint/DeepPose/transforms.py`, `pytorch_keypoint/DeepPose/utils.py`, `pytorch_keypoint/DeepPose/wflw_horizontal_flip_indices.py`, `pytorch_keypoint/HRNet/draw_utils.py`, `pytorch_keypoint/HRNet/model/__init__.py`, `pytorch_keypoint/HRNet/model/hrnet.py`, `pytorch_keypoint/HRNet/plot_curve.py`, `pytorch_keypoint/HRNet/train_utils/__init__.py`, `pytorch_keypoint/HRNet/train_utils/coco_eval.py`, `pytorch_keypoint/HRNet/train_utils/coco_utils.py`, `pytorch_keypoint/HRNet/train_utils/distributed_utils.py`, `pytorch_keypoint/HRNet/train_utils/group_by_aspect_ratio.py`, `pytorch_keypoint/HRNet/train_utils/loss.py`, `pytorch_keypoint/HRNet/train_utils/train_eval_utils.py`, `pytorch_keypoint/HRNet/transforms.py`
- **Evidence:** [pytorch_keypoint/DeepPose/train_utils/distributed_utils.py:7](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/DeepPose/train_utils/distributed_utils.py#L7); [pytorch_keypoint/DeepPose/train_utils/losses.py:8](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/DeepPose/train_utils/losses.py#L8); [pytorch_keypoint/DeepPose/train_utils/train_eval_utils.py:15](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/DeepPose/train_utils/train_eval_utils.py#L15); [pytorch_keypoint/DeepPose/transforms.py:12](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/DeepPose/transforms.py#L12); [pytorch_keypoint/DeepPose/utils.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/DeepPose/utils.py#L5); [pytorch_keypoint/DeepPose/wflw_horizontal_flip_indices.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/DeepPose/wflw_horizontal_flip_indices.py); [pytorch_keypoint/HRNet/draw_utils.py:29](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/HRNet/draw_utils.py#L29); [pytorch_keypoint/HRNet/model/__init__.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/HRNet/model/__init__.py)

### pytorch_object_detection package (`pytorch_object_detection`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 117 file(s) under pytorch_object_detection package (observed from repository paths and static analysis). Observed top-level classes: AnchorsGenerator, AssignGTtoDefaultBox, Backbone, BackboneWithFPN, BalancedPositiveNegativeSampler, BasicBlock. Observed top-level functions: _coco_remove_images_without_annotations, _compute_aspect_ratios_coco_dataset, _compute_aspect_ratios_custom_dataset, _compute_aspect_ratios_slow, _compute_aspect_ratios_subset_dataset, _compute_aspect_ratios_voc_dataset.
- **Paths:** `pytorch_object_detection/faster_rcnn/backbone/__init__.py`, `pytorch_object_detection/faster_rcnn/backbone/feature_pyramid_network.py`, `pytorch_object_detection/faster_rcnn/backbone/mobilenetv2_model.py`, `pytorch_object_detection/faster_rcnn/backbone/resnet50_fpn_model.py`, `pytorch_object_detection/faster_rcnn/backbone/vgg_model.py`, `pytorch_object_detection/faster_rcnn/draw_box_utils.py`, `pytorch_object_detection/faster_rcnn/my_dataset.py`, `pytorch_object_detection/faster_rcnn/network_files/__init__.py`, `pytorch_object_detection/faster_rcnn/network_files/boxes.py`, `pytorch_object_detection/faster_rcnn/network_files/det_utils.py`, `pytorch_object_detection/faster_rcnn/network_files/faster_rcnn_framework.py`, `pytorch_object_detection/faster_rcnn/network_files/image_list.py`, `pytorch_object_detection/faster_rcnn/network_files/roi_head.py`, `pytorch_object_detection/faster_rcnn/network_files/rpn_function.py`, `pytorch_object_detection/faster_rcnn/network_files/transform.py`, `pytorch_object_detection/faster_rcnn/plot_curve.py`, `pytorch_object_detection/faster_rcnn/train_utils/__init__.py`, `pytorch_object_detection/faster_rcnn/train_utils/coco_eval.py`, `pytorch_object_detection/faster_rcnn/train_utils/coco_utils.py`, `pytorch_object_detection/faster_rcnn/train_utils/distributed_utils.py`, `pytorch_object_detection/faster_rcnn/train_utils/group_by_aspect_ratio.py`, `pytorch_object_detection/faster_rcnn/train_utils/train_eval_utils.py`, `pytorch_object_detection/faster_rcnn/transforms.py`, `pytorch_object_detection/mask_rcnn/backbone/__init__.py`, `pytorch_object_detection/mask_rcnn/backbone/feature_pyramid_network.py`, `pytorch_object_detection/mask_rcnn/backbone/resnet50_fpn_model.py`, `pytorch_object_detection/mask_rcnn/draw_box_utils.py`, `pytorch_object_detection/mask_rcnn/network_files/__init__.py`, `pytorch_object_detection/mask_rcnn/network_files/boxes.py`, `pytorch_object_detection/mask_rcnn/network_files/det_utils.py`, `pytorch_object_detection/mask_rcnn/network_files/faster_rcnn_framework.py`, `pytorch_object_detection/mask_rcnn/network_files/image_list.py`, `pytorch_object_detection/mask_rcnn/network_files/mask_rcnn.py`, `pytorch_object_detection/mask_rcnn/network_files/roi_head.py`, `pytorch_object_detection/mask_rcnn/network_files/rpn_function.py`, `pytorch_object_detection/mask_rcnn/network_files/transform.py`, `pytorch_object_detection/mask_rcnn/plot_curve.py`, `pytorch_object_detection/mask_rcnn/train_utils/__init__.py`, `pytorch_object_detection/mask_rcnn/train_utils/coco_eval.py`, `pytorch_object_detection/mask_rcnn/train_utils/coco_utils.py`, `pytorch_object_detection/mask_rcnn/train_utils/distributed_utils.py`, `pytorch_object_detection/mask_rcnn/train_utils/group_by_aspect_ratio.py`, `pytorch_object_detection/mask_rcnn/train_utils/train_eval_utils.py`, `pytorch_object_detection/mask_rcnn/transforms.py`, `pytorch_object_detection/retinaNet/backbone/__init__.py`, `pytorch_object_detection/retinaNet/backbone/feature_pyramid_network.py`, `pytorch_object_detection/retinaNet/backbone/resnet50_fpn_model.py`, `pytorch_object_detection/retinaNet/draw_box_utils.py`, `pytorch_object_detection/retinaNet/my_dataset.py`, `pytorch_object_detection/retinaNet/network_files/__init__.py`, `pytorch_object_detection/retinaNet/network_files/anchor_utils.py`, `pytorch_object_detection/retinaNet/network_files/boxes.py`, `pytorch_object_detection/retinaNet/network_files/det_utils.py`, `pytorch_object_detection/retinaNet/network_files/image_list.py`, `pytorch_object_detection/retinaNet/network_files/losses.py`, `pytorch_object_detection/retinaNet/network_files/retinanet.py`, `pytorch_object_detection/retinaNet/network_files/transform.py`, `pytorch_object_detection/retinaNet/plot_curve.py`, `pytorch_object_detection/retinaNet/train_utils/__init__.py`, `pytorch_object_detection/retinaNet/train_utils/coco_eval.py`, `pytorch_object_detection/retinaNet/train_utils/coco_utils.py`, `pytorch_object_detection/retinaNet/train_utils/distributed_utils.py`, `pytorch_object_detection/retinaNet/train_utils/group_by_aspect_ratio.py`, `pytorch_object_detection/retinaNet/train_utils/train_eval_utils.py`, `pytorch_object_detection/retinaNet/transforms.py`, `pytorch_object_detection/ssd/draw_box_utils.py`, `pytorch_object_detection/ssd/my_dataset.py`, `pytorch_object_detection/ssd/plot_curve.py`, `pytorch_object_detection/ssd/src/__init__.py`, `pytorch_object_detection/ssd/src/res50_backbone.py`, `pytorch_object_detection/ssd/src/ssd_model.py`, `pytorch_object_detection/ssd/src/utils.py`, `pytorch_object_detection/ssd/train_utils/__init__.py`, `pytorch_object_detection/ssd/train_utils/coco_eval.py`, `pytorch_object_detection/ssd/train_utils/coco_utils.py`, `pytorch_object_detection/ssd/train_utils/distributed_utils.py`, `pytorch_object_detection/ssd/train_utils/group_by_aspect_ratio.py`, `pytorch_object_detection/ssd/train_utils/train_eval_utils.py`, `pytorch_object_detection/ssd/transforms.py`, `pytorch_object_detection/train_coco_dataset/backbone/__init__.py`, `pytorch_object_detection/train_coco_dataset/backbone/feature_pyramid_network.py`, `pytorch_object_detection/train_coco_dataset/backbone/mobilenetv2_model.py`, `pytorch_object_detection/train_coco_dataset/backbone/resnet.py`, `pytorch_object_detection/train_coco_dataset/backbone/resnet50_fpn_model.py`, `pytorch_object_detection/train_coco_dataset/backbone/vgg_model.py`, `pytorch_object_detection/train_coco_dataset/compute_receptive_field.py`, `pytorch_object_detection/train_coco_dataset/draw_box_utils.py`, `pytorch_object_detection/train_coco_dataset/my_dataset.py`, `pytorch_object_detection/train_coco_dataset/network_files/__init__.py`, `pytorch_object_detection/train_coco_dataset/network_files/boxes.py`, `pytorch_object_detection/train_coco_dataset/network_files/det_utils.py`, `pytorch_object_detection/train_coco_dataset/network_files/faster_rcnn_framework.py`, `pytorch_object_detection/train_coco_dataset/network_files/image_list.py`, `pytorch_object_detection/train_coco_dataset/network_files/roi_head.py`, `pytorch_object_detection/train_coco_dataset/network_files/rpn_function.py`, `pytorch_object_detection/train_coco_dataset/network_files/transform.py`, `pytorch_object_detection/train_coco_dataset/plot_curve.py`, `pytorch_object_detection/train_coco_dataset/train_utils/__init__.py`, `pytorch_object_detection/train_coco_dataset/train_utils/coco_eval.py`, `pytorch_object_detection/train_coco_dataset/train_utils/distributed_utils.py`, `pytorch_object_detection/train_coco_dataset/train_utils/group_by_aspect_ratio.py`, `pytorch_object_detection/train_coco_dataset/train_utils/train_eval_utils.py`, `pytorch_object_detection/train_coco_dataset/transforms.py`, `pytorch_object_detection/yolov3_spp/build_utils/__init__.py`, `pytorch_object_detection/yolov3_spp/build_utils/datasets.py`, `pytorch_object_detection/yolov3_spp/build_utils/img_utils.py`, `pytorch_object_detection/yolov3_spp/build_utils/layers.py`, `pytorch_object_detection/yolov3_spp/build_utils/parse_config.py`, `pytorch_object_detection/yolov3_spp/build_utils/torch_utils.py`, `pytorch_object_detection/yolov3_spp/build_utils/utils.py`, `pytorch_object_detection/yolov3_spp/draw_box_utils.py`, `pytorch_object_detection/yolov3_spp/train_utils/__init__.py`, `pytorch_object_detection/yolov3_spp/train_utils/coco_eval.py`, `pytorch_object_detection/yolov3_spp/train_utils/coco_utils.py`, `pytorch_object_detection/yolov3_spp/train_utils/distributed_utils.py`, `pytorch_object_detection/yolov3_spp/train_utils/group_by_aspect_ratio.py`, `pytorch_object_detection/yolov3_spp/train_utils/train_eval_utils.py`
- **Evidence:** [pytorch_object_detection/faster_rcnn/backbone/__init__.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/backbone/__init__.py); [pytorch_object_detection/faster_rcnn/backbone/feature_pyramid_network.py:11](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/backbone/feature_pyramid_network.py#L11); [pytorch_object_detection/faster_rcnn/backbone/mobilenetv2_model.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/backbone/mobilenetv2_model.py#L6); [pytorch_object_detection/faster_rcnn/backbone/resnet50_fpn_model.py:10](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/backbone/resnet50_fpn_model.py#L10); [pytorch_object_detection/faster_rcnn/backbone/vgg_model.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/backbone/vgg_model.py#L5); [pytorch_object_detection/faster_rcnn/draw_box_utils.py:34](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/draw_box_utils.py#L34); [pytorch_object_detection/faster_rcnn/my_dataset.py:10](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/my_dataset.py#L10); [pytorch_object_detection/faster_rcnn/network_files/__init__.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/network_files/__init__.py)

### pytorch_segmentation package (`pytorch_segmentation`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 43 file(s) under pytorch_segmentation package (observed from repository paths and static analysis). Observed top-level classes: ASPP, ASPPConv, ASPPPooling, Bottleneck, CenterCrop, Compose. Observed top-level functions: _make_divisible, _resnet, all_gather, build_target, cat_list, conv1x1.
- **Paths:** `pytorch_segmentation/deeplab_v3/get_palette.py`, `pytorch_segmentation/deeplab_v3/my_dataset.py`, `pytorch_segmentation/deeplab_v3/src/__init__.py`, `pytorch_segmentation/deeplab_v3/src/deeplabv3_model.py`, `pytorch_segmentation/deeplab_v3/src/mobilenet_backbone.py`, `pytorch_segmentation/deeplab_v3/src/resnet_backbone.py`, `pytorch_segmentation/deeplab_v3/train_utils/__init__.py`, `pytorch_segmentation/deeplab_v3/train_utils/distributed_utils.py`, `pytorch_segmentation/deeplab_v3/train_utils/train_and_eval.py`, `pytorch_segmentation/deeplab_v3/transforms.py`, `pytorch_segmentation/fcn/get_palette.py`, `pytorch_segmentation/fcn/my_dataset.py`, `pytorch_segmentation/fcn/src/__init__.py`, `pytorch_segmentation/fcn/src/backbone.py`, `pytorch_segmentation/fcn/src/fcn_model.py`, `pytorch_segmentation/fcn/train_utils/__init__.py`, `pytorch_segmentation/fcn/train_utils/distributed_utils.py`, `pytorch_segmentation/fcn/train_utils/train_and_eval.py`, `pytorch_segmentation/fcn/transforms.py`, `pytorch_segmentation/lraspp/get_palette.py`, `pytorch_segmentation/lraspp/my_dataset.py`, `pytorch_segmentation/lraspp/src/__init__.py`, `pytorch_segmentation/lraspp/src/lraspp_model.py`, `pytorch_segmentation/lraspp/src/mobilenet_backbone.py`, `pytorch_segmentation/lraspp/train_utils/__init__.py`, `pytorch_segmentation/lraspp/train_utils/distributed_utils.py`, `pytorch_segmentation/lraspp/train_utils/train_and_eval.py`, `pytorch_segmentation/lraspp/transforms.py`, `pytorch_segmentation/u2net/src/__init__.py`, `pytorch_segmentation/u2net/train_utils/__init__.py`, `pytorch_segmentation/u2net/train_utils/distributed_utils.py`, `pytorch_segmentation/u2net/train_utils/train_and_eval.py`, `pytorch_segmentation/u2net/transforms.py`, `pytorch_segmentation/unet/my_dataset.py`, `pytorch_segmentation/unet/src/__init__.py`, `pytorch_segmentation/unet/src/mobilenet_unet.py`, `pytorch_segmentation/unet/src/unet.py`, `pytorch_segmentation/unet/src/vgg_unet.py`, `pytorch_segmentation/unet/train_utils/__init__.py`, `pytorch_segmentation/unet/train_utils/dice_coefficient_loss.py`, `pytorch_segmentation/unet/train_utils/distributed_utils.py`, `pytorch_segmentation/unet/train_utils/train_and_eval.py`, `pytorch_segmentation/unet/transforms.py`
- **Evidence:** [pytorch_segmentation/deeplab_v3/get_palette.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/get_palette.py); [pytorch_segmentation/deeplab_v3/my_dataset.py:7](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/my_dataset.py#L7); [pytorch_segmentation/deeplab_v3/src/__init__.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/src/__init__.py); [pytorch_segmentation/deeplab_v3/src/deeplabv3_model.py:12](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/src/deeplabv3_model.py#L12); [pytorch_segmentation/deeplab_v3/src/mobilenet_backbone.py:9](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/src/mobilenet_backbone.py#L9); [pytorch_segmentation/deeplab_v3/src/resnet_backbone.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/src/resnet_backbone.py#L5); [pytorch_segmentation/deeplab_v3/train_utils/__init__.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/train_utils/__init__.py); [pytorch_segmentation/deeplab_v3/train_utils/distributed_utils.py:11](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/train_utils/distributed_utils.py#L11)

### tensorflow_classification package (`tensorflow_classification`)

- **Kind:** library
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 20 file(s) under tensorflow_classification package (observed from repository paths and static analysis). Observed top-level classes: AlexNet_v2, Attention, BasicBlock, Block, Bottleneck, ConcatClassTokenAddPosEmbed. Observed top-level functions: AlexNet_v1, InceptionV1, MobileNetV2, _inverted_res_block, _make_divisible, _se_block.
- **Paths:** `tensorflow_classification/ConvNeXt/utils.py`, `tensorflow_classification/Test11_efficientnetV2/utils.py`, `tensorflow_classification/Test2_alexnet/read_pth.py`, `tensorflow_classification/Test3_vgg/read_ckpt.py`, `tensorflow_classification/Test4_goolenet/model_add_bn.py`, `tensorflow_classification/Test4_goolenet/read_pth.py`, `tensorflow_classification/Test5_resnet/read_h5.py`, `tensorflow_classification/Test5_resnet/subclassed_model.py`, `tensorflow_classification/Test6_mobilenet/model_v2.py`, `tensorflow_classification/Test6_mobilenet/model_v3.py`, `tensorflow_classification/Test6_mobilenet/utils.py`, `tensorflow_classification/Test7_shuffleNet/utils.py`, `tensorflow_classification/Test9_efficientNet/utils.py`, `tensorflow_classification/analyze_weights_featuremap/alexnet_model.py`, `tensorflow_classification/analyze_weights_featuremap/analyze_feature_map.py`, `tensorflow_classification/analyze_weights_featuremap/analyze_kernel_weight.py`, `tensorflow_classification/custom_dataset/utils.py`, `tensorflow_classification/swin_transformer/utils.py`, `tensorflow_classification/vision_transformer/utils.py`, `tensorflow_classification/vision_transformer/vit_model.py`
- **Evidence:** [tensorflow_classification/ConvNeXt/utils.py:11](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/ConvNeXt/utils.py#L11); [tensorflow_classification/Test11_efficientnetV2/utils.py:9](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/Test11_efficientnetV2/utils.py#L9); [tensorflow_classification/Test2_alexnet/read_pth.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/Test2_alexnet/read_pth.py#L6); [tensorflow_classification/Test3_vgg/read_ckpt.py:4](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/Test3_vgg/read_ckpt.py#L4); [tensorflow_classification/Test4_goolenet/model_add_bn.py:4](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/Test4_goolenet/model_add_bn.py#L4); [tensorflow_classification/Test4_goolenet/read_pth.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/Test4_goolenet/read_pth.py#L6); [tensorflow_classification/Test5_resnet/read_h5.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/Test5_resnet/read_h5.py); [tensorflow_classification/Test5_resnet/subclassed_model.py:4](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/Test5_resnet/subclassed_model.py#L4)

### Tests (`tests`)

- **Kind:** test
- **Status:** Observed
- **Confidence:** 0.85
- **Responsibility:** Groups 5 file(s) under tests (observed from repository paths and static analysis). Observed top-level functions: bboxes_iou, check_path_exist, clip_coords, create_model, main, my_self.
- **Paths:** `others_project/openvinotest/openvino_cls_test/speed_test.py`, `pytorch_classification/MobileViT/unfold_test.py`, `pytorch_object_detection/ssd/predict_test.py`, `pytorch_object_detection/yolov3_spp/load_onnx_test.py`, `pytorch_object_detection/yolov3_spp/predict_test.py`
- **Evidence:** [others_project/openvinotest/openvino_cls_test/speed_test.py:15](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/openvinotest/openvino_cls_test/speed_test.py#L15); [pytorch_classification/MobileViT/unfold_test.py:14](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/MobileViT/unfold_test.py#L14); [pytorch_object_detection/ssd/predict_test.py:14](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/ssd/predict_test.py#L14); [pytorch_object_detection/yolov3_spp/load_onnx_test.py:10](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/yolov3_spp/load_onnx_test.py#L10); [pytorch_object_detection/yolov3_spp/predict_test.py:16](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/yolov3_spp/predict_test.py#L16)

## 5. Execution flow

**Observed** entry point(s):

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
- [pytorch_segmentation/u2net/src/model.py:225](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/u2net/src/model.py#L225)

**Observed** routes (from decorators):

- `ROUTE /predict` -> `predict` in `deploying_service/deploying_pytorch/pytorch_flask_service/main.py:65`
- `ROUTE /` -> `root` in `deploying_service/deploying_pytorch/pytorch_flask_service/main.py:73`

Representative flow (derived from observed entry points and the import graph; steps beyond the entry point are **Inferred**):

1. Execution starts at an observed entry point listed above, if present.
2. `entrypoint` imports `external_integrations` (Application entry point -> External integrations).
3. `entrypoint` imports `pytorch_keypoint` (Application entry point -> pytorch_keypoint package).
4. `pytorch_keypoint` imports `entrypoint` (pytorch_keypoint package -> Application entry point).

## 6. Project structure

### `(root)`

- `.gitignore` - other (217 bytes)
- `LICENSE` - docs (35149 bytes)
- `README.md` - docs (8014 bytes)
- `summary_problem.md` - docs (1643 bytes)

### `.github`

- `.github/ISSUE_TEMPLATE/issue-template.md` - docs (481 bytes)

### `article_link`

- `article_link/README.md` - docs (8571 bytes)

### `course_ppt`

- `course_ppt/README.md` - docs (4413 bytes)

### `data_set`

- `data_set/README.md` - docs (757 bytes)
- `data_set/split_data.py` - source, Python (2295 bytes)

### `deploying_service`

- `deploying_service/deploying_pytorch/convert_onnx_cls/class_indices.json` - config (102 bytes)
- `deploying_service/deploying_pytorch/convert_onnx_cls/main.py` - source, Python (3247 bytes)
- `deploying_service/deploying_pytorch/convert_onnx_cls/model.py` - source, Python (5003 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/README.md` - docs (869 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_fps.py` - source, Python (3733 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_onnx_and_ir.py` - source, Python (1981 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/convert_pytorch2onnx.py` - source, Python (1797 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/model.py` - source, Python (12689 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/quantization_int8.py` - source, Python (2848 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/requirements.txt` - manifest (116 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/utils.py` - source, Python (5301 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/README.md` - docs (2071 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_fps.py` - source, Python (3597 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_onnx_and_ir.py` - source, Python (1879 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/draw_box_utils.py` - source, Python (6045 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/evaluation.py` - source, Python (1440 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/predict.py` - source, Python (1689 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/quantization_int8.py` - source, Python (3554 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/requirements.txt` - manifest (136 bytes)
- `deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/utils.py` - source, Python (21799 bytes)
- `deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/compare_onnx_and_trt.py` - source, Python (3181 bytes)
- `deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/convert_pytorch2onnx.py` - source, Python (1889 bytes)
- `deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/my_dataset.py` - source, Python (1165 bytes)
- `deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/quantization.py` - source, Python (7978 bytes)
- `deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/utils.py` - source, Python (5092 bytes)
- `deploying_service/deploying_pytorch/pytorch_flask_service/class_indices.json` - config (102 bytes)
- `deploying_service/deploying_pytorch/pytorch_flask_service/main.py` - source, Python (2529 bytes)
- `deploying_service/deploying_pytorch/pytorch_flask_service/model.py` - source, Python (4109 bytes)
- `deploying_service/deploying_pytorch/pytorch_flask_service/requirements.txt` - manifest (38 bytes)
- `deploying_service/deploying_pytorch/pytorch_flask_service/templates/up.html` - other (4455 bytes)
- `deploying_service/pruning_model_pytorch/class_indices.json` - config (102 bytes)
- `deploying_service/pruning_model_pytorch/main.py` - source, Python (3890 bytes)
- `deploying_service/pruning_model_pytorch/model.py` - source, Python (5003 bytes)
- `deploying_service/pruning_model_pytorch/predict.py` - source, Python (1188 bytes)
- `deploying_service/pruning_model_pytorch/train.py` - source, Python (4045 bytes)

### `others_project`

- `others_project/draw_dilated_conv/main.py` - source, Python (3080 bytes)
- `others_project/kmeans_anchors/main.py` - source, Python (2897 bytes)
- `others_project/kmeans_anchors/plot_kmeans.py` - source, Python (2110 bytes)
- `others_project/kmeans_anchors/read_voc.py` - source, Python (3008 bytes)
- `others_project/kmeans_anchors/yolo_kmeans.py` - source, Python (1265 bytes)
- `others_project/openvinotest/openvino_cls_test/class_indices.json` - config (102 bytes)
- `others_project/openvinotest/openvino_cls_test/create_imagenet_annotation.py` - source, Python (1075 bytes)
- `others_project/openvinotest/openvino_cls_test/float32vsint8.py` - source, Python (3661 bytes)
- `others_project/openvinotest/openvino_cls_test/main.py` - source, Python (3486 bytes)
- `others_project/openvinotest/openvino_cls_test/model.py` - source, Python (5003 bytes)
- `others_project/openvinotest/openvino_cls_test/speed_test.py` - test, Python (5932 bytes)
- `others_project/readPbFile/README.md` - docs (405 bytes)
- `others_project/readPbFile/export/checkpoint` - other (77 bytes)
- `others_project/readPbFile/pascal_label_map.pbtxt` - other (705 bytes)
- `others_project/readPbFile/readPb.py` - source, Python (2142 bytes)
- `others_project/readPbFile/test_images/image_info.txt` - docs (230 bytes)
- `others_project/readPbFile/using_function.py` - source, Python (6828 bytes)
- `others_project/textcnnKeras/dataGenerator.py` - source, Python (2445 bytes)
- `others_project/textcnnKeras/data_link.txt` - docs (86 bytes)
- `others_project/textcnnKeras/main.py` - source, Python (1409 bytes)
- `others_project/textcnnKeras/models.py` - source, Python (4468 bytes)
- `others_project/trans_widerface_to_xml/create_xml.py` - source, Python (4781 bytes)
- `others_project/trans_widerface_to_xml/main.py` - source, Python (4417 bytes)

### `pytorch_classification`

- `pytorch_classification/ConfusionMatrix/class_indices.json` - config (102 bytes)
- `pytorch_classification/ConfusionMatrix/main.py` - source, Python (4847 bytes)
- `pytorch_classification/ConfusionMatrix/model.py` - source, Python (4109 bytes)
- `pytorch_classification/ConvNeXt/README.md` - docs (1550 bytes)
- `pytorch_classification/ConvNeXt/model.py` - source, Python (9250 bytes)
- `pytorch_classification/ConvNeXt/my_dataset.py` - source, Python (1165 bytes)
- `pytorch_classification/ConvNeXt/predict.py` - source, Python (1983 bytes)
- `pytorch_classification/ConvNeXt/train.py` - source, Python (6240 bytes)
- `pytorch_classification/ConvNeXt/utils.py` - source, Python (9060 bytes)
- `pytorch_classification/MobileViT/README.md` - docs (1550 bytes)
- `pytorch_classification/MobileViT/model.py` - source, Python (19702 bytes)
- `pytorch_classification/MobileViT/model_config.py` - source, Python (5783 bytes)
- `pytorch_classification/MobileViT/my_dataset.py` - source, Python (1165 bytes)
- `pytorch_classification/MobileViT/predict.py` - source, Python (1922 bytes)
- `pytorch_classification/MobileViT/train.py` - source, Python (5885 bytes)
- `pytorch_classification/MobileViT/transformer.py` - source, Python (5008 bytes)
- `pytorch_classification/MobileViT/unfold_test.py` - test, Python (1753 bytes)
- `pytorch_classification/MobileViT/utils.py` - source, Python (7002 bytes)
- `pytorch_classification/README.md` - docs (510 bytes)
- `pytorch_classification/Test10_regnet/README.md` - docs (1534 bytes)
- `pytorch_classification/Test10_regnet/model.py` - source, Python (11457 bytes)
- `pytorch_classification/Test10_regnet/my_dataset.py` - source, Python (1165 bytes)
- `pytorch_classification/Test10_regnet/predict.py` - source, Python (1886 bytes)
- `pytorch_classification/Test10_regnet/pretrain_weights.py` - source, Python (4286 bytes)
- `pytorch_classification/Test10_regnet/train.py` - source, Python (6150 bytes)
- `pytorch_classification/Test10_regnet/utils.py` - source, Python (5992 bytes)
- `pytorch_classification/Test11_efficientnetV2/README.md` - docs (1534 bytes)
- `pytorch_classification/Test11_efficientnetV2/class_indices.json` - config (102 bytes)
- `pytorch_classification/Test11_efficientnetV2/model.py` - source, Python (13555 bytes)
- `pytorch_classification/Test11_efficientnetV2/my_dataset.py` - source, Python (1165 bytes)
- `pytorch_classification/Test11_efficientnetV2/predict.py` - source, Python (2046 bytes)
- `pytorch_classification/Test11_efficientnetV2/train.py` - source, Python (6395 bytes)
- `pytorch_classification/Test11_efficientnetV2/trans_effv2_weights.py` - source, Python (8695 bytes)
- `pytorch_classification/Test11_efficientnetV2/utils.py` - source, Python (6983 bytes)
- `pytorch_classification/Test1_official_demo/model.py` - source, Python (920 bytes)
- `pytorch_classification/Test1_official_demo/predict.py` - source, Python (768 bytes)
- `pytorch_classification/Test1_official_demo/train.py` - source, Python (2693 bytes)
- `pytorch_classification/Test2_alexnet/class_indices.json` - config (102 bytes)
- `pytorch_classification/Test2_alexnet/model.py` - source, Python (2061 bytes)
- `pytorch_classification/Test2_alexnet/predict.py` - source, Python (1858 bytes)
- `pytorch_classification/Test2_alexnet/train.py` - source, Python (5018 bytes)
- `pytorch_classification/Test3_vggnet/class_indices.json` - config (102 bytes)
- `pytorch_classification/Test3_vggnet/model.py` - source, Python (2616 bytes)
- `pytorch_classification/Test3_vggnet/predict.py` - source, Python (1894 bytes)
- `pytorch_classification/Test3_vggnet/train.py` - source, Python (4652 bytes)
- `pytorch_classification/Test4_googlenet/class_indices.json` - config (102 bytes)
- `pytorch_classification/Test4_googlenet/model.py` - source, Python (6184 bytes)
- `pytorch_classification/Test4_googlenet/predict.py` - source, Python (2006 bytes)
- `pytorch_classification/Test4_googlenet/train.py` - source, Python (5649 bytes)
- `pytorch_classification/Test5_resnet/README.md` - docs (206 bytes)
- `pytorch_classification/Test5_resnet/batch_predict.py` - source, Python (2509 bytes)
- `pytorch_classification/Test5_resnet/class_indices.json` - config (102 bytes)
- `pytorch_classification/Test5_resnet/load_weights.py` - source, Python (1184 bytes)
- `pytorch_classification/Test5_resnet/model.py` - source, Python (7225 bytes)
- `pytorch_classification/Test5_resnet/predict.py` - source, Python (1940 bytes)
- `pytorch_classification/Test5_resnet/train.py` - source, Python (5364 bytes)
- `pytorch_classification/Test6_mobilenet/class_indices.json` - config (102 bytes)
- `pytorch_classification/Test6_mobilenet/model_v2.py` - source, Python (4109 bytes)
- `pytorch_classification/Test6_mobilenet/model_v3.py` - source, Python (12689 bytes)
- `pytorch_classification/Test6_mobilenet/predict.py` - source, Python (1852 bytes)
- `pytorch_classification/Test6_mobilenet/train.py` - source, Python (5543 bytes)
- `pytorch_classification/Test7_shufflenet/README.md` - docs (1550 bytes)
- `pytorch_classification/Test7_shufflenet/class_indices.json` - config (102 bytes)
- `pytorch_classification/Test7_shufflenet/model.py` - source, Python (7748 bytes)
- `pytorch_classification/Test7_shufflenet/my_dataset.py` - source, Python (1165 bytes)
- `pytorch_classification/Test7_shufflenet/predict.py` - source, Python (1868 bytes)
- `pytorch_classification/Test7_shufflenet/train.py` - source, Python (5942 bytes)
- `pytorch_classification/Test7_shufflenet/utils.py` - source, Python (5992 bytes)
- `pytorch_classification/Test8_densenet/README.md` - docs (1550 bytes)
- `pytorch_classification/Test8_densenet/model.py` - source, Python (9965 bytes)
- `pytorch_classification/Test8_densenet/my_dataset.py` - source, Python (1165 bytes)
- `pytorch_classification/Test8_densenet/predict.py` - source, Python (1853 bytes)
- `pytorch_classification/Test8_densenet/train.py` - source, Python (5702 bytes)
- `pytorch_classification/Test8_densenet/utils.py` - source, Python (5992 bytes)
- `pytorch_classification/Test9_efficientNet/README.md` - docs (1534 bytes)
- `pytorch_classification/Test9_efficientNet/model.py` - source, Python (14251 bytes)
- `pytorch_classification/Test9_efficientNet/my_dataset.py` - source, Python (1165 bytes)
- `pytorch_classification/Test9_efficientNet/predict.py` - source, Python (2145 bytes)
- `pytorch_classification/Test9_efficientNet/requirements.txt` - manifest (62 bytes)
- `pytorch_classification/Test9_efficientNet/train.py` - source, Python (6343 bytes)
- `pytorch_classification/Test9_efficientNet/trans_weights_to_pytorch.py` - source, Python (4788 bytes)
- `pytorch_classification/Test9_efficientNet/utils.py` - source, Python (5992 bytes)
- `pytorch_classification/analyze_weights_featuremap/alexnet_model.py` - source, Python (2147 bytes)
- `pytorch_classification/analyze_weights_featuremap/analyze_feature_map.py` - source, Python (1334 bytes)
- `pytorch_classification/analyze_weights_featuremap/analyze_kernel_weight.py` - source, Python (1326 bytes)
- `pytorch_classification/analyze_weights_featuremap/resnet_model.py` - source, Python (5105 bytes)
- `pytorch_classification/custom_dataset/main.py` - source, Python (2049 bytes)
- `pytorch_classification/custom_dataset/my_dataset.py` - source, Python (1166 bytes)
- `pytorch_classification/custom_dataset/utils.py` - source, Python (4289 bytes)
- `pytorch_classification/grad_cam/README.md` - docs (644 bytes)
- `pytorch_classification/grad_cam/imagenet1k_classes.txt` - docs (21674 bytes)
- `pytorch_classification/grad_cam/main_cnn.py` - source, Python (1846 bytes)
- `pytorch_classification/grad_cam/main_swin.py` - source, Python (2696 bytes)
- `pytorch_classification/grad_cam/main_vit.py` - source, Python (2718 bytes)
- `pytorch_classification/grad_cam/swin_model.py` - source, Python (28563 bytes)
- `pytorch_classification/grad_cam/utils.py` - source, Python (8041 bytes)
- `pytorch_classification/grad_cam/vit_model.py` - source, Python (18234 bytes)
- `pytorch_classification/mini_imagenet/README.md` - docs (423 bytes)
- `pytorch_classification/mini_imagenet/imagenet_class_index.json` - config (35363 bytes)
- `pytorch_classification/mini_imagenet/model.py` - source, Python (6622 bytes)
- `pytorch_classification/mini_imagenet/multi_train_utils/__init__.py` - source, Python (124 bytes)
- `pytorch_classification/mini_imagenet/multi_train_utils/distributed_utils.py` - source, Python (2248 bytes)
- `pytorch_classification/mini_imagenet/multi_train_utils/train_eval_utils.py` - source, Python (3215 bytes)
- `pytorch_classification/mini_imagenet/my_dataset.py` - source, Python (1913 bytes)
- `pytorch_classification/mini_imagenet/restructure_csv.py` - source, Python (3194 bytes)
- `pytorch_classification/mini_imagenet/train_multi_gpu_using_launch.py` - source, Python (8293 bytes)
- `pytorch_classification/mini_imagenet/train_single_gpu.py` - source, Python (6070 bytes)
- `pytorch_classification/model_complexity/main.py` - source, Python (1044 bytes)
- `pytorch_classification/model_complexity/model.py` - source, Python (16199 bytes)
- `pytorch_classification/model_complexity/utils.py` - source, Python (2237 bytes)
- `pytorch_classification/swin_transformer/README.md` - docs (1550 bytes)
- `pytorch_classification/swin_transformer/create_confusion_matrix.py` - source, Python (5926 bytes)
- `pytorch_classification/swin_transformer/model.py` - source, Python (28563 bytes)
- `pytorch_classification/swin_transformer/my_dataset.py` - source, Python (1165 bytes)
- `pytorch_classification/swin_transformer/predict.py` - source, Python (1928 bytes)
- `pytorch_classification/swin_transformer/select_incorrect_samples.py` - source, Python (3806 bytes)
- `pytorch_classification/swin_transformer/train.py` - source, Python (5675 bytes)
- `pytorch_classification/swin_transformer/utils.py` - source, Python (6983 bytes)
- `pytorch_classification/tensorboard_test/data_utils.py` - source, Python (7857 bytes)
- `pytorch_classification/tensorboard_test/model.py` - source, Python (5003 bytes)
- `pytorch_classification/tensorboard_test/my_dataset.py` - source, Python (1611 bytes)
- `pytorch_classification/tensorboard_test/requirements.txt` - manifest (83 bytes)
- `pytorch_classification/tensorboard_test/train.py` - source, Python (7270 bytes)
- `pytorch_classification/tensorboard_test/train_eval_utils.py` - source, Python (1588 bytes)
- `pytorch_classification/train_multi_GPU/README.md` - docs (810 bytes)
- `pytorch_classification/train_multi_GPU/model.py` - source, Python (5003 bytes)
- `pytorch_classification/train_multi_GPU/multi_train_utils/distributed_utils.py` - source, Python (1769 bytes)
- `pytorch_classification/train_multi_GPU/multi_train_utils/train_eval_utils.py` - source, Python (1992 bytes)
- `pytorch_classification/train_multi_GPU/my_dataset.py` - source, Python (1165 bytes)
- `pytorch_classification/train_multi_GPU/plot_results.py` - source, Python (3107 bytes)
- `pytorch_classification/train_multi_GPU/requirements.txt` - manifest (64 bytes)
- `pytorch_classification/train_multi_GPU/train_multi_gpu_using_launch.py` - source, Python (8665 bytes)
- `pytorch_classification/train_multi_GPU/train_multi_gpu_using_spawn.py` - source, Python (9748 bytes)
- `pytorch_classification/train_multi_GPU/train_single_gpu.py` - source, Python (6360 bytes)
- `pytorch_classification/train_multi_GPU/utils.py` - source, Python (4558 bytes)
- `pytorch_classification/vision_transformer/README.md` - docs (1554 bytes)
- `pytorch_classification/vision_transformer/flops.py` - source, Python (591 bytes)
- `pytorch_classification/vision_transformer/my_dataset.py` - source, Python (1165 bytes)
- `pytorch_classification/vision_transformer/predict.py` - source, Python (1895 bytes)
- `pytorch_classification/vision_transformer/train.py` - source, Python (6213 bytes)
- `pytorch_classification/vision_transformer/utils.py` - source, Python (6983 bytes)
- `pytorch_classification/vision_transformer/vit_model.py` - source, Python (18234 bytes)

### `pytorch_keypoint`

- `pytorch_keypoint/DeepPose/README.md` - docs (3010 bytes)
- `pytorch_keypoint/DeepPose/datasets.py` - source, Python (4198 bytes)
- `pytorch_keypoint/DeepPose/export_onnx.py` - source, Python (843 bytes)
- `pytorch_keypoint/DeepPose/model.py` - source, Python (582 bytes)
- `pytorch_keypoint/DeepPose/predict.py` - source, Python (1816 bytes)
- `pytorch_keypoint/DeepPose/requirements.txt` - manifest (63 bytes)
- `pytorch_keypoint/DeepPose/train.py` - source, Python (7267 bytes)
- `pytorch_keypoint/DeepPose/train_multi_GPU.py` - source, Python (7970 bytes)
- `pytorch_keypoint/DeepPose/train_utils/distributed_utils.py` - source, Python (2626 bytes)
- `pytorch_keypoint/DeepPose/train_utils/losses.py` - source, Python (4085 bytes)
- `pytorch_keypoint/DeepPose/train_utils/metrics.py` - source, Python (2027 bytes)
- `pytorch_keypoint/DeepPose/train_utils/train_eval_utils.py` - source, Python (3299 bytes)
- `pytorch_keypoint/DeepPose/transforms.py` - source, Python (8029 bytes)
- `pytorch_keypoint/DeepPose/utils.py` - source, Python (554 bytes)
- `pytorch_keypoint/DeepPose/wflw_horizontal_flip_indices.py` - source, Python (1185 bytes)
- `pytorch_keypoint/HRNet/README.md` - docs (6158 bytes)
- `pytorch_keypoint/HRNet/draw_utils.py` - source, Python (2055 bytes)
- `pytorch_keypoint/HRNet/model/__init__.py` - source, Python (37 bytes)
- `pytorch_keypoint/HRNet/model/hrnet.py` - source, Python (10789 bytes)
- `pytorch_keypoint/HRNet/my_dataset_coco.py` - source, Python (4103 bytes)
- `pytorch_keypoint/HRNet/person_keypoints.json` - config (667 bytes)
- `pytorch_keypoint/HRNet/plot_curve.py` - source, Python (1478 bytes)
- `pytorch_keypoint/HRNet/predict.py` - source, Python (2753 bytes)
- `pytorch_keypoint/HRNet/requirements.txt` - manifest (96 bytes)
- `pytorch_keypoint/HRNet/train.py` - source, Python (10112 bytes)
- `pytorch_keypoint/HRNet/train_multi_GPU.py` - source, Python (12171 bytes)
- `pytorch_keypoint/HRNet/train_utils/__init__.py` - source, Python (305 bytes)
- `pytorch_keypoint/HRNet/train_utils/coco_eval.py` - source, Python (4853 bytes)
- `pytorch_keypoint/HRNet/train_utils/coco_utils.py` - source, Python (3395 bytes)
- `pytorch_keypoint/HRNet/train_utils/distributed_utils.py` - source, Python (9603 bytes)
- `pytorch_keypoint/HRNet/train_utils/group_by_aspect_ratio.py` - source, Python (7533 bytes)
- `pytorch_keypoint/HRNet/train_utils/loss.py` - source, Python (710 bytes)
- `pytorch_keypoint/HRNet/train_utils/train_eval_utils.py` - source, Python (4293 bytes)
- `pytorch_keypoint/HRNet/transforms.py` - source, Python (16808 bytes)
- `pytorch_keypoint/HRNet/validation.py` - source, Python (7967 bytes)

### `pytorch_object_detection`

- `pytorch_object_detection/faster_rcnn/README.md` - docs (4435 bytes)
- `pytorch_object_detection/faster_rcnn/backbone/__init__.py` - source, Python (195 bytes)
- `pytorch_object_detection/faster_rcnn/backbone/feature_pyramid_network.py` - source, Python (9270 bytes)
- `pytorch_object_detection/faster_rcnn/backbone/mobilenetv2_model.py` - source, Python (4687 bytes)
- `pytorch_object_detection/faster_rcnn/backbone/resnet50_fpn_model.py` - source, Python (7796 bytes)
- `pytorch_object_detection/faster_rcnn/backbone/vgg_model.py` - source, Python (2450 bytes)
- `pytorch_object_detection/faster_rcnn/change_backbone_with_fpn.py` - source, Python (11620 bytes)
- `pytorch_object_detection/faster_rcnn/change_backbone_without_fpn.py` - source, Python (10781 bytes)
- `pytorch_object_detection/faster_rcnn/draw_box_utils.py` - source, Python (6045 bytes)
- `pytorch_object_detection/faster_rcnn/my_dataset.py` - source, Python (8978 bytes)
- `pytorch_object_detection/faster_rcnn/network_files/__init__.py` - source, Python (108 bytes)
- `pytorch_object_detection/faster_rcnn/network_files/boxes.py` - source, Python (6278 bytes)
- `pytorch_object_detection/faster_rcnn/network_files/det_utils.py` - source, Python (16839 bytes)
- `pytorch_object_detection/faster_rcnn/network_files/faster_rcnn_framework.py` - source, Python (17254 bytes)
- `pytorch_object_detection/faster_rcnn/network_files/image_list.py` - source, Python (829 bytes)
- `pytorch_object_detection/faster_rcnn/network_files/roi_head.py` - source, Python (17578 bytes)
- `pytorch_object_detection/faster_rcnn/network_files/rpn_function.py` - source, Python (30098 bytes)
- `pytorch_object_detection/faster_rcnn/network_files/transform.py` - source, Python (12293 bytes)
- `pytorch_object_detection/faster_rcnn/pascal_voc_classes.json` - config (348 bytes)
- `pytorch_object_detection/faster_rcnn/plot_curve.py` - source, Python (1478 bytes)
- `pytorch_object_detection/faster_rcnn/predict.py` - source, Python (3935 bytes)
- `pytorch_object_detection/faster_rcnn/record_mAP.txt` - docs (1744 bytes)
- `pytorch_object_detection/faster_rcnn/requirements.txt` - manifest (78 bytes)
- `pytorch_object_detection/faster_rcnn/split_data.py` - source, Python (962 bytes)
- `pytorch_object_detection/faster_rcnn/train_mobilenetv2.py` - source, Python (9942 bytes)
- `pytorch_object_detection/faster_rcnn/train_multi_GPU.py` - source, Python (11682 bytes)
- `pytorch_object_detection/faster_rcnn/train_res50_fpn.py` - source, Python (10830 bytes)
- `pytorch_object_detection/faster_rcnn/train_utils/__init__.py` - source, Python (246 bytes)
- `pytorch_object_detection/faster_rcnn/train_utils/coco_eval.py` - source, Python (11998 bytes)
- `pytorch_object_detection/faster_rcnn/train_utils/coco_utils.py` - source, Python (1805 bytes)
- `pytorch_object_detection/faster_rcnn/train_utils/distributed_utils.py` - source, Python (10687 bytes)
- `pytorch_object_detection/faster_rcnn/train_utils/group_by_aspect_ratio.py` - source, Python (7557 bytes)
- `pytorch_object_detection/faster_rcnn/train_utils/train_eval_utils.py` - source, Python (4234 bytes)
- `pytorch_object_detection/faster_rcnn/transforms.py` - source, Python (1067 bytes)
- `pytorch_object_detection/faster_rcnn/validation.py` - source, Python (8147 bytes)
- `pytorch_object_detection/mask_rcnn/README.md` - docs (9373 bytes)
- `pytorch_object_detection/mask_rcnn/backbone/__init__.py` - source, Python (54 bytes)
- `pytorch_object_detection/mask_rcnn/backbone/feature_pyramid_network.py` - source, Python (9223 bytes)
- `pytorch_object_detection/mask_rcnn/backbone/resnet50_fpn_model.py` - source, Python (7609 bytes)
- `pytorch_object_detection/mask_rcnn/coco91_indices.json` - config (1824 bytes)
- `pytorch_object_detection/mask_rcnn/det_results20220406-141544.txt` - docs (2760 bytes)
- `pytorch_object_detection/mask_rcnn/draw_box_utils.py` - source, Python (6044 bytes)
- `pytorch_object_detection/mask_rcnn/my_dataset_coco.py` - source, Python (5314 bytes)
- `pytorch_object_detection/mask_rcnn/my_dataset_voc.py` - source, Python (8220 bytes)
- `pytorch_object_detection/mask_rcnn/network_files/__init__.py` - source, Python (140 bytes)
- `pytorch_object_detection/mask_rcnn/network_files/boxes.py` - source, Python (6278 bytes)
- `pytorch_object_detection/mask_rcnn/network_files/det_utils.py` - source, Python (16839 bytes)
- `pytorch_object_detection/mask_rcnn/network_files/faster_rcnn_framework.py` - source, Python (17255 bytes)
- `pytorch_object_detection/mask_rcnn/network_files/image_list.py` - source, Python (829 bytes)
- `pytorch_object_detection/mask_rcnn/network_files/mask_rcnn.py` - source, Python (11793 bytes)
- `pytorch_object_detection/mask_rcnn/network_files/roi_head.py` - source, Python (23580 bytes)
- `pytorch_object_detection/mask_rcnn/network_files/rpn_function.py` - source, Python (29487 bytes)
- `pytorch_object_detection/mask_rcnn/network_files/transform.py` - source, Python (18965 bytes)
- `pytorch_object_detection/mask_rcnn/pascal_voc_indices.json` - config (388 bytes)
- `pytorch_object_detection/mask_rcnn/plot_curve.py` - source, Python (1478 bytes)
- `pytorch_object_detection/mask_rcnn/predict.py` - source, Python (3505 bytes)
- `pytorch_object_detection/mask_rcnn/requirements.txt` - manifest (80 bytes)
- `pytorch_object_detection/mask_rcnn/seg_results20220406-141544.txt` - docs (2759 bytes)
- `pytorch_object_detection/mask_rcnn/train.py` - source, Python (11615 bytes)
- `pytorch_object_detection/mask_rcnn/train_multi_GPU.py` - source, Python (12345 bytes)
- `pytorch_object_detection/mask_rcnn/train_utils/__init__.py` - source, Python (305 bytes)
- `pytorch_object_detection/mask_rcnn/train_utils/coco_eval.py` - source, Python (6523 bytes)
- `pytorch_object_detection/mask_rcnn/train_utils/coco_utils.py` - source, Python (3395 bytes)
- `pytorch_object_detection/mask_rcnn/train_utils/distributed_utils.py` - source, Python (9599 bytes)
- `pytorch_object_detection/mask_rcnn/train_utils/group_by_aspect_ratio.py` - source, Python (7533 bytes)
- `pytorch_object_detection/mask_rcnn/train_utils/train_eval_utils.py` - source, Python (3932 bytes)
- `pytorch_object_detection/mask_rcnn/transforms.py` - source, Python (1160 bytes)
- `pytorch_object_detection/mask_rcnn/validation.py` - source, Python (8323 bytes)
- `pytorch_object_detection/retinaNet/README.md` - docs (4569 bytes)
- `pytorch_object_detection/retinaNet/backbone/__init__.py` - source, Python (146 bytes)
- `pytorch_object_detection/retinaNet/backbone/feature_pyramid_network.py` - source, Python (10783 bytes)
- `pytorch_object_detection/retinaNet/backbone/resnet50_fpn_model.py` - source, Python (7792 bytes)
- `pytorch_object_detection/retinaNet/draw_box_utils.py` - source, Python (6045 bytes)
- `pytorch_object_detection/retinaNet/my_dataset.py` - source, Python (8468 bytes)
- `pytorch_object_detection/retinaNet/network_files/__init__.py` - source, Python (33 bytes)
- `pytorch_object_detection/retinaNet/network_files/anchor_utils.py` - source, Python (8771 bytes)
- `pytorch_object_detection/retinaNet/network_files/boxes.py` - source, Python (6278 bytes)
- `pytorch_object_detection/retinaNet/network_files/det_utils.py` - source, Python (16784 bytes)
- `pytorch_object_detection/retinaNet/network_files/image_list.py` - source, Python (829 bytes)
- `pytorch_object_detection/retinaNet/network_files/losses.py` - source, Python (1746 bytes)
- `pytorch_object_detection/retinaNet/network_files/retinanet.py` - source, Python (23351 bytes)
- `pytorch_object_detection/retinaNet/network_files/transform.py` - source, Python (12293 bytes)
- `pytorch_object_detection/retinaNet/pascal_voc_classes.json` - config (347 bytes)
- `pytorch_object_detection/retinaNet/plot_curve.py` - source, Python (1478 bytes)
- `pytorch_object_detection/retinaNet/predict.py` - source, Python (3300 bytes)
- `pytorch_object_detection/retinaNet/requirements.txt` - manifest (78 bytes)
- `pytorch_object_detection/retinaNet/results20210421-142632.txt` - docs (2345 bytes)
- `pytorch_object_detection/retinaNet/train.py` - source, Python (9634 bytes)
- `pytorch_object_detection/retinaNet/train_multi_GPU.py` - source, Python (11615 bytes)
- `pytorch_object_detection/retinaNet/train_utils/__init__.py` - source, Python (246 bytes)
- `pytorch_object_detection/retinaNet/train_utils/coco_eval.py` - source, Python (11987 bytes)
- `pytorch_object_detection/retinaNet/train_utils/coco_utils.py` - source, Python (1805 bytes)
- `pytorch_object_detection/retinaNet/train_utils/distributed_utils.py` - source, Python (10620 bytes)
- `pytorch_object_detection/retinaNet/train_utils/group_by_aspect_ratio.py` - source, Python (7533 bytes)
- `pytorch_object_detection/retinaNet/train_utils/train_eval_utils.py` - source, Python (4235 bytes)
- `pytorch_object_detection/retinaNet/transforms.py` - source, Python (1067 bytes)
- `pytorch_object_detection/retinaNet/validation.py` - source, Python (8238 bytes)
- `pytorch_object_detection/ssd/README.md` - docs (2826 bytes)
- `pytorch_object_detection/ssd/draw_box_utils.py` - source, Python (6045 bytes)
- `pytorch_object_detection/ssd/my_dataset.py` - source, Python (9231 bytes)
- `pytorch_object_detection/ssd/pascal_voc_classes.json` - config (348 bytes)
- `pytorch_object_detection/ssd/plot_curve.py` - source, Python (1479 bytes)
- `pytorch_object_detection/ssd/predict_test.py` - test, Python (3138 bytes)
- `pytorch_object_detection/ssd/record_mAP.txt` - docs (1746 bytes)
- `pytorch_object_detection/ssd/requirements.txt` - manifest (78 bytes)
- `pytorch_object_detection/ssd/src/__init__.py` - source, Python (150 bytes)
- `pytorch_object_detection/ssd/src/res50_backbone.py` - source, Python (3850 bytes)
- `pytorch_object_detection/ssd/src/ssd_model.py` - source, Python (9566 bytes)
- `pytorch_object_detection/ssd/src/utils.py` - source, Python (26177 bytes)
- `pytorch_object_detection/ssd/train_multi_GPU.py` - source, Python (11086 bytes)
- `pytorch_object_detection/ssd/train_ssd300.py` - source, Python (8577 bytes)
- `pytorch_object_detection/ssd/train_utils/__init__.py` - source, Python (246 bytes)
- `pytorch_object_detection/ssd/train_utils/coco_eval.py` - source, Python (12062 bytes)
- `pytorch_object_detection/ssd/train_utils/coco_utils.py` - source, Python (2394 bytes)
- `pytorch_object_detection/ssd/train_utils/distributed_utils.py` - source, Python (10620 bytes)
- `pytorch_object_detection/ssd/train_utils/group_by_aspect_ratio.py` - source, Python (7533 bytes)
- `pytorch_object_detection/ssd/train_utils/train_eval_utils.py` - source, Python (4961 bytes)
- `pytorch_object_detection/ssd/transforms.py` - source, Python (7127 bytes)
- `pytorch_object_detection/ssd/validation.py` - source, Python (8800 bytes)
- `pytorch_object_detection/train_coco_dataset/README.md` - docs (5553 bytes)
- `pytorch_object_detection/train_coco_dataset/backbone/__init__.py` - source, Python (217 bytes)
- `pytorch_object_detection/train_coco_dataset/backbone/feature_pyramid_network.py` - source, Python (9223 bytes)
- `pytorch_object_detection/train_coco_dataset/backbone/mobilenetv2_model.py` - source, Python (4654 bytes)
- `pytorch_object_detection/train_coco_dataset/backbone/resnet.py` - source, Python (7225 bytes)
- `pytorch_object_detection/train_coco_dataset/backbone/resnet50_fpn_model.py` - source, Python (7796 bytes)
- `pytorch_object_detection/train_coco_dataset/backbone/vgg_model.py` - source, Python (2450 bytes)
- `pytorch_object_detection/train_coco_dataset/change_backbone_with_fpn.py` - source, Python (11819 bytes)
- `pytorch_object_detection/train_coco_dataset/coco91_indices.json` - config (1824 bytes)
- `pytorch_object_detection/train_coco_dataset/compute_receptive_field.py` - source, Python (463 bytes)
- `pytorch_object_detection/train_coco_dataset/draw_box_utils.py` - source, Python (6045 bytes)
- `pytorch_object_detection/train_coco_dataset/my_dataset.py` - source, Python (6015 bytes)
- `pytorch_object_detection/train_coco_dataset/network_files/__init__.py` - source, Python (108 bytes)
- `pytorch_object_detection/train_coco_dataset/network_files/boxes.py` - source, Python (6278 bytes)
- `pytorch_object_detection/train_coco_dataset/network_files/det_utils.py` - source, Python (16839 bytes)
- `pytorch_object_detection/train_coco_dataset/network_files/faster_rcnn_framework.py` - source, Python (17253 bytes)
- `pytorch_object_detection/train_coco_dataset/network_files/image_list.py` - source, Python (829 bytes)
- `pytorch_object_detection/train_coco_dataset/network_files/roi_head.py` - source, Python (17578 bytes)
- `pytorch_object_detection/train_coco_dataset/network_files/rpn_function.py` - source, Python (29487 bytes)
- `pytorch_object_detection/train_coco_dataset/network_files/transform.py` - source, Python (12293 bytes)
- `pytorch_object_detection/train_coco_dataset/plot_curve.py` - source, Python (1478 bytes)
- `pytorch_object_detection/train_coco_dataset/predict.py` - source, Python (3800 bytes)
- `pytorch_object_detection/train_coco_dataset/requirements.txt` - manifest (78 bytes)
- `pytorch_object_detection/train_coco_dataset/results20220408-201436.txt` - docs (3162 bytes)
- `pytorch_object_detection/train_coco_dataset/train.py` - source, Python (11211 bytes)
- `pytorch_object_detection/train_coco_dataset/train_multi_GPU.py` - source, Python (11188 bytes)
- `pytorch_object_detection/train_coco_dataset/train_utils/__init__.py` - source, Python (197 bytes)
- `pytorch_object_detection/train_coco_dataset/train_utils/coco_eval.py` - source, Python (6523 bytes)
- `pytorch_object_detection/train_coco_dataset/train_utils/distributed_utils.py` - source, Python (9599 bytes)
- `pytorch_object_detection/train_coco_dataset/train_utils/group_by_aspect_ratio.py` - source, Python (7533 bytes)
- `pytorch_object_detection/train_coco_dataset/train_utils/train_eval_utils.py` - source, Python (3663 bytes)
- `pytorch_object_detection/train_coco_dataset/transforms.py` - source, Python (1067 bytes)
- `pytorch_object_detection/train_coco_dataset/validation.py` - source, Python (8391 bytes)
- `pytorch_object_detection/yolov3_spp/README.md` - docs (7254 bytes)
- `pytorch_object_detection/yolov3_spp/build_utils/__init__.py` - source, Python (0 bytes)
- `pytorch_object_detection/yolov3_spp/build_utils/datasets.py` - source, Python (28697 bytes)
- `pytorch_object_detection/yolov3_spp/build_utils/img_utils.py` - source, Python (2247 bytes)
- `pytorch_object_detection/yolov3_spp/build_utils/layers.py` - source, Python (5576 bytes)
- `pytorch_object_detection/yolov3_spp/build_utils/parse_config.py` - source, Python (3181 bytes)
- `pytorch_object_detection/yolov3_spp/build_utils/torch_utils.py` - source, Python (4471 bytes)
- `pytorch_object_detection/yolov3_spp/build_utils/utils.py` - source, Python (20106 bytes)
- `pytorch_object_detection/yolov3_spp/calculate_dataset.py` - source, Python (3725 bytes)
- `pytorch_object_detection/yolov3_spp/cfg/hyp.yaml` - config (868 bytes)
- `pytorch_object_detection/yolov3_spp/cfg/yolov3-spp.cfg` - config (8733 bytes)
- `pytorch_object_detection/yolov3_spp/data/pascal_voc_classes.json` - config (348 bytes)
- `pytorch_object_detection/yolov3_spp/draw_box_utils.py` - source, Python (6045 bytes)
- `pytorch_object_detection/yolov3_spp/export_onnx.py` - source, Python (3690 bytes)
- `pytorch_object_detection/yolov3_spp/load_onnx_test.py` - test, Python (9982 bytes)
- `pytorch_object_detection/yolov3_spp/models.py` - source, Python (12977 bytes)
- `pytorch_object_detection/yolov3_spp/predict_test.py` - test, Python (3399 bytes)
- `pytorch_object_detection/yolov3_spp/requirements.txt` - manifest (127 bytes)
- `pytorch_object_detection/yolov3_spp/results20210515-152935.txt` - docs (3602 bytes)
- `pytorch_object_detection/yolov3_spp/train.py` - source, Python (14335 bytes)
- `pytorch_object_detection/yolov3_spp/train_multi_GPU.py` - source, Python (15907 bytes)
- `pytorch_object_detection/yolov3_spp/train_utils/__init__.py` - source, Python (170 bytes)
- `pytorch_object_detection/yolov3_spp/train_utils/coco_eval.py` - source, Python (11987 bytes)
- `pytorch_object_detection/yolov3_spp/train_utils/coco_utils.py` - source, Python (2026 bytes)
- `pytorch_object_detection/yolov3_spp/train_utils/distributed_utils.py` - source, Python (10986 bytes)
- `pytorch_object_detection/yolov3_spp/train_utils/group_by_aspect_ratio.py` - source, Python (7533 bytes)
- `pytorch_object_detection/yolov3_spp/train_utils/train_eval_utils.py` - source, Python (7215 bytes)
- `pytorch_object_detection/yolov3_spp/trans_voc2yolo.py` - source, Python (6882 bytes)
- `pytorch_object_detection/yolov3_spp/validation.py` - source, Python (8835 bytes)

### `pytorch_segmentation`

- `pytorch_segmentation/deeplab_v3/README.md` - docs (3436 bytes)
- `pytorch_segmentation/deeplab_v3/get_palette.py` - source, Python (425 bytes)
- `pytorch_segmentation/deeplab_v3/my_dataset.py` - source, Python (2334 bytes)
- `pytorch_segmentation/deeplab_v3/palette.json` - config (5522 bytes)
- `pytorch_segmentation/deeplab_v3/pascal_voc_classes.json` - config (348 bytes)
- `pytorch_segmentation/deeplab_v3/predict.py` - source, Python (2592 bytes)
- `pytorch_segmentation/deeplab_v3/requirements.txt` - manifest (55 bytes)
- `pytorch_segmentation/deeplab_v3/results20211027-104607.txt` - docs (2220 bytes)
- `pytorch_segmentation/deeplab_v3/src/__init__.py` - source, Python (98 bytes)
- `pytorch_segmentation/deeplab_v3/src/deeplabv3_model.py` - source, Python (10399 bytes)
- `pytorch_segmentation/deeplab_v3/src/mobilenet_backbone.py` - source, Python (13419 bytes)
- `pytorch_segmentation/deeplab_v3/src/resnet_backbone.py` - source, Python (7204 bytes)
- `pytorch_segmentation/deeplab_v3/train.py` - source, Python (8610 bytes)
- `pytorch_segmentation/deeplab_v3/train_multi_GPU.py` - source, Python (11349 bytes)
- `pytorch_segmentation/deeplab_v3/train_utils/__init__.py` - source, Python (151 bytes)
- `pytorch_segmentation/deeplab_v3/train_utils/distributed_utils.py` - source, Python (8837 bytes)
- `pytorch_segmentation/deeplab_v3/train_utils/train_and_eval.py` - source, Python (3085 bytes)
- `pytorch_segmentation/deeplab_v3/transforms.py` - source, Python (2880 bytes)
- `pytorch_segmentation/deeplab_v3/validation.py` - source, Python (2406 bytes)
- `pytorch_segmentation/fcn/README.md` - docs (3298 bytes)
- `pytorch_segmentation/fcn/get_palette.py` - source, Python (425 bytes)
- `pytorch_segmentation/fcn/my_dataset.py` - source, Python (2392 bytes)
- `pytorch_segmentation/fcn/palette.json` - config (5522 bytes)
- `pytorch_segmentation/fcn/pascal_voc_classes.json` - config (348 bytes)
- `pytorch_segmentation/fcn/predict.py` - source, Python (2580 bytes)
- `pytorch_segmentation/fcn/requirements.txt` - manifest (55 bytes)
- `pytorch_segmentation/fcn/results20210918-122740.txt` - docs (4470 bytes)
- `pytorch_segmentation/fcn/src/__init__.py` - source, Python (51 bytes)
- `pytorch_segmentation/fcn/src/backbone.py` - source, Python (7204 bytes)
- `pytorch_segmentation/fcn/src/fcn_model.py` - source, Python (6467 bytes)
- `pytorch_segmentation/fcn/train.py` - source, Python (8268 bytes)
- `pytorch_segmentation/fcn/train_multi_GPU.py` - source, Python (11331 bytes)
- `pytorch_segmentation/fcn/train_utils/__init__.py` - source, Python (151 bytes)
- `pytorch_segmentation/fcn/train_utils/distributed_utils.py` - source, Python (8837 bytes)
- `pytorch_segmentation/fcn/train_utils/train_and_eval.py` - source, Python (3085 bytes)
- `pytorch_segmentation/fcn/transforms.py` - source, Python (2880 bytes)
- `pytorch_segmentation/fcn/validation.py` - source, Python (2468 bytes)
- `pytorch_segmentation/lraspp/README.md` - docs (3265 bytes)
- `pytorch_segmentation/lraspp/get_palette.py` - source, Python (425 bytes)
- `pytorch_segmentation/lraspp/my_dataset.py` - source, Python (2334 bytes)
- `pytorch_segmentation/lraspp/palette.json` - config (5522 bytes)
- `pytorch_segmentation/lraspp/pascal_voc_classes.json` - config (348 bytes)
- `pytorch_segmentation/lraspp/predict.py` - source, Python (2399 bytes)
- `pytorch_segmentation/lraspp/requirements.txt` - manifest (55 bytes)
- `pytorch_segmentation/lraspp/results20211028-105233.txt` - docs (2220 bytes)
- `pytorch_segmentation/lraspp/src/__init__.py` - source, Python (51 bytes)
- `pytorch_segmentation/lraspp/src/lraspp_model.py` - source, Python (6343 bytes)
- `pytorch_segmentation/lraspp/src/mobilenet_backbone.py` - source, Python (13419 bytes)
- `pytorch_segmentation/lraspp/train.py` - source, Python (8048 bytes)
- `pytorch_segmentation/lraspp/train_multi_GPU.py` - source, Python (11096 bytes)
- `pytorch_segmentation/lraspp/train_utils/__init__.py` - source, Python (151 bytes)
- `pytorch_segmentation/lraspp/train_utils/distributed_utils.py` - source, Python (8837 bytes)
- `pytorch_segmentation/lraspp/train_utils/train_and_eval.py` - source, Python (3085 bytes)
- `pytorch_segmentation/lraspp/transforms.py` - source, Python (2880 bytes)
- `pytorch_segmentation/lraspp/validation.py` - source, Python (2321 bytes)
- `pytorch_segmentation/u2net/README.md` - docs (4078 bytes)
- `pytorch_segmentation/u2net/convert_weight.py` - source, Python (4732 bytes)
- `pytorch_segmentation/u2net/my_dataset.py` - source, Python (3004 bytes)
- `pytorch_segmentation/u2net/predict.py` - source, Python (2123 bytes)
- `pytorch_segmentation/u2net/requirements.txt` - manifest (72 bytes)
- `pytorch_segmentation/u2net/results20220723-123632.txt` - docs (2579 bytes)
- `pytorch_segmentation/u2net/src/__init__.py` - source, Python (42 bytes)
- `pytorch_segmentation/u2net/src/model.py` - source, Python (8599 bytes)
- `pytorch_segmentation/u2net/train.py` - source, Python (6785 bytes)
- `pytorch_segmentation/u2net/train_multi_GPU.py` - source, Python (9734 bytes)
- `pytorch_segmentation/u2net/train_utils/__init__.py` - source, Python (170 bytes)
- `pytorch_segmentation/u2net/train_utils/distributed_utils.py` - source, Python (11093 bytes)
- `pytorch_segmentation/u2net/train_utils/train_and_eval.py` - source, Python (3918 bytes)
- `pytorch_segmentation/u2net/transforms.py` - source, Python (2312 bytes)
- `pytorch_segmentation/u2net/validation.py` - source, Python (2158 bytes)
- `pytorch_segmentation/unet/README.md` - docs (2682 bytes)
- `pytorch_segmentation/unet/compute_mean_std.py` - source, Python (1071 bytes)
- `pytorch_segmentation/unet/my_dataset.py` - source, Python (2524 bytes)
- `pytorch_segmentation/unet/predict.py` - source, Python (2424 bytes)
- `pytorch_segmentation/unet/requirements.txt` - manifest (55 bytes)
- `pytorch_segmentation/unet/results20220109-165837.txt` - docs (33084 bytes)
- `pytorch_segmentation/unet/src/__init__.py` - source, Python (96 bytes)
- `pytorch_segmentation/unet/src/mobilenet_unet.py` - source, Python (4247 bytes)
- `pytorch_segmentation/unet/src/unet.py` - source, Python (3371 bytes)
- `pytorch_segmentation/unet/src/vgg_unet.py` - source, Python (4009 bytes)
- `pytorch_segmentation/unet/train.py` - source, Python (7721 bytes)
- `pytorch_segmentation/unet/train_multi_GPU.py` - source, Python (10872 bytes)
- `pytorch_segmentation/unet/train_utils/__init__.py` - source, Python (151 bytes)
- `pytorch_segmentation/unet/train_utils/dice_coefficient_loss.py` - source, Python (2081 bytes)
- `pytorch_segmentation/unet/train_utils/distributed_utils.py` - source, Python (10483 bytes)
- `pytorch_segmentation/unet/train_utils/train_and_eval.py` - source, Python (3959 bytes)
- `pytorch_segmentation/unet/transforms.py` - source, Python (3172 bytes)

### `tensorflow_classification`

- `tensorflow_classification/ConfusionMatrix/class_indices.json` - config (102 bytes)
- `tensorflow_classification/ConfusionMatrix/main.py` - source, Python (5033 bytes)
- `tensorflow_classification/ConfusionMatrix/model.py` - source, Python (3964 bytes)
- `tensorflow_classification/ConvNeXt/model.py` - source, Python (8201 bytes)
- `tensorflow_classification/ConvNeXt/predict.py` - source, Python (1777 bytes)
- `tensorflow_classification/ConvNeXt/train.py` - source, Python (5355 bytes)
- `tensorflow_classification/ConvNeXt/trans_weights.py` - source, Python (5777 bytes)
- `tensorflow_classification/ConvNeXt/utils.py` - source, Python (7872 bytes)
- `tensorflow_classification/README.md` - docs (513 bytes)
- `tensorflow_classification/Test11_efficientnetV2/model.py` - source, Python (14656 bytes)
- `tensorflow_classification/Test11_efficientnetV2/predict.py` - source, Python (1820 bytes)
- `tensorflow_classification/Test11_efficientnetV2/train.py` - source, Python (5957 bytes)
- `tensorflow_classification/Test11_efficientnetV2/trans_weights.py` - source, Python (1436 bytes)
- `tensorflow_classification/Test11_efficientnetV2/utils.py` - source, Python (6837 bytes)
- `tensorflow_classification/Test1_official_demo/model.py` - source, Python (644 bytes)
- `tensorflow_classification/Test1_official_demo/train.py` - source, Python (2869 bytes)
- `tensorflow_classification/Test2_alexnet/class_indices.json` - config (102 bytes)
- `tensorflow_classification/Test2_alexnet/fine_train_alexnet.py` - source, Python (6700 bytes)
- `tensorflow_classification/Test2_alexnet/model.py` - source, Python (3535 bytes)
- `tensorflow_classification/Test2_alexnet/predict.py` - source, Python (1560 bytes)
- `tensorflow_classification/Test2_alexnet/read_pth.py` - source, Python (2964 bytes)
- `tensorflow_classification/Test2_alexnet/train.py` - source, Python (7770 bytes)
- `tensorflow_classification/Test2_alexnet/trainGPU.py` - source, Python (7135 bytes)
- `tensorflow_classification/Test3_vgg/class_indices.json` - config (102 bytes)
- `tensorflow_classification/Test3_vgg/fine_train_vgg16.py` - source, Python (4184 bytes)
- `tensorflow_classification/Test3_vgg/model.py` - source, Python (2320 bytes)
- `tensorflow_classification/Test3_vgg/predict.py` - source, Python (1614 bytes)
- `tensorflow_classification/Test3_vgg/read_ckpt.py` - source, Python (3398 bytes)
- `tensorflow_classification/Test3_vgg/train.py` - source, Python (4299 bytes)
- `tensorflow_classification/Test3_vgg/trainGPU.py` - source, Python (6962 bytes)
- `tensorflow_classification/Test4_goolenet/class_indices.json` - config (102 bytes)
- `tensorflow_classification/Test4_goolenet/model.py` - source, Python (4840 bytes)
- `tensorflow_classification/Test4_goolenet/model_add_bn.py` - source, Python (6139 bytes)
- `tensorflow_classification/Test4_goolenet/predict.py` - source, Python (1671 bytes)
- `tensorflow_classification/Test4_goolenet/read_pth.py` - source, Python (2921 bytes)
- `tensorflow_classification/Test4_goolenet/train.py` - source, Python (5996 bytes)
- `tensorflow_classification/Test4_goolenet/trainGPU.py` - source, Python (6669 bytes)
- `tensorflow_classification/Test4_goolenet/train_add_bn.py` - source, Python (6286 bytes)
- `tensorflow_classification/Test5_resnet/batch_predict.py` - source, Python (2898 bytes)
- `tensorflow_classification/Test5_resnet/class_indices.json` - config (102 bytes)
- `tensorflow_classification/Test5_resnet/model.py` - source, Python (5773 bytes)
- `tensorflow_classification/Test5_resnet/predict.py` - source, Python (2260 bytes)
- `tensorflow_classification/Test5_resnet/read_ckpt.py` - source, Python (1858 bytes)
- `tensorflow_classification/Test5_resnet/read_h5.py` - source, Python (315 bytes)
- `tensorflow_classification/Test5_resnet/subclassed_model.py` - source, Python (6161 bytes)
- `tensorflow_classification/Test5_resnet/train.py` - source, Python (6677 bytes)
- `tensorflow_classification/Test5_resnet/trainGPU.py` - source, Python (7409 bytes)
- `tensorflow_classification/Test6_mobilenet/model_v2.py` - source, Python (4264 bytes)
- `tensorflow_classification/Test6_mobilenet/model_v3.py` - source, Python (10578 bytes)
- `tensorflow_classification/Test6_mobilenet/predict.py` - source, Python (1964 bytes)
- `tensorflow_classification/Test6_mobilenet/read_ckpt.py` - source, Python (2623 bytes)
- `tensorflow_classification/Test6_mobilenet/trainGPU_mobilenet_v2.py` - source, Python (6767 bytes)
- `tensorflow_classification/Test6_mobilenet/train_mobilenet_v2.py` - source, Python (6378 bytes)
- `tensorflow_classification/Test6_mobilenet/train_mobilenet_v3.py` - source, Python (4186 bytes)
- `tensorflow_classification/Test6_mobilenet/trans_v3_weights.py` - source, Python (1633 bytes)
- `tensorflow_classification/Test6_mobilenet/utils.py` - source, Python (6397 bytes)
- `tensorflow_classification/Test7_shuffleNet/model.py` - source, Python (7003 bytes)
- `tensorflow_classification/Test7_shuffleNet/predict.py` - source, Python (1711 bytes)
- `tensorflow_classification/Test7_shuffleNet/train.py` - source, Python (5141 bytes)
- `tensorflow_classification/Test7_shuffleNet/trans_weights.py` - source, Python (4938 bytes)
- `tensorflow_classification/Test7_shuffleNet/utils.py` - source, Python (6465 bytes)
- `tensorflow_classification/Test9_efficientNet/model.py` - source, Python (14498 bytes)
- `tensorflow_classification/Test9_efficientNet/predict.py` - source, Python (1843 bytes)
- `tensorflow_classification/Test9_efficientNet/train.py` - source, Python (5613 bytes)
- `tensorflow_classification/Test9_efficientNet/utils.py` - source, Python (6065 bytes)
- `tensorflow_classification/analyze_weights_featuremap/alexnet_model.py` - source, Python (3770 bytes)
- `tensorflow_classification/analyze_weights_featuremap/analyze_feature_map.py` - source, Python (1938 bytes)
- `tensorflow_classification/analyze_weights_featuremap/analyze_kernel_weight.py` - source, Python (1271 bytes)
- `tensorflow_classification/custom_dataset/train_fit.py` - source, Python (2547 bytes)
- `tensorflow_classification/custom_dataset/utils.py` - source, Python (6325 bytes)
- `tensorflow_classification/swin_transformer/model.py` - source, Python (27396 bytes)
- `tensorflow_classification/swin_transformer/predict.py` - source, Python (1803 bytes)
- `tensorflow_classification/swin_transformer/train.py` - source, Python (5483 bytes)
- `tensorflow_classification/swin_transformer/trans_weights.py` - source, Python (5793 bytes)
- `tensorflow_classification/swin_transformer/utils.py` - source, Python (6907 bytes)
- `tensorflow_classification/tensorboard_test/train_fit.py` - source, Python (4593 bytes)
- `tensorflow_classification/tensorboard_test/train_not_fit.py` - source, Python (6696 bytes)
- `tensorflow_classification/vision_transformer/predict.py` - source, Python (1776 bytes)
- `tensorflow_classification/vision_transformer/train.py` - source, Python (5851 bytes)
- `tensorflow_classification/vision_transformer/trans_weights.py` - source, Python (4012 bytes)
- `tensorflow_classification/vision_transformer/utils.py` - source, Python (6835 bytes)
- `tensorflow_classification/vision_transformer/vit_model.py` - source, Python (13360 bytes)

## 7. Key dependencies and integrations

| Name | Category | Status | Confidence | Evidence |
| --- | --- | --- | --- | --- |
| Flask | framework | Observed | 0.90 | [deploying_service/deploying_pytorch/pytorch_flask_service/main.py:7](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/pytorch_flask_service/main.py#L7); [deploying_service/deploying_pytorch/pytorch_flask_service/requirements.txt:1](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/pytorch_flask_service/requirements.txt#L1) |
| NumPy | library | Observed | 0.95 | [deploying_service/deploying_pytorch/convert_onnx_cls/main.py:7](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_onnx_cls/main.py#L7); [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_fps.py:2](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_fps.py#L2); [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_onnx_and_ir.py:1](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_onnx_and_ir.py#L1); [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/convert_pytorch2onnx.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/convert_pytorch2onnx.py#L5) |
| pandas | library | Observed | 0.95 | [pytorch_classification/mini_imagenet/my_dataset.py:4](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/mini_imagenet/my_dataset.py#L4); [pytorch_classification/mini_imagenet/restructure_csv.py:4](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/mini_imagenet/restructure_csv.py#L4) |
| requests | library | Observed | 0.90 | [pytorch_classification/Test10_regnet/pretrain_weights.py:1](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/Test10_regnet/pretrain_weights.py#L1) |

## 8. Data and state

- Data component `data_layer` (Observed): Groups 36 file(s) under data layer (observed from repository paths and static analysis). Observed top-level classes: AlexNet, AlexNet_v2, BasicBlock, BasicConv2d, BasicLayer, Block. Observed top-level functions: AlexNet_v1, GoogLeNet, MobileNetV2, VGG, _make_divisible, _make_layer.

## 9. Configuration and deployment clues

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

## 10. Design observations

- An entry/API layer is separated from other code (Inferred from paths and decorators).
- Data-related code is grouped separately, suggesting a data-layer boundary (Inferred).
- Tests are present alongside source code (Observed from test file paths).
- External integrations appear isolated behind a boundary component (Inferred from imports/paths).

These observations are interpretations (**Inferred**) of the observed structure, not guarantees about runtime design.

## 11. Limitations and unknowns

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

## 12. Source references

- [data_set/split_data.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/data_set/split_data.py#L6)
- [data_set/split_data.py:66](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/data_set/split_data.py#L66)
- [deploying_service/deploying_pytorch/convert_onnx_cls/class_indices.json](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_onnx_cls/class_indices.json)
- [deploying_service/deploying_pytorch/convert_onnx_cls/main.py:7](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_onnx_cls/main.py#L7)
- [deploying_service/deploying_pytorch/convert_onnx_cls/main.py:13](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_onnx_cls/main.py#L13)
- [deploying_service/deploying_pytorch/convert_onnx_cls/main.py:78](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_onnx_cls/main.py#L78)
- [deploying_service/deploying_pytorch/convert_onnx_cls/model.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_onnx_cls/model.py#L5)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_fps.py:2](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_fps.py#L2)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_fps.py:10](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_fps.py#L10)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_fps.py:125](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_fps.py#L125)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_onnx_and_ir.py:1](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_onnx_and_ir.py#L1)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_onnx_and_ir.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_onnx_and_ir.py#L6)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_onnx_and_ir.py:64](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/compare_onnx_and_ir.py#L64)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/convert_pytorch2onnx.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/convert_pytorch2onnx.py#L5)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/convert_pytorch2onnx.py:11](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/convert_pytorch2onnx.py#L11)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/convert_pytorch2onnx.py:55](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/convert_pytorch2onnx.py#L55)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/model.py:9](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/model.py#L9)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/quantization_int8.py:9](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/quantization_int8.py#L9)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/quantization_int8.py:83](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/quantization_int8.py#L83)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/requirements.txt](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/requirements.txt)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/utils.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/utils.py#L6)
- [deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/utils.py:11](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_resnet34/utils.py#L11)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_fps.py:2](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_fps.py#L2)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_fps.py:9](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_fps.py#L9)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_fps.py:120](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_fps.py#L120)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_onnx_and_ir.py:1](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_onnx_and_ir.py#L1)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_onnx_and_ir.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_onnx_and_ir.py#L6)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_onnx_and_ir.py:60](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/compare_onnx_and_ir.py#L60)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/draw_box_utils.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/draw_box_utils.py#L5)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/draw_box_utils.py:34](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/draw_box_utils.py#L34)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/evaluation.py:43](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/evaluation.py#L43)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/predict.py:49](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/predict.py#L49)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/quantization_int8.py:101](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/quantization_int8.py#L101)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/requirements.txt](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/requirements.txt)
- [deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/utils.py:27](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_openvino/convert_yolov5/utils.py#L27)
- [deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/my_dataset.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/my_dataset.py#L6)
- [deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/utils.py:11](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/convert_tensorrt/convert_resnet34/utils.py#L11)
- [deploying_service/deploying_pytorch/pytorch_flask_service/class_indices.json](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/pytorch_flask_service/class_indices.json)
- [deploying_service/deploying_pytorch/pytorch_flask_service/main.py:7](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/pytorch_flask_service/main.py#L7)
- [deploying_service/deploying_pytorch/pytorch_flask_service/model.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/pytorch_flask_service/model.py#L5)
- [deploying_service/deploying_pytorch/pytorch_flask_service/requirements.txt](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/pytorch_flask_service/requirements.txt)
- [deploying_service/deploying_pytorch/pytorch_flask_service/requirements.txt:1](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/deploying_pytorch/pytorch_flask_service/requirements.txt#L1)
- [deploying_service/pruning_model_pytorch/class_indices.json](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/pruning_model_pytorch/class_indices.json)
- [deploying_service/pruning_model_pytorch/model.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/pruning_model_pytorch/model.py#L5)
- [deploying_service/pruning_model_pytorch/predict.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/pruning_model_pytorch/predict.py)
- [deploying_service/pruning_model_pytorch/train.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/deploying_service/pruning_model_pytorch/train.py)
- [others_project/kmeans_anchors/read_voc.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/kmeans_anchors/read_voc.py#L6)
- [others_project/kmeans_anchors/yolo_kmeans.py:4](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/kmeans_anchors/yolo_kmeans.py#L4)
- [others_project/openvinotest/openvino_cls_test/class_indices.json](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/openvinotest/openvino_cls_test/class_indices.json)
- [others_project/openvinotest/openvino_cls_test/create_imagenet_annotation.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/openvinotest/openvino_cls_test/create_imagenet_annotation.py)
- [others_project/openvinotest/openvino_cls_test/model.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/openvinotest/openvino_cls_test/model.py#L5)
- [others_project/openvinotest/openvino_cls_test/speed_test.py:15](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/openvinotest/openvino_cls_test/speed_test.py#L15)
- [others_project/readPbFile/readPb.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/readPbFile/readPb.py)
- [others_project/readPbFile/using_function.py:37](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/readPbFile/using_function.py#L37)
- [others_project/textcnnKeras/dataGenerator.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/textcnnKeras/dataGenerator.py#L6)
- [others_project/textcnnKeras/models.py:4](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/textcnnKeras/models.py#L4)
- [others_project/trans_widerface_to_xml/create_xml.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/others_project/trans_widerface_to_xml/create_xml.py#L6)
- [pytorch_classification/ConfusionMatrix/class_indices.json](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/ConfusionMatrix/class_indices.json)
- [pytorch_classification/ConfusionMatrix/model.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/ConfusionMatrix/model.py#L5)
- [pytorch_classification/ConvNeXt/model.py:11](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/ConvNeXt/model.py#L11)
- [pytorch_classification/ConvNeXt/my_dataset.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/ConvNeXt/my_dataset.py#L6)
- [pytorch_classification/ConvNeXt/utils.py:14](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/ConvNeXt/utils.py#L14)
- [pytorch_classification/MobileViT/model_config.py:1](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/MobileViT/model_config.py#L1)
- [pytorch_classification/MobileViT/my_dataset.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/MobileViT/my_dataset.py#L6)
- [pytorch_classification/MobileViT/transformer.py:8](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/MobileViT/transformer.py#L8)
- [pytorch_classification/MobileViT/unfold_test.py:14](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/MobileViT/unfold_test.py#L14)
- [pytorch_classification/MobileViT/utils.py:13](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/MobileViT/utils.py#L13)
- [pytorch_classification/Test10_regnet/my_dataset.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/Test10_regnet/my_dataset.py#L6)
- [pytorch_classification/Test10_regnet/pretrain_weights.py:1](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/Test10_regnet/pretrain_weights.py#L1)
- [pytorch_classification/Test10_regnet/utils.py:13](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/Test10_regnet/utils.py#L13)
- [pytorch_classification/mini_imagenet/my_dataset.py:4](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/mini_imagenet/my_dataset.py#L4)
- [pytorch_classification/mini_imagenet/restructure_csv.py:4](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_classification/mini_imagenet/restructure_csv.py#L4)
- [pytorch_keypoint/DeepPose/train_utils/distributed_utils.py:7](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/DeepPose/train_utils/distributed_utils.py#L7)
- [pytorch_keypoint/DeepPose/train_utils/losses.py:8](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/DeepPose/train_utils/losses.py#L8)
- [pytorch_keypoint/DeepPose/train_utils/train_eval_utils.py:15](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/DeepPose/train_utils/train_eval_utils.py#L15)
- [pytorch_keypoint/DeepPose/transforms.py:12](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/DeepPose/transforms.py#L12)
- [pytorch_keypoint/DeepPose/utils.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/DeepPose/utils.py#L5)
- [pytorch_keypoint/DeepPose/wflw_horizontal_flip_indices.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/DeepPose/wflw_horizontal_flip_indices.py)
- [pytorch_keypoint/HRNet/draw_utils.py:29](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/HRNet/draw_utils.py#L29)
- [pytorch_keypoint/HRNet/model/__init__.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_keypoint/HRNet/model/__init__.py)
- [pytorch_object_detection/faster_rcnn/backbone/__init__.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/backbone/__init__.py)
- [pytorch_object_detection/faster_rcnn/backbone/feature_pyramid_network.py:11](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/backbone/feature_pyramid_network.py#L11)
- [pytorch_object_detection/faster_rcnn/backbone/mobilenetv2_model.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/backbone/mobilenetv2_model.py#L6)
- [pytorch_object_detection/faster_rcnn/backbone/resnet50_fpn_model.py:10](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/backbone/resnet50_fpn_model.py#L10)
- [pytorch_object_detection/faster_rcnn/backbone/vgg_model.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/backbone/vgg_model.py#L5)
- [pytorch_object_detection/faster_rcnn/draw_box_utils.py:34](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/draw_box_utils.py#L34)
- [pytorch_object_detection/faster_rcnn/my_dataset.py:10](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/my_dataset.py#L10)
- [pytorch_object_detection/faster_rcnn/network_files/__init__.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/faster_rcnn/network_files/__init__.py)
- [pytorch_object_detection/ssd/predict_test.py:14](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/ssd/predict_test.py#L14)
- [pytorch_object_detection/yolov3_spp/load_onnx_test.py:10](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/yolov3_spp/load_onnx_test.py#L10)
- [pytorch_object_detection/yolov3_spp/predict_test.py:16](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_object_detection/yolov3_spp/predict_test.py#L16)
- [pytorch_segmentation/deeplab_v3/get_palette.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/get_palette.py)
- [pytorch_segmentation/deeplab_v3/my_dataset.py:7](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/my_dataset.py#L7)
- [pytorch_segmentation/deeplab_v3/src/__init__.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/src/__init__.py)
- [pytorch_segmentation/deeplab_v3/src/deeplabv3_model.py:12](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/src/deeplabv3_model.py#L12)
- [pytorch_segmentation/deeplab_v3/src/mobilenet_backbone.py:9](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/src/mobilenet_backbone.py#L9)
- [pytorch_segmentation/deeplab_v3/src/resnet_backbone.py:5](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/src/resnet_backbone.py#L5)
- [pytorch_segmentation/deeplab_v3/train_utils/__init__.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/train_utils/__init__.py)
- [pytorch_segmentation/deeplab_v3/train_utils/distributed_utils.py:11](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/deeplab_v3/train_utils/distributed_utils.py#L11)
- [pytorch_segmentation/u2net/src/model.py:225](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/pytorch_segmentation/u2net/src/model.py#L225)
- [tensorflow_classification/ConvNeXt/utils.py:11](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/ConvNeXt/utils.py#L11)
- [tensorflow_classification/Test11_efficientnetV2/utils.py:9](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/Test11_efficientnetV2/utils.py#L9)
- [tensorflow_classification/Test2_alexnet/read_pth.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/Test2_alexnet/read_pth.py#L6)
- [tensorflow_classification/Test3_vgg/read_ckpt.py:4](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/Test3_vgg/read_ckpt.py#L4)
- [tensorflow_classification/Test4_goolenet/model_add_bn.py:4](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/Test4_goolenet/model_add_bn.py#L4)
- [tensorflow_classification/Test4_goolenet/read_pth.py:6](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/Test4_goolenet/read_pth.py#L6)
- [tensorflow_classification/Test5_resnet/read_h5.py](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/Test5_resnet/read_h5.py)
- [tensorflow_classification/Test5_resnet/subclassed_model.py:4](https://github.com/WZMIAOMIAO/deep-learning-for-image-processing/blob/1ec3fe6f374fc9969973a61f819de25658595afa/tensorflow_classification/Test5_resnet/subclassed_model.py#L4)
