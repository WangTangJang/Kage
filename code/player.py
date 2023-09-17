import pygame
from setFont import *

class Player:
    def __init__(self, hp, mp, rect, font, screen, path):
        font = Font()
        # 位置
        self.rect = rect
        self.font = font.font_25
        self.screen = screen
        # 攻击
        self.speed = 10
        self.is_attacking = False
        self.attack_duration = 10
        self.animation_timer = 0
        self.attack_timer = 0
        self.animation_fps = 10 
        self.image_path = "assets/sage/Magic/Magic_0"
        self.cur_frame = 0
        self.cur_frameStr = str(self.cur_frame).zfill(2)
        self.image = pygame.image.load(self.image_path + str(self.cur_frameStr) + ".png")
        self.image.set_colorkey((168, 208, 160))
        self.image = pygame.transform.scale(self.image, (self.rect.width * 4.5, self.rect.height * 3))
        # 血条参数
        self.x = 10  # 血条左上角 x 坐标
        self.y = 10  # 血条左上角 y 坐标
        self.HpWidth = 300  # 血条宽度
        self.HpHeight = 20  # 血条高度
        self.max_health = hp  # 最大血量
        self.current_health = self.max_health  # 当前血量
        self.max_mp = mp  # 最大力气
        self.MpWidth = 100  # 力条宽度
        self.MpHeight = 20  # 力条高度
        self.current_mp = self.max_mp  # 当前力气

    def acttack(self):
        if not self.is_attacking:
            self.is_attacking = True
            self.attack_timer = self.attack_duration

    def update(self, FPS):
        if self.is_attacking:
            self.animation_timer += 0.5
            self.attack_fps = 3
            if self.animation_timer == self.attack_fps:
                self.animation_timer = 0
                self.cur_frame += 1
                if self.cur_frame == 19:
                    self.cur_frame = 1
                    self.is_attacking = False
            self.cur_frameStr = str(self.cur_frame).zfill(2)
            self.image = pygame.image.load(self.image_path + str(self.cur_frameStr) + ".png")
            self.image = pygame.transform.scale(self.image, (self.rect.width * 4.5, self.rect.height * 3))
            self.image.set_colorkey((168, 208, 160))

    def draw(self):
        self.screen.blit(pygame.transform.flip(self.image, True, False), self.rect)        
        # 计算每个血格和力气格的宽度
        health_cell_width = self.HpWidth / self.max_health
        mp_cell_width = self.MpWidth / self.max_mp
        
        # 绘制每个血格和分隔线
        for i in range(self.max_health):
            health_cell_x = self.x + i * health_cell_width
            
            # 根据当前血量决定血格的颜色
            cell_color = (255, 0, 0) if i < self.current_health else (255, 255, 255)
            
            # 绘制血格
            pygame.draw.rect(self.screen, cell_color, (health_cell_x, self.y, health_cell_width, self.HpHeight))
            
            # 绘制分隔线
            pygame.draw.rect(self.screen, (0, 0, 0), (health_cell_x, self.y, 1, self.HpHeight))
        
        # 绘制每个力气格和分隔线
        for i in range(self.max_mp):
            mp_cell_x = self.x + i * mp_cell_width
            
            # 根据当前力气决定力气格的颜色
            cell_color = (0, 0, 255) if i < self.current_mp else (255, 255, 255)
            
            # 绘制力气格
            pygame.draw.rect(self.screen, cell_color, (mp_cell_x, self.y + self.MpHeight + 5, mp_cell_width, self.MpHeight))
            
            # 绘制分隔线
            pygame.draw.rect(self.screen, (0, 0, 0), (mp_cell_x, self.y + self.MpHeight + 5, 1, self.MpHeight))
