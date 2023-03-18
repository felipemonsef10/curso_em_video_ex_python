sal = float(input('Digite o valor do seu salário para calcular o aumento: R$'))
if sal>1250:
    nov = sal * 1.1
    print('Você receberá um aumento de 10% em cima de R${}, sendo assim, o seu salário foi reajustado para R${:.2f}'.format(sal, nov))
else:
    nov = sal * 1.15
    print('Você receberá um aumento de 15% em cima de R${}, sendo assim, o seu salário foi reajustado para R${:.2f}'.format(sal, nov))