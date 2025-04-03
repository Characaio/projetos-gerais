#basic pygame template

import pygame as pg
import random as rand
import math
pg.init()

WIDTH,HEIGHT = 900,600
screen = pg.display.set_mode((WIDTH,HEIGHT))
BLACK = (0,0,0)
RED = (255,0,0)
ORANGE = (255,127,0)
YELLOW = (255,255,0)
CYAN =  (0,255,255)
PURPLE = (127,0,255)
MAGENTA = (255,0,127)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
PIPECOLOR = (103,198,87)
clock = pg.time.Clock()
pause = False
run = True
alive = True
array = []
array0 = []
arraycopy = []
gridx = int(WIDTH/30)
gridy = int(HEIGHT/30)
grid = []

key_pressed_last_frame = False
key_pressed_last_frame1 = False
key_pressed_last_frame2 = False
key_pressed_last_frame3 = False
font = pg.font.SysFont("Arial", 10)
timer = 0
class bird:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rect = pg.Rect((self.x,self.y,10,10))
        self.velocity = 0



    def render(self):
        pg.draw.rect(screen,(YELLOW),self.rect)
        
    def update(self):
        self.y += self.velocity
        if self.velocity < 30:
            self.velocity += 1 * timer
        self.rect = pg.Rect((self.x,self.y,10,10))
        
class pip:
        def __init__(self,width):
            self.width = width
            self.dist = rand.randint(int(HEIGHT/6),int(HEIGHT/4))
            self.wid = 35
            self.rad = rand.randint(int(HEIGHT/3),HEIGHT)
            self.rect     = pg.Rect((self.width, self.rad,self.wid, (self.rad-self.dist)))
            self.toprect  = pg.Rect((self.width, 0,       self.wid, (self.rad - HEIGHT)))
            self.bordert  = pg.Rect((self.width-int(self.wid/4), self.rad,self.wid+int(self.wid/2) , int(HEIGHT/28)))
            self.borderb  = pg.Rect((self.width-int(self.wid/4), self.rad,self.wid+int(self.wid/2) , int(HEIGHT/28)))
        def render(self):
            
            
            pg.draw.rect(screen,(PIPECOLOR),self.rect)
            pg.draw.rect(screen,(PIPECOLOR),self.toprect)
            pg.draw.rect(screen,(PIPECOLOR),self.bordert)
            pg.draw.rect(screen,(PIPECOLOR),self.borderb)
        def update(self):
            self.width -= 1
            self.toprect  = pg.Rect((self.width,0        ,self.wid,(self.rad-self.dist)))
            self.rect     = pg.Rect((self.width, self.rad,self.wid,(HEIGHT-self.rad)))
            self.bordert  = pg.Rect((self.width-int(self.wid/4), self.rad,self.wid+int(self.wid/2) , int(HEIGHT/28)))
            self.borderb  = pg.Rect((self.width-int(self.wid/4), self.rad-self.dist       ,self.wid+int(self.wid/2) , int(HEIGHT/28)))
        
bufferL = []
jumpbuffer = []
pipebuffer = []
bird = bird(WIDTH/10,HEIGHT/2)
pipes = []
pipedown = []

def spawn_shit():
    pipes.append(pip(WIDTH))

spawn_shit()

while run:
    screen.fill((BLACK))
    key = pg.key.get_pressed()
    if len(bufferL) > 2:
        if alive:
            bird.update()
        bird.render()
        
    if len(pipebuffer) > rand.randint(150,400):
        spawn_shit()
        pipebuffer = []
    else:
        pipebuffer.append('hi')
    
    
    for i,pipe in enumerate(pipes):
        pipe.render()
        if alive:
            pipe.update()
        if pipe.rect.collidepoint(bird.x,bird.y):
            alive = False
    timer += 0.008
        
    if bird.y > HEIGHT:
        
        print(bird.velocity)
        bird.velocity = 0
        while bird.y > HEIGHT:
            bird.y -= 1
    if bird.y < 0:
        
        print(bird.velocity)
        bird.velocity = 0
        while bird.y < 0:
            bird.y += 1

    if key[pg.K_d]:
        bird.x +=1
        
    if key[pg.K_a]:
        bird.x -= 1
    if len(jumpbuffer) > 6:
        if key[pg.K_UP]:
            if not key_pressed_last_frame:#isso verifica se a tecla esta pressionada no ultimo frame
                #coloca algo
                
                    jumpbuffer = []
                    timer = 0
                    if bird.velocity > -10:
                        
                        bird.velocity = -2
                        
                    else:
                        bird.velocity = -10
        else:
        
            key_pressed_last_frame = False #isso vira falso quando a tecla não esta
    else:
        jumpbuffer.append('JUMP')
                
        key_pressed_last_frame = True#isso atualiza o estado
        
    
       
    
    if key[pg.K_p] == True: 
        if not key_pressed_last_frame1:#isso verifica se a tecla esta pressionada no ultimo frame
            #coloca algo
            pause = not pause
        key_pressed_last_frame1 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame1 = False #isso vira falso quando a tecla não esta


    if len(jumpbuffer) > 6:
        if key[pg.K_w] == True: 
            if not key_pressed_last_frame2:#isso verifica se a tecla esta pressionada no ultimo frame
                #coloca algo
                jumpbuffer = []
                timer = 0
                if bird.velocity > -10:
                    
                    bird.velocity = -5
                    
                else:
                    bird.velocity = -10
            key_pressed_last_frame2 = True#isso atualiza o estado  
        else:
            key_pressed_last_frame2 = False#isso atualiza o estado  
    else:
        jumpbuffer.append('JUMP')
                
        key_pressed_last_frame = True#isso atualiza o estado

        
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
            run = False
            
        #o down e up define um sistema de drag do mouse
        if (event.type == pg.MOUSEBUTTONDOWN) and (event.type != pg.MOUSEWHEEL):
            #é um clique normal
            spawn_shit()
            
            
        if event.type == pg.MOUSEBUTTONUP and event.type != pg.MOUSEWHEEL:
            #serve pra tirar um clicking ou só adicionar outra mecanica
            pass
        if event.type == pg.MOUSEWHEEL:
            if event.y == 1:
                #scroll pra cima
                pass
            if event.y == -1:
                #scroll pra cima
                pass
            
    pg.display.update()
    clock.tick(60)
pg.quit()
quit()
