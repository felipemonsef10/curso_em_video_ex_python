ano = int(input('Ano de nascimento do atleta: '))
id = 2022 - ano
if id <= 9:
    print('Categoria do atleta: MIRIM')
elif 9 < id <= 14:
    print('Categoria do atleta: INFANTIL')
elif 14 < id <= 19:
    print('Categoria do atleta: JUNIOR')
elif 19 < id <= 25:
    print('Categoria do atleta: SÊNIOR')
else:
    print('Categoria do atleta: MASTER')