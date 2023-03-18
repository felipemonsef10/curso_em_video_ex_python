s = 0
q = 0
media = 0
nome = ''
id_m = 0
id_f = 0
for c in range(1, 5):
    nomes = str(input('Nome pessoa {}: '.format(c))).strip()
    idade = int(input('Idade pessoa {}: '.format(c)))
    sexo = str(input('Sexo pessoa {}: '.format(c)).upper()).strip()
    s += idade
    media = s / 4
    if sexo == 'MASCULINO':
        if c == 1:
            id_m = idade
            nome = nomes
        else:
            if idade > id_m:
                id_m = idade
                nome = nomes
    if sexo == 'FEMININO':
        if idade < 20:
            id_f += 1
print('A quantidade de mulheres com menos de 20 anos é {}.'.format(id_f))
print('O nome do homem mais velho é {}, com {} anos.'.format(nome, id_m))
print('A média de idade do grupo é {:.0f} anos.'.format(media))
