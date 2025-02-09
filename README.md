# Python Asteroids Game

A classic arcade-style asteroids game built with Pygame.

## Description

This is a 2D space shooter where you control a player ship trying to survive an increasingly dangerous asteroid field. The game features:

- Player-controlled spaceship
- Randomly spawning asteroids
- Collision detection
- Smooth movement physics
- 60 FPS gameplay

## Prerequisites

The game requires:
- Python 3.x
- Pygame

You can install the required dependencies using:
```sh
pip install -r requirements.txt
```

## How to Run

To start the game, run:
```sh
python main.py
```

## Game Controls
- Use keyboard controls to navigate your ship through the asteroid field
- Avoid colliding with asteroids
- Game ends if your ship collides with an asteroid

## Project Structure
- 

main.py

 - Main game loop and initialization
- 

player.py

 - Player ship logic
- 

asteroid.py

 - Asteroid object implementation
- 

asteroidfield.py

 - Asteroid spawning system
- 

constants.py

 - Game constants and configuration
- 

circleshape.py

 - Collision detection utilities

## Development
This game is built using the Pygame library and follows object-oriented programming principles with sprite groups for efficient game object management.