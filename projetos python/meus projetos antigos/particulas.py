import turtle as turt
import pygame as pg
turt.getscreen()
turt.speed(10)
turt.tracer()
clones = []
class particle:
    def __init__(self, posx, posy, velocity, size, name):
        self.posx = posx
        self.posy = posy
        self.velocity = velocity
        self.size = size
        self.name = name
        self.turtle = turt.Turtle()
        self.turtle.speed(3)
        self.turtle.goto(turt.pos())
        
        turt.goto(self.posx, self.posy)
        turt.write(str(self.posx) + ',' + str(self.posy))
        print(str(self.posx) + ',' + str(self.posy) + ',' + str(velocity))
        self.move()
    def move(self):
        
        for i in range(10):
            
            self.turtle.dot(self.size)
            
            self.posx += self.velocity #isso é a velocidade de movimento deles
            self.turtle.goto(self.posx, self.posy)
        lastposx.append(self.posx)
        lastposy.append(self.posy)
        
particles = []
lastposx = []
lastposy = []

for i in range(10):
    particles.append(particle(i*10, i*16, i*3, i*2, i))
    #isso permite a inicialização de uma instnacia da classe particula
    print('imove')
for i in range(len(lastposx)):
    turt.up()
    turt.goto(lastposx[i], lastposy[i])
    turt.dot()
# isso me permite achar o valor de uma instancia de uma classe, peguei do quarto item
    
    

