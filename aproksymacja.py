import matplotlib.pyplot as plt
from gaussLaguerre import *

def wielomianem(funkcja, a, b):
    stopien = int(input("Podaj stopień wielomianu aproksymującego: "))
    # wezly dla metody calkowania gaussa-laguerre'a
    iloscWezlow = int(input("Ilość węzłów (2-5): "))
    wspolczynniki = obliczWspolczynniki(funkcja, stopien, iloscWezlow)
    blad = obliczBlad(funkcja, wspolczynniki, a, b)

    print(f"Współczynniki wielomianu aproksymacyjnego stopnia {stopien}:")
    for i, wspolczynnik in enumerate(wspolczynniki):
        print(f"a{i} = {wspolczynnik:.6f}")

    print(f"Błąd aproksymacji: {blad:.6f}")
    rysujWykresy(funkcja, wspolczynniki, a, b)

def iteracyjna(funkcja, a, b):
    oczekiwanyBlad = float(input("Podaj oczekiwany błąd aproksymacji: "))
    iloscWezlow = int(input("Ilość węzłów (2, 3, 4 lub 5): "))
    stopien = 1
    znalezionoStopien = False

    while stopien <= 20 and not znalezionoStopien:  # ograniczenie do stopnia 20
        # wezly dla metody calkowania gaussa-laguerre'a
        wspolczynniki = obliczWspolczynniki(funkcja, stopien, iloscWezlow)
        blad = obliczBlad(funkcja, wspolczynniki, a, b)

        print(f"Stopień wielomianu: {stopien}\nBłąd aproksymacji: {blad:.6f}")

        if blad <= oczekiwanyBlad:
            znalezionoStopien = True
        else:
            stopien += 1

    if znalezionoStopien:
        print(f"Znaleziono wielomian stopnia {stopien} z błędem {blad:.6f} <= {oczekiwanyBlad}")

        print(f"Współczynniki wielomianu aproksymacyjnego stopnia {stopien}:")
        for i, wspolczynnik in enumerate(wspolczynniki):
            print(f"a{i} = {wspolczynnik:.6f}")

        rysujWykresy(funkcja, wspolczynniki, a, b)
    else:
        print(f"\nNie udało się znaleźć wielomianu o błędzie <= {oczekiwanyBlad} w zakresie stopni 1-20")


def rysujWykresy(funkcja, wspolczynniki, a, b, iloscPunktow=1000):
    x = np.linspace(a, b, iloscPunktow)
    y_funkcja = [funkcja(punkt) for punkt in x]
    y_aproksymacja = [wielomianAproksymujacy(punkt, wspolczynniki) for punkt in x]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y_funkcja, "b-", label="Funkcja oryginalna")
    plt.plot(x, y_aproksymacja, "r--", label=f"Aproksymacja (stopień {len(wspolczynniki) - 1})")
    plt.grid(True)
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()