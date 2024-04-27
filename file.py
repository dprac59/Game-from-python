#создай игру "Лабиринт"!
from pygame import *
from random import *
from time import time as tm
import pygame
#создай окно игры
pygame.init()
mixer.init()
font.init()
mixer.music.load('space.ogg')
kick= mixer.Sound('fire.ogg')

font = font.Font(None,70)
winn = font.render('Press P to PLAY', True, (224, 29, 130))
window=display.set_mode((700,500))
display.set_caption('shooter')
score = 0
scoreb = 0
bc = transform.scale(image.load('galaxy.jpg'),(700,500))
bcmenu = transform.scale(image.load('bc.jpg'),(700,500))
los_bg= transform.scale(image.load('lose.jpg'),(700,500))

win_bg= transform.scale(image.load('win.jpg'),(700,500))
clock = time.Clock()
state = 'menu'
FPS=120
ammo = 0
real_time = False
real_start = 0
real_end = 0
bulets = sprite.Group()
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
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
        
    def fire(self):
        bull = Bullet('bullet.png',15,self.rect.centerx,self.rect.top,15,20)
        bulets.add(bull)
        
        
class Enemy(GameSprite):
    
    def update(self):
        global score
        self.rect.y += self.speed
        if self.rect.y >= 490:
            self.rect.y = 0
            self.rect.x = randint(0,620)
            score = score + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
        



                 

        
        
y2 = 100
x2 = 340
y1 = 450 
x1 = 350  
pl1 = Player('rocket.png',5,x1,y1,80,100)



monsters = sprite.Group()
for i in range(5):
    monsters.add(Enemy('ufo.png',randint(1,2),randint(0,620),randint(0,23),80,50))

asteroids = sprite.Group()
for i in range(3):
    asteroids.add(Enemy('asteroid.png',randint(1,2),randint(0,620),randint(0,23),80,50))

game = True

mixer.music.play()

while game:

    if state == 'menu':
        window.blit(bcmenu,(0,0))
        window.blit(winn,(180,250))
        keys = key.get_pressed()
        if keys[K_p] :
            state = 'game'
            print(state)
    elif state == 'game':
        

        window.blit(bc, (0,0))
        monsters.draw(window)
        monsters.update()
        asteroids.draw(window)
        asteroids.update()
        bulets.draw(window)
        bulets.update()

        pl1.update()
        pl1.reset()
        a = font.render('пропущено '+str(score), True, (224, 29, 130))
        if score > 10:
            state = 'lose'
        b = font.render('score '+str(scoreb), True, (224, 29, 130))
        if sprite.groupcollide(monsters,bulets,True,False):
            scoreb += 1
            monsters.add(Enemy('ufo.png',randint(2,5),randint(0,620),0,80,50))
        if scoreb > 10:
            state = 'win'
        window.blit(a,(0,0))
        window.blit(b,(0,50))
        if real_time == True:
            real_end = tm()
            if real_end - real_start >= 3:
                real_time = False
                ammo = 0
            else:
                window.blit(font.render('RELOAD', True, (224, 29, 130)),(250,450))

    elif state == 'lose':
        window.blit(los_bg,(0,0))
    elif state == 'win':
        window.blit(win_bg,(0,0))
        
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if ammo < 5 and real_time == False:
                    pl1.fire()
                    kick.play()
                    ammo += 1
                if ammo >= 5 and real_time == False:
                    real_time = True
                    real_start = tm()
                
    clock.tick(FPS)
    display.update()

