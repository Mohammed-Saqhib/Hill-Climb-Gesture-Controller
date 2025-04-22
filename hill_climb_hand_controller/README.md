# Hill Climb Racing Hand Controller

Control Hill Climb Racing using hand gestures captured by your webcam!

## Features

- Play Hill Climb Racing using hand gestures
- Visual feedback of detected gestures
- Customizable settings
- Real-time performance metrics

## Controls

- **Open Hand (5 fingers)**: Gas (right arrow key)
- **Closed Fist (0 fingers)**: Brake (left arrow key)
- **Other Gestures**: No action (releases all keys)

## Requirements

- Python 3.7+
- Webcam
- Hill Climb Racing (or similar game)

## Installation

1. Clone this repository:
```
git clone <repository-url>
cd hill_climb_hand_controller
```

2. Install required dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Start Hill Climb Racing and keep it visible on your screen
2. Run the application:
```
python main.py
```

3. Position your hand in front of the webcam
4. Use the gestures to control the game
5. Press 'q' to quit, 'i' to toggle instructions

## Troubleshooting

- **Poor detection**: Ensure good lighting and keep your hand within frame
- **Lag**: Reduce camera resolution in config.py
- **Key not working**: Make sure game window is active/focused

## Customization

Edit `config.py` to customize:
- Camera settings
- Key bindings
- Detection sensitivity
- UI appearance

## License

This project is open source and available under the MIT License.
