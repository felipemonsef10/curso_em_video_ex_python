c = 0
while True:
    sac = int(input('VALOR A SER SACADO: R$ '))
    not50 = sac // 50
    not20 = sac % 50 // 20
    not10 = sac % 50 % 20 // 10
    not5 = sac % 50 % 20 % 10 // 5
    not1 = sac % 50 % 20 % 10 % 5 // 1
    c += 1
    if c == 1:
        break
notas = 'cédula(s)'
print(f'SACANDO...\n {not50} {notas} de R$50\n {not20} {notas} de R$20\n {not10} {notas} de R$10\n {not5} {notas} '
      f'de R$5\n {not1} moeda(s) de R$1')
