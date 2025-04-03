

livros:int = 1
desconto:int = 0
preço:int = 25
repeat:bool = True

#desconto maximo = 25
#cada livro custa 25
#a cada 3 livros o desconto aumenta em 5%


# desconto de algo por 5% == preço do item * 95%
#achar o desconto do item por 5
#subtrair o desconto do item do preço



def calcular_desconto():
    global livros
    global desconto
    global preço
    global repeat
    if desconto < 25:
        if livros % 3 == 0: # se os livros forem{3,6,9,12,15,18,21....}
            desconto += 5
            print('aumentei o desconto em 5')
        print(f'o preço total é {livros*preço}')
        if desconto > 0:
            final = livros*preço*(desconto/100) #5% = 0,05, 25% = 0,25
        else:
            final = livros*preço
        preço_total = livros*preço
        descontado = preço_total-final
        livros += 1
        return descontado
    else:
        repeat = False
        return 

while repeat:
    print(f'{calcular_desconto()} isso é o preço total pos desconto')
    


