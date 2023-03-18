palavras = ('pao', 'arroz', 'beleza', 'ok', 'joao', 'corno', 'felipe')
for palavra in palavras:
    print(f'\nAs vogais presentes na palavra "{palavra.upper()}" são:', end=' ')
    for vogal in palavra.strip():
        if vogal in 'aeiou':
            print(f'{vogal}', end=' ')
