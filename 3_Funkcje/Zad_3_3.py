'''Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
- `suma(liczby)` - zwraca sumę liczb z listy `liczby`
- `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
- `max(liczby)` – zwraca największą wartość z listy `liczby`
- `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
- `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
- `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
- `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
- `wypisz_podzielne(tab, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
- `pierwsza_podzielna(tab, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `ile_wiekszych(tab, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
- `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma'''

import pytest


def suma(liczby: list) -> int:
    suma = sum(liczby)
    return suma


def srednia(liczby: list) -> float:
    srednia = sum(liczby) / len(liczby)
    return round(srednia, 2)


def maxymalna(liczby: list) -> int:
    return max(liczby)


def roznica_min_max(liczby: list) -> int:
    if len(liczby) == 0:
        return 0
    else:
        roznica = max(liczby) - min(liczby)
        return roznica


def wieksze_od_x(liczby: list, x: int) -> list:
    wynik = []
    for i in liczby:
        if i > x:
            wynik.append(i)
    return wynik


def pierwsza_wieksza(liczby: list, x: int):
    for i in liczby:
        if i > x:
            return i
    return None

def suma_wiekszych(liczby: list, x: int) -> int:
    wynik = []
    for i in liczby:
        if i > x:
            wynik.append(i)
    return sum(wynik)

def ile_wiekszych(liczby: list, x: int) -> list:
    wynik = []
    for i in liczby:
        if i > x:
            wynik.append(i)
    return len(wynik)

def podzielne(liczby:list, x: int) -> list:
    wynik = []
    for i in liczby:
        if i % x == 0:
            wynik.append(i)
    return wynik

def pierwsza_podzielna(liczby:list, x: int) -> int:
    for i in liczby:
        if i % x == 0:
            return i
    return None

def element_wspolny(liczby1:list, liczby2:list) -> list:
    wynik = []
    for i in liczby1:
        if i in liczby2:
            wynik.append(i)
    if wynik == []:
        return None
    else:
        return wynik




# ==============================================================================

def test_sumatora():
    assert suma([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 45


def test_sredniej():
    assert srednia([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 4.5


def test_max():
    assert maxymalna([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == 9


def test_roznicy():
    assert roznica_min_max([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 8
    assert roznica_min_max([]) == 0


def test_wieksze():
    assert wieksze_od_x([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [4, 5, 6, 7, 8, 9]
    assert wieksze_od_x([1, 2, 3, 4, 5, 6, 7, 8, 9], 8) == [9]


def test_pierwsza_wieksza():
    assert pierwsza_wieksza([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == 4
    assert pierwsza_wieksza([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) is None

def test_suma_wiekszych():
    assert suma_wiekszych([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == 39
    assert suma_wiekszych([1, 2, 3, 4, 5, 6, 7, 8, 9], 7) == 17

def test_ile_wiekszych():
    assert ile_wiekszych([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == 6
    assert ile_wiekszych([1, 2, 3, 4, 5, 6, 7, 8, 9], 7) == 2
    assert ile_wiekszych([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 0

def test_podzielne():
    assert podzielne([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [3, 6, 9]
    assert podzielne([1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == [2,4,6,8]

def test_pierwsza_podzielna():
    assert pierwsza_podzielna([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == 3
    assert pierwsza_podzielna([1, 2, 3, 4, 5, 6, 7, 8, 9], 14) is None

def test_wspolna():
    assert element_wspolny([1,2,3,4,5], [5,6,7,8,9]) == [5]
    assert element_wspolny([1,2,3,4,5,6,7], [5,6,7,8,9]) == [5,6,7]
    assert element_wspolny([1,3,5,7,9], [2,4,6,8]) is None