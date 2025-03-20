#imports
from Functions import *
import time, random, sys, pygame
from images import *

#config
pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Hells_Kitchen')
bg = pygame.image.load("images/bg_title.png")
start_game = False
gameOver = False
running = True

GRAY = (180,180,180)
BLACK = (0,0,0)


font = pygame.font.SysFont('Arial', 40)
WIDTH = screen.get_width()
HEIGHT = screen.get_height()

button_width, button_height = 200, 80
button_x, button_y = (WIDTH - button_width) // 2, (HEIGHT - button_height) // 2 + 200
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)


#game loop
while running:
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, GRAY, button_rect)
    text_surface = font.render("START", True, BLACK)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                start_game = True

    while start_game: #once start button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_game = False
                running = False
        pygame.display.update()

pygame.quit()



