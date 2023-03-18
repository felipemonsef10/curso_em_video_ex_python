# MEU JEITO
def factorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O valor cujo fatorial será calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O resultado de n!.
    """
    x = ' x '
    cont = 0
    result = 1
    for c in range(n, 0, -1):
        cont += 1
        result *= c
        if show:
            print(c, end='')
            if cont < n:
                print(x, end='')
            else:
                print(' =', end=' ')
    return result


print('_' * 30)
print(factorial(5, True))
help(factorial)
print()


# OUTRO JEITO
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O npumero a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print('_' * 30)
print(fatorial(5, True))
