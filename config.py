import os


class Config:
    device = os.environ.get("DEVICE", "cpu")
    device_index = os.environ.get("DEVICE_INDEX", 0)

    img_width = os.environ.get("IMG_WIDTH", 640)
    img_height = os.environ.get("IMG_HEIGHT", 480)

    use_agnostic_nms = True if os.environ.get("AGNOSTIC_NMS", False) == "True" else False
    IoU = os.environ.get("IOU", 0.75)

    use_half_precision = True if os.environ.get("USE_HALF", False) == "True" and device == "cuda" else False
    