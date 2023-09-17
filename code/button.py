import pygame

class PlayCardButton(pygame.sprite.Sprite):
    def __init__(self, screen, font,gameInit):
        self.screen = screen
        self.font=font
        self.image = pygame.image.load("assets/buttonRelease.png")
        self.imagePressed = pygame.image.load("assets/buttonPress.png")
        self.image = pygame.transform.scale(self.image, (120, 100))
        self.imagePressed = pygame.transform.scale(self.imagePressed, (120, 100))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.screen.get_width() - 130, self.screen.get_height() - 130)
        self.text = "施放"
        self.text_color = (255, 255, 255)
        self.text_rect = self.font.render(self.text, True, self.text_color).get_rect()
        self.text_offset = 0

        self.is_pressed = False
        
        self.deck=gameInit.deck
        self.player=gameInit.player
        self.enemy=gameInit.enemy
        self.battleInfo=gameInit.battleInfo
    def event(self, event):
        #按钮的动画效果
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.is_pressed = True
            self.text_offset = 6
        elif event.type == pygame.MOUSEBUTTONUP and self.is_pressed and self.rect.collidepoint(event.pos):
            
            # 执行按钮点击后的操作
            self.is_pressed = False
            self.text_offset = 0
            current_mpSum=0
            cout=0
            #循环当前手牌
            i = 0
            for i in range(len(self.deck.handDraw)):
                if(self.deck.handDraw[i]!=None):
                    #若有手牌被选中
                    if(self.deck.handDraw[i].Selected==True):
                        #计算消耗量
                        cout+=1
                        if self.deck.hand[i]!=None:
                            current_mpSum=self.deck.hand[i].consume
            #若消耗量足够
            if current_mpSum<=self.player.current_mp and cout==1:
                #遍历手牌
                i = 0
                for i in range(len(self.deck.handDraw)):
                    if(self.deck.handDraw[i]!=None):
                        
                        #让被选中的手牌
                        if self.deck.handDraw[i].Selected==True:
                            if self.deck.hand[i]!=None:
                                self.deck.hand[i].use(self.player,self.enemy)
                                #使用卡牌后从手牌中移除
                                self.battleInfo.add_battle_info(self.deck.hand[i].effectText)
                                self.deck.played_card_indices.append(i)
                                self.deck.discardHand(i)
                                self.deck.handDraw[i]=None
                                break
                            
                self.player.acttack()
                self.enemy.injured()
            else:
                if cout>1:
                    self.battleInfo.add_battle_info("一次只可出一张牌哟")  
                elif current_mpSum>self.player.current_mp and current_mpSum:
                    self.battleInfo.add_battle_info("体力不足") 
        
    def draw(self):
        self.text_rect.center = self.rect.center
        self.text_rect.y += self.text_offset
        #被按下时将切换图片
        if self.is_pressed:
            self.screen.blit(self.imagePressed, self.rect)
        else:
            self.screen.blit(self.image, self.rect)
        self.screen.blit(self.font.render(self.text, True, self.text_color), self.text_rect)
class SkipButton(pygame.sprite.Sprite):
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        #按钮的图像
        self.image = pygame.image.load("assets/buttonRelease.png")
        self.imagePressed = pygame.image.load("assets/buttonPress.png")
        self.image = pygame.transform.scale(self.image, (120, 100))
        self.imagePressed = pygame.transform.scale(self.imagePressed, (120, 100))
        #按钮的位置
        self.image_rect = self.image.get_rect()
        self.image_rect.bottomleft = (self.screen.get_width() - 130, self.screen.get_height() - 50)
        #按钮上的字
        self.text = "跳过"
        self.text_color = (255, 255, 255)
        self.text_rect = self.font.render(self.text, True, self.text_color).get_rect()
        
        self.is_pressed = False #是否被按下
        self.text_offset = 0 #文字偏移量---为了与按钮的图像协调
    def event(self, event,gameInit):
        #按钮的动画效果
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.image_rect.collidepoint(event.pos):
                self.is_pressed = True
                self.text_offset = 6
        #切换回合的功能    
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.is_pressed and self.image_rect.collidepoint(event.pos):
                self.is_pressed = False
                self.text_offset = 0
                gameInit.current_player=gameInit.enemy
    def draw(self):

        self.text_rect.center = self.image_rect.center
        self.text_rect.y += self.text_offset
        #被按下时将切换图片
        if self.is_pressed:
            self.screen.blit(self.imagePressed, self.image_rect)
        else:
            self.screen.blit(self.image, self.image_rect)

        self.screen.blit(self.font.render(self.text, True, self.text_color), self.text_rect)