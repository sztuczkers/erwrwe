from hero import Hero

def choose_hero(name):
    print("Wybierz swoją postać:")
    print("1. Wojownik: 200 punktów życia, 180 many, 650 pieniędzy, 120 punktów ataku i 180 punktów obrony")
    print("2. Mag: 180 punktów życia, 240 many, 600 pieniędzy, 140 punktów ataku i 140 punktów obrony")
    print("3. Łowca: 200 punktów życia, 200 many, 700 pieniędzy, 110 punktów ataku i 170 punktów obrony")
    print("4. Paladyn: 220 punktów życia, 160 many, 800 pieniędzy, 130 punktów ataku i 160 punktów obrony")

    while True:
        try:
            character_decision = int(input("Wybierz numer postaci: "))
            if 1 <= character_decision <= 4:
                break
            else:
                print("Wybierz liczbę od 1 do 4.")
        except ValueError:
            print("Wybierz poprawną liczbę.")

    if character_decision == 1:
        return Hero(name, 200, 180, 650, 120, 180)
    elif character_decision == 2:
        return Hero(name, 180, 240, 600, 140, 140)
    elif character_decision == 3:
        return Hero(name, 200, 200, 700, 110, 170)
    elif character_decision == 4:
        return Hero(name, 220, 160, 800, 130, 160)
