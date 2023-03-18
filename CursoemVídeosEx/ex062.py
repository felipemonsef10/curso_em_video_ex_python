print('=-' * 8)
print('Termos de uma PA'.upper())
print('=-' * 8)
a1 = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
c = 0
s = 0
print('Os 10 primeiros termos dessa PA são: ')
while c < 10:
    c += 1
    num = a1 + raz
    a1 = num
    print(a1 - raz, end=' ')
pergunta = int(input('\nVer mais quantos termos: '))
c = pergunta + pergunta
c1 = pergunta
while pergunta > 0:
    while c1 < c:
        c1 += 1
        a1 += raz
        print(a1 - raz, end=' ')
    pergunta = int(input('\nVer mais quantos termos: '))
    if pergunta != 0:
        c = pergunta + pergunta
        c1 = pergunta
        c1 += 1
        a1 += raz
        print(a1 - raz, end=' ')
    else:
        from time import sleep
        print('FINALIZANDO O PROGRAMA...')
        sleep(2)
        print('PROGRAMA FINALIZADO!')
