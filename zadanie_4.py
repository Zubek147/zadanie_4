#Zadanie z 4 modułu - kalkulator

def wprowadz_liczbe():
    while True:
        try:
            liczba =float(input("Wprowadź liczbę: "))
            return liczba
        except ValueError:
            print("To nie jest prawidłowa liczba. Spróbuj ponownie.")

def wprowadz_liczby():
    liczby = []
    while True:
        try:
            wprowadzona_wartosc = input("Wprowadź liczbę lub wpisz 'koniec', aby obliczyć wynik: ")
            if wprowadzona_wartosc.lower() == 'koniec':
                if len(liczby) < 2:
                    print("Potrzebujesz co najmniej dwóch liczb.")
                else:
                    return liczby
            else:
                liczba = float(wprowadzona_wartosc)
                liczby.append(liczba)
        except ValueError:
            print("To nie jest prawidłowa liczba. Spróbuj ponownie.")

def oblicz_sume(liczby):
    suma =  sum(liczby)
    return suma

def oblicz_iloczyn(liczby):
    iloczyn = 1
    for liczba in liczby:
        iloczyn = iloczyn * liczba
    return iloczyn