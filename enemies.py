from characters import Character

class Enemy(Character):
    def __init__(self, name, life, attack_power):
        super().__init__(name, life, attack_power)

class Wolf(Enemy):
    def __init__(self, name):
        super().__init__(name, life=80, attack_power=20)

class Dragon(Enemy):
    def __init__(self, name):
        super().__init__(name, life=100, attack_power=40)

class Shark(Enemy):
    def __init__(self, name):
        super().__init__(name, life=80, attack_power=20)

class Barbarian(Enemy):
    def __init__(self, name):
        super().__init__(name, life=60, attack_power=20)

class Scorpio(Enemy):
    def __init__(self, name):
        super().__init__(name, life=50, attack_power=15)

class Shaman(Enemy):
    def __init__(self, name):
        super().__init__(name, life=40, attack_power=25)

class Fox(Enemy):
    def __init__(self, name):
        super().__init__(name, life=60, attack_power=15)

class Snake(Enemy):
    def __init__(self, name):
        super().__init__(name, life=100, attack_power=10)

class Bear(Enemy):
    def __init__(self, name):
        super().__init__(name, life=40, attack_power=20)

class Spider(Enemy):
    def __init__(self, name):
        super().__init__(name, life=20, attack_power=18)

class Deer(Enemy):
    def __init__(self, name):
        super().__init__(name, life=30, attack_power=9)

class Sigma(Enemy):
    def __init__(self, name):
        super().__init__(name, life=35, attack_power=22)

class Demon(Enemy):
    def __init__(self, name):
        super().__init__(name, life=50, attack_power=30)
