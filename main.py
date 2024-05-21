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
        print("Боец делает выстрел изnлука")


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
    pass


# Создаём объекты классов оружия:
sword1 = Sword()
bow1 = Bow()


# Создаём объект класса бойца:
fighter = Fighter(sword1)

# Наносим удар:
fighter.fight()

# Заменяем оружие:
fighter.change_weapon(bow1)

# Стреляем из лука:
fighter.fight()
