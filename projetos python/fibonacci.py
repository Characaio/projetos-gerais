

def fibonacci(o,a):
    
    
    next = o+a
    a,b = a,next
    
    print(next)
    fibonacci(a,b)
    
        


if __name__ == "__main__":
    fibonacci(0,1)