# MEU JEITO
def valor(x):
    numbers = '1234567890'
    while True:
        cont = 0
        n = input(x).strip()
        for c in range(len(n)):
            if n[c] in numbers:
                cont += 1
        if cont == len(n) and cont != 0:
            break
        else:
            print('\033[1;31mERRO! DIGITE UM VALOR NUMÉRICO INTEIRO.\033[m')
    return n


num = valor('Digite um valor inteiro: ')
print(f'O valor digitado foi {num}.')
print('_' * 30)


# OUTRO JEITO
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! DIGITE UM VALOR NUMÉRICO VÁLIDO.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
