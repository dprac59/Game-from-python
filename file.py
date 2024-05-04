import pygame as pg 
from pygame import *
from random import randint

pg.init()
red=(255,0,0)
green=(0,255,51)
lg = (200,255,200)
lr = (250,128,114)
black=(0,0,0)
blue=(0,0,100)
orange = (227,131,14)
bc=(randint(0,255),randint(0,255),randint(0,255))
w = 1000
h = 600
fps = 120
SPEED = 3
window = pg.display.set_mode((w,h))

clock = pg.time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self,image_pl,speed,x,y,size_x,size_y):
        super().__init__()
        self.image =transform.scale(image.load(image_pl),(size_x,size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
  
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < 650:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 650:
            self.rect.y += self.speed

ball = GameSprite('ball.png',600,350,50,50,50)
plat = Player('plat_1.png',30,20,90,100,250)
plat2 = Player2('plat_2.png',920,900,30,100,250)
start_x = 5
start_y = 5
count = 9

speed_x = 3
speed_y = 3




pg.font.init()
font1=pg.font.SysFont('verdana',60,)
win_ing = font1.render('pl2 lose!',True,(200,0,0))
los_ing = font1.render('pl1 lose!',True,(225,0,0))

run = True
while run:
    window.fill(bc)
   

    keys = pg.key.get_pressed()
    if keys[pg.K_w] and plat.rect.y > 5:
        plat.rect.y -= SPEED
    if keys[pg.K_s] and plat.rect.y < h - 250:
        plat.rect.y += SPEED
    if keys[pg.K_UP] and plat2.rect.y > 5:
        plat2.rect.y -= SPEED
    if keys[pg.K_DOWN] and plat2.rect.y < h - 250:
        plat2.rect.y += SPEED

    if ball.rect.colliderect(plat.rect):
        speed_x *= -1
    if ball.rect.colliderect(plat2.rect):
        speed_x *= -1
    if ball.rect.y<0:
        speed_y *=-1
    if ball.rect.y >550:
        speed_y *= -1
    if ball.rect.x > w - 50 or ball.rect.x < 0:
        speed_x *=-1

    if ball.rect.x < plat.rect.x + 20:
        window.blit(los_ing,(350,200))
        run = False
    if ball.rect.x > plat2.rect.x + 20:
        window.blit(win_ing,(350,200))
        run = False 
        
    
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    ball.reset()
    plat.reset()
    plat2.reset()
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False
    pg.display.update()
    clock.tick(fps)

