'''Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą
stanowić boki trójkąta (np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?),
a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach'''

import math

a = int(input('Podaj długość pierwszego boku: '))
b = int(input('Podaj długość drugiego boku: '))
c = int(input('Podaj długość trzciego boku: '))

p = (a+b+c) / 2

if a+b > c and a+c > b and c+b > a:
    pole = math.sqrt(p * (p-a) * (p-b) * (p-c))
    print(f'Podany trójkąt ma powierzchnie {pole}')
else:
    print('Podane długości boków nie stworzą trójkąta. Podaje inne wartości')