

# 🎉 Bingo In Air 🎉  
> **A gesture-based Bingo game using Computer Vision and Machine Learning**

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.8.x-orange)
![Pygame](https://img.shields.io/badge/Pygame-2.x-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📖 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [License](#license)

---

## 📝 About the Project
**Bingo In Air** is a unique, gesture-controlled Bingo game. This project uses **Computer Vision** and **Hand Detection** to allow players to select Bingo numbers by simply pointing at them! Featuring custom sounds and visuals, this game provides an engaging, immersive experience. Perfect for tech enthusiasts, gamers, and anyone interested in interactive applications.

### ⚙️ Built With
- **Python** - For the core game logic
- **OpenCV** - For video capturing and image processing
- **MediaPipe** - For real-time hand detection
- **Pygame** - For sound effects and audio integration



---

## ✨ Features
- **Gesture-Based Interaction**: Select Bingo numbers using your fingers — no mouse or keyboard needed!
- **Real-Time Hand Tracking**: Powered by MediaPipe, it detects hand landmarks to enable precise interaction.
- **Multiplayer Support**: Includes Bingo boards for two players.
- **Custom Sounds**: Pop and applause sound effects for enhanced gameplay.
- **Custom Logo**: Displays a custom logo at the start of the game.

---

## 🚀 Installation

To get a local copy up and running, follow these steps:

### Prerequisites
Make sure you have Python and `pip` installed. Then, install the required packages:
```bash
pip install opencv-python mediapipe pygame numpy
```

### Clone the Repository
```bash
git clone https://github.com/your-username/Bingo-In-Air.git
cd Bingo-In-Air
```

### Run the Game
```bash
python se_final.py
```

---

## 🎮 How to Play

1. **Start the Game**:
   - Run the `se_final.py` script to start the game.
   - The game will display a logo and then load the Bingo boards.

2. **Interact with the Board**:
   - Use your **index finger** to point at a number on the Bingo board.
   - When a number is selected, you’ll hear a pop sound.

3. **Winning**:
   - The first player to clear their board wins! The game plays an applause sound and displays a congratulatory message.

4. **Controls**:
   - **'q'**: Quit the game.
   - **'r'**: Restart the game.

---

## 📂 Project Structure

| File               | Description                                                    |
|--------------------|----------------------------------------------------------------|
| `se_final.py`      | Main game logic and UI implementation.                         |
| `applause.wav`     | Sound effect that plays when a player wins.                    |
| `pop.wav`          | Sound effect that plays when a number is selected.             |
| `background_music.wav` | Background music for a more immersive experience.          |
| `logo.png`         | Custom logo displayed at the start of the game.                |

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📧 Contact



Linkedin : [https://www.linkedin.com/in/venkata-rahul-batta-822722278/](link)

---

## 🌟 Acknowledgments

This project uses [MediaPipe](https://google.github.io/mediapipe/) for hand tracking, which is developed and maintained by Google.

