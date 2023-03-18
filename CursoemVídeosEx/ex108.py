from ex108MEU import moeda

num = float(input('Digite um valor: R$'))
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}.')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}.')
print(f'Aumentando {moeda.moeda(num)} em 15%, temos {moeda.moeda(moeda.aumento(num, 15))}.')
print(f'Descontando {moeda.moeda(num)} em 18%, temos {moeda.moeda(moeda.desconto(num, 18))}.')
