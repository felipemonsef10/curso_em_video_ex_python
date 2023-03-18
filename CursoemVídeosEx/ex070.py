s = 0
c = 0
c2 = 0
menor = c3 = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    continuar = str(input('Deseja continuar(S/N)? ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar(S/N)? ')).upper().strip()[0]
    s += preco
    c2 += 1
    c3 += 1
    if preco > 1000:
        c += 1
    if c3 == 1 or preco < menor:
        menor = preco
        barato = produto
    if continuar == 'N':
        break
print(f'TOTAL GASTO: R${s:.2f}')
print(f'{c} PRODUTO/S CUSTA/M MAIS DE R$1000.00.')
print(f'O PRODUTO MAIS BARATO FOI A/O {barato}, custando R${menor:.2f}')
