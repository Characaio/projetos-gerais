import numpy as np
import turtle as turt
import time
from scipy import interpolate

p1 = (0,300)
p2 = (300,0)
p3 = (600, 300)

current_p2 = None

screen = turt.Screen()
run = True

def get_mouse_coor(x,y):
    global p3
    p3 = (x,y)
    print(p2)
    main()
    
def lerp(p1,p2,t):
    return p1 + (p2- p1) * t

def main():
    turt.clearscreen()
    n = 0.05
    print(p1,p2,p3)
    for t in np.arange(0,1,n):
        x1 = lerp(p1[0],p2[0], t)
        y1 = lerp(p1[1],p2[1], t)
        x2 = lerp(p2[0],p3[0], t)
        y2 = lerp(p2[1],p3[1], t)
        x3 = lerp(x1,x2,t)
        y3 = lerp(y1,y2,t)
        x = lerp(x2,x3,t)
        y = lerp(y2,y3,t)
        turt.teleport(x,y)
        turt.dot(4)
    screen.onscreenclick(get_mouse_coor)
    turt.mainloop()

while run:
    main()
        