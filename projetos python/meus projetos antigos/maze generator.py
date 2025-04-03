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
click = False
array = []
array0 = []
arraycopy = []
gridx = int(WIDTH/30)
gridy = int(HEIGHT/30)
grid = []
key_pressed_last_frame = False
key_pressed_last_frame1 = False
key_pressed_last_frame2 = False
key_pressed_last_frame3 = False
font = pg.font.SysFont("Arial", 10)
errors = []
start = False
def convert_index(i,j):
    if j == 1:
        index = 0+(gridx*i)
    else:
        index = j+(gridx*i)
    #print(index)
    return index
    
class cells:
    
    def __init__(self,pos,rect,i,j,recx,recy,recw,rech):
        self.x,self.y = pos
        self.rect = rect
        self.i = i
        self.j = j
        self.recx = recx
        self.recy = recy
        self.recw = recw
        self.rech = rech
        self.color = BLACK
        self.updat = False
        self.walls = [True,True,True,True]
        self.visited = False
        self.visited1 = False
        self.visited2 = False
    def render(self):
        #top right bottom left
        #tudo verdade
        #self.walls = [False,False,False,False]#tudo mentira
        #self.walls = [True,False,True,False]#sem a direita e esquerda
        #self.walls = [False,True,False,True]#sem o topo e embaixo
        
        #offset = 2
        self.recttop    = pg.Rect((self.recx,self.recy,self.recw,self.rech/10))
        self.rectright  = pg.Rect((self.recx-(2),self.recy,self.recw/10,self.rech))
        self.rectbottom = pg.Rect((self.recx,self.recy-(2),self.recw,self.rech/10))
        self.rectleft   = pg.Rect((self.recx,self.recy,self.recw/10,self.rech))
        #0 = nada
        #1 celula ja visitada
        #2 celula atual
        if not self.visited:
            pg.draw.rect(screen,(BLACK),self.rect)
        if array[self.i][self.j] == 1:
            pg.draw.rect(screen,(CYAN),self.rect)
        
        if array[self.i][self.j] == 2:
            pg.draw.rect(screen,(GREEN),self.rect)
            
        if self.walls[0]:#top
            pg.draw.rect(screen,(WHITE),self.recttop)
            
        if self.walls[1]:#right
            pg.draw.rect(screen,(WHITE),self.rectright)
            
        if self.walls[2]:#bottom
            pg.draw.rect(screen,(WHITE),self.rectbottom)
            
        if self.walls[3]:#left
            pg.draw.rect(screen,(WHITE),self.rectleft)
            
#resolver o bug da movimntação em grid, mesmo problema do sandbox,
#esta se movendo instantaneamente
    def update(self):
        ran = rand.randint(0,3)
        #ran = 2
        lastran = None
        #0 = nada
        #1 celula ja visitada
        #2 celula atual
        #top, right, bottom, left
        # 0 ,   1  ,   2   ,   3        
        
        if ran == 0 and (self.j-1 >= 0):#top
##            if False in self.walls:
##                self.visited = True
##            else:
##                self.visited = False
            if grid[convert_index(self.i,self.j)].visited == False:
                if False in self.walls:
                    self.visited = True
                else:
                    self.visited = False
                
                if not self.visited:
                    self.walls[0] = False
                    self.walls[2] = False
                
            array[self.i][self.j] = 1
            array[self.i][self.j-1] = 2     
        if ran == 1 and (self.i+1 < gridx):#right
##            if False in self.walls:
##                self.visited = True
##            else:
##                self.visited = False
            if grid[convert_index(self.i,self.j)].visited == False:
                
                if False in self.walls:
                    self.visited = True
                else:
                    self.visited = False
                    
                if not self.visited:
                    grai = grid[convert_index(self.i+1,self.j)]
                    grai.walls[1] = False
                    grai.walls[3] = False
                    
            array[self.i][self.j] = 1  
            array[self.i+1][self.j] = 2
                
        if ran == 2 and (self.j+1 < gridy):#bottom
##            if False in self.walls:
##                self.visited = True
##            else:
##                self.visited = False
            if grid[convert_index(self.i,self.j)].visited == False:
                
                if True in self.walls:
                    self.visited = False
                else:
                    self.visited = True
                    
                if not self.visited:
                    grai = grid[convert_index(self.i,self.j+1)]
                    grai.walls[0] = False
                    grai.walls[2] = False
                    
            array[self.i][self.j] = 1
            array[self.i][self.j+1] = 2       
        if ran == 3 and (self.i-1 >= 0):#left
##            if False in self.walls:
##                self.visited = True
##            else:
##                self.visited = False
            if grid[convert_index(self.i,self.j)].visited == False:
                
                if False in self.walls:
                    self.visited = True
                else:
                    self.visited = False
                    
                if not self.visited:
                    self.walls[1] = False
                    self.walls[3] = False
                    
            array[self.i][self.j] = 1
            array[self.i-1][self.j] = 2
            
        
                #camadas superiores não estão bonitas, estão toda ferradas
                    #arrumma isso caio 
def make_2d_array():
    
##    array.append(list1)
##    array.append(list2)
##    array.append(list3)
##    return array
    rai = rand.randint(5,gridx-5)
    raj = rand.randint(5,gridy-5)
    for i in range(gridx):
        temparray = []
        grid1 = []
        for j in range(gridy):
            #verifica se a celular esta no limite da grid
            if (i == 10 and  j == 10) :
                temparray.append(2)
            else: #faz a grid normal
                temparray.append(0)
            grid.append(cells(
                pg.mouse.get_pos(),
                pg.Rect((i*WIDTH/gridx,j*HEIGHT/gridy, WIDTH/gridx,HEIGHT/gridy)),
                i,
                j,
                i*WIDTH/gridx,#x 
                j*HEIGHT/gridy,#y
                WIDTH/gridx,#width
                HEIGHT/gridy#height
                #pg.Rect((X,Y,XSIZE,YSIZE))
                ))
        
        array.append(temparray)
    array0 = array
    arraycopy = array
    
    return array

bufferL = []

print(make_2d_array())

while run:
    
    key = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
            run = False
            
        #o down e up define um sistema de drag do mouse
        if (event.type == pg.MOUSEBUTTONDOWN) and (event.type != pg.MOUSEWHEEL):
            #é um clique normal
            click == True
            
            
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
    
    screen.fill((BLUE))
    for i,cell in enumerate(grid):
        cell.render()
        
        if array[cell.i][cell.j] == 2:
            if len(bufferL) == 1 :
                if start:
                    cell.update()
                    bufferL = []
                else:
                    print('im starting')
                    start = True
                    bufferL = []
            else:
                bufferL.append(1)
        if cell.rect.collidepoint(pg.mouse.get_pos()):
            print(cell.walls)
            
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




        
    
            
    pg.display.update()
    clock.tick(60)
pg.quit()
quit()
