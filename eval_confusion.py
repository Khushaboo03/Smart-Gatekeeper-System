from __future__ import annotations

import numpy as np
from ultralytics import YOLO


def main() -> None:
    model = YOLO("runs/detect/train4/weights/best.pt")
    r = model.val(
        data="dataset/data.yaml",
        split="val",
        imgsz=640,
        conf=0.25,
        iou=0.7,
        plots=True,
        save=False,
        verbose=False,
    )

    box = getattr(r, "box", None)
    mp = getattr(box, "mp", None) if box is not None else None
    mr = getattr(box, "mr", None) if box is not None else None
    map50 = getattr(box, "map50", None) if box is not None else None
    map5095 = getattr(box, "map", None) if box is not None else None

    print("METRICS")
    print("precision_mean", mp)
    print("recall_mean", mr)
    print("mAP50", map50)
    print("mAP50-95", map5095)

    cm_obj = getattr(r, "confusion_matrix", None)
    cm = getattr(cm_obj, "matrix", None) if cm_obj is not None else None
    if cm is None:
        raise RuntimeError("No confusion matrix found in results object")

    cm = np.asarray(cm)
    print("\nCLASSES")
    names = model.names
    class_names = [names[i] for i in range(len(names))]
    print(class_names)

    print("\nCONFUSION_MATRIX")
    print("shape", cm.shape)
    np.set_printoptions(suppress=True, linewidth=200)
    print(cm)


if __name__ == "__main__":
    main()

