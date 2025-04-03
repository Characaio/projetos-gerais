import pygame as pg
import numpy as np
import math

pg.init()
WIDTH,HEIGHT = 500,500
screen = pg.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
BLACK = (0,0,0)
clock = pg.time.Clock()
size = 2
body_parts = []
def normalize(v):
    norm = np.linalg.norm(v)

    if norm == 0:
         return v
    return v / norm

class body:
    def __init__(self,pos,radius):
        self.pos = list(pos)
        self.radius = 30
        self.constraint = 0
    def render_circle(self):
        pg.draw.circle(screen,(0,255,0),(self.pos),self.radius)
        pg.draw.circle(screen,(0,255,0),(self.pos[0] + self.radius, self.pos[1] + self.radius),self.radius)
        x,y = pg.mouse.get_pos()[0]/100, pg.mouse.get_pos()[1]/100
        
        dx = self.pos[0] - pg.mouse.get_pos()[0]
        dy = self.pos[1] - pg.mouse.get_pos()[1]
        print(f'{dx}: {dy}')
        
        
        self.pos[0] -= dx/100
        self.pos[1] -= dy/100
        
def clear():
    screen.fill(BLACK)  


        

def main():
    idx = 0
    key = pg.key.get_pressed()
    x,y = 0,0
    run = True
    p1 = body((100,100), 30)
    while run:
        clear()
        print(1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        print(2)
       
        
        print(3)
        p1.render_circle()
        
            
        print(4)
        clock.tick(60)
        pg.display.update()
    pg.quit()

main()