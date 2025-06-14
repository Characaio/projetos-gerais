# Importa o módulo tkinter para criar a interface gráfica
import tkinter as tk
from tkinter import messagebox,ttk  # Para mostrar alertas e mensagens
import os
# Classe principal da aplicação
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Usuários")  # Título da janela
        for i in range(6):
            self.root.grid_columnconfigure(i,weight=1)
        self.dados = []  # Lista que vai armazenar tuplas (login, senha)
        self.aba = 'Livros'
        
        self.pasta_atual = os.path.dirname(os.path.abspath(__file__))
        self.livros_arquivo = os.path.join(self.pasta_atual,'livros.txt')
        self.autores_arquivo = os.path.join(self.pasta_atual,'autores.txt')
        self.livrarias_arquivo = os.path.join(self.pasta_atual,'livrarias.txt')
        
        self.livros = ''
        self.autores = ''
        self.livrarias =''
        self.abas = ['Livros','Autores','Livrarias']
        
        self.escolha= {
            'livros_info_geral':('Nome do Livro:',"Autor do Livro:","Editora do Livro:","Livraria do Livro:"),
            'Autores_info_geral':("Nome do Autor:","Idade do Autor:","Editora do Autor:","Livros do Autor:"),
            'Editora_info_geral':("Nome da Livraria:","Dono da Livraria:","Telefone da Livraria:","quantidade de livros:")
        }
        
        self.quantidade = 4
        # === Interface gráfica ===
        
        

        # Campo de entrada para o login
        self.nome_do_livro = tk.Entry(root)
        self.nome_do_livro.grid(row=0, column=1, padx=5, pady=5)

        self.autor_do_livro = tk.Entry(root)
        self.autor_do_livro.grid(row=1, column=1, padx=5, pady=5)
        
        self.editora_do_livro = tk.Entry(root)
        self.editora_do_livro.grid(row=2, column=1, padx=5, pady=5)
        
        self.livraria_do_livro = tk.Entry(root)
        self.livraria_do_livro.grid(row=3, column=1, padx=5, pady=5)
        
        self.entrada1 = tk.Label(root, text="")
        self.entrada1.grid(row=0, column=0, padx=5, pady=5)
        
        self.entrada2 = tk.Label(root, text="")
        self.entrada2.grid(row=1, column=0, padx=5, pady=5)
        
        self.entrada3 = tk.Label(root, text="")
        self.entrada3.grid(row=2, column=0, padx=5, pady=5)
        
        self.entrada4 = tk.Label(root, text="")
        self.entrada4.grid(row=3, column=0, padx=5, pady=5)
        
        self.carregar_dados()

        # Botão "Registrar" que chama a função registrar_usuario quando clicado
        self.btn_registrar = tk.Button(root, text="Registrar", command=self.registrar_usuario)
        self.btn_registrar.grid(row=4, column=0, pady=10)

        self.escolha_de_dados = ttk.Combobox(self.root, values=self.abas)
        self.escolha_de_dados.grid(row=4,column=6,pady=10)

        self.escolha_de_dados.set('Livros')
        self.escolha_de_dados.bind("<<ComboboxSelected>>",self.mudar_aba_placeholder)
        # Listbox (caixa de lista) para exibir os usuários registrados
        
        self.colunas = self.get_columns()
        self.minha_arvore = ttk.Treeview(root,columns=self.colunas,show='headings')
        self.minha_arvore.grid(row=6,column=0,columnspan=8,sticky='we',padx=5,pady=5)

        self.btn_apagar_tudo = tk.Button(root, text="apagar tudo", command=self.apagar_tudo)
        self.btn_apagar_tudo.grid(row=5, column=0, pady=10)
  
        self.mudar_aba()
        self.decidir_entradas()

    
    def get_columns(self):
        if self.aba == 'Livros':
            return self.escolha['Livros_info_geral']
        if self.aba == 'Autores':
            return self.escolha['Autores_info_geral']
        if self.aba == 'Livrarias':
            return self.escolha['Editora_info_geral']

    def mudar_nomes(self,tipo):
        self.entrada1.config(text=self.escolha[tipo][0])
        self.entrada2.config(text=self.escolha[tipo][1])
        self.entrada3.config(text=self.escolha[tipo][2])
        self.entrada4.config(text=self.escolha[tipo][3])

    def decidir_entradas(self):
        
        if self.aba == 'Livros':
            self.mudar_nomes('Livros_info_geral')
        if self.aba == 'Autores':
            self.mudar_nomes('Autores_info_geral')
        if self.aba == 'Livrarias':
            self.mudar_nomes('Editora_info_geral')
            
    def carregar_um_dado(self,arquivo):
        with open(arquivo,'r') as file:
            coisas = file.readlines()
            ngcs = []
            for coisa in coisas:
                ngc = []
                ngc = coisa.strip().split('|')
                ngcs.append(tuple(ngc))
            
            #print(ngcs)
            return ngcs
        
    def carregar_dados(self):
        if os.path.exists(self.livros_arquivo):
            self.livros = self.carregar_um_dado(self.livros_arquivo)
        else:
            temp = [('livro1','o brabo','sla','oi'),('livro2','o lixo','oi','sla'),('livro3','machado de asis','socorro','ui ui ui')]
            self.livros = temp
            self.criar_arquivo(self.livros_arquivo,temp)

        if os.path.exists(self.autores_arquivo):
            self.autores = self.carregar_um_dado(self.autores_arquivo)
        else:
            temp = [('machado de asis','60','adeus?','venha'),('sla','socorro','ola','SAI')]
            self.autores = temp
            self.criar_arquivo(self.autores_arquivo,temp)

        if os.path.exists(self.livrarias_arquivo):
           self.livrarias = self.carregar_um_dado(self.livrarias_arquivo)
        else:
            temp = [('toninho do grau','tonin','idoso','lerdo'),('tonhão do caminhão','tonhão','novo','rapido')]
            self.livrarias = temp
            self.criar_arquivo(self.livrarias_arquivo,temp)

    def criar_arquivo(self,arquivo,temp):
        print(f'criar arquivo de {arquivo}')
        temp2 = ''
        with open(arquivo,'w') as file:
            for linha in temp:
                for item in linha:
                    temp2 += item + '|'
                #print(temp2)
                file.write(temp2 + '\n')
                temp2 = ''
                
    # Função que registra o usuário
    def update_lista(self):
        print('atualizando a lista')
        print(self.aba)
        self.minha_arvore.delete(*self.minha_arvore.get_children())
        
        if self.aba == 'Livros':
            for i in range(len(self.livros)):
                self.minha_arvore.insert('','end',values=self.livros[i])
        if self.aba == 'Autores':
            for i in range(len(self.autores)):
                self.minha_arvore.insert('','end',values=self.autores[i])
        if self.aba == 'Livrarias':
            for i in range(len(self.livrarias)):
                self.minha_arvore.insert('','end',values=self.livrarias[i])

    def mudar_aba(self):
        print('mudando a aba')
        self.aba = self.escolha_de_dados.get()
        self.colunas = self.get_columns()
        self.minha_arvore.delete(*self.minha_arvore.get_children())
        self.minha_arvore.configure(columns=self.colunas)
        self.minha_arvore.heading(self.colunas[0],text=self.colunas[0])
        self.minha_arvore.heading(self.colunas[1],text=self.colunas[1])
        self.minha_arvore.heading(self.colunas[2],text=self.colunas[2])
        self.minha_arvore.heading(self.colunas[3],text=self.colunas[3])
        
        
        self.update_lista()
        self.decidir_entradas()
        
    def mudar_aba_placeholder(self,event):
        self.mudar_aba()
        

    def registrar_usuario(self):
        print('registrando o usuario')
        # Captura os valores dos campos de entrada
        nome_do_livro = self.nome_do_livro.get().strip()
        autor_do_livro = self.autor_do_livro.get().strip()
        editora_do_livro = self.editora_do_livro.get().strip()
        livraria_do_livro = self.livraria_do_livro.get().strip()

        # Verifica se os campos estão vazios
        if not nome_do_livro or not autor_do_livro or not editora_do_livro or not livraria_do_livro:
            messagebox.showwarning("Erro", "Algo ta vazio vagabundo")
            return

        # Verifica se o login já está na lista de usuários
        if any(u[0] == nome_do_livro for u in self.dados):
            messagebox.showwarning("Erro", "Livro já cadastrado seu vagabundo")
            return

        # Adiciona o usuário à lista (como uma tupla)
        item = (nome_do_livro,autor_do_livro,editora_do_livro,livraria_do_livro)
        if self.aba == 'Livros':
            self.livros.append(item)
        if self.aba == 'Autores':
            self.autores.append(item)
        if self.aba == 'Livrarias':
            self.livrarias.append(item)

        # Atualiza a lista na interface
        self.atualizar_lista()

        # Limpa os campos de entrada
        self.nome_do_livro.delete(0, tk.END)
        self.autor_do_livro.delete(0, tk.END)
        self.editora_do_livro.delete(0, tk.END)
        self.livraria_do_livro.delete(0, tk.END)
    
    def salvar(self,arquivo,tipo_de_item):
        print(f'salavamento individual {tipo_de_item}')
        with open(arquivo,'w') as file:
            temp2 = ''
            for linha in tipo_de_item:
                for item in linha:
                    temp2 += item + '|'
                #print(temp2)
                file.write(temp2 + '\n')
                temp2 = ''
                
    def salvar_arquivo(self):
        print('salvando arquivos')
        if os.path.exists(self.livros_arquivo):
            self.salvar(self.livros_arquivo,self.livros)

        if os.path.exists(self.autores_arquivo):
            self.salvar(self.autores_arquivo,self.autores)
        
        if os.path.exists(self.livrarias_arquivo):
            self.salvar(self.livrarias_arquivo,self.livrarias)
        
    def apagar_tudo(self):
        print('apagando tudo')
        self.livros,self.autores,self.livrarias = '','',''
        if os.path.exists(self.livros_arquivo):
            os.remove(self.livros_arquivo)
        if os.path.exists(self.autores_arquivo):
            os.remove(self.autores_arquivo)
        if os.path.exists(self.livrarias_arquivo):
            os.remove(self.livrarias_arquivo)
            
    def sair(self):
        if messagebox.askokcancel("quit",'salvar antes de sair?'):
            self.salvar_arquivo()
            self.root.destroy()
        else:
            self.root.destroy()
            
    def deletar_usuario(self):
        print('deletando usuario')
        selecionado = self.minha_arvore.selection()
        self.minha_arvore.delete(*selecionado)
        
        self.salvar_arquivo()
        
    # Função que atualiza a Listbox com os dados dos usuários
    def atualizar_lista(self):
        for login in self.dados:
            # Mostra login e senha na mesma linha
            if self.aba == 'Livros':
                self.livros.append((login))
            if self.aba == 'Autores':
                self.autores.append((login))
            if self.aba == 'Livrarias':
                self.livrarias.append((login))
        self.update_lista()
        
        self.dados = []

# Código principal para iniciar a aplicação
if __name__ == "__main__":
    root = tk.Tk()      # Cria a janela principal
    app = App(root)     # Instancia o aplicativo
    root.protocol("WM_DELETE_WINDOW",app.sair)
    root.mainloop()     # Executa o loop da interface gráfica