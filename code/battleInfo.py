class BattleInfo:
    def __init__(self,font,screen):
        self.font = font
        self.battle_info = []
        self.screen = screen
        self.screen_width=screen.get_width()
        self.screen_height =screen.get_height()
    def add_battle_info(self, info_text):
        self.battle_info.append(info_text)
        if len(self.battle_info) > 4:
            self.battle_info.pop(0)
    def draw(self):
        #战斗信息显示
        for i, text in enumerate(self.battle_info):
            if i == len(self.battle_info) - 1:
                text_surface = self.font.render(text, True, (0, 255, 0))
            else:
                text_surface = self.font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.bottomleft = (20, self.screen_height - 20 - i * 30)
            self.screen.blit(text_surface, text_rect)
class CardRemainingInfo:
        def __init__(self,deck,font,screen):
            self.screen = screen
            self.deck = deck 
            self.font = font
        def draw(self):
            #卡牌剩余信息
            text = "剩余牌数:"+str(len(self.deck.cards))
            text_surface = self.font.render(text,True,(255,255,255))
            text_rect = text_surface.get_rect()
            text_rect.bottomleft = (self.screen.get_width()-160,self.screen.get_height())
            self.screen.blit(text_surface,text_rect)

