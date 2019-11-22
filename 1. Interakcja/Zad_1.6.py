'''Założenia:
	- 0-6   - wiek przedszkolny - cena biletu: 0
	- 7-17  - wiek szkolny      - cena biletu: 2.28
	- 18-64 - wiek dorosły      - cena biletu: 3.80
	- +65   - wiek emerytalny   - cena biletu: 1.90

Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.
Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić. Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli. '''

przedszkolny = 0
szkolny = 0
dorosly = 0
emerytalny = 0
x = True

while x == True:
    kategoria = input('''Z której kategorii chciałby Pan/Pani bilety?
    1-przedszkolny 0-6
    2-szkolny 7-17
    3-dorosły 18-64
    4-emerytalny +65: ''')
    if kategoria == '1':
        ile = int(input('Ile sztuk biletów? '))
        przedszkolny += ile
    elif kategoria == '2':
        ile = int(input('Ile sztuk biletów? '))
        szkolny += ile
    elif kategoria == '3':
        ile = int(input('Ile sztuk biletów? '))
        dorosly += ile
    elif kategoria == '4':
        ile = int(input('Ile sztuk biletów? '))
        emerytalny += ile
    dod = input('Czy chciałbyś dodatkowe bilety? T/N ')
    if dod == 'N':
        x = False

print()
cena = przedszkolny * 0 + szkolny * 2.28 + dorosly * 3.8 + emerytalny * 1.9
print(f'Za wszystkie zamówione bilety należy zapłacić {cena:.2f}zł')
