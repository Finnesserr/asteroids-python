# Import necessary modules
import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
   
    # Initialize Pygame
    pygame.init()
   
    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create a clock & delta time object to manage the frame rate 
    clock = pygame.time.Clock()
    dt = 0

    # Create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign instances to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create Player instance
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    # Create AsteroidField instance
    asteroid_field = AsteroidField()
    
    # Main game loop
    # This loop will run until the user closes the window
    # or the game ends 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Clear the screen with black
        screen.fill("black")
        # Limit the frame rate to 60 FPS and get delta time in seconds
        dt = clock.tick(60) / 1000
        # Update and draw game objects here
        for shape in drawable:
            shape.draw(screen)
        updatable.update(dt)
        
        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collide(asteroid):
                raise sys.exit("Game Over!")
        # Check for collisions between shots and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()


        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
