question = str("null")
invalid = False
loop = int("0")
import webbrowser
import random
from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
admin = False
questionaire = False
data = []



    
def get_user_data():
    import tkinter as tk
    
    root = tk.Tk()
    root.geometry("300x500")
    root.resizable(False, False) #esse (false,false) quer dizer que ela bnão pode ser esticada
    root.title("sign in")

   
        
    #essas são as variaveis,
    #o stringvar é uma variavel que pode ser mudada por uma janela TK
    name = tk.StringVar()
    age = tk.StringVar()
    city = tk.StringVar()
    email = tk.StringVar()
    RA = tk.StringVar()
    extra = tk.StringVar()
    caio_data = ["caio, 14, sbo"]
    name1 = ''
    age1 = ''
    city1 = ''
    email1 = ''
    RA1 = ''
    extra1 = '' 
    def person_login(dat):
        pass
            
            
    
    #isso computa suas respostas e abre uma janela com o showinfo
    def login_clicked():
        
        name1 = name_entry.get()
        age1 = age_entry.get()
        city1 = city_entry.get()
        email1 = email_entry.get()
        RA1 = RA_entry.get()
        extra1 = extra1_entry.get()
        data = name1 + '|' + age1 + '|' + city1 + '|' + email1 + '|' + RA1 + '|'
        data_full = name1 + ' ' + age1 + ' ' + city1
        
        

                
        
                
        try:
            with open(f'{name1} data.txt', 'r+') as user_data:
                print('its read')
        except:
            with open(f'{name1} data.txt', 'w') as user_data:
                user_data.write('')
                print('its written')
        def view_content():
            with open(f'{name1} data.txt', 'r') as user_data:
                print(f'{user_data.read()}')
        def write_content():
            with open(f'{name1} data.txt', 'a') as user_data:
                user_data.write(f'{write_entry.get()}.\n')
        def clear():
            with open(f'{name1} data.txt', 'w') as user_data:
                user_data.write('')
        
        
        with open(f'{name1} data.txt') as file:
            file_content = file.read()
            if data not in file_content:
                msg = f' seu nome é {name_entry.get()},você tem {age_entry.get()} anos de idade e mora em {city_entry.get()}'
                showinfo(
                    title='Information',
                    message=msg
                )
                with open('data.txt', 'r+') as file:
                    file_read = file.read()
                    if data_full in file_read:
                        print('the data is already here')
                    else:
                        print('data is written')
                        file.write(f'{data_full}.\n')
                person_login(data)
                print(data)
                print(msg)
            else:
                
                print('wait for next')
        import tkinter as tk
        root = tk.Tk()
        root.geometry('300x300')
        view_button = Button(root,text='view', width=5, height=3,
                             command=view_content)
        write_button = Button(root,text='write', width=5, height=3,
                              command=write_content)
        write_entry = Entry(root)
        clear_file = Button(root, text='clear', width=5, height=3,
                            command=clear)
                
                

                
        view_button.grid(row=0, column=0, pady=5, padx=5)
        write_button.grid(row=1, column=0, pady=5, padx=5)
        clear_file.grid(row=2, column=0, pady=5, padx=5)
        write_entry.grid(row=3, column=0, pady=5, padx=5)
        
                
                            
                        
                
    #um frame de referencia
    signin = tk.Frame(root)
    instructions_label = tk.Label(signin, text='ra,idade e RA é obrigatorio,o resto é opcional')
    signin.pack(padx=10, pady=10, fill="x")


    name_label = tk.Label(signin,
                          text="coloque seu nome:")
    name_label.pack(fill='x')

    name_entry = tk.Entry(signin,
                          textvariable=name)
    name_entry.pack(fill='x')
    name_entry.focus()

    
    age_label = tk.Label(signin,
                         text="sua idade:")
    age_label.pack(fill='x')

    age_entry = tk.Entry(signin,
                         textvariable=age)
    age_entry.pack(fill='x')


    city_label = tk.Label(signin,
                          text="sua cidade:")
    city_label.pack(fill="x")

    city_entry = tk.Entry(signin,
                          textvariable=city)
    city_entry.pack(fill="x")

    
    email_label = tk.Label(signin,
                          text="seu email:")
    email_label.pack(fill="x")

    email_entry = tk.Entry(signin,
                          textvariable=email)
    email_entry.pack(fill="x")


    RA_label = tk.Label(signin,
                          text="seu RA:")
    RA_label.pack(fill="x")

    RA_entry = tk.Entry(signin,
                          textvariable=RA)
    RA_entry.pack(fill="x")



    


    confirm_button = tk.Button(signin,
                               text="login",
                               command=login_clicked)
    confirm_button.pack(fill="x", pady=10)

    root.mainloop()
    
    
    
numb = ""
next_expression = True
new_acc = False
operator1 = False
def math_process(): #calculadora funcional, não suporta multiplos tipos de conta em uma expressão
    import tkinter as tk

    root2 = tk.Tk()

    root2.geometry("500x500")
    root2.title("my first GUI")

    display_box = tk.Text(root2, width=20, height=5, font=("arial", 18))
    display_box.pack(fill="x", padx=15, pady = 15)

    buttonframe = tk.Frame(root2)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    buttonframe.columnconfigure(2, weight=1)
    
    
        

        
    global addition1
    addition1 = False
    global subtraction1
    subtraction1 = False
    global multiplication1
    multiplication1 = False
    global division1
    division1 = False

    

    def clear():
        display_box.delete("1.0", "end")
        global numb
        numb = ""
        global new_acc
        new_acc = False

    def get_total(total):
        global totali
        global nextex
        nextex = True
        totali = ""
        print(str(addition1) + "+")
        print(str(subtraction1) + "-")
        print(str(multiplication1) + "*")
        print(str(division1) + "/")
        if addition1 == True:
            totali = str(total) + "+"
        elif subtraction1 == True:
            totali = str(total) + "-"
        elif multiplication1 == True:
            totali = str(total) + "*"
        elif division1 == True:
            totali = str(total) + "/"
        else:
            totali = total
            print(str(totali) + " allFALSE")
        global operator1
        operator1 = False
        global new_acc
        new_acc = True
        display_box.delete("1.0", "end")
        display_box.insert(END, totali)
        global numb
        numb = ""



        
    def addition(numb):
            
            [num1, num2] = (numb.split("+"))
            num1 = float(num1)
            num2 = float(num2)
            total = num1 + num2
            get_total(total)
    def subtraction(numb):
            [num1, num2] = (numb.split("-"))
            num1 = float(num1)
            num2 = float(num2)
            total = num1 - num2
            get_total(total)
    def multiplication(numb):
            [num1, num2] = (numb.split("*"))
            num1 = float(num1)
            num2 = float(num2)
            total = num1 * num2
            get_total(total)
    def division(numb):
            [num1, num2] = (numb.split("/"))
            num1 = float(num1)
            num2 = float(num2)
            total = num1 / num2
            get_total(total)
    def turn_in_decimal():
        pass
    #resolver problema de não continuar a conta apos colocar um segundo operador
    def get_numb(number):
        global numb
        global nextex
        global addition1
        addition1 = False
        global subtraction1
        subtraction1 = False
        global multiplication1
        multiplication1 = False
        global division1
        division1 = False
        operators = ["+", "-", "*", "/"]
        if new_acc == False:
            numb = numb + str(number)
        else:
            if nextex == True:
                global totali
                
                if number in operators:
                    numb = numb + str(number)

                else:
                    numb = str(totali) + str(float(number))
                nextex = False
                print(str(nextex)+'afterassigniment')
            else:
                if numb in operators:
                    print("oops, its the bug time")
                else:
                    print(str(nextex)+"falsexpression")
                    numb = float(totali) + float(number)
        print(numb)
        
        


    def account(x):
        global operator1
        global numb
        global addition1
        global subtraction1
        global multiplication1
        global division1

        operators = ["+", "-", "*", "/"]
        if x != "=":
            if x in operators and "+" in numb:
                if x == "+":
                    
                    addition1 = True
                    addition(numb)
                if x == "-":
                    
                    subtraction1 = True
                    addition(numb)
                if x == "*":
                    
                    multiplication1 = True
                    addition(numb)
                if x == "/":
                    
                    division1 = True
                    addition(numb)
            elif x in operators and "-" in numb:
                if x == "+":
                    
                    addition1 = True
                    subtraction(numb)
                if x == "-":
                    
                    subtraction1 = True
                    subtraction(numb)
                if x == "*":
                    
                    multiplication1 = True
                    subtraction(numb)
                if x == "/":
                    
                    division1 = True
                    subtraction(numb)
            elif x in operators and "*" in numb:
                if x == "+":
                    
                    addition1 = True
                    multiplication(numb)
                if x == "-":
                    
                    subtraction1 = True
                    multiplication(numb)
                if x == "*":
                    
                    multiplication1 = True
                    multiplication(numb)
                if x == "/":
                    
                    division1 = True
                    multiplication(numb)
            elif x in operators and "/" in numb:
                if x == "+":
                    
                    addition1 = True
                    division(numb)
                if x == "-":
                    
                    subtraction1 = True
                    division(numb)
                if x == "*":
                    
                    multiplication1 = True
                    division(numb)
                if x == "/":
                    
                    division1 = True
                    division(numb)
            else:
                
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

    def conversion():
        import tkinter as tk
        conv = tk.Tk()
        conv.geometry("500x300")
        conv.title("convertor")

        #centimetro para inches, taxa de conversão, 0.3937
        
        
        def convert():
            result.delete("1.0", "end")
            
            selected = selected_unit.get()
            inch_conversion = float(0.3937) #in
            yard_conversion = float(1.0936) #yards
            mile_conversion = float(0.6214) #mile
            if selected == "cm to in":
                centimeters=f'{entry_convert.get()}'
                converted = float(centimeters) * inch_conversion
                converted = str(converted) + "inches"
                print(converted)
                result.insert(END, converted)
            elif selected == "meter to yards":
                meter = f'{entry_convert.get()}'
                converted = float(meter) * yard_conversion
                converted = str(converted) + "yards"
                print(converted)
                result.insert(END, converted)
            elif selected == "kilometer to mile":
                kilometer =f'{entry_convert.get()}'
                converted = float(kilometer) * mile_conversion
                converted = str(converted) + "miles"
                print(converted)
                result.insert(END, converted)

        
        
        btn_frame = Frame(conv)

        btn_frame = Frame(conv)
        options = ("cm to in", "meter to yards", "kilometer to mile")
        selected_unit = tk.StringVar()
        selected_unit.set(options[0])
        selection = tk.OptionMenu(btn_frame, selected_unit, *options,)
        
        
        

        
        

        btncon1 = Button(btn_frame, text="convert", command=convert)
        
        entry_convert = Entry(btn_frame)
        
        btn_label = Label(conv, text="conversion math", font=("arial", 24, "bold"))
        
        btn_label2 = Label(conv, text="", font=("arial", 12, "bold"))

        btn_label3 = Label(conv, text="")
        btn_label3.config(text=f'{selected_unit.get()}')
        result = Text(btn_frame,font=("arial", 12), height=1)

        
        
        btncon1.grid(row=0, column=3)
        entry_convert.grid(row=0, column=1, sticky=tk.W+tk.E)
        result.grid(row=0, column=4)
        
        btn_label.pack()
        btn_frame.pack()
        btn_label2.pack()
        btn_label3.pack()
        selection.grid(row=1, column=0, columnspan=2)

        

        conv.mainloop()
        
            


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
                     text="=",
                     command=lambda:account("="),
                     font=("arial", 18))
    btn11.grid(row=3, column=2, sticky=tk.W+tk.E+tk.S+tk.N)


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
    
    btn16= tk.Button(buttonframe,
                     text=".",
                     command=turn_in_decimal,
                     font=("arial", 18))
    btn16.grid(row=4, column=3, sticky=tk.W+tk.E)

    btn17= tk.Button(buttonframe,
                     text="conversion calculator",
                     command=conversion,
                     font=("arial", 18))
    btn17.grid(row=4, column=0, columnspan=3, sticky=tk.W+tk.E)
    
    buttonframe.pack(fill="x", pady=1)


    root.mainloop





process = "null"
def first_question():
    
    root.title("test")
    root.geometry("350x200")
    
    def draw_triangle():
        
        import turtle as turtle1
        loop1 = 0
        screen1 = turtle1.Screen()
        screen1.reset
        screen1.setup(500, 500)
        screen1.bgcolor('blue')
        tur1 = turtle1.Turtle()
        while loop1 != 33:
            trianglelist = [50, 30, 10, -20, -40, -60]
            value1 = random.choice(trianglelist)
            tur1.forward(100)
            tur1.left(120)
            tur1.forward(value1)
            turtlecordx = tur1.xcor()
            turtlecordy = tur1.ycor()
    def draw_circle():
        
        loop2 = True
        turn2 = 0
        import turtle as turtle2
        screen2 = turtle2.Screen()
        screen2.reset
        screen2.setup(500, 500)
        screen2.bgcolor('red')
        tur2 = turtle2.Turtle()
        tur2.forward(100)
        tur2.left(90)
        while loop2 == True:
            tur2.left(2)
            tur2.forward(5)
            turn2 += 1
            if turn2 == 360:
                tur2.left(20)
                turn2 = 0

    def draw_square():

        
        loop3 = True

        import turtle as turtle3
        screen3 = turtle3.Screen()
        screen3.reset
        screen3.setup(500, 500)
        screen3.bgcolor("green")
        tur3 = turtle3.Turtle()
        while loop3 == True:
            squarelist = [50, 30, 10, -20, -40, -60]
            value3 = random.choice(squarelist)
            tur3.forward(100 + value3)
            tur3.left(90)

    def combo():
        
        loop4 = 1
        loop1 = True
        loop2 = True
        loopT = 0
        turn4 = 0
        turns4 = 0

        import turtle as turtle4
        screen4 = turtle4.Screen()
        screen4.reset
        screen4.setup(500, 500)
        screen4.bgcolor("pink")
        tur4 = turtle4.Turtle()
        if loop4 == 1:
            while loopT != 6:
                trianglelist = [50, 30, 10, -20, -40, -60]
                value = random.choice(trianglelist)
                tur4.forward(100)
                tur4.left(120)
                tur4.forward(value)
                turtlecordx = tur4.xcor()
                turtlecordy = tur4.ycor()
                loopT += 1
                loop4 = 2
                loop14 = True
        if loop4 == 2:
            tur4.left(2)
            tur4.forward(5)
            turn=0
            while loop14 == True:
                circlelist = [-30, 30]
                value4 = random.choice(circlelist)
                tur4.left(2)
                tur4.forward(value)
                turn4 += 1
                if turn4 == 45:
                    
                    loop4 = 3
                    loop2 = True
                    loop1 = False
                    
        if loop4 == 3:
            while loop2 == True:
                turns4 += 1
                squarelist4 = [50, 30, 10, -20, -40, -60]
                value4 = random.choice(squarelist)
                tur4.forward(100 + value4)
                tur4.left(90)
                if turns4 == 12:
                    loop4 = 1
                    loopT = 0
                    turn4 = 0
                    loop2 = False
                    




    
    import tkinter as tk2
    def login():
        #btn1["state"] = "disabled"   #button state  disabled means?(already clicked)
        #btn1["text"] = "logged" #text
        #btn1["bg"] = "white" #background
        
        get_user_data()
        
    def math():
        #btn2["state"] = "disabled"   #button state  disabled means?(already clicked)
        #btn2["text"] = "math tine" #text
        #btn2["bg"] = "white" #background
        
        math_process()


    def other():
        
        root2 = tk2.Tk()
    
        root2.title("other")
        root2.geometry("350x200")
        root2.focus()
        
        btnSquare = Button(root2, text="square",
                           fg="white", bg="green",
                           width=10, height=2,
                           command=draw_square)
        btnTriangle = Button(root2, text="triangle",
                             fg="white", bg="blue",
                             width=10, height=2,
                             command=draw_triangle)
        btnCircle = Button(root2, text="circle",
                           fg="white", bg="red",
                           width=10, height=2,
                           command=draw_circle)

        btnCombo = Button(root2, text="combo",
                           fg="white", bg="pink",
                           width=10, height=2,
                           command=combo)
        

        btnSquare.grid(column=0, row=0, padx=10, pady=10)
        btnTriangle.grid(column=0, row=1, padx=10, pady=10)
        btnCircle.grid(column=0, row=2, padx=10, pady=10)
        btnCombo.grid(column=1, row=0, padx=10, pady=10)
    def tic_tac_toe():
        with open("tic tac toe.py") as file:
                  exec(file.read())
    def get_games():
        import tkinter as tk
        root2 = tk.Tk()
        btnSnake = Button(root2, text="tic tac toe",
                          fg="white", bg="green",
                          width=10, height=2,
                          command=tic_tac_toe)


        btnSnake.grid(row=0,column=0, padx=10, pady=10)

    
        
        
    
    btn1 = Button(root, text="login",   #button refernece, same meaning as before
             fg="white", bg="green",#this button is enabled, it means that it
             width = 10, height = 2,  #this button is enabled, it means that it
             command=login)      # can be clicked
    btn1.grid(column=0, row=0, padx=10, pady=10)


    btn2 = Button(root, text="math",   #button refernece, same meaning as before
             fg="white", bg="blue",#this button is enabled, it means that it
             width = 10, height = 2,
             command=math)      # can be clicked
    btn2.grid(column=0, row=1, padx=10, pady=10)

    btn3 = Button(root, text="other",   #button refernece, same meaning as before
             fg="white", bg="red", #this button is enabled, it means that it
             width = 10, height = 2,
             command=other)      # can be clicked
    btn3.grid(column=0, row=2, padx=10, pady=10)

    btn4 = Button(root, text="games",
                              fg="white", bg="orange",
                              width=10, height=2,
                              command=get_games)
    btn4.grid(column=1, row=0, padx=10, pady=10)

    

    root.mainloop()


first_question()

