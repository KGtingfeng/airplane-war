import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ship,screen):
        super(Bullet, self).__init__()
        self.img=pygame.image.load("bullet.png")
        self.ship_rect=ship.rect
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.rect=self.img.get_rect()
        self.rect.bottom = self.ship_rect.top
        self.rect.centerx=self.ship_rect.centerx

    def show(self):
        self.screen.blit(self.img,self.rect)
        self.rect.centery-=1
