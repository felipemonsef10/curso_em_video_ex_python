import moeda

p = float(input('Digite um valor: R$'))
print(f'A medade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Diminuindo 20%, temos R${moeda.diminuir(p, 20)}')
