import os

separador = '|'
arquivo_dos_produtos = 'produtinhos.txt'
Mudança = ''
def verificar_arquivo():
    if os.path.exists(arquivo_dos_produtos):
        print('arquivo existe')
    else:
        print('criando arquivo')
        open(arquivo_dos_produtos, 'x')
        print('arquivo criado')
        
    
        
def adicionar_produto(item_final):
    global Mudança
    Mudança = ''
    temporario = ''
    produto_cadastrado = False
    produto = int
    escolha2 = ''
    item1,preço1,quant1 = str,str,str
    print('-'*20)
    item,preço,quantidade = item_final.split(separador)
    repete = True
    with open(arquivo_dos_produtos, 'r') as file:
        linhas = file.readlines() 
        a = file.read()
    for id,linha in enumerate(linhas):
        if linha != '\n':
            item1,preço1,quant1 = linha.split(separador)
            if item1 == item:
                produto_cadastrado = True
                Mudança = id
                escolha1 = str(input('produto ja cadastrado, deseja alterar ele?[Sim/Não] \n$ '))
                alterar_produto()
                # listar_produtos()
                
                # escolha2 = int(input('Escolha o produto pelo ID'))
                # if escolha1.lower() == 'sim':
                #     quant1 = int(quant1) + 1
                #     mudado = str(item1) + separador + str(preço1) + separador + str(quant1)
                # # print(linhas)
                # # print('mudei')
                # linhas[escolha2] = mudado
                # # print(linhas)
                # # print('a')
                # # print(temporario)
    with open(arquivo_dos_produtos, 'r') as file:
        temporario = file.read()
        
    with open(arquivo_dos_produtos, 'w') as file:
        if not produto_cadastrado:
            print(f'Adiconado {quantidade} {item} com o o preço de R${preço}')
            file.write(f'{temporario}\n{item_final} ')
        else:
            file.write(f'{temporario}')
        #print(f'Item: {item} Adicionado com preço de R${preço}')
        
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
            escolha = int(input('Remova um produto pelo id: \n$ '))
            referencia = linhas[escolha]
            del linhas[escolha]
            print(f'{referencia} apagado')
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
            produto,preço,quantidade, = item.split(separador)
            
            for i,quant in enumerate(quantidade):
                if quant == '\n' or quant == ' ':
                    pass
                else:
                    quant1 = quant
                    
            print(f'Id: {id}  Item: {produto}  Quantidade: {quant1}  Preço: R${preço} ')

                
def alterar_produto():
    linhas = ''
    repete = True
    with open(arquivo_dos_produtos, "r+") as file:
        
        linhas = file.readlines()

        print('-'*20)
        listar_produtos()
        if Mudança == '':
            escolha = int(input('Qual item vc quer trocar? Use seu ID: \n$ '))
        else:
            escolha = Mudança
        itemzin,preço,quantidade = linhas[escolha].split(separador)
        
        while repete:
            print('-'*20)
            print(f'Item: {itemzin}  Preço: {preço}  Quantidade {quantidade}')
            print('-'*20)
            escolha2 = str(input("Quer trocar o preço, item ou quer sair?\nPreço\nItem\nQuantidade\nSair \n$ "))
            escolha2.lower()
            print('-'*20)
            
            if escolha2 == 'preço':
                print('-'*20)
                preço = float(input('Coloque um novo preço: \n$ '))
                print(preço)
            elif escolha2 == 'item':
                print('-'*20)
                itemzin = str(input('Coloque um novo item: \n$ '))
                print(itemzin)
            elif escolha2 == 'quantidade':
                print('-'*20)
                quantidade = int(input('Coloque uma nova quantidade \n$ '))
            elif escolha2 == 'sair':
                print('-'*20)
                if linhas[escolha] == linhas[-1]:
                    mudado = str(itemzin) + separador  + str(preço) + separador + str(quantidade)
                else:
                    mudado = str(itemzin) + separador  + str(preço) + separador + str(quantidade) + '\n'
                print(str(itemzin) + separador  + str(preço) + separador + str(quantidade))
                escolha3 = str(input('Certeza que você quer aplicar essas mudanças?[Sim/Não] \n$ '))
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
    escolha = str(input('Excluir aquivo?[Sim/Não] \n$ '))
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
    item = str(input("Escolha um produtinho: \n$ "))
    preço = float(input('Qual seu valor?: \n$ '))
    quantidade = int(input('Quantos desse produto tem? \n$ '))
    item_final = str(item ) + separador + str(preço) + separador + str(quantidade)
    adicionar_produto(item_final)


def menu():
    repeat = True
    verificar_arquivo()
    
    while repeat:
        try:
            print('-'*20)
            escolha = int(input('Adicionar(0) Remover(1) Remover Tudo(2) Alterar Produto(3) Listar Produtos(4) ou Sair(5)? \n$ '))
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
        except ValueError as e:
            print(e)
            print('numero invalido')
            
        except IndexError as e:
            print(e)
            print('id inexistente')
    print('programa terminado')
    quit()

menu()