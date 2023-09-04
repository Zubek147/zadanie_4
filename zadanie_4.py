#Zadanie z 4 modułu - kalkulator

def wprowadz_liczbe():
    while True:
        try:
            liczba =float(input("Wprowadź liczbę: "))
            return liczba
        except ValueError:
            print("To nie jest prawidłowa liczba. Spróbuj ponownie.")