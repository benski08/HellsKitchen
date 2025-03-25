#imports
from pygame import MOUSEBUTTONDOWN

from Functions import *
import time, random, sys, pygame

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

#keystroke definitions
key_list = ["K_a", "K_b", "K_c", "K_d","K_e", "K_f", "K_g", "K_h","K_i", "K_j", "K_k", "K_l", "K_m", "K_n", "K_o", "K_p", "K_q", "K_r","K_s","K_t", "K_u","K_v","K_w", "K_x", "K_y", "K_z"]
used_list = ["K_a","K_a","K_a"]

#controlsinfo buttons
info_font = pygame.font.SysFont("Arial", 30, bold=True)
info_button_width, info_button_height = 40, 40

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
        self.MAXTIME = 5
        self.MAXWIDTH = 80
        self.HEIGHT = 20
        self.WIDTH = self.MAXWIDTH/100 * self.progress
        self.XDISPLACEMENT = self.WIDTH/2
        self.p_bar_rect = pygame.Rect(self.x - self.XDISPLACEMENT,self.y, self.WIDTH, self.HEIGHT)
        self.COLOR = (self.progress/100 * 255, (1-self.progress/100)*255,0)
        pygame.draw.rect(screen, self.COLOR, self.p_bar_rect)
        self.progress += 100/(self.MAXTIME*30)
        return self.progress

    def controlInfo(self,surface, x, y, side_length):
        self.surface = surface
        self.side_length = side_length
        self.x = x
        self.y = y
        self.cI_rect = pygame.Rect(x, y, side_length, side_length)
        self.text_rect = surface.get_rect(center=self.cI_rect.center)
        pygame.draw.rect(screen, BLACK, self.cI_rect)
        screen.blit(CP_info_surface, self.text_rect)
    pass
class CookingPot(Task):
    def __init__(self, x, y, progress, key):
        super().__init__(x, y, progress, key)
        self.toggle_lid = True
        self.frame_counter = 0
    def animate(self):
        self.min_frames = 5 #in frames
        self.max_frames = 30 #in frames
        self.switch_rate = int(self.max_frames - (self.progress / 100) * (self.max_frames - self.min_frames)) #calculate switchrate based on progress
        print(self.switch_rate)
        if self.frame_counter == self.switch_rate: #if the framecounter is high enough, it will switch states of lid
            self.toggle_lid = not self.toggle_lid
            self.frame_counter = 0
        if self.toggle_lid == True:
            screen.blit(cookingpot_lid_right, ((WIDTH - 50) // 2 + 182, (HEIGHT - 50) // 2 - 12))
        else:
            screen.blit(cookingpot_lid_left, ((WIDTH - 50) // 2 + 182, (HEIGHT - 50) // 2 - 12))
        self.frame_counter += 1



cooking_pot_x, cooking_pot_y = (WIDTH - 50) // 2 + 250, (HEIGHT - 40) // 2
Cooking_pot = CookingPot(cooking_pot_x, cooking_pot_y, 0, randomKey("K_a"))
tea_pot_key = randomKey("K_a")
trash_can_key = randomKey("K_a")
plates_key = randomKey("K_a")
print(Cooking_pot.key, used_list)


#cooking pot button
CP_info_surface = info_font.render(Cooking_pot.key[2], True, (255, 255, 255))
CP_info_button_x, CP_info_button_y = (WIDTH - info_button_width) // 2 + 400, (HEIGHT - info_button_height) // 2 + 250


#tea pot button
TP_info_surface = info_font.render(tea_pot_key[2], True, (255, 255, 255))
TP_info_button_x, TP_info_button_y = (WIDTH - info_button_width) // 2 + 320, (HEIGHT - info_button_height) // 2 + 250


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
        CookingPot.controlInfo(Cooking_pot, CP_info_surface, CP_info_button_x, CP_info_button_y, 40)
        screen.blit(plate, ((WIDTH - info_button_width) // 2 + 320, (HEIGHT - info_button_height) // 2 + 250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_game = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == getattr(pygame, Cooking_pot.key):
                    print("Cooking pot")
                    cooking_pot_interact()
                elif event.key == getattr(pygame, tea_pot_key):
                    print("Tea pot")
        if Cooking_pot.progress >= 100:
            gameOver()
        else:
            Cooking_pot.pBarUpdate()
            Cooking_pot.animate()
        pygame.display.update()
        clock.tick(FRAMERATE)

pygame.quit()