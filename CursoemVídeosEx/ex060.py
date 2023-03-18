#UTILIZANDO WHILE
n = int(input())
c = n
f = 1
print('{}! = '.format(n))
while c > 0:
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))

#UTILIZANDO FOR IN
n = int(input())
f = 1
for c in range(n, 0, -1):
    f *= c
print(f)
