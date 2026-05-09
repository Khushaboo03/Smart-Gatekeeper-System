import torch
from ultralytics import YOLO
import cv2
import easyocr

# PyTorch compatibility:
# - torch>=2.6 uses add_safe_globals during safe weight loading
# - older torch versions do not have this API
from ultralytics.nn.tasks import DetectionModel
if hasattr(torch.serialization, "add_safe_globals"):
    torch.serialization.add_safe_globals([DetectionModel])

# ================== MODEL PATHS ==================
VEHICLE_MODEL_PATH = "runs/detect/train4/weights/best.pt"
PLATE_MODEL_PATH = "models/plate_model.pt"

# ================== LOAD MODELS ==================
vehicle_model = YOLO(VEHICLE_MODEL_PATH)
plate_model = YOLO(PLATE_MODEL_PATH)

# OCR Reader (CPU safe)
reader = easyocr.Reader(['en'], gpu=False)

# ================== DROIDCAM STREAM ==================
URL = "http://10.46.44.214:4747/video"
cap = cv2.VideoCapture(URL)

if not cap.isOpened():
    print("❌ Cannot open DroidCam stream")
    exit()

print("✅ Live stream started... Press 'Q' to exit")

# ================== MAIN LOOP ==================
while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Frame not received")
        break

    frame = cv2.resize(frame, (640, 480))

    # ================== VEHICLE DETECTION ==================
    vehicle_results = vehicle_model.predict(frame, conf=0.25, verbose=False)

    for v in vehicle_results:
        if v.boxes is None:
            continue

        for box in v.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box)

            # Boundary fix
            x1 = max(0, x1)
            y1 = max(0, y1)
            x2 = min(frame.shape[1], x2)
            y2 = min(frame.shape[0], y2)

            # 🔴 Vehicle box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

            vehicle_crop = frame[y1:y2, x1:x2]
            if vehicle_crop.size == 0:
                continue

            # ================== PLATE DETECTION ==================
            plate_results = plate_model.predict(vehicle_crop, conf=0.25, verbose=False)

            for p in plate_results:
                if p.boxes is None:
                    continue

                for pb in p.boxes.xyxy:
                    px1, py1, px2, py2 = map(int, pb)

                    # Convert to original frame
                    px1 += x1
                    py1 += y1
                    px2 += x1
                    py2 += y1

                    # Boundary fix
                    px1 = max(0, px1)
                    py1 = max(0, py1)
                    px2 = min(frame.shape[1], px2)
                    py2 = min(frame.shape[0], py2)

                    plate_crop = frame[py1:py2, px1:px2]
                    if plate_crop.size == 0:
                        continue

                    # ================== OCR ==================
                    plate_text = ""
                    try:
                        gray = cv2.cvtColor(plate_crop, cv2.COLOR_BGR2GRAY)
                        gray = cv2.resize(gray, None, fx=2, fy=2)

                        result = reader.readtext(gray, detail=0)
                        plate_text = " ".join(result).replace(" ", "").upper()
                    except:
                        pass

                    # 🟢 Plate box
                    cv2.rectangle(frame, (px1, py1), (px2, py2), (0, 255, 0), 2)

                    if plate_text:
                        cv2.putText(
                            frame,
                            plate_text,
                            (px1, py1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0, 255, 0),
                            2
                        )

    # ================== SHOW ==================
    cv2.imshow("Smart Gatekeeper - Live", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ================== CLEANUP ==================
cap.release()
cv2.destroyAllWindows()
print("✅ Live detection stopped")