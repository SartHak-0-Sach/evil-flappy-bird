# ✈️🏢 Evil flappy bird

Evil flappy bird is a side-scrolling 2D arcade game developed using **Python** and **Pygame**. Inspired by Flappy Bird, the player controls a small plane that must navigate through gaps between pairs of buildings that continuously appear across the screen. The goal is to survive as long as possible and achieve the highest score.

---

## 🚀 Features

- 🛩️ **Plane Physics**: Simulates realistic gravity and lift mechanics.
- 🧱 **Obstacle Pairs**: Buildings are spawned in pairs with gaps in between.
- 🎨 **Custom Graphics**: Includes plane, buildings, background, explosion, and more.
- 🔊 **Sound Effects**: Crash and explosion sounds on collision.
- 📈 **Score System**: Score increases as the player successfully passes building pairs.
- 🖱️ **User Input**: Controlled using `Spacebar` or mouse click.
- 🎬 **Start Screen**: Idle screen before the game begins.
- 💥 **Explosion Effect**: Explosion image shown on collision.

---

## 📂 Project Structure

```

FlappyPlane/
├── assets/
│   ├── background.png
│   ├── building.png
│   ├── crash.wav
│   ├── explosion.png
│   ├── explosion.wav
│   ├── plane.png
│   └── Ubuntu-Bold.ttf
├── main.py
└── README.md

````

---

## 🛠️ How to Run

### 1. Prerequisites

Ensure you have **Python 3.6+** installed.

Install required dependencies:

```bash
pip install pygame
````

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/FlappyPlane.git
cd FlappyPlane
```

### 3. Run the Game

```bash
python main.py
```

---

## 🎮 Controls

| Key / Action  | Function                   |
| ------------- | -------------------------- |
| `Spacebar`    | Make the plane go up       |
| `Mouse Click` | Also makes the plane go up |
| `ESC` / `X`   | Quit the game              |

---

## 🧠 Game Mechanics

* The plane constantly falls due to gravity.
* Pressing **Space** or clicking **mouse** gives it an upward thrust (`lift`).
* Pairs of buildings move from right to left.
* The player must navigate the plane through the vertical gaps.
* Every time a pair is passed, the score increases by 1.
* Collision with buildings or flying off-screen ends the game.
* Upon crash, an explosion graphic and sound are triggered, followed by a restart.

---

## 📜 Code Overview

The main components:

* `game_loop()`: Runs the actual game logic including spawning, collision detection, scoring, etc.
* `draw_window()`: Handles all the drawing of graphics every frame.
* `spawn_building()`: Randomly creates a new pair of buildings at a fixed interval.
* `game_started`: Boolean flag to handle the idle start screen.
* `game_over`: Boolean to trigger explosion and reset mechanism.

Key variables:

* `plane_y`, `plane_vel`: Plane’s vertical position and speed.
* `gravity`, `lift`: Physics constants for downward pull and upward force.
* `buildings`: List storing tuples of top and bottom building positions and their X coordinates.
* `SPAWN_RATE`: Interval between spawning new obstacles (in milliseconds).
* `GAP`: Vertical space between the building pair.

---

## 🖼️ Assets

* `plane.png`: Image of the airplane (flipped horizontally).
* `building.png`: Used for both top and bottom parts of building pairs.
* `background.png`: Background scene.
* `explosion.png`: Explosion shown on collision.
* `crash.wav` & `explosion.wav`: Sounds played on crash.
* `Ubuntu-Bold.ttf`: Font used for score and start screen.

---

## 📊 Scoring System

* The score increments by 1 when the plane crosses each pair of buildings.
* The score is displayed at the top-left corner of the screen.
* No leaderboard or persistent high score yet (can be added later).

---

## ⚠️ Known Limitations

* Game speed and difficulty do not increase over time.
* No restart button — the game auto-restarts after a crash.
* No pause feature or game menu.
* Only one plane skin and background.

---

## 💡 Possible Future Enhancements

* Add a main menu and pause menu.
* Add difficulty scaling over time (faster scroll, smaller gaps).
* Add sound toggle and mute option.
* Include high score saving via local file.
* Support for mobile-like touch inputs.
* Add different plane models/skins.

---

## 📚 Requirements

* Python 3.6+
* Pygame (tested on Pygame 2.0+)

---

## 👨‍💻 Author

**Sarthak Sachdev**
[GitHub](https://github.com/SartHak-0-Sach) • [LinkedIn](https://www.linkedin.com/in/sarthak2004/)

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).