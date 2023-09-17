import pygame
import random

class Enemy:
    def __init__(self, hp, mp, rect, font, screen, image_path):
        self.text = None
        self.screen = screen
        self.font = font
        self.rect = rect
        self.speed = 3
        self.is_attacking = False
        self.image_path = "assets/Vanilla/3. Axe/Axe_0"
        self.cur_frame = 0
        self.cur_frameStr = str(self.cur_frame).zfill(2)
        self.image = pygame.image.load(self.image_path+self.cur_frameStr + ".png")
        self.image.set_colorkey((168, 208, 160))
        self.image = pygame.transform.scale(self.image, (self.rect.width * 4.5, self.rect.height * 3))
        self.rect_x=rect.x #敌人原来的位置
        self.rect_y=rect.y #敌人原来的位置
        self.attack_duration = 10
        self.attack_timer = 0
        self.animation_timer = 0
        self.isInjured = False
        self.injury_duration = 20  # 受伤的持续时间
        self.injury_timer = 0  # 受伤的计时器
        self.hp_rect = self.rect
        self.HpWidth = 100  # 血条宽度
        self.HpHeight = 10  # 血条高度
        self.max_health = hp  # 最大血量
        self.current_health = self.max_health  # 当前血量

    def attack(self):
        if not self.is_attacking:
            self.is_attacking = True
            self.attack_timer = self.attack_duration

    def injured(self):
        if not self.isInjured:
            self.isInjured = True
            self.injury_timer = self.injury_duration

    def update(self, FPS):
        if self.isInjured:
            self.image.set_alpha(0)  # 设置透明度为0
            self.injury_timer -= 1  # 计时器递减
            if self.injury_timer <= 0:  # 判断受伤时间是否结束
                self.isInjured = False
        else:
            self.image.set_alpha(255)  # 恢复完全不透明

        if self.is_attacking:
            self.animation_timer += 0.5
            self.attack_fps = 3
            if self.animation_timer == self.attack_fps:
                self.animation_timer = 0
                self.cur_frame += 1
                self.rect.x=300
                self.rect.y=270
                if self.cur_frame == 14:
                    self.cur_frame = 1
                    self.rect.x=self.rect_x
                    self.rect.y=self.rect_y
                    self.is_attacking = False
            self.cur_frameStr = str(self.cur_frame).zfill(2)
            self.image = pygame.image.load(self.image_path + str(self.cur_frameStr) + ".png")
            self.image = pygame.transform.scale(self.image, (self.rect.width * 4.5, self.rect.height * 3))
            self.image.set_colorkey((168, 208, 160))
            
    def draw(self):
        self.screen.blit(self.image, (self.rect.x-400,self.rect.y-200))
        health_cell_width = self.HpWidth / self.max_health
        # 绘制每个血格和分隔线
        for i in range(self.max_health):
            health_cell_x = self.hp_rect.x + i * health_cell_width
            
            # 根据当前血量决定血格的颜色
            cell_color = (255, 0, 0) if i < self.current_health else (255, 255, 255)
            
            # 绘制血格
            pygame.draw.rect(self.screen, cell_color, (health_cell_x+40, self.hp_rect.y-30, health_cell_width, self.HpHeight))
            
            # 绘制分隔线
            pygame.draw.rect(self.screen, (0, 0, 0), (health_cell_x+40, self.hp_rect.y-30, 1, self.HpHeight))
    def claw_attack(self, player):
        damage = random.randint(5, 10)
        player.current_health -= damage
        self.text = f"敌人对你使用了爪击，造成了{damage}点伤害"

    def tail_slap(self, player):
        damage = random.randint(8, 12)
        player.current_health -= damage
        self.text = f"敌人对你使用了甩尾，造成了{damage}点伤害"

    def spell(self, player):
        damage = random.randint(10, 15)
        player.current_health -= damage
        self.text = f"敌人释放了法术，造成了{damage}点伤害"

    def heal(self, player):
        heal_amount = random.randint(5, 10)
        self.current_health += heal_amount
        self.text = f"敌人使用法术，回复了{heal_amount}点血量"

    def action(self, player):
        actions = [self.claw_attack, self.tail_slap, self.spell, self.heal]
        action = random.choice(actions)
        action(player)
        return self.text
