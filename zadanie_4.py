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

def dodawanie():
    logging.info("Wywołuję funkcję dodawanie.")
    liczby = wprowadz_liczby()
    wynik = sum(liczby)
    logging.info(f"Wynik dodawania to: {wynik}")
    print(f"Wynik dodawania to: {wynik}")
    
def odejmowanie():
    logging.info("Wywołuję funkcję odejmowanie.")
    x = wprowadz_liczbe("Podaj pierwszą liczbę: ")
    y = wprowadz_liczbe("Podaj drugą liczbę: ")
    wynik = x - y
    logging.info(f"Wynik odejmowania to: {wynik}")
    print(f"Wynik odejmowania to: {wynik}")
    
def mnozenie():
    logging.info("Wywołuję funkcję mnożenia")
    liczby = wprowadz_liczby()

    if len(liczby) <2:
        logging.error("Potrzebujesz co najmniej dwóch liczb.")
        print("Potrzebujesz co najmniej dwóch liczb.")
    else:
        wynik = 1

        for liczba in liczby:
            wynik *= liczba
    logging.info(f"Wynik mnożenia to: {wynik}")        
    print(f"Wynik mnożenia to: {wynik}")

