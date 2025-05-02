
produto = None

def adicionar_produto(item_final):
    with open('produtinhos.txt') as sla:
        temporario = sla.read()
    item,preço = item_final.split(' ')
    with open("produtinhos.txt", 'w') as f:
        f.write()
        f.write(f'{ temporario}{item_final} \n')
        print(f'item {item} adicionado com preço de R${preço}')


def remover_produto():
    pass
def alterar_texto():
    print(" Você g")
def remover_tudo():
    with open('produtinhos.txt', 'w+') as f:
        f.write("")

def selecione():
    #arroz, feijão
    item = str(input("escolha um produtinhooooooooo: "))
    preço = float(input('e qual seu valor?: '))
    item_final = str(item ) + ' ' + str(preço)
    adicionar_produto(item_final)

def mostrar_produtos():
   
    try:
        with open("produtinhos.txt") as produtos:
            print(produtos.read())
            print('arquivo lido')
    except:
        print('criando um arquivo')
        f = open("produtinhos.txt", "x")
        print('arquivo criado')
    escolha = int(input('vocÊ quer adicionar(0), remover(1) ou outro?'))
    if escolha == 0:
        selecione()
    

def mostrar_selecionados():
    pass


mostrar_produtos()