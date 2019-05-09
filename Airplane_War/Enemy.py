import pygame
import random
from pygame.sprite import Sprite
#敌人类
class Enemy(Sprite):
    def __init__(self,screen):
        super(Enemy,self).__init__()
        self.img=pygame.image.load("enemy.png")
        self.screen=screen
        self.rect=self.img.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.bottom=self.screen_rect.top
        # 敌人出生位置随机
        self.rect.right = random.randint(10,self.screen_rect.right)
        #记录时间
        self.time=0
        # 敌人运动方向
        self.direction=random.randint(1,2)

    def show_me(self):
        self.screen.blit(self.img, self.rect)
        # 敌人一直向下移动
        self.rect.centery+=1
        # 敌人一定时间后改变左右移动方向
        if self.time<100:
            if self.direction==1:
                # 限制敌人不能移动出屏幕右方
                if self.rect.right <= self.screen_rect.right:
                    self.rect.centerx+=2
                else:self.direction=2
            else:
                # 限制敌人不能移动出屏幕左方
                if self.rect.left >= self.screen_rect.left:
                    self.rect.centerx-=2
                else:self.direction=1
            self.time+=1
        else:
            self.direction=random.randint(1,2)
            self.time=0