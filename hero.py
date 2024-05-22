from characters import Character

class Hero(Character):
    def __init__(self, name, life, mana, money, attack, defense):
        super().__init__(name, life, attack)
        self.mana = mana
        self.money = money
        self.defense = defense
        self.life = life
        self.attack = attack
