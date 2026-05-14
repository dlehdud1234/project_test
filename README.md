# 🎬 Gesture-Based YouTube Controller

노트북 웹캠과 MediaPipe 기반 손 제스처를 이용하여 YouTube를 제어하는 프로젝트입니다.  
손바닥 및 스와이프 제스처를 인식하여 키보드 입력으로 YouTube 기능을 제어합니다.

---

# 📁 프로젝트 구조

project/
│
├── main.py
│
├── input/
│   ├── __init__.py
│   ├── camera.py
│   ├── gesture_detector.py
│
├── events/
│   ├── __init__.py
│   ├── debounce.py
│
├── core/
│   ├── __init__.py
│   ├── policy_engine.py
│
├── execution/
│   ├── __init__.py
│   ├── youtube_controller.py
│   ├── keyboard_controller.py
│
└── requirements.txt

---

# 🧠 시스템 구조

Camera Input
    ↓
Gesture Detection (MediaPipe)
    ↓
Debounce / Noise Filtering
    ↓
Policy Engine (Gesture → Action)
    ↓
Keyboard Controller (YouTube Control)

---

# ⚙️ 기술 스택

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

---

# ✋ 지원 제스처

## 🖐 Palm Gesture (손바닥)

MediaPipe landmark 기반:
- 0 (wrist)
- 5, 9, 13, 17 (finger base)
- 8, 12, 16, 20 (finger tip)

판별 방식:
- 손가락 3개 이상 펼쳐짐 → OPEN_PALM

동작:
OPEN_PALM → Play / Pause

---

## 👉 Swipe Gesture

wrist(0번 landmark)의 이동 방향 기반

판별 기준:
- dx → 좌우
- dy → 상하
- threshold 기반 이동 감지
- cooldown 적용

동작:

SWIPE_RIGHT → Next Video
SWIPE_LEFT  → Previous Video
SWIPE_UP    → Volume Up
SWIPE_DOWN  → Volume Down

---

# 🎮 YouTube 제어 방식

| 기능 | 키 |
|------|----|
| 재생 / 정지 | Space |
| 다음 영상 | Shift + N |
| 이전 영상 | Shift + P |
| 볼륨 증가 | ↑ |
| 볼륨 감소 | ↓ |

---

# 🧠 Gesture Detection 로직

## Palm Detection

open_fingers >= 3 → OPEN_PALM

---

## Swipe Detection

wrist 이동량 기반:

- dx > threshold → RIGHT / LEFT
- dy > threshold → UP / DOWN

---

# 🧯 안정성 처리

## 1. Debounce

같은 제스처 연속 실행 방지

- cooldown 적용 (0.8 ~ 1.5초)

---

## 2. Noise Filtering

- 작은 손 떨림 제거
- threshold 이하 movement 무시

---

# 🚀 실행 방법

## 1. 설치

```bash
pip install opencv-python mediapipe pyautogui numpy

dd