import math

def obliczWielomianHornerem(x, wspolczynniki):
    wynik = wspolczynniki[0]
    for wspolczynnik in wspolczynniki[1:]:
        wynik = wynik * x + wspolczynnik
    return wynik

def funkcjaLiniowa(x):
    # 2x - 3
    return 2 * x - 3

def funkcjaModul(x):
    # |x|
    return abs(x)

def funkcjaWielomianowa(x):
    # -2x^3 + 4x^2 + 5
    wspolczynniki = [-2, 4, 0, 5]
    return obliczWielomianHornerem(x, wspolczynniki)

def funkcjaTrygonometryczna(x):
    # sin(x) - 0.5
    return math.sin(x) - 0.5

def funkcjaZlozona(x):
    # exp(sin(x)) - 2
    return math.e**(math.sin(x)) - 2