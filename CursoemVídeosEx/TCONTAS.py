n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))

s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
i = n1 // n2
r = n1 % n2
print('A soma é {}, a subtração é {}, o produto é {}, a divisão é {}'.format(s, su, m, d))
print('A divisão inteira é {}, e o resto é {}'.format(i, r))
print()
print()

# FORMATAÇÃO
print(f'{"OI":-^30}') # ALINHA AO CENTRO
print(f'{"OI":-<30}') # ALINHA À ESQUERDA
print(f'{"OI":->30}') # ALINHA À DIREITA
