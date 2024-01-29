# This script allows us to create different heroes and give them stats
# It also stores the current health points of heroes and the attack functions

import keyboard
from spells_description_file_script import list_of_spells

class HeroDescription:
    def __init__(self, name, health, strength, armor, wisdom, action_points):
        self.name = name
        self.health = health
        self.strength = strength
        self.armor = armor
        self.wisdom = wisdom
        self.action_points = action_points
        
viktor = HeroDescription("Viktor", 15, 15, 18, 4, 10)
xena = HeroDescription("Xena", 13, 17, 14, 5, 10)
penelope = HeroDescription("Penelope", 8, 6, 5, 18, 10)
badger = HeroDescription("Badger", 10, 9, 9, 13, 10)

hero_references = {
    viktor,
    xena,
    penelope,
    badger
}

# This function allows the player to choose an attack for their current character
def player_choose_spell(hero):
    available_spells = []
    available_spells.clear()
    for spell in list_of_spells:
        if hero.strength >= spell.required_strength and hero.wisdom >= spell.required_wisdom:
            available_spells.append(spell)
            print(f"{available_spells.index(spell) + 1} - {spell.name} - {spell.cost} AP")
    choosing = True
    while choosing is True:
        event = keyboard.read_event()
        for spell in available_spells:
            if event.name == str(available_spells.index(spell) + 1) and event.event_type == keyboard.KEY_DOWN:
                choosing = False
                return spell
