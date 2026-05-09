from ultralytics import YOLO

# Load trained model
model = YOLO("runs/detect/train4/weights/best.pt")

# Evaluate on test set
model.val(
    data="dataset/data.yaml",   #loads data as car,truck,auto
    split="test"    #use only on test unseen images
)
