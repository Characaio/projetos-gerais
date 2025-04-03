

notas = [3,6,'R',10,4,7,'I',3,'MB','B',2,5,8,4,'R','B',3,11]
velocidades = [10,20,70,80,60,30,65,38,97,69,56,58]
pães = [10,6,28,9,109,1,5]
repeat = True
tipo = 3
#0 = avaliação
#1 = multa
#2 padaria
#3 portugol


def avaliação(nota):
    if nota == int:
        if nota >= 5 and nota <= 10:
            return 'aprovado'
        elif nota > 10:
            return 'erro'
        else:
            return 'reprovado'
    else:
        if nota == 'I':
            return 'reprovado'
        else:
            return 'aprovado'

def multa(vel_do_carro):
    if vel_do_carro > 60:
        return 'tomou multa'
    else:
        return 'não tomou multa'


def padaria(quant):
    valor = quant *0.90
    return valor

def portugol(num):
    global repeat
    try:
        num = int(num)
        print(f'isso é um numero fi, ele é {num}, gatão ele ein fiu fiu')
        repeat = False
    except:
        print('o seu desgraça isso nn é um numero top')
        
    
    
if tipo == 0:
    for i in range(len(notas)):
        print(f'a nota do aluno {i} é de {notas[i]} e ele foi {avaliação(notas[i])}')
elif tipo == 1:
    for i in range(len(velocidades)):
        print(f'o carro esta indo a {velocidades[i]} por hora, ele {multa(velocidades[i])}')
elif tipo == 2:
    for i in range(len(pães)):
        print(f'quantidade de pães é de {pães[i]} e o valor pago é de {padaria(pães[i])}')
elif tipo == 3:
    while repeat:
        numero = input('mete um numeero top ')
        portugol(numero)
