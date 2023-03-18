file = 'teste.txt'





a = open(file, 'rt')
for linha in a:
    dado = linha.split(';')
    dado[1] = dado[1].replace('\n', '')
    print(dado[0], dado[1])
