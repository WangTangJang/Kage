import pygame
class CardInfo:
    def __init__(self,name,consume,color,attack,heal):
        self.name=name
        self.color = color
        self.consume = consume
        self.attack = attack  
        self.heal = heal
class Stone:
    def __init__(self):
        self.consume=2
        self.name="攻击"
        self.attack=4
        self.heal = None
        self.color=(136,173,166)
        self.effectText=f"你使用了{self.name}对敌人造成了{self.attack}伤害"
        self.cardInfo = CardInfo(self.name,self.consume,self.color,self.attack,self.heal)
    def use(self, player,enemy):
        enemy.current_health-=self.attack
        player.current_mp -= self.consume
class Sand:
    def __init__(self):
        self.consume=1
        self.name="雷击"
        self.attack=2
        self.heal = None
        self.color=(250,140,53)
        self.effectText=f"你使用了{self.name}对敌人造成了{self.attack}伤害"
        self.cardInfo = CardInfo(self.name,self.consume,self.color,self.attack,self.heal)
    def use(self, player,enemy):
        enemy.current_health-=self.attack
        player.current_mp -= self.consume
class Fireball:
    def __init__(self):
        self.consume = 4
        self.name = "火球"
        self.attack = 6
        self.imagePath = "assets/fire.png"
        self.color = (255, 0, 0)
        self.heal = None
        self.effectText=f"你使用了{self.name}对敌人造成了{self.attack}伤害"
        self.cardInfo = CardInfo(self.name,self.consume,self.color,self.attack,self.heal)
    def use(self, player,enemy):
        enemy.current_health-=self.attack
        player.current_mp -= self.consume

class Herb:
    def __init__(self):
        self.attack=None  # 回复的生命值
        self.consume = 3
        self.name = "回血"
        self.color = (0, 255, 0)  # 绿色
        self.heal = 10  
        self.effectText=f"你使用了{self.name}对回复了{self.heal}血量"
        self.cardInfo = CardInfo(self.name,self.consume,self.color,self.attack,self.heal)
    def use(self, player,enemy):
        player.current_health += self.heal
        player.current_mp -= self.consume
        