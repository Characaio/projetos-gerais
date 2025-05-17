import pygame as pg
import numpy as np

pg.init()

run = True

WIDTH,HEIGHT = 800,600



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
escalax = '3'
escalay = '3'
menu = pg.Rect(0,0,WIDTH/2.5,HEIGHT/1.5)
sair = pg.Rect(WIDTH-80,0,80,50)
state = 'grafico'
pressed = False
font = pg.font.SysFont('arial black', 15)
active1 = False
active2 = False
active3 = False
active4 = False
active5 = False
active6 = False
active7 = False
active8 = False
positiveXsize = '30'
positiveYsize = '20'
negativeXsize = '-10'
negativeYsize = '-20'
pontos = [(5,5),(6,6),(8,8),(-5,-3),(-6,-2)]
positive,negative = False,False
positiveXsizeFrame = pg.Rect(10,10,80,50)
positiveYsizeFrame = pg.Rect(10,65,80,50)
negativeXsizeFrame = pg.Rect(10,120,80,50)
negativeYsizeFrame = pg.Rect(10,175,80,50)
escalaxFrame = pg.Rect(10,230,80,50)
escalayFrame = pg.Rect(10,285,80,50)
starting_point = [300,300]
Menu_pontos = pg.Rect(WIDTH-105,0,105,260)
pontox = pg.Rect(WIDTH-100,10,95,55)
pontoy = pg.Rect(WIDTH-100,75,95,55)
confirmar = pg.Rect(WIDTH-100,140,95,55)
limpar = pg.Rect(WIDTH-100,200,95,50)
escolhax = ''
escolhay = ''
ativar_menu = False
ativar_menu2 = False

escalaxscrollup = pg.Rect(escalaxFrame.x+escalaxFrame.w-10,escalaxFrame.y,10,escalaxFrame.h/2-5)
escalaxscrolldown = pg.Rect(escalaxFrame.x+escalaxFrame.w-10,escalaxFrame.y+escalaxFrame.h/2+5,10,escalaxFrame.h/2-5)

escalayscrollup = pg.Rect(escalayFrame.x+escalayFrame.w-10,escalayFrame.y,10,escalayFrame.h/2-5)
escalayscrolldown = pg.Rect(escalayFrame.x+escalayFrame.w-10,escalayFrame.y+escalayFrame.h/2+5,10,escalayFrame.h/2-5)

positiveXsizescrollup = pg.Rect(positiveXsizeFrame.x+positiveXsizeFrame.w-10,positiveXsizeFrame.y,10,positiveXsizeFrame.h/2-5)
positiveXsizescrolldown = pg.Rect(positiveXsizeFrame.x+positiveXsizeFrame.w-10,positiveXsizeFrame.y+positiveXsizeFrame.h/2+5,10,positiveXsizeFrame.h/2-5)

positiveYsizescrollup = pg.Rect(positiveYsizeFrame.x+positiveYsizeFrame.w-10,positiveYsizeFrame.y,10,positiveYsizeFrame.h/2-5)
positiveYsizescrolldown = pg.Rect(positiveYsizeFrame.x+positiveYsizeFrame.w-10,positiveYsizeFrame.y+positiveYsizeFrame.h/2+5,10,positiveYsizeFrame.h/2-5)

negativeXsizescrollup = pg.Rect(negativeXsizeFrame.x+negativeXsizeFrame.w-10,negativeXsizeFrame.y,10,negativeXsizeFrame.h/2-5)
negativeXsizescrolldown = pg.Rect(negativeXsizeFrame.x+negativeXsizeFrame.w-10,negativeXsizeFrame.y+negativeXsizeFrame.h/2+5,10,negativeXsizeFrame.h/2-5)

negativeYsizescrollup = pg.Rect(negativeYsizeFrame.x+negativeYsizeFrame.w-10,negativeYsizeFrame.y,10,negativeYsizeFrame.h/2-5)
negativeYsizescrolldown = pg.Rect(negativeYsizeFrame.x+negativeYsizeFrame.w-10,negativeYsizeFrame.y+negativeYsizeFrame.h/2+5,10,negativeYsizeFrame.h/2-5)


def update():
    global positive,pontos,negative,escolhax,escolhay,coords,active1,active2,active3,active4,active5,positiveXsize,positiveYsize,negativeXsize,negativeYsize,escalax,escalay
    

    if escalax == '':
        escalax = '0'

    if escalay == '':
        escalay = '0'

    if positiveXsize == '':
        positiveXsize = '0'

    if positiveYsize == '':
        positiveYsize = '0'

    if negativeXsize == '' or negativeXsize == '-':
        negativeXsize = '0'

    if negativeYsize == '' or negativeYsize == '-':
        negativeYsize = '0'

        
    if negativeYsize != '' and negativeYsize != '-':
        negy = eval(negativeYsize)
    else:
        negy = 0
        
    if negativeXsize != '' and negativeXsize != '-':
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
        
        
        coiso1 = eval(escalax)*posix*10
        coiso2 = eval(escalay)*posiy*10
        coiso3 = eval(escalax)*negx*10
        coiso4 = eval(escalay)*negy*10
        pg.draw.line(screen,BLACK,starting_point,(starting_point[0]+coiso1,starting_point[1]),5)
        pg.draw.line(screen,BLACK,starting_point,(starting_point[0],starting_point[1]-coiso2),5)
        pg.draw.line(screen,BLACK,starting_point,(starting_point[0]+coiso3,starting_point[1]),5)
        pg.draw.line(screen,BLACK,starting_point,(starting_point[0],starting_point[1]-coiso4),5)
        pg.draw.circle(screen,(RED),(starting_point[0],starting_point[1]),10)
        pg.draw.rect(screen,(BLACK),canto)
        surface8 = font.render(str('menu'), True, WHITE)
        screen.blit(surface8,(canto.x,canto.y))
        ballsize = 5

        for i in range(0,posix+1):
            escala1 = abs(i)*10*eval(escalax)
            escala2 = abs(i)*10*eval(escalay)
            if i != 0:
                pg.draw.circle(screen,RED,(starting_point[0]-escala1*-1,starting_point[1]),ballsize)
                letras = font.render(str(abs(i)), True, BLACK)
                screen.blit(letras,((starting_point[0]+escala1-5,starting_point[1]+5)))
            
        for i in range(0,posiy+1):
            escala1 = abs(i)*10*eval(escalax)
            escala2 = abs(i)*10*eval(escalay)
            if i != 0:
                pg.draw.circle(screen,RED,(starting_point[0],starting_point[1]-escala2),ballsize)
                letras = font.render(str(i), True, BLACK)
                screen.blit(letras,((starting_point[0]-25,starting_point[1]-escala2-10)))
            
        for i in range(0,negx-1,-1):
            escala1 = abs(i)*10*eval(escalax)
            escala2 = abs(i)*10*eval(escalay)
            if i != 0:
                pg.draw.circle(screen,RED,(starting_point[0]-escala1,starting_point[1]),ballsize)
                letras = font.render(str(i), True, BLACK)
                screen.blit(letras,((starting_point[0]-escala1-10,starting_point[1]+5)))
            
        for i in range(-1,negy-1,-1):
            escala1 = abs(i)*10*eval(escalax)
            escala2 = abs(i)*10*eval(escalay)
            pg.draw.circle(screen,RED,(starting_point[0],starting_point[1]+escala2+1),ballsize)
            letras = font.render(str(i), True, BLACK)
            if i != 0 or i != -1:
                screen.blit(letras,((starting_point[0]-25,starting_point[1]+escala2-5)))
        for i, ponto in enumerate(pontos):
            escala_x = 10 * eval(escalax)
            escala_y = 10 * eval(escalay)

            iniciox = ponto[0] * escala_x
            inicioy = ponto[1] * escala_y

            screen_x = starting_point[0] + iniciox
            screen_y = starting_point[1] - inicioy  
            
            if (eval(negativeXsize) <= ponto[0] <= eval(positiveXsize)) and (eval(negativeYsize) <= ponto[1] <= eval(positiveYsize)):
                pg.draw.line(screen, (180,180,180), (starting_point[0], screen_y), (screen_x, screen_y), 3)
                pg.draw.line(screen, (180,180,180), (screen_x, starting_point[1]), (screen_x, screen_y), 3)
                
            
        for i,ponto in enumerate(pontos):
            escala_x = 10 * eval(escalax)
            escala_y = 10 * eval(escalay)

            iniciox = ponto[0] * escala_x
            inicioy = ponto[1] * escala_y

            screen_x = starting_point[0] + iniciox
            screen_y = starting_point[1] - inicioy  
            textoponto = font.render(str(ponto),True,BLACK)
            pg.draw.circle(screen, BLACK, (screen_x, screen_y), ballsize)
            screen.blit(textoponto,(screen_x, screen_y-10))
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
            pg.draw.rect(screen,(RED),sair)
            #pg.draw.circle(screen,(BLACK),(starting_point[0],starting_point[1]),5)
            pg.draw.rect(screen,(color1),positiveXsizeFrame)
            pg.draw.rect(screen,(color2),positiveYsizeFrame)
            pg.draw.rect(screen,(color3),negativeXsizeFrame)
            pg.draw.rect(screen,(color4),negativeYsizeFrame)
            pg.draw.rect(screen,(color5),escalaxFrame)
            pg.draw.rect(screen,(color6),escalayFrame)
            
            pg.draw.rect(screen,(GREEN),escalaxscrollup)
            pg.draw.rect(screen,(BLUE),escalaxscrolldown)
            
            pg.draw.rect(screen,(GREEN),escalayscrollup)
            pg.draw.rect(screen,(BLUE),escalayscrolldown)
            
            pg.draw.rect(screen,(GREEN),positiveXsizescrollup)
            pg.draw.rect(screen,(BLUE),positiveXsizescrolldown)
            
            pg.draw.rect(screen,(GREEN),positiveYsizescrollup)
            pg.draw.rect(screen,(BLUE),positiveYsizescrolldown)
            
            pg.draw.rect(screen,(GREEN),negativeXsizescrollup)
            pg.draw.rect(screen,(BLUE),negativeXsizescrolldown)
            
            pg.draw.rect(screen,(GREEN),negativeYsizescrollup)
            pg.draw.rect(screen,(BLUE),negativeYsizescrolldown)
            
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
        else:
            pg.draw.rect(screen,(BLACK),Menu_pontos)
            pg.draw.rect(screen,(150,150,150),pontox)
            pg.draw.rect(screen,(150,150,150),pontoy)
            pg.draw.rect(screen,(GREEN),confirmar)
            pg.draw.rect(screen,(RED),limpar)
            
            texto1 = font.render('Ponto x',True,BLACK)
            texto2 = font.render('ponto y',True,BLACK)
            texto3 = font.render('confirmar',True,BLACK)
            texto4 = font.render(str(escolhax),True,BLACK)
            texto5 = font.render(str(escolhay),True,BLACK)
            texto6 = font.render('limpar',True,BLACK)
            
            screen.blit(texto1,(pontox.x-70,pontox.y))
            screen.blit(texto2,(pontoy.x-70,pontoy.y))
            screen.blit(texto3,(confirmar.x-70,confirmar.y))
            screen.blit(texto4,(pontox.x+5,pontox.y+5))
            screen.blit(texto5,(pontoy.x+5,pontoy.y+5))
            screen.blit(texto6,(limpar.x+5,limpar.y+5))
            if ativar_menu2:
                menu2 = pg.Rect(WIDTH-200,0,200,HEIGHT/1.5)
                pg.draw.rect(screen,(150,150,150),menu2)  
                texto7 = font.render('fazer linha entre quais' ,True,BLACK)
                texto8 = font.render('pontos?' ,True,BLACK)
                screen.blit(texto7,(menu2.x+10,menu2.y+5))
                screen.blit(texto8,(menu2.x+70,menu2.y+20))
                linhaponto1 = pg.Rect(menu2.x,menu2.y+50,menu2.w/2-5,90)
                linhaponto2 = pg.Rect(menu2.x+menu2.w/2+5,menu2.y+50,menu2.w/2-5,90)
                pg.draw.rect(screen,BLACK,linhaponto1)
                pg.draw.rect(screen,BLACK,linhaponto2)
    if escalax == '0':
        escalax = ''
    if escalay == '0':
        escalay = ''
    if positiveXsize == '0':
        positiveXsize = ''
    if positiveYsize == '0':
        positiveYsize = ''
    if negativeXsize == '0':
        negativeXsize = '-'
    if negativeYsize == '0':
        negativeYsize = '-'
        
def desenhar_grade():
    global escalax,escalay
    if escalax == '':
        escalax = '0'
    if escalay == '':
        escalay = '0'
    largura, altura = screen.get_size()
    escala_x = 10 * eval(escalax)
    escala_y = 10 * eval(escalay)
    cinza = (190,190,190)
    if escalax != '0':
        x = starting_point[0]
        while x < largura:
            pg.draw.line(screen, cinza, (x, 0), (x, altura))
            x += escala_x
        x = starting_point[0] - escala_x
        while x > 0:
            pg.draw.line(screen, cinza, (x, 0), (x, altura))
            x -= escala_x
    if escalay != '0':
        y = starting_point[1]
        while y < altura:
            pg.draw.line(screen, cinza, (0, y), (largura, y))
            y += escala_y
        y = starting_point[1] - escala_y
        while y > 0:
            pg.draw.line(screen, cinza, (0, y), (largura, y))
            y -= escala_y

    if escalax == '0':
        escalax = ''
    if escalay == '0':
        escalay = ''
pressed1 = False
pressed2 = False
def lerp(a,b,t):
    return a + (b-a) * t


def isvalid(input):
    valid = ['-']
    return input in valid
        
while run:
    
    screen.fill(WHITE)
    key = pg.key.get_pressed()
    desenhar_grade()
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
                
            if escalaxscrollup.collidepoint(event.pos):
                a = eval(escalax)
                a += 0.1
                escalax = str(round(a,2))
            if escalaxscrolldown.collidepoint(event.pos):
                a = eval(escalax)
                if a > 0:
                    a -= 0.1
                escalax = str(round(a,2))
                
            if escalayscrollup.collidepoint(event.pos):
                a = eval(escalay)
                a += 0.1
                escalay = str(round(a,2))
            if escalayscrolldown.collidepoint(event.pos):
                a = eval(escalay)
                if a > 0:
                    a -= 0.1
                escalay = str(round(a,2))
                
            if positiveXsizescrollup.collidepoint(event.pos):
                a = eval(positiveXsize)
                a += 1
                positiveXsize = str(a)
            if positiveXsizescrolldown.collidepoint(event.pos):
                a = eval(positiveXsize)
                if a > 0:
                    a -= 1
                positiveXsize = str(a)
            
            if positiveYsizescrollup.collidepoint(event.pos):
                a = eval(positiveYsize)
                a += 1
                positiveYsize = str(a)
            if positiveYsizescrolldown.collidepoint(event.pos):
                a = eval(positiveYsize)
                if a > 0:
                    a -= 1
                positiveYsize = str(a)
            
            if negativeXsizescrollup.collidepoint(event.pos):
                a = eval(negativeXsize)
                if a < 0:
                    a += 1
                negativeXsize = str(a)
            if negativeXsizescrolldown.collidepoint(event.pos):
                a = eval(negativeXsize)
                a -= 1
                negativeXsize = str(a)
            
            if negativeYsizescrollup.collidepoint(event.pos):
                a = eval(negativeYsize)
                if a < 0:
                    a += 1
                negativeYsize = str(a)
            if negativeYsizescrolldown.collidepoint(event.pos):
                a = eval(negativeYsize)
                a -= 1
                negativeYsize = str(a)
            
            if pontox.collidepoint(event.pos):
                active7 = True
            else:
                active7 = False
            if pontoy.collidepoint(event.pos):
                active8 = True
            else:
                active8 = False        
            if confirmar.collidepoint(event.pos):
                item = (eval(escolhax),eval(escolhay))
                pontos.append(item)
            if limpar.collidepoint(event.pos):
                pontos = []
            
        if event.type == pg.KEYDOWN:
            if active1:
                if event.key == pg.K_BACKSPACE: 
                    positiveXsize = positiveXsize[:-1] 
                elif event.unicode.isdigit() and event.unicode not in ['.','-']: 
                    positiveXsize += event.unicode
            if active2:
                if event.key == pg.K_BACKSPACE: 
                    positiveYsize = positiveYsize[:-1] 
                elif event.unicode.isdigit() and event.unicode not in ['.','-']: 
                    positiveYsize += event.unicode
            if active3:
                if event.key == pg.K_BACKSPACE: 
                    negativeXsize = negativeXsize[:-1] 
                elif event.unicode.isdigit() or isvalid(event.unicode): 
                    negativeXsize += event.unicode
                
            if active4:
                if event.key == pg.K_BACKSPACE: 
                    negativeYsize = negativeYsize[:-1] 
                elif event.unicode.isdigit() or isvalid(event.unicode): 
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
            if active7:
                if event.key == pg.K_BACKSPACE: 
                    escolhax = escolhax[:-1] 
                elif event.unicode.isdigit() or isvalid(event.unicode): 
                    escolhax += event.unicode
            if active8:
                if event.key == pg.K_BACKSPACE: 
                    escolhay = escolhay[:-1] 
                elif event.unicode.isdigit() or isvalid(event.unicode): 
                    escolhay += event.unicode
            
    if key[pg.K_p]:
        if pressed == False:
            pressed = True
            state = 'menu'
    else:
        pressed = False
    
    if key[pg.K_o]:
        if pressed1 == False:
            pressed1 = True
            ativar_menu2 = not ativar_menu2
    else:   
        pressed1 = False
    
    if key[pg.K_i]:
        if pressed2 == False:
            pressed2 = True
            
    else:
        pressed2 = False
    if key[pg.K_RIGHT]:
        coords[0] -= 0.1
        starting_point[0] -= 0.1
    if key[pg.K_DOWN]:
        coords[1] -= 0.1
        starting_point[1] -= 0.1
    if key[pg.K_UP]:
        coords[1] += 0.1
        starting_point[1] += 0.1
    if key[pg.K_LEFT]:
        coords[0] += 0.1
        starting_point[0] += 0.1
        
    if key[pg.K_d]:
        coords[0] -= 1
        starting_point[0] -= 1
    if key[pg.K_s]:
        coords[1] -= 1
        starting_point[1] -= 1
    if key[pg.K_w]:
        coords[1] += 1
        starting_point[1] += 1
    if key[pg.K_a]:
        coords[0] += 1
        starting_point[0] += 1
    pg.display.update()