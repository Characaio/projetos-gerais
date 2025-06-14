dados = [2,5,7,4,2,7,1,23,1,5,4,78,5,3,67,43]
total = 0
quant = 1
for i in range(len(dados)):
    total = total + dados[i]
    print(str(total) + ' ' + str(i))
    
print(total/len(dados))
    
