question = str("null")
invalid = False
loop = int("0")
import webbrowser
import random
from tkinter import *

root = Tk()
admin = False
questionaire = False
name = ""
age = ""
city = ""
numb = ""



    
def get_user_data():
    name = ""
    age = ""
    city = ""
    question = ""
    senhas = ""
    
    import turtle
    turtle.penup()
    screen = turtle.Screen()
    screen.clear()
    screen.setup(500, 500)
    screen.bgcolor('green')
    FONT_SIZE = 16
    FONT = ('Arial', FONT_SIZE, 'bold')
    tur = turtle

    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # URL do video

    #isso é para conseguir os dados
    
    tur.goto(-150, 150)
    tur.write("whats your name?", align='left', font=FONT)
    while len(name) == 0:
        name = tur.textinput("Name", "Please enter your name:")
    tur.goto(-150, 120)
    tur.write("hello " + str(name), font=FONT )
    while len(age) == 0:
        age = tur.textinput("age", "Please enter your age:")
    tur.goto(-150, 90)
    tur.write("Okay", font=FONT)
    while len(city) == 0:
        city = tur.textinput("city", "Please enter your city name:")
    tur.goto(-150, 60)
    tur.write("your name is " + name + " you are " + str(age) + " years old " + "and live on " + city, font=FONT)
    while len(question) == 0:
        question = tur.textinput("confirmation", "is this right?:")
    tur.clear()
    invalid = False

    #identificar sua respota
    
    if question == "yes": 
        import turtle
        screen = turtle.Screen()
        screen.clear()
        tur.goto(-150, 150)
        tur.write("good")
        if name == "caio":
            tur.goto(-150, 120)
            tur.write("welcome back caio")
            admin = True
            while len(senhas) == 0:
                senhas = tur.textinput("senhas", "what password do you want?:")
            if senhas == "spotify":
                screen.clear()
                tur.write("placeholder")
            elif senhas == "pokemon planet":
                screen.clear()
                tur.write("placeholder2")
            else:
                screen.clear()
                tur.goto(-80, 0)
                FONT_SIZE = 35
                FONT = ('Arial', FONT_SIZE, 'bold')
                tur.write("fuck you" , font=FONT )
                webbrowser.open(url)
        else:
            print("Not admin, normal user iniciating")
            
        
    elif question == "no":
        tur.write("oh well, time to restart")
        screen.clear()
        get_user_data()
    else:
        tur.write("INVALID OUTPUT")
        screen.clear()
        get_user_data() #não funcional 21/08/24

        
def math_process(): #função de para resolver conta, precisa de muitas melhoras
    import tkinter as tk


    root = tk.Tk()

    root.geometry("500x500")
    root.title("my first GUI")

    display_box = tk.Text(root, width=20, height=5, font=("arial", 18))
    display_box.pack(fill="x", padx=15, pady = 15)

    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    buttonframe.columnconfigure(2, weight=1)

    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0
    num7 = 0
    num8 = 0
    num9 = 0
    newacc = False

    def clear():
        display_box.delete("1.0", "end")
        global numb
        numb = ""
    


    def get_total(total):
        global totali
        totali = total
        display_box.delete("1.0", "end")
        display_box.insert(END, total)
        global numb
        numb = ""

        global newacc
        newacc = True
        


        
    def addition(numb):
            [num1, num2] = (numb.split("+"))
            num1 = int(num1)
            num2 = int(num2)
            total = num1 + num2
            get_total(total)
    def subtraction(numb):
            [num1, num2] = (numb.split("-"))
            num1 = int(num1)
            num2 = int(num2)
            total = num1 - num2
            get_total(total)
    def multiplication(numb):
            [num1, num2] = (numb.split("*"))
            num1 = int(num1)
            num2 = int(num2)
            total = num1 * num2
            get_total(total)
    def division(numb):
            [num1, num2] = (numb.split("/"))
            num1 = int(num1)
            num2 = int(num2)
            total = num1 / num2
            get_total(total)


    def get_numb(number):
        global numb
        if newacc == True:
            numb = str(totali) + str(number)
        else:
            numb = numb + str(number)
        print(numb)
        


    def account(x):

        if x != "=":
            display_box.insert(END, x)
            get_numb(x)
        else:
            if "+" in numb:
                addition(numb)
            if "-" in numb:
                subtraction(numb)
            if "*" in numb:
                multiplication(numb)
            if "/" in numb:
                division(numb)
            
        
            


    btn1 = tk.Button(buttonframe, text="1",
                     command=lambda: account(1),
                     font=("arial", 18))
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

    btn2 = tk.Button(buttonframe, text="2",
                     command=lambda: account(2),
                     font=("arial", 18))
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

    btn3 = tk.Button(buttonframe, text="3",
                     command=lambda: account(3),
                     font=("arial", 18))
    btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

    btn4 = tk.Button(buttonframe, text="4",
                     command=lambda: account(4),
                     font=("arial", 18))
    btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

    btn5 = tk.Button(buttonframe, text="5",
                     command=lambda: account(5),
                     font=("arial", 18))
    btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

    btn6 = tk.Button(buttonframe, text="6",
                     command=lambda: account(6),
                     font=("arial", 18))
    btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

    btn7 = tk.Button(buttonframe, text="7",
                     command=lambda: account(7),
                     font=("arial", 18))
    btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

    btn8 = tk.Button(buttonframe, text="8",
                     command=lambda: account(8),
                     font=("arial", 18))
    btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

    btn9 = tk.Button(buttonframe,
                     text="9",
                     command=lambda: account(9),
                     font=("arial", 18))
    btn9.grid(row=2, column=2, sticky=tk.W+tk.E)

    btn10= tk.Button(buttonframe,
                     text="0",
                     command=lambda: account(0),
                     font=("arial", 18))
    btn10.grid(row=3, column=0, sticky=tk.W+tk.E)

    btn11= tk.Button(buttonframe,
                     text="result",
                     command=lambda:account("="),
                     font=("arial", 18))
    btn11.grid(row=3, column=2, sticky=tk.W+tk.E)


    btn12 = tk.Button(buttonframe, text="+",
                     command=lambda: account("+"),
                     font= ("arial", 18))
    btn12.grid(row=0, column=3, sticky=tk.W+tk.E)

    btn13 = tk.Button(buttonframe,
                     text="-",
                     command=lambda: account("-"),
                     font=("arial", 18))
    btn13.grid(row=1, column=3, sticky=tk.W+tk.E)

    btn14= tk.Button(buttonframe,
                     text="*",
                     command=lambda: account("*"),
                     font=("arial", 18))
    btn14.grid(row=2, column=3, sticky=tk.W+tk.E)

    btn15= tk.Button(buttonframe,
                     text="/",
                     command=lambda: account("/"),
                     font=("arial", 18))
    btn15.grid(row=3, column=3, sticky=tk.W+tk.E)

    btn15= tk.Button(buttonframe,
                     text="clear",
                     command=clear,
                     font=("arial", 18))
    btn15.grid(row=3, column=1, sticky=tk.W+tk.E)

    buttonframe.pack(fill="x")


    root.mainloop




process = "null"
def first_question():

    root.title("test")
    root.geometry("350x200")
    
    def draw_triangle(triangle, circle, square):
        root.destroy()
        import turtle
        screen = turtle.Screen()
        screen.reset
        screen.setup(500, 500)
        screen.bgcolor('blue')
        tur = turtle.Turtle()
        while loop != 33:
            trianglelist = [50, 30, 10, -20, -40, -60]
            value = random.choice(trianglelist)
            tur.forward(100)
            tur.left(120)
            tur.forward(value)
            turtlecordx = tur.xcor()
            turtlecordy = tur.ycor()
    def draw_circle(circle, triangle, square):
        root.destroy()
        loop = True
        turn = 0
        import turtle
        screen = turtle.Screen()
        screen.reset
        screen.setup(500, 500)
        screen.bgcolor('red')
        tur = turtle.Turtle()
        tur.forward(100)
        tur.left(90)
        while loop == True:
            tur.left(2)
            tur.forward(5)
            turn += 1
            if turn == 360:
                tur.left(20)
                turn = 0

    def draw_square():
        pass
    def snake():
        print("bitch, i dont have snake done, chill tf down")
    def parabola():
        import parabola
    def particle():
        import pygame_test_fr_this_time

    
    def login():
        btn1["state"] = "disabled"   #button state  disabled means?(already clicked)
        btn1["text"] = "logged" #text
        btn1["bg"] = "white" #background
        root.destroy()
        get_user_data()
        
    def math():
        btn2["state"] = "disabled"   #button state  disabled means?(already clicked)
        btn2["text"] = "math tine" #text
        btn2["bg"] = "white" #background
        root.destroy()
        math_process()


    def other():
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btnSquare = Button(root, text="square",
                           fg="white", bg="blue",
                           width=10, height=2,
                           command= lambda:draw_square(btnTriangle, btnCircle, btnSquare))
        btnTriangle = Button(root, text="triangle",
                             fg="white", bg="blue",
                             width=10, height=2,
                             command=lambda:draw_triangle(btnTriangle, btnCircle, btnSquare))
        btnCircle = Button(root, text="circle",
                           fg="white", bg="red",
                           width=10, height=2,
                           command=lambda:draw_circle(btnTriangle, btnCircle, btnSquare))

        btnTriangle.grid(column=1, row=1, padx=10, pady=10)
        btnCircle.grid(column=1, row=2, padx=10, pady=10)
    def games():
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btnsnake = Button(root, text="Snake",
                           fg="white", bg="green",
                           width=10, height=2,
                           command=snake)
        btnparabola = Button(root, text="Parabola",
                             fg="white", bg="blue",
                             width=10, height=2,
                             command=parabola)
        btnparticle = Button(root, text="Particles",
                           fg="white", bg="red",
                           width=10, height=2,
                           command=particle)

        btnsnake.grid(column=1, row=0, padx=10, pady=10)
        btnparabola.grid(column=1, row=1, padx=10, pady=10)
        btnparticle.grid(column=1, row=2, padx=10, pady=10)

        
    
    btn1 = Button(root, text="login",   #button refernece, same meaning as before
             fg="white", bg="green",#this button is enabled, it means that it
             width = 10, height = 2,  #this button is enabled, it means that it
             command=login)      # can be clicked
    btn1.grid(column=1, row=0, padx=10, pady=10)


    btn2 = Button(root, text="math",   #button refernece, same meaning as before
             fg="white", bg="blue",#this button is enabled, it means that it
             width = 10, height = 2,
             command=math)      # can be clicked
    btn2.grid(column=1, row=1, padx=10, pady=10)

    btn3 = Button(root, text="other",   #button refernece, same meaning as before
             fg="white", bg="red", #this button is enabled, it means that it
             width = 10, height = 2,
             command=other)      # can be clicked
    btn3.grid(column=1, row=2, padx=10, pady=10)
    btn4 = Button(root, text="games",   #button refernece, same meaning as before
             fg="white", bg="orange", #this button is enabled, it means that it
             width = 10, height = 2,
             command=games)      # can be clicked
    btn4.grid(column=2, row=0, padx=10, pady=10)
    root.mainloop()


first_question()

