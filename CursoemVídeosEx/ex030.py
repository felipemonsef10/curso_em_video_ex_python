num = int(input('Digite um número: '))
rest = num % 2
if rest == 1:
    print('O número {} é IMPAR'.format(num))
else:
    print('O número {} é PAR'.format(num))