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

def cubica(a,b,c,d,x):
    return (a*x**3) + (b*x**2) + (c*x) + d == 0 
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
                
            if middle_mouse:
                pos = pg.mouse.get_pos()
                
            if right_mouse:
                pos = pg.mouse.get_pos()
    for i in range(40):
        pass
        
        
        
    pg.display.update()
    


        