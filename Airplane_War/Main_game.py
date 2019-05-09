
import pygame
from pygame.sprite import Group
from pygame.locals import *
from sys import exit
from Airplane_War.Events import *
from Airplane_War.Screen import Screen
from Airplane_War.Boom import Boom
from Airplane_War.Airplane import Airplane
from Airplane_War.Enemy import Enemy
class Game:
    def __init__(self,screen):
        self.screen=screen
        self.img = pygame.image.load("start.png")
        #进入游戏标志
        self.flag1=[False]
        #第一次游戏标志
        self.flag2=[False]

    def start(self):
        pygame.init()
        # 创建窗口参数设置的对象
        window_setting = Screen(self.screen.name,self.screen.size,self.screen.color)
        screen = pygame.display.set_mode(window_setting.size)  # 窗口尺寸
        pygame.display.set_caption("飞机大战")  # 设置窗口标题
        #分数
        mark=0
        while True:
            self.flag1[0]=False
            start_event(self.flag1)
            start_screen(screen,self.img,self.flag2,mark)
            if self.flag1[0]:
                self.flag2[0] = True
                airplane = Airplane(screen)
                bullets=Group()
                enemys=Group()
                booms=Group()
                while True:
                    #敌人数量小于3则刷出敌人
                    if len(enemys)<3:
                        e = Enemy(screen)
                        enemys.add(e)
                    check_event(airplane,screen,bullets)
                    #子弹与敌人碰撞检测
                    for a in enemys:
                            if pygame.sprite.spritecollide(a,bullets,True):
                                airplane.mark+=1
                                rect=a.rect
                                #添加爆炸特效
                                b = Boom(screen,rect)
                                booms.add(b)
                                enemys.remove(a)
                    #飞机与敌人碰撞检测
                    for a in enemys:
                        if pygame.sprite.collide_rect(a,airplane):
                            airplane.blood-=1
                            rect = a.rect
                            # 添加爆炸特效
                            b = Boom(screen, rect)
                            booms.add(b)
                            enemys.remove(a)
                    update_screen(screen, window_setting, airplane,bullets,enemys,booms)
                    #若血量小于0则结束游戏
                    if airplane.blood<=0:
                        #记录分数
                        mark=airplane.mark
                        break

scr=Screen("mygame",(480,800),(255,255,255))
start=Game(scr)
start.start()