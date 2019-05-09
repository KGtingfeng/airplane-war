import pygame
from Airplane_War.Screen import Screen
from pygame.sprite import Sprite
#飞机类
class Airplane(Sprite):
    def __init__(self, screen):
        super(Airplane,self).__init__()
        self.screen = screen
        self.img = pygame.image.load("airplane.png")
        self.rect = self.img.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        #控制飞机是否向右移动
        self.moving_right = False
        # 控制飞机是否向左移动
        self.moving_left = False
        # 血量为3
        self.blood = 3
        #分数
        self.mark=0

    def show_ship(self):
            #在屏幕上显示飞机
            self.screen.blit(self.img, self.rect)

    def update_pos(self):
        #向右移动，限制飞机不能飞出右屏幕
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.rect.centerx += 5
        #向左移动，限制飞机不能飞出左屏幕
        if self.moving_left and self.rect.left >= self.screen_rect.left:
            self.rect.centerx -= 5

