"""Game controller module to handle keyboard inputs."""

import keyboard
import time
from config import GAS_KEY, BRAKE_KEY, GAS_GESTURE_FINGERS, BRAKE_GESTURE_FINGERS, NEUTRAL_GESTURE_FINGERS

class GameController:
    def __init__(self):
        """Initialize the game controller."""
        self.current_state = "neutral"
        self.last_command_time = 0
        self.command_cooldown = 0.05  # 50ms cooldown to prevent rapid key presses
        
    def control_game(self, finger_count):
        """Control the game based on finger count."""
        current_time = time.time()
        
        # Check if cooldown has elapsed
        if current_time - self.last_command_time < self.command_cooldown:
            return self.current_state
            
        # Update last command time
        self.last_command_time = current_time
        
        # Handle different gestures
        if finger_count == BRAKE_GESTURE_FINGERS:  # Brake gesture (closed fist)
            keyboard.release(GAS_KEY)
            keyboard.press(BRAKE_KEY)
            new_state = "brake"
        elif finger_count == GAS_GESTURE_FINGERS:  # Gas gesture (open hand)
            keyboard.release(BRAKE_KEY)
            keyboard.press(GAS_KEY)
            new_state = "gas"
        else:  # Neutral or unrecognized gesture
            keyboard.release(GAS_KEY)
            keyboard.release(BRAKE_KEY)
            new_state = "neutral"
        
        self.current_state = new_state
        return new_state
        
    def cleanup(self):
        """Release all keys when exiting."""
        keyboard.release(GAS_KEY)
        keyboard.release(BRAKE_KEY)
