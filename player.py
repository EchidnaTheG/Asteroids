import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    timer = 0
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS )
        self.rotation = 0
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw (self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN
        self.timer -= dt
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def shoot(self,):
         # Calculate the direction the shot should travel
        direction = pygame.Vector2(0, 1).rotate(self.rotation)

        # Scale the direction to get the velocity of the shot
        velocity = direction * PLAYER_SHOOT_SPEED

        # Create the shot using its position and velocity
        shot = Shot(self.position.x, self.position.y, velocity)

        
class Shot(CircleShape):
    def __init__(self, x, y,velocity):
        super().__init__(x, y,SHOT_RADIUS )
        self.velocity = velocity
    def update(self, dt):
        self.position += self.velocity *dt

    def draw(self, screen):
        pygame.draw.circle(screen, "red", (int(self.position.x), int(self.position.y)), self.radius)