from ex107MEU import moeda

num = float(input('Digite um valor: R$'))
print(f'O dobro de {num} é {moeda.dobro(num)}.')
print(f'A metade de {num} é {moeda.metade(num)}.')
print(f'Aumentando em 10%, temos: {moeda.aumento(num, 10)}.')
print(f'Descontando em 15%, temos: {moeda.desconto(num, 15)}.')
