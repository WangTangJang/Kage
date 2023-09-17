import time
import pygame
import sys
from gameInit import *


class Game:
    def __init__(self, screen_width, screen_height, caption):
        # 初始化游戏的各项数据
        self.gameInit = GameInit(screen_width, screen_height, caption)
        self.clock = pygame.time.Clock()

    def run(self):
        FPS = 60
        while True:
            pygame.display.flip()
            self.event()
            self.update(FPS)
            self.clock.tick(FPS)  # 最多每秒执行FPS次这个函数
            self.draw()
            self.turn()

    def event(self):
        for event in pygame.event.get():
            # 退出游戏检测
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 出牌事件检测
            self.gameInit.playCardButton.event(event)
            # 跳过事件检测
            self.gameInit.skip_button.event(event, self.gameInit)
            # 卡牌是否被选中检测
            self.gameInit.deck.event(event)

    def update(self, FPS):
        self.gameInit.player.update(FPS)
        self.gameInit.enemy.update(FPS)
    def turn(self):
        # 如果是敌人的回合
        if self.gameInit.current_player == self.gameInit.enemy:
            self.gameInit.enemy.attack()  # 敌人切换至攻击状态
            enemy_text = self.gameInit.enemy.action(self.gameInit.player)  # 敌人行动
            self.gameInit.deck.tackHand()  # 起牌
            self.gameInit.deck.played_card_indices = []  # 将指向被打出的牌的索引清空
            self.gameInit.current_player = self.gameInit.player  # 轮到玩家行动
            self.gameInit.player.current_mp = 5  # 回复MP
            self.gameInit.battleInfo.add_battle_info(enemy_text)  # 增加战斗信息
    def draw(self):
        # 加载背景
        self.gameInit.background.draw()

        # 加入主角
        if self.gameInit.player.current_health > 0:
            self.gameInit.player.draw()
        # 加入敌人
        if self.gameInit.enemy.current_health > 0:
            self.gameInit.enemy.draw()
        # 绘制牌组
        self.gameInit.deck.draw()
        # 战斗文本
        self.gameInit.battleInfo.draw()
        # 卡牌剩余信息
        self.gameInit.cardRemainingInfo.draw()
        # 按钮绘制
        self.gameInit.playCardButton.draw()
        self.gameInit.skip_button.draw()
        
if __name__ == "__main__":
    game = Game(1100, 600, "My Pygame Window")
    game.run()
