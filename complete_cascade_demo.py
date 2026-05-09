# Complete Cascade ALPR Demo
from ultralytics import YOLO
import cv2
import numpy as np

vehicle_model = YOLO('runs/detect/train4/weights/best.pt')
plate_model = YOLO('runs/detect/Plate_Detection/train/weights/best.pt')

img_path = 'input_data/download.jpg'
img = cv2.imread(img_path)
h, w = img.shape[:2]

v_results = vehicle_model(img, conf=0.25, verbose=False)
img_out = img.copy()

for r in v_results:
  if r.boxes is not None:
    boxes = r.boxes.xyxy.cpu().numpy()
    for box in boxes:
      x1, y1
