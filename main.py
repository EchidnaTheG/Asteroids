import pygame
from constants import *
from player import *


def main():
   
   x= SCREEN_WIDTH/2
   y= SCREEN_HEIGHT/2
   player= Player(x, y)
   
   pygame.init()
   TimeClock=pygame.time.Clock()
   dt= 0
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
   while True:
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       screen.fill("black")
       player.draw(screen)
       player.update(dt)
       pygame.display.flip()
       dt=TimeClock.tick(60)/1000
       
if __name__ == "__main__":
    main()