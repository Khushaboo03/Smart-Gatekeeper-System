from ultralytics import YOLO

# Load pretrained YOLOv8 nano model
model = YOLO("yolov8n.pt")

# Train on plate dataset
model.train(
    project="Plate_Detection",
    data="Plate_Detection/plate_data.yaml",
epochs=5,
    imgsz=640,
    batch=8
)
