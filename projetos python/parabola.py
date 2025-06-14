
import turtle as turt

result = ' '
for i in range(11):
    
    x = input(str('cmon dude give ne a valuee'))
    y = int(x)**2*-1 + 10*int(x) + 12
    print(str(x) + ', ' + str(y))
    result = str(x) + ',' + str(y)
    if result != ' ':
        turt.getscreen()
        for n in range(11):
            x_turt = int(x)+n
            y_turt = x_turt**2*-1 + 10*x_turt + 12
            turt.goto(-100, 0)
            y_turte = y_turt*5
            x_turte = x_turt*6
            turt.up()
            turt.left(90)
            turt.forward(y_turte)
            turt.right(90)
            turt.forward(x_turte)
            turt.down()
            turt.dot()
            turt.up()
            

