import random as rand

##mercado negro
##orgãos, ossos de varios tamanhos e de diferentes vitimas
##vem de crianças, adultos e idosos
##classifique eles em tipo, depois idade, depois o nome do item




def mercado_negro():
    items_na_caixa = []
    escolha_da_caixa = []
    max_da_caixa = 10
    idade = ['criança', 'adulto', 'idoso']
    ossos = ['femur', 'costela', 'cranio', 'maxilar', 'escapula', 'tibia','vertebra']
    orgãos = ['coração', 'pulmão', 'rim', 'figado', 'olhos', 'lingua', 'pancreas', 'intestino']
    aleatorio = rand.randint(0,1)
    for i in range(max_da_caixa):
        if aleatorio == 0 :
            items_na_caixa.append((idade[rand.randint(0,2)], orgãos[rand.randint(0,7)]))
        else:
            items_na_caixa.append((idade[rand.randint(0,2)], ossos[rand.randint(0,6)]))
                 
    for j in range(max_da_caixa):
        print(f' o {items_na_caixa[j][1]} pertence a/ao {items_na_caixa[j][0]}')
        
    print(items_na_caixa)
   
##sistema de escrita
##o usuario coloca uma palavra ou frase
##cada letra da frase é multiplicado por um numero aleatorio
## cada letra é randomizada quando o programa é rodado
##a randomização vai de 1 a 27
##no final retorne o resultado


repeat = True
def sistema_de_escrita():
    letras = []
    final:str = ''
    multiplicadores = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
                       16,17,18,19,20,21,22,23,24,25,26,27]
    rand.shuffle(multiplicadores)
    palavra = str(input('escreva algo '))
    for letra in palavra:
        letras.append(letra)
    for i in range(len(letras)):
        if letras[i] != ' ':
            final += letras[i]*multiplicadores[i]
        else: 
            final += letras[i]
    return final
        



while repeat:
    tipo = str(input('qual função você quer?(0/1) '))
    if tipo == '0':
        mercado_negro()
    elif tipo == '1':
        escolha = str(input('tu quer escrrever algo novo?sim/não '))
        if escolha == 'sim':
            print(sistema_de_escrita())
        else:
            repeat = False

