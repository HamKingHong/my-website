#导入模块。。。

import random

import pygame,sys,os

pygame.mixer.init()

from pygame.locals import *

pygame.init()

fps = 30

fpsClock = pygame.time.Clock()

icon = pygame.image.load('resource/h-2.JPG')

bali = pygame.image.load('resource/baligonglu.png')

cake = pygame.image.load('resource/cake.png')

fire1 = pygame.image.load('resource/firework1.png')

fire2 = pygame.image.load('resource/firework2.png')

fire3 = pygame.image.load('resource/firework3.png')

fire4 = pygame.image.load('resource/firework4.png')

firesImg = [fire1,fire2,fire3,fire4]

font = pygame.font.Font('resource/繁星糖果.ttf',50)

font1 = pygame.font.Font('resource/繁星糖果.ttf',30)

boom_sound = pygame.mixer.Sound('resource/爆炸.wav')

pygame.mixer.music.load('resource/铃声.wav')

pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((340,700))

pygame.display.set_caption('生日快乐')

pygame.display.set_icon(icon)

#加载。。。

class Load(object):

    def display(self):

        screen.blit(bali,(0,0))

        pygame.display.update()

l = Load()

#蛋糕

class Cake(object):

    def display(self):

        screen.blit(cake,(46,300))

c = Cake()

#预设烟花数量

fires = []

fire_num = 6

fire = False

#烟花

class Firework(object):

    def __init__(self):

        self.x = random.randint(20,220)

        self.y = random.randint(20,280)

        self.fire = random.choice(firesImg)

    def display(self):

        global fires

        screen.blit(self.fire,(self.x,self.y))

        boom_sound.play()

        fires.remove(random.choice(fires))

        fires.append(Firework())

f = Firework()

for i in range(fire_num):

    fires.append(Firework())

#祝福语的文字对象

class Birth(object):

    def __init__(self):

        self.text1 = '生'

        self.text2 = '日'

        self.text3 = '快'

        self.text4 = '乐'

        self.text5 = '历经千帆'

        self.text6 = '归来依旧'

        self.text7 = '19'

        self.render1 = font.render(self.text1,True,(128,128,0))

        self.render2 = font.render(self.text2, True, (128, 0, 128))

        self.render3 = font.render(self.text3, True, (0, 128, 128))

        self.render4 = font.render(self.text4, True, (255, 255, 255))

        self.render5 = font1.render(self.text5, True, (128, 0, 0))

        self.render6 = font1.render(self.text6, True, (255, 255, 255))

        self.render7 = font1.render(self.text7, True, (128, 0, 128))

    def display(self):

        screen.blit(self.render1,(155,20))

        screen.blit(self.render2,(155,80))

        screen.blit(self.render3,(155,160))

        screen.blit(self.render4,(155,220))

        screen.blit(self.render5, (110,550))

        screen.blit(self.render6, (110,590))

        screen.blit(self.render7,(155,630))

b = Birth()

load = True

while load:

    l.display()

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.pos[0] in range(248,315) and event.pos[1] in range(540,600):

                load = False

pygame.mixer.music.load('resource/生日快乐.wav')

pygame.mixer.music.play(-1)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            exit()

    screen.fill((0, 0, 0))

    b.display()

    for f in fires:

        f.display()

    c.display()

    fpsClock.tick(fps)

    pygame.display.update()
