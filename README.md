# Asteroids

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [Highscore](#highscore)
- [Sound Effects](#sound-effects)
- [Dependencies](#dependencies)
- [License](#license)

## Introduction
Asteroids is a classic arcade game where the player controls a spaceship and must destroy incoming asteroids. The game features an asteroid field, a player-controlled spaceship, and various game mechanics such as shooting, asteroid splitting, and collision detection.

## Features
- Randomly spawning asteroids of different sizes
- Player-controlled spaceship with rotation and movement
- Shooting mechanism to destroy asteroids
- Asteroid splitting upon destruction
- Collision detection between player, asteroids, and shots
- Highscore tracking
- Sound effects for shooting, asteroid destruction, and game over

## Installation
1. Ensure you have Python 3.12 or higher installed on your system.
2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the `main.py` file to start the game.
2. The main menu will be displayed, where you can choose to play the game, view the controls, or quit.
3. If you choose to play, the game will start, and you can control the spaceship using the provided controls.
4. The game will continue until you lose all your lives, at which point the game over screen will be displayed.

## Controls
- `W`: Move forward
- `A`: Rotate left
- `D`: Rotate right
- `Space`: Shoot
- `Esc`: Quit to main menu

## Highscore
The game will keep track of the highest score achieved and save it to a file named `highscore.txt`. The highscore will be displayed on the main menu and the game over screen.

## Sound Effects
The game includes the following sound effects:
- Shooting sound
- Large asteroid destruction sound
- Small asteroid destruction sound
- Game over sound

The sound effects can be disabled if the system does not support audio playback.

## Dependencies
The game uses the following Python library:
- `pygame==2.6.1`
To run the game you will need some sort of virtual environment. I used:
- `uv==0.8.17`

## License
This project is licensed under the [MIT License](LICENSE).

