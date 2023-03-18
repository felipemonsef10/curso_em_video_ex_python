#IMC = 80 kg ÷ (1,80 m × 1,80 m) = 24,69 kg/m2 (Peso ideal)
from time import sleep
peso = float(input('Informe o seu peso (kg): '))
alt = float(input('Informe a sua altura (m): '))
imc = peso / (alt ** 2)
print('Calculando seu IMC...')
sleep(3)
print('Resultado: {:.1f}kg/m2'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 < imc < 25:
    print('O seu peso está ideal.')
elif 25 < imc < 30:
    print('Você está com sobrepeso.')
elif 30 < imc < 40:
    print('Você está com obesidade.')
elif imc > 40:
    print('Você está com obesidade mórbida.')
