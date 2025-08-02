import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5)

class Whiteboard:
    def _init_(self):
        self.canvas = np.ones((720, 1280, 3), dtype=np.uint8) * 255
        self.prev_point = None
        self.current_gesture = None
        self.pen_color = (0, 0, 0)  # Default pen color is black
        self.pen_thickness = 5  # Default pen thickness
        self.eraser_size = 20  # Size of eraser

    def update(self, gesture, current_point):
        self.current_gesture = gesture
        if self.current_gesture == "writing":
            if self.prev_point:
                cv2.line(self.canvas, self.prev_point, current_point, self.pen_color, self.pen_thickness)
            self.prev_point = current_point
        elif self.current_gesture == "erasing":
            # Draw with white color to simulate erasing
            if self.prev_point:
                cv2.line(self.canvas, self.prev_point, current_point, (255, 255, 255), self.eraser_size)
            self.prev_point = current_point
        else:
            self.prev_point = None

    def clear(self):
        """Resets the canvas to a blank white screen."""
        self.canvas = np.ones((720, 1280, 3), dtype=np.uint8) * 255

def get_index_tip_position(hand_landmarks):
    """
    Calculates the x and y coordinates of the index finger tip.
    Args:
      hand_landmarks: The detected hand landmarks.
    Returns:
      A tuple containing the x and y coordinates of the index finger tip.
    """
    index_tip_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    frame_width, frame_height = 1280, 720
    x = int(index_tip_landmark.x * frame_width)
    y = int(index_tip_landmark.y * frame_height)
    return (x, y)

def classify_gesture(hand_landmarks):
    """
    Classifies the hand gesture as "writing", "erasing", or "none".
    Args:
      hand_landmarks: The detected hand landmarks.
    Returns:
      A string indicating the classified gesture.
    """
    # Get landmark positions for key fingers
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y
    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
    thumb_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x

    # Thresholds (may need adjustment based on testing)
    writing_threshold = wrist + (wrist * 0.1)  # Index tip below this threshold
    erasing_threshold = wrist - (wrist * 0.1)  # All tips above this threshold
    thumb_threshold = 0.2  # Thumb position threshold

    # Check for writing gesture (index finger extended down, others up)
    if (index_tip > writing_threshold and
        middle_tip < writing_threshold and
        ring_tip < writing_threshold and
        pinky_tip < writing_threshold):
        return "writing"

    # Check for erasing gesture (all fingers extended up)
    if (index_tip < erasing_threshold and
        middle_tip < erasing_threshold and
        ring_tip < erasing_threshold and
        pinky_tip < erasing_threshold and
        thumb_tip_x < hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x - thumb_threshold):
        return "erasing"

    return "none"

def detect_hands(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    return results

def main():
    cap = cv2.VideoCapture(0)
    whiteboard = Whiteboard()

    # Set up matplotlib display
    plt.ion()
    fig, ax = plt.subplots(figsize=(12, 7))
    img_display = ax.imshow(whiteboard.canvas)
    plt.axis('off')
    plt.tight_layout()

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Flip frame for mirror effect
            frame = cv2.flip(frame, 1)

            # Detect hands
            results = detect_hands(frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Get gesture and position
                    gesture = classify_gesture(hand_landmarks)
                    index_tip = get_index_tip_position(hand_landmarks)

                    # Update whiteboard
                    whiteboard.update(gesture, index_tip)

                    # Draw landmarks on frame for visualization (optional)
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
                        mp.solutions.drawing_styles.get_default_hand_connections_style())

            # Update display
            img_display.set_data(cv2.cvtColor(whiteboard.canvas, cv2.COLOR_BGR2RGB))
            fig.canvas.draw()
            fig.canvas.flush_events()

            # Check for quit command (works in local environment)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        plt.ioff()
        plt.show()

if _name_ == "_main_":
    main()
