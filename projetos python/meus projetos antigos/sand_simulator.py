import pygame as pg
import random as rand
import math
import numba
pg.init()

WIDTH,HEIGHT = 600,600
screen = pg.display.set_mode((WIDTH,HEIGHT))
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
clock = pg.time.Clock()
run = True
array = []
array0 = []
arraycopy = []
grid = []
grid1 = []
gridx = int(WIDTH/8)
gridy = int(HEIGHT/8)
##gridx = int(WIDTH/10)
##gridy = int(HEIGHT/10)
clicking = False
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]
list3 = [1,2,3,4,5]
solids = [1,2]
pause = False
key_pressed_last_frame = False
key_pressed_last_frame1 = False
key_pressed_last_frame2 = False
key_pressed_last_frame3 = False
key_pressed_last_frame4 = False
key_pressed_last_frame5 = False
key_pressed_last_frame6 = False
key_pressed_last_frame7 = False
key_pressed_last_frame8 = False
key_pressed_last_frame9 = False
key_pressed_last_frame10 = False
font = pg.font.SysFont("Arial", 10)
qpartic = 0
cpartic = 0
##[[1, 2, 3, 4, 5],
## [6, 7, 8, 9, 0],
## [1, 2, 3, 4, 5]]
ptype = 'sand'

def i_in_bounds(i):
    if (i+1 < gridx) or (i-1 > 0):
        return True
def j_in_bounds(j):
    if (j+1 < gridy) or (j-1 > 0):
        return True
class cells:
    def __init__(self,pos,rect,i,j):
        self.x,self.y = pos
        self.rect = rect
        self.state = False
        self.i = i
        self.j = j
        self.color = BLACK
        self.color1 = 0
        self.color2 = 0
        self.color3 = 255
        self.below = 0
        self.draw = False
        
        self.frames = []
    
    def render(self):
##        print(array[self.i][self.j]
        
        if array[self.i][self.j] == 1:
            
            pg.draw.rect(screen,(self.color),self.rect)
        elif array[self.i][self.j] == 2:
            self.color = RED
            pg.draw.rect(screen,(self.color),self.rect)
            
        
        

    def update(self):
        self.ptype = ptype
        
        
        if self.ptype == 'sand':
            
            self.color = BLUE
            self.ra = rand.randint(-1,1)
            #checa se os parametros que irei usar esta dentro da lista
            if (self.j+1 < gridy) and (self.j-1 > 0) and (self.i+1 < gridx) and (self.i-1 > 0):
                if ((array[self.i+1][self.j+1] == 1) and
                    (array[self.i-1][self.j+1] == 1) and
                    (array[self.i][self.j+1] == 1)):
                    if len(self.frames) > 60:
                        self.state = True
                    else:
                        self.state = False
                        
                if self.state == False:
                    #verifica se o item é uma particula
                    if array[self.i][self.j] == 1:
                        #verifica se a celular abaixo esta vazia
                        if array[self.i][self.j+1] == 0:
                            #atualiza o array
                            array[self.i][self.j] = 0
                            array[self.i][self.j+1] = 1
                        #verifica oque acontecera com a particula se a celular abaixo estiver ocupada
                        else:
                             #define o aleatorio
                            #faz com que a celula va a direita

                            if self.ra == 1:
                                if array[self.i+1][self.j+1] == 0:
                                    array[self.i+1][self.j+1] = 1
                                    array[self.i][self.j] = 0
                            elif self.ra == -1:
                                if array[self.i-1][self.j+1] == 0:
                                    array[self.i-1][self.j+1] = 1
                                    array[self.i][self.j] = 0
                                
            
        if self.ptype == 'liquid':
            
            
            self.color = YELLOW
            self.ra = rand.randint(-1,1)
            #checa se os parametros que irei usar esta dentro da lista
            if (self.j+1 < gridy) and (self.j-1 > 0) and (self.i+1 < gridx) and (self.i-1 > 0):
                if ((array[self.i+1][self.j+1] == 1) and
                    (array[self.i-1][self.j+1] == 1) and
                    (array[self.i][self.j+1] == 1)):
                    if len(self.frames) > 60:
                        self.state = True
                    else:
                        self.state = False
                        
                if self.state == False:
                    #verifica se o item é uma particula
                    if array[self.i][self.j] == 1:
                        #verifica se a celular abaixo esta vazia
                        if array[self.i][self.j+1] == 0:
                            #atualiza o array
                            array[self.i][self.j] = 0
                            array[self.i][self.j+1] = 1
                        #verifica oque acontecera com a particula se a celular abaixo estiver ocupada
                        else:
                            #print('updating')
                            #print(f'loop update of {r}')
                            #define o aleatorio
                            #faz com que a celula va a direita
                            qa = 0
                            if self.ra == 1:
                                
                                if qa < 6:
                                    if array[self.i+1][self.j] == 0:
                                        qa += 1
                                        #print(f'positive loop of i:{i}, and of r:{r}')
                                        array[self.i+1][self.j] = 1
                                        array[self.i][self.j] = 0
                                
                            if self.ra == -1:
                                if qa < 6:
                                    if array[self.i-1][self.j] == 0:
                                        qa += 1
                                        #print(f'negative loop of i:{i}, and of r:{r}')
                                        array[self.i-1][self.j] = 1
                                        array[self.i][self.j] = 0
                                
                                
        if self.ptype == 'gas':
            #print('gas not implemented yet')
            pass
        if self.ptype == 'solid':
            #print('solids not implemented yet')
            pass
#implementar os diferentes tipos de particulas
#tambem implementar uma maneira para elas ainda se atualizarem independentemente do tipo atual
#tambem implementar os diferentes tipos de comportamentos para cada particula
#como gas, liquido e solido

                
#eu não sei o porque
#eu não sei qual motivo
#EU NÃO SEI PORQUE QUAL MOTIVO EM TODO UNIVERSO
#mas sem o "and array[self.i+rand.randint(-2,2)][self.j]" as particulas não cai devagar
#com isso a particula cai devagar, meio travadão, mas cai devagar igual uma particula
#sem ele, a particula jorra igual agua pra baixo
#fica ai a dica se você quiser implementar um tipo de despejo automatico de particulas
                    
                
            
        
def make_2d_array():
    
##    array.append(list1)
##    array.append(list2)
##    array.append(list3)
##    return array

    for i in range(gridx):
        temparray = []
        for j in range(gridy):
            #verifica se a celular esta no limite da grid
            if (i == 0 or j == 0) or (i == gridx-1 or j == gridy-1):
                temparray.append(2)
            else: #faz a grid normal
                temparray.append(0)
            grid.append(cells(
                pg.mouse.get_pos(),
                pg.Rect((i*WIDTH/gridx,j*HEIGHT/gridy, WIDTH/gridx,HEIGHT/gridy
                         )),
                i,
                j
                #pg.Rect((X,Y,XSIZE,YSIZE))
                ))
        array.append(temparray)
    array0 = array
    arraycopy = array
    return array

print(make_2d_array())
erasing = False
buffer1 = 0
bufferL = []
size = 1
opacity = 0
stream = False

while run:
    
    key = pg.key.get_pressed()
    
    clicked = False
    screen.fill((BLACK))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
            run = False
        #o down e up define um sistema de drag do mouse
        if (event.type == pg.MOUSEBUTTONDOWN) and (event.type != pg.MOUSEWHEEL):
            clicking = True
        if event.type == pg.MOUSEBUTTONUP and (event.type != pg.MOUSEWHEEL):
            clicking = False
        if event.type == pg.MOUSEWHEEL:
            if event.y == 1:
                size += 1
                #print(size)
            if event.y == -1:
                if size > 1:
                    #print(size)
                    size -= 1
            
            
    
            
    for p,cell in enumerate(grid):
        #spawna uma particula
        cell.render()
        
        if not pause:
            if stream:
            
                if len(buffer1) > 1:
                    cell.update()
                    buffer = 0
                else:
                    buffer1 += 1
            if not stream:
                bufferL.append(1)
                if len(bufferL) > 1:
                    cell.update()
                    bufferL = []
        if cell.rect.collidepoint(pg.mouse.get_pos()) and clicking:
            for o in range(size):
                for u in range(size):
                    try:
                        if (array[cell.i+o][cell.j+u] not in solids):
                            if size > 1:
                                opacity = 0.8*size/0.9
                                if rand.triangular(0,size) > opacity:
                                    cell.ptype = ptype
                                    try:
                                        if array[cell.i+o][cell.j+u] == 0:
                                            qpartic += 1
                                            
                                            array[cell.i+o][cell.j+u] = 1
                                        
                                    except:
                                        pass
                            else:
                                if array[cell.i+o][cell.j+u] == 0:
                                    qpartic += 1
                                    array[cell.i+o][cell.j+u] = 1
                    except:
                        pass
                    
        #apaga uma particula
        elif (cell.rect.collidepoint(pg.mouse.get_pos())) and (erasing):
            for o in range(size):
                for u in range(size):
                    if (cell.j+u < gridy or cell.j-u > 0) and (cell.i+o < gridx or cell.i-o > 0):
                        try:
                            if array[cell.i+o][cell.j+u] == 1:
                                array[cell.i+o][cell.j+u] = 0
                                qpartic -= 1
                        except:
                            pass
       
##        print(f'this is the i of the cell : {cell.i}')
##        print(f'this is the j of the cell : {cell.j}')

    #limpa a grid
    if key[pg.K_r]:
        qpartic = 0
        for i in range(gridx):
            for j in range(gridy):
                if (i == 0 or j == 0) or (i == gridx-1 or j == gridy-1):
                    array[i][j] = 2
                else:
                    if array[i][j] == 1:
                        cpartic += 1
                        array[i][j] = 0
        print(cpartic)
        cpartic = 0
    if key[pg.K_z] == True: 
        if not key_pressed_last_frame:#isso verifica se a tecla esta pressionada no ultimo frame
            erasing = not erasing
        key_pressed_last_frame = True#isso atualiza o estado  
    else:
        key_pressed_last_frame = False #isso vira falso quando a tecla não esta

    if key[pg.K_p] == True: 
        if not key_pressed_last_frame1:#isso verifica se a tecla esta pressionada no ultimo frame
            pause = not pause
        key_pressed_last_frame1 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame1 = False #isso vira falso quando a tecla não esta

    if key[pg.K_t] == True: 
        if not key_pressed_last_frame2:#isso verifica se a tecla esta pressionada no ultimo frame
            stream = not stream
        key_pressed_last_frame2 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame2 = False #isso vira falso quando a tecla não esta



    if key[pg.K_l] == True: 
        if not key_pressed_last_frame3:#isso verifica se a tecla esta pressionada no ultimo frame
            ptype = 'sand'
            print('sand')
        key_pressed_last_frame3 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame3 = False #isso vira falso quando a tecla não esta

    if key[pg.K_k] == True: 
        if not key_pressed_last_frame4:#isso verifica se a tecla esta pressionada no ultimo frame
            ptype = 'liquid'
            print('liquid')
        key_pressed_last_frame4 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame4 = False #isso vira falso quando a tecla não esta

    if key[pg.K_j] == True: 
        if not key_pressed_last_frame5:#isso verifica se a tecla esta pressionada no ultimo frame
            ptype = 'gas'
            print('gas')
        key_pressed_last_frame5 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame5 = False #isso vira falso quando a tecla não esta

    if key[pg.K_h] == True: 
        if not key_pressed_last_frame6:#isso verifica se a tecla esta pressionada no ultimo frame
            ptype = 'solid'
            print('solid')
        key_pressed_last_frame6 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame6 = False #isso vira falso quando a tecla não esta
        
    txtsurf = font.render(f'we have{qpartic} sands!!!', True, (WHITE))
    txtsurf1 = font.render(f'your pencil size is {size}', True, (WHITE))
    screen.blit(txtsurf,(10,10))
    screen.blit(txtsurf1,(100,10))
    pg.display.update()
    clock.tick(60)
pg.quit()
quit()
