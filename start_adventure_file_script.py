import keyboard
from generate_battle_file_script import *
from spells_description_file_script import *

print("\
=============================================\n\
You prepare to embark on a new heroic journey\n\
=============================================\n\
\n\
\n\
\n\
Press enter to begin")

keyboard.wait("enter")

print("You're travelling with your party of heroes when, suddenly,\n\
a group of enemies are blocking your path.\n\
They attack. Prepare to battle !")

# Creates of group of enemies to fight
select_new_foes()
for foe in foes_battlegroup:
    print(f"A {foe.name} is approaching.")

# Determine intiative for all characters in the battle    
participants = create_battle_iniative_order()

## For each fighter involved in the fight, we need to print their name and basic infos
# The player will then be able to choose an attack if the fighter is a hero
while True:
    for participant in participants:
        print(f"It's {participant.name}'s turn.")
        if participant in hero_references:
            print(f"{participant.name} has {participant.action_points} AP")
            spell_to_use = player_choose_spell(participant)
            target_of_spell = Target(foes_battlegroup, True)
        else:
            spell_to_use = enemy_choose_spell(participant)
            target_of_spell = Target(list(hero_references), False)

        if RollDice() == True:
            ApplyDamage(target_of_spell, spell_to_use)
            print(f"{participant.name} used {spell_to_use.name} on {target_of_spell.name} !")
