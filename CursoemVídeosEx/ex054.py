n = 0
f = 0
for c in range(7):
    ano = int(input('Ano de nascimento: '))
    if ano > 2004:
        n += 1
    elif ano <= 2004:
        f += 1
print('{} pessoa(a) não é/são maior(es) de idade.'.format(n))
print('{} pessoa(a) já é/são maior(es) de idade.'.format(n))
