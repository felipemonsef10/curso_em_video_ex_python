print('=' * 21)
print('FAÇA O CADASTRO AQUI!')
print('=' * 21)
pessoas = 0
homem = 0
mulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = ''
    continuar = ''
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexualidade[M/F]: ')).upper().strip()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja cadastrar mais uma pessoa? ')).upper().strip()[0]
    if idade > 18:
        pessoas += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if continuar == 'N':
        break
print('=' * 34)
print(f'{pessoas} pessoa(s) possue(m) mais de 18 anos.')
print(f'{homem} homem(s) foi/foram cadastrado(s). ')
print(f'{mulher} mulher(es) possui/possui menos de 20 anos.')
print('=' * 34)
