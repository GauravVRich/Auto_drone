import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO(r"yolo_model\yolov8n.pt")  # Adjust path

def detect_objects(img_bytes):
    np_img = np.frombuffer(img_bytes, dtype=np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    results = model(img)[0]
    detections = []
    for box in results.boxes:
        cls = int(box.cls[0])
        name = model.names[cls]
        detections.append((name, box.xyxy[0].tolist()))
    return detections
