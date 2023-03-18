co = float(input('Medida do cateto oposto:'))
ca = float(input('Medida do cateto adjacente:'))
hip1 = ((co ** 2) + (ca ** 2)) ** (1/2)
print('A hipotenusa desse triângulo retângulo é igual a {}'.format(hip1))


from math import pow, sqrt, hypot
co = float(input('Medida do cateto oposto:'))
ca = float(input('Medida do cateto adjacente:'))
hip1 = hypot(co, ca)
print('A hipotenusa desse triângulo retângulo é igual a {}'.format(hip1))


from math import pow, sqrt
co = float(input('Medida do cateto oposto:'))
ca = float(input('Medida do cateto adjacente:'))
hip1 = pow(co, 2) + pow(ca, 2)
hip2 = sqrt(hip1)
print('A hipotenusa desse triângulo retângulo é igual a {}'.format(hip2))
