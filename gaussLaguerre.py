import numpy as np
import math
import json

def wielomianAproksymujacy(x, wspolczynniki):
    # funkcja obliczajaca wartosc wielomianu aproksymujacego w punkcie x
    wynik = 0
    for n in range(len(wspolczynniki)):
        wynik += wspolczynniki[n] * wielomianLaguerra(n, x)
    return wynik


def wielomianLaguerra(n, x):
    # funkcja do obliczania wartosci wielomianu laguerre'a dla danego stopnia
    if n == 0:
        return 1
    elif n == 1:
        return 1 - x
    else:
        l0, l1 = 1, 1 - x
        for i in range(1, n):
            l0, l1 = l1, ((2 * i + 1 - x) * l1 - i * l0) / (i + 1)
        return l1


def gaussLaguerre(f, iloscWezlow):
    # przyblizenie calki e^(–x) * f(x) metoda Gaussa - Laguerre'a
    # wczytaj plik JSON z wprowadzonymi wezlami i odpowiadajacymi im wagami
    with open("wezly_wagi.json", "r") as file:
        data = json.load(file)

    if str(iloscWezlow) not in data:
        print("Liczba węzłów musi wynosić 2, 3, 4 lub 5")
        return None

    wezly = data[str(iloscWezlow)]["wezly"]
    wagiWezlow = data[str(iloscWezlow)]["wagiWezlow"]

    # obliczenie przyblizenia calki metoda Gaussa – Laguerre'a
    wynik = 0.0
    for i in range(iloscWezlow):
        wynik += wagiWezlow[i] * f(wezly[i])
    return wynik


# oblicz wspolczynniki wielomianow laguerre'a dla danej funkcji
def obliczWspolczynniki(funkcja, stopien, iloscWezlow):
    wspolczynniki = []

    for n in range(stopien + 1):
        # definiujemy funkcje do scalkowania
        # dla metody gaussa-laguerre'a funkcja zawiera juz wage exp(-x)
        def funkcjaDoScalkowania(x):
            return funkcja(x) * wielomianLaguerra(n, x)

        # obliczamy calke metoda gaussa-laguerre'a
        wynik = gaussLaguerre(funkcjaDoScalkowania, iloscWezlow)
        wspolczynniki.append(wynik)

    return wspolczynniki

def obliczBlad(funkcja, wspolczynniki, a, b, iloscPunktow=100):
    # blad liczymy na podstawie punktow
    # zapisz "sciezke" 100 punktow na x
    x = np.linspace(a, b, iloscPunktow)
    blad = 0

    # blad jest slabo liczony i zle wypada w funkcjach wielomian/zlozona
    for punkt in x:
        wartoscFunkcji = funkcja(punkt)
        wartoscAproksymacji = wielomianAproksymujacy(punkt, wspolczynniki)
        blad += abs(wartoscFunkcji - wartoscAproksymacji)

    return math.sqrt(blad / iloscPunktow)
