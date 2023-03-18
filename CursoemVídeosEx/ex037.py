num = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções abaixo:
[ 1 ] coverter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O número {} convertido em BINÁRIO é: {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido em OCTAL é: {}'.format(num, oct(num)[2:]))
else:
    print('O número {} convertido em HEXADECIMAL é: {}'.format(num, hex(num)[2:]))
