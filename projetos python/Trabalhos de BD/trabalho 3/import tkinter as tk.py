import tkinter as tk
from tkinter import ttk

# Janela principal
root = tk.Tk()
root.title("Exemplo de Treeview com Hierarquia")
root.geometry("400x300")

# Criando o Treeview
tree = ttk.Treeview(root)

# Definindo as colunas (a coluna "#0" é a especial da hierarquia)
tree["columns"] = ("info",)
tree.column("#0", width=150, anchor="w")  # Coluna de hierarquia
tree.heading("#0", text="Nome")
tree.column("info", width=100, anchor="center")
tree.heading("info", text="Tipo")

# Inserindo itens hierárquicos
pasta1 = tree.insert("", "end", text="Documentos", values=["Pasta"])         # Raiz
tree.insert(pasta1, "end", text="Currículo.pdf", values=["Arquivo"])
tree.insert(pasta1, "end", text="Notas.txt", values=["Arquivo"])

pasta2 = tree.insert("", "end", text="Imagens", values=["Pasta"])           # Outra raiz
subpasta = tree.insert(pasta2, "end", text="Viagem", values=["Subpasta"])   # Subnível
tree.insert(subpasta, "end", text="praia.png", values=["Imagem"])
tree.insert(subpasta, "end", text="montanha.jpg", values=["Imagem"])

# Exibir o Treeview
tree.pack(expand=True, fill="both")

# Loop da interface
root.mainloop()
