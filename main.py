from rownania import *
import aproksymacja

while True:
    print("Wybierz funkcję do aproksymacji:\n"
        "1. Liniowa: 2x - 3\n"
        "2. Moduł: |x|\n"
        "3. Wielomian: -2x^3 + 4x^2 + 5\n"
        "4. Trygonometryczna: sin(x) - 0.5\n"
        "5. Złożona: e^(sin(x)) - 2\n"
        "0. Zakończ program")

    czyFunkcjaWybrana = False
    while czyFunkcjaWybrana != True:
        wybor = int(input("Wybierz funkcję (1-5): "))

        # wybor funkcji
        if wybor == 0:
            exit(0)
        elif wybor == 1:
            funkcja = funkcjaLiniowa
            nazwaFunkcji = "2x - 3"
            czyFunkcjaWybrana = True
        elif wybor == 2:
            funkcja = funkcjaModul
            nazwaFunkcji = "|x|"
            czyFunkcjaWybrana = True
        elif wybor == 3:
            funkcja = funkcjaWielomianowa
            nazwaFunkcji = "-2x^3 + 4x^2 + 5"
            czyFunkcjaWybrana = True
        elif wybor == 4:
            funkcja = funkcjaTrygonometryczna
            nazwaFunkcji = "sin(x) - 0.5"
            czyFunkcjaWybrana = True
        elif wybor == 5:
            funkcja = funkcjaZlozona
            nazwaFunkcji = "e^(sin(x)) - 2"
            czyFunkcjaWybrana = True
        else:
            print("Wpisano niewłaściwą funkcję!")

    # wybor przedzialu aproksymacji
    a = float(input("Początek przedziału aproksymacji: "))
    b = float(input("Koniec przedziału aproksymacji: "))

    # wybor trybu pracy
    print("Wybierz tryb pracy:")
    print("1. Aproksymacja wielomianem o podanym stopniu")
    print("2. Iteracyjne dobieranie stopnia wielomianu dla zadanej dokładności")

    czyWybranoTryb = False
    while czyWybranoTryb != True:
        trybPracy = int(input("Wybierz tryb (1-2): "))
        if trybPracy == 1:
            aproksymacja.wielomianem(funkcja, a, b)
            czyWybranoTryb = True
        elif trybPracy == 2:
            aproksymacja.iteracyjna(funkcja, a, b)
            czyWybranoTryb = True
        else:
            print("Wybrano niewłaściwą opcję!")
    print("----------------------------------")