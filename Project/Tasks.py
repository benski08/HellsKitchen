import pygame
from Functions import *
class Task:
    def __init__(self, progress, key, screen, key_list, used_list, info_font):
        self.font = info_font
        self.screen = screen
        self.used_list = used_list
        self.key_list = key_list
        self.HEIGHT = screen.get_height()
        self.WIDTH = screen.get_width()
        self.progress = progress
        self.key = key
        self.BLACK = (0,0,0)
        return
    def randomKey(self, previous_letter):
        import random
        n = 0
        for item in self.used_list:
            if item == previous_letter:
                self.used_list.pop(n)
                n += 1
        index = random.randint(0, 25)
        self.key = self.key_list[index]
        self.used_list.append(self.key)
        return self.key, self.used_list
    def calculateScore(self):
        self.MINSCORE = 0
        self.MAXSCORE = 100
        self.score = (self.MAXSCORE/100) * self.progress
        return self.score
    def controlInfo(self, side_length, x, y, alpha=0):
        self.side_length = side_length
        self.surface = self.font.render(self.key[2], True, (255, 255, 255))
        self.cix = x
        self.ciy = y
        self.cI_rect = pygame.Rect(x, y, side_length, side_length)
        self.text_rect = self.surface.get_rect(center=self.cI_rect.center)
        pygame.draw.rect(self.screen, self.BLACK, self.cI_rect)
        self.screen.blit(self.surface, self.text_rect)

class CooPot(Task):
    import pygame
    def __init__(self, progress, key, screen, key_list, used_list, info_font):
        super().__init__(progress, key, screen, key_list, used_list, info_font)
        self.toggle_lid = True
        self.frame_counter = 0
        self.pbarx = (self.screen.get_width() - 80) // 2 + 241
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
        self.pygame.display.update()
    def interact(self):
        self.progress = 0
        self.randomKey(self.key)
        #score
    def pBarUpdate(self, difficulty):
        self.difficulty = difficulty
        self.MAXTIME = 5
        self.pbarMAXWIDTH = 80
        self.pbarHEIGHT = 10
        self.pbarWIDTH = self.pbarMAXWIDTH/100 * self.progress
        self.XDISPLACEMENT = self.pbarWIDTH/2
        self.p_bar_rect = pygame.Rect(self.pbarx - self.XDISPLACEMENT,self.pbary, self.pbarWIDTH, self.pbarHEIGHT)
        self.COLOR = (self.progress/100 * 255, (1-self.progress/100)*255,0)
        pygame.draw.rect(self.screen, self.COLOR, self.p_bar_rect)
        self.progress += 100/(self.MAXTIME*30) * self.difficulty
        return self.progress
class Dishes():
    pass