'''Program losuje liczbę z zakresu od 0 do 999.
Użytkownik ma zgadnąć tę liczbę nie widząc jej.
Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc
czy podana liczba była za duża, czy za mała. Gdy użytkownik poda właściwą liczbę,
program wypisuje gratulacje jednocześnie informując, w której próbie udało się zgadnąć liczbę.'''

from random import randint

x = randint(1, 1000)
i = 0

while True:
    y = int(input('Zgadnij liczbę z zakresu 1-999: '))
    i += 1
    if y == x:
        break
    else:
        if y < x:
            print('Pudło! Za mało!')
        if y > x:
            print('Pudło! Za dużo!')

print(f'Bingo! Twoja liczba to {x}!\nUdało Ci się zgadnąć w {i} próbach!')


