preç = float(input('Qual o preço total do(S) produto(s)? R$'))
print ('Formas de pagamento disponíveis: ')
print('OPÇÃO [1] DINHEIRO/CHEQUE')
print('OPÇÃO [2] CARTÃO DÉBITO')
print('OPÇÃO [3] 2x NO CARTÃO DE CRÉDITO')
print('OPÇÃO [4] 3x OU MAIS NO CARTÃO DE CRÉDITO')
pag = int(input('Qual opção de pagamento deseja? '))
if pag == 1:
    desc = preç * 0.9
    print('Você obteve um desconto de 10%, Preço final: R${:.2f}.'.format(desc))
elif pag == 2:
    desc = preç * 0.95
    print('Você obteve um desconto de 5%. Preço final: R${:.2f}.'.format(desc))
elif pag == 3:
    preç2 = preç / 2
    print('Você não obteve desconto. Preço final: 2x de R${:.2f}.'.format(preç2))
elif pag == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = preç * 1.2
    mes = juros / parcelas
    print('Você deverá pagar um juros de 20% ao mês. Preço final: {}x de R${:.2f}'.format(parcelas, mes))

preç = float(input('Qual o preço do(s) produto(s)? R$ '))
print('Formas de pagamento disponíveis: ')
print('DINHEIRO/CHEQUE')
print('CARTÃO')
pag = str(input('Qual é a forma de pagamento? ').upper())
if pag == 'DINHEIRO' or pag == 'CHEQUE':
    desc = 0.9 * preç
    print('Você terá um desconto de 10% em cima de R${:.2f}. Sendo assim, a sua compra ficou em R${:.2f}'.format(preç, desc))
elif pag == 'CARTÃO' or pag == 'CARTAO':
    parcela = int(input('Em quantas vezes deseja parcelar? '))
    if parcela == 1:
        desc = 0.95 * preç
        print('Você receberá um desconto de 5% em cima de R${:.2f}. Sendo assim, a sua compra ficará em uma única parcela de R${:.2f}'.format(preç, desc))
    if parcela == 2:
        print('Você não receberá nenhum desconto. Sendo assim sua compra ficará em R${:.2f}'.format(preç))
    if 2 < parcela <= 10:
        juros = 1.2 * preç
        parcelas = juros / parcela
        print('Parcelando em {} vezes será cobrado um juros de 20% sobre R${:.2f}.\nSendo assim, sua compra ficará em {} parcelas de R${:.2f}. \nTotalizando R${:.2f}'.format(parcela, preç, parcela, parcelas, juros))