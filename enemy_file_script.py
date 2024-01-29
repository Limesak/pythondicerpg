# This script allows us to create different enemies and give them stats

import random
from spells_description_file_script import *

class EnemyDescription:    
    def __init__(self, name, health, armor, action_points):
        self.name = name
        self.health = health
        self.armor = armor
        self.action_points = action_points

orc = dict(name = "Orc", health = 12, armor = 8, action_points = 7)
troll = dict(name = "Troll", health = 15, armor = 9, action_points = 5)
wolf = dict(name = "Wolf", health = 7, armor = 4, action_points = 3)

list_of_enemies = [orc, troll, wolf]

def enemy_choose_spell(participant):
    spells_to_choose_from = [slash, slam]
    available_spells = []
    for spell in spells_to_choose_from:
        if participant.action_points >= spell.cost:
            available_spells.append(spell)
    chosen_spell = random.choice(available_spells)
    return chosen_spell
