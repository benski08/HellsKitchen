import random, pygame

pygame.init()
score_font = pygame.font.SysFont("Comic Sans MS", 20, bold=True)
high_score_font = pygame.font.SysFont("Arial", 120, bold=True)

def scoreRenderText(screen, x, y, width, height, color, alpha=0):
    # Create transparent surface
    transparent_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    transparent_surface.fill((255, 255, 255, alpha))  # Last value is Alpha (0 = Fully Transparent, 255 = Fully Opaque)
    # Create the text surface
    score_text_surface = score_font.render("SCORE:", True, color)
    # Get text rectangle and center it in hs_rect
    score_text_rect = score_text_surface.get_rect(center=(width // 2, height // 2))
    # Blit the text onto the transparent surface
    transparent_surface.blit(score_text_surface, score_text_rect)
    # blit text to main screen
    screen.blit(transparent_surface, (x, y))

def scoreRenderNum(screen, score, x, y, width, height,color, alpha=0):
    # Create transparent surface
    transparent_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    transparent_surface.fill((255, 255, 255, alpha))  # Last value is Alpha (0 = Fully Transparent, 255 = Fully Opaque)
    # Create the text surface
    score_text_surface = score_font.render(f"{round(score)}", True, color)
    # Get text rectangle and center it in hs_rect
    score_text_rect = score_text_surface.get_rect(center=(width // 2, height // 2))
    # Blit the text onto the transparent surface
    transparent_surface.blit(score_text_surface, score_text_rect)
    # blit text to main screen
    screen.blit(transparent_surface, (x, y))

def highScoreText(screen, x, y, width, height, color, alpha=0):
    # Create transparent surface
    transparent_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    transparent_surface.fill((255, 255, 255, alpha)) # Last value is Alpha (0 = Fully Transparent, 255 = Fully Opaque)
    # Create the text surface
    score_text_surface = high_score_font.render("HIGHSCORE:", True, color)
    # Get text rectangle and center it in hs_rect
    score_text_rect = score_text_surface.get_rect(center=(width // 2, height // 2))
    # Blit the text onto the transparent surface
    transparent_surface.blit(score_text_surface, score_text_rect)
    # blit text to main screen
    screen.blit(transparent_surface, (x, y))

def highScoreNum(highscore, screen, x, y, width, height, color,alpha=0):
    # Create transparent surface
    transparent_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    transparent_surface.fill((255, 255, 255, alpha)) # Last value is Alpha (0 = Fully Transparent, 255 = Fully Opaque)
    # Create the text surface
    score_text_surface = high_score_font.render(f"{highscore}", True, color)
    # Get text rectangle and center it in hs_rect
    score_text_rect = score_text_surface.get_rect(center=(width // 2, height // 2))
    # Blit the text onto the transparent surface
    transparent_surface.blit(score_text_surface, score_text_rect)
    # blit text to main screen
    screen.blit(transparent_surface, (x, y))
def writeHighScore(score, filename="HIGHSCORE.txt"):
    with open(filename, "w") as file:
        file.write(f"{int(round(score,0))}")

def readHighScore(filename="HIGHSCORE.txt"):
    try:
        with open(filename, "r") as file:
            high_score = file.readline().strip()
            return int(high_score) if high_score else 0
    except FileNotFoundError:
        with open(filename, "w") as file:
            file.write("0")
        return 0