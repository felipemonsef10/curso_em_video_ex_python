aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: ')).capitalize()
aluno['Média'] = float(input(f'Média do {aluno["Nome"]}: '))
print('-=' * 10)
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k}: {v}')
print('-=' * 10)
