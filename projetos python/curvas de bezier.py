import numpy as np
import turtle as turt
import time
import random as rand

import pygame as pg


pg.init()
pg.display.set_caption("me mata")
WIDTH,HEIGHT = 800,600
WHITE = (255,255,255)
BLACK = ((0,0,0))
screen = pg.display.set_mode((WIDTH,HEIGHT))
screen.fill((WHITE))

GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
PINK = (255,0,255)
AMARELO = (255,255,0)
ROXO = (255,0,255)
pontos = [
    
]
pos = []
multi = 10
clock = pg.time.Clock()

# p4 = (700, 300)
# p5 = (625,50)
FPS = 60
key_pressed_last_frame = False
    
def lerp(p1,p2,t):
    return p1 + (p2 - p1) * t

def lerp_quadratica(p1,p2,p3,t):
    x1 = lerp(p1[0],p2[0], t)
    y1 = lerp(p1[1],p2[1], t)
    x2 = lerp(p2[0],p3[0], t)
    y2 = lerp(p2[1],p3[1], t)
    x = lerp(x1,x2,t)
    y = lerp(y1,y2,t)
    return (x,y)

def lerp_cubica(p1,p2,p3,p4,t):
    v1 = (lerp_quadratica(p1,p2,p3,t))
    v2 = (lerp_quadratica(p2,p3,p4,t))
    x = lerp(v1[0], v2[0], t)
    y = lerp(v2[1], v2[1], t)
    return (x,y)
def lerp_quadrupla(p1,p2,p3,p4,p5,t):
    v2 = lerp_cubica(p1,p2,p3,p4,t)
    v1 = lerp_cubica(p2,p3,p4,p5,t)
    x = lerp(v1[0], v2[0], t)
    y = lerp(v2[1], v2[1], t)
    return (x,y)
    
def clear():
    screen.fill(WHITE)

def main():
    run = True
    p1 = (100,300)
    p2 = (250,250)
    p3 = (300,150)
    p4 = (400,300)
    p5 = (50,400)
    while run:
        clock.tick(FPS)
        key = pg.key.get_pressed()
        n = 0.001
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                left_mouse, middle_mouse, right_mouse = pg.mouse.get_pressed()
                clear()
                if left_mouse:
                    pos = pg.mouse.get_pos()
                    p1 = pos
                if middle_mouse:
                    pos = pg.mouse.get_pos()
                    p2 = pos
                if right_mouse:
                    pos = pg.mouse.get_pos()
                    p3 = pos
        
        
        
        if key[pg.K_w]:
            # p1 puxa a linha
            p3 = pg.mouse.get_pos()
            clear()
            
        if key[pg.K_a]:
            # p2 ponto que escolhe o Y do fim da linha
            p2 = pg.mouse.get_pos()
            clear()
        
        if key[pg.K_d]:
            # p3 ponto que escolhe o X do fim da linha
            p1 = pg.mouse.get_pos()
            clear()
            
        if key[pg.K_s]:
            # p4 ponto ancora
            p4 = pg.mouse.get_pos()
            clear()
        if key[pg.K_e]:
            p5 = pg.mouse.get_pos()
            clear()
        
        for t in np.arange(0,1,n):
            #lerp_cubica(a,b,c,d,t) explicação:
            # a/p1 decide o x do fim da linha
            # b/p2 decide o y do fim da linha
            # c/p3 decide o quão puxada vai ser a linha
            # d/p4 decide o inicio da linha
            
            x,y = lerp_quadrupla(p1,p2,p3,p4,p5,t)
            pg.draw.circle(screen,((GREEN)),(x,y),1) # linha interpolada
            pg.draw.circle(screen,((RED)),(p1),3)    # ponto que puxa
            pg.draw.circle(screen,((BLUE)),(p2),3)   # ponto que escolhe o y
            pg.draw.circle(screen,((PINK)),(p3),3)   # potno que escolhe o x
            pg.draw.circle(screen,((AMARELO)),(p4),3)# ancora
            pg.draw.circle(screen,((ROXO)),(p5),3)
            
        pg.display.update()
    
    
    
if __name__ == "__main__":
    main()


        