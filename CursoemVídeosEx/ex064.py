n = 0
c = -1
s = -999
while n != 999:
    c += 1
    n = int(input('Digite um valor [999 to stop]: '))
    s += n
print('Foram digitados {} números e a soma entre eles é {}.'.format(c, s))
