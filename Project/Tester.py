#imports
from Functions import *
import time, random, sys, pygame
from images import *

#config
pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Hells_Kitchen')
title_bg = pygame.image.load("images/title_bg.jpg")
game_bg = pygame.image.load("images/game_bg.png")
cookingpot = pygame.image.load("images/cookingpot.jpg")
start_game = False
gameOver = False
running = True

GRAY = (180,180,180)
BLACK = (0,0,0)
GREEN = (0, 255, 0)
WIDTH = screen.get_width()
HEIGHT = screen.get_height()

#Menubutton
menu_font = pygame.font.SysFont('Arial', 40)
menu_button_width, menu_button_height = 200, 80
menu_button_x, menu_button_y = (WIDTH - menu_button_width) // 2, (HEIGHT - menu_button_height) // 2 + 200
button_rect = pygame.Rect(menu_button_x, menu_button_y, menu_button_width, menu_button_height)
text_surface = menu_font.render("START", True, BLACK)
text_rect = text_surface.get_rect(center=button_rect.center)

#keystroke definitions
key_list = ["K_a", "K_b", "K_c", "K_d","K_e", "K_f", "K_g", "K_h","K_i", "K_j", "K_k", "K_l", "K_m", "K_n", "K_o", "K_p", "K_q", "K_r","K_s","K_t", "K_u","K_v","K_w", "K_x", "K_y", "K_z"]
used_list = ["K_a","K_a","K_a"]


def randomKey(previous_letter):
    n = 0
    for item in used_list:
        if item == previous_letter:
            used_list.pop(n)
            n += 1
    index = random.randint(0, 25)
    key = key_list[index]
    used_list.append(key)
    return key

class Task:
    def __init__(self, x,y, progress, key):
        self.x = x
        self.y = y
        self.progress = progress
        self.key = key
        return
    def pBarUpdate(self):
        self.MAXWIDTH = 80
        self.HEIGHT = 20
        self.WIDTH = self.MAXWIDTH/100 * self.progress
        self.p_bar_rect = pygame.Rect(self.x,self.y, self.WIDTH, self.HEIGHT)
        pygame.draw.rect(screen, GREEN, self.p_bar_rect)
        self.progress += 5
        time.sleep(1)
    pass

cooking_pot_x, cooking_pot_y = (WIDTH - 50) // 2 + 250, (HEIGHT - 50) // 2
cooking_pot = Task(cooking_pot_x, cooking_pot_y, 0, randomKey("K_a"))
tea_pot_key = randomKey("K_a")
trash_can_key = randomKey("K_a")
print(cooking_pot.key, used_list)

#controlsinfo buttons
info_font = pygame.font.SysFont("Arial", 30, bold=True)
info_button_width, info_button_height = 40, 40

#cooking pot button
CP_info_surface = info_font.render(cooking_pot.key[2], True, (255, 255, 255))
CP_info_button_x, CP_info_button_y = (WIDTH - info_button_width) // 2 + 400, (HEIGHT - info_button_height) // 2 + 250
CP_button_rect = pygame.Rect(CP_info_button_x, CP_info_button_y, info_button_width, info_button_height)
CP_text_rect = CP_info_surface.get_rect(center=CP_button_rect.center)


#cooking pot progress bar


#tea pot button
TP_info_surface = info_font.render(tea_pot_key[2], True, (255, 255, 255))
TP_info_button_x, TP_info_button_y = (WIDTH - info_button_width) // 2 + 320, (HEIGHT - info_button_height) // 2 + 250
TP_button_rect = pygame.Rect(TP_info_button_x, TP_info_button_y, info_button_width, info_button_height)
TP_text_rect = TP_info_surface.get_rect(center=TP_button_rect.center)

#game loop
while running:
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
        #render buttons
        pygame.draw.rect(screen, BLACK, CP_button_rect)
        screen.blit(CP_info_surface, CP_text_rect)
        pygame.draw.rect(screen, BLACK, TP_button_rect)
        screen.blit(TP_info_surface,TP_text_rect)
        screen.blit(cookingpot, (450, 300))
        cooking_pot.pBarUpdate()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_game = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == getattr(pygame, cooking_pot.key):
                    print("Cooking pot")
                    cooking_pot_interact()
                elif event.key == getattr(pygame, tea_pot_key):
                    print("Tea pot")
        pygame.display.update()

pygame.quit()