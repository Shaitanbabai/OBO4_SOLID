# Импортируем возможность работы с абстрактным классом
from abc import ABC, abstractmethod


# Создаем класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Создаем класс меча
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом")


# Создаем класс лука
class Bow(Weapon):
    def attack(self):
        print("Боец cтреляет из лука")


# Создаем класс зубов монстра
class Teeth(Weapon):
    def attack(self):
        print("Монстр делает кусь!")


# Создаем класс бойца
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        print(self.weapon.attack())


# Создаём класс монстра
class Monster:

    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        print(self.weapon.attack())


# Создаём объекты классов оружия:
sword1 = Sword()
bow1 = Bow()
teeth1 = Teeth()

# Создаём объект класса бойца:
fighter = Fighter(sword1)
print("Oh, ty z kurwa bober! Ja perdole jakyi bydlo!")

# Создаем объект класса монстра
monster = Monster(teeth1)
print("Я твой дом труба шатал!")

# Наносим удар:
fighter.fight()
monster.fight()

# Заменяем оружие:
fighter.change_weapon(bow1)
print("Боец меняет оружие")

# Стреляем из лука:
fighter.fight()
print("Монстр повержен, а-то чо он, как этот!")
