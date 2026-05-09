from ultralytics import YOLO

# Load YOUR trained model (not COCO)
model = YOLO("runs/detect/train4/weights/best.pt")

# Validate on your dataset
model.val(data="dataset/data.yaml")
