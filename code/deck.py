import random
import math
from cardInfo import *
from cardDraw import *
class Deck:
    def __init__(self,screen):
        self.cards = []
        self.discard_pile = []
        self.hand = []
        self.handDraw=[]
        self.CardX ,self.spacing=1000 ,200 #牌组的起始位置和间距
        self.init_deck()
        self.screen=screen
        self.played_card_indices=[] #已经打出的牌
    def init_hand(self):
        for i in range(4):
            self.hand.append(self.tackCard())
    def init_deck(self):
        # 初始化牌组
        for i in range(2):
            self.cards.append(Herb())
            self.cards.append(Stone())
            self.cards.append(Sand())
            self.cards.append(Fireball())
        self.shuffle()
    #从牌组中拿牌
    def tackCard(self):
        if len(self.cards) != 0:
            card = self.cards.pop(0)
            return card
        return None
    #起牌
    def tackHand(self):
        for i in self.played_card_indices:
            self.hand[i]=self.tackCard()
            card = self.hand[i]
            if card is not None :
                self.handDraw[i]=CardDraw(self.CardX+self.spacing*i, 1000,card.cardInfo)  
    #将手牌弃出
    def discardHand(self,card):
        self.discard_pile.append(card)
        self.hand[card]=None
        
    def shuffle(self):
        random.shuffle(self.cards)

    def HandDrawAdd(self):
        for i in range(len(self.hand)):
                card = self.hand[i]
                self.handDraw.append(CardDraw(self.CardX+self.spacing*i, 1000,card.cardInfo))

    def draw(self):
        for cardDraw in self.handDraw:
            if cardDraw is not None:
                cardDraw.draw(self.screen)

    def event(self, event):
        for i in range(len(self.handDraw)):
            cardDraw = self.handDraw[i]
            if cardDraw is not None:
                cardDraw.event(event)
