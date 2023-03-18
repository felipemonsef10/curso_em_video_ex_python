def aumentar(p=0, taxa=0, formato=False):
    res = p + (p * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(p=0, taxa=0, formato=False):
    res = p - (p * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(p=0, formato=False):
    res = p * 2
    return res if formato is False else moeda(res)


def metade(p=0, formato=False):
    res = p / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)
