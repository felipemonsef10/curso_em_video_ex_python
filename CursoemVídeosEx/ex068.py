from random import randint
s = 0
while True:
    sort = randint(0, 10)
    jogador = str(input('Par ou ímpar(P/I)? ')).upper().strip()[0]
    if jogador == 'P':
        print('Eu quero ímpar!')
        n = int(input('Jogue um número: '))
        print(f'Joguei {sort}!')
        soma = sort + n
        if soma % 2 == 0:
            print('Você ganhou, play again!')
            s += 1
        else:
            break
    if jogador == 'I':
        print('Eu quero par!')
        n = int(input('Jogue um número: '))
        print(f'Joguei {sort}!')
        soma = sort + n
        if soma % 2 != 0:
            print('Você ganhou, play again!')
            s += 1
        else:
            break
if s == 0:
    print('EU ganhei. Você não ganhou nenhuma vez!')
else:
    print(f'Você ganhou {s} vezes seguida(s), mas eu ganhei dessa vez!!')
