qd = int(input('Quantidade de dias de aluguel do carro: '))
qkm = float(input('Quantidades de Km rodados: '))
prça = qd * 60
prçb = qkm * 0.15
pt = prça + prçb
print('O preço total a se pagar pelo aluguel do carro, levando em consideração os {} dias de aluguel e os {}Km rodados é de R${:.2f}'.format(qd, qkm, pt))
