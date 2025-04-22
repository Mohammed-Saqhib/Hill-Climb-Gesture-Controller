"""UI elements for the Hill Climb Racing Hand Controller."""

import cv2
import numpy as np
import time
from config import (
    FONT, FONT_SCALE, FONT_COLOR, FONT_THICKNESS, BACKGROUND_COLOR,
    GAS_COLOR, BRAKE_COLOR, NEUTRAL_COLOR, GAS_KEY, BRAKE_KEY
)

class UIManager:
    def __init__(self, width, height):
        """Initialize the UI manager."""
        self.width = width
        self.height = height
        self.fps_list = []
        self.last_frame_time = time.time()
        
    def calculate_fps(self):
        """Calculate frames per second."""
        current_time = time.time()
        fps = 1 / (current_time - self.last_frame_time)
        self.last_frame_time = current_time
        
        # Keep only the last 10 FPS readings for smoother average
        self.fps_list.append(fps)
        if len(self.fps_list) > 10:
            self.fps_list.pop(0)
            
        return sum(self.fps_list) / len(self.fps_list)
        
    def add_status_bar(self, frame, game_state, gesture_name, finger_count):
        """Add a status bar to the bottom of the frame."""
        # Create a black background for the status bar
        status_height = 80
        status_bar = np.zeros((status_height, frame.shape[1], 3), dtype=np.uint8)
        
        # Add FPS counter
        fps = self.calculate_fps()
        cv2.putText(
            status_bar, 
            f"FPS: {fps:.1f}", 
            (10, 20), 
            FONT, 
            FONT_SCALE, 
            FONT_COLOR, 
            FONT_THICKNESS
        )
        
        # Add gesture information
        cv2.putText(
            status_bar, 
            f"Gesture: {gesture_name} ({finger_count} fingers)", 
            (10, 50), 
            FONT, 
            FONT_SCALE, 
            FONT_COLOR, 
            FONT_THICKNESS
        )
        
        # Add game state with color coding
        if game_state == "gas":
            color = GAS_COLOR
            state_text = f"GAS ({GAS_KEY})"
        elif game_state == "brake":
            color = BRAKE_COLOR
            state_text = f"BRAKE ({BRAKE_KEY})"
        else:
            color = NEUTRAL_COLOR
            state_text = "NEUTRAL"
        
        cv2.putText(
            status_bar, 
            state_text, 
            (frame.shape[1] - 200, 50), 
            FONT, 
            FONT_SCALE, 
            color, 
            FONT_THICKNESS
        )
        
        # Combine the original frame with the status bar
        combined_frame = np.vstack((frame, status_bar))
        return combined_frame
    
    def add_instruction_overlay(self, frame, show_instructions=True):
        """Add an instruction overlay to help the user."""
        if not show_instructions:
            return frame
            
        instructions = [
            "CONTROLS:",
            f"Open Hand (5 fingers) = GAS ({GAS_KEY} key)",
            f"Closed Fist (0 fingers) = BRAKE ({BRAKE_KEY} key)",
            "Other gestures = No action",
            "Press 'q' to quit, 'i' to toggle instructions"
        ]
        
        # Create semi-transparent overlay
        overlay = frame.copy()
        cv2.rectangle(overlay, (10, 10), (400, 150), (0, 0, 0), -1)
        
        # Add text instructions
        for i, line in enumerate(instructions):
            cv2.putText(
                overlay,
                line,
                (20, 30 + i * 25),
                FONT,
                0.6,
                FONT_COLOR,
                1
            )
        
        # Blend the overlay with the original frame
        alpha = 0.7
        frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
        
        return frame
