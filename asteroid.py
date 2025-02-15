from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random as r

class Asteroid(CircleShape):
    
        def __init__(self, x, y, radius):
                super().__init__(x, y, radius)
                self.x= x
                self.y= y
        def draw(self,screen ):
                pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        def update(self, dt):
             self.position += self.velocity * dt   
        def split(self):
             self.kill()
             angle= r.uniform(20.0, 50.0)
             if self.radius <= ASTEROID_MIN_RADIUS:
                    return 
             rotated_velocity1=self.velocity.rotate(angle)
             rotated_velocity2=self.velocity.rotate(-angle)
             new_radius=self.radius- ASTEROID_MIN_RADIUS
             offset_distance = self.radius * 0.5  # Adjust this factor if needed
             offset1 = rotated_velocity1.normalize() * offset_distance
             offset2 = rotated_velocity2.normalize() * offset_distance

             fragment1= Asteroid(self.x, self.y, new_radius)
             fragment2= Asteroid(self.x, self.y, new_radius)
             fragment1.position= self.position + offset1
             fragment2.position= self.position + offset2
             fragment1.velocity= rotated_velocity1 *1.2
             fragment2.velocity = rotated_velocity2 *1.2
             