'''Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
​Logikę obliczania liczby dni wydziel do osobnej funkcji.

​**Wersja A**

Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.

​**Wersja B (trudniejsza)**

Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie. '''


def rok_przestepny(rok:int) ->int:
    if rok % 4 == 0 and rok % 100 != 0:
        wynik = 29
    elif rok % 400 == 0:
        wynik = 29
    else:
        wynik = 28
    return wynik

def liczba_dni(miesiac: str) -> int:
    if miesiac == 'styczeń' or miesiac == 'marzec' or miesiac == 'maj' or miesiac == 'lipiec' or miesiac == 'sierpień' or miesiac == 'październik' or miesiac == 'grudzień':
        wynik = 31
    else:
        wynik = 30
    return wynik

def test_liczba_dni():
    assert liczba_dni('grudzień') == 31
    assert liczba_dni('czerwiec') == 30

def test_roku():
    assert rok_przestepny(2012) == 29
    assert rok_przestepny(2010) == 28
    assert rok_przestepny(2000) == 29



