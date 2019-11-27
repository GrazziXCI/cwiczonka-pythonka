'''Napisz program, który wczytuje liczbę całkowitą,
a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`'''

s = int(input('Ile stopni powinna mieć choinka? '))

x = s - 1
y = 1

for i in range(s):
    print(' ' * x + '*' * y + ' ' * x)
    x -= 1
    y += 2