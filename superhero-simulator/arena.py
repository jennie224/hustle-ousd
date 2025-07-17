
# arena.py Jennie Cruz

from hero import Hero
from ability import Ability
from armor import Armor

def main():
    # Create some abilities
    fireball = Ability("Fireball", 50)
    lightning_strike = Ability("Lightning Strike", 70)

    # Create some armors
    shield = Armor("Shield", 30)
    armor_plate = Armor("Armor Plate", 40)

    # Create heroes
    hero1 = Hero("Grace Hopper", 200)
    hero2 = Hero("Alan Turing", 200)

    # Add abilities to heroes
    hero1.add_ability(fireball)
    hero1.add_ability(lightning_strike)
    
    hero2.add_ability(fireball)

    # Add armor to heroes
    hero1.add_armor(shield)
    hero2.add_armor(armor_plate)

    # Print initial stats
    print(f"{hero1.name} Health: {hero1.current_health}")
    print(f"{hero2.name} Health: {hero2.current_health}")

    # Hero1 attacks hero2
    hero1_attack = hero1.sum_of_attacks()
    print(f"{hero1.name} attacks with a total damage of {hero1_attack}")

    # Hero2 defends
    hero2_defense = hero2.defend()
    print(f"{hero2.name} defends with a total block of {hero2_defense}")

    # Print the final battle result
    final_damage = hero1_attack - hero2_defense
    hero2.current_health -= max(final_damage, 0)
    print(f"{hero2.name}'s Health after attack: {hero2.current_health}")

    # Determine the winner
    if hero2.current_health <= 0:
        print(f"{hero1.name} wins the battle!")
    else:
        print(f"{hero2.name} is still standing!")

    # Battle between two heroes (randomized winner)
    hero1.battle(hero2)

if __name__ == "__main__":
    main()