import tkinter as tk
from tkinter import ttk

# Função para aplicar tema personalizado
def aplicar_tema_personalizado():
    style = ttk.Style()

    # Base do tema (use clam, alt, classic, default)
    style.theme_use('clam')

    # === Botão ===
    style.configure('MeuBotao.TButton',
                    background='#2b2b2b',
                    foreground='white',
                    font=('Segoe UI', 10, 'bold'),
                    padding=6,
                    borderwidth=1)
    style.map('MeuBotao.TButton',
              background=[('active', '#3c3f41')],
              foreground=[('disabled', 'gray')])

    # === Label ===
    style.configure('MeuLabel.TLabel',
                    background='#1e1e1e',
                    foreground='white',
                    font=('Segoe UI', 10))

    # === Entry ===
    style.configure('MeuEntry.TEntry',
                    fieldbackground='#2b2b2b',
                    foreground='white',
                    borderwidth=1,
                    font=('Segoe UI', 10))

    # === Combobox ===
    style.configure('MeuCombobox.TCombobox',
                    fieldbackground='#2b2b2b',
                    background='#2b2b2b',
                    foreground='white',
                    arrowcolor='white',
                    font=('Segoe UI', 10))

# Criar a janela principal
root = tk.Tk()
root.title("Tema Personalizado")
root.configure(bg='#1e1e1e')  # Fundo da janela

# Aplicar o tema
aplicar_tema_personalizado()

# Exemplo de Label
label = ttk.Label(root, text="Nome:", style='MeuLabel.TLabel')
label.pack(pady=(10, 0))

# Exemplo de Entry
entry = ttk.Entry(root, style='MeuEntry.TEntry')
entry.pack(pady=5, padx=10)

# Exemplo de Combobox
combo = ttk.Combobox(root, values=["Opção 1", "Opção 2"], style='MeuCombobox.TCombobox')
combo.set("Escolha")
combo.pack(pady=5, padx=10)

# Exemplo de Botão
botao = ttk.Button(root, text="Enviar", style='MeuBotao.TButton', command=lambda: print("Enviado"))
botao.pack(pady=20)

root.mainloop()
