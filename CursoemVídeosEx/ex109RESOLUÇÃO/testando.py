from ex109RESOLUÇÃO import moeda

p = float(input('Digite um valor: R$'))
print(f'A medade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 20%, temos {moeda.diminuir(p, 20, True)}')
