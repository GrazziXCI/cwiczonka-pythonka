'''Zakładamy, że 1 ludzki rok, to 5 lat psich.

Za pomocą konsoli wczytaj imię i wiek psa.

Wypisz komunikat ile pies miałby lat gdyby był człowiekiem. '''
#pozwoliłem sobie przyjąć 7lat psich na 1 ludzki

imie = input('Jak wabi sie pies? ')
wiek_psi = int(input('Ile lat ma pies? '))

wiek_ludzki = wiek_psi * 7

print(f'Gyby {imie} był/a człowiekiem, miałby teraz {wiek_ludzki} lat')

