from xml.sax.saxutils import escape

import pygame as pg
import pygame.key
import random as rand
import math
pg.init()

BLACK = (0,0,0)
WHITE = (255, 255, 255)
WIDTH,HEIGHT = 600, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
player = pg.Rect((10,10,10,10))
clock = pg.time.Clock()
test_font = pg.font.Font(None, 50)
move_speed = 200

run = True
fric = False
speed = False
key_pressed_last_frame = False
key_pressed_last_frame2 = False

#test_surface = pg.image.load('C:/Users/user/Documents/knight.png')
text_surface = test_font.render('test my', False, 'blue')
class particle:
    def __init__(self,pos,friction, velocity,vx, vy, color,size):
        self.pos = list(pos)
        self.friction = friction
        self.fric = fric
        self.velocity = velocity
        self.vx = vx
        self.vy = vy
        
        self.size = size
        self.color = color
        
    def update(self):
        if fric: #ativa a fricção
            self.pos[0] += self.vx * self.velocity * self.friction
            self.pos[1] += self.vy * self.velocity * self.friction        
        elif speed: #ativa a velocidade
            self.pos[0] += self.vx * self.velocity * float(self.friction + 1)
            self.pos[1] += self.vy * self.velocity * float(self.friction + 1)
        else: #normal
            self.pos[0] += self.vx * self.velocity
            self.pos[1] += self.vy * self.velocity
        #faz a particula bater nas paredes
        if self.pos[0] > WIDTH or self.pos[0] < 0 :
            self.vx *= -1
            
        elif self.pos[1] > HEIGHT or self.pos[1] < 0:
            self.vy *= -1
            
    def render(self): #renderixa a bola depois das atualizações
        pg.draw.circle(screen,self.color,(int(self.pos[0]), int(self.pos[1])), self.size)

    def collide(self, me, other):
        dx = me.pos[0] - other.pos[0]
        dy = me.pos[1] - other.pos[1]

        dist = math.sqrt(dx**2 + dy**2)

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

particles = []
while run:
    
    screen.fill((BLACK))
    pg.draw.rect(screen, (255,0,0), player)
    for i,p1 in enumerate(particles):
        for j in range(i+1, len(particles)): #isso faz essas duas funções para todas particulas presentes
            p1.collide(p1, particles[j])

        p1.render() #isso renderiza as particulas   
        p1.update() #isso atualiza os valores
        

    key = pygame.key.get_pressed()
    #
    #explicação para o clock.get_time()/1000, ele quer fizer o delta, ou seja, o tempo que passou
    #deis do ultimo frama, assim normalizando o movimento
    if key[pg.K_a] == True:
        player.move_ip(move_speed *-1*clock.get_time()/1000, 0)
    if key[pg.K_d] == True:
        player.move_ip(move_speed *clock.get_time()/1000, 0)
    if key[pg.K_s] == True:
        player.move_ip(0, move_speed*clock.get_time()/1000)
    if key[pg.K_w] == True:
        player.move_ip(0, move_speed*-1*clock.get_time()/1000)
    if key[pg.K_z] == True:
       #self,pos,velocity,color,size
        particles.append(particle(
            pg.mouse.get_pos(),
            0.9,                #fricção
            
            rand.randint(3,8), #velocidade
            rand.triangular(-1,1), #vectorx, retorna um float com o .triangular
            rand.triangular(-1,1), #vectory, retorna um float com o .triangular
            (rand.randint(0,255),rand.randint(0,255),rand.randint(0,255)), #cor 
            rand.randint(5,10))) #tamanho
        
    if key[pg.K_q] == True:
        if not key_pressed_last_frame:#isso verifica se a tecla esta pressionada no ultimo frame
            fric = not fric #isso ativa a fricção
            print("fricção é " + str(fric))
        key_pressed_last_frame = True#isso atualiza o estado
        
    else:
        key_pressed_last_frame = False #isso vira falso quando a tecla não esta

        
    if key[pg.K_e] == True:
        if not key_pressed_last_frame2:#isso verifica se a tecla esta pressionada no ultimo frame
            speed = not speed #isso ativa a fricção
            print("speed é " + str(speed))
        key_pressed_last_frame2 = True#isso atualiza o estado
        
    else:
        key_pressed_last_frame2 = False #isso vira falso quando a tecla não esta 
            
    

        
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            
            run = False
            
        elif event.type == pg.MOUSEBUTTONDOWN:
            pass
                
                                     
        
    
    #screen.blit(test_surface,(100,150))
    #screen.blit(text_surface,(200, 50))
    pg.display.update()
    clock.tick(60)
pygame.quit()
