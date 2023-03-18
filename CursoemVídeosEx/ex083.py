# MEU JEITO
lista = str(input('Digite a expressão: ')).strip()
lista2 = []
s = 0
for posi, caracter in enumerate(lista):
    if caracter in '()':
        if caracter == '(':
            lista2.append('(')
        if caracter == ')' and '(' in lista2:
            lista2.remove('(')
            s += 1
        if caracter == ')':
            lista2.append(')')
if lista.count('(') == lista.count(')') and lista2.count(')') == s:
    print('Expressão correta!')
else:
    print('Expressão incorreta!')
print('-=' * 41)

# OUTRO JEITO
expr = str(input('Expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
