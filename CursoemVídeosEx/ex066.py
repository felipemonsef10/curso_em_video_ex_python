s = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'{c} valores foram digitados e a soma entre eles é {s}')
