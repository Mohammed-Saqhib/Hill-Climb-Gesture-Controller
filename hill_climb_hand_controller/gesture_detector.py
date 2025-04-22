"""Hand gesture detection module using MediaPipe."""

import cv2
import mediapipe as mp
import numpy as np
from config import MIN_DETECTION_CONFIDENCE, MIN_TRACKING_CONFIDENCE

class GestureDetector:
    def __init__(self):
        """Initialize the hand tracking module."""
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE
        )
        
    def detect_hands(self, frame):
        """Process the frame and detect hands."""
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        return results
        
    def draw_landmarks(self, frame, results):
        """Draw hand landmarks on the frame."""
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    frame, 
                    hand_landmarks, 
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style()
                )
        return frame
    
    def count_fingers(self, hand_landmarks):
        """Count extended fingers using landmark positions with improved reliability."""
        fingers = []
        
        # Landmarks for fingertips and joints
        tips = [4, 8, 12, 16, 20]  # Thumb, index, middle, ring, pinky tips
        pips = [3, 6, 10, 14, 18]  # Second joints
        
        # Special case for thumb
        # Compare horizontal position to determine if thumb is extended
        if hand_landmarks.landmark[tips[0]].x < hand_landmarks.landmark[pips[0]].x:
            fingers.append(1)  # Extended
        else:
            fingers.append(0)  # Not extended
        
        # For other fingers, compare vertical positions
        for i in range(1, 5):
            if hand_landmarks.landmark[tips[i]].y < hand_landmarks.landmark[pips[i]].y:
                fingers.append(1)  # Extended (finger tip is above finger pip)
            else:
                fingers.append(0)  # Not extended
        
        return sum(fingers), fingers  # Return total count and list of extended fingers
        
    def detect_gesture(self, frame):
        """Detect hand gestures in a frame."""
        results = self.detect_hands(frame)
        finger_count = 0
        finger_states = []
        gesture_name = "No hand detected"
        
        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]  # Use the first detected hand
            finger_count, finger_states = self.count_fingers(hand_landmarks)
            
            # Name the gesture based on finger count
            if finger_count == 0:
                gesture_name = "Brake"
            elif finger_count == 5:
                gesture_name = "Gas"
            elif finger_count == 2 and finger_states[1] and finger_states[2]:
                gesture_name = "Neutral"  # Two fingers (index and middle) extended
            else:
                gesture_name = f"Fingers: {finger_count}"
                
        return {
            "frame": frame,
            "results": results,
            "finger_count": finger_count,
            "finger_states": finger_states,
            "gesture_name": gesture_name
        }
        
    def close(self):
        """Release resources."""
        self.hands.close()
