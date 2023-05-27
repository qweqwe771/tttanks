from pygame import *

from random import randint
window = display.set_mode((600, 300))
display.set_caption('тттанки')

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image =  transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def colliderect(self, rect) :
        return self.rect.colliderect(rect)
class Wall(sprite.Sprite):
    def __init__(self,player_x,player_y):
        sprite.Sprite.__init__(self)
        self.image =  transform.scale(image.load('wall.png'), (10,10))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
walls=list()
def creat_wall(x,y,side_x,side_y):
    for i in range(side_y):
        for u in range (side_x):    
            wall= Wall(x,y)
            walls.append(wall)
            x+=10
            if u+1 == side_x:
                x-=10*side_x
                y+=10
bullets= list()
class bullet_w_1(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed,vector):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.u=False
    def update(self):
        self.rect.y-=self.speed
        if self.rect.y<=25:
            bullets.remove(self)
        for i in walls:
            if self.rect.colliderect(i):
                walls.remove(i)
                self.u=True
        for i in walls:
            if self.rect.colliderect(i):
                walls.remove(i)
                self.u=True
        if self.u:
            bullets.remove(self)
class bullet_d_1(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed,vector):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.u=False
    def update(self):
        self.rect.x+=self.speed
        if self.rect.x>=605:
            bullets.remove(self)
        for i in walls:
            if self.rect.colliderect(i):
                walls.remove(i)
                self.u=True
        for i in walls:
            if self.rect.colliderect(i):
                walls.remove(i)
                self.u=True
        if self.u:
            bullets.remove(self)
class bullet_s_1(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed,vector):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.u=False
    def update(self):
        self.rect.y+=self.speed
        if self.rect.y>=305:
            bullets.remove(self)
        for i in walls:
            if self.rect.colliderect(i):
                walls.remove(i)
                self.u=True
        for i in walls:
            if self.rect.colliderect(i):
                walls.remove(i)
                self.u=True
        if self.u:
            bullets.remove(self)
class bullet_a_1(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed,vector):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.u=False
    def update(self):
        self.rect.x-=self.speed
        if self.rect.x<=-5:
            bullets.remove(self)
        for i in walls:
            if self.rect.colliderect(i):
                walls.remove(i)
                self.u=True
        for i in walls:
            if self.rect.colliderect(i):
                walls.remove(i)
                self.u=True
        if self.u:
            bullets.remove(self)


class TANK_pl(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed,vector):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.vector = vector
        
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]  :
            self.rect.y -= self.speed
            self.image = transform.scale(image.load('TANK_1_w.png'), (30, 30))
            self.vector='w'
            for t in walls:
                if self.rect.colliderect(t) or self.rect.y<=-5:
                    self.rect.y+=self.speed 
        elif keys_pressed[K_s] :
            self.rect.y += self.speed
            self.image = transform.scale(image.load('TANK_1_s.png'), (30, 30))
            self.vector='s'
            for t in walls:
                if self.rect.colliderect(t) or self.rect.y>=275:
                    self.rect.y-=self.speed       
        elif keys_pressed[K_a] :
            self.rect.x-=self.speed
            self.image = transform.scale(image.load('TANK_1_a.png'), (30, 30))
            self.vector='a'
            for t in walls:
                if self.rect.colliderect(t) or self.rect.x<=-5:
                    self.rect.x+=self.speed
        elif keys_pressed[K_d] :
            self.rect.x+=self.speed
            self.image = transform.scale(image.load('TANK_1_d.png'), (30, 30))
            self.vector='d'
            for t in walls:
                if self.rect.colliderect(t) or self.rect.x>=575:
                    self.rect.x-=self.speed
    def fire(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_z]:   
            if self.vector == 'w':
                x=self.rect.x
                y=self.rect.y-5
                bullet=bullet_w_1('pyla_w.png',x,y,30,10,10,'1')
                bullets.append(bullet)
                for i in bullets:
                    i.reset()
            elif self.vector == 'd':
                x=self.rect.x+25
                y=self.rect.y
                bullet=bullet_d_1('pyla_d.png',x,y,10,30,10,'1')
                bullets.append(bullet)
                for i in bullets:
                    i.reset()
            elif self.vector == 's':
                x=self.rect.x
                y=self.rect.y+25
                bullet=bullet_s_1('pyla_s.png',x,y,30,10,10,'1')
                bullets.append(bullet)
                for i in bullets:
                    i.reset()
            elif self.vector == 'a':
                x=self.rect.x+5
                y=self.rect.y
                bullet=bullet_a_1('pyla_a.png',x,y,10,30,10,'1')
                bullets.append(bullet)
                for i in bullets:
                    i.reset()
class TANK_en(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed,vector='d'):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.vector = vector
    def update(self):
        if self.vector== 'd':
            self.rect.x+=self.speed
            self.image = transform.scale(image.load('TANK_1_d.png'), (30, 30))
            for t in walls:
                if self.rect.colliderect(t) or self.rect.x>=575:
                    self.rect.x-=self.speed
                    if randint(1,2)==1:
                        self.vector='w'
                    else:
                        self.vector='s'
        elif self.vector== 'a':
            self.rect.x-=self.speed
            self.image = transform.scale(image.load('TANK_1_a.png'), (30, 30))
            for t in walls:
                if self.rect.colliderect(t) or self.rect.x<=-5:
                    self.rect.x+=self.speed
                    if randint(1,2)==1:
                        self.vector='w'
                    else:
                        self.vector='s'
        elif self.vector== 'w':
            self.rect.y-=self.speed
            self.image = transform.scale(image.load('TANK_1_w.png'), (30, 30))
            for t in walls:
                if self.rect.colliderect(t) or self.rect.y<=-5:
                    self.rect.y+=self.speed
                    if randint(1,2)==1:
                        self.vector='a'
                    else:
                        self.vector='d'
        elif self.vector== 's':
            self.rect.y+=self.speed
            self.image = transform.scale(image.load('TANK_1_s.png'), (30, 30))
            for t in walls:
                if self.rect.colliderect(t) or self.rect.y>=275:
                    self.rect.y-=self.speed
                    if randint(1,2)==1:
                        self.vector='a'
                    else:
                        self.vector='d'
    def up(self):
        u=randint(1,4)
        if u==1:
            self.vector='a'
        elif u==2:
            self.vector='s'
        elif u==3:
            self.vector='d'
        elif u==4:
            self.vector='w'
    def fire(self):
        if self.vector == 'w':
            x=self.rect.x
            y=self.rect.y-5
            bullet=bullet_w_1('pyla_w.png',x,y,30,10,10,'1')
            bullets.append(bullet)
            for i in bullets:
                i.reset()
        elif self.vector == 'd':
            x=self.rect.x+25
            y=self.rect.y
            bullet=bullet_d_1('pyla_d.png',x,y,10,30,10,'1')
            bullets.append(bullet)
            for i in bullets:
                i.reset()
        elif self.vector == 's':
            x=self.rect.x
            y=self.rect.y+25
            bullet=bullet_s_1('pyla_s.png',x,y,30,10,10,'1')
            bullets.append(bullet)
            for i in bullets:
                i.reset()
        elif self.vector == 'a':
            x=self.rect.x+5
            y=self.rect.y
            bullet=bullet_a_1('pyla_a.png',x,y,10,30,10,'1')
            bullets.append(bullet)
            for i in bullets:
                i.reset()




enemy = TANK_en('TANK_1_d.png',30,30,30,30,5)
tttank= TANK_pl('TANK_1_w.png',540,120,30,30,5,'w')
creat_wall(270,30,27,3)
creat_wall(90,60,3,18)
creat_wall(270,240,27,3)
creat_wall(210,90,3,12)

game= True
finish=True
clock = time.Clock()
from time import time
ui= time()
while game:
    if finish:
        window.fill((0,0,0))
        tttank.update()
        tttank.reset()
        tttank.fire()
        enemy.update()
        enemy.reset()
        for i in walls:
            i.reset()
        for i in bullets:
            i.update()
            i.reset()

        ui2=time()
        if ui2-ui>=0.6:
            enemy.up()
        if ui2-ui>=1:
            enemy.fire()
            ui=time()    


    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()
    clock.tick(30)
