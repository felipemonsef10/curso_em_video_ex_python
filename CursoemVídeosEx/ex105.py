# MEU JEITO
def escola(*num, sit=False):
    """
    ->Analisa notas e a situação de vários alunos.
    :param num: Notas de alunos capitadas e analisadas pelo sistema.
    :param sit: (Opicional) Indica se vai ou não mostrar a situação dos alunos de acordo com a média das notas.
    :return: Dicionário com informações sobre as notas.
    """
    notas = {}
    cont = 0
    maior = menor = 0
    soma = 0
    for n in num:
        cont += 1
        soma += n
        if cont == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
    media = soma / cont
    notas['Tot'] = cont
    notas['Maior'] = maior
    notas['Menor'] = menor
    notas['Media'] = f'{media:.2f}'
    if sit:
        if media < 6:
            notas['Situação'] = 'RUIM'
        if 6 < media < 7:
            notas['Situação'] = 'RAZOAVEL'
        if media > 7:
            notas['Situação'] = 'BOA'
    return notas


resp = escola(3.5, 10, 6.5, sit=False)
print(resp)
# help(escola)
print()


# OUTRO JEITO
def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] > 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
