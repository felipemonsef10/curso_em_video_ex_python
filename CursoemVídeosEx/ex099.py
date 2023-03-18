from time import sleep


def larger(* num):
    print('-=' * 30)
    size = len(num)
    if len(num) == 0:
        print('Não foi informado nenhum número.')
    elif len(num) > 0:
        big = num[0]
        for n in num:
            if n > big:
                big = n
        print(f'Foram informados {size} números,', end=' ')
        for c in num:
            print(f'[{c}]', end='')
            sleep(0.4)
        print('.')
        print(f'O maior número é o {big}.')


larger(2, 9, 4, 5, 7, 1)
larger(4, 7, 0)
larger(1, 2)
larger(6)
larger()
