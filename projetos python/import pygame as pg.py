import pygame as pg
import numpy as np
import simuladordegrafico as sg
pg.init()

WIDTH,HEIGHT = 600,600

screen = pg.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
BLACK = (0,0,0)
#pg.Rect(x,y, width, height)
Xaxis = pg.Rect(10,10,50,80)

moldura = pg.Rect(100,100,500,500)
canva = pg.Rect(105,105,490,490)
starting_point = (130,570)
limitex,limitey = (570,570),(130,130)
linha = pg.Rect(128,130,4,445)
linha1 = pg.Rect(130,568,445,4)
run = True
tamanhoX,tamanhoY = 10,10
font = pg.font.Font(None, 36)


def main():
    run = True
    while run:
        screen.fill(WHITE)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        sg.update()
                
        pg.display.flip()
    quit()

if __name__ == "__main__":
    main()