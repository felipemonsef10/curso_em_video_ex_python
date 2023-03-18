numeros = 'zero', 'um', 'dois', 'três', \
          'quatro', 'cinco', 'seis', 'sete', \
          'oito', 'nove', 'dez', 'onze', 'doze', \
          'treze', 'quatorze', 'quinze', 'dezesseis', \
          'dezessete', 'dezoito', 'dezenove', 'vinte'

# Jeito 1
while True:
    while True:
        n = int(input('Digite um número de 0 a 20: '))
        if 0 <= n <= 20:
            break
        print('Valor inválido. ', end='')
    print(f'O número {n} escrito por extenso é {numeros[n]}.')
    continuar = str(input('Deseja continuar o programa(S/N)? ')).upper().strip()[0]
    if continuar == 'N':
        break

print(''
      ''
      ''
      ''
      '')

# Jeito 2
num = int(input('Digite um número entre 0 e 20: '))
while True:
    while 20 < num or num < 0:
        num = int(input('Valor não aceito. Digite um número entre 0 e 20: '))
    print(f'O número {num} escrito por extenso é {numeros[num]}.')
    continuar = str(input('Deseja continuar(S/N)? ')).strip()[0].upper()
    if continuar == 'N':
        break
    num = int(input('Digite um número entre 0 e 20: '))
