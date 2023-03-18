print('Velocidade permitida na via: 80Km/h')
vel = float(input('Velocidade do carro(Km/h): '))
if vel<= 80:
    print('Você estava dentro da velocidade permitida e não receberá multa.')
else:
    print('Você foi multado em R${:.2f}!'.format((vel - 80) * 7))