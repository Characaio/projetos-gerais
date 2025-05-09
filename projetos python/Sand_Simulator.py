import pygame as pg
import random as rand
import math
pg.init()

WIDTH,HEIGHT = 600,600
screen = pg.display.set_mode((WIDTH,HEIGHT))
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
clock = pg.time.Clock()
run = True
array = []
array0 = []
arraycopy = []
grid = []
grid1 = []
gridx = int(WIDTH/4)
gridy = int(HEIGHT/4)
##gridx = int(WIDTH/10)
##gridy = int(HEIGHT/10)
clicking = False
element = 'sand'
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

pg.init()
cells = [
    
]
class cell:
    def __init__(self,rect,i,j,element,velocity):
        self.rect = rect
        self.i = i
        self.j = j
        self.move = 0
        self.element = element
        self.xvelocity = velocity[0]
        self.yvelocity = velocity[1]
        
    def render(self):
        if array[self.i][self.j] == "void":
            pg.draw.rect(screen, BLACK, self.rect)
        elif array[self.i][self.j] == "water":
            pg.draw.rect(screen, BLUE, self.rect)
        elif array[self.i][self.j] == "WALLS":
            pg.draw.rect(screen, RED, self.rect)
        elif array[self.i][self.j] == "sand":
            pg.draw.rect(screen,YELLOW, self.rect)
            
    def update(self):
        
        if array[self.i][self.j] == 'sand' :
            if array[self.i][self.j+1] == 'void':
                array[self.i][self.j+1] = 'sand'
                array[self.i][self.j] = 'void'
            
                
                
def make_2d_list():
    for i in range(gridx):
        temparray = []
        for j in range(gridy):
            #verifica se a celular esta no limite da grid
            if (i == 0 or j == 0) or (i == gridx-1 or j == gridy-1):
                temparray.append('WALLS')
            else: #faz a grid normal
                temparray.append('void')
                cells.append(cell(
                    pg.Rect((i*WIDTH/gridx,j*HEIGHT/gridy, WIDTH/gridx,HEIGHT/gridy)),
                    i,
                    j,
                    element,
                    (1,1)
                    )
                    )
        array.append(temparray)
    array0 = array
    arraycopy = array
    return array

print(make_2d_list())
buffer = []
fuck = False
help = [-1, 1]
def update():
     for j in range(gridy-2, 0, -1):  # ignora bordas
        for i in range(1, gridx-1):
            aleatorio = rand.randint(0,1)
            if array[i][j] == 'sand':
                if array[i][j+1] == 'void':
                    array[i][j+1] = 'sand'
                    array[i][j] = 'void'
                else:
                    if rand.choice([True,False]):
                        if array[i+1][j+1] != "sand":
                            array[i+1][j+1] = 'sand'
                            array[i][j] = 'void'
                    else:
                        if array[i-1][j+1] == 'void':
                            array[i-1][j+1] = 'sand'
                            array[i][j] = 'sand'
            elif array[i][j] == "water":
                if array[i][j+1] == "void":
                    array[i][j+1] = "water"
                    array[i][j] = "void"
                else:
                    if rand.choice([True,False]):
                        if array[i+1][j+1] == "void":
                            array[i+1][j+1] = 'water'
                            array[i][j] = 'void'
                        elif array[i+1][j] == "void":
                            array[i+1][j] = 'water'
                            array[i][j] = 'void'
                    else:
                        if array[i-1][j+1] == "void":
                            array[i-1][j+1] = 'water'
                            array[i][j] = 'void'
                        elif array[i-1][j] == "void":
                            array[i-1][j] = 'water'
                            array[i][j] = 'void'
                

size = 8
opacity = 0.50
while run:
    key = pg.key.get_pressed()
    screen.fill(BLACK)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
            run = False
        #o down e up define um sistema de drag do mouse
        if event.type != pg.MOUSEWHEEL:
            if (event.type == pg.MOUSEBUTTONDOWN):
                clicking = True
            if event.type == pg.MOUSEBUTTONUP:
                clicking = False
        else:
            if event.y == 1:
                size += 1
                print(size)
            if event.y == -1:
                if size > 1:
                    print(size)
                    size -= 1
    
    update()
    if key[pg.K_e]:
        print('changing to sand')
        element = "sand"
    if key[pg.K_q]:
        print('changing to water')
        element = 'water'
    for i,p1 in enumerate(cells):
        p1.render()
        if p1.rect.collidepoint(pg.mouse.get_pos()) and clicking:
            for o in range(-int(size/2),int(size/2)):
                for p in range(-int(size/2),int(size/2)):
                    if rand.triangular(0,1) > 0.8:
                        if element == 'sand':
                            try:
                                array[p1.i+o][p1.j+p] = 'sand'
                            except IndexError as e:
                                print(e)
                        elif element == 'water':
                            try:
                                array[p1.i+o][p1.j+p] = 'water'
                            except IndexError as e:
                                print(e)
    clock.tick(60)
    pg.display.update()
    
pg.quit()
quit()
    
if __name__ == '__main__':
    main()