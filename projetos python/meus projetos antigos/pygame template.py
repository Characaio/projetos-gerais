#basic pygame template

import pygame as pg
import random as rand
import math
pg.init()

WIDTH,HEIGHT = 600,600
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
clock = pg.time.Clock()
pause = False
run = True
array = []
array0 = []
arraycopy = []
gridx = int(WIDTH/30)
gridy = int(HEIGHT/30)
grid = []
bufferL = []
key_pressed_last_frame = False
key_pressed_last_frame1 = False
key_pressed_last_frame2 = False
key_pressed_last_frame3 = False
font = pg.font.SysFont("Arial", 10)

            
        

while run:
    
    key = pg.key.get_pressed()
    
    
    screen.fill((BLACK))


    if key[pg.K_z] == True: 
        if not key_pressed_last_frame:#isso verifica se a tecla esta pressionada no ultimo frame
            #coloca algo
            pass
        key_pressed_last_frame = True#isso atualiza o estado  
    else:
        key_pressed_last_frame = False #isso vira falso quando a tecla não esta

    if key[pg.K_p] == True: 
        if not key_pressed_last_frame1:#isso verifica se a tecla esta pressionada no ultimo frame
            #coloca algo
            pause = not pause
        key_pressed_last_frame1 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame1 = False #isso vira falso quando a tecla não esta

    if key[pg.K_t] == True: 
        if not key_pressed_last_frame2:#isso verifica se a tecla esta pressionada no ultimo frame
            #coloca algo
            pass
        key_pressed_last_frame2 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame2 = False #isso vira falso quando a tecla não esta




        
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
            run = False
            
        #o down e up define um sistema de drag do mouse
        if (event.type == pg.MOUSEBUTTONDOWN) and (event.type != pg.MOUSEWHEEL) and (not erasing):
            #é um clique normal
            pass
            
            
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
