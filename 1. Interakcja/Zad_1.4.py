'''Potem napisz taki program: użytkownik podaje swój wiek
i ile nocy spędzi w hotelu, a program wylicza, ile trzeba zapłacić. Zasady są takie:

- nieletni (poniżej 18 roku życia) płacą 100 zł za noc
- dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
	- 200 zł za noc, jeśli nocują jedną noc
	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
	- 150 zł za noc, jeśli nocują pięć lub więcej nocy
    - emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki'''
from typing import Tuple, Union

wiek = int(input('Podaj swój wiek: '))
pobyt = float(input('Ile nocy spędzisz w hotelu: '))
doba = 0

if wiek < 18:
    doba = 100
elif wiek >= 18:
    if pobyt == 1:
        doba = 200
    if pobyt >= 2 and pobyt < 5:
        doba = 180
    if pobyt >= 5:
        doba = 150

if wiek > 65:
    rabat = doba * 0.1
    z_rabatem = doba - rabat
    cena = z_rabatem * pobyt
    print(f'Za pobyt w hotelu przez {pobyt:.0f} nocy osoby w wieku {wiek} lat \nnależy zapłacić {z_rabatem:.0f}zł za noc. \nKoszt całego pobytu wyniesie {cena:.2f}zł')
else:
    cena = doba * pobyt
    print(f'Za pobyt w hotelu przez {pobyt:.0f} nocy osoby w wieku {wiek} lat \nnależy zapłacić {doba:.0f}zł za noc. \nKoszt całego pobytu wyniesie {cena:.2f}zł')

