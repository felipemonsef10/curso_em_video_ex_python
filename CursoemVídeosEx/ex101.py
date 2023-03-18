# MEU JEITO
def vote(year):
    from datetime import datetime
    today = datetime.now().year
    age = today - year
    if 18 <= age <= 70:
        print(f'Com {age} anos de idade, o voto é obrigatório.')
    elif age > 70 or age == 16 or age == 17:
        print(f'Com {age} anos de idade, o voto é facultativo.')
    else:
        print(f'Com {age} anos de idade, o voto não é permitido.')


print('-=' * 20)
vote(int(input('Ano de nascimento: ')))
print()


# OUTRO JEITO
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos : NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print('=' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
