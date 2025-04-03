##sistema de mercado
##usuario compra 1 tem de cada prateleira
##desconto é aplicado aleatoriamente em certos items
##5 itens no total tera algum desconto
##cada prateleira tem 10 items
##no final, um caixa eletronico ira te dar o valor total da compra


import random as rand


#isso é uma lista 3d,isso quer dizer que, é uma lista, dentro de uma lista, dentro de uma, eu fiz isso para
#a lista de fora é referenciada por I, do meio por J, e a menor por numero de 0 para o nome do item, 1 para o preço
#do item, e 2 para o desconto
#a lista esta assim montada nesse estilo:
##    [
##        [
##            [
##            ]
##        ]
##    ]
#a lista menor tem o nome do item, preço, e seu desconto
#isso facilita e deixa mais facil para achar os valores e muda-los

informações = [
    [
        ['Garrafa de Água', 3.5, 1],
        ['Pacote de Arroz', 15.5, 1],
        ['Sabonete', 2.0, 1],
        ['Detergente', 4.3, 1],
        ['Café', 8.5, 1],
        ['Desinfetante', 7.0, 1],
        ['Balde de Plástico', 9.5, 1],
        ['Escova de Dentes', 5.0, 1],
        ['Papel Higiênico', 12.0, 1],
        ['Motosserra', 799.0, 1]
    ],
    [
        ['Espátula de Cozinha', 10.0, 1],
        ['Panela de Pressão', 150.0, 1],
        ['Aspirador de Pó', 299.0, 1],
        ['Alvejante', 5.5, 1],
        ['Máquina de Café', 250.0, 1],
        ['Cesta de Frutas', 30.0, 1],
        ['Liquidificador', 120.0, 1],
        ['Feijão', 7.0, 1],
        ['Cerveja', 5.0, 1],
        ['Abridor de Latas', 8.0, 1]
    ],
    [
        ['Biscoito', 3.8, 1],
        ['Vassoura', 15.0, 1],
        ['Cesta de Pão', 25.0, 1],
        ['Garfo de Churrasco', 18.0, 1],
        ['Cozinha Elétrica', 100.0, 1],
        ['Paninho de Prato', 6.0, 1],
        ['Café em Grãos', 35.0, 1],
        ['Saco de Batatas', 10.0, 1],
        ['Saco de Sal', 3.0, 1],
        ['Chá', 12.0, 1]
    ],
    [
        ['Frigideira', 45.0, 1],
        ['Corta Verduras', 22.0, 1],
        ['Batedeira', 150.0, 1],
        ['Churrasqueira', 220.0, 1],
        ['Fogão', 800.0, 1],
        ['Máquina de Lavar Roupas', 1200.0, 1],
        ['Mesa de Jantar', 600.0, 1],
        ['Sofá', 1500.0, 1],
        ['Cadeira de Escritório', 350.0, 1],
        ['Estante de Livros', 250.0, 1]
    ],
    [
        ['Garrafa de Vinho', 35.0, 1],
        ['Cadeira de Praia', 40.0, 1],
        ['Lâmpada LED', 15.0, 1],
        ['Toalha de Banho', 25.0, 1],
        ['Tapete', 150.0, 1],
        ['Espelho de Banheiro', 120.0, 1],
        ['Secador de Cabelos', 90.0, 1],
        ['Cortina de Sala', 100.0, 1],
        ['Rodo', 12.0, 1],
        ['Ferro de Passar', 150.0, 1]
    ],
    [
        ['Mochila', 60.0, 1],
        ['Protetor Solar', 25.0, 1],
        ['Papel Alumínio', 7.0, 1],
        ['Corda de Pular', 20.0, 1],
        ['Jogo de Xadrez', 50.0, 1],
        ['Livro de Receitas', 35.0, 1],
        ['Escova de Cabelos', 40.0, 1],
        ['Faca de Cozinha', 80.0, 1],
        ['Grãos de Milho', 12.0, 1],
        ['Camiseta', 30.0, 1]
    ],
    [
        ['Tênis Esportivo', 150.0, 1],
        ['Cinto de Ferramentas', 75.0, 1],
        ['Macarrão', 6.0, 1],
        ['Almofada', 35.0, 1],
        ['Caminhão de Brinquedo', 50.0, 1],
        ['Caixa de Som', 120.0, 1],
        ['Monitor de Computador', 900.0, 1],
        ['Caixa Térmica', 80.0, 1],
        ['Pistola de Cola Quente', 25.0, 1],
        ['Câmera Fotográfica', 1200.0, 1]
    ],
    [
        ['Cadeira de Escritório', 400.0, 1],
        ['Carregador de Celular', 40.0, 1],
        ['Roupão', 70.0, 1],
        ['Régua', 5.0, 1],
        ['Relógio de Pulso', 200.0, 1],
        ['Cama Box', 800.0, 1],
        ['Carrinho de Bebê', 600.0, 1],
        ['Travesseiro', 50.0, 1],
        ['Óculos de Sol', 100.0, 1],
        ['Relógio de Parede', 60.0, 1]
    ],
    [
        ['Balança', 45.0, 1],
        ['Câmera de Segurança', 250.0, 1],
        ['Almofada de Pescoço', 25.0, 1],
        ['Desodorante', 15.0, 1],
        ['Livro', 40.0, 1],
        ['Cortador de Cabelo', 150.0, 1],
        ['Fritadeira Elétrica', 350.0, 1],
        ['Mochila de Camping', 130.0, 1],
        ['Relógio de Pulso', 120.0, 1],
        ['Pó de Café', 25.0, 1]
    ],
    [
        ['Cachorro Quente', 8.0, 1],
        ['Sorvete', 15.0, 1],
        ['Saco de Lixo', 3.0, 1],
        ['Cerveja', 6.0, 1],
        ['Caixa de Papelão', 7.0, 1],
        ['Alicate', 25.0, 1],
        ['Escova de Roupas', 15.0, 1],
        ['Galocha', 90.0, 1],
        ['Garfo de Mesa', 10.0, 1],
        ['Bateria para Carro', 300.0, 1]
    ]
]


#essa lissta ira segurar o nome e o preço dos items, o nome sera referido por [0] e o preço por[1]
info_dos_escolhidos = []

#descontos a ser escolhido
possiveis_descontos = [0.95,0.90,0.85,0.80,0.75,0.70,0.65,0.60,0.55,0.50,0.45,0.40,0.35,0.30,0.25,0.20]

#nome das prateleiras
nomes_da_prateleiras = ['primeira','segunda',
                            'terceira','quarta',
                            'quinta','sexta',
                            'setima','oitava',
                            'nona','decima']
def compras():
    
    total:int = 0
    correct:bool = False

    #isso randomiza os descontos, e no for loop eu mudo o desconto de um item aleatorio
    rand.shuffle(possiveis_descontos)
    for i in range(5):
        informações[rand.randint(0,9)][rand.randint(0,9)][2] = possiveis_descontos[i]

    #esse for loop passa por TODAS prateleiras
    for i in range(len(nomes_da_prateleiras)):
        escolhido:bool = False
        print(f'escolha um item da {nomes_da_prateleiras[i]} prateleira')
        #esse for loop passa por todos os items da prateleira
        for j in range(10):
            #define se o item tem desconto, se tiver ele aplica o desconto e avisa o usuario sobre ele
            if informações[i][j][2] != 1:
                   print(f'ID= {j} item:{(informações[i][j][0])} preço:{round(float(informações[i][j][1])*informações[i][j][2],2)} desconto:{informações[i][j][2]}')
            else:
                print(f'ID= {j} item:{(informações[i][j][0])} preço:{round(float(informações[i][j][1]))}')

        #esse while força o usuario a escolher algo antes de ir ao proximo
        while not escolhido:
            
            #escolhe o item da prateleira
            try:
                escolha = int((input('qual item da prateleira você quer?')))
                #esse if verifica se o numero é valido, ou seja,
                #se ele é um integer e se ele esta entre 0 a 10
                
                if escolha > 0 and escolha < 10:
                    escolhido = True
                else:
                    print('escolha um numero valido')
            #isso cuida dos erros caso o usuario coloque um algo que não é um integer
            #por isso que colocamos o escolha como um integer de maneira forçada
            except:
                print('nananinanão, mete um NUMERO imbecil')
                #print('escolha um numero valido')
       
       
        #isso verifica se o item escolhido tem um desconto
        if informações[i][escolha][2] != 1:
            print(f' opa tu achou um desconto massa aqui, ele é de {round(1-informações[i][escolha][2],2)}%')
        #isso coloca a informação dos items em uma lista para uso futuro
        info_dos_escolhidos.append((informações[i][escolhido][0],
                                    informações[i][escolhido][1]*informações[i][j][2]))

        #isso fala qual item você escolheu e de qual prateleira
        print(f'você escolheu o item {informações[i][escolha][0]} da {nomes_da_prateleiras[i]} prateleira')

    #isso passa por todos os items escolhidos 
    for v in range(len(info_dos_escolhidos)):
        #mostra as informações do item e na linha debaixa adiciona o preço ao total
        print(f' o item escolhido é o {info_dos_escolhidos[v][0]}, e o preço dele é {round(info_dos_escolhidos[v][1],3)}')
        total += info_dos_escolhidos[v][1]
    #retorna o total e o aredonda até 3 digitos para evitar erro em relação a floats
    return round(total,3)

print(compras())
