print( '-=-' * 10)
print('Analisando um triângulo...')
print('-=-' * 10)
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if a >= b + c or b >= a + c or c >= b + a:
    print('Esse triângulo não existe.')
elif a == b == c:
    print('O triângulo formado por esses segmentos é equilátero.')
elif a == b or b == c or a == c:
    print('O triângulo formado por esses segmentos é isósceles.')
else:
    print('O triângulo formado por esses segmentos é escaleno.')
#OR
a = float(input('Reta a: '))
b = float(input('Reta b: '))
c = float(input('Reta c: '))
if a < b + c and b < a + c and c < a + b:
    print('Esses segmentos PODEM formar um triângulo ', end='') #IMPORTANTE
    if a == b == c:                                             #IMPORTANTE
        print('EQUILÁTERO.')
    elif a != b != c != a:                                      #IMPORTANTE
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Esses segmentos NÃO podem formar um triângulo.')
