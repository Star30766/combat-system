import random

class Character:
    def __init__(self, name="Unknown", hitPoints=10, hitChance=50, maxDamage=5, armor=2):
        self._name = name
        self._hitPoints = hitPoints
        self._hitChance = hitChance
        self._maxDamage = maxDamage
        self._armor = armor

    @property
    def name(self):
        return self._name

    @property
    def hitPoints(self):
        return self._hitPoints

    @hitPoints.setter
    def hitPoints(self, value):
        self._hitPoints = value

    @property
    def hitChance(self):
        return self._hitChance

    @property
    def maxDamage(self):
        return self._maxDamage

    @property
    def armor(self):
        return self._armor

    def printStats(self):
        print(f"{self._name}\n==================")
        print(f"Hit points: {self._hitPoints}")
        print(f"Hit chance: {self._hitChance}")
        print(f"Max damage: {self._maxDamage}")
        print(f"Armor:      {self._armor}\n")

def fight(character1, character2):
    while character1.hitPoints > 0 and character2.hitPoints > 0:
        if random.randint(1, 100) <= character1.hitChance:
            damage = random.randint(1, character1.maxDamage)
            damage -= character2.armor
            damage = max(0, damage)
            character2.hitPoints -= damage
            print(f"{character1.name} hits {character2.name} for {damage} points of damage")
            print(f"{character2.name}'s armor can absorb {min(character2.armor, damage)} points")
        else:
            print(f"{character1.name} misses {character2.name}")

        if character2.hitPoints <= 0:
            print(f"{character2.name} is defeated!")
            print(f"{character1.name} wins!")
            break

        if random.randint(1, 100) <= character2.hitChance:
            damage = random.randint(1, character2.maxDamage)
            damage -= character1.armor
            damage = max(0, damage)
            character1.hitPoints -= damage
            print(f"{character2.name} hits {character1.name} for {damage} points of damage")
            print(f"{character1.name}'s armor can absorb {min(character1.armor, damage)} points")
        else:
            print(f"{character2.name} misses {character1.name}")

        if character1.hitPoints <= 0:
            print(f"{character1.name} is defeated!")
            print(f"{character2.name} wins!")
            break

