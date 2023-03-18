from time import sleep
print('EMPRÉSTIMO BANCÁRIO.')
casa = float(input('Qual o valor da casa que deseja comprar?R$'))
sal = float(input('Qual o seu salário mensal?R$'))
anos = int(input('Em quantos anos deseja pagar? '))
prest = ((casa/anos)/12)
salf = 0.3 * sal
print('Calculando o valor da prestação...')
sleep(3)
if prest > salf:
    print('O seu empréstimo foi negado pois não segue os requisitos para tal empréstimo.')
else:
    print('O seu empréstimo foi aprovado, parabéns.')