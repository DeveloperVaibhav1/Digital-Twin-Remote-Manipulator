# 🤖 Digital Twin Remote Manipulator

Real-time system that tracks human hand movement and mirrors it on a physical robotic arm using computer vision, WiFi, and ESP32.

---

## 🧠 Overview

* Camera captures hand movement
* Python processes and extracts coordinates
* Data sent wirelessly to ESP32
* Motors move robotic arm accordingly

---

## ⚙️ Workflow

1. Hand detected using MediaPipe
2. X, Y coordinates calculated
3. Values mapped to motor angles
4. Data sent via WiFi
5. ESP32 controls stepper motors

---

## 🧩 Architecture

```
Camera → Hand Tracking → Mapping → WiFi → ESP32 → Motors → Arm
```

---

## 🛠️ Tech Stack

**Software:**

* Python
* OpenCV
* MediaPipe

**Hardware:**

* ESP32
* servo Motors
* Motor Driver

---

## 📁 Structure

```
hand_tracking_robot/
├── main.py
├── hand_tracking.py
├── communication.py
├── utils.py
├── config.py
└── requirements.txt
```

---

## ▶️ Run

```bash
pip install -r requirements.txt
python main.py
```

---

