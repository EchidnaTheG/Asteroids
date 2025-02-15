

# Python Asteroids Game

A classic arcade-style asteroids game built with Pygame.

## Description

This is a 2D space shooter where you control a player ship trying to survive an increasingly dangerous asteroid field. The game features:

- Player-controlled spaceship with smooth rotation and movement
- Shooting mechanics with bullet-asteroid collision
- Splitting asteroids when shot
- Randomly spawning asteroid field
- Collision detection system
- 60 FPS gameplay
- Game over condition on player-asteroid collision

## Prerequisites

The game requires:
- Python 3.x
- Pygame 2.6.1

Install dependencies using:
```sh
pip install -r requirements.txt
```

## Game Controls
- `W` - Move forward
- `S` - Move backward
- `A` - Rotate left
- `D` - Rotate right
- `SPACE` - Shoot
- Close window to quit

## Project Structure
- main.py - Main game loop and initialization
- player.py - Player ship and shooting mechanics
- asteroid.py - Asteroid object with splitting behavior
- asteroidfield.py - Asteroid spawning system
- constants.py - Game constants and configuration
- circleshape.py - Base class for circular collision detection

## Features
- Dynamic asteroid splitting when shot
- Continuous asteroid spawning from screen edges
- Smooth player movement with acceleration
- Cooldown-based shooting mechanics
- Precise circular collision detection

## How to Run
```sh
python main.py
```

## Development
Built using Pygame with object-oriented programming principles. Uses sprite groups for efficient game object management and circular collision detection for accurate hit detection.