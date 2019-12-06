'''Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
2. `max` - zwraca większą z dwóch liczb,
3. `srednia` - oblicza średnią z dwóch liczb,
4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
podpowiedź: wartość PI jest dostępna jako `Math.PI`
5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry'''

import pytest
import math

def ft_to_m(stopy: float) -> float:
    """
    Funkcja przelicza odległośc podaną w stopach (ft) na odległośc w metrach (m)
    :param stopy:
    :return:
    """
    metr = stopy * 0.3048
    return metr

def max(a:int, b:int) -> int:
    """
    Podaje większą z podanych liczb
    :param a:
    :param b:
    :return:
    """
    if a > b:
        wynik = a
    else:
        wynik = b
    return wynik

def srednia(a:int, b:int) -> float:
    wynik = (a+b) / 2
    return wynik

def pole_kola(r:float):
    """
    Funkcja licząca pole koła na podstawie długości promienia
    :param a:
    :return:
    """
    pole = math.pi * r ** 2
    return round(pole, 2)

def bmi(waga:int, wzrost:float) ->float:
    """
    Funkcja licząca BMI dla konkretnej wagi i wzrostu
    :param waga:
    :param wzrost:
    :return:
    """
    BMI = waga / wzrost**2
    return round(BMI, 2)

def pole_trojkata(a:int, b:int, c:int) -> int:
    """
    Funkcja obliczająca pole trójkąta
    :param a:
    :param b:
    :param c:
    :return:
    """
    if a+b > c and a+c > b and b+c > a:
        p = (a+b+c)/2
        wynik = math.sqrt(p * (p-a)*(p-b)*(p-c))
        return wynik
    else:
        raise ValueError('Podane boki nie stworzą trójkąta!')

def km_na_mile(km:float) -> float:
    """
    Funkcja przelicza kilometry na mile
    :param km:
    :return:
    """
    mile = km * 0.62137
    return round(mile, 2)

def mi_na_km(mi:float) -> float:
    """
    Funkcja przelicza mile na kilometry
    :param mi:
    :return:
    """
    km = mi / 0.62137
    return round(km, 2)

#=================================================================

def test_stopy_na_metry():
    assert ft_to_m(4) == 1.2192
    assert ft_to_m(10) == 3.048

def test_max():
    assert max(4, 10) == 10
    assert max(7, 20) == 20

def test_srednia():
    assert srednia(2,4) == 3
    assert srednia(5, 10) == 7.5

def test_pole_kola():
    assert pole_kola(5) == 78.54
    assert pole_kola(4) == 50.27

def test_bmi():
    assert bmi(110, 1.89) == 30.79

def test_pola_trojkata():
    assert pole_trojkata(3,4,5) == 6
    with pytest.raises(ValueError):
        pole_trojkata(2,2,5)

def test_km_na_mile():
    assert km_na_mile(1) == 0.62
    assert km_na_mile(5) == 3.11

def test_mi_na_km():
    assert mi_na_km(1) == 1.61
    assert mi_na_km(10) == 16.09
