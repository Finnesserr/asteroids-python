import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, rotation=0):
        super().__init__(x, y, SHOT_RADIUS)
        # Load and scale down the laserblast image
        original_image = pygame.image.load("assets/laserblast.png").convert_alpha()
        scale_factor = 0.05  # 50% size
        width = int(original_image.get_width() * scale_factor)
        height = int(original_image.get_height() * scale_factor)
        self.base_image = pygame.transform.smoothscale(original_image, (width, height))
        self.rotation = rotation
        self.image = pygame.transform.rotate(self.base_image, -self.rotation)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        # Rotate image to match direction
        self.image = pygame.transform.rotate(self.base_image, -self.rotation)
        self.rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, self.rect)

    def update(self, dt):
        self.position += self.velocity * dt