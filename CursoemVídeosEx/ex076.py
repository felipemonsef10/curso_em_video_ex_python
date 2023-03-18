# Meu jeito
lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25.00,
         'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
c = 0
s = 0
s1 = 1
print('=' * 40)
print(f'{"TABELA DE PREÇOS:":^40}')
print('=' * 40)
while c < len(lista):
    print(f'{lista[s]:.<30} R$', f'{lista[s1]:>6.2f}')
    c += 2
    s += 2
    s1 += 2
print('')
print('')

# Jeito diferente
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
print('')
print('')

# Outro jeito
produtos = ("Lápis", 1.75, "Borracha", 2.00,
            "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)

for c in range(0, len(produtos), 2):
    print(f"{produtos[c]:.<40}", f" R$ {produtos[c+1]:>7.2f}")

print("="*50)
