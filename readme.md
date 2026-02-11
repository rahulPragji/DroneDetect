# 🐘 DroneDetect

Real-time wildlife detection system using drone RGB / thermal video feed.

Built to assist wildlife officials in Botswana track animals entering human zones.

---

## 🚀 Features (Current)

- HDMI capture input
- Real-time object detection
- Bounding box visualization
- Optimized for low-power Ubuntu laptop

---

## 🧠 Planned Features

- Custom-trained wildlife detection model
- Thermal + RGB adaptive detection
- Trip-based PDF reporting
- Offline-first design (remote deployment ready)

---

## 🛠 Tech Stack

- Python 3.12
- OpenCV
- Ultralytics YOLO
- Ubuntu Linux

---

## ⚙️ Setup

```bash
git clone https://github.com/yourusername/DroneDetect.git
cd DroneDetect
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
