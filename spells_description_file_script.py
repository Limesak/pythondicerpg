# This script allows us to create different spells and give them stats

class SpellDescription:
    def __init__(self, name, required_strength, required_wisdom, power, cost):
        self.name = name
        self.required_strength = required_strength
        self.required_wisdom = required_wisdom
        self.power = power
        self.cost = cost

fireball = SpellDescription("Fireball", 0, 12, 7, 3)
slash = SpellDescription("Slash", 6, 0, 5, 2)
slam = SpellDescription("Slam", 15, 0, 10, 4)
dark_ritual = SpellDescription("Dark Ritual", 5, 15, 20, 7)
heroic_bash = SpellDescription("Heroic Bash", 15, 5, 20, 7)

list_of_spells = {
    fireball,
    slash,
    slam,
    dark_ritual,
    heroic_bash
}
