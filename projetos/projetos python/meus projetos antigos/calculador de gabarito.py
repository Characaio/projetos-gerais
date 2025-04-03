caio_respostas = ['C', 'C', 'C', 'A', 'B', 'B', 'C', 'A', 'B', 'D', 'A', 'C', 'D', 'C',
                  'D', 'D', 'D', 'C', 'A', 'C', 'A', 'B', 'B', 'D', 'A', 'A', 'D', 'D',
                  'D', 'C', 'C', 'C', 'D', 'C', 'C', 'B', 'D', 'B', 'B', 'A', 'B', 'D',
                  'C', 'B', 'A', 'D', 'B', 'C']
GABARITO = ['C', 'D', 'C', 'A', 'D', 'B', 'C', 'D', 'B', 'D', 'A', 'C', 'C', 'D', 'C',
            'D', 'A', 'C', 'B', 'C', 'B', 'A', 'C', 'D', 'A', 'A', 'D', 'A', 'D', 'C',
            'A', 'C', 'D', 'C', 'C', 'B', 'D', 'C', 'C', 'A', 'B', 'C', 'C', 'B', 'A',
            'D', 'B', 'A']

questões_corretas = ' '

corretas = 0
erradas = 0
for i in range(len(GABARITO)):
    num_da_questão = i+1
    if caio_respostas[i] == GABARITO[i]:
        print('Você acertou a resposta ' + str(num_da_questão))
        questões_corretas = questões_corretas + str(num_da_questão) + ','
        corretas += 1
    else:
        print('Você errou a resposta ' + str(num_da_questão) +
        ', a resposta correta era ' + GABARITO[i])
        erradas += 1



total = corretas + erradas
porcentagem = corretas/total
print('Você acertou as questões' + questões_corretas)
print('Você acertou ' + str(corretas) + ' questões'
      '\nVocê errou ' + str(erradas) + ' questões'
      '\nVocê acertou ' + str(porcentagem) + '%')
