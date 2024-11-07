# Bingo In Air

This project implements a virtual Bingo game that can be controlled using hand gestures. It utilizes OpenCV for video capture and MediaPipe for hand detection, allowing players to interact with the game by touching virtual bingo numbers with their fingers. Sounds and a logo are added to enhance the gaming experience.

## Features
- Real-time hand gesture detection using MediaPipe.
- Interactive Bingo boards for two players.
- Pop sound effect when a number is selected.
- Applause sound effect when a player wins.
- Customizable Bingo board with blocked cells.
- Displays a custom logo at the start of the game.

## Requirements
- Python 3.x
- OpenCV
- NumPy
- MediaPipe
- Pygame

To install the required packages, run:
```bash
pip install opencv-python mediapipe pygame numpy
```

## Files
- `se_final.py`: The main Python script for running the game.
- `applause.wav`: Sound effect played when a player wins.
- `pop.wav`: Sound effect played when a number is selected.
- `background_music.wav`: Background music for the game.
- `logo.png`: Custom logo displayed at the start of the game.

## How to Run the Game
1. Ensure you have the necessary dependencies installed.
2. Run the game by executing the Python script:
   ```bash
   python se_final.py
   ```

3. The game window will open, displaying the Bingo boards for two players. Use hand gestures to select numbers on the board. The game ends when one of the players clears all the numbers on their board.

4. Press **'r'** to restart the game or **'q'** to quit.

