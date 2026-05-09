from ultralytics import YOLO

# Load pretrained YOLOv8 nano model
model = YOLO("yolov8n.pt")

# Train on your custom dataset
model.train(
    data="dataset/data.yaml",
    epochs=50,
    imgsz=640,    #resize images to 640X640 pixels
    batch=8       #8 images processed at a time
)
#The runs/detect/train4 folder stores the trained model, performance graphs, evaluation results, 
# and visual outputs created automatically by YOLOv8 after training.