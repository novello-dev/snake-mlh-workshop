# 🐍 Major League Hacking API Workshop - Snake

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.6.1-green)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)

Small Snake game built with Python + Pygame.

###  Main files
- `src/neon_snake.py` — main game
- `src/intro.py` — tiny demo/intro
- `src/pygame2.py` — simple movement demo

###  Requirements
- Python 3.10+ (or compatible)
- `pygame==2.6.1` (see `requirements.txt`)

## Quick start (Windows — PowerShell)
```powershell
python -m venv .venv
& .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src\neon_snake.py
```

### Controls
- Arrow keys — move the snake
- Close window — quit

### Notes
- `.gitignore` already ignores `.venv/` and Python build artifacts.
- `src/intro.py` and `src/pygame2.py` are small demos and safe to run.

### What I Learned

Working on this small project taught me several important fundamentals:

- **Game loops** - Understanding how each frame updates logic, renders graphics, and processes input.
- **Keyboard input handling** - reacting to arrow keys and ensuring the snake can’t reverse direction instantly.
- **Basic collision detection** - wall checks, fruit collision, and self-collision.
- **Grid-based movement** - updating the snake in fixed 10px increments for predictable logic.
- **State management** - keeping track of score, direction, fruit spawning, and game-over state.
- **Rendering with Pygame** - drawing rectangles, updating the screen, and using the `Clock` object for FPS control.
- **Separating logic into methods** - using a class to organize the code into smaller, readable parts.
- **Debugging real-time programs** - dealing with timing issues, lag perception, and event loop behavior.


### Attribution
This project was created as part of the Major League Hacking (MLH) API Week workshop.
The base implementation and logic come from the MLH instructor’s session.
This repository exists solely for learning and personal study.
