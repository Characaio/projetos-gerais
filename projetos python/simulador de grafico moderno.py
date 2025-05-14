import pygame as pg
import numpy as np

pg.init()

run = True

WIDTH,HEIGHT = 600,600



BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
VIOLET = (255,0,255)
WHITE = (255,255,255)
screen = pg.display.set_mode((WIDTH,HEIGHT))
coords = [300,300]
canto = pg.Rect(100,100,100,50)
escalax = 1
escalay = 1
pontos = [300,200,100,50]
menu = pg.Rect(0,0,WIDTH,HEIGHT)
state = 'grafico'
pressed = False
font = pg.font.SysFont('arial black', 15)
active1 = False
active2 = False
active3 = False
active4 = False
active5 = False
active6 = False
positiveXsize = '30'
positiveYsize = '20'
negativeXsize = '-10'
negativeYsize = '-10'
positiveXsizeFrame = pg.Rect(10,10,80,50)
positiveYsizeFrame = pg.Rect(10,65,80,50)
negativeXsizeFrame = pg.Rect(10,120,80,50)
negativeYsizeFrame = pg.Rect(10,175,80,50)
escalaxFrame = pg.Rect(10,230,80,50)
escalayFrame = pg.Rect(10,285,80,50)
starting_point = [300,300]
def update():
    global coords,active1,active2,active3,active4,active5
    if state == 'grafico':
        #pra cima
        coiso1 = pg.Rect(coords[0],coords[1],escalax*abs(eval(positiveXsize)*10),10)
        coiso2 = pg.Rect(coords[0]-escalax*abs(eval(negativeXsize)*10),coords[1],escalax*abs(eval(negativeXsize)*10),10)
        coiso3 = pg.Rect(coords[0],coords[1],10,escalay*abs(eval(negativeYsize)*10))
        coiso4 = pg.Rect(coords[0],coords[1]-abs(eval(negativeYsize)*10)*escalay,10,escalay*abs(eval(negativeYsize)*10))
        inicio = pg.Rect(coords[0],coords[1],10,10)
        pg.draw.rect(screen,(BLACK),canto)
        pg.draw.rect(screen,BLUE,coiso1)
        pg.draw.rect(screen,GREEN,coiso2)
        pg.draw.rect(screen,VIOLET,coiso3)
        pg.draw.rect(screen,YELLOW,coiso4)
        pg.draw.rect(screen,RED,inicio)
    elif state == 'menu':
        color1 = (0,0,0)
        color2 = (0,0,0)
        color3 = (0,0,0)
        color4 = (0,0,0)
        color5 = (0,0,0)
        color6 = (0,0,0)
        if active1:
            color1 = (150,150,150)
        if active2:
            color2 = (150,150,150)
        if active3:
            color3 = (150,150,150)
        if active4:
            color4 = (150,150,150)
        if active5:
            color5 = (150,150,150)
        if active6:
            color6 = (150,150,150)
        pg.draw.rect(screen,(200,200,200), menu)
        pg.draw.rect(screen,(color1),positiveXsizeFrame)
        pg.draw.rect(screen,(color2),positiveYsizeFrame)
        pg.draw.rect(screen,(color3),negativeXsizeFrame)
        pg.draw.rect(screen,(color4),negativeYsizeFrame)
        pg.draw.rect(screen,(color5),escalaxFrame)
        pg.draw.rect(screen,(color6),escalayFrame)
        surface1 = font.render(str(positiveXsize), True,WHITE)
        surface2 = font.render(str(positiveYsize), True,WHITE)
        surface3 = font.render(str(negativeXsize), True,WHITE)
        surface4 = font.render(str(negativeYsize), True,WHITE)
        surface5 = font.render(str(escalay), True,WHITE)
        surface6 = font.render(str(escalax), True,WHITE)
        screen.blit(surface1,(positiveXsizeFrame.x+5,positiveXsizeFrame.y))
        screen.blit(surface2,(positiveYsizeFrame.x+5,positiveYsizeFrame.y))
        screen.blit(surface3,(negativeXsizeFrame.x+5,negativeXsizeFrame.y))
        screen.blit(surface4,(negativeYsizeFrame.x+5,negativeYsizeFrame.y))
        screen.blit(surface5,(escalaxFrame.x+5,escalaxFrame.y))
        screen.blit(surface6,(escalayFrame.x+5,escalayFrame.y))
        info1 = font.render('Positive X Size', True,WHITE)
        info2 = font.render('Positive Y Size', True,WHITE)
        info3 = font.render('Negative X Size', True,WHITE)
        info4 = font.render('Negative Y Size', True,WHITE)
        screen.blit(info1,(positiveXsizeFrame.x+5+positiveXsizeFrame.w,positiveXsizeFrame.y))
        screen.blit(info2,(positiveYsizeFrame.x+5+positiveYsizeFrame.w,positiveYsizeFrame.y))
        screen.blit(info3,(negativeXsizeFrame.x+5+negativeXsizeFrame.w,negativeXsizeFrame.y))
        screen.blit(info4,(negativeYsizeFrame.x+5+negativeYsizeFrame.w,negativeYsizeFrame.y))
        
def isvalid(input):
    valid = ['-']
    return input in valid
        
while run:
    
    screen.fill(WHITE)
    key = pg.key.get_pressed()
    update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if positiveXsizeFrame.collidepoint(event.pos):
                active1 = True
            else:
                active1 = False
                
            if positiveYsizeFrame.collidepoint(event.pos):
                active2 = True
            else:
                active2 = False
                
            if negativeXsizeFrame.collidepoint(event.pos):
                active3 = True
            else:
                active3 = False
                
            if negativeYsizeFrame.collidepoint(event.pos):
                active4 = True
            else:
                active4 = False
            if escalaxFrame.collidepoint(event.pos):
                active5 = True
            else:
                active5 = False
            if escalayFrame.collidepoint(event.pos):
                active6 = True
            else:
                active6 = False
        if event.type == pg.KEYDOWN:
            if active1:
                if event.key == pg.K_BACKSPACE: 
                    positiveXsize = positiveXsize[:-1] 
                elif event.unicode.isdigit(): 
                    positiveXsize += event.unicode
            if active2:
                if event.key == pg.K_BACKSPACE: 
                    positiveYsize = positiveYsize[:-1] 
                elif event.unicode.isdigit(): 
                    positiveYsize += event.unicode
            if active3:
                if event.key == pg.K_BACKSPACE: 
                    negativeYsize = negativeYsize[:-1] 
                elif event.unicode.isdigit() or isvalid(event.unicode): 
                    negativeYsize += event.unicode
            if active4:
                if event.key == pg.K_BACKSPACE: 
                    negativeXsize = negativeXsize[:-1] 
                elif event.unicode.isdigit() or isvalid(event.unicode): 
                    negativeXsize += event.unicode
            if active5:
                if event.key == pg.K_BACKSPACE: 
                    escalax = escalax[:-1] 
                elif event.unicode.isdigit(): 
                    escalax += event.unicode
            if active6:
                if event.key == pg.K_BACKSPACE: 
                    escalay = escalay[:-1] 
                elif event.unicode.isdigit(): 
                    escalay += event.unicode
    if key[pg.K_0]:
        if pressed == False:
            pressed = True
            if state == 'menu':
                state = 'grafico'
            else:
                state = 'menu'
    else:
        pressed = False
    if key[pg.K_RIGHT]:
        coords[0] -= 0.1
    if key[pg.K_DOWN]:
        coords[1] -= 0.1
    if key[pg.K_UP]:
        coords[1] += 0.1
    if key[pg.K_LEFT]:
        coords[0] += 0.1
    pg.display.update()
    