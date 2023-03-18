def leiaint(msg='Digite um valor: '):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: O VALOR DIGITADO  NÃO É UM NÚMERO INTEIRO.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não digitar esse número.\033[m')
            n = 0
            return n
        else:
            return num
