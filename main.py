# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
   
    # Initialize Pygame
   
    pygame.init()
   
    # Create the game window
   
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create a clock & delta time object to manage the frame rate
   
    clock = pygame.time.Clock()
    dt = 0

    # Main game loop
    # This loop will run until the user closes the window
    # or the game ends
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()
       
        # Limit the frame rate to 60 FPS and get delta time in seconds
       
        dt = clock.tick(60) / 1000  

if __name__ == "__main__":
    main()
