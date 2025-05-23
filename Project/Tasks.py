import pygame
from Functions import *


#eigene klasse
class Task:
    def __init__(self, progress, key, screen, key_list, used_list, info_font, FRAMERATE, interact_sound):
        self.font = info_font
        self.screen = screen
        self.used_list = used_list
        self.key_list = key_list
        self.HEIGHT = screen.get_height()
        self.WIDTH = screen.get_width()
        self.progress = progress
        self.key = key
        self.BLACK = (0,0,0)
        self.interact_sound = interact_sound
        return
    def randomKey(self, previous_letter):
        import random
        loop = True
        while loop:
            loop = False
            index = random.randint(0, 25)
            self.key = self.key_list[index]
            for item in self.used_list:
                if self.key == item:
                    loop = True
        n=0
        for item in self.used_list:
            if item == previous_letter:
                self.used_list.pop(n)
                n += 1
        self.used_list.append(self.key)
        return self.key, self.used_list
    def calculateScore(self):
        self.MINSCORE = 0
        self.MAXSCORE = 100
        self.score = (self.MAXSCORE/100) * self.progress
        return self.score
    #ChatGPT hat die alpha blitting Funktion gemacht
    def controlInfo(self, side_length, x, y, image, image_width, image_height, alpha=0):
        self.side_length = side_length
        self.surface = self.font.render(self.key[2], True, (0,0,0))  # Render text

        # Create a transparent surface with per-pixel alpha
        transparent_surface = pygame.Surface((side_length, side_length), pygame.SRCALPHA)
        transparent_surface.fill((255, 255, 255, alpha))  # Set transparency

        # Center the text on the transparent surface
        text_rect = self.surface.get_rect(center=(side_length // 2, side_length // 2))
        transparent_surface.blit(self.surface, text_rect)  # Blit text onto transparent surface

        # Blit the image first
        self.screen.blit(image, (x-image_width/2 + 12, y - image_height/2 + 12))  # Use x, y for positioning the image

        # Then blit the transparent surface with text on top
        self.screen.blit(transparent_surface, (x, y-2))

        # Finally, re-blit the text to ensure it's on top
        self.screen.blit(self.surface, (x + (side_length - text_rect.width) // 2,
                                        y + (side_length - text_rect.height) // 2 - 2))

    def interact(self, game_bg):
        self.progress = 0
        self.randomKey(self.key)
        pygame.mixer.Channel(6).play(self.interact_sound)

class CooPot(Task):
    import pygame
    def __init__(self, progress, key, screen, key_list, used_list, info_font, FRAMERATE, interact_sound):
        super().__init__(progress, key, screen, key_list, used_list, info_font, FRAMERATE, interact_sound)
        self.toggle_lid = True
        self.frame_counter = 0
        self.MAXTIME = 5
        self.pbarMAXWIDTH = 80
        self.pbarHEIGHT = 10
        self.pbarx = (self.screen.get_width() - self.pbarMAXWIDTH) // 2 + 241
        self.pbary = (self.screen.get_height() - 70)// 2 - 37
        self.rlid_x = (self.screen.get_width() - 80) // 2 + 195
        self.rlid_y = (self.screen.get_height() - 70) // 2
        self.llid_x = (self.screen.get_width() - 80) // 2 + 195
        self.llid_y = (self.screen.get_height() - 61) // 2 - 10
    def animate(self, state_1, state_2):
        #pot lid animation
        self.state_1 = state_1
        self.state_2  = state_2
        self.min_frames = 1 #in frames
        self.max_frames = 10 #in frames
        self.switch_rate = int(self.max_frames - (self.progress / 100) * (self.max_frames - self.min_frames)) #calculate switchrate based on progress
        if self.state_1 is None or self.state_2 is None:
            print("Error: Images not loaded properly")
        if self.frame_counter >= self.switch_rate: #if the framecounter is high enough, it will switch states of lid
            self.toggle_lid = not self.toggle_lid
            self.frame_counter = 0
        if self.toggle_lid == True:
            self.screen.blit(self.state_2, (self.rlid_x, self.rlid_y))
        else:
            self.screen.blit(self.state_1, (self.llid_x, self.llid_y))
        self.frame_counter += 1
        #self.pygame.display.update()
    def pBarUpdate(self, difficulty):
        self.difficulty = difficulty
        self.pbarWIDTH = int(self.pbarMAXWIDTH/100 * self.progress)
        self.XDISPLACEMENT = self.pbarWIDTH/2
        self.p_bar_rect = pygame.Rect(self.pbarx - self.XDISPLACEMENT,self.pbary, self.pbarWIDTH, self.pbarHEIGHT)
        self.COLOR = (int(self.progress/100 * 255), int((1-self.progress/100)*255),0)
        pygame.draw.rect(self.screen, self.COLOR, self.p_bar_rect)
        self.progress += 100/(self.MAXTIME*30) * self.difficulty
        return self.progress
class Dishes(Task):
    import pygame
    def __init__(self, progress, key, screen, key_list, used_list, info_font, FRAMERATE, interact_sound):
        super().__init__(progress, key, screen, key_list, used_list, info_font, FRAMERATE, interact_sound)
        self.pbarMAXHEIGHT = 80
        self.pbarWIDTH = 10
        self.pbary = (self.HEIGHT - self.pbarMAXHEIGHT)//2
        self.pbarx = (self.WIDTH - self.pbarWIDTH)//2
        self.MAXTIME = 5

    def updateProgress(self, difficulty):
        self.progress += 100/(self.MAXTIME*30) * difficulty
        return self.progress

    def animate(self, plate):
        if self.progress >= 5:
            self.screen.blit(plate, (482, 283))
        if self.progress >= 15:
            self.screen.blit(plate, (482, 275))
        if self.progress >= 25:
            self.screen.blit(plate, (482, 267))
        if self.progress >= 35:
            self.screen.blit(plate, (482, 259))
        if self.progress >= 45:
            self.screen.blit(plate, (482, 251))
        if self.progress >= 55:
            self.screen.blit(plate, (552, 283))
        if self.progress >= 65:
            self.screen.blit(plate, (552, 275))
        if self.progress >= 75:
            self.screen.blit(plate, (552, 267))
        if self.progress >= 85:
            self.screen.blit(plate, (552, 259))
        if self.progress >= 95:
            self.screen.blit(plate, (552, 251))
        return
    pass

class Kettle(Task):
    def __init__(self, progress, key, screen, key_list, used_list, info_font, FRAMERATE, interact_sound):
        super().__init__(progress, key, screen, key_list, used_list, info_font, FRAMERATE, interact_sound)
        self.kettle_done = False
        self.MAXTIME = 41
        self.FRAMERATE = FRAMERATE
    def resetSound(self, kettle):
        pygame.mixer.Channel(7).stop()
        pygame.mixer.Channel(7).play(kettle)

    def updateProgress(self):
        self.progress += 100 / (self.MAXTIME * self.FRAMERATE)
class Trashcan(Task):
        def __init__(self, progress, key, screen, key_list, used_list, info_font, FRAMERATE, interact_sound):
            super().__init__(progress, key, screen, key_list, used_list, info_font, FRAMERATE, interact_sound)
            self.MAXTIME = 10
            self.FRAMERATE = FRAMERATE
        def updateProgress(self, difficulty):
            self.progress += 100 / (self.MAXTIME * self.FRAMERATE) * difficulty
            return self.progress

        def pBarUpdate(self, x, y, can0, can20, can40, can60, can80, can100):
            if self.progress < 15:
                self.screen.blit(can0, (x,y))
            elif self.progress >= 15 and self.progress < 35:
                self.screen.blit(can20, (x,y))
            elif self.progress >= 35 and self.progress < 55:
                self.screen.blit(can40, (x, y))
            elif self.progress >= 55 and self.progress < 75:
                self.screen.blit(can60, (x,y))
            elif self.progress >= 75 and self.progress < 95:
                self.screen.blit(can80, (x,y))
            elif self.progress >= 95:
                self.screen.blit(can100, (x,y))

