from time import sleep
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('Analisando {} e {}...'.format(num1, num2))
sleep(2)
if num1 > num2:
    print('O primeiro número, {}, é maior do que o segundo, {}.'.format(num1, num2))
elif num2 > num1:
    print('O segundo número, {}, é maior do que o primeiro, {}.'.format(num2, num1))
else:
    print('O primeiro número, {}, e o segundo número, {}, são iguais!'.format(num1, num2))
