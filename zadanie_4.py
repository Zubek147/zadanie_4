import logging

log_directory = "C:\\Kodilla\\kurs_python\\Modul 4\\Zad_4"

log_file = f"{log_directory}/kalkulator.log"

logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()

def dodawanie(*args):
    wynik = sum(args)
    liczby_str = ', '.join(map(str, args))
    logger.info(f"Dodane liczby to: {liczby_str}, wynik dodawania to: {wynik}")
    print(f"Dodane liczby to: {liczby_str}, wynik dodawania to: {wynik}")

def odejmowanie(x, y):
    wynik = x - y
    logger.info(f"Pierwsza liczba to: {x}, liczba odejmowana to: {y}, wynik odejmowania to: {wynik}")
    print(f"Pierwsza liczba to: {x}, liczba odejmowana to: {y}, wynik odejmowania to: {wynik}")

def mnozenie(*args):
    if len(args) < 2:
        logger.error("Potrzebujesz co najmniej dwóch liczb.")
        print("Potrzebujesz co najmniej dwóch liczb.")
    else:
        wynik = 1
        liczby_str = ', '.join(map(str, args))
        for liczba in args:
            wynik *= liczba
        logger.info(f"Liczby które zostały przemnożone to: {liczby_str}, wynik mnożenia to: {wynik}")
        print(f"Liczby które zostały przemnożone to: {liczby_str}, wynik mnożenia to: {wynik}")

def dzielenie(x, y):
    while True:
        try:
            wynik = x / y
            if y == 0:
                raise ZeroDivisionError("Nie można dzielić przez zero, podaj poprawną wartość")
            logger.info(f"Liczba Dzielna to: {x}, dzielnik to: {y}, wynik dzielenia to: {wynik}")
            print(f"Liczba Dzielna to: {x}, dzielnik to: {y}, wynik dzielenia to: {wynik}")
            break
        except (ZeroDivisionError, ValueError):
            logger.error("Nie można dzielić przez zero, podaj poprawną wartość")
            print("Nie można dzielić przez zero, podaj poprawną wartość")
            y = pobierz_liczbe()

def zakoncz_program():
    logger.info("Wybrano zakończenie programu")
    print("Wybrano zakończenie programu")
    exit()

def pobierz_liczbe():
    while True:
        wprowadzona_wartosc = input("Wprowadź liczbę lub wpisz 'koniec', aby obliczyć wynik: ")
        if wprowadzona_wartosc.lower() == 'koniec':
            return None
        elif wprowadzona_wartosc.replace('.', '').replace('-', '').isdigit():
            return float(wprowadzona_wartosc)
        else:
            logger.error("To nie jest prawidłowa liczba. Spróbuj ponownie.")
            print("To nie jest prawidłowa liczba. Spróbuj ponownie.")

def wyswietl_menu():
    print("\nPodaj działanie posługując się odpowiednią liczbą:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Zakończ program")

def wykonaj_operacje(operacje, wybor):
    if wybor in operacje:
        if wybor in {'1', '3'}:
            liczby = []
            while True:
                liczba = pobierz_liczbe()
                if liczba is not None:
                    liczby.append(liczba)
                else:
                    break
            if len(liczby) >= 2:
                operacje.get(wybor)(*liczby)
        else:
            x = pobierz_liczbe()
            y = pobierz_liczbe()
            if x is not None and y is not None:
                operacje.get(wybor)(x, y)
    else:
        print("Nieprawidłowy wybór!")

def kalkulator():
    operacje = {
        '1': dodawanie,
        '2': odejmowanie,
        '3': mnozenie,
        '4': dzielenie,
        '5': zakoncz_program
    }

    while True:
        wyswietl_menu()

        wybor = input("Twój wybór: ")

        if wybor == '5':
            operacje[wybor]()
        else:
            wykonaj_operacje(operacje, wybor)

if __name__ == '__main__':
    kalkulator()
