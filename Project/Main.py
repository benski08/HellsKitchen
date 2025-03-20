#imports
from Functions import *
import time, random, sys, pygame
from images import *

#config
pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Hells_Kitchen')
running = True
bg = pygame.image.load("images/bg.png")
start_game = False
gameOver = False
font = pygame.font.SysFont('Arial', 40)
objects = []


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



