#Zadanie z 4 modułu - kalkulator
import logging
def wprowadz_liczbe():
    while True:
        try:
            liczba =float(input("Wprowadź liczbę: "))
            return liczba
        except ValueError:
            logging.error("To nie jest prawidłowa liczba. Spróbuj ponownie.")
            print("To nie jest prawidłowa liczba. Spróbuj ponownie.")

def wprowadz_liczby():
    liczby = []
    while True:
        try:
            wprowadzona_wartosc = input("Wprowadź liczbę lub wpisz 'koniec', aby obliczyć wynik: ")
            if wprowadzona_wartosc.lower() == 'koniec':
                if len(liczby) < 2:
                    logging.error("Potrzebujesz co najmniej dwóch liczb.")
                    print("Potrzebujesz co najmniej dwóch liczb.")
                else:
                    return liczby
            else:
                liczba = float(wprowadzona_wartosc)
                liczby.append(liczba)
        except ValueError:
            logging.error("To nie jest prawidłowa liczba. Spróbuj ponownie.")
            print("To nie jest prawidłowa liczba. Spróbuj ponownie.")

