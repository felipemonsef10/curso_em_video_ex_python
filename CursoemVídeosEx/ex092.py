from time import sleep
from datetime import datetime
dados = dict()
for c in range(1):
    dados['Nome'] = str(input('Nome: ')).capitalize()
    dados['Idade'] = datetime.now().year - int(input(f'Ano de nascimento de {dados["Nome"]}: '))
    while True:
        ctps = int(input('Número da carteira trabalhista: '))
        if ctps == 0:
            dados['carteira trabalhista'] = ctps
            break
        if ctps > 0:
            dados['carteira trabalhista'] = ctps
            break
    if ctps > 0:
        dados['Aposentadoria'] = 35 - (datetime.now().year - int(input('Ano de contratação: '))) + dados['Idade']
        dados['Salário'] = float(input('Valor salarial: R$'))
print('=' * 30)
print(f'{"COSTATANDO DADOS:":^30}')
print('=' * 30)
sleep(2)
frases = ''
for k, v in dados.items():
    if k == 'Nome':
        frases = 'do cadastrado:'
        print(f'{k} {frases} {v}')
    if k == 'Idade':
        frases = 'do cadastrado:'
        print(f'{k} {frases} {v} anos')
    if k == 'carteira trabalhista' and v != 0:
        frases = 'Número da'
        print(f'{frases} {k}: {v}')
    if k == 'Salário' and v != 0:
        frases = f'Valor salarial:'
        print(f'{frases} R${v:.2f}')
if dados['carteira trabalhista'] != 0:
    print(f'{dados["Nome"]} se aposentará com {dados["Aposentadoria"]} anos.')
