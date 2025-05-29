# Importa o módulo tkinter para criar a interface gráfica
import tkinter as tk
from tkinter import messagebox  # Para mostrar alertas e mensagens

# Classe principal da aplicação
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Usuários")  # Título da janela

        self.usuarios = []  # Lista que vai armazenar tuplas (login, senha)

        # === Interface gráfica ===

        # Label "Login"
        tk.Label(root, text="Login:").grid(row=0, column=0, padx=5, pady=5)

        # Campo de entrada para o login
        self.entry_login = tk.Entry(root)
        self.entry_login.grid(row=0, column=1, padx=5, pady=5)

        # Label "Senha"
        tk.Label(root, text="Senha:").grid(row=1, column=0, padx=5, pady=5)

        # Campo de entrada para a senha (com os caracteres ocultos)
        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.grid(row=1, column=1, padx=5, pady=5)

        # Botão "Registrar" que chama a função registrar_usuario quando clicado
        self.btn_registrar = tk.Button(root, text="Registrar", command=self.registrar_usuario)
        self.btn_registrar.grid(row=2, column=0, columnspan=2, pady=10)

        # Listbox (caixa de lista) para exibir os usuários registrados
        self.lista_usuarios = tk.Listbox(root, width=50)
        self.lista_usuarios.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # Função que registra o usuário
    def registrar_usuario(self):
        # Captura os valores dos campos de entrada
        login = self.entry_login.get().strip()
        senha = self.entry_senha.get().strip()

        # Verifica se os campos estão vazios
        if not login or not senha:
            messagebox.showwarning("Erro", "Login e senha não podem ser vazios!")
            return

        # Verifica se o login já está na lista de usuários
        if any(u[0] == login for u in self.usuarios):
            messagebox.showwarning("Erro", "Login já cadastrado!")
            return

        # Adiciona o usuário à lista (como uma tupla)
        self.usuarios.append((login, senha))

        # Atualiza a lista na interface
        self.atualizar_lista()

        # Limpa os campos de entrada
        self.entry_login.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)

    # Função que atualiza a Listbox com os dados dos usuários
    def atualizar_lista(self):
        self.lista_usuarios.delete(0, tk.END)  # Limpa a lista anterior
        for login, senha in self.usuarios:
            # Mostra login e senha na mesma linha
            self.lista_usuarios.insert(tk.END, f"Login: {login} | Senha: {senha}")

# Código principal para iniciar a aplicação
if __name__ == "__main__":
    root = tk.Tk()      # Cria a janela principal
    app = App(root)     # Instancia o aplicativo
    root.mainloop()     # Executa o loop da interface gráfica