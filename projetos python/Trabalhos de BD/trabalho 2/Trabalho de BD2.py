import tkinter as tk
from tkinter import messagebox, colorchooser 
import random as rand

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Usuários")
        self.usuarios = []
        self.usuarios_cadastrados = 0
        self.senha_nova = ''
        self.teclado_caracteres = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', '^', '~',
        '¨', '˘', '˚', '˙', '¯','!', '@', '#', '$', '%', '¨', '&', '*',
        '(', ')','-', '_', '=', '+', '[', ']', '{', '}', '\\', '/', '?',
        '°', 'ª', 'º', '§', '¬', '¢', '£', '₢',':', ';', '.', ',', '<',
        '>'
        ]

        self.login_name = tk.Label(root, text="Login:")
        self.login_name.grid(row=0, column=0, padx=5, pady=5)

        self.entry_login = tk.Entry(root)
        self.entry_login.grid(row=0, column=1, padx=5, pady=5)

        self.senha_name = tk.Label(root, text="Senha:")
        self.senha_name.grid(row=1, column=0, padx=5, pady=5)

        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.grid(row=1, column=1, padx=5, pady=5)

        self.btn_registrar = tk.Button(root, text="Registrar", command=self.registrar_usuario)
        self.btn_registrar.grid(row=2, column=0, pady=10)

        self.btn_cor = tk.Button(root, text="mudar tema", command=self.escolher_cor)
        self.btn_cor.grid(row=2, column=2, pady=10)
        
        self.nome_de_quant = tk.Label(root, text='Quantidade de \n usuarios cadastrados')
        self.nome_de_quant.grid(row=0, column=2, padx=5, pady=5)

        self.quantidade = tk.Label(root, text=self.usuarios_cadastrados)
        self.quantidade.grid(row=1, column=2, padx=5, pady=5)

        self.lista_usuarios = tk.Listbox(root, width=50)
        self.lista_usuarios.grid(row=3, column=0, columnspan=4, padx=5, pady=5)
        
        self.salvar_arquivo = tk.Button(root, text="salvar usuarios", command=self.salvar_usuarios)
        self.salvar_arquivo.grid(row=4, column=0, columnspan=1, padx=5, pady=5)
        
        self.btn_deletar_usuario = tk.Button(root, text="deletar usuario", command=self.deletar_usuario)
        self.btn_deletar_usuario.grid(row=4, column=1, pady=10)
        
        self.btn_senha_aleatoria = tk.Button(root, text="senha aleatoria", command=self.senha_aleatoria)
        self.btn_senha_aleatoria.grid(row=4, column=2, pady=10)
        
        self.colocar_usuarios_antigos()
        self.ler_cor_antiga()
        
    def ler_cor_antiga(self):
        try:
            with open('cores do tema.txt','r') as file:
                cores = file.readlines()
                for i in cores:
                    self.cor1,self.cor2,self.cor3,self.fgcor = i.split(',')
                self.mudar_cores()
        except:
            file = open('cores do tema.txt','x')
            file.close()
            
    def deletar_usuario(self):
        print('deletando usuario')
        selecionado = self.lista_usuarios.curselection()
        if selecionado:
            self.lista_usuarios.delete(selecionado)
            self.atualizar_contador(-1)
            self.atualizar_lista()
            self.salvar_usuarios()
        print('usuario deletado') 
        
    def atualizar_contador(self,quantidade):
        print("Atualizando o contador")
        self.usuarios_cadastrados += quantidade
        self.contador_de_usuario = tk.Label(self.root, text=self.usuarios_cadastrados)
        try:
            self.contador_de_usuario.configure(bg=self.cor1,fg=self.fgcor)
        except Exception as e:
            print(e)
        self.contador_de_usuario.grid(row=1, column=2, padx=5, pady=5)
        print('Contador Atualizado')
        
    def senha_aleatoria(self):
        print('Gerando senha aleatoria')
        for i in range(rand.randint(8,20)):
            self.senha_nova += rand.choice(self.teclado_caracteres)
        self.entry_senha.insert(0,self.senha_nova)
        print('Senha aleatoria gerada')
        
    def colocar_usuarios_antigos(self):
        print('Lendo arquivos de cadastro')
        try:
            with open('usuarios.txt','r') as file:
                items = file.readlines()
            for item in items:
                self.atualizar_contador(1)
                self.lista_usuarios.insert(0, f"{item}")  
        except:
            print("Arquivo não existe")
        print('Arquivo de cadastro lido')
        
    def salvar_usuarios(self):
        print("salvei")
        coisas = self.lista_usuarios.get(0, tk.END)
        with open('usuarios.txt','w') as file:
            for coisa in coisas:
                if '\n' not in coisa:
                    file.write(f'{coisa} \n')
                else:
                    file.write(coisa)
                    
    def mudar_cores(self):
        print(self.cor1,self.cor2,self.cor3,self.fgcor)
        
        self.cor1.replace('|', '#')
        self.cor2.replace('|', '#')
        self.cor3.replace('|', '#')
        self.fgcor.replace('|', '#')
        
        print(self.cor1,self.cor2,self.cor3,self.fgcor)
        self.root.configure(bg=self.cor1)
    
        self.login_name.configure(bg=self.cor1,fg=self.fgcor)
        self.senha_name.configure(bg=self.cor1,fg=self.fgcor)
        self.nome_de_quant.configure(bg=self.cor1,fg=self.fgcor)
        self.quantidade.configure(bg=self.cor1,fg=self.fgcor)
        self.contador_de_usuario.configure(bg=self.cor1,fg=self.fgcor)
        
        self.btn_cor.configure(bg=self.cor2,fg=self.fgcor)
        self.btn_registrar.configure(bg=self.cor2,fg=self.fgcor)
        self.salvar_arquivo.configure(bg=self.cor2,fg=self.fgcor)
        self.btn_senha_aleatoria.configure(bg=self.cor2,fg=self.fgcor)
        self.btn_deletar_usuario.configure(bg=self.cor2,fg=self.fgcor)
        
        self.entry_login.configure(bg=self.cor3, fg=self.fgcor)
        self.entry_senha.configure(bg=self.cor3, fg=self.fgcor)
        self.lista_usuarios.configure(bg=self.cor3,fg=self.fgcor)
        
    def escolher_cor(self):
        print('mudei')
        self.cor1 = colorchooser.askcolor(title='escolha a cor principal')[1]
        self.cor2 = colorchooser.askcolor(title='escolha a cor secundaria')[1]
        self.cor3 = colorchooser.askcolor(title='escolha a cor de input')[1]
        self.fgcor = colorchooser.askcolor(title='escolha a cor do texto')[1]
            
        self.mudar_cores()
        
        with open('cores do tema.txt','w') as file:
            cores = [self.cor1,',',self.cor2,',',self.cor3,',',self.fgcor]
            for cor in cores:
                if '#' in cor:
                    cor.replace('#','|')
                file.write(str(cor))
                
    def registrar_usuario(self):
        print('Registrando usuario')
        login = self.entry_login.get().strip()
        senha = self.entry_senha.get().strip()
        if not login or not senha:
            messagebox.showwarning("Erro", "Login e senha não podem ser vazios!")
            return
        if any(u[0] == login for u in self.usuarios):
            messagebox.showwarning("Erro", "Login já cadastrado!")
            return
        self.usuarios.append((login, senha))
        self.atualizar_lista()
        self.atualizar_contador(1)
        self.entry_login.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        
        print('Usuario Registrado')
        
    def quando_fechar(self):
        if messagebox.askokcancel('sair?',"salvar os usuarios antes de sair?"):
            self.salvar_usuarios()
            self.root.destroy()
        else:
            self.root.destroy()
    
    def atualizar_lista(self):
        print('atualizando lista')
        for login, senha in self.usuarios:
            self.lista_usuarios.insert(tk.END, f"Login: {login} | Senha: {senha}")
        self.usuarios = []
        print('lista atualizada')
    
def main():
    root = tk.Tk()     
    app = App(root)     
    root.protocol("WM_DELETE_WINDOW", app.quando_fechar)
    root.mainloop()       
if __name__ == "__main__":
      main()