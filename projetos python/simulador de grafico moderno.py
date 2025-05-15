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
canto = pg.Rect(0,0,100,50)
escalax = '1'
escalay = '1'
pontos = [300,200,100,50]
menu = pg.Rect(0,0,WIDTH/2.5,HEIGHT/1.5)
sair = pg.Rect(520,0,80,50)
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
ativar_menu = False
def update():
    global coords,active1,active2,active3,active4,active5,positiveXsize,positiveYsize,negativeXsize,negativeYsize,escalax,escalay
    

    if escalax == '':
        escalax = '0'
    if escalay == '':
        escalay = '0'
        
    if negativeYsize != '':
        negy = eval(negativeYsize)
    else:
        negy = 0
        
    if negativeXsize != '':
        negx = eval(negativeXsize)
    else:
        negx = 0
    
    if positiveYsize != '':
        posiy = eval(positiveYsize)
    else:
        posiy = 0
        
    if positiveXsize != '':
        posix = eval(positiveXsize)
    else:
        posix = 0
        
    if state == 'grafico':
        #pra cima
        LinhaXpositivo = pg.Rect(coords[0],coords[1],eval(escalax)*posix*10+5,10)
        LinhaXNegativo = pg.Rect(coords[0]-eval(escalax)*abs(negx*10),coords[1],eval(escalax)*abs(negx*10),10)
        LinhaYNegativa = pg.Rect(coords[0],coords[1],10,eval(escalay)*abs(negy*10))
        LinhaYPositiva = pg.Rect(coords[0],coords[1]+10-posiy*10*eval(escalay),10,eval(escalay)*posiy*10+-5)
        inicio = pg.Rect(coords[0],coords[1],10,10)
        pg.draw.rect(screen,(BLACK),canto)
        pg.draw.rect(screen,BLUE,LinhaXpositivo)
        pg.draw.rect(screen,GREEN,LinhaXNegativo)
        pg.draw.rect(screen,VIOLET,LinhaYNegativa)
        pg.draw.rect(screen,YELLOW,LinhaYPositiva)
        pg.draw.rect(screen,RED,inicio)
        surface8 = font.render(str('menu'), True, WHITE)
        screen.blit(surface8,(canto.x,canto.y))
        for i in range(-1*posix,0,1):
            if i != 0:
                pg.draw.circle(screen,RED,(LinhaXpositivo.x+abs(i)*10*eval(escalax)+5,LinhaXpositivo.y+5),5)
                letras = font.render(str(abs(i)), True, BLACK)
                screen.blit(letras,((LinhaXpositivo.x+abs(i)*10*eval(escalax)+5,LinhaXpositivo.y+5)))
            
        for i in range(-1*posiy,0,1):
            if i != 0:
                pg.draw.circle(screen,RED,(LinhaYPositiva.x+5,LinhaYPositiva.y+i*10*eval(escalay)+10+LinhaYPositiva.h),5)
                letras = font.render(str(-1*i), True, BLACK)
                screen.blit(letras,((LinhaYPositiva.x-25,LinhaYPositiva.y+i*10*eval(escalay)+10+LinhaYPositiva.h-10)))
            
        for i in range(0,negx-1,-1):
            if i != 0:
                pg.draw.circle(screen,RED,(starting_point[0]+i*10*eval(escalax),starting_point[1]+5),5)
                letras = font.render(str(i), True, BLACK)
                screen.blit(letras,((starting_point[0]+i*10*eval(escalax),starting_point[1])))
            
        for i in range(-1,negy-1,-1):
            pg.draw.circle(screen,RED,(LinhaYNegativa.x+5,LinhaYNegativa.y+abs(i)*10*eval(escalay)),5)
            letras = font.render(str(i), True, BLACK)
            if i != 0 or i != -1:
                screen.blit(letras,((LinhaYNegativa.x-25,LinhaYNegativa.y+abs(i)*10*eval(escalay))))
        
        pg.draw.circle(screen,(BLACK),(starting_point[0]+5*10*eval(escalax),starting_point[1]-5*10*eval(escalay)),5)
        
        if ativar_menu:
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
            #pg.draw.rect(screen,(RED),sair)
            pg.draw.circle(screen,(BLACK),(starting_point[0]+5,starting_point[1]+5),5)
            pg.draw.rect(screen,(color1),positiveXsizeFrame)
            pg.draw.rect(screen,(color2),positiveYsizeFrame)
            pg.draw.rect(screen,(color3),negativeXsizeFrame)
            pg.draw.rect(screen,(color4),negativeYsizeFrame)
            pg.draw.rect(screen,(color5),escalaxFrame)
            pg.draw.rect(screen,(color6),escalayFrame)
            surface1 = font.render(str(positiveXsize), True, WHITE)
            surface2 = font.render(str(positiveYsize), True, WHITE)
            surface3 = font.render(str(negativeXsize), True, WHITE)
            surface4 = font.render(str(negativeYsize), True, WHITE)
            surface5 = font.render(str(escalax), True, WHITE)
            surface6 = font.render(str(escalay), True, WHITE)
            surface7 = font.render(str('X'), True, WHITE)
            
            screen.blit(surface1,(positiveXsizeFrame.x+5,positiveXsizeFrame.y))
            screen.blit(surface2,(positiveYsizeFrame.x+5,positiveYsizeFrame.y))
            screen.blit(surface3,(negativeXsizeFrame.x+5,negativeXsizeFrame.y))
            screen.blit(surface4,(negativeYsizeFrame.x+5,negativeYsizeFrame.y))
            screen.blit(surface5,(escalaxFrame.x+5,escalaxFrame.y))
            screen.blit(surface6,(escalayFrame.x+5,escalayFrame.y))
            screen.blit(surface7,(sair.x+35,12))
            
            info1 = font.render('Positive X Size', True,BLACK)
            info2 = font.render('Positive Y Size', True,BLACK)
            info3 = font.render('Negative X Size', True,BLACK)
            info4 = font.render('Negative Y Size', True,BLACK)
            info5 = font.render('Escala X', True,BLACK)
            info6 = font.render('Escala Y', True,BLACK)
            screen.blit(info1,(positiveXsizeFrame.x+5+positiveXsizeFrame.w,positiveXsizeFrame.y))
            screen.blit(info2,(positiveYsizeFrame.x+5+positiveYsizeFrame.w,positiveYsizeFrame.y))
            screen.blit(info3,(negativeXsizeFrame.x+5+negativeXsizeFrame.w,negativeXsizeFrame.y))
            screen.blit(info4,(negativeYsizeFrame.x+5+negativeYsizeFrame.w,negativeYsizeFrame.y))
            screen.blit(info5,(escalaxFrame.x+5+escalaxFrame.w,escalaxFrame.y))
            screen.blit(info6,(escalayFrame.x+5+escalayFrame.w,escalayFrame.y))
    if escalax == '0':
        escalax = ''
    if escalay == '0':
        escalay = ''
def isvalid(input):
    valid = ['-' ,'.']
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
            if canto.collidepoint(event.pos):
                ativar_menu = True
            if sair.collidepoint(event.pos):
                ativar_menu = False
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
                    negativeXsize = negativeXsize[:-1] 
                elif event.unicode.isdigit() or isvalid(event.unicode) and event.unicode != '.': 
                    negativeXsize += event.unicode
                
            if active4:
                if event.key == pg.K_BACKSPACE: 
                    negativeYsize = negativeYsize[:-1] 
                elif event.unicode.isdigit() or isvalid(event.unicode) and event.unicode != '.': 
                    negativeYsize += event.unicode
            if active5:
                if event.key == pg.K_BACKSPACE: 
                    escalax = escalax[:-1] 
                elif event.unicode.isdigit() or isvalid(event.unicode): 
                    escalax += event.unicode

            if active6:
                if event.key == pg.K_BACKSPACE: 
                    escalay = escalay[:-1] 
                elif event.unicode.isdigit() or isvalid(event.unicode): 
                    escalay += event.unicode
    if key[pg.K_p]:
        if pressed == False:
            pressed = True
            if ativar_menu:
                ativar_menu = False
            else:
                ativar_menu = True
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
    