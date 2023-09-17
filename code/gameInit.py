import pygame
from background import *
from enemy import *
from cardInfo import *
from deck import *
from battleInfo import *
from button import *
from cardDraw import *
from player import *
from setFont import *
class GameInit():
        def __init__(self,screen_width, screen_height, caption):
            pygame.init()
            # 窗口的初始化
            self.screen_width = screen_width
            self.screen_height = screen_height
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))  # 加载窗口
            pygame.display.set_caption(caption)  # 窗口的名字
            self.icon = pygame.image.load("assets/icon.jpg")  # 加载图片
            pygame.display.set_icon(self.icon)
            
            # 背景设置
            self.background = Background(self.screen)
            # 字体设置
            font = Font()
            self.font1 = font.font_25
            self.font2 = font.font_15
            #人物设置
            player_x=-100
            player_y=-50
            player_w=200
            player_h=250
            playerHealthPoints = 100
            playerMagicPoints = 10
            playerImagePath = "assets/sword.png"
            PlayerRect = pygame.Rect(player_x,player_y,player_w,player_h)
            self.player = Player(playerHealthPoints,playerMagicPoints,PlayerRect,self.font1,self.screen,playerImagePath)
            enemy_x=650
            enemy_y=230
            enemy_w=192
            enemy_h=192
            enemyHealthPoints=20
            enemyMagicPoints = 100
            enemyImagePath = "assets/ani02_192.gif"
            enemyRect = pygame.Rect(enemy_x,enemy_y,enemy_w,enemy_h)
            self.enemy = Enemy(enemyHealthPoints,enemyMagicPoints,enemyRect,self.font1,self.screen,enemyImagePath)
            #牌区设置
            self.deck= Deck(self.screen)
            self.deck.init_hand()
            self.handDraw=[] #卡牌组的手牌绘制
            self.CardX ,self.spacing=1000 ,250
            self.selected_card_index=[]
            self.deck.HandDrawAdd()
            #回合设置
            self.current_player = self.player  # 当前角色为玩家
            self.turn_number = 0  # 回合数为0
            #战斗信息设置
            self.battleInfo = BattleInfo(self.font2,self.screen)
            #卡牌剩余信息
            self.cardRemainingInfo =  CardRemainingInfo(self.deck,self.font1,self.screen)
            #按钮
            self.playCardButton = PlayCardButton(self.screen,self.font1,self)
            self.skip_button = SkipButton(self.screen,self.font1)