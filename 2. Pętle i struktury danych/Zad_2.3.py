'''Napisz program, który odczytuje od użytkownika wiele liczb.

Program powinien wyliczyć i na końcu wypisać następujące statystyki:

- liczba podanych liczb (ile sztuk),
- suma,
- średnia,
- minimum
- maksimum'''

list = []

while True:
    a = input('Podaj liczbę lub wpisz \'koniec\': ')
    if a == 'koniec':
        break
    else:
        list.append(int(a))

print(f'Podałeś następujące liczby: {list}')
print(f'Ilość liczb w zbiorze: {len(list)}')
print(f'Suma liczb w zbiorze: {sum(list)}')
print(f'Najmniejsza liczba w zbiorze: {min(list)}')
print(f'Największa liczba w zbiorze: {max(list)}')


