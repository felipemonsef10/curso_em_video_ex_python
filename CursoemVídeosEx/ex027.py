nome = str(input('Digite o seu nome: ')).strip()
n = nome.split()
print('O seu primeiro nome é: {}'.format(nome.split()[0]))
print('O seu último nome é: {}'.format(n[len(n) - 1]))