todos = []
par = []
impar = []
for c in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        par.append(valor)
    if valor % 2 != 0:
        impar.append(valor)
todos.append(impar)
todos.append(par)
print(f'Os números ímpares digitados foram: {sorted(todos[0])}')
print(f'Os números pares digitados foram: {sorted(todos[1])}')
