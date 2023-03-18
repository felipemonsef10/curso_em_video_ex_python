nome = str(input('Digite seu nome:')).strip()
print('O seu nome em letras minúsculas é {}'.format(nome.lower()))
print('O seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('O seu nome completo posssui {} letras'.format(len(nome) - nome.count(' ')))
sp = nome.split()
#print ('O seu primeiro nome possui {} letras'.format(nome.find(' ')))
print('{} é o seu primeiro nome e possui {} letras'.format(sp[0], len(sp[0])))

