from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import os

vehicle_model = YOLO('runs/detect/train4/weights/best.pt')
plate_model = YOLO('runs/detect/Plate_Detection/train/weights/best.pt')

for f in ['input_data/download.jpg']:
  img = cv2.imread(f)
  v_results = vehicle_model.predict(img, conf=0.25, verbose=False)
  for r in v_results:
    img_anno = r.orig_img.copy()
    if r.boxes:
      for box in r.boxes:
x1,y1,x2,y2 = map(int, box.xyxy[0].cpu().numpy())
        crop = img_anno[y1:y2, x1:x2]
        p_results = plate_model.predict(crop, verbose=False
