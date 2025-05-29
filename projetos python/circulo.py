import tkinter as tk

def criar_janela_redonda():
    janela = tk.Tk()
    janela.title("Janela redonda")

    janela.overrideredirect(True)

    largura = 400
    altura = 400 
    janela.geometry(f"{largura}x{altura}+100+100")
    canvas = tk.Canvas(janela,width=largura, height=altura)
    canvas.pack()
    colors = ["lightblue","blue","red","lightblue","blue","red","lightblue","blue","red","lightblue","blue","red","lightblue","blue","red","lightblue","blue"]
    for i in range(0,len(colors)):
        canvas.create_oval(0+(10*i),0+(10*i), largura-(10*i), altura-10*i, fill=colors[i], outline=colors[1])
        #canvas.create_polygon(10,10,200,100,(200,200))
    def fechar_janela():
        janela.destroy()
    
    def mudar():
        colors.pop(-1)
    botao = tk.Button(janela, text="fechar", command=fechar_janela, bg="red", fg="white", relief="flat")  
    botao2 = tk.Button(janela,text="mudar",command=mudar)  
    botao2.pack()
    canvas.create_window(largura // 2, altura // 2, window=botao)

    janela.mainloop()
criar_janela_redonda()