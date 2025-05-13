import pygame as pg
import numpy as np
pg.init()

WIDTH,HEIGHT = 600,600

screen = pg.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
VIOLET = (255,0,255)
GREEN = (0,255,0)
#pg.Rect(x,y, width, height)
Xaxis = pg.Rect(10,10,80,50)
Yaxis = pg.Rect(10,65,80,50)
parabola = pg.Rect(10,120,80,50)
Xsize = pg.Rect(10,175,80,50)
Ysize = pg.Rect(10,240,80,50)
moldura = pg.Rect(100,100,500,500)
canva = pg.Rect(105,105,490,490)
starting_point = (130,570)
limitex,limitey = (570,570),(130,130)
linha = pg.Rect(128,130,4,445)
linha1 = pg.Rect(130,568,445,4)
run = True
tamanhoX,tamanhoY = 10,10
font = pg.font.SysFont("arial black", 15)
font1 = pg.font.SysFont("arial black", 10)

active = False
escala_geral = [0,0]
user_text1 = ''
user_text2 = ''
user_text3 = ''
user_text4 = ''
user_text5 = '-i**2+i*9+4'
active1 = False
active2 = False
active3 = False
active4 = False
active5 = False
color = (0,0,0)

pontos = []
estado = 'grafico'
escolhax = 20
escolhay = 10
user_text3 = escolhax
user_text4 = escolhay
highest_number = escolhay
def update():
    global user_text1,user_text2,user_text3,user_text4,user_text5,active1,active2,color1,color2,color5,estado,escolhax,escolhay,highest_number
    pg.draw.rect(screen,color1,Xaxis)
    pg.draw.rect(screen,color2,Yaxis)
    pg.draw.rect(screen,color5,parabola)
    pg.draw.rect(screen,color3,Xsize)
    pg.draw.rect(screen,color4,Ysize)
    pg.draw.rect(screen,BLACK,moldura)
    pg.draw.rect(screen,WHITE,canva)
    pg.draw.rect(screen,BLACK, linha)
    pg.draw.rect(screen,BLACK, linha1)
    
    pg.draw.circle(screen,(255,0,0),starting_point, 5)
    pg.draw.circle(screen,(0,0,255), limitex , 4)
    pg.draw.circle(screen,(0,0,255), limitey , 4)
    
    surf1 = font.render('x',True, BLACK)
    surf2 = font.render('y',True, BLACK)
    surf3 = font.render('parabola',True,BLACK)
    
    text_surface1 = font.render(user_text1,True,(WHITE))
    text_surface2 = font.render(user_text2,True,(WHITE))
    text_surface3 = font1.render(user_text5,True,(WHITE))
    text_surface4 = font.render(str(user_text3),True,(WHITE))
    text_surface5 = font.render(str(user_text4),True,(WHITE))
    
    screen.blit(surf1,(Xaxis.x+Xaxis.w+5,Xaxis.y))
    screen.blit(surf2,(Yaxis.x+Yaxis.w+5,Yaxis.y))
    screen.blit(surf3,(parabola.x,parabola.y))
    screen.blit(text_surface1,(Xaxis.x+5,Xaxis.y))
    screen.blit(text_surface2,(Yaxis.x+5,Yaxis.y))
    screen.blit(text_surface3,(parabola.x+5,parabola.y))
    screen.blit(text_surface4,(Xsize.x+5,Xsize.y))
    screen.blit(text_surface5,(Ysize.x+5,Ysize.y))
    
    
        
    if user_text1 != '' and eval(user_text1) > escolhax and (not active3):
        escolhax = eval(user_text1)
        user_text3 = user_text1
    
    if user_text2 != '' and eval(user_text2) > escolhay and (not active4):
        escolhay = eval(user_text2)
        user_text4 = user_text2
        
        
    if user_text3 != '' and type(user_text3) != int:
        escolhax = eval(user_text3)
    
    user_text4 = str(user_text4)
    if user_text4 != '' and type(user_text4) != int:
        escolhay = eval(user_text4)
    if estado == 'parabola':
        for cell in pontos:
            if cell[1] > highest_number:
                highest_number = cell[1]
                
        escolhay = highest_number
    
    
    for i in range(0,escolhax):
        escalax = (i*(570-130)/escolhax)
        text1 = font.render(str(escolhax), True, BLACK)
        texta = font.render(str(i), True, BLACK)
        screen.blit(texta,(starting_point[0]+escalax-5,starting_point[1]-25))
        if i != 0:
            screen.blit(text1,(limitex[0]-5,limitex[1]-25))
            pg.draw.circle(screen,GREEN,(starting_point[0]+escalax,starting_point[1]),3)
            
    
    for j in range(0,escolhay):
        escalay = (j*(570-130)/escolhay)
        text2 = font.render(str(escolhay), True, BLACK)
        textb = font.render(str(j), True, BLACK)
        screen.blit(textb,(starting_point[0]+5,starting_point[1]-escalay-8))
        if j != 0:
            screen.blit(text2,(limitey[0]+5,limitey[1]-8))
            pg.draw.circle(screen,GREEN,(starting_point[0],starting_point[1]-escalay),3)
    if user_text1 != '' and user_text2 != '':
        if estado == 'grafico':
            valor1 = eval(user_text1)
            valor2 = eval(user_text2)
            linhaA = pg.Rect(starting_point[0]+escala_geral[0]*valor1-2,starting_point[1]-escala_geral[1]*valor2,3,escalay*valor2)
            linhaB = pg.Rect(starting_point[0],starting_point[1]-escala_geral[1]*valor2,escala_geral[0]*valor1,3)
            pg.draw.rect(screen,YELLOW, linhaA)
            pg.draw.rect(screen,VIOLET, linhaB)
    escala_geral[0] = (570-130)/escolhax
    escala_geral[1] = (570-130)/escolhay
        #print(escala_geral)
    

def criar_pontos():
    global user_text1,user_text2,escolhax,escolhay,highest_nuumber
    if user_text1 != '' and user_text2 != '' and estado == 'grafico' :
        x,y = eval(user_text1),eval(user_text2)
        pg.draw.circle(screen,(BLACK),(starting_point[0]+escala_geral[0]*x, starting_point[1]-escala_geral[1]*y),4)
    elif estado == 'parabola':

        escolhay = highest_number
        
        for i,cell in enumerate(pontos):
            #print(cell)
            pg.draw.circle(screen,YELLOW,(starting_point[0]+(escala_geral[0]*cell[0]),starting_point[1]-(escala_geral[1]*cell[1])),4)
operators = {'+', '-', '*', '/'}    

def is_operator(input_char):
    return input_char in operators  
  
def fazer_parabola():
    
    global estado,user_text5,pontos
    for i in range(0,10):
        socorro = [i, int(eval(user_text5))]
        #socorro =[i,-i**2+i*8+4]
        pontos.append(socorro)
    estado = 'parabola'

def inicio():
    global pontos,estado,user_text1,Ysize,Xsize,user_text2,user_text3,user_text4,user_text5,active1,active2,active3,active4,active5,color1,color2,color3,color4,color5
    run = True
    while run:
        screen.fill(WHITE)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if Xaxis.collidepoint(event.pos):
                    active1 = True
                else:
                    active1 = False
                if Yaxis.collidepoint(event.pos):
                    active2 = True
                else:
                    active2 = False
                if parabola.collidepoint(event.pos):
                    fazer_parabola()
                    # pontos = []
                    active5 = True
                else:
                    active5 = False
                if Xsize.collidepoint(event.pos):
                    active3 = True
                else:
                    active3 = False
                if Ysize.collidepoint(event.pos):
                    active4 = True
                else:
                    active4 = False
                
            if event.type == pg.KEYDOWN:
                if active1:
                    if event.key == pg.K_BACKSPACE: 
                        user_text1 = user_text1[:-1] 
                    elif event.unicode.isdigit(): 
                        user_text1 += event.unicode
                if active2:
                    if event.key == pg.K_BACKSPACE: 
                        user_text2 = user_text2[:-1] 
                    elif event.unicode.isdigit(): 
                        user_text2 += event.unicode
                if active3:
                    estado = 'grafico'
                    user_text3 = str(user_text3)
                    if event.key == pg.K_BACKSPACE: 
                        user_text3 = user_text3[:-1] 
                    elif event.unicode.isdigit(): 
                        user_text3 += event.unicode
                if active4:
                    estado = 'grafico'
                    user_text4 = str(user_text4)
                    if event.key == pg.K_BACKSPACE: 
                        user_text4 = user_text4[:-1] 
                    elif event.unicode.isdigit() or event.unicode.isoperator(): 
                        user_text4 += event.unicode
                if active5:
                    user_text5 = str(user_text5)
                    if event.key == pg.K_BACKSPACE: 
                        user_text5 = user_text5[:-1] 
                    elif event.unicode.isdigit() or is_operator(event.unicode): 
                        user_text5 += event.unicode
            
        if active1:
            color1 = (127,127,127)
        else:
            color1 = (0,0,0)
            
        if active2:
            color2 = (127,127,127)
        else:
            color2 = (0,0,0)
            
        if active3:
            color3 = (127,127,127)
        else:
            color3 = (0,0,0)
            
        if active4:
            color4 = (127,127,127)
        else:
            color4 = (0,0,0)
        
        if active5:
            color5 = (127,127,127)
        else:
            color5 = (0,0,0)
            
        update()
        criar_pontos()
        pg.display.flip()
    quit()

if __name__ == "__main__":
    inicio()