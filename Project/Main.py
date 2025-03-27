#imports
from pygame import MOUSEBUTTONDOWN
from Functions import *
import time, random, sys, pygame, math
from Tasks import *
print("Imports Successful!")

#config
pygame.init()
#assets
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Hell´s Kitchen')
title_bg = pygame.image.load("images/title_bg.jpg").convert()
game_bg = pygame.image.load("images/game_bg.png").convert()
cookingpot_lid_right = pygame.image.load("images/cookingpot_lid_right.png").convert_alpha()
cookingpot_lid_left = pygame.image.load("images/cookingpot_lid_left.png").convert_alpha()
plate = pygame.image.load("images/plate.png").convert_alpha()
game_icon = pygame.image.load("images/gordon.png").convert_alpha()
randomthingy = pygame.image.load("images/key-removebg-preview.png")
pygame.display.set_icon(game_icon)

start_game = False
game_over = False
running = True

GRAY = (180,180,180)
BLACK = (0,0,0)
GREEN = (0, 255, 0)
WHITE = (255,255,255)
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
FRAMERATE = 30
MIN_DIFFICULTY = 1
MAX_DIFFICULTY = 5
DIFF_SCALING = 0.5


clock = pygame.time.Clock()

#Menubutton
menu_font = pygame.font.SysFont('Arial', 40)
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
info_font = pygame.font.SysFont("Arial", 30, bold=True)
cooking_pot_x, cooking_pot_y = (WIDTH - 50) // 2 + 250, (HEIGHT - 40) // 2
Cooking_pot = CooPot(0, "K_a", screen, key_list, used_list, info_font)
#cooking pot button
SIDELENGTH = 25
CP_info_surface = info_font.render(Cooking_pot.key[2], True, (255, 255, 255))
CP_info_button_x, CP_info_button_y = Cooking_pot.pbarx - (SIDELENGTH//2),Cooking_pot.pbary + 15




# Play Again Button
play_again_font = pygame.font.SysFont('Arial', 35)
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
    #update high score
    if score > readHighScore():
        writeHighScore(score)
    high_score = readHighScore()
    #render play again button
    Cooking_pot.progress = 0
    while game_over == True:
        screen.blit(title_bg, (0, 0))
        pygame.draw.rect(screen, GRAY, play_again_rect)
        screen.blit(pa_text_surface, pa_text_rect)
        highScoreText(screen, HS_TEXT_X, HS_TEXT_Y, HS_TEXT_WIDTH, HS_TEXT_HEIGHT, WHITE)
        highScoreNum(high_score, screen, HS_NUM_X, HS_NUM_Y, HS_NUM_WIDTH, HS_NUM_HEIGHT, WHITE)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(event.pos):
                    game_over = False
                    print("Hello")
            else:
                pass
    return


#tea pot button
#TP_info_surface = info_font.render(tea_pot_key[2], True, (255, 255, 255))
#TP_info_button_x, TP_info_button_y = (WIDTH - info_button_width) // 2 + 400, (HEIGHT - info_button_height) // 2 + 250


#game loop
while running:
    score = 0
    screen.blit(title_bg, (0, 0))
    pygame.draw.rect(screen, GRAY, button_rect)
    screen.blit(text_surface, text_rect)
    screen.blit(randomthingy, (450, 300))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                #game start
                screen.blit(game_bg, (0, 0))
                start_game = True

    while start_game: #once start button is pressed
        #calculate difficulty
        difficulty_multiplier = calculateDifficulty(score, MIN_DIFFICULTY, MAX_DIFFICULTY, DIFF_SCALING)
        screen.blit(game_bg, (0, 0))
        #render score
        scoreRenderText(screen, SCORE_TEXT_X, SCORE_TEXT_Y, SCORE_TEXT_WIDTH, SCORE_TEXT_HEIGHT, WHITE)
        scoreRenderNum(screen, score, SCORE_NUM_X, SCORE_NUM_Y, SCORE_NUM_WIDTH, SCORE_NUM_HEIGHT, WHITE)
        #render buttons
        CooPot.controlInfo(Cooking_pot, SIDELENGTH, CP_info_button_x, CP_info_button_y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_game = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == getattr(pygame, Cooking_pot.key):
                    print("Cooking pot")
                    score += Cooking_pot.calculateScore()
                    Cooking_pot.interact()
                #elif event.key == getattr(pygame, tea_pot_key):
                    #print("Tea pot")
        if Cooking_pot.progress >= 100:
            print(score)
            gameOver(score)
        else:
            Cooking_pot.pBarUpdate(difficulty_multiplier)
            Cooking_pot.animate(cookingpot_lid_left, cookingpot_lid_right)
        pygame.display.update()
        clock.tick(FRAMERATE)

pygame.quit()