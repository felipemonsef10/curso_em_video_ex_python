n = int(input('Digite um valor: '))
s_n = 'S'
s = 0
s += n
c = 1
maior = n
menor = n
while s_n == 'S':
    c += 1
    n = int(input('Digite outro valor: '))
    s_n = str(input('Quer continuar(S/N)? ')).upper().strip()[0]
    s += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
media = s / c
print('A média entre esses valores é {:.2f}, o maior é {} e o menor {}.'.format(media, maior, menor))
