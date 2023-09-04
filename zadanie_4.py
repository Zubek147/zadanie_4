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

def oblicz_sume(liczby):
    suma =  sum(liczby)
    return suma

def oblicz_iloczyn(liczby):
    iloczyn = 1
    for liczba in liczby:
        iloczyn = iloczyn * liczba
    return iloczyn

def kalkulator():

    logging.basicConfig(filename='kalkulator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()

    while True:
        print("\nPodaj działanie posługując się odpowiednią liczbą:")
        print("1. Dodawanie")
        print("2. Odejmowanie")
        print("3. Mnożenie")
        print("4. Dzielenie")
        print("5. Zakończ program")

        wybor = input("Twój wybór: ")

        if wybor == '1':
            liczby = wprowadz_liczby()
            wynik = oblicz_sume(liczby)
            print("Wynik dodawania:", wynik)
            logging.info(f"Wynik dodawania: {wynik}")
        elif wybor == '2':
            x = wprowadz_liczbe()
            y = wprowadz_liczbe()
            wynik  = x - y
            print("Wynik odejmowania:", wynik)
            logging.info(f"Wynik odejmowania: {wynik}")
        elif wybor == '3':
            liczby = wprowadz_liczby()
            wynik = oblicz_iloczyn(liczby)
            print("Wynik mnożenia:", wynik)
            logging.info(f"Wynik mnożenia: {wynik}")
        elif wybor == '4':
            x = wprowadz_liczbe()
            y = wprowadz_liczbe()
            if y != 0:
                wynik = x/y
                print("Wynik dzielenia:", wynik)
                logging.info(f"Wynik dzielenia: {wynik}")
            else:
                print("Nie można dizelić przez zero.")
                logging.error("Nie można dzielić przez zero")
        elif wybor == '5':
            print("Program zakończony.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            logging.error("Nieprawidłowy wybór. Spróbuj ponownie.")

kalkulator()
