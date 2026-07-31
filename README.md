修改`config.py`和`config_positions.py`中的相关配置进行适配

`config.py`中包含运行设置，邮箱相关的信息一定要设置

`config_positions.py`中包含点击位置设置

RKNN 相关固件信息
```
I RKNN: [09:39:32.960] RKNN Runtime Information, librknnrt version: 2.3.0 (c949ad889d@2024-11-07T11:35:33)
I RKNN: [09:39:32.961] RKNN Driver Information, version: 0.9.8
I RKNN: [09:39:32.963] RKNN Model Information, version: 6, toolkit version: 2.3.2(compiler version: 2.3.2 (839b70f037@2025-04-03T10:34:04)), target: RKNPU v2, target platform: rk3588, framework name: ONNX, framework layout: NCHW, model inference type: static_shape
W RKNN: [09:39:32.990] query RKNN_QUERY_INPUT_DYNAMIC_RANGE error, rknn model is static shape type, please export rknn with dynamic_shapes
W Query dynamic range failed. Ret code: RKNN_ERR_MODEL_INVALID. (If it is a static shape RKNN model, please ignore the above warning message.)
```

运行`run.py`进行每日活动


# RKNN:

https://github.com/airockchip/rknn_model_zoo

https://github.com/airockchip/rknn-toolkit2

# Redroid:

https://github.com/CNflysky/redroid-rk3588

# Models and Converting:

https://github.com/minquejoe/Re1999-AutoDailyScript-Models