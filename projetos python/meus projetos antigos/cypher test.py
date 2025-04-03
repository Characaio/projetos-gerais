my_alphabet = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
               ' ', ' ', ' ', ' ']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
a=0
b=1
c=2
d=3
e=4
f=5
z=26
change = ''
valid_nums = ['0','1','2','3','4','5','6','7','8','9']
while change not in valid_nums:
    change = input(str('what chyper key you want to use? '))

def get_index(change, i):
    index = i-int(change)
    return index
def cypher_the_alphabet(change):
    for i in range(len(alphabet)):
        index = get_index(change, i)
        #print(str(index) + ' ' + str(i) + 'is the index')  
        if index > len(alphabet) or index == len(alphabet):
            repeat = index - len(alphabet)
            my_alphabet[i] = alphabet[repeat]
        elif index < len(alphabet):
            my_alphabet[i] = alphabet[index]
    print('the alphabet is' + str(my_alphabet))
    return my_alphabet

print('the alphabet is' + str(alphabet))
cypher_the_alphabet(change)
for i in range(len(alphabet)):
    index = get_index(change,i)
    print('decypher my alphabet')
    change_my_alphabet = input(str('whos is equals to who?'))
    if my_alphabet[i] == alphabet[int(change_my_alphabet)]:
        my_alphabet[i], alphbet[int(change_my_alphabet)] = my_alphabet[int(change_my_alphabet)], my_alphabet[i]
     
    #if change_my_alphabet == my_alphabet[i]:
        #print('you are right')
        #if index > len(alphabet) or index == len(alphabet):
            #index = index - len(alphabet)
            #pass
        #elif index < len(alphabet):
            #pass
        #my_alphabet[i], my_alphabet[index] = my_alphabet[index], my_alphabet[i]
#print('my cyphered alphabet is' + str(cypher_the_alphabet(int(change))))
