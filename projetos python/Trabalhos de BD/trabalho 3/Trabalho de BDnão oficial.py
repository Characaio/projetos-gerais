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
            'Livros_info_geral':('Nome do Livro:',"Autor do Livro:","Editora do Livro:","Livraria do Livro:"),
            'Autores_info_geral':("Nome do Autor:","Idade do Autor:","Editora do Autor:","Livros do Autor:"),
            'Editora_info_geral':("Nome da Livraria:","Dono da Livraria:","Telefone da Livraria:","quantidade de livros:")
        }
        
        self.quantidade = 4
        # === Interface gráfica ===
        
        

        # Campo de entrada para o login
        self.entrada_info1 = tk.Entry(root)
        self.entrada_info1.grid(row=0, column=1, padx=5, pady=5)

        self.entrada_info2 = tk.Entry(root)
        self.entrada_info2.grid(row=1, column=1, padx=5, pady=5)
        
        self.entrada_info3 = tk.Entry(root)
        self.entrada_info3.grid(row=2, column=1, padx=5, pady=5)
        
        self.entrada_info4 = tk.Entry(root)
        self.entrada_info4.grid(row=3, column=1, padx=5, pady=5)
        
        self.entrada1 = tk.Label(root, text="")
        self.entrada1.grid(row=0, column=0, padx=5, pady=5)
        
        self.entrada2 = tk.Label(root, text="")
        self.entrada2.grid(row=1, column=0, padx=5, pady=5)
        
        self.entrada3 = tk.Label(root, text="")
        self.entrada3.grid(row=2, column=0, padx=5, pady=5)
        
        self.entrada4 = tk.Label(root, text="")
        self.entrada4.grid(row=3, column=0, padx=5, pady=5)
        
        self.entradas = [self.entrada_info1,self.entrada_info2,self.entrada_info3,self.entrada_info4]
        self.entradas_labels = [self.entrada1,self.entrada2,self.entrada3,self.entrada4]
        
        
        self.escolha_de_dados_texto = tk.Label(root,text='Aba Escolhida:',justify='right')
        self.escolha_de_dados_texto.grid(row=4,column=5,sticky='e')
        
        self.escolha_de_dados = ttk.Combobox(root, values=self.abas)
        self.escolha_de_dados.grid(row=4,column=6,pady=10)
        self.escolha_de_dados.set('Livros')
        self.escolha_de_dados.bind("<<ComboboxSelected>>",self.mudar_aba_placeholder)
        
        
        
        
        
        
        # Listbox (caixa de lista) para exibir os usuários registrados
        
        self.colunas = self.get_columns()
        
        self.minha_arvore = ttk.Treeview(root,columns=self.colunas,show='headings')
        self.minha_arvore.bind("<<TreeviewSelect>>",self.socorro)
        self.minha_arvore.bind("<Button-1>",self.verificar_clique)
        self.minha_arvore.grid(row=6,column=0,columnspan=8,sticky='we',padx=5,pady=5)

        
        
        
        
        self.btn_registrar = tk.Button(root, text="Registrar", command=self.registrar_usuario)
        self.btn_registrar.grid(row=4, column=0)
        
        self.btn_apagar_tudo = tk.Button(root, text="apagar tudo", command=self.apagar_tudo)
        self.btn_apagar_tudo.grid(row=5, column=0)
        
        self.btn_apagar_item = tk.Button(root,text='apagar item',command=self.deletar_item)
        self.btn_apagar_item.grid(row=5,column=1,pady=10)
        
        self.btn_editar_item = tk.Button(root,text='editar item',command=self.editar_item)
        self.btn_editar_item.grid(row=5,column=2,pady=10)
        
        self.arquivos_base = tk.Button(root,text='criar arquivos base',command=self.criar_arquivos_base)
        self.arquivos_base.grid(row=5,column=3,pady=10)
        
        self.carregar_dados()
        
        self.escolha_de_filtro_texto = tk.Label(root,text='flitrar por:',justify='right')
        self.escolha_de_filtro_texto.grid(row=5,column=5,sticky='e')
        
        self.escolha_de_filtro = ttk.Combobox(root, values='')
        self.escolha_de_filtro.set("")
        self.escolha_de_filtro.bind("<<ComboboxSelected>>",self.mudar_de_filtro)
        self.escolha_de_filtro.set("Nenhum")
        self.escolha_de_filtro.grid(row=5,column=6,pady=10)

        self.escolha_SLA_texto = tk.Label(root,text='socorro')
        self.escolha_SLA_texto.grid(row=0,column=4,pady=10,sticky='e')
        
        self.escolha_SLA = ttk.Combobox(root,values=self.get_columns())
        self.escolha_SLA.bind("<<ComboboxSelected>>",self.mudar_escolhar_placeholder)
        self.escolha_SLA.grid(row=0,column=5,pady=10)
        
        self.indice = 0
        
        self.mudar_aba()
        self.decidir_entradas()
        self.update_lista()
    
        
    def mudar_escolhar_placeholder(self,event):
        self.mudar_escolhar()
    
    def mudar_escolhar(self):
        print('socorro')
        temp = []
        self.indice = self.converter_escolha_para_indice()
        #self.escolha_de_filtro.config(values=self.escolha_SLA.get())
        for item in self.extrair_valores_dos_itens():
            print(f'não {item}')
            temp.append(item[self.indice])
        print(temp)
        self.escolha_de_filtro.config(values=temp)
    
    def get_seletores(self):
        temp = ['Nenhum']
        if self.aba == 'Livros':
            for livro in self.livros:
                print(f'1: {livro[2]}')
                temp.append(livro[2])
                
        if self.aba == 'Autores':
            for autor in self.autores:
                print(f'2: {autor[2]}')
                temp.append(autor[2])
                
        if self.aba == 'Livrarias':
            for livraria in self.livrarias:
                print(f'3: {livraria[2]}')
                temp.append(livraria[2])
                
        return temp
    
    def converter_escolha_para_indice(self):
        valor = self.escolha_SLA.get()
        print(f'self.escolha.items: {self.escolha.items()}')
        print(f'base: {valor}')
        
        #print(f'valor:  {self.escolha_SLA.get()}')
        for key,value in self.escolha.items():
            print(key,value)
            for i,valorzin in enumerate(value):
                if valorzin == valor:
                    self.indice = i
                    return i
    
    def mudar_de_filtro(self,event):
        valor = self.escolha_de_filtro.get()
        itens = []
        if valor == 'Nenhum':
            self.update_lista()
            return
        
        valores = self.extrair_valores_dos_itens()
        
        print(f'extrair valores: {valores}')
        print(f'valor do combobox {valor}')
        
        for valorzin in valores:
            print(f'brabo: {valorzin[self.converter_escolha_para_indice()]}')
            if valor in valorzin[self.converter_escolha_para_indice()]:
                print('EU TO AQUIIIIIII')
                itens.append(valorzin)
                self.minha_arvore.delete(*self.minha_arvore.get_children())
                self.minha_arvore.configure(columns=self.get_columns())
        print(itens)
        self.mudar_aba()
        
        for i in range(len(itens)):
            self.minha_arvore.insert('','end',values=itens[i])
        
                
                
                
    def verificar_clique(self,event):
        region = self.minha_arvore.identify("region",event.x,event.y)
        
        if region != "cell":
            self.minha_arvore.selection_remove(self.minha_arvore.selection())
            self.limpar_entradas()
            
    def criar_arquivos_base(self):
        self.apagar_tudo()
        self.carregar_dados()
        
    def socorro(self,event):
        selecionado = self.minha_arvore.selection()
        if selecionado:
            #print(selecionado)
            valores = self.minha_arvore.item(selecionado)['values']
            #print(f'oi: {valores}')
            #print(f'get info: {self.get_info()}')
            #self.minha_arvore.item(selecionado[0],values=self.get_info())
            self.limpar_entradas()
            values = []
            for i,entrada in enumerate(self.entradas):
                isso = self.minha_arvore.item(selecionado)['values']
                entrada.insert(0,isso[i])
            
    def editar_item(self):
        pass
        #if self.entrada_info1.get() and self.entrada_info2.get() and self.entrada_info3.get() and self.entrada_info4.get():
        selecionado = self.minha_arvore.selection()
        if selecionado:
            print(selecionado)
            valores = self.minha_arvore.item(selecionado)['values']
            print(f'oi: {valores}')
            print(f'get info: {self.get_info()}')
            self.minha_arvore.item(selecionado[0],values=self.get_info())
            self.limpar_entradas()
            
            values = self.extrair_valores_dos_itens()
                
            if self.aba == 'Livros':
                self.livros = values
                print(f'baguio brabasso{self.livros}')
            if self.aba == 'Autores':
                self.autores = values
                print(f'baguio brabasso{self.autores}')
            if self.aba == 'Livrarias':
                self.livrarias = values
                print(f'baguio brabasso{self.livrarias}')
            #quit()
            
    def get_columns(self):
        pass
        if self.aba == 'Livros':
            return self.escolha['Livros_info_geral']
        if self.aba == 'Autores':
            return self.escolha['Autores_info_geral']
        if self.aba == 'Livrarias':
            return self.escolha['Editora_info_geral']

    def mudar_nomes(self,tipo,quantidade):
        for i in range(quantidade):
            self.entradas_labels[i].config(text=self.escolha[tipo][i])
        

    def decidir_entradas(self):
        
        if self.aba == 'Livros':
            self.mudar_nomes('Livros_info_geral',len(self.escolha['Livros_info_geral']))
        if self.aba == 'Autores':
            self.mudar_nomes('Autores_info_geral',len(self.escolha['Autores_info_geral']))
        if self.aba == 'Livrarias':
            self.mudar_nomes('Editora_info_geral',len(self.escolha['Editora_info_geral']))
            
    def carregar_um_dado(self,arquivo):
        with open(arquivo,'r') as file:
            coisas = file.readlines()
            ngcs = []
            for coisa in coisas:
                ngc = []
                ngc = coisa.strip()
                ngc = ngc.split('|')
                ngc.remove('')
                ngcs.append(tuple(ngc))
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
        self.update_lista()

    def criar_arquivo(self,arquivo,temp):
        print(f'criar arquivo de {arquivo}')
        temp2 = ''
        with open(arquivo,'w') as file:
            for linha in temp:
                for item in linha:
                    temp2 += item + '|'
                file.write(temp2 + '\n')
                temp2 = ''
                
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
        for i in range(4):
            self.minha_arvore.heading(self.colunas[i],text=self.colunas[i])
        try:
            self.escolha_SLA.config(values=self.get_columns())
        except Exception as e:
            print(e)
        #self.update_lista()
        self.decidir_entradas()
        if self.escolha_de_filtro.get() == '':
            self.escolha_de_filtro.set("Nenhum")
    def mudar_aba_placeholder(self,event):
        self.mudar_aba()
        self.update_lista()
        
    def limpar_entradas(self):
        self.entrada_info1.delete(0, tk.END)
        self.entrada_info2.delete(0, tk.END)
        self.entrada_info3.delete(0, tk.END)
        self.entrada_info4.delete(0, tk.END)
        
    def get_info(self):
        info1 = self.entrada_info1.get().strip()
        info2 = self.entrada_info2.get().strip()
        info3 = self.entrada_info3.get().strip()
        info4 = self.entrada_info4.get().strip()
        return (info1,info2,info3,info4)
    
    def registrar_usuario(self):
        print('registrando o usuario')
        info1,info2,info3,info4 = self.get_info()

        if not info1 or not info2 or not info3 or not info4:
            messagebox.showwarning("Erro", "Algo ta vazio vagabundo")
            return
        if self.aba == 'Livros':
            if any(u[0] == info1 for u in self.livros):
                messagebox.showwarning("Erro", "Livro já cadastrado seu vagabundo")
                return
        if self.aba == 'Autores':
            if any(u[0] == info1 for u in self.autores):
                messagebox.showwarning("Erro", "autor já cadastrado seu vagabundo")
                return
        if self.aba == 'Livrarias':
            if any(u[0] == info1 for u in self.livrarias):
                messagebox.showwarning("Erro", "Livraria já cadastrado seu vagabundo")
                return

        item = (info1,info2,info3,info4)
        if self.aba == 'Livros':
            self.livros.append(item)
        if self.aba == 'Autores':
            self.autores.append(item)
        if self.aba == 'Livrarias':
            self.livrarias.append(item)

        self.update_lista()

        self.limpar_entradas()
    
    
    def salvar(self,arquivo,tipo_de_item):
        #print(f'salavamento individual {tipo_de_item}')
        with open(arquivo,'w') as file:
            for linha in tipo_de_item:
                temp2 = ''
                for item in linha:
                    str(item).strip()
                    if item:
                        temp2 += item + '|'
                file.write(temp2 + '\n')
                
                
    def extrair_valores_dos_itens(self):
        self.update_lista()
        values = []
        for item in self.minha_arvore.get_children():
            baguio = []
            for value in self.minha_arvore.item(item)['values']:
                if value:
                    
                    str(value).strip()
                    baguio.append(value)
            values.append(tuple(baguio))
        return values
    
    def salvar_dados_novos(self):   
        ngcs = self.extrair_valores_dos_itens()
        return ngcs
    
    def salvar_arquivo(self):
        #print(f'(NGC BRABOOOOOOOO :{self.salvar_dados_novos()})')
        print('salvando arquivos')
        print(f'livros: {self.livros}')
        #print(f'autores: {self.autores}')
        #print(f'Livrarias {self.livrarias}')
        
        if os.path.exists(self.livros_arquivo):
            self.salvar(self.livros_arquivo,self.livros)

        if os.path.exists(self.autores_arquivo):
            self.salvar(self.autores_arquivo,self.autores)
        
        if os.path.exists(self.livrarias_arquivo):
            self.salvar(self.livrarias_arquivo,self.livrarias)
        #print(f'(NGC BRABOOOOOOOO :{self.salvar_dados_novos()})')
        
    def apagar_tudo(self):
        print('apagando tudo')
        self.livros,self.autores,self.livrarias = '','',''
        
        if os.path.exists(self.livros_arquivo):
            os.remove(self.livros_arquivo)
        if os.path.exists(self.autores_arquivo):
            os.remove(self.autores_arquivo)
        if os.path.exists(self.livrarias_arquivo):
            os.remove(self.livrarias_arquivo)
        
        self.minha_arvore.delete(*self.minha_arvore.get_children())
        
        self.limpar_entradas()
        
    def sair(self):
        if messagebox.askokcancel("quit",'salvar antes de sair?'):
            self.salvar_arquivo()
            self.root.destroy()
        else:
            self.root.destroy()
            
    def deletar_item(self):
        print('deletando usuario')
        selecionado = self.minha_arvore.selection()
        itens = []
        self.minha_arvore.delete(*selecionado)
        for linha in self.minha_arvore.get_children():
            coiso = []
            for item in self.minha_arvore.item(linha)['values']:
                coiso.append(item)
            itens.append(tuple(coiso))
            
        if self.aba == 'Livros':
            self.livros = itens
        if self.aba == 'Autores':
            self.autores = itens
        if self.aba == 'Livrarias':
            self.livrarias = itens
            
        
        self.salvar_arquivo()
        self.limpar_entradas()
        
    
        
        
# Código principal para iniciar a aplicação
if __name__ == "__main__":
    root = tk.Tk()      # Cria a janela principal
    app = App(root)     # Instancia o aplicativo
    root.protocol("WM_DELETE_WINDOW",app.sair)
    root.mainloop()     # Executa o loop da interface gráfica
