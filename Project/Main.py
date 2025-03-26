#imports
from pygame import MOUSEBUTTONDOWN

from Functions import *
import time, random, sys, pygame
from Tasks import *


#config
pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Hells_Kitchen')
title_bg = pygame.image.load("images/title_bg.jpg").convert()
game_bg = pygame.image.load("images/game_bg.png").convert()
cookingpot_lid_right = pygame.image.load("images/cookingpot_lid_right.png").convert_alpha()
cookingpot_lid_left = pygame.image.load("images/cookingpot_lid_left.png").convert_alpha()
plate = pygame.image.load("images/plate.png").convert_alpha()
game_icon = pygame.image.load("images/gordon.png").convert_alpha()
pygame.display.set_icon(game_icon)

start_game = False
gameOver = False
running = True

GRAY = (180,180,180)
BLACK = (0,0,0)
GREEN = (0, 255, 0)
WHITE = (255,255,255)
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
FRAMERATE = 30

clock = pygame.time.Clock()

#Menubutton
menu_font = pygame.font.SysFont('Arial', 40)
menu_button_width, menu_button_height = 200, 80
menu_button_x, menu_button_y = (WIDTH - menu_button_width) // 2, (HEIGHT - menu_button_height) // 2 + 200
button_rect = pygame.Rect(menu_button_x, menu_button_y, menu_button_width, menu_button_height)
text_surface = menu_font.render("START", True, BLACK)
text_rect = text_surface.get_rect(center=button_rect.center)

#HIGHSCORETEXT
score_font = pygame.font.SysFont("Arial", 20, bold=True)
score_width = 150
score_height = 30
score_x = WIDTH - score_width //2 - 95
score_y = HEIGHT - score_height//2 - 400


def scoreRender(score, x, y, width, height, alpha=0):
    # Create transparent surface
    transparent_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    transparent_surface.fill((255, 255, 255, alpha))  # Last value is Alpha (0 = Fully Transparent, 255 = Fully Opaque)
    # Create the text surface
    high_score_surface = score_font.render(f"SCORE: {round(score, 0)}", True, WHITE)
    # Get text rectangle and center it in hs_rect
    hs_text_rect = high_score_surface.get_rect(center=(width // 2, height // 2))
    # Blit the text onto the transparent surface
    transparent_surface.blit(high_score_surface, hs_text_rect)
    # blit text to main screen
    screen.blit(transparent_surface, (x, y))

"""def scoreRendernum(score, x, y, width, height, alpha=0):
    # Create transparent surface
    transparent_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    transparent_surface.fill((255, 255, 255, alpha))  # Last value is Alpha (0 = Fully Transparent, 255 = Fully Opaque)
    # Create the text surface
    high_score_surface = score_font.render(f"SCORE: {round(score, 0)}", True, WHITE)
    # Get text rectangle and center it in hs_rect
    hs_text_rect = high_score_surface.get_rect(center=(width // 2, height // 2))
    # Blit the text onto the transparent surface
    transparent_surface.blit(high_score_surface, hs_text_rect)
    # blit text to main screen
    screen.blit(transparent_surface, (x, y))"""

#keystroke definitions
key_list = ["K_a", "K_b", "K_c", "K_d","K_e", "K_f", "K_g", "K_h","K_i", "K_j", "K_k", "K_l", "K_m", "K_n", "K_o", "K_p", "K_q", "K_r","K_s","K_t", "K_u","K_v","K_w", "K_x", "K_y", "K_z"]
used_list = ["K_a","K_a","K_a"]

#controlsinfo buttons
info_font = pygame.font.SysFont("Arial", 30, bold=True)
SIDELENGTH = 25


# Play Again Button
play_again_font = pygame.font.SysFont('Arial', 35)
pa_button_width, pa_button_height = 200, 80
pa_button_x, pa_button_y = (WIDTH - pa_button_width) // 2, (HEIGHT - pa_button_height) // 2 - 200
play_again_rect = pygame.Rect(pa_button_x, pa_button_y, pa_button_width, pa_button_height)
pa_text_surface = play_again_font.render("PLAY AGAIN?", True, BLACK)
pa_text_rect = pa_text_surface.get_rect(center=play_again_rect.center)

def gameOver():
    global running
    global start_game
    gameOver = True
    start_game = False
    #render play again button
    Cooking_pot.progress = 0
    while gameOver == True:
        screen.blit(title_bg, (0, 0))
        pygame.draw.rect(screen, GRAY, play_again_rect)
        screen.blit(pa_text_surface, pa_text_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(event.pos):
                    gameOver = False
                    print("Hello")
            else:
                pass
    return

cooking_pot_x, cooking_pot_y = (WIDTH - 50) // 2 + 250, (HEIGHT - 40) // 2
Cooking_pot = CooPot(0, "K_a", screen, key_list, used_list, info_font)

print(Cooking_pot.key, used_list)


#cooking pot button
CP_info_surface = info_font.render(Cooking_pot.key[2], True, (255, 255, 255))
CP_info_button_x, CP_info_button_y = (WIDTH - SIDELENGTH) // 2 + 400, (HEIGHT - SIDELENGTH) // 2 + 250
print(CP_info_button_x, CP_info_button_y)

#tea pot button
#TP_info_surface = info_font.render(tea_pot_key[2], True, (255, 255, 255))
#TP_info_button_x, TP_info_button_y = (WIDTH - info_button_width) // 2 + 400, (HEIGHT - info_button_height) // 2 + 250


#game loop
while running:
    score = 0
    screen.blit(title_bg, (0, 0))
    pygame.draw.rect(screen, GRAY, button_rect)
    screen.blit(text_surface, text_rect)
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
        screen.blit(game_bg, (0, 0))
        #render score
        scoreRender(score, score_x, score_y, score_width, score_height)
        #render buttons
        CooPot.controlInfo(Cooking_pot, 25)
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
            gameOver()
        else:
            Cooking_pot.pBarUpdate()
            Cooking_pot.animate(cookingpot_lid_left, cookingpot_lid_right)
        pygame.display.update()
        clock.tick(FRAMERATE)

pygame.quit()