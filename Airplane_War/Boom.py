import pygame
from pygame.sprite import Sprite
from Airplane_War.Enemy import Enemy
class Boom(Sprite):
    def __init__(self,screen,rect):
        super(Boom,self).__init__()
        self.img=pygame.image.load("boom.png")
        self.screen=screen
        self.enemy_rect=rect
        self.rect=self.img.get_rect()
        self.rect.centerx=self.enemy_rect.centerx
        self.rect.bottom = self.enemy_rect.bottom
        self.time=0

    def show(self):
        self.screen.blit(self.img,self.rect)
        self.time+=1