import random
import os

litery = "qwertyuiopasdfghjklzxcvbnm"
cyfry = "qwertyuiopasdfghjklzxcvbnm1234567890"
znaki = "qwertyuiopasdfghjklzxcvbnm!@#$"
zil = "qwertyuiopasdfghjklzxcvbnm!@#$1234567890"
duzil = "qwertyuiopasdfghjklzxcvbnm!@#$1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
duznki = "qwertyuiopasdfghjklzxcvbnm!@#$QWERTYUIOPASDFGHJKLZXCVBNM"
duzcyf = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

while True:

    haslo = ""

    print("co chcesz zrobic?")
    print("1. wygeneruj haslo")
    print("2. pokaz zapisane")
    print("3. wyjdz")

    robic = int(input(""))

    if robic == 1:
        print("podaj dlugosc hasla (max 30)")
        dlugosc = int(input(""))

        if dlugosc <= 30 and dlugosc > 0:

            print("czy maja byc cyfry? (tak/nie)")
            cyfy = input("")

            print("czy maja byc duze litery? (tak/nie)")
            duze = input("")

            print("czy maja byc znaki specjalne? (tak/nie)")
            znki = input("")

            for i in range(dlugosc):

                if duze == "tak":
                    if cyfy == "tak":
                        if znki == "tak":
                            haslo += random.choice(duzil)
                        else:
                            haslo += random.choice(duzcyf)

                    elif znki == "tak":
                        haslo += random.choice(duznki)

                    else:
                        haslo += random.choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")

                else:
                    if cyfy == "tak":
                        if znki == "tak":
                            haslo += random.choice(zil)
                        else:
                            haslo += random.choice(cyfry)

                    elif znki == "tak":
                        haslo += random.choice(znaki)

                    else:
                        haslo += random.choice(litery)

            print("twoje haslo:", haslo)
            print("czy chcesz je zapisac? (tak/nie)")
            taklubnie = input("")

            if taklubnie == "tak":
                print("do czego jest to haslo?")
                platforma = input("")

                with open("hasla.txt", "a") as plik:
                    plik.write(platforma + ": " + haslo + "\n")

        else:
            print("dlugosc musi byc od 1 do 30")

    elif robic == 2:
        try:
            with open("hasla.txt", "r") as plik:
                print(plik.read())
        except FileNotFoundError:
            print("nie masz jeszcze zapisanych hasel")

    elif robic == 3:
        print("koniec")
        break

    else:
        print("niepoprawna opcja")