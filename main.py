import cv2
import time
from ultralytics import YOLO

# Load lightweight model (CPU friendly)
model = YOLO("yolov8n.pt")

# Open HDMI capture card (usually /dev/video0)
cap = cv2.VideoCapture(2)

if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

prev_time = 0
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for performance
    frame = cv2.resize(frame, (1080, 720))

    frame_count += 1

    # Only run detection every 2nd frame (performance boost)
    if frame_count % 2 == 0:
        results = model(frame, conf=0.4, verbose=False)

        # Draw bounding boxes
        annotated_frame = results[0].plot()
    else:
        annotated_frame = frame

    # FPS calculation
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
    prev_time = current_time

    cv2.putText(
        annotated_frame,
        f"FPS: {int(fps)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2,
    )

    cv2.imshow("Wildlife Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
