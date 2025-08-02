# 🖐️ AI-Powered Hand Gesture Whiteboard

An intelligent, hands-free whiteboard system built using **OpenCV**, **MediaPipe**, and **Matplotlib**, allowing users to draw and erase in real-time using simple hand gestures. Ideal for presentations, teaching, creative sketching, and human-computer interaction experiments.

---

## 📸 Demo

> ✨ Real-time hand tracking with gesture-based writing and erasing  
> ✨ Interactive canvas without touching any screen or device  
> ✨ Runs on your local webcam input  

---

## 🚀 Features

- 🧠 Real-time hand gesture recognition (Writing, Erasing, Idle)
- 🎨 Virtual whiteboard canvas using `matplotlib`
- ✍️ Draw using your **index finger** only
- 🧽 Erase using a multi-finger open palm gesture
- 🔁 Mirror view with live webcam feed
- ⚙️ Configurable pen color, thickness, and eraser size

---

## 🧰 Tech Stack

| Component      | Library/Framework      |
|----------------|------------------------|
| Hand Tracking  | [MediaPipe](https://github.com/google/mediapipe) |
| Drawing & Camera | [OpenCV](https://opencv.org/) |
| Canvas Display | [Matplotlib](https://matplotlib.org/) |
| Logic & UI     | Python 3.x             |

---

## 🔧 Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/himanshu9470/SkySketch-Real-Time-Gesture-Writing-
   cd SkySketch-Real-Time-Gesture-Writing-


2. **Install dependencies**

   ```bash
   pip install opencv-python mediapipe matplotlib numpy
   ```

3. **Run the whiteboard**

   ```bash
   python app.py
   ```

4. **Quit anytime**

   * Press **`q`** to stop the application.

---

## ✋ Gesture Guide

| Gesture    | Description                             |
| ---------- | --------------------------------------- |
| ✍️ Writing | Index finger pointing down (others up)  |
| 🧼 Erasing | All fingers extended with thumb outward |
| ✋ Idle     | No recognized gesture                   |

---

## 📁 File Structure

```
gesture-whiteboard/
│
├── app.py       # Main script
├── README.md           # Documentation
└── requirements.txt    # Optional dependency list
```

---

## 🧠 How It Works

* The webcam feed is flipped and processed frame-by-frame.
* MediaPipe identifies hand landmarks.
* Based on finger positions and thresholds, a gesture is classified:

  * If only the index finger is down → "writing"
  * If all fingers are extended → "erasing"
* The system draws/erases on a white canvas displayed via Matplotlib.

---

## 🧪 Future Improvements

* Add gesture to **change pen color**
* Support for **multiple hands**
* Save drawings as **image files**
* Toggle between **drawing/erasing/undo** using gestures
* UI buttons for more controls

---

## 🙌 Acknowledgements

* [Google MediaPipe](https://mediapipe.dev/)
* [OpenCV Python](https://pypi.org/project/opencv-python/)
* [Matplotlib](https://matplotlib.org/)

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

> Created with 💡 and 🤖 by \[HIMANSHU KUMAR]

```
