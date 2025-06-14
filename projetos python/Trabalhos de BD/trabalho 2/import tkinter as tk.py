import tkinter as tk
from tkinter import ttk, messagebox
import os

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Biblioteca")

        # Estrutura de dados
        self.livros = []

        # Arquivo para salvar os dados
        self.arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "livros.txt")

        # Campos de entrada
        tk.Label(root, text="Título:").grid(row=0, column=0)
        tk.Label(root, text="Autor:").grid(row=1, column=0)
        tk.Label(root, text="Editora:").grid(row=2, column=0)
        tk.Label(root, text="Livraria:").grid(row=3, column=0)

        self.titulo = tk.Entry(root)
        self.autor = tk.Entry(root)
        self.editora = tk.Entry(root)
        self.livraria = tk.Entry(root)

        self.titulo.grid(row=0, column=1)
        self.autor.grid(row=1, column=1)
        self.editora.grid(row=2, column=1)
        self.livraria.grid(row=3, column=1)

        # Treeview
        self.tree = ttk.Treeview(root, columns=("Título", "Autor", "Editora", "Livraria"), show='headings')
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.grid(row=5, column=0, columnspan=3, sticky="we")

        # Botões
        tk.Button(root, text="Registrar", command=self.registrar).grid(row=4, column=0)
        tk.Button(root, text="Apagar Selecionado", command=self.apagar_selecionado).grid(row=4, column=1)
        tk.Button(root, text="Filtrar Autor", command=self.filtrar_autor).grid(row=4, column=2)
        tk.Button(root, text="Limpar Filtro", command=self.atualizar_tree).grid(row=6, column=0)

        self.filtro_autor_entry = tk.Entry(root)
        self.filtro_autor_entry.grid(row=6, column=1)

        # Carregar dados do arquivo
        self.carregar()

        # Atualizar visual
        self.atualizar_tree()

    def registrar(self):
        t = self.titulo.get().strip()
        a = self.autor.get().strip()
        e = self.editora.get().strip()
        l = self.livraria.get().strip()

        if not t or not a or not e or not l:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        self.livros.append((t, a, e, l))
        self.salvar()
        self.atualizar_tree()

        self.titulo.delete(0, tk.END)
        self.autor.delete(0, tk.END)
        self.editora.delete(0, tk.END)
        self.livraria.delete(0, tk.END)

    def salvar(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            for livro in self.livros:
                f.write("|".join(livro) + "\n")

    def carregar(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as f:
                for linha in f:
                    dados = linha.strip().split("|")
                    if len(dados) == 4:
                        self.livros.append(tuple(dados))

    def atualizar_tree(self, lista=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
        lista = lista if lista is not None else self.livros
        for livro in lista:
            self.tree.insert("", tk.END, values=livro)

    def apagar_selecionado(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Info", "Selecione um item para apagar.")
            return
        for item in sel:
            valores = self.tree.item(item, "values")
            if valores in self.livros:
                self.livros.remove(valores)
        self.salvar()
        self.atualizar_tree()

    def filtrar_autor(self):
        autor_filtro = self.filtro_autor_entry.get().strip()
        if not autor_filtro:
            messagebox.showinfo("Info", "Digite um autor para filtrar.")
            return
        filtrados = [livro for livro in self.livros if livro[1].lower() == autor_filtro.lower()]
        self.atualizar_tree(filtrados)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
