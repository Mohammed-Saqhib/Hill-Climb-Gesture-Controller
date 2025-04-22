"""
Hill Climb Racing Hand Controller

Play Hill Climb Racing using hand gestures captured by your webcam.
- Open hand (5 fingers) = Gas
- Closed fist (0 fingers) = Brake
- Other gestures = Neutral (no action)
"""

import cv2
import time
import numpy as np
from gesture_detector import GestureDetector
from game_controller import GameController
from ui_elements import UIManager
from config import (
    CAMERA_INDEX, CAMERA_WIDTH, CAMERA_HEIGHT, FLIP_CAMERA,
    FPS_TARGET
)

def main():
    """Main application function."""
    # Initialize components
    gesture_detector = GestureDetector()
    game_controller = GameController()
    
    # Set up video capture
    cap = cv2.VideoCapture(CAMERA_INDEX)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
    
    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    # Get actual width and height
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    ui_manager = UIManager(width, height)
    
    # UI state
    show_instructions = True
    
    # Main loop
    try:
        while True:
            # Control frame rate
            start_time = time.time()
            
            # Read frame
            ret, frame = cap.read()
            if not ret:
                print("Error: Can't receive frame. Exiting...")
                break
            
            # Flip frame horizontally for natural movement if enabled
            if FLIP_CAMERA:
                frame = cv2.flip(frame, 1)
            
            # Process hand gestures
            gesture_data = gesture_detector.detect_gesture(frame)
            
            # Draw hand landmarks
            frame = gesture_detector.draw_landmarks(frame, gesture_data["results"])
            
            # Control game based on gesture
            game_state = game_controller.control_game(gesture_data["finger_count"])
            
            # Add UI elements
            frame = ui_manager.add_instruction_overlay(frame, show_instructions)
            frame = ui_manager.add_status_bar(
                frame, 
                game_state, 
                gesture_data["gesture_name"], 
                gesture_data["finger_count"]
            )
            
            # Display the resulting frame
            cv2.imshow("Hill Climb Racing Hand Controller", frame)
            
            # Handle keyboard input
            key = cv2.waitKey(1)
            if key == ord('q'):
                print("Quitting application...")
                break
            elif key == ord('i'):
                show_instructions = not show_instructions
            
            # Control frame rate
            elapsed_time = time.time() - start_time
            sleep_time = max(0, 1/FPS_TARGET - elapsed_time)
            if sleep_time > 0:
                time.sleep(sleep_time)
                
    finally:
        # Clean up resources
        game_controller.cleanup()
        gesture_detector.close()
        cap.release()
        cv2.destroyAllWindows()
        print("Application closed successfully.")

if __name__ == "__main__":
    main()
