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
WIDTH,HEIGHT = 1000, 700
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
player = pg.Rect((10,10,10,10))
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
collide = True
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
    def __init__(self,pos,friction, velocity,vx, vy,
                 color,size,gravity,momentum,xspread,yspread,opacity):
        self.pos = list(pos)
        self.friction = friction
        self.fric = fric
        self.velocity = velocity
        self.vx = vx
        self.vy = vy
        
        self.size = size
        self.color = tuple(color)#isso é lsita para acessar cada valor
        self.gravity = gravity
        self.momentum = momentum
        self.momentu = self.momentum
        self.xspread = xspread
        self.yspread = yspread
        self.opacity = opacity
        self.repels = 180
    
    def update(self):
        match condition:
            case 'fric': #ativa a fricção
                self.pos[0] += self.vx * self.velocity / -float(self.gravity/5)
                self.pos[1] -= self.vy* self.momentu
                if self.momentu < terminal:
                    self.momentu += self.momentum
                #self.vy = -6
                self.vy -= -float(self.gravity/100)
                # self.vy - float(self.gravity/100) * self.momentu
            case 'gas': #ativa a fisica de gas
                self.pos[0] += self.vx * self.velocity + self.xspread
                self.pos[1] += self.gravity * self.momentu +self.yspread
                self.momentu += self.momentum
                #os whiles previne um crash devido ao valor da opacidade negativo
                # os ifs define a a opacidade da cor
                if self.color[0] > 0:
                    self.color[0] -= self.opacity
                while self.color[0] < 0:
                    self.color[0] += 1
                    
                if self.color[1] > 0:
                    self.color[1] -= self.opacity
                while self.color[1] < 0:
                    self.color[1] += 1
                    
                if self.color[2] > 0:
                    self.color[2] -= self.opacity
                while self.color[2] < 0:
                    self.color[2] += 1
            # define particulas saltitantes, mas não funciona
            case 'bouncy':
                self.pos[0] += self.vx * self.velocity 
                self.pos[1] -= self.vy * self.velocity
                
                self.vy += -0.1

            #isso ativa um campo gravitacaional para atrair outras particulas,
            #mas, desativa a colisão
            case 'attract':
                if not self.vx > limit and not self.vx < limit*-1:
                    
                    if attractorx > self.pos[0]:
                        self.vx += 0.1
                        
                        if attractorx > self.pos[0]*2:
                                self.vx += 0.3

                    if attractorx < self.pos[0]:
                        self.vx -= 0.1
                        
                        if attractorx < self.pos[0]*2:
                            self.vx -= 0.3
                
                        
                if not self.vy > limit and  not self.vy < limit*-1:      
                    if attractory > self.pos[1]:
                        self.vy += 0.1
                        
                        if attractory > self.pos[1]*2:
                            self.vy += 0.1 
                              
                    if attractory < self.pos[1]:
                        self.vy -= 0.1
                        
                        if attractory < self.pos[1]*2:
                            self.vy -= 0.1
                #a explosão atrai TODAS particulas a um ponto e ao aumenta os
                #vectors para acompanhar o movimento do mouse
                if explosion:
                    while attractorx > self.pos[0]+10:
                        self.pos[0] += 0.5
                        self.vx += 0.1

                    while attractorx < self.pos[0]-10:
                        self.pos[0] -= 0.5
                        self.vx -= 0.1
                    while attractory > self.pos[1]+10:
                        self.pos[1] += 0.5
                        self.vy += 0.1
                    while attractory < self.pos[1]-10:
                        self.pos[1] -= 0.5
                        self.vy -= 0.1
                if attractorx == self.pos[0]:
                    self.vx *= 0.2
                if attractory == self.pos[1]:
                    self.vy *= 0.2

                # isso serve para definar o repelimento das particulas
                #definido pelo repel
                rdx = self.pos[0] - attractorx1
                rdy = self.pos[1] - attractory1

                rdist = math.sqrt(rdx**2 + rdy**2)
                
                if rdist < self.repels+self.size and repel:
                        
                    rnormal_x = rdx/rdist
                    rnormal_y = rdy/rdist

                
                    roverlap = self.size+self.repels - rdist
                    self.vx = rand.triangular(-6,6)
                    self.vy = rand.triangular(-6,6)
                    self.pos[0] += rnormal_x * roverlap / 2
                    self.pos[1] += rnormal_y * roverlap / 2
                    #repelimento de particulas
                    if self.pos[0] > attractorx1:
                        self.pos[0] += 10
                        self.vx += 0.5
                    else:
                        self.pos[0] -= 10
                        self.vx += -0.5
                    if self.pos[1] > attractory1:
                        self.pos[1] += 10
                        self.vy += 0.5
                    else:
                        self.pos[1] -= 10
                        self.vy += -0.5
                    
                else:   
                    self.pos[0] += self.vx * self.momentu 
                    self.pos[1] += self.vy * self.momentu 
                    self.vx *= 0.995 #quanto menor esses dois valores forem,
                    self.vy *= 0.995 #maior sera a perda de velocidade
                    if self.momentu > terminal:
                        self.momentu -= 2
                    if self.momentu < terminal:
                        self.momentu += self.momentum
                    if abs(self.momentu) > terminal:
                        print(f'passou do terminal, o valor é de {self.momentu}')
            case 'no': #normal
                self.pos[0] += self.vx * self.velocity
                self.pos[1] += self.vy * self.velocity
                self.velocity *= 0.999
        if repel:
            #isso é o repel basico para todas as outras particula,
            #menos o sistema de orbita
            

            rdx = self.pos[0] - attractorx1
            rdy = self.pos[1] - attractory1

            rdist = math.sqrt(rdx**2 + rdy**2)
            
            if rdist < self.repels+self.size:
                    
                rnormal_x = rdx/rdist
                rnormal_y = rdy/rdist

            
                roverlap = self.size+self.repels - rdist
                
                self.pos[0] += rnormal_x * roverlap 
                self.pos[1] += rnormal_y * roverlap
                if self.vx > attractorx1:
                    self.vx,self.vy = self.vy, self.vx*-1
                else:
                    self.vx,self.vy = self.vy*-1, self.vx
                
            
            
        
            
        #faz a particula bater nas paredes
        if self.pos[0] > WIDTH and not attract or self.pos[0] < 0 and not attract :
            self.vx *= -1    
        elif self.pos[1] > HEIGHT and not attract or self.pos[1] < 0 and not attract:
            self.vy *= -1
            if bouncy:
                self.velocity *= 0.9

    
    def render(self):
        
        #renderixa a bola depois das atualizações
        #deixa de renderizar particulas sem cor
        if (not self.pos[0] > WIDTH  or not self.pos[0] < 0 or
            not self.pos[1] > HEIGHT  or not self.pos[1] < 0 or
            self.color[0] == 0 and self.color [1] == 0, self.color[2] == 0):  
            pg.draw.circle(screen,(self.color),
        (int(self.pos[0]),int(self.pos[1])),self.size)

    
    def collide(self, me, other):
        dx = me.pos[0] - other.pos[0]
        dy = me.pos[1] - other.pos[1]

        dist = math.sqrt(dx**2 + dy**2)
        try:
            if dist < me.size+other.size:
                    
                normal_x = dx/dist
                normal_y = dy/dist

                me.vx,other.vx = other.vx,me.vx
                me.vy,other.vy = other.vy,me.vy
                overlap = me.size+other.size - dist
                
                me.pos[0] += self.friction * normal_x * overlap / 2
                me.pos[1] += self.friction * normal_y * overlap / 2
                other.pos[0] -= self.friction * normal_x * overlap / 2
                other.pos[1] -= self.friction * normal_y * overlap / 2
        except:
            print('something broke lil bro')
            run = False
                
            
            


def spawn_particle():
    #self,pos,velocity,color,size
        particles.append(particle(
            pg.mouse.get_pos(),
            0.9,                #fricção
            
            rand.randint(3,8), #velocidade
            rand.triangular(-1,1), #vectorx, retorna um float com o .triangular
            rand.triangular(-1,1), #vectory, retorna um float com o .triangular
            (rand.randint(0,255),rand.randint(0,255),rand.randint(0,255)), #cor 
            rand.randint(5,10),  #tamanho
            -4.86, #gravidade
            0.1, #momentum
            rand.triangular(-6,6), #xspread
            rand.triangular(-3,3), #yspread
            rand.randint(5,10) #opacidade
            ))

        

        
def prepare_particles(pos):
    #self,pos,velocity,color,size
        particles.append(particle(
            pos, #posição
            0.9,                #fricção
            
            rand.randint(3,8), #velocidade
            rand.triangular(-1,1), #vectorx, retorna um float com o .triangular
            rand.triangular(-1,1), #vectory, retorna um float com o .triangular
            (rand.randint(0,255),rand.randint(0,255),rand.randint(0,255)), #cor 
            rand.randint(5,10),  #tamanho
            -4.86, #gravidade
            0.1, #momentum
            rand.triangular(-6,6), #xspread
            rand.triangular(-3,3), #yspread
            rand.randint(5,10) #opacidade
            ))
        


#inicia 100 particulas iniciais
for row in range(10):
    for column in range(10):
        prepare_particles((100*int(row+1), 70*int(column+1)))
        #print(f'{100*int(row+1)} , {70*int(column+1)}')


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
    pg.draw.rect(screen, (255,0,0), player)
    for i,p1 in enumerate(particles):
        for j in range(i+1, len(particles)): #isso faz essas duas funções para todas particulas presentes
            if collide:
                #não colide se estiver pausado, em orbita ou bouncy
                p1.collide(p1, particles[j])

        p1.render() #isso renderiza as particulas
        if not pause:
            p1.update() #isso atualiza os valores
            if repel:
                #desenha o circulo para uma representação visual do repel
##                pg.draw.circle(screen,(0,0,0),
##                               (attractorx1, attractory1),p1.repels)
                pass
        #isso remove a particula se ela esticver fora de tela,
        #aumentando o desempenho
        if p1.pos[0] > WIDTH or p1.pos[0] < 0 or p1.pos[1] > HEIGHT or p1.pos[1] < 0:
            if fric or gas:
                #print(f'{p1.momentu}')
                particles.remove(p1)
                
        
        

    key = pygame.key.get_pressed()
    #
    #explicação para o clock.get_time()/1000, ele define o delta, ou seja,
    #o tempo que passou deis do ultimo frama, assim normalizando o movimento
    if key[pg.K_a] == True:
        player.move_ip(move_speed *-1*clock.get_time()/1000, 0)
    if key[pg.K_d] == True:
        player.move_ip(move_speed *clock.get_time()/1000, 0)
    if key[pg.K_s] == True:
        player.move_ip(0, move_speed*clock.get_time()/1000)
    if key[pg.K_w] == True:
        player.move_ip(0, move_speed*-1*clock.get_time()/1000)
    if key[pg.K_z] == True:
        if not repel:
            spawn_particle()

    #define um atrator ao mouse para as orbitas
    if attract or repel:
        if renew:
            attractorx,attractory = pg.mouse.get_pos()
        attractorx1,attractory1 = pg.mouse.get_pos()
    

    if fric:
        condition = 'fric'
    elif gas:
        condition = 'gas'
    elif bouncy:
        condition = 'bouncy'
    elif attract:
        condition = 'attract'
    else:
        condition = 'no'

    
    #ativa gravidade
    if key[pg.K_q] == True:
        if not key_pressed_last_frame:#isso verifica se a tecla esta pressionada no ultimo frame
            fric = not fric #isso ativa a gravidade
            collide = True
            
            print(f'gravidade é {fric}')
        key_pressed_last_frame = True#isso atualiza o estado
        
    else:
        key_pressed_last_frame = False #isso vira falso quando a tecla não esta
    
    #ativa o gas
    if key[pg.K_e] == True:
        if not key_pressed_last_frame2:#isso verifica se a tecla esta pressionada no ultimo frame
            gas = not gas #isso ativa o gas
            collide = True
            
            print(f'gas é {gas}')
        key_pressed_last_frame2 = True#isso atualiza o estado
        
    else:
        key_pressed_last_frame2 = False #isso vira falso quando a tecla não esta 

    #ativa o bouncy
    if key[pg.K_x] == True: 
        if not key_pressed_last_frame3:#isso verifica se a tecla esta pressionada no ultimo frame
            bouncy = not bouncy #isso ativa o bouncy
            collide = False
            
            print(f'bouncy é {bouncy}')
        key_pressed_last_frame3 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame3 = False #isso vira falso quando a tecla não esta

    #ativa a orbita
    if key[pg.K_c] == True:
        
        if not key_pressed_last_frame4:#isso verifica se a tecla esta pressionada no ultimo frame
            
            attract = not attract #isso ativa a orbita
            collide = False
            
            print(f'attract é {attract}')
        key_pressed_last_frame4 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame4 = False #isso vira falso quando a tecla não est

    #fixa uma orbita
    if key[pg.K_v]:
        if not key_pressed_last_frame5:#isso verifica se a tecla esta pressionada no ultimo frame
            
            renew = not renew #isso renova os atratores
            
            print(f'renew é {renew}')
        key_pressed_last_frame5 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame5 = False #isso vira falso quando a tecla não esta

    #ativa a explosão
    if key[pg.K_i]:
        if not key_pressed_last_frame6:#isso verifica se a tecla esta pressionada no ultimo frame
            
            explosion = not explosion #isso ativa a explosão
            
            print(f'explosion é {explosion}')
        key_pressed_last_frame6 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame6 = False #isso vira falso quando a tecla não esta

    #pausa a simulação
    if key[pg.K_p]:
        if not key_pressed_last_frame7:#isso verifica se a tecla esta pressionada no ultimo frame
            
            pause = not pause #isso ativa o pause
            collide = True
            print(f'pause é {pause}')
        key_pressed_last_frame7 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame7 = False #isso vira falso quando a tecla não esta

    #ativa o repel
    if key[pg.K_b]:
        if not key_pressed_last_frame8:#isso verifica se a tecla esta pressionada no ultimo frame
            
            repel = not repel #isso ativa o repel
            collide = True
            print(f'repel é {repel}')
        key_pressed_last_frame8 = True#isso atualiza o estado  
    else:
        key_pressed_last_frame8 = False #isso vira falso quando a tecla não esta


        
    #limpa as particulas
    if key[pg.K_r]:
        particles = []
        
        
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            
            run = False
            
        elif event.type == pg.MOUSEBUTTONDOWN:
            spawn_particle()
                
    pg.draw.rect(screen,(100,100,100),background)
    
    for i,key in enumerate(KEYS):
        txtsurf = font.render(f'{KNAME[i]}', True, (255,255,255))
        screen.blit(txtsurf,(25,10+15*i))
        pg.draw.rect(screen, (255,0,0), KEYS[i])
        if repel:
            pg.draw.rect(screen, (0,255,0), B)
        if pause:
            pg.draw.rect(screen, (0,255,0), P)
        if explosion:
            pg.draw.rect(screen, (0,255,0), I)
        if renew:
            pg.draw.rect(screen, (0,255,0), V)
        if attract:
            pg.draw.rect(screen, (0,255,0), C)
        if bouncy:
            pg.draw.rect(screen, (0,255,0), X)
        if gas:
            pg.draw.rect(screen, (0,255,0), E)
        if fric:
            pg.draw.rect(screen, (0,255,0), Q)
    
        

        
    #screen.blit(test_surface,(100,150))
    #screen.blit(text_surface,(200, 50))
    
    pg.display.update()
    clock.tick(FPS)
    
pg.quit()
