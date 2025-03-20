#imports
from Functions import *
import time, random, sys, pygame
from images import *

#config
pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Hells_Kitchen')
bg = pygame.image.load("images/bg.png")
start_game = False
gameOver = False
running = True

start_button_color = (255,255,255)
font = pygame.font.SysFont('Arial', 40)
start_button_text = font.render("START", True, start_button_color)



#game loop
while running:
    screen.blit(bg, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    while start_game: #once start button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

pygame.quit()



