reais = 'R$'
values = {}


def moeda(n):
    return reais + str(f'{n:.2f}')


def dobro(n):
    values['dobro'] = f'{n * 2:.2f}'
    return reais + str(f'{n * 2:.2f}')


def metade(n):
    values['metade'] = f'{n / 2:.2f}'
    return reais + str(f'{n / 2:.2f}')


def aumento(n, a=100):
    values['aumento'] = f'{n * (1 + (a / 100)):.2f}'
    return reais + str(f'{n * (1 + (a / 100)):.2f}')


def desconto(n, d=100):
    values['desconto'] = f'{n * (1 - (d / 100)):.2f}'
    return reais + str(f'{n * (1 - (d / 100)):.2f}')


def resumo(a, b=100, c=100):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^36}')
    print('-' * 40)
    dobro(a)
    metade(a)
    aumento(a, b)
    desconto(a, c)
    print(f'{"Valor analisado:":<33}{moeda(a)}')
    print(f'{"Dobro do valor:":<33}{dobro(a)}')
    print(f'{"Metade do valor:":<33}{metade(a)}')
    print(f'{b}%{" de aumento:":<30}{aumento(a, b)}')
    print(f'{b}%{" de desconto:":<30}{desconto(a, c)}')
    print('-' * 40)
