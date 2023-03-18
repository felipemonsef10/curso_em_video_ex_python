frase = str(input('Digite uma frase: ')).split()
jun = ''.join(frase).upper()
qtd_letr = len(jun)
inverso = ''
for letra in range(qtd_letr - 1, -1, -1):
    inverso += jun[letra]
if jun == inverso:
    print('{} é um palindromo, e seu inverso é: {}'.format(jun, inverso))
elif jun != inverso:
    print('{} não é um palindromo, e seu inverso é: {}'.format(jun, inverso))
