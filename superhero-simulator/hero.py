
# hero.py for hero profile Jennie Cruz 

import random
from ability import Ability
from armor import Armor

# hero.py
class Hero:
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armor_list = []

    def battle(self, opponent):
        self.opponent = opponent
        '''Fight another hero and randomly declare a winner'''
        winner = random.choice([self, opponent])
        print(f"The winner is: {winner.name}")

    def add_ability(self, ability):
        self.abilities.append(ability)

    def sum_of_attacks(self):
        total_damage = 0
        for ability in self.abilities:
          total_damage += ability.attack()
        return total_damage
     
    def add_armor(self, new_armor):
        self.armor_list.append(new_armor)

    def defend(self):
        total_defense = 0
        for armor in self.armor_list:
          total_defense += armor.block()
          return total_defense

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)            # Grace Hopper
    print(my_hero.current_health)  # 200

