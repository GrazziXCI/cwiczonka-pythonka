'''Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej).
Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej).
Użytkownik ma odgadnąć (no, policzyć w głowie) wynik. Program pyta o wynik wielokrotnie,
tak długo, aż użytkownik poda prawidłowy wynik.'''

import random

x = random.randint(1, 101)
y = random.randint(1, 101)

print(f'Wylosowane zostały liczby {x} oraz {y}.')

suma = x + y

while True:
    odp = int(input('Jaka jest suma tych liczb? '))
    if odp == suma:
        print(f'Gratulacje! Suma z {x} i {y} to {suma}! Masz ciasteczko!')
        break
    else:
        print('Niestety nie, spróbuj jeszcze raz!')
        print()

