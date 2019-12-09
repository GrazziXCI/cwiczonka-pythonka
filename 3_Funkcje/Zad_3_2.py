'''Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
​Logikę obliczania liczby dni wydziel do osobnej funkcji.

​**Wersja A**

Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.

​**Wersja B (trudniejsza)**

Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie. '''


def rok_przestepny(rok:int) ->int:
    if rok % 4 == 0:
        wynik = 29
    else:
        wynik = 28
    return wynik

def liczba_dni(miesiac: str) -> int:
    if miesiac == 'styczeń' or 'marzec' or 'maj' or 'lipiec' or 'sierpień' or 'październik' or 'grudzień':
        wynik = 31
    else:
        wynik = 30
    return wynik

miesiac = input('Ktory miesiąc? ')


if miesiac == 'luty':
    rok = int(input('W którym roku? '))
    rok_przestepny(rok)
else:
    liczba_dni(miesiac)

print(f'Miesiąc {miesiac} ma dokładnie {wynik} dni.')


def test_liczba_dni():
    assert liczba_dni('styczeń') == 31
    assert liczba_dni('wrzesień') == 30

def test_roku():
    assert rok_przestepny(2012) == 29
    assert rok_przestepny(2010) == 28



