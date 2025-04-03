import random as rand

unsorted_list1 = [1,6, 234, 12,8, 1, 23, 198, 46, 1, 3, 9, 5, 3]
unsorted_list = [ 6, 5, 10, 6, 9, 5 ,7, 5 , 10]
def bubblesort(lista):
    for i in range(len(lista)):
        #print(i)
        for j in range(0, len(lista) - i - 1):
            #print(j)
            #print('dayum, nice index brotha')
            if lista[j] > lista[j+1]:
                   #print('nice swap brotha')
                   lista[j], lista[j+1] = lista[j+1], lista[j]
                   #print(lista)
    return lista

rand.shuffle(unsorted_list)

print(bubblesort(unsorted_list))
