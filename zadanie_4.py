#Zadanie z 4 modułu - kalkulator
import logging
log_directory = "C:\\Kodilla\\kurs_python\\Modul 4\\Zad_4"

log_file = f"{log_directory}/kalkulator.log"

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
    print("Wywołuję funkcję dodawanie.")
    liczby = wprowadz_liczby()
    wynik = sum(liczby)
    liczby_str = ', '.join(map(str, liczby))
    logging.info(f"Dodane liczby to: {liczby_str}, wynik dodawania to: {wynik}")
    print(f"Dodane liczby to: {liczby_str}, wynik dodawania to: {wynik}")
    
def odejmowanie():
    logging.info("Wywołuję funkcję odejmowanie.")
    print("Wywołuję funkcję odejmowanie.")
    x = wprowadz_liczbe()
    y = wprowadz_liczbe()
    wynik = x - y
    logging.info(f"Pierwsza liczba to: {x}, liczba odejmowana to: {y}, wynik odejmowania to: {wynik}")
    print(f"Pierwsza liczba to: {x}, liczba odejmowana to: {y}, wynik odejmowania to: {wynik}")
    
def mnozenie():
    logging.info("Wywołuję funkcję mnożenia")
    print("Wywołuję funkcję mnożenia")
    liczby = wprowadz_liczby()

    if len(liczby) <2:
        logging.error("Potrzebujesz co najmniej dwóch liczb.")
        print("Potrzebujesz co najmniej dwóch liczb.")
    else:
        wynik = 1

        for liczba in liczby:
            wynik *= liczba
            liczby_str = ', '.join(map(str, liczby))
    logging.info(f"Liczby które zostały przemnożone to: {liczby_str}, wynik mnożenia to: {wynik}")        
    print(f"Liczby które zostały przemnożone to: {liczby_str}, wynik mnożenia to: {wynik}")

def dzielenie():
    logging.info("Wywołuję funkcję dzielenia")
    print("Wywołuję funkcję dzielenia")
    x = wprowadz_liczbe()

    while True:
        y = wprowadz_liczbe()
        try:
            wynik = x / y
            if y == 0:
                raise ZeroDivisionError("Nie można dzielić przez zero, podaj poprawną wartość")
            logging.info(f"Liczba Dzielna to: {x}, dzielnik to: {y}, wynik dzielenia to: {wynik}")
            print(f"Liczba Dzielna to: {x}, dzielnik to: {y}, wynik dzielenia to: {wynik}")
            break
        except (ZeroDivisionError, Exception):
            logging.error("Nie można dzielić przez zero, podaj poprawną wartość")
            print("Nie można dzielić przez zero, podaj poprawną wartość")


def zakoncz_program():
    logging.info("Wybrano zakończenie programu")
    print("Wybrano zakończenie programu")
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
