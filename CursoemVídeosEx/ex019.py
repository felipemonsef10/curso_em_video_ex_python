import random
a1 = str(input('Nome do aluno 1: '))
a2 = str(input('Nome do aluno 2: '))
a3 = str(input('Nome do aluno 3: '))
a4 = str(input('Nome do aluno 4: '))
srtds = [a1, a2, a3, a4]
a = random.choice(srtds)
print('O aluno sorteado foi o(a) {}'.format(a))


from random import choice
a1 = str(input('Nome do aluno 1: '))
a2 = str(input('Nome do aluno 2: '))
a3 = str(input('Nome do aluno 3: '))
a4 = str(input('Nome do aluno 4: '))
srtds = [a1, a2, a3, a4]
a = choice(srtds)
print('O aluno sorteado foi o(a) {}'.format(a))