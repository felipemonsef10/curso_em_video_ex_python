from ex109MEU import moeda

num = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, False)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'Aumentando 15% em {moeda.moeda(num)}, temos {moeda.aumento(num, True)}')
print(f'Reduzindo 10% em{moeda.moeda(num)}, temos {moeda.desconto(num, True)}')
