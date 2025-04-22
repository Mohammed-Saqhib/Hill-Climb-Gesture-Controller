"""Configuration settings for Hill Climb Racing Hand Controller."""

import cv2  # Add this import statement

# Camera settings
CAMERA_INDEX = 0
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
FLIP_CAMERA = True  # Mirror the camera

# MediaPipe settings
MIN_DETECTION_CONFIDENCE = 0.7
MIN_TRACKING_CONFIDENCE = 0.7

# Game control settings
GAS_KEY = "right"
BRAKE_KEY = "left"

# Gesture settings
GAS_GESTURE_FINGERS = 5      # Full open hand for gas
BRAKE_GESTURE_FINGERS = 0    # Closed fist for brake
NEUTRAL_GESTURE_FINGERS = 2  # Two fingers for neutral

# UI settings
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.7
FONT_COLOR = (255, 255, 255)  # White
FONT_THICKNESS = 2
BACKGROUND_COLOR = (0, 0, 0)  # Black
GAS_COLOR = (0, 255, 0)       # Green
BRAKE_COLOR = (0, 0, 255)     # Red
NEUTRAL_COLOR = (255, 255, 0)  # Yellow

# Performance settings
FPS_TARGET = 30
