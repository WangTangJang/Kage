import pygame
# 背景设置
class Background():
    def __init__(self,screen):
        self.screen_width=screen.get_width()
        self.screen_height=screen.get_height()
        self.image_path = "assets/backgroud/bg.png"
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))
        self.screen = screen
    def draw(self):
        self.screen.blit(self.image, (0, 0))