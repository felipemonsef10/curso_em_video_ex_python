def linha(tam):
    print('=' * tam)


def leianome(msg):
    while True:
        try:
            nome = str(input(msg)).strip().title()
        except KeyboardInterrupt:
            print('O usuário preferiu não informar o nome.')
        else:
            return nome


def leiaint(msg1, msg2=''):
    while True:
        try:
            num = int(input(msg1))
        except (ValueError, TypeError):
            print(f'ERRO! Digite uma {msg2} válida.')
            linha(35)
        else:
            return num
