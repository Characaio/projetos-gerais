import numpy as np
import turtle as turt
import time
import random as rand
from scipy import interpolate
import pygame as pg



pg.init()
pg.display.set_caption("me mata")
WIDTH,HEIGHT = 800,600
WHITE = (255,255,255)
BLACK = ((0,0,0))
screen = pg.display.set_mode((WIDTH,HEIGHT))
screen.fill((WHITE))
run = True
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
PINK = (255,0,255)
AMARELO = (255,255,0)
pontos = [
    
]
pos = []


key_pressed_last_frame = False
    

    
def clear():
    screen.fill(WHITE)

def draw(i,c,dir,repetion,mouse):
    multi = 10    
    wideness = 0.8 #quanto menor esse valor, mais estreito a parabaola vai ser, quanto maior, mais larga
    if not mouse:
        if dir == 1:
            y =  500 + (i**2*dir - (repetion-1)*i + c) 
            x =  WIDTH/4 + i * multi * wideness
        else:
            y =  0 + (i**2*dir + (repetion-1)*i + c) 
            x =  WIDTH/4 + i * multi * wideness
    else:
        
        
        if dir == 1:
            y = pg.mouse.get_pos()[1] + (i**2*dir - (repetion-1)*i + c) 
            x = pg.mouse.get_pos()[0] + i*multi*wideness
        else:
            y =  (pg.mouse.get_pos()[1]/2) + (i**2*dir + (repetion-1)*i + c) 
            x = pg.mouse.get_pos()[0] + i*multi*wideness
       
    return (x,y)
while run:
    mouse =  None
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
                mouse = left_mouse
                clear()
            if middle_mouse:
                pos = pg.mouse.get_pos()
                
            if right_mouse:
                pos = pg.mouse.get_pos()
    repetion = 41
      
    for i in range(repetion):
        
        pg.draw.circle(screen,(BLACK),(draw(i,50,1  ,repetion,mouse)),4)
        pg.draw.circle(screen,(BLUE) ,(draw(i,19,1  ,repetion,mouse)),4)
        pg.draw.circle(screen,(GREEN),(draw(i,0,1   ,repetion,mouse)),4)
        pg.draw.circle(screen,(BLACK),(draw(i,50,-1 ,repetion,mouse)),4)
        pg.draw.circle(screen,(BLUE) ,(draw(i,19,-1 ,repetion,mouse)),4)
        pg.draw.circle(screen,(GREEN),(draw(i,0,-1  ,repetion,mouse)),4)
        
        
        
    pg.display.update()
    


        