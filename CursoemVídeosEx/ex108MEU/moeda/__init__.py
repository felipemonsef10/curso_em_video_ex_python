reais = 'R$'


def moeda(n):
    return reais + str(n)


def metade(n):
    return f'{n / 2:.2f}'


def dobro(n):
    return f'{n * 2:.2f}'


def aumento(n, a=1):
    return f'{n * (1 + a / 100):.2f}'


def desconto(n, a=1):
    return f'{n * (1 - a / 100):.2f}'
