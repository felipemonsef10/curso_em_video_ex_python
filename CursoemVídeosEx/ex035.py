from time import sleep
print('-=-' * 17)
print('\033[1;34mVerificador de condição  existêncial de triângulos\033[m')
print('-=-' * 17)
a = float(input('\033[4;33mComprimento da reta 1:\033[m '))
b = float(input('\033[4;36mComprimento da reta 2:\033[m '))
c = float(input('\033[4;35mComprimento da reta 3:\033[m '))
print('Analisando às retas...')
sleep(2)
if a<b + c and b<a + c and c<b + a:
    print('\033[4;34mEsse triângulo existe!\033[m')
else:
    print('\033[4;31mNão é possível formar um triângulo a partir dessas retas!\033[m')