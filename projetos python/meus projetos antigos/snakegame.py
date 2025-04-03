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
clicking = False
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
##snake variables##
snakeind = []
length = 6
apple_spawn = False
direction = 0
class cells:
    
    def __init__(self,pos,rect,i,j):
        self.x,self.y = pos
        self.rect = rect
        self.i = i
        self.j = j
        self.color = BLACK
        self.updat = False
        
    def render(self):
        #0 = nada
        #1 = cobra
        #2 = pareda
        #3 = maçã
        if array[self.i][self.j] == 1:
            self.color = (0,255,0)
            
            #print(f'the list is {snakeind} and the item that gonna be in will be ({self.i}, {self.j})')
            if (self.i,self.j) not in snakeind:
                snakeind.append((self.i,self.j))
                
            if len(snakeind) > length:
                #print(f'im deleting item {snakeind[0]} from {snakeind}')
                del snakeind[0]
            
            for i in range(len(snakeind)):
                self.rect = pg.Rect((snakeind[i][0]*WIDTH/gridx,snakeind[i][1]*HEIGHT/gridy,
                                 WIDTH/gridx-1,HEIGHT/gridy-1))
                
                pg.draw.rect(screen,(self.color),self.rect)
        if array[self.i][self.j] == 2:
            self.color = (255,0,0)
            pg.draw.rect(screen,(self.color),self.rect)

        if array[self.i][self.j] == 3:
            self.color = (255,0,255)
            pg.draw.rect(screen,(self.color),self.rect)
        
            
        


#resolver o bug da movimntação em grid, mesmo problema do sandbox,
#esta se movendo instantaneamente
    def update(self):
        ri = rand.randint(1,gridx-2)
        rj = rand.randint(1,gridy-2)
        global length
        global apple_spawn
        if (not apple_spawn):
            if ((ri,rj) not in snakeind):
                
                array[ri][rj] = 3
                apple_spawn = True
                
##        print('im updatinnnnnng')
        #abovegrid = array[self.i][self.j-1]
        #belowgrid = array[self.i][self.j+1]
        #rightgrid = array[self.i+1][self.j]
        #leftgrid  = array[self.i-1][self.j]
        
        if direction == 2:#S
            
            if (array[self.i][self.j+1] == 2) or ((self.i,self.j+1) in snakeind):
                print('game over S')
                print(snakeind)
                print(len(snakeind))
                pg.quit()
                quit()
                
            if (array[self.i][self.j+1] == 3):
                print('i ate an apple S')
                print(f'my size now is {length}')
                apple_spawn = False
                length += 1
                array[self.i][self.j+1] = 0
            if (self.j+1 < int(gridx-1)):
                    array[self.i][self.j+1] = 1
                    array[self.i][self.j] = 0
                    print(self.j)
            
                    
        if direction == 4: #A
            
            if (array[self.i-1][self.j] == 2) or ((self.i-1,self.j) in snakeind):
                print('game over A')
                print(snakeind)
                print(len(snakeind))
                pg.quit()
                quit()
                
            if (array[self.i-1][self.j] == 3):
                print('i ate an apple A')
                print(f'my size now is {length}')
                apple_spawn = False
                length += 1
                array[self.i-1][self.j] = 0
            if (self.i-1 > 0):
                array[self.i-1][self.j] = 1
                array[self.i][self.j] = 0
                print(self.i)
            
        if direction == 6:#D
            
            if (array[self.i+1][self.j] == 2) or ((self.i+1,self.j) in snakeind):
                print('game over D')
                print(snakeind)
                print(len(snakeind))
                pg.quit()
                quit()
                
            if (array[self.i+1][self.j] == 3):
                print('i ate an apple D')
                print(f'my size now is {length}')
                apple_spawn = False
                length += 1
                array[self.i+1][self.j] = 0
            if (self.i+1 < int(gridx-1)):
                array[self.i+1][self.j] = 1
                array[self.i][self.j] = 0
                print(self.i)
            
        if direction == 8:#W
            
            if (array[self.i][self.j-1] == 2) or ((self.i,self.j-1) in snakeind):
                print('game over W')
                print(snakeind)
                print(len(snakeind))
                pg.quit()
                quit()
                
            if (array[self.i][self.j-1] == 3):
                print('i ate an apple W')
                print(f'my size now is {length}')
                apple_spawn = False
                length += 1
                array[self.i][self.j-1] = 0
                
            if (self.j-1 > 0):
                array[self.i][self.j-1] = 1
                array[self.i][self.j] = 0
                print(self.j)
                
def make_2d_array():
    
##    array.append(list1)
##    array.append(list2)
##    array.append(list3)
##    return array
    rai = rand.randint(5,gridx-5)
    
    
    raj = rand.randint(5,gridy-5)
    for i in range(gridx):
        temparray = []
        for j in range(gridy):
            #verifica se a celular esta no limite da grid
            if (i == 0 or j == 0) or (i == gridx-1 or j == gridy-1):
                temparray.append(2)
            elif (i == rai) and (j == raj):
                temparray.append(1)
            else: #faz a grid normal
                temparray.append(0)
            grid.append(cells(
                pg.mouse.get_pos(),
                 pg.Rect((i*WIDTH/gridx,j*HEIGHT/gridy, WIDTH/gridx,HEIGHT/gridy)),
                i,
                j
                #pg.Rect((X,Y,XSIZE,YSIZE))
                ))
        array.append(temparray)
    array0 = array
    arraycopy = array
    alive = True
    return array
print(make_2d_array())



    
while run:
    clock.tick(60)
    key = pg.key.get_pressed()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            print(array)
            run = False
            quit()
        if (event.type == pg.MOUSEBUTTONDOWN) and (event.type != pg.MOUSEWHEEL):
            clicking = True
        
            
    screen.fill((BLACK))
    
    for i,cell in enumerate(grid):
        
        cell.render()
        if array[cell.i][cell.j] == 1:
            
            if (len(bufferL) > 7) and (not pause):
                    clock.tick(800)
                    cell.update()
                    bufferL = []
            else:
                 bufferL.append(1)
        
    
       
        
        
    
    
    if key[pg.K_w] or key[pg.K_UP]:#8
        if not key_pressed_last_frame:#isso verifica se a tecla esta pressionada no ultimo frame
            if direction != 2:
                direction = 8
                print(direction)
        key_pressed_last_frame = True#isso atualiza o estado  
    else:
        key_pressed_last_frame = False #isso vira falso quando a tecla não esta


    if key[pg.K_a] or key[pg.K_LEFT]:#4
        if not key_pressed_last_frame1:#isso verifica se a tecla esta pressionada no ultimo frame
            if direction != 6:
                direction = 4
                print(direction)
        key_pressed_last_frame1 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame1 = False #isso vira falso quando a tecla não esta

        
    if key[pg.K_s] or key[pg.K_DOWN]:#2
        if not key_pressed_last_frame2:#isso verifica se a tecla esta pressionada no ultimo frame
            if direction != 8:
                direction = 2
                print(direction)
        key_pressed_last_frame2 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame2 = False #isso vira falso quando a tecla não esta

        
    if key[pg.K_d] or key[pg.K_RIGHT]:#6
        if not key_pressed_last_frame3:#isso verifica se a tecla esta pressionada no ultimo frame
            if direction != 4:
                direction = 6
                print(direction)
        key_pressed_last_frame3 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame3 = False #isso vira falso quando a tecla não esta

                
    if key[pg.K_p] == True: 
        if not key_pressed_last_frame5:#isso verifica se a tecla esta pressionada no ultimo frame
            #coloca algo
            pause = not pause
        key_pressed_last_frame5 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame5 = False #isso vira falso quando a tecla não esta
        
    pg.display.update()
    
pg.quit()
quit()

##    if key[pg.K_z] == True: 
##        if not key_pressed_last_frame:#isso verifica se a tecla esta pressionada no ultimo frame
##            #coloca algo
##            pass
##        key_pressed_last_frame = True#isso atualiza o estado  
##    else:
##        key_pressed_last_frame = False #isso vira falso quando a tecla não esta
##
##
##    if key[pg.K_t] == True: 
##        if not key_pressed_last_frame2:#isso verifica se a tecla esta pressionada no ultimo frame
##            #coloca algo
##            pass
##        key_pressed_last_frame2 = True#isso atualiza o estado  
##    else:
##        key_pressed_last_frame2 = False #isso vira falso quando a tecla não esta
