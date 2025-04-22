# Hill-Climb-Gesture-Controller

# Hill Climb Racing Hand Controller

Control Hill Climb Racing (or any similar driving game) using real‑time hand gestures captured by your webcam!

![Demo](docs/demo.gif)

## Features

- Play the game using simple hand gestures:
  - ✋ Open Hand (5 fingers) → **Gas** (press ▶️)
  - ✊ Closed Fist (0 fingers) → **Brake** (press ◀️)
  - ✌️ Two Fingers → **Neutral** (no key pressed)
- Visual feedback:
  - Live camera feed with overlaid hand landmarks
  - On‑screen status bar showing FPS, current gesture & game state
  - Instruction overlay you can toggle at any time
- Configurable:
  - Camera resolution, flip mode
  - Minimum detection & tracking confidence
  - Key bindings for gas/brake
  - UI colors, fonts & layout
  - Target FPS for smooth performance

## Prerequisites

- Python 3.7+
- Webcam
- Windows / macOS / Linux
- Hill Climb Racing or any game that responds to arrow keys

## Installation

1. Clone this repository  
   ```bash
   git clone https://github.com/<your‑username>/hill_climb_hand_controller.git
   cd hill_climb_hand_controller
   ```
2. Create & activate a virtual environment (recommended)  
   ```bash
   python -m venv venv
   .\venv\Scripts\activate    # Windows
   source venv/bin/activate   # macOS/Linux
   ```
3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

All settings live in `config.py`:

- CAMERA_INDEX, CAMERA_WIDTH, CAMERA_HEIGHT, FLIP_CAMERA  
- MIN_DETECTION_CONFIDENCE, MIN_TRACKING_CONFIDENCE  
- GAS_KEY, BRAKE_KEY, gesture finger counts  
- UI fonts, colors, target FPS  

Feel free to tweak these values to suit your environment and preferences.

## Usage

1. Make sure your game window is open and focused.
2. Run the application:  
   ```bash
   python main.py
   ```
3. Position your hand within the webcam frame.
4. Use gestures to control the game:
   - Open hand for gas
   - Closed fist for brake
   - Two fingers for neutral
5. Press `i` to toggle the instruction overlay.
6. Press `q` to quit.

## Troubleshooting

- **No camera feed**: Verify your webcam is connected and accessible. Check `CAMERA_INDEX`.
- **Poor detection**: Ensure good lighting and keep your hand centered in the frame.
- **Laggy performance**: Lower `CAMERA_WIDTH`/`HEIGHT` or reduce `FPS_TARGET`.
- **Keys not working**: Make sure the game window is active and that your OS allows synthetic key presses.

## Contributing

Contributions, issues and feature requests are welcome!  
1. Fork it (<https://github.com/Mohammed-Saqhib/Hill-Climb-Gesture-Controller/tree/main/hill_climb_hand_controller/fork>)  
2. Create your feature branch (`git checkout -b feature/YourFeature`)  
3. Commit your changes (`git commit -m 'Add some feature'`)  
4. Push to the branch (`git push origin feature/YourFeature`)  
5. Open a Pull Request

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Need Help or Want to Connect?
If you encounter any issues, have suggestions, or would like to express your appreciation, please feel free to reach out via email at msaqhib76@gmail.com. I am always happy to assist and welcome your feedback.
