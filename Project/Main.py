from Functions import *
import time
import random
import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 660))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
print("hello")
Hello()
