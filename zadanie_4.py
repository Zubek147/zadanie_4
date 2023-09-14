#Zadanie z 4 modułu - kalkulator
import logging
logging.basicConfig(filename='kalkulator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

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
    x = wprowadz_liczbe()
    y = wprowadz_liczbe()
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

def dzielenie():
    logging.info("Wywołuję funkcję dzielenia")
    x = wprowadz_liczbe()
    y = wprowadz_liczbe()
    if y != 0:
        wynik = x / y
        logging.info(f"Wynik dzielenia to: {wynik}")
        print(f"Wynik dzielenia to: {wynik}")
    else:
        logging.error("Nie można dzielić przez zero")
        print("Nie można dzielić przez zero")

def zakoncz_program():
    exit()

def kalkulator():
    operacje = {
        '1' : dodawanie,
        '2' : odejmowanie,
        '3' : mnozenie,
        '4' : dzielenie,
        '5' : zakoncz_program
    }   

    while True:
        print("\nPodaj działanie posługując się odpowiednią liczbą:")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Zakończ program")

        wybor = input("Twój wybór: ")

        operacja = operacje.get(wybor)
        if operacja:
            operacja()
        else:
            print("Nieprawidłowy wybór!")

if __name__ == '__main__':
    kalkulator()
