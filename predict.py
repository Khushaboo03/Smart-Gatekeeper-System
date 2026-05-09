from ultralytics import YOLO
import os
import shutil
import cv2
import easyocr

# ================== PATHS ==================
VEHICLE_MODEL_PATH = "yolov8n.pt"   # Pretrained vehicle model
PLATE_MODEL_PATH = "models/plate_model.pt"  # Your plate model
SOURCE_PATH = "input_data"

PROJECT_PATH = r"F:\Vehicle_Type_Classification_Project(BASIC MODEL)\runs\detect"
OUTPUT_NAME = "predict"
OUTPUT_DIR = os.path.join(PROJECT_PATH, OUTPUT_NAME)

# ================== VEHICLE CLASSES ==================
# COCO classes: car=2, bike=3, bus=5, truck=7
VEHICLE_CLASSES = [2, 3, 5, 7]

# ================== CHECK FILES ==================
if not os.path.exists(PLATE_MODEL_PATH):
    print("❌ plate_model.pt not found")
    exit()

if os.path.getsize(PLATE_MODEL_PATH) < 100000:
    print("❌ plate_model.pt is invalid or corrupted")
    exit()

# ================== CLEAN OUTPUT ==================
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ================== LOAD MODELS ==================
vehicle_model = YOLO(VEHICLE_MODEL_PATH)
print("✅ Vehicle model loaded")

plate_model = YOLO(PLATE_MODEL_PATH)
print("✅ Plate model loaded")

# ================== OCR ==================
reader = easyocr.Reader(['en'], gpu=False)

# ================== PROCESS ==================
for file in os.listdir(SOURCE_PATH):

    file_path = os.path.join(SOURCE_PATH, file)
    img = cv2.imread(file_path)

    if img is None:
        continue

    print(f"\n📸 Processing: {file}")

    # 🔴 VEHICLE DETECTION
    results = vehicle_model.predict(img, imgsz=640, conf=0.10, verbose=False)

    for r in results:
        if r.boxes is None:
            continue

        print(f"👉 Total detections: {len(r.boxes)}")

        for box, cls in zip(r.boxes.xyxy, r.boxes.cls):

            # 🚫 Filter only vehicles
            if int(cls) not in VEHICLE_CLASSES:
                continue

            x1, y1, x2, y2 = map(int, box)

            # Boundary fix
            x1 = max(0, x1)
            y1 = max(0, y1)
            x2 = min(img.shape[1], x2)
            y2 = min(img.shape[0], y2)

            # 🔴 Draw vehicle box
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

            vehicle_crop = img[y1:y2, x1:x2]

            if vehicle_crop.size == 0:
                continue

            # 🟢 PLATE DETECTION
            plate_results = plate_model.predict(vehicle_crop, conf=0.15, verbose=False)

            for p in plate_results:
                if p.boxes is None:
                    continue

                for pb in p.boxes.xyxy:
                    px1, py1, px2, py2 = map(int, pb)

                    # Convert to original image
                    px1 += x1
                    py1 += y1
                    px2 += x1
                    py2 += y1

                    # Boundary fix
                    px1 = max(0, px1)
                    py1 = max(0, py1)
                    px2 = min(img.shape[1], px2)
                    py2 = min(img.shape[0], py2)

                    plate_crop = img[py1:py2, px1:px2]

                    if plate_crop.size == 0:
                        continue

                    # ================== OCR ==================
                    plate_text = ""
                    try:
                        gray = cv2.cvtColor(plate_crop, cv2.COLOR_BGR2GRAY)
                        gray = cv2.resize(gray, None, fx=2, fy=2)

                        result = reader.readtext(gray, detail=0)
                        plate_text = " ".join(result)

                        # Clean text
                        plate_text = plate_text.replace(" ", "").upper()

                    except:
                        pass

                    # 🟢 Draw plate box
                    cv2.rectangle(img, (px1, py1), (px2, py2), (0, 255, 0), 2)

                    # Draw text
                    if plate_text:
                        cv2.putText(
                            img,
                            plate_text,
                            (px1, py1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0, 255, 0),
                            2
                        )

    # ================== SAVE ==================
    output_path = os.path.join(OUTPUT_DIR, file)
    cv2.imwrite(output_path, img)

# ================== DONE ==================
print("\n✅ Prediction completed successfully")
print(f"📁 Results saved in: {OUTPUT_DIR}")