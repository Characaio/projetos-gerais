from xml.sax.saxutils import escape

import pygame as pg
import pygame.key
import random as rand
pg.init()

WIDTH,HEIGHT = 400, 400

screen = pg.display.set_mode((WIDTH, HEIGHT))

player = pg.Rect((10,10,10,10))

test_font = pg.font.Font(None, 50)
run = True
clock = pg.time.Clock()
particle = pg.Rect((10,10,10,10))
#test_surface = pg.image.load('C:/Users/user/Documents/knight.png')
text_surface = test_font.render('test my', False, 'blue')
class particle:
    def __init__(self, pos, velocity, size):
        self.pos = pos
        self.velocity = velocity
        self.size = size
        self.rect = particle
        self.color1 = rand.randint(0,255)
        self.color2 = rand.randint(0,255)
        self.color3 = rand.randint(0,255)
        self.color = str(self.color1) + ',' + str(self.color2) + ',' + str(self.color3) 
        self.rect.move(self.pos)
        print(str(self.pos)+ ',' + str(self.velocity))
        self.move()
    def drawing(Self):
        while run:
            pg.draw.rect(screen,(self.color1, self.color2, self.color3), self.rect)
    def move(self):
        print('first move')
        pg.draw.rect(screen, (255,255,0), particle)
        for i in range(10):
            
            
            self.rect.move_ip(self.pos + 190*dt)
        self.drawing()
        
            
            
        
dt = 0
particles = []
while run:

    screen.fill((0,0,0))
    pg.draw.rect(screen, (255,0,0), player)
    
    key = pygame.key.get_pressed()
    #
    if key[pg.K_a] and key[pg.K_s] == True:
        player.move_ip(-190*dt, 190*dt)
    elif key[pg.K_d] and key[pg.K_s] == True:
        player.move_ip(190*dt, 190*dt)
    elif key[pg.K_a] and key[pg.K_w] == True:
        player.move_ip(-190*dt, -190*dt)
    elif key[pg.K_d] and key[pg.K_w] == True:
        player.move_ip(190*dt, -190*dt)
    elif key[pg.K_a] == True:
        player.move_ip(-250*dt, 0)
    elif key[pg.K_d] == True:
        player.move_ip(250*dt, 0)
    elif key[pg.K_s] == True:
        player.move_ip(0, 250*dt)
    elif key[pg.K_w] == True:
        player.move_ip(0, -250*dt)

   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONUP:
            print('im pressed')
            print(pg.mouse.get_pos())
            print('this was the mouse pos')
            particles.append(particle(pg.mouse.get_pos(),
                                      rand.randint(0,6),
                                      rand.randint(0,10)))
    
    #screen.blit(test_surface,(100,150))
    #screen.blit(text_surface,(200, 50))
    pg.display.update()
    dt = clock.tick(60)/1000
pygame.quit()
