current = 0
desired = 10
inter = 1
size = 0
def lerp(a,b,t,size):
    lerped = a+(b-a)*t
    current = lerped
    print(lerped)
    
    lerp(current,desired,inter,size)
        

lerp(current,desired,inter,size)
