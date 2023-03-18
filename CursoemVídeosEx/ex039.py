ano = int(input('Em quem ano você nasceu? '))
atual = 2022
ano1 = 2005
ano2 = 2003
temp1 = (2022 - ano) - 18
temp2 = 18 - (2022 - ano)
if ano == 2004:
    print('Esse ano você deve se apresentar ao exército para se alistar!!')
elif ano == 2003:
    print('Já se passou 1 ano do prazo de seu alistamento ao exército!')
elif ano < 2004:
    print('Já se passaram {} anos do prazo para você se alistar ao exército!'.format(temp1))
elif ano == 2005:
    print('Falta apenas 1 ano para o seu alistamento ao serviço militar!')
else:
    print('Faltam {} anos para o seu alistamento ao serviço militar!'.format(temp2))
