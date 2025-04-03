from xml.sax.saxutils import escape

import pygame as pg
import pygame.key
import random as rand
import math
pg.init()



#variaveis com numeros e listas
move_speed = 200
gracity = 5.86
FPS = 60
dt = 1/FPS
mousex = 0
mousey = 0
BLACK = (0,0,0)
WHITE = (255, 255, 255)
WIDTH,HEIGHT = 1000, 600
CHUNK_HEIGHT = 100
CHUNK_WIDTH = 100
attractorx, attractory = 0,0
attractorx1, attractory1 = 0,0
limit = 6 #limit para a orbita
terminal = 4.5
COLOR = (0,255,0)
rendered = []
particles = []
xline = []
initialx = [10]
initialy = [7]

    
#variaveis com dependencia do PYGAME
R = pg.Rect((10,10,10,10))#limpar
B = pg.Rect((10,25,10,10))#repel
P = pg.Rect((10,40,10,10))#pausar
I = pg.Rect((10,55,10,10))#explosion
V = pg.Rect((10,70,10,10))#define atratores
C = pg.Rect((10,85,10,10))#gravidade atrativa
X = pg.Rect((10,100,10,10))#bouncy
E = pg.Rect((10,115,10,10))#gas
Q = pg.Rect((10,130,10,10))#fric
font = pg.font.SysFont("Arial", 10)
background = pg.Rect((0,0,50,150))
screen = pg.display.set_mode((WIDTH, HEIGHT))
particle = pg.Rect((10,10,10,10))
clock = pg.time.Clock()


#variaveis booleans e escritas
KEYS = [R,B,P,I,V,C,X,E,Q]
KNAME = ['R','B','P','I','V','C','X','E','Q']
attract = False
fric = False
gas = False
bouncy = False
run = True
renew = True
spawn = False
explosion = False
pause = False
repel = False
collide = False
condition = 'no'
key_pressed_last_frame = False
key_pressed_last_frame2 = False
key_pressed_last_frame3 = False
key_pressed_last_frame4 = False
key_pressed_last_frame5 = False
key_pressed_last_frame6 = False
key_pressed_last_frame7 = False
key_pressed_last_frame8 = False
key_pressed_last_frame9 = False
key_pressed_last_frame10 = False
key_pressed_last_frame11 = False

#test_surface = pg.image.load('C:/Users/user/Documents/knight.png')

class particle:
    def __init__(self,pos,size,ptype):
        self.pos = list(pos)
        self.size = size
        self.ptype = ptype
        self.nocollide = False
        self.lastpos = self.pos[1]
        
    def update(self):
        if self.nocollide == False:
            self.lastpos = self.pos[1]
            if self.pos[1] != HEIGHT-self.size:
                self.pos[1] += 1
            else:
                self.pos[1] = self.lastpos
                self.pos[0] += rand.randint(-1,1)*self.size
                self.nocollide = True
    def render(self):
        self.rect = pg.Rect((self.pos[0],self.
                             pos[1],self.size,self.size))
        pg.draw.rect(screen, (255,0,0), self.rect)

    def collide(self,other):
        if self.pos[1]+self.size == other.pos[1]+self.size and self.pos[0]+self.size == other.pos[0]+self.size:
            self.pos[1] = self.lastpos-3
            self.nocollide = True
            
    
            
            


def spawn_particle():
    #self,pos,velocity,color,size
        particles.append(particle(
            pg.mouse.get_pos(),
            4,
            'sand'))

        
        




print('---------INFORMAÇÕES---------')
print('R = limpa a tela')
print('B =ativa o repel')
print('P = pausa a simulação')
print('I = incrementa o atrator, ele concentra as particulas em um ponto só')
print('V = desliga a atualização de atratores')
print('C = ativa o atrator')
print('X = ativa as particulas saltitantes')
print('E = ativa as particulas de gas')
print('Q = ativa a gravidade')
print('-----------------------------')
print('alguns modos não funcionam se ligados juntos')
print('então, para melhor experiencia, desative aqueles que não funcionam em conjunto')
while run:
    
    screen.fill((BLACK))
    
    for i,p1 in enumerate(particles):
        
        p1.render()
        
                
        
        

    key = pygame.key.get_pressed()
    

    #pausa a simulação
    if key[pg.K_p]:
        if not key_pressed_last_frame7:#isso verifica se a tecla esta pressionada no ultimo frame
            
            pause = not pause #isso ativa o pause
            collide = True
            print(f'pause é {pause}')
        key_pressed_last_frame7 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame7 = False #isso vira falso quando a tecla não esta

    #limpa as particulas
    if key[pg.K_r]:
        particles = []
    if key[pg.K_z]:
        spawn_particle()
    if key[pg.K_t]:
        print(len(particles))
        
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            
            run = False
            
        elif event.type == pg.MOUSEBUTTONDOWN:
            spawn_particle()
    
    
    pg.display.update()
    clock.tick(FPS)
    
pg.quit()
