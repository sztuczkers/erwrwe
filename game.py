from random import randint

from hero import Hero

from enemies import Wolf, Dragon, Shark, Barbarian, Scorpio, Shaman, Fox, Snake, Bear, Spider, Deer, Sigma, Demon

class Game:
    def __init__(self):
        self.difficulty = None
        self.hero = None
        self.artifacts_collected = 0

    def start(self):
        print("Witaj w magicznym królestwie! Czy jesteś gotowy na swoją przygodę?")
        
        print("Podaj imię swojego bohatera:")
        self.name = input()
        
        print("Wybierz swoją postać:")
        print("1.Wojownik ma  200 punktów życia, 180 many, 650 pieniedzy, 120 punktów ataku i 180 punktów obrony")
        print("2. Mag ma  180 punktów życia, 240 many, 600 pieniedzy, 140 punktów ataku i 140 punktów obrony")
        print("3. Łowca ma  200 punktów życia, 200 many, 700 pieniedzy, 110 punktów ataku i 170 punktów obrony")
        print("4. Paladyn ma  220 punktów życia, 160 many, 800 pieniedzy, 130 punktów ataku i 160 punktów obrony")
    
        
        while True:
            try:
                character_decision = int(input("Wybierz numer postaci: "))
                if 1 <= character_decision <= 4:
                    break
                else:
                    print("Wybierz liczbę od 1 do 4.")
            except ValueError:
                print("Wybierz poprawną liczbę.")

        self.hero = self.create_hero(character_decision)
            
        print("Witaj, " + self.name + "! Zapraszamy do magicznego królestwa, gdzie odważni bohaterowie wyruszają na niebezpieczne przygody, by uratować świat przed mrocznymi siłami")
        print(f"Masz {self.hero.money} pieniędzy.")
        print(f"Masz {self.hero.life} punktów życia.")
        print(f"Masz {self.hero.defense} punktów obrony." )
        print(f"Masz {self.hero.attack} punktów ataku.")
        print(f"Masz {self.hero.mana} many.")
        self.choose_difficulty()
    
    def create_hero(self, decision):
        if decision == 1:
            return Hero("Wojownik", 200, 180, 650, 120, 180)
        elif decision == 2:
            return Hero("Mag", 180, 240, 600, 140, 140)
        elif decision == 3:
            return Hero("Łowca", 200, 200, 700, 110, 170)
        elif decision == 4:
            return Hero("Paladyn", 220, 160, 800, 130, 160)


    def choose_difficulty(self):
        print("Wybierz poziom trudności:")
        print("1. Bardzo łatwy")
        print("2. Łatwy")
        print("3. Średni")
        print("4. Trudny")
        print("5. Bardzo trudny")

        while True:
            try:
                self.difficulty = int(input("Wybierz numer poziomu trudności: "))
                if 1 <= self.difficulty <= 5:
                    break
                else:
                    print("Wybierz liczbę od 1 do 5.")
            except ValueError:
                print("Wybierz poprawną liczbę.")

        self.hero.life -= self.difficulty * 10
        self.hero.attack -= self.difficulty * 10
        print("Twój bohater traci", self.difficulty * 10, "punktów życia z powodu wybranego poziomu trudności.")
        print("Twój bohater traci", self.difficulty * 10, "punktów ataku z powodu wybranego poziomu trudności.")
        
        print("Rozpoczynasz grę na poziomie trudności:", self.get_difficulty_name())
        print("Twoja misja zaczyna się podczas konnej wyprawy. Nagle atakuje cię trzy zmutowanne wilki!")
        self.make_decision()

    def get_difficulty_name(self):
        if self.difficulty == 1:
            return "Bardzo łatwy"
        elif self.difficulty == 2:
            return "Łatwy"
        elif self.difficulty == 3:
            return "Średni"
        elif self.difficulty == 4:
            return "Trudny"
        elif self.difficulty == 5:
            return "Bardzo trudny"
        
    def make_decision(self):
        print("Co robisz?") 
        print("1. Walczysz z trzema wilkami")
        print("2. Jedziesz inną drogą")
        print("3. Omijasz go jadąc przez las")

        decision = input("Podaj numer opcji: ")

        if decision == "1":
            print("Rozpoczynasz walkę z trzema wilkami!")
            self.battle_wolf()
        elif decision == "2":
            print("Postanawiasz jechać inną drogą.")
            self.other_route()
        elif decision == "3":
            print("Omijasz wilka, jadąc przez las.")
            self.pass_through_forest()
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            self.make_decision()

    def battle_wolf(self):
        for i in range(3):
            wolf_name = input(f"Podaj imię {i+1} wilka: ")
            wolf = Wolf(wolf_name, )
            print(f"Rozpoczynasz walkę z {wolf.name}em!")

            reward = randint(50, 100)
            print(f"{wolf.name} atakuje cię i zadaje", wolf.attack_power, "obrażeń.")
            self.hero.life -= wolf.attack_power
            self.hero.defense -= wolf.attack_power

            if self.hero.life <= 0 and self.hero.defense <= 0:
                print(f"Zostałeś pokonany przez {wolf.name}a. Koniec gry.")
                return

            print(f"Pokonałeś {wolf.name}a i zdobywasz", reward, "pieniędzy jako nagrodę za walkę!")
            self.hero.money += reward

            print("Aktualny stan pieniędzy:", self.hero.money)
            print("Aktualny stan życia:", self.hero.life)
            print("Aktualny stan obrony:", self.hero.defense)
            print("Aktualny stan ataku:", self.hero.attack)
            print("Aktualny stan many:", self.hero.mana)
            print(f"Gratulacje! Wygrałeś walkę z {wolf.name}em.")
        
        self.encounter_dragon()
        self.show_artifacts_collected()
        self.encounter_Shark()
        self.show_artifacts_collected()
        self.encounter_barbarian()
        self.show_artifacts_collected()
        self.encounter_scorpio()
        self.show_artifacts_collected()
        self.encounter_shaman()
        self.show_artifacts_collected()
        self.exchange_artifacts_for_reward()
        self.Shopping_in_shop()
        self.encounter_beggar()

    def other_route(self):
        print("Wybrałeś inną drogę.")
        print("Podróż jest bezpieczna, ale zajmuje trochę więcej czasu.")
        self.hero.money += 30
        mana = randint(1,10)
        
        print("Zdobywasz dodatkowo 30 pieniędzy za podróż inną drogą i tracisz",mana, "many")
        self.hero.mana -= mana
        
        print("Aktualny stan pieniędzy:", self.hero.money)
        print("Aktualny stan życia:", self.hero.life)
        print("Aktualny stan obrony:", self.hero.defense)
        print("Aktualny stan ataku:", self.hero.attack)
        print("Aktualny stan many:", self.hero.mana)

        self.encounter_dragon()
        self.show_artifacts_collected()
        self.encounter_Shark()
        self.show_artifacts_collected()
        self.encounter_barbarian()
        self.show_artifacts_collected()
        self.encounter_scorpio()
        self.show_artifacts_collected()
        self.encounter_shaman()
        self.show_artifacts_collected()
        self.exchange_artifacts_for_reward()
        self.Shopping_in_shop()
        self.encounter_beggar()

    def pass_through_forest(self):
        print("Decydujesz się ominąć wilka, jadąc przez las.")
        print("W lesie spotykasz czarownice")

        health_potion = randint(10, 20)
        print("Otrzymujesz miksturę zdrowia, która daje", health_potion, "punktów życia")

        print("Otrzymujesz kilka monet znalezionych na drodze.")
        self.hero.life += health_potion
        self.hero.money += 10
        
        print("Zdobywasz dodatkowo 10 pieniędzy za omijanie wilka.")
        
        print("Aktualny stan pieniędzy:", self.hero.money)
        print("Aktualny stan życia:", self.hero.life)
        print("Aktualny stan obrony:", self.hero.defense)
        print("Aktualny stan ataku:", self.hero.attack)
        print("Aktualny stan many:", self.hero.mana)
        
        self.encounter_dragon()
        self.show_artifacts_collected()
        self.encounter_Shark()
        self.show_artifacts_collected()
        self.encounter_barbarian()
        self.show_artifacts_collected()
        self.encounter_scorpio()
        self.show_artifacts_collected()
        self.encounter_shaman()
        self.show_artifacts_collected()
        self.exchange_artifacts_for_reward()
        self.Shopping_in_shop()
        self.encounter_beggar()

    def encounter_dragon(self):
        print("Zaczynasz swoją przygode musisz zdobyc 5 artefaktow aby ukonczyc gre.")
        dragon_name = input("Podaj imię smoka: ")
        dragon = Dragon(dragon_name,)
        print(f"Podczas podróży przez las, natykasz się na straszliwego smoka o imieniu {dragon.name}!")
        print("To jest boss tego obszaru. Walczysz z nim, aby zdobyć pierwszy z pieciu magicznych artefaktów.")

        print("Co chcesz zrobić?")
        print(f"1. Obudzić {dragon_name}a i walczyc z {dragon_name}em")
        print(f"2. Próbujesz zabrac artefakt bez budzenia i bez walki z {dragon_name}em ")
        
        decision = input("Wybierz opcję: ")
        
        if decision == "1":
            self.battle_forest_boss(dragon)
        elif decision == "2":
            self.trick_forest_boss(dragon)
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            self.encounter_dragon()
        
    def battle_forest_boss(self,dragon):
        for _ in range(10):  
            print("Walka rozpoczęta!")
            hero_damage = randint(self.hero.attack // 2, self.hero.attack)
            dragon_damage = randint(dragon.attack_power // 2, dragon.attack_power)

            print(f"Atakujesz {dragon.name}a i zadajesz mu {hero_damage} obrażeń.")
            dragon.life -= hero_damage

            if dragon.life <= 0:
                print(f"Gratulacje! Pokonałeś {dragon.name}a i zdobywasz pierwszy magiczny artefakt.")
                self.artifacts_collected += 1
                return

            print(f"{dragon.name} kontratakuje i zadaje ci {dragon_damage} obrażeń.")
            self.hero.life -= dragon_damage

            if self.hero.life <= 0:
                print(f"Zostałeś pokonany przez {dragon.name}a. Koniec gry.")
                return

            print(f"Aktualny stan życia {dragon.name}a: {dragon.life}")
            print(f"Aktualny stan  życia {self.name}a : {self.hero.life}")

        print("Walka zakończona.")
    
    def trick_forest_boss(self,dragon):
        print(f"Próbujesz nie obudzić {dragon.name}a.")

        success_chance = randint(1, 10)
        if success_chance> 5:
            print(f"Udało ci się nie obudzić {dragon.name}a i zabrac artefakt! Otrzymujesz pierwszy magiczny artefakt.")
            self.artifacts_collected += 1
        else:
            print(f"Obudziłeś {dragon.name}a. Musisz z nim walczyc.")
            self.battle_forest_boss(dragon)
    
    def encounter_Shark(self):
        shark_name = input("Podaj imię rekina : ")
        shark = Shark(shark_name,)
        print(f"Podczas swojej przygody natrafiasz na bossa oceanu o imieniu {shark.name}!")
        print("To jest boss tego obszaru. Walczysz z nim, aby zdobyć drugi z pieciu magicznych artefaktów.")

        print("Co chcesz zrobić?")
        print(f"1. Walczyć z {shark_name}em")
        print(f"2. Próbujesz ukraść artefakt bez walki z {shark_name}em ")
        
        decision = input("Wybierz opcję: ")
        
        if decision == "1":
            self.battle_ocean_boss(shark)
        elif decision == "2":
            self.escape_from_shark(shark)
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            self.encounter_Shark()
        
    def battle_ocean_boss(self,shark):
        for _ in range(8):
            print("Walka rozpoczęta!")
            hero_damage = randint(self.hero.attack // 2, self.hero.attack)
            shark_damage = randint(shark.attack_power // 2, shark.attack_power)

            print(f"Atakujesz {shark.name}a i zadajesz mu {hero_damage} obrażeń.")
            shark.life -= hero_damage

            if shark.life <= 0:
                print(f"Gratulacje! Pokonałeś {shark.name}a i zdobywasz drugi magiczny artefakt.")
                self.artifacts_collected += 1
                return
            
            print(f"{shark.name} kontratakuje i zadaje ci {shark_damage} obrażeń.")
            self.hero.life -= shark_damage

            if self.hero.life <= 0:
                print(f"Zostałeś pokonany przez {shark.name}a. Koniec gry.")
                return
            
            print(f"Aktualny stan życia {shark.name}a: {shark.life}")
            print(f"Aktualny stan  życia {self.name}a : {self.hero.life}")
        
        print("Walka zakończona.")
    
    def escape_from_shark(self, shark):
        print(f"Próbujesz uciec z drugim artefaktem przed {shark.name}em.")

        chance_to_escape = randint(1, 3) 

        if chance_to_escape == 1:
            print("Udało ci się uciec przed rekinem!")
            print("Zdołałeś uniknąć walki i zdobywasz drugi magiczny artefakt.")
            self.artifacts_collected += 1
        else:
            print("Niestety, rekin cię złapał!")
            self.battle_ocean_boss(shark)

    def encounter_barbarian(self):
        barbarian_name = input("Podaj imie barbarzyńcy: ")
        barbarian = Barbarian(barbarian_name,)
        print(f"Podczas swojej przygody natrafiasz na bossa miasta o imieniu {barbarian.name}!")
        print("To jest boss tego obszaru. Walczysz z nim lub możesz go przekupić aby zdobyć trzeci z pieciu magicznych artefaktów.")

        print("Co wybierasz?")
        print(f"1. Walczysz z {barbarian_name}em ")
        print(f"2. Próbujesz przekupić {barbarian_name}a ")

        decision = input("Podaj numer opcji: ")

        if decision == "1":
            self.battle_city_boss(barbarian)
        elif decision == "2":
            self.bribe_city_boss(barbarian)
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            self.encounter_barbarian()
        
    def battle_city_boss(self,barbarian):      
        for _ in range(6):
            print(f"Rozpoczynasz walkę z {barbarian.name}em !")
            hero_damage = randint(self.hero.attack // 2, self.hero.attack)
            barbarian_damage = randint(barbarian.attack_power // 2, barbarian.attack_power)

            print(f"Atakujesz {barbarian.name}a i zadajesz mu {hero_damage} obrażeń.")
            barbarian.life -= hero_damage

            if barbarian.life <= 0:
                print(f"Gratulacje! Pokonałeś {barbarian.name}a i zdobywasz trzeci magiczny artefakt.")
                self.artifacts_collected += 1
                return

            print(f"{barbarian.name} kontratakuje i zadaje ci {barbarian_damage} obrażeń.")
            self.hero.life -= barbarian_damage

            if self.hero.life <= 0:
                print(f"Zostałeś pokonany przez {barbarian.name}a. Koniec gry.")
                return
            
            print(f"Aktualny stan życia {barbarian.name}a: {barbarian.life}")
            print(f"Aktualny stan  życia {self.name}a : {self.hero.life}")

        print("Walka zakończona.")

    def bribe_city_boss(self,barbarian):
        
        print(f"Próbujesz przekupić {barbarian.name}a za złoto i manę.")

        
        if self.hero.money >= 200 and self.hero.mana >= 100:
            print(f"Udało ci się przekupić {barbarian.name}a! Zdobywasz kolejny magiczny artefakt.")
            self.artifacts_collected += 1
            self.hero.money -= 200
            self.hero.mana -= 100
        else:
            print(f"Nie masz wystarczająco dużo złota i many, aby przekupić {barbarian.name}.")
        
        print("Aktualny stan pieniędzy:", self.hero.money)
        print("Aktualny stan many:", self.hero.mana)
    
    def encounter_scorpio(self):
        scorpio_name = input("Podaj imie skorpiona: ")
        scorpio = Scorpio(scorpio_name,)
        
        print(f"Podczas swojej przygody natrafiasz na bossa pustyni o imieniu {scorpio.name}!")
        print("To jest boss tego obszaru. Walczysz z nim, aby zdobyć czwarty z magicznych artefaktów.")

        print("Co wybierasz?")
        print(f"1. Walczysz z {scorpio_name}em ")
        print("2. Próbujesz go oszukać")

        decision = input("Podaj numer opcji: ")

        if decision == "1":
            self.battle_desert_boss(scorpio)
        elif decision == "2":
            self.trick_desert_boss(scorpio)
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            self.encounter_scorpio()

    def battle_desert_boss(self,scorpio):
      for _ in range(5):
            print(f"Rozpoczynasz walkę z {scorpio.name}em !")
            hero_damage = randint(self.hero.attack // 2, self.hero.attack)
            barbarian_damage = randint(scorpio.attack_power // 2, scorpio.attack_power)

            print(f"Atakujesz {scorpio.name}a i zadajesz mu {hero_damage} obrażeń.")
            scorpio.life -= hero_damage

            if scorpio.life <= 0:
                print(f"Gratulacje! Pokonałeś {scorpio.name}a i zdobywasz czwarty magiczny artefakt.")
                self.artifacts_collected += 1
                return

            print(f"{scorpio.name} kontratakuje i zadaje ci {barbarian_damage} obrażeń.")
            self.hero.life -= barbarian_damage

            if self.hero.life <= 0:
                print(f"Zostałeś pokonany przez {scorpio.name}a. Koniec gry.")
                return
            
            print(f"Aktualny stan życia {scorpio.name}a: {scorpio.life}")
            print(f"Aktualny stan  życia {self.name}a : {self.hero.life}")
            
            print("Walka zakończona.")

    
    def trick_desert_boss(self,scorpio):
        print(f"Postanawiasz spróbować oszukać {scorpio.name}a .")
        
        print("Co wybierasz?")
        print("1.Wybierasz lewą kryjówkę i próbujesz uniknąć walki  ")
        print("2. Wybierasz prawą kryjówkę i próbujesz uniknąć walki")

        decision = input("Podaj numer opcji: ")

        if decision == "1":
            self.left_hiding_place(scorpio)
        elif decision == "2":
            self.right_hiding_places(scorpio)
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            self.encounter_scorpio()
        
    def left_hiding_place(self,scorpio):
        
        success_chance = randint(1, 10)
        if success_chance > 5:
            print(f"Udało ci się oszukać {scorpio.name}a ! Zdobywasz czwarty magiczny artefakt.")
            self.artifacts_collected += 1
        else:
            print(f"Twoje oszustwo zostało wykryte! Musisz walczyć z {scorpio.name}em.")
            self.battle_desert_boss(scorpio)
    
    def right_hiding_places(self,scorpio):
        
        success_chance = randint(1, 10)
        if success_chance < 5:
            print(f"Udało ci się oszukać {scorpio.name}a ! Zdobywasz czwarty magiczny artefakt.")
            self.artifacts_collected += 1
        else:
            print(f"Twoje oszustwo zostało wykryte! Musisz walczyć z {scorpio.name}em.")
            self.battle_desert_boss(scorpio)
    
    def encounter_shaman(self):
        shaman_name = input("Podaj imie shamana: ")
        shaman = Shaman(shaman_name,)
        
        print(f"Podczas swojej przygody natrafiasz na bossa gor o imieniu {shaman.name}!")
        print("To jest boss tego obszaru. Walczysz z nim, aby zdobyć piaty  z magicznych artefaktów.")

        print("Co wybierasz?")
        print(f"1. Walczysz z {shaman_name}em ")
        print(f"2. Próbujesz zawrzeć sojusz z {shaman_name}em")

        decision = input("Podaj numer opcji: ")

        if decision == "1":
            self.battle_mountain_boss(shaman)
        elif decision == "2":
            self.alliance_with_mountain_boss(shaman)
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            self.encounter_shaman()

    def battle_mountain_boss(self,shaman):
        for _ in range(4):
            print(f"Rozpoczynasz walkę z {shaman.name}em !")
            hero_damage = randint(self.hero.attack // 2, self.hero.attack)
            barbarian_damage = randint(shaman.attack_power // 2, shaman.attack_power)

            print(f"Atakujesz {shaman.name}a i zadajesz mu {hero_damage} obrażeń.")
            shaman.life -= hero_damage

            if shaman.life <= 0:
                print(f"Gratulacje! Pokonałeś {shaman.name}a i zdobywasz piaty magiczny artefakt.")
                self.artifacts_collected += 1
                return

            print(f"{shaman.name} kontratakuje i zadaje ci {barbarian_damage} obrażeń.")
            self.hero.life -= barbarian_damage

            if self.hero.life <= 0:
                print(f"Zostałeś pokonany przez {shaman.name}a. Koniec gry.")
                return
            
            print(f"Aktualny stan życia {shaman.name}a: {shaman.life}")
            print(f"Aktualny stan  życia {self.name}a : {self.hero.life}")
            
            print("Walka zakończona.")
        
    def alliance_with_mountain_boss(self,shaman):
        print(f"Próbujesz zawrzeć sojusz z {shaman.name}em.")

        alliance_chance = randint(1, 10)
        if alliance_chance > 5:
            print(f"Udało ci się zawrzeć sojusz z {shaman.name}em! Otrzymujesz piąty magiczny artefakt.")
            self.artifacts_collected += 1
        else:
            print(f"{shaman.name} nie chce zawrzeć sojuszu. Musisz z nim walczyc.")
            self.battle_mountain_boss(shaman)

    def show_artifacts_collected(self,):
        print(f"Aktualna liczba zebranych artefaktów: {self.artifacts_collected}")

    def exchange_artifacts_for_reward(self):
        if self.artifacts_collected == 5:
            print("Gratulacje! Zdobyłeś wszystkie artefakty!")
            print("Możesz teraz wymienić wszystkie artefakty na nagrode .")
            
            gold = randint(400,600)
            life = randint(100,250)
            attack = randint(100,250)
            defense = randint(100,250)

            print("Jaką nagrode wybierasz?")
            print(f"1. {gold} pieniedzy i {life} puntkow zycia ")
            print(f"2. {gold} pieniedzy i {attack} punktow ataku ")
            print(f"3. {gold} pieniedzy i {defense} punktow obrony") 
            
            decision = input("Podaj numer opcji: ")

            if decision == "1":
                self.gold_life(gold,life)
            elif decision == "2":
                self.gold_attack(gold,attack)
            elif decision == "3":
                self.gold_defense(gold,defense)
            else:
                print("Niepoprawny wybór. Spróbuj ponownie.")
                self.exchange_artifacts_for_reward()

    def gold_life(self,gold,life):
        self.hero.money += gold
        self.hero.life +=life
        print(f"Wmieniles wszystkie artefakty na {gold} pieniedzy i {life} punktow zycia")
        print(f"Aktualny stan pieniędzy: {self.hero.money}")
        print(f"Aktualny stan zycia: {self.hero.life}")
    
    def gold_attack(self,gold,attack):
        self.hero.money += gold
        self.hero.attack += attack
        print(f"Wmieniles wszystkie artefakty na {gold} pieniedzy i {attack} punktow ataku")
        print(f"Aktualny stan pieniędzy: {self.hero.money}")
        print(f"Aktualny stan ataku: {self.hero.attack}")
    
    def gold_defense(self,gold,defense):
        self.hero.money += gold
        self.hero.defense += defense
        print(f"Wmieniles wszystkie artefakty na {gold} pieniedzy i {defense} punktow obrony")
        print(f"Aktualny stan pieniędzy: {self.hero.money}")
        print(f"Aktualny stan obrony: {self.hero.defense}")
    
    def Shopping_in_shop(self):
        print("Chcesz wejść do sklepu?")
        print("1. Tak")
        print("2. Nie")

        decision = input("Podaj numer opcji: ")

        if decision == "1":
            print("Witaj w sklepie!")
            self.visit_shop()
        elif decision == "2":
            print("Nie wchodzisz do sklepu i walczysz z lisem.")
            self.battle_fox()
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            self.Shopping_in_shop()

    def visit_shop(self):
        print("Co chcesz kupić?"  )
        available_items = {
            "1.Eliksir zdrowia (300 pieniedzy)": self.eliksir_zdrowia,
            "2.Duży eliksir zdrowia (550 pieniedzy)": self.duzy_eliksir_zdrowia,
            "3.Miecz (300 pieniedzy)": self.miecz,
            "4.Miecz i tarcza (600 pieniedzy)": self.miecz_tarcza
        }
        print("Dostępne przedmioty:")
        for item, self.visit_shop in available_items.items():
            print(f"{item}")

        decision = input("Podaj numer opcji: ")
        if decision.isdigit() and 0 < int(decision) <= len(available_items):
            selected_item = list(available_items.values())[int(decision) - 1]
            selected_item()
        else:
            print("Niepoprawny wybór.")

    def eliksir_zdrowia(self):
        if self.hero.money >= 300:
            self.hero.money -= 300
            self.hero.life += 50
            print("Kupiłeś eliksir zdrowia, tracisz 300 złotych. Twoje życie zostało przywrócone o 50 punktów.")
        else:
                print("Nie masz wystarczająco złota. Spróbuj jeszcze raz.")
        
        print("Aktualny stan pieniędzy:", self.hero.money)
        print("Aktualny stan życia:", self.hero.life)
        print("Aktualny stan obrony:", self.hero.defense)
        print("Aktualny stan ataku:", self.hero.attack)
        print("Aktualny stan many:", self.hero.mana)
    
    def duzy_eliksir_zdrowia(self):
        if self.hero.money >= 550:
            self.hero.money -= 550
            self.hero.life += 100
            print("Kupiłeś duży eliksir zdrowia, tracisz 550 złotych. Twoje życie zostało przywrócone o 100 punktów.")
        else:
                print("Nie masz wystarczająco złota. Spróbuj jeszcze raz.")
        
        print("Aktualny stan pieniędzy:", self.hero.money)
        print("Aktualny stan życia:", self.hero.life)
        print("Aktualny stan obrony:", self.hero.defense)
        print("Aktualny stan ataku:", self.hero.attack)
        print("Aktualny stan many:", self.hero.mana)
    
    def miecz(self):
        if self.hero.money >= 300:
            self.hero.money -= 300
            self.hero.attack += 55
            print("Kupiłeś miecz, tracisz 300 złotych. Twój atak został zwiększony o 55 punktów.")
        else:
            print("Nie masz wystarczająco złota. Spróbuj jeszcze raz.")
        
        print("Aktualny stan pieniędzy:", self.hero.money)
        print("Aktualny stan życia:", self.hero.life)
        print("Aktualny stan obrony:", self.hero.defense)
        print("Aktualny stan ataku:", self.hero.attack)
        print("Aktualny stan many:", self.hero.mana)
    
    def miecz_tarcza(self):
        if self.hero.money >= 600:
            self.hero.money -= 600
            self.hero.attack += 55
            self.hero.defense += 50
            print("Kupiłeś miecz i tarczę, tracisz 600 złotych. Twój atak został zwiększony o 55 punktów i obrona została zwiększona o 50 punktów.")
        else:
            print("Nie masz wystarczająco złota. Spróbuj jeszcze raz.")
        
        print("Aktualny stan pieniędzy:", self.hero.money)
        print("Aktualny stan życia:", self.hero.life)
        print("Aktualny stan obrony:", self.hero.defense)
        print("Aktualny stan ataku:", self.hero.attack)
        print("Aktualny stan many:", self.hero.mana)

    def battle_fox(self):
        fox_name = input("Podaj imię lisa: ")
        fox = Fox(fox_name,)
        print(f"Rozpoczynasz walkę z {fox.name}em!")

        reward = randint(100, 200)
        print(f"{fox.name} atakuje cię i zadaje", fox.attack_power, "obrażeń.")
        self.hero.life -= fox.attack_power
        self.hero.defense -= fox.attack_power

        if self.hero.life <= 0 and self.hero.defense <= 0:
                print(f"Zostałeś pokonany przez {fox.name}a. Koniec gry.")
                return
        
        print(f"Pokonałeś {fox.name}a i zdobywasz", reward, "punktów życia i", reward, "punktów obrony jako nagrodę za walkę!")
        self.hero.life += reward
        self.hero.defense += reward

        print("Aktualny stan pieniędzy:", self.hero.money)
        print("Aktualny stan życia:", self.hero.life)
        print("Aktualny stan obrony:", self.hero.defense)
        print("Aktualny stan ataku:", self.hero.attack)
        print("Aktualny stan many:", self.hero.mana)
        print(f"Gratulacje! Wygrałeś walkę z {fox.name}em.")

    def encounter_beggar(self):
        print("Spotykasz biedaka na swojej drodze.")
        print("1. Zapłać biedakowi 100 pieniędzy i idź bezpieczną drogą, która prowadzi do królestwa")
        print("2. Omiń biedaka i podążaj niebezpieczną drogą, która prowadzi do królestwa.")

        decision = input("Co chcesz zrobić? Wybierz opcję: ")

        if decision == "1":
            self.go_safe_way()
        elif decision == "2":
            self.go_dangerous_way()
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            self.encounter_beggar()

    def go_safe_way(self):
        if self.hero.money >= 100:
            print("Płacisz biedakowi.")
            print("Idziesz bezpieczną drogą do królestwa i tracisz 100 pieniędzy.")
            self.hero.money -= 100
            print("Aktualny stan pieniędzy:", self.hero.money)

            print("Ponieważ wybrałeś, żeby zapłacić biedakowi, masz mniej walk.")
        else:
            print("Nie masz wystarczająco dużo pieniędzy, aby zapłacić biedakowi.")
            self.encounter_beggar()
        
        self.encounter_snake()
        self.encounter_bear()
        self.final_battle()
        
    def encounter_snake(self):
        snake_name = input("Podaj imię węża: ")
        snake = Snake(snake_name,)
        
        print(f"Podczas swojej przygody do królestwa natrafiasz na węża o imieniu {snake.name}!")
        money = randint(30,50)  
        mana = randint(10,20)

        print("Co chcesz zrobić?")
        print(f"1. Walczyć z {snake_name}em i dostać nagrodę.")
        print(f"2. Ominąć {snake_name}a i stracić {money} pieniędzy i {mana} many.")
    
        decision = input("Wybierz opcję: ")

        if decision == "1":
            self.battle_snake(snake)
        elif decision == "2":
                self.avoiding_snake(snake,money,mana)
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            self.encounter_snake()
    
    def battle_snake(self,snake):
        for _ in range(5):
            print(f"Rozpoczynasz walkę z {snake.name}em !")
            hero_damage = randint(self.hero.attack // 2, self.hero.attack)
            snake_damage = randint(snake.attack_power // 2, snake.attack_power)

            print(f"Atakujesz {snake.name}a i zadajesz mu {hero_damage} obrażeń.")
            snake.life -= hero_damage

            if snake.life <= 0:
                print(f"Gratulacje! Pokonałeś {snake.name}a, dostajesz 100 pieniedzy i 50 many i możesz iść dalej.")
                self.hero.money += 100
                self.hero.mana += 50
                print(f"Aktualny stan zlota: {self.hero.money}")
                print(f"Aktualny stan many: {self.hero.mana}")
                return

            print(f"{snake.name} kontratakuje i zadaje ci {snake_damage} obrażeń.")
            self.hero.life -= snake_damage

            if self.hero.life <= 0:
                print(f"Zostałeś pokonany przez {snake.name}a. Koniec gry.")
                return
            
            print(f"Aktualny stan życia {snake.name}a: {snake.life}")
            print(f"Aktualny stan  życia {self.name}a : {self.hero.life}")
            
            print("Walka zakończona.")

    def avoiding_snake(self, snake, money,mana):
        print(f"Omijasz {snake.name}a.")
        print("Podróż jest bezpieczna, ale zajmuje trochę więcej czasu.")
        print("Tracisz",money ,"pieniedzy i", mana,"many za podróż inną drogą.")
        
        self.hero.mana -= mana
        self.hero.money -= money
        print(f"Aktualny stan zlota: {self.hero.money}")
        print(f"Aktualny stan many: {self.hero.mana}")

    def encounter_bear(self):
        bear_name = input("Podaj imię misia: ")
        bear = Bear(bear_name,)

        print(f"Podczas swojej przygody do królestwa natrafiasz na ostatniego potwora misia o imieniu {bear.name}!")
        money = randint(40, 60)  
        attack = randint(30, 50)

        print("Co chcesz zrobić?")
        print(f"1. Walczyć z {bear_name}em i dostać nagrodę.")
        print(f"2. Ominąć {bear_name}a i stracić {money} pieniędzy.")

        decision = input("Wybierz opcję: ")

        if decision == "1":
            self.battle_bear(bear,attack,money)
        elif decision == "2":
                self.avoiding_bear(bear,money,)
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            self.encounter_bear()
    
    def battle_bear(self,bear,attack,money):
        for _ in range(3):
            print(f"Rozpoczynasz walkę z {bear.name}em !")
            hero_damage = randint(self.hero.attack // 2, self.hero.attack)
            bear_damage = randint(bear.attack_power // 2, bear.attack_power)

            print(f"Atakujesz {bear.name}a i zadajesz mu {hero_damage} obrażeń.")
            bear.life -= hero_damage

            if bear.life <= 0:
                print(f"Gratulacje! Pokonałeś {bear.name}a, dostajesz {attack} punktów ataku i {money} pieniedzy.")
                self.hero.attack += attack
                self.hero.money += money
                print(f"Aktualny stan zlota: {self.hero.money}")
                print(f"Aktualny stan punktów ataku: {self.hero.attack}")
                return

            print(f"{bear.name} kontratakuje i zadaje ci {bear_damage} obrażeń.")
            self.hero.life -= bear_damage

            if self.hero.life <= 0:
                print(f"Zostałeś pokonany przez {bear.name}a. Koniec gry.")
                return
            
            print(f"Aktualny stan życia {bear.name}a: {bear.life}")
            print(f"Aktualny stan  życia {self.name}a : {self.hero.life}")
            
            print("Walka zakończona.")
    
    def avoiding_bear(self,bear,money):
        print(f"Omijasz {bear.name}a.")
        print("Podróż jest bezpieczna, ale zajmuje trochę więcej czasu.")
        print("Tracisz",money ,"pieniedzy.")
          
        self.hero.money -= money
        
        print(f"Aktualny stan zlota: {self.hero.money}")
    
    def go_dangerous_way(self):
        print("Ominałes biedaka.")
        print("Idziesz niebezpieczną drogą do królestwa przez co masz wiecej walk. ")

        self.encounter_big_spider()
        self.encounter_deer()
        self.encounter_sigma()
        self.final_battle()

    def encounter_big_spider(self):
        spider_name = input("Podaj imię pająka: ")
        spider = Spider(spider_name,)
        
        print(f"Podczas swojej przygody do królestwa wchodzisz do jaskini gdzie jest duzy pająk o imieniu {spider.name}!")

        attack = randint(30,50)  
        money = randint(10,16)
        print("Co chcesz zrobić?")
        print(f"1. Walczyć z {spider_name}em i dostać nagrodę.")
        print(f"2. Uciec przed {spider_name}em i stracić {money} pieniędzy.")

        decision = input("Wybierz opcję: ")

        if decision == "1":
            self.battle_spider(spider,attack)
        elif decision == "2":
            self.escape_spider(spider,money)
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            self.encounter_big_spider()
    
    def battle_spider(self,spider,attack):
        for _ in range(4):
            print(f"Rozpoczynasz walkę z {spider.name}em !")
            hero_damage = randint(self.hero.attack // 2, self.hero.attack)
            spider_damage = randint(spider.attack_power // 2, spider.attack_power)
            
            print(f"Atakujesz {spider.name}a i zadajesz mu {hero_damage} obrażeń.")
            spider.life -= hero_damage

            if spider.life <= 0:
                print(f"Gratulacje! Pokonałeś {spider.name}a, dostajesz {attack} punktów ataku .")
                self.hero.attack += attack
                print(f"Aktualny stan punktów ataku: {self.hero.attack}")
                return
            
            print(f"{spider.name} kontratakuje i zadaje ci {spider_damage} obrażeń.")
            self.hero.life -= spider_damage

            if self.hero.life <= 0:
                print(f"Zostałeś pokonany przez {spider.name}a. Koniec gry.")
                return
            
            print(f"Aktualny stan życia {spider.name}a: {spider.life}")
            print(f"Aktualny stan  życia {self.name}a : {self.hero.life}")
            
            print("Walka zakończona.")
    
    def escape_spider(self,spider,money):
        print(f"Uciekasz z jaskini przed {spider.name}em.")
        print(f"Podczas ucieczki tracisz", money ,"pieniedzy.")

        self.hero.money -= money
        
        print(f"Aktualny stan zlota: {self.hero.money}")

    def encounter_deer(self):
        deer_name = input("Podaj imię jelenia: ")
        deer = Deer(deer_name,)

        print(f"Podczas swojej przygody do królestwa wchodzisz do lasu i trafiasz na jelenia o imieniu {deer.name}!")

        money = randint(40, 60)  
        defense = randint(30, 50)
        life = randint(40, 60)
        
        print("Co chcesz zrobić?")
        print(f"1. Walczyć z {deer_name}em i dostać nagrodę.")
        print(f"2. Dać mu pieniadze i stracić {money} pieniędzy.")

        decision = input("Wybierz opcję: ")

        if decision == "1":
            self.battle_deer(deer,defense,life)
        elif decision == "2":
            self.give_money_deer(deer,money)
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            self.encounter_deer()
    
    def battle_deer(self,deer,defense,life):
        for _ in range(5):
            print(f"Rozpoczynasz walkę z {deer.name}em !")
            hero_damage = randint(self.hero.attack // 2, self.hero.attack)
            deer_damage = randint(deer.attack_power // 2, deer.attack_power)
            
            print(f"Atakujesz {deer.name}a i zadajesz mu {hero_damage} obrażeń.")
            deer.life -= hero_damage

            if deer.life <= 0:
                print(f"Gratulacje! Pokonałeś {deer.name}a, dostajesz {life} punktów ataku i {defense} punktów obrony .")
                self.hero.life += life
                self.hero.defense += defense
                print(f"Aktualny stan punktów ataku: {self.hero.attack}")
                return
            
            print(f"{deer.name} kontratakuje i zadaje ci {deer_damage} obrażeń.")
            self.hero.life -= deer_damage

            if self.hero.life <= 0:
                print(f"Zostałeś pokonany przez {deer.name}a. Koniec gry.")
                return
            
            print(f"Aktualny stan życia {deer.name}a: {deer.life}")
            print(f"Aktualny stan  życia {self.name}a : {self.hero.life}")
            
            print("Walka zakończona.")
    
    def give_money_deer(self,deer,money):
        print(f"Dajesz pieniadze {deer.name}owi i tracisz.", money,"pieniedzy")
        
        self.hero.money -= money

        print(f"Aktualny stan zlota: {self.hero.money}")


    def encounter_sigma(self):
        sigma_name = input("Podaj imię sigmy: ")
        sigma = Sigma(sigma_name,)

        print(f"Podczas swojej przygody do królestwa trafiasz na ostatniego bossa o imieniu {sigma.name}!")

        money = randint(40, 60)  
        mana = randint(20, 50)
        life = randint(40, 60)
        
        print("Co chcesz zrobić?")
        print(f"1. Walczyć z {sigma_name}em i dostać nagrodę.")
        print(f"2. Zaproponować silownie sigmie")
    
        decision = input("Wybierz opcję: ")

        if decision == "1":
            self.battle_sigma(sigma,mana,life)
        elif decision == "2":
            self.go_gym_with_sigma(sigma,money,mana,life)
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            self.encounter_sigma()

    def battle_sigma(self,sigma,mana,life):
        for _ in range(3):
            print(f"Rozpoczynasz walkę z {sigma.name}em !")
            hero_damage = randint(self.hero.attack // 2, self.hero.attack)
            sigma_damage = randint(sigma.attack_power // 2, sigma.attack_power)

            print(f"Atakujesz {sigma.name}a i zadajesz mu {hero_damage} obrażeń.")
            sigma.life -= hero_damage

            if sigma.life <= 0:
                print(f"Gratulacje! Pokonałeś {sigma.name}a, dostajesz {life} punktów zycia i {mana} many.")
                self.hero.life += life
                self.hero.mana += mana
                print(f"Aktualny stan punktów życia: {self.hero.life}")
                print(f"Aktualny stan many: {self.hero.mana}")
                return
            
            print(f"{sigma.name} kontratakuje i zadaje ci {sigma_damage} obrażeń.")
            self.hero.life -= sigma_damage

            if self.hero.life <= 0:
                print(f"Zostałeś pokonany przez {sigma.name}a. Koniec gry.")
                return
            
            print(f"Aktualny stan życia {sigma.name}a: {sigma.life}")
            print(f"Aktualny stan  życia {self.name}a : {self.hero.life}")

            print("Walka zakończona.")
        
    def go_gym_with_sigma(self,sigma,money,mana,life):
        print(f"Proponujesz  silownie  {sigma.name}owi.")

        success_chance = randint(1, 10)
        if success_chance > 5:
            print(f"Udało ci się przekonac {sigma.name}a ! Idziesz z nim na silownie i tracisz", money,"pieniedzy")
            self.hero.money -= money
            print(f"Aktualny stan  pieniedzy {self.name}a : {self.hero.money}")
        else:
            print(f"Twoja prośba zostala odrzucona ! Musisz walczyć z {sigma.name}em.")
            self.battle_sigma(sigma,mana,life)

    def final_battle(self):
        print("Ostateczna walka, stajesz naprzeciwko Wielkiego demona!")
        
        demon_name = input("Podaj imię demona: ")
        demon = Demon(demon_name,)

        for _ in range(3):
            print(f"Rozpoczynasz walkę z {demon.name}em !")
            hero_damage = randint(self.hero.attack // 2, self.hero.attack)
            demon_damage = randint(demon.attack_power // 2, demon.attack_power)

            print(f"Atakujesz {demon.name}a i zadajesz mu {hero_damage} obrażeń.")
            demon.life -= hero_damage

            if demon.life <= 0:
                print(f"Gratulacje! Pokonałeś {demon.name}a i wygrałeś grę!")                
                
                print(f"Końcowy stan punktów życia: {self.hero.life}")
                print(f"Końcowy stan many: {self.hero.mana}")
                print(f"Końcowy stan punktów ataku: {self.hero.attack}")
                print(f"Końcowy stan punktów obrony: {self.hero.defense}")
                print(f"Końcowy stan pieniedzy: {self.hero.money}")
                return
            
            print(f"{demon.name} kontratakuje i zadaje ci {demon_damage} obrażeń.")
            self.hero.life -= demon_damage

            if self.hero.life <= 0:
                print(f"Zostałeś pokonany przez {demon.name}a. Koniec gry.")
                return


    
game = Game()
game.start()
