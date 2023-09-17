import pygame
from setFont import *
class CardDraw:
    def __init__(self, x, y,cardInfo):
        width=80
        heiht=120
        rect_x = x // 2 - width // 2
        rect_y = y // 2 - heiht // 2
        self.rect = pygame.Rect(rect_x, rect_y, width, heiht)
        self.normal_rect = self.rect
        self.highlighted_rect = pygame.Rect(self.rect.x - 20, self.rect.y - 20, 
                                    self.rect.width + 40, self.rect.height + 40)
        #卡牌名字字体 
        self.font =  Font()
        self.fontName = self.font.font_25
        #卡牌属性字体
        self.fontSkill = self.font.font_15
        #卡牌背景图
        self.image= pygame.image.load("assets/CardBackground.png")
        self.card = cardInfo
        #是否被选中
        self.Selected = False
    def event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if(self.Selected==False):
                self.Selected = True
                self.rect = self.highlighted_rect
                self.fontName = self.font.font_30
                self.fontSkill = self.font.font_20
            else:
                self.Selected = False
                self.rect = self.normal_rect
                self.fontName = self.font.font_25
                self.fontSkill = self.font.font_15
    def draw(self, screen):
        # 绘制背景图
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        screen.blit(self.image, self.rect)
        # 绘制卡牌名称
        self.draw_text(screen, self.card.name, self.fontName, (255,255,255), 
                    center=(self.rect.centerx, self.rect.centery + 30))
        # 绘制攻击力  
        if self.card.attack:
            self.draw_text(screen, f'攻击:{self.card.attack}', self.fontSkill, (255,0,0),
                        center=(self.rect.centerx, self.rect.centery - self.rect.height // 3))
        # 绘制回复量     
        if self.card.heal:
            self.draw_text(screen, f'回复:{self.card.heal}', self.fontSkill, (0,255,0),
                        center=(self.rect.centerx, self.rect.centery - self.rect.height // 3))   
        
        # 绘制消耗量
        self.draw_text(screen, f'耗力:{self.card.consume}', self.fontSkill, (0,0,255),
                    center=(self.rect.centerx, self.rect.centery - self.rect.height // 5))
        
    def draw_text(self, screen, text, font, color, center):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=center)
        screen.blit(text_surface, text_rect)
