import tkinter as tk
from tkinter import ttk, messagebox
import os

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Dados")

        self.aba = 'Livros'
        self.livros_arquivo = 'livros.txt'
        self.autores_arquivo = 'autores.txt'
        self.livrarias_arquivo = 'livrarias.txt'

        self.livros = []
        self.autores = []
        self.livrarias = []

        self.escolha = {
            'Livros_info_geral': ['Nome', 'Autor', 'Editora', 'Ano'],
            'Autores_info_geral': ['Nome', 'Idade', 'País', 'Obra Famosa'],
            'Editora_info_geral': ['Nome', 'Apelido', 'Tempo de Mercado', 'Velocidade'],
        }

        self.colunas = self.escolha['Livros_info_geral']

        self.setup_interface()
        self.carregar_dados()
        self.update_lista()

    def setup_interface(self):
        # Frame de escolha
        topo_frame = tk.Frame(self.root)
        topo_frame.pack()

        self.escolha_de_dados = ttk.Combobox(topo_frame, values=['Livros', 'Autores', 'Livrarias'])
        self.escolha_de_dados.set('Livros')
        self.escolha_de_dados.bind("<<ComboboxSelected>>", self.mudar_aba_placeholder)
        self.escolha_de_dados.pack(side=tk.LEFT)

        # Árvore
        self.minha_arvore = ttk.Treeview(self.root, columns=self.colunas, show='headings')
        for col in self.colunas:
            self.minha_arvore.heading(col, text=col)
        self.minha_arvore.pack()

        self.minha_arvore.bind('<Double-1>', self.socorro)

        # Entradas
        self.entradas = []
        self.entradas_labels = []
        for i in range(4):
            lbl = tk.Label(self.root, text=self.colunas[i])
            lbl.pack()
            self.entradas_labels.append(lbl)
            entry = tk.Entry(self.root)
            entry.pack()
            self.entradas.append(entry)

        self.entrada_info1 = self.entradas[0]
        self.entrada_info2 = self.entradas[1]
        self.entrada_info3 = self.entradas[2]
        self.entrada_info4 = self.entradas[3]

        # Botões
        botoes_frame = tk.Frame(self.root)
        botoes_frame.pack()

        tk.Button(botoes_frame, text='Registrar', command=self.registrar_usuario).pack(side=tk.LEFT)
        tk.Button(botoes_frame, text='Editar', command=self.editar_item).pack(side=tk.LEFT)
        tk.Button(botoes_frame, text='Deletar', command=self.deletar_item).pack(side=tk.LEFT)
        tk.Button(botoes_frame, text='Salvar', command=self.salvar_arquivo).pack(side=tk.LEFT)
        tk.Button(botoes_frame, text='Apagar Tudo', command=self.apagar_tudo).pack(side=tk.LEFT)

    def mudar_aba_placeholder(self, event):
        self.aba = self.escolha_de_dados.get()
        self.colunas = self.get_columns()
        self.minha_arvore.configure(columns=self.colunas)
        for i in range(4):
            self.minha_arvore.heading(self.colunas[i], text=self.colunas[i])
        self.decidir_entradas()
        self.update_lista()

    def get_columns(self):
        if self.aba == 'Livros':
            return self.escolha['Livros_info_geral']
        if self.aba == 'Autores':
            return self.escolha['Autores_info_geral']
        if self.aba == 'Livrarias':
            return self.escolha['Editora_info_geral']

    def decidir_entradas(self):
        nomes = self.get_columns()
        for i, lbl in enumerate(self.entradas_labels):
            lbl.config(text=nomes[i])

    def carregar_um_dado(self, arquivo):
        ngcs = []
        with open(arquivo, 'r') as file:
            for linha in file:
                partes = [p for p in linha.strip().split('|') if p]
                ngcs.append(tuple(partes))
        return ngcs

    def carregar_dados(self):
        if os.path.exists(self.livros_arquivo):
            self.livros = self.carregar_um_dado(self.livros_arquivo)
        else:
            temp = [('livro1', 'o brabo', 'sla', 'oi')]
            self.livros = temp
            self.criar_arquivo(self.livros_arquivo, temp)

        if os.path.exists(self.autores_arquivo):
            self.autores = self.carregar_um_dado(self.autores_arquivo)
        else:
            temp = [('machado de asis', '60', 'brasil', 'dom casmurro')]
            self.autores = temp
            self.criar_arquivo(self.autores_arquivo, temp)

        if os.path.exists(self.livrarias_arquivo):
            self.livrarias = self.carregar_um_dado(self.livrarias_arquivo)
        else:
            temp = [('livraria x', 'x', '20 anos', 'rápido')]
            self.livrarias = temp
            self.criar_arquivo(self.livrarias_arquivo, temp)

    def criar_arquivo(self, arquivo, dados):
        with open(arquivo, 'w') as file:
            for linha in dados:
                file.write('|'.join(linha) + '|\n')

    def update_lista(self):
        self.minha_arvore.delete(*self.minha_arvore.get_children())
        dados = self.obter_dados_atual()
        for item in dados:
            self.minha_arvore.insert('', 'end', values=item)

    def obter_dados_atual(self):
        if self.aba == 'Livros':
            return self.livros
        if self.aba == 'Autores':
            return self.autores
        if self.aba == 'Livrarias':
            return self.livrarias
        return []
    def get_info(self):
        return tuple(entry.get().strip() for entry in self.entradas)

    def registrar_usuario(self):
        info = self.get_info()
        if any(not campo for campo in info):
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        self.minha_arvore.insert('', 'end', values=info)
        self.adicionar_ao_dado(info)
        self.salvar_arquivo()
        self.limpar_entradas()

    def adicionar_ao_dado(self, info):
        if self.aba == 'Livros':
            self.livros.append(info)
        elif self.aba == 'Autores':
            self.autores.append(info)
        elif self.aba == 'Livrarias':
            self.livrarias.append(info)

    def editar_item(self):
        selecionado = self.minha_arvore.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um item para editar!")
            return

        novos_valores = self.get_info()
        self.minha_arvore.item(selecionado, values=novos_valores)

        # Atualiza na lista
        valores_antes = tuple(str(v).strip() for v in self.minha_arvore.item(selecionado)['values'])
        self.remover_dado(valores_antes)
        self.adicionar_ao_dado(novos_valores)

        self.salvar_arquivo()
        self.limpar_entradas()

    def remover_dado(self, valores):
        if self.aba == 'Livros':
            self.livros = [item for item in self.livros if item != valores]
        elif self.aba == 'Autores':
            self.autores = [item for item in self.autores if item != valores]
        elif self.aba == 'Livrarias':
            self.livrarias = [item for item in self.livrarias if item != valores]

    def deletar_item(self):
        selecionado = self.minha_arvore.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um item para deletar!")
            return

        for item_id in selecionado:
            valores = tuple(str(v).strip() for v in self.minha_arvore.item(item_id)['values'])
            self.minha_arvore.delete(item_id)
            self.remover_dado(valores)

        self.salvar_arquivo()
        self.limpar_entradas()

    def salvar_arquivo(self):
        self.salvar(self.livros_arquivo, self.livros)
        self.salvar(self.autores_arquivo, self.autores)
        self.salvar(self.livrarias_arquivo, self.livrarias)

    def salvar(self, arquivo, dados):
        with open(arquivo, 'w') as file:
            for item in dados:
                file.write('|'.join(item) + '|\n')

    def apagar_tudo(self):
        if not messagebox.askyesno("Confirmação", "Tem certeza que deseja apagar tudo?"):
            return
        self.livros, self.autores, self.livrarias = [], [], []
        for arquivo in [self.livros_arquivo, self.autores_arquivo, self.livrarias_arquivo]:
            if os.path.exists(arquivo):
                os.remove(arquivo)
        self.minha_arvore.delete(*self.minha_arvore.get_children())
        self.limpar_entradas()

    def extrair_valores_dos_itens(self):
        values = []
        for item in self.minha_arvore.get_children():
            valores = tuple(str(v).strip() for v in self.minha_arvore.item(item)['values'] if v)
            values.append(valores)
        return values

    def socorro(self, event):
        selecionado = self.minha_arvore.selection()
        if selecionado:
            valores = self.minha_arvore.item(selecionado)['values']
            for i in range(len(self.entradas)):
                self.entradas[i].delete(0, tk.END)
                self.entradas[i].insert(0, valores[i])

    def limpar_entradas(self):
        for entry in self.entradas:
            entry.delete(0, tk.END)

    def sair(self):
        if messagebox.askokcancel("Sair", "Salvar antes de sair?"):
            self.salvar_arquivo()
        self.root.destroy()


# Código principal
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.protocol("WM_DELETE_WINDOW", app.sair)
    root.mainloop()
