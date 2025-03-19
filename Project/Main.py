from Functions import *
import time
import random
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Hells_Kitchen')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
print("hello")
Hello()


