reais = 'R$'


def moeda(n):
    return reais + str(f'{n:.2f}')


def metade(n, format=True):
    if format:
        return reais + f'{n / 2:.2f}'
    elif not format:
        return reais + str(n / 2)


def dobro(n, format=True):
    if format:
        return reais + f'{n * 2:.2f}'
    elif not format:
        return reais + str(n * 2)


def aumento(n, a=1, format=True):
    if format:
        return reais + f'{n * (1 + a / 100):.2f}'
    elif not format:
        return reais + str(n * (1 + a / 100))


def desconto(n, a=1, format=True):
    if format:
        return reais + f'{n * (1 - a / 100):.2f}'
    elif not format:
        return reais + str(n * (1 - a / 100))
