import pygame as pg
import random as rand

pg.init()
run = True
pg.display.set_caption("xadrezin")
WIDTH,HEIGHT = 640,640
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
light_square = (239,217,180)
dark_square = (181,133,97)
pontos = [
    
]
pos = []
multi = 10
p1 = (100,300)
p2 = (250,650)
p3 = (300,150)
p4 = (600,300)
# p4 = (700, 300)
# p5 = (625,50)

font = pg.font.SysFont('arial', 24)

key_pressed_last_frame = False
clock = pg.time.Clock()
class board:
    def __init__(self,x,y,i,j):
        self.x = x
        self.y = y 
        self.i = i
        self.j = j
        self.rect = pg.Rect(x,y,(WIDTH/8),(HEIGHT/8))
        self.follow = False
        self.board_pos = None
        self.board_color = None
    def render(self):
        #print('im rendering')
        
        if (self.i+self.j) % 2 == 0 :
            pg.draw.rect(screen,(dark_square),self.rect)
        else:
            pg.draw.rect(screen,(light_square),self.rect)
        
    def move(self):
        text = font.render(str(color_board[self.j][self.i]) +
                           str(initial_board[self.j][self.i]),True,BLACK,None)
        textrect = text.get_rect() 
        if not self.follow:
            #print('noooooooo')
            screen.blit(text, (
                    (WIDTH/8*self.i) + WIDTH/8/2-15,
                    (HEIGHT/8*self.j) + HEIGHT /8/2-15
                    ))
        else:
            #print('yessssssssssss')
            screen.blit(text, (
                    pg.mouse.get_pos()
                    ))

boards = [
    
]

initial_board = [
    ['T','C','B','K','R','B','C','T'],
    ['P','P','P','P','P','P','P','P'],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    ['P','P','P','P','P','P','P','P'],
    ['T','C','B','K','R','B','C','T']
]
color_board = [
    ['W','W','W','W','W','W','W','W'],
    ['W','W','W','W','W','W','W','W'],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    ['B','B','B','B','B','B','B','B'],
    ['B','B','B','B','B','B','B','B']
]
for i in range(8):
    temp = []
    for j in range(8):
        
        boards.append(board(i*WIDTH/8,j*HEIGHT/8,i,j))
    
    
clicking = False
while run:
    screen.fill(WHITE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            clicking = True
        if event.type == pg.MOUSEBUTTONUP:
            clicking = False
            #pos = pg.mouse.get_pos()
            
    for i,p1 in enumerate(boards):
        #print("hi")
        p1.render()
        if p1.rect.collidepoint(pg.mouse.get_pos()) and clicking:
            #print('hi')
            p1.follow = not p1.follow
        elif p1.rect.collidepoint(pg.mouse.get_pos()) and not clicking:
            pass
        p1.move()
    clock.tick(30)
    pg.display.update()