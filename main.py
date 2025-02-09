import pygame
from constants import *
from player import *
from asteroid import *
from circleshape import *
from asteroidfield import *
import sys

def main():
   updatable_group = pygame.sprite.Group()
   drawable_group = pygame.sprite.Group()
   asteroid_group = pygame.sprite.Group()
   shot_group = pygame.sprite.Group()
   Player.containers = (updatable_group, drawable_group)
   Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
   
   x= SCREEN_WIDTH/2
   y= SCREEN_HEIGHT/2
   player= Player(x, y)
   AsteroidField.containers = (updatable_group,)
   asteroid_field = AsteroidField()
   pygame.init()
   TimeClock=pygame.time.Clock()
   dt= 0
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
   while True:
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       screen.fill("black")
       updatable_group.update(dt)
       for sprite in drawable_group:
           sprite.draw(screen)
       for asteroid in asteroid_group:
           if asteroid.check_collision(player):
               print("GAME OVER!")
               pygame.quit()
               sys.exit()
       pygame.display.flip()
       dt=TimeClock.tick(60)/1000
       
if __name__ == "__main__":
    main()