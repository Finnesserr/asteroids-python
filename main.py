# Import necessary modules
import pygame, sys
import os
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
from button import Button

 # Initialize Pygame
pygame.init()
sound_enabled = True
try:
    # Use recommended mixer settings for smoother music playback
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
except pygame.error:
    sound_enabled = False

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")

menuBG = pygame.image.load("assets/Background.png")
gameBG = pygame.image.load("assets/starbg.png")
asteroid50 = pygame.image.load("assets/asteroid50.png")
asteroid100 = pygame.image.load("assets/asteroid100.png")
asteroid150 = pygame.image.load("assets/asteroid150.png")

if sound_enabled:
    bullet_sound = pygame.mixer.Sound("sounds/shoot.wav")
    bang_large = pygame.mixer.Sound("sounds/bangLarge.wav")
    bang_small = pygame.mixer.Sound("sounds/bangSmall.wav")
    gameover_sound = pygame.mixer.Sound("sounds/gameover.wav")
    # Lower sound effect volumes
    bullet_sound.set_volume(0.2)
    bang_large.set_volume(0.2)
    bang_small.set_volume(0.2)
    gameover_sound.set_volume(0.2)
else:
    bullet_sound = None
    bang_large = None
    bang_small = None
    gameover_sound = None



def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)


def play():
    
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
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Create instances
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS, bullet_sound=bullet_sound)
    asteroid_field = AsteroidField()
   

    # Play background music if sound is enabled
    if sound_enabled:
        try:
            pygame.mixer.music.load("sounds/spacemusic.wav")
            # Only call play(-1) once, not in a loop
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.2)
            # If jitter persists, convert spacemusic.mp3 to WAV for best results
        except pygame.error:
            pass

    # Highscore file logic
    highscore_file = "highscore.txt"
    if os.path.exists(highscore_file):
        with open(highscore_file, "r") as f:
            try:
                highscore = int(f.read())
            except ValueError:
                highscore = 0
    else:
        highscore = 0

    # Main game loop
    gameover = False
    lives = 3
    score = 0

    while not gameover:
        screen.blit(gameBG, (0, 0))
        pygame.display.set_caption("Asteroids - FPS: " + str(int(clock.get_fps())))
        dt = clock.tick(60) / 1000

        font = get_font(18)
        livestext = font.render('Lives: ' + str(lives), True, (0, 255, 111))
        scoretext = font.render('Score: ' + str(score), True, (255, 255, 0))
        highscoretext = font.render('Highscore: ' + str(highscore), True, (255, 255, 255))

        

        for shape in drawable:
            shape.draw(screen)
        updatable.update(dt)

        screen.blit(livestext, (10, 10))
        screen.blit(scoretext, (550, 10))
        screen.blit(highscoretext, (1035, 10))

        for asteroid in asteroids:
            if player.collide(asteroid):
                lives -= 1
                asteroid.kill()
                if lives <= 0:
                    gameover = True
                    # Stop music on gameover
                    pygame.mixer.music.stop()
                    if gameover_sound:
                        gameover_sound.play()
                    break
            for shot in shots:
                if asteroid.collide(shot):
                    if asteroid.radius > ASTEROID_MIN_RADIUS:
                        if bang_large:
                            bang_large.play()
                    else:
                        if bang_small:
                            bang_small.play()
                    asteroid.split()
                    shot.kill()
                    score += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                    return

        pygame.display.update()
        pygame.display.flip()

    # Update highscore if needed
    if score > highscore:
        highscore = score
        with open(highscore_file, "w") as f:
            f.write(str(highscore))

    # Game Over Screen
    font = get_font(72)
    gameover_text = font.render('GAME OVER', True, (255, 0, 0))
    info_font = get_font(36)
    info_text = info_font.render('Press any key to return to menu', True, (255, 255, 255))
    final_score_text = info_font.render('Final Score: ' + str(score), True, (255, 255, 0))
    highscore_text = info_font.render('Highscore: ' + str(highscore), True, (255, 215, 0))
    while True:
        screen.fill((0, 0, 0))
        screen.blit(gameover_text, gameover_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 80)))
        screen.blit(final_score_text, final_score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)))
        screen.blit(highscore_text, highscore_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40)))
        screen.blit(info_text, info_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80)))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                main_menu()
                return

def Info_menu():
        # Play background music if sound is enabled
    if sound_enabled:
        try:
            pygame.mixer.music.load("sounds/menumusic.wav")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.2)
            # If jitter persists, convert menumusic.mp3 to WAV for best results
        except pygame.error:
            pass

    while True:
        screen.blit(menuBG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("KEYS", True, "#40b67f")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        INFO_TEXT = get_font(30).render("W - Move Forward", True, "White")
        INFO_RECT = INFO_TEXT.get_rect(center=(640, 175))
        INFO3_TEXT = get_font(30).render("A - Rotate Left", True, "White")
        INFO3_RECT = INFO3_TEXT.get_rect(center=(640, 225))
        INFO4_TEXT = get_font(30).render("D - Rotate Right", True, "White")
        INFO4_RECT = INFO4_TEXT.get_rect(center=(640, 275))
        INFO5_TEXT = get_font(30).render("SPACE - Shoot", True, "White")
        INFO5_RECT = INFO5_TEXT.get_rect(center=(640, 325))
        INFO6_TEXT = get_font(30).render("ESC - Quit", True, "White")
        INFO6_RECT = INFO6_TEXT.get_rect(center=(640, 375))
        # Show highscore from file
        highscore_file = "highscore.txt"
        if os.path.exists(highscore_file):
            with open(highscore_file, "r") as f:
                try:
                    highscore = int(f.read())
                except ValueError:
                    highscore = 0
        else:
            highscore = 0
        HIGH_SCORE_TEXT = get_font(30).render(f"Highscore: {highscore}", True, "Red")
        HIGH_SCORE_RECT = HIGH_SCORE_TEXT.get_rect(center=(640, 625))
        BACK_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 550), 
                            text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="Pink")

        screen.blit(MENU_TEXT, MENU_RECT,)
        screen.blit(INFO_TEXT, INFO_RECT)
        screen.blit(INFO3_TEXT, INFO3_RECT)
        screen.blit(INFO4_TEXT, INFO4_RECT)
        screen.blit(INFO5_TEXT, INFO5_RECT)
        screen.blit(INFO6_TEXT, INFO6_RECT)


        BACK_BUTTON.changeColor(MENU_MOUSE_POS)
        BACK_BUTTON.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return

        pygame.display.update()
def main_menu():
    # Stop any currently playing music before starting menu music
    pygame.mixer.music.stop()
    if sound_enabled:
        try:
            pygame.mixer.music.load("sounds/menumusic.wav")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.2)
            # If jitter persists, convert menumusic.mp3 to WAV for best results
        except pygame.error:
            pass
    while True:
        screen.blit(menuBG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Asteroids", True, "#40b67f")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Pink")
        INFO_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 400), 
                            text_input="INFO", font=get_font(75), base_color="#d7fcd4", hovering_color="Pink")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Pink")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, INFO_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if INFO_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Info_menu()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
