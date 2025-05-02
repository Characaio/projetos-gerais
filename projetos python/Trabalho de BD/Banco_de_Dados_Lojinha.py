import os

separador = '|'
arquivo_dos_produtos = 'produtinhos.txt'

def verificar_arquivo():
    if os.path.exists(arquivo_dos_produtos):
        print('arquivo existe')
    else:
        print('criando arquivo')
        open(arquivo_dos_produtos, 'x')
        print('arquivo criado')
        
    
        
def adicionar_produto(item_final):
    temporario = ''
    print('-'*20)
    
    with open(arquivo_dos_produtos, 'r') as file:
        temporario = file.read()
    
    with open(arquivo_dos_produtos, 'w') as file:
        
        item,preço = item_final.split(separador)
        file.write(f'{temporario}\n{item_final} ')
        print(f'Item: {item} Adicionado com preço de R${preço}')
        
        listar_produtos()
        
def tem_produtos(linhas):
    for i in range(len(linhas)):
        for j in range(len(linhas[i])):
            if linhas[i][j] == separador:
                return True
    return False

def remover_produto():
    print('-'*20)
    repete = True
    with open(arquivo_dos_produtos, 'r+') as file:
        linhas = file.readlines()
        listar_produtos()
        
        if tem_produtos(linhas):
            escolha = int(input('Remova um produto pelo id: '))
            referencia = linhas[escolha]
            del linhas[escolha]
            print(f'Item apagado')
        else:
            print('Não tem produto aqui')
    with open(arquivo_dos_produtos, 'w') as file:
        file.writelines(linhas)
        
def listar_produtos():
    print('-'*20)
    with open(arquivo_dos_produtos, 'r') as file:
        linhas = file.readlines()
    for id,item in enumerate(linhas):
        if item != '\n':
            produto,preço = item.split(separador)
            print(f'Id:{id} Item:{produto} Preço:{preço}')
    
                
def alterar_produto():
    linhas = ''
    repete = True
    with open(arquivo_dos_produtos, "r+") as file:
        
        linhas = file.readlines()

        print('-'*20)
        listar_produtos()
        
        escolha = int(input('Qual item vc quer trocar? Use seu ID: '))
        
        itemzin,preço = linhas[escolha].split(separador)
        print(f'Item: {itemzin} Preço: {preço}')
        while repete:
            print('-'*20)
            escolha2 = str(input("Quer trocar o preço, item ou quer sair?\nPreço\nItem\nSair"))
            escolha2.lower()
            print('-'*20)
            
            if escolha2 == 'preço':
                print('-'*20)
                preço = float(input('Coloque um novo preço: \n'))
                print(preço)
            elif escolha2 == 'item':
                print('-'*20)
                itemzin = str(input('Coloque um novo item: \n'))
                print(itemzin)
            elif escolha2 == 'sair':
                print('-'*20)
                mudado = str(itemzin) + separador  + str(preço) 
                print(str(itemzin) + separador  + str(preço))
                escolha3 = str(input('Certeza que você quer aplicar essas mudanças?[Sim/Não] \n'))
                if escolha3.lower() == 'sim':
                    
                    linhas[escolha] = mudado
                    print('Mudanças salvas')
                    repete = False
            else:
                print('Opção Invalida')
        
    with open(arquivo_dos_produtos, 'w') as file:
        file.writelines(linhas)
        
def remover_tudo():
    print('-'*20)
    escolha = str(input('Excluir aquivo?[Sim/Não]'))
    if escolha.lower() == 'sim':
        if os.path.exists(arquivo_dos_produtos):
            os.remove(arquivo_dos_produtos)
            print('Arquivo apagado')
        else:
            print('O arquivo nn existe mlk')
    menu()
    

def selecione():
    print('-'*20)
    #arroz, feijão
    item = str(input("Escolha um produtinho: "))
    preço = float(input('E qual seu valor?: '))
    item_final = str(item ) + separador + str(preço)
    adicionar_produto(item_final)


def menu():
    repeat = True
    verificar_arquivo()
    
    while repeat:
        try:
            print('-'*20)
            escolha = int(input('Adicionar(0) Remover(1) Remover Tudo(2) Alterar Produto(3) Listar Produtos(4) ou Sair(5)? \n'))
            if escolha == 0:
                selecione()
            elif escolha == 1:
                remover_produto()
            elif escolha == 2:
                remover_tudo()
            elif escolha == 3:
                alterar_produto()
            elif escolha == 4:
                listar_produtos()
            elif escolha == 5:
                print('saindo do programa')
                repeat = False
                
            else:
                print('escolha uma opção valida')
        except ValueError:
            print('numero invalido')
        except IndexError:
            print('index fora da lista')
    print('programa terminado')
    quit()

menu()