from Functions import *
import time, random, sys, pygame
from images import *

configuration
pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Hells_Kitchen')
running = True
bg = pygame.image.load("images/bg.png")
gameOver = False
font = pygame.font.SysFont('Arial', 40)
objects = []


while running:
    screen.blit(bg, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
print("hello")
Hello()


