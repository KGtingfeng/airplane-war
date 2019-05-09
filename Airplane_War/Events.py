import pygame
import sys
from pygame.sprite import Group
from Airplane_War.Enemy import Enemy
from Airplane_War.Bullet import Bullet
from Airplane_War.Boom import Boom

def start_event(flag):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()
        elif ev.type==pygame.MOUSEBUTTONDOWN:
            print(1)
            flag[0] = True

def start_screen(screen,img,flag,mark):
    screen.blit(img,(0,0))
    txt = pygame.font.Font("st.otf", 25)
    if flag[0]:
        txt_fm = txt.render(u"总得分:"+str(mark), 1, (0, 0, 0))
        screen.blit(txt_fm, (120, 400))
    txt_f = txt.render(u"点击屏幕开始游戏...", 1, (0, 0, 0))
    screen.blit(txt_f, (120, 600))
    pygame.display.flip()


def check_event(ship,screen,bullet):
    for ev in pygame.event.get():
        if (ev.type == pygame.QUIT):
             sys.exit()
        elif ev.type == pygame.KEYDOWN:  # 按下键
            if ev.key == pygame.K_RIGHT:
                ship.moving_right = True
            if ev.key == pygame.K_LEFT:
                ship.moving_left = True
            if ev.key==pygame.K_SPACE:
                if len(bullet)<5:
                    b=Bullet(ship,screen)
                    bullet.add(b)
        elif ev.type == pygame.KEYUP:  # 弹起键
            if ev.key == pygame.K_RIGHT:
                ship.moving_right = False
            if ev.key == pygame.K_LEFT:
                ship.moving_left = False


#绘制和更新屏幕
def update_screen(screen,window_setting,airplane,bullets,enemys,booms):
    bg_color = window_setting.color
    screen.fill(bg_color)

    txt = pygame.font.Font("st.otf", 25)
    txt_blood = txt.render(u"命:"+str(airplane.blood), 1, (0, 0, 0))
    txt_mark= txt.render(u"分数:" + str(airplane.mark), 1, (0, 0, 0))
    txt_bullet = txt.render(u"子弹数:" + str(5-len(bullets)), 1, (0, 0, 0))
    screen.blit(txt_blood, (window_setting.size[0] - 50, 0))
    screen.blit(txt_mark,(window_setting.size[0]-150,0))
    screen.blit(txt_bullet, (0, 0))

    for bullet in bullets:
        bullet.show()
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for enemy in enemys:
        enemy.show_me()
        if enemy.rect.top > enemy.screen_rect.bottom:
            airplane.blood -= 1
            rect = enemy.rect
            b = Boom(screen, rect)
            booms.add(b)
            enemys.remove(enemy)
    airplane.update_pos()
    airplane.show_ship()
    for boom in booms:
        boom.show()
        if boom.time>30:
            booms.remove(boom)
    pygame.display.flip()