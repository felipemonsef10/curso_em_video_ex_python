def leiadin(n):
    while True:
        cont1 = 0
        cont2 = 0
        cont3 = 0
        numeros1 = ''
        numeros2 = ''
        ler = str(input(n)).strip()
        for c in ler:
            if c.isnumeric():
                if cont1 < 1:
                    numeros1 += c
            elif c in ',.':
                cont1 += 1
            else:
                cont3 += 1
            if cont1 > 0:
                if c.isnumeric():
                    numeros2 += c
                    cont2 += 1
        if ler.isnumeric():
            return float(ler)
        elif cont3 == 0 and cont1 == 1 or cont3 == 0 and cont2 == 1:
            if numeros1 == '':
                numeros1 = '0'
            if numeros2 == '':
                numeros2 = '0'
            ler = float(numeros1 + numeros2) / float('1' + (cont2 * '0'))
            return ler
        else:
            print(f'\033[1;31mERRO!\033[4m"{ler.upper()}\033[m\033[1;31m" NÃO É VALIDO. DIGITE UM VALOR VÁLIDO.\033[m')
