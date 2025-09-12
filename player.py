import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0  # in degrees
        self.shoot_cooldown = 0.0  # seconds
        raw_image = pygame.image.load("assets/spaceship.png").convert_alpha()
        size = int(radius * 3)
        self.image = pygame.transform.scale(raw_image, (size, size))
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        self.rect = rotated_image.get_rect(center=(self.position.x, self.position.y))
        screen.blit(rotated_image, self.rect)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        new_position = self.position + forward * PLAYER_SPEED * dt
        # Clamp to screen boundaries
        min_x = self.radius
        max_x = SCREEN_WIDTH - self.radius
        min_y = self.radius
        max_y = SCREEN_HEIGHT - self.radius
        new_x = max(min_x, min(new_position.x, max_x))
        new_y = max(min_y, min(new_position.y, max_y))
        self.position = pygame.Vector2(new_x, new_y)

    def shoot(self):
        if self.shoot_cooldown <= 0:
            shot = Shot(self.position.x, self.position.y, self.rotation)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        self.rect = rotated_image.get_rect(center=(self.position.x, self.position.y))
    
    def collide(self, other):
        shrink_factor = 0.75
        player_hitbox = self.rect.inflate(-self.rect.width * (1 - shrink_factor), -self.rect.height * (1 - shrink_factor))
        other_hitbox = other.rect.inflate(-other.rect.width * (1 - shrink_factor), -other.rect.height * (1 - shrink_factor))
        return player_hitbox.colliderect(other_hitbox)
    
    
    # Keybinds for movement
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()