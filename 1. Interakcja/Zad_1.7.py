'''Przy pomocy `input()` zapytaj użytkownika co chce kupić, jaką ilość towaru
chce kupić i jaka jest jego cena. Wyświetl odpowiedni komunikat. '''

towar = input('Jaki towar chciałbys kupić? ')
ilosc = float(input('Jaką ilość chciałbyś kupić? '))
cena = float(input('Jaka jest cena towaru za szt/kg? '))

kwota = ilosc * cena

print(f'Za {towar}, które chcesz kupić, łącznie zapłacisz {kwota:.2f}zł.')