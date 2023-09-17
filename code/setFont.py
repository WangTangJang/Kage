import pygame
class Font():
    def __init__(self):
        self.font_path = "font/Pixel.ttf"
        self.font_15 = pygame.font.Font(self.font_path, 15)
        self.font_20 = pygame.font.Font(self.font_path, 20)
        self.font_25 = pygame.font.Font(self.font_path, 25)
        self.font_30 = pygame.font.Font(self.font_path, 30)