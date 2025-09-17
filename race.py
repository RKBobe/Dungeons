# race.py

class Race:
    def __init__(self, name, attribute_modifiers, special_abilities):
        self.name = name
        # attribute_modifiers will be a dictionary, e.g., {'constitution': 2, 'strength': 1}
        self.attribute_modifiers = attribute_modifiers
        # special_abilities will be a list of strings
        self.special_abilities = special_abilities

# A dictionary to hold all predefined races
RACES = {
    "dwarf": Race(
        name="Dwarf",
        attribute_modifiers={"constitution": 2},
        special_abilities=["Darkvision", "Dwarven Resilience", "Stonecunning"]
    ),
    "elf": Race(
        name="Elf",
        attribute_modifiers={"dexterity": 2},
        special_abilities=["Darkvision", "Fey Ancestry", "Trance"]
    ),
    "human": Race(
        name="Human",
        attribute_modifiers={
            "strength": 1, "dexterity": 1, "constitution": 1,
            "intelligence": 1, "wisdom": 1, "charisma": 1
        },
        special_abilities=["Versatile", "Skilled"]
    )
}