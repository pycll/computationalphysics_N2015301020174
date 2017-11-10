# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit
import random

background_image_filename = '10-14050Q43TRQ.jpg'
plane_image = 'plane.png'
bullet_image = 'bu1.png'
enemy_image = 'enemy.png'

pygame.mixer.pre_init(44100, 16, 2, 1024*4)
pygame.init()

sound = pygame.mixer.Sound("7222.wav")
shoot = pygame.mixer.Sound("3698.wav")

screen = pygame.display.set_mode((488, 650), 0, 32)

pygame.display.set_caption('da fei ji ha ha ha')
background = pygame.image.load(background_image_filename).convert()
plane = pygame.image.load(plane_image)
bullet = pygame.image.load(bullet_image)
heart = pygame.image.load('heart.png')
enemy = pygame.image.load(enemy_image)
go=pygame.image.load('go.png')
numbers={}
for num in '1234567890':
    numbers[num] = pygame.image.load('number'+num+'.png')

'''
number=pygame.image.load('number1.png').convert_alpha()
numbers['1']=number.subsurface((0,0),(50,68))
numbers['2']=number.subsurface((40+18*1,0),(50+18*1+53*1,68))
numbers['3']=number.subsurface((40+18*2+53*1,0),(40+18*2+53*2,68))
numbers['4']=number.subsurface((40+18*3+53*2,0),(40+18*3+53*3,68))
numbers['5']=number.subsurface((40+18*4+53*3,0),(40+18*4+53*4,68))
numbers['6']=number.subsurface((342 , 0),(405 , 68))
numbers['7']=number.subsurface((40+18*6+53*5 , 0),(40+18*6+53*6 , 68))
numbers['8']=number.subsurface((40+18*7+53*6 , 0),(40+18*7+53*7 , 68))
numbers['9']=number.subsurface((40+18*8+53*7 , 0),(40+18*8+53*8 , 68))
numbers['0']=number.subsurface((646 , 0),(686, 68))
'''

re=pygame.image.load('re.png')
scoreimage =pygame.image.load('score.png')
#my_font = pygame.font.SysFont(u'nanumgothic', 16)

clock = pygame.time.Clock()

while True: 
    x, y = 0, 500
    move_x, move_y = 0, 0
    bullets=[]
    enemies=[]
    butime=0
    ttot=0

    lives=3
    score=0
    dead = False

    while True:
        if lives == 5:
            break

        if dead:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        lives = 5
                        break
            screen.fill((0,0,0))
            screen.blit(go, (47,200))
            screen.blit(scoreimage, (47,300))
            stt=320
            score_str=str(score)
            for num in score_str:
                screen.blit(numbers[num],(stt,290))
                stt+=40
            screen.blit(re, (43,500))
            pygame.display.update()
        else:
            for event in pygame.event.get():
                if event.type == QUIT:
                   exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        move_x = -1
                    elif event.key == K_RIGHT:
                        move_x = 1
                    elif event.key == K_UP:
                        move_y = -1
                    elif event.key == K_DOWN:
                        move_y = 1
                elif event.type == KEYUP:
                    move_x = 0
                    move_y = 0
         

            if 0<=x+move_x<=424:
                x+= move_x
            if 0<=y+move_y<=586:
                y+= move_y
            v_t=ttot**0.5/700+0.25
            dtime = clock.tick()
            clock.tick(120)
            dy_bullet = dtime*3
            for bu in bullets:
                bu[1]-=dy_bullet
                if bu[1]<0:
                    bullets.remove(bu)
            butime=butime+dtime
            if butime>60:
                bullets.append([x+16,y-32])
                shoot.play()
                butime=0
            for ene in enemies:
                for bu in bullets:
                    if -55<ene[0]-bu[0]<27 and -38<ene[1]-bu[1]<20:
                        sound.play()
                        bullets.remove(bu)
                        enemies.remove(ene)
                        score+=1
            for ene in enemies:
                if ttot%800>400:
                    i=-1
                else:
                    i=1
                ene[0]+= dtime*i*ene[2]
                ene[1]+= dtime*v_t
                if ene[1]>630:
                    lives-=1
                    enemies.remove(ene)
                    if lives == 0:
                        dead=True
                
            a_t=(30+1360000//(15000+ttot))
            if ttot%a_t+dtime>a_t:
                enemies.append([random.randint(20,404),-25,random.randint(-100,100)/100.0])    
            ttot=ttot+dtime
            
            screen.fill((0,0,0))
            screen.blit(background, (0,0))
            screen.blit(plane,(x,y))
            for bu in bullets:
                screen.blit(bullet,bu)
            for ene in enemies:
                screen.blit(enemy,(ene[0],ene[1]))
            for lvs in range(lives):
                screen.blit(heart,(458-lvs*50,10))
            pygame.display.update()
