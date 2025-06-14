respostas = ['A', 'B', 'C', 'C', 'D', 'C', 'D', 'C', 'A', 'A', 'C', 'D', 'C', 'A', 'B', 'C', 'D', 'A', 'C', 'B', 'D', 'A', 'C', 'D' , 'C']
GABARITO = ['A', 'C', 'B', 'C', 'D', 'A', 'C', 'B', 'D', 'B', 'C', 'A', 'C', 'D', 'B', 'C', 'A', 'C', 'B', 'D', 'C', 'A', 'C', 'D' , 'B']
corretas = 0
erradas = 0
for i in range(len(GABARITO)):
    pergunta = i+1
    if respostas[i] == GABARITO[i]:
        corretas += 1
        print('a pergunta ' + str(pergunta) + ' esta certa')
    else:
        erradas += 1
        print('a pergunta ' + str(pergunta) + ' esta errada')
porcentagem = corretas/len(GABARITO)
print('você acertou ' + str(corretas) + ' de '+ str(len(GABARITO)) +
      '\nvocê errou ' + str(erradas) + ' de ' + str(len(GABARITO)) +
      '\nvocê acertou ' + str(porcentagem) + '%')
