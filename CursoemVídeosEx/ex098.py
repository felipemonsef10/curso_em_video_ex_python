from time import sleep


def contador1():
    for c in range(1, 10 + 1):
        print(c, end=' ')
        sleep(0.3)
    print('FIM!')


def contador2():
    for c in range(10, -1, -1):
        if c % 2 == 0:
            print(c, end=' ')
            sleep(0.3)
    print('FIM!')


def contador3():
    inicio = int(input('Início da contagem: '))
    fim = int(input('Fim da contagem: '))
    passo = int(input('Passo: '))
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo += 1
    if inicio < fim:
        for c in range(inicio, fim, passo):
            print(c, end=' ')
            sleep(0.3)
        print('FIM!')
    if inicio > fim:
        while inicio >= fim:
            print(inicio, end=' ')
            sleep(0.3)
            inicio -= passo
        print('FIM!')


contador1()
contador2()
contador3()
print()

# OUTRO JEITO


def contagem1(i, f, p):
    for cont1 in range(i, f + 1, p):
        print(cont1, end=' ')
        sleep(0.3)
    print('END')


def contagem2(i, f, p):
    for cont2 in range(i, f, -1):
        if cont2 % p == 0:
            print(cont2, end=' ')
            sleep(0.3)
    print('END')


def contagem3(i, f, p):
    if p < 0:
        p *= - 1
    if i < f:
        for cont3 in range(i, f, p):
            print(cont3, end=' ')
            sleep(0.3)
    if i > f:
        while i >= f:
            print(i, end=' ')
            i -= p
            sleep(0.3)
    print('END')


contagem1(1, 10, 1)
contagem2(10, 0 - 1, 2)
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contagem3(a, b, c)
