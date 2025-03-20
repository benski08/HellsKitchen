from Functions import *
import time, random, sys, pygame
from images import *

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Hells_Kitchen')
running = True
bg = pygame.image.load("images/bg.png")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg, (0,0))
    pygame.display.update()
pygame.quit()
print("hello")
Hello()


