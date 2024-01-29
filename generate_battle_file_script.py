import random
import keyboard
from enemy_file_script import *
from hero_description_file_script import *

# This list contains all foes for a battle
foes_battlegroup = []

# Before each battle, we need to make sure the list is empty
def clear_foes_group():
    foes_battlegroup.clear

# We choose a random number of enemies to fight then add this many random enemies to the battle list 
def select_new_foes():
    clear_foes_group()
    number_of_foes = random.randint(2, 5)
    for i in range (number_of_foes):
        randomFoe = random.choice(list_of_enemies)
        newFoe = EnemyDescription(randomFoe["name"], randomFoe["health"], randomFoe["armor"], randomFoe["action_points"])
        add_foe_to_battle(newFoe)

def add_foe_to_battle(enemy):
    foes_battlegroup.append(enemy)

# This function generates a random order in which each fighter will be able to take action
def create_battle_iniative_order():
    list_battle_participants = foes_battlegroup + list(hero_references)
    random.shuffle(list_battle_participants)
    return list_battle_participants

# This function allows all fighters to target an enemy to attack
def Target(potential_targets, hero_attack):
    if hero_attack is True:
        print(f"Choose a foe to attack")
        for potential_target in potential_targets:
            print(f"{potential_targets.index(potential_target) + 1} - {potential_target.name}")

        choosing = True
        while choosing is True:
            event = keyboard.read_event()
            for potential_target in potential_targets:
                if event.name == str(potential_targets.index(potential_target) + 1) and event.event_type == keyboard.KEY_DOWN:
                    choosing = False
                    return potential_target
    else:
        hero_to_attack = random.choice(potential_targets)
        return hero_to_attack

def ApplyDamage(target_of_spell, spell_to_use):
    return 0

def RollDice():
    
    return True

    return False