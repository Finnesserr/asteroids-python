import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        if radius <= 50:
            self.image = pygame.image.load("assets/asteroid50.png")
        elif radius <= 100:
            self.image = pygame.image.load("assets/asteroid100.png")
        else:
            self.image = pygame.image.load("assets/asteroid150.png")
        self.rect = self.image.get_rect(center=(int(x), int(y)))

    def draw(self, screen):
        self.rect.center = (int(self.position.x), int(self.position.y))
        screen.blit(self.image, self.rect)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)

            sm_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            sm_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)

            sm_asteroid_1.velocity = self.velocity.rotate(angle) * 1.2
            sm_asteroid_2.velocity = self.velocity.rotate(-angle) * 1.2

            sm_asteroid_1.add(*Asteroid.containers)
            sm_asteroid_2.add(*Asteroid.containers)
