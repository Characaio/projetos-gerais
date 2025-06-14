a = int(input('qual é o valor de a?'))
b = int(input('qual é o valor de b?'))
c = int(input('qual é o valor de c?'))


delta = b*b - 4*a*c

upper1 = -b + delta**.5
print(upper1)
divisor1 = 2*a
X1 = upper1/divisor1

upper2 = -b - delta**.5
print(upper2)
divisor2 = 2*a
X2 = upper2/divisor2

print('a primeira raiz é' + str(X1) + '\na segunda raiz é' + str(X2))
