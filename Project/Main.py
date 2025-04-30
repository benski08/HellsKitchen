#imports
from pygame import MOUSEBUTTONDOWN, K_ESCAPE
from Functions import *
import time, random, sys, pygame, math
from Tasks import *
print("Imports Successful!")

#config
pygame.init()
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN])

#assets
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Hell´s Kitchen')
title_bg = pygame.image.load("assets/title_bg2.png").convert()
game_over_bg = pygame.image.load("assets/endscreen.png").convert()
game_bg = pygame.image.load("assets/game_bg.png").convert()
game_bg_rendered = False
cookingpot_lid_right = pygame.image.load("assets/cookingpot_lid_right.png").convert_alpha()
cookingpot_lid_left = pygame.image.load("assets/cookingpot_lid_left.png").convert_alpha()
plate = pygame.image.load("assets/plate.png").convert_alpha()
game_icon = pygame.image.load("assets/gordon.png").convert_alpha()
key_bg = pygame.image.load("assets/key_fixed-removebg-preview.png").convert_alpha()
pygame.display.set_icon(game_icon)
kettle_sound = pygame.mixer.Sound("assets/Whistling Kettle.mp3")
bg_music = pygame.mixer.Sound("assets/bgmusic.mp3")
explosion = pygame.mixer.Sound("assets/explosion.mp3")

start_game = False
game_over = False
running = True

GRAY = (180,180,180)
BLACK = (0,0,0)
GREEN = (0, 255, 0)
WHITE = (255,255,255)
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
FRAMERATE = 15
MIN_DIFFICULTY = 0.5
MAX_DIFFICULTY = 2
DIFF_SCALING = 0.5

clock = pygame.time.Clock()

INFOKEY_WIDTH = 75
INFOKEY_HEIGHT = int(INFOKEY_WIDTH / 1.776)
#resize if necessary
key_bg = pygame.transform.scale(key_bg, (INFOKEY_WIDTH, INFOKEY_HEIGHT))
title_bg = pygame.transform.scale(title_bg, (WIDTH, HEIGHT))
game_over_bg = pygame.transform.scale(game_over_bg, (WIDTH,HEIGHT))

#Menubutton
menu_font = pygame.font.SysFont('Comic Sans MS', 40)
menu_button_width, menu_button_height = 200, 80
menu_button_x, menu_button_y = (WIDTH - menu_button_width) // 2, (HEIGHT - menu_button_height) // 2 + 200
button_rect = pygame.Rect(menu_button_x, menu_button_y, menu_button_width, menu_button_height)
text_surface = menu_font.render("START", True, BLACK)
text_rect = text_surface.get_rect(center=button_rect.center)

# SCORETEXT
SCORE_TEXT_WIDTH = 150
SCORE_TEXT_HEIGHT = 30
SCORE_TEXT_X = WIDTH - SCORE_TEXT_WIDTH // 2 - 95
SCORE_TEXT_Y = HEIGHT - SCORE_TEXT_HEIGHT // 2 - 400

# SCORENUMBER
SCORE_NUM_WIDTH = 150
SCORE_NUM_HEIGHT = 30
SCORE_NUM_X = WIDTH - SCORE_NUM_WIDTH // 2 - 95
SCORE_NUM_Y = HEIGHT - SCORE_NUM_HEIGHT // 2 - 370

# HIGHSCORETEXT
HS_TEXT_WIDTH = 350
HS_TEXT_HEIGHT = 200
HS_TEXT_X = (WIDTH - HS_TEXT_WIDTH // 2) - 450
HS_TEXT_Y = (HEIGHT - HS_TEXT_HEIGHT // 2) - 350

# HIGHSCORENUMBER
HS_NUM_WIDTH = 350
HS_NUM_HEIGHT = 200
HS_NUM_X = (WIDTH - HS_TEXT_WIDTH // 2) - 450
HS_NUM_Y = (HEIGHT - HS_TEXT_HEIGHT // 2) - 300

#keystroke definitions
key_list = ["K_a", "K_b", "K_c", "K_d","K_e", "K_f", "K_g", "K_h","K_i", "K_j", "K_k", "K_l", "K_m", "K_n", "K_o", "K_p", "K_q", "K_r","K_s","K_t", "K_u","K_v","K_w", "K_x", "K_y", "K_z"]
used_list = ["K_a","K_a","K_a"]

#initialize cooking_pot
info_font = pygame.font.SysFont("Comic Sans MS", 28, bold=True)
cooking_pot_x, cooking_pot_y = (WIDTH - 50) // 2 + 250, (HEIGHT - 40) // 2
Cooking_pot = CooPot(0, "K_a", screen, key_list, used_list, info_font, 30)
#cooking pot button
SIDELENGTH = 25
CP_info_button_x, CP_info_button_y = Cooking_pot.pbarx - (SIDELENGTH//2),Cooking_pot.pbary + 12
print(CP_info_button_y, CP_info_button_x)
#initialize dishes
Dishes = Dishes(0, "K_a", screen, key_list, used_list, info_font, 30)

#initialize kettle
Kettle = Kettle(0, "K_a", screen, key_list, used_list, info_font, 30)




# Play Again Button
play_again_font = pygame.font.SysFont('Comic Sans MS', 35)
pa_button_width, pa_button_height = 200, 80
pa_button_x, pa_button_y = (WIDTH - pa_button_width) // 2, (HEIGHT - pa_button_height) // 2 - 200
play_again_rect = pygame.Rect(pa_button_x, pa_button_y, pa_button_width, pa_button_height)
pa_text_surface = play_again_font.render("PLAY AGAIN?", True, BLACK)
pa_text_rect = pa_text_surface.get_rect(center=play_again_rect.center)


def gameOver(score):
    global running
    global start_game
    global game_over
    game_over = True
    start_game = False
    Cooking_pot.progress = 0
    Dishes.progress = 0
    pygame.mixer.music.stop()
    explosion.play()
    #update high score
    if score > readHighScore():
        writeHighScore(score)
    high_score = readHighScore()
    while game_over == True:
        screen.blit(game_over_bg, (0, 0))
        pygame.draw.rect(screen, GRAY, play_again_rect)
        screen.blit(pa_text_surface, pa_text_rect)
        highScoreText(screen, HS_TEXT_X, HS_TEXT_Y, HS_TEXT_WIDTH, HS_TEXT_HEIGHT, WHITE)
        highScoreNum(high_score, screen, HS_NUM_X, HS_NUM_Y, HS_NUM_WIDTH, HS_NUM_HEIGHT, WHITE)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(event.pos):
                    game_over = False
                    print("Hello")
            else:
                pass
    return

#game loop
while running:
    score = 0
    prev_score = 0
    screen.blit(title_bg, (0, 0))
    pygame.draw.rect(screen, GRAY, button_rect)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    #initialize randomkeys
    Cooking_pot.interact(game_bg)
    Dishes.interact(game_bg)
    Kettle.interact(game_bg)
    Kettle.resetSound(kettle_sound)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                #game start
                screen.blit(game_bg, (0, 0))
                game_bg_rendered = True
                start_game = True
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    while start_game: #once start button is pressed
        game_over = False
        #calculate difficulty
        difficulty_multiplier = calculateDifficulty(score, MIN_DIFFICULTY, MAX_DIFFICULTY, DIFF_SCALING)
        if game_bg_rendered:
            screen.blit(game_bg, (0, 0))
            game_bg_rendered = True
        # render score
        scoreRenderText(screen, SCORE_TEXT_X, SCORE_TEXT_Y, SCORE_TEXT_WIDTH, SCORE_TEXT_HEIGHT, WHITE)
        scoreRenderNum(screen, score, SCORE_NUM_X, SCORE_NUM_Y, SCORE_NUM_WIDTH, SCORE_NUM_HEIGHT, WHITE)
        # render buttons
        CooPot.controlInfo(Cooking_pot, SIDELENGTH, CP_info_button_x, CP_info_button_y, key_bg, INFOKEY_WIDTH, INFOKEY_HEIGHT)
        Dishes.controlInfo(SIDELENGTH, 450, 275, key_bg, INFOKEY_WIDTH, INFOKEY_HEIGHT)
        Kettle.controlInfo(SIDELENGTH, 692, 240, key_bg, INFOKEY_WIDTH, INFOKEY_HEIGHT)
        # update Tasks
        # update Cookingpot
        Cooking_pot.pBarUpdate(difficulty_multiplier)
        Cooking_pot.animate(cookingpot_lid_left, cookingpot_lid_right)
        # update Dishes
        #Dishes.pBarUpdate(difficulty_multiplier)
        Dishes.animate(plate)
        Dishes.updateProgress(difficulty_multiplier)
        # update Kettle
        Kettle.updateProgress()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_game = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    start_game = False
                    running = False
                if event.key == getattr(pygame, Cooking_pot.key):
                    print("Cooking pot")
                    score += Cooking_pot.calculateScore()
                    Cooking_pot.interact(game_bg)
                if event.key == getattr(pygame, Dishes.key):
                    print("Dishes")
                    score += Dishes.calculateScore()
                    Dishes.interact(game_bg)
                if event.key == getattr(pygame,Kettle.key):
                    print("Kettle")
                    score += Kettle.calculateScore()
                    Kettle.resetSound(kettle_sound)
                    Kettle.interact(game_bg)
        #check if gameover criteria are met
        if Cooking_pot.progress >= 100 or Dishes.progress >= 100 or Kettle.progress >= 100:
            pygame.mixer.Channel(7).stop()
            game_over = True
            gameOver(score)

        elif not pygame.mixer.music.get_busy() and not game_over:
            pygame.mixer.music.load("assets/bgmusic.mp3")
            pygame.mixer.music.play()

        pygame.display.update()
        clock.tick(FRAMERATE)

pygame.quit()