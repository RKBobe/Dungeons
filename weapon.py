# weapon.py

class Weapon:
    def __init__(self, name, damage_dice_sides):
        self.name = name
        self.damage_dice_sides = damage_dice_sides # e.g., 8 for a d8, 6 for a d6

# A dictionary to hold predefined weapons for easy access
WEAPONS = {
    "longsword": Weapon(
        name="Longsword",
        damage_dice_sides=8
    ),
    "dagger": Weapon(
        name="Dagger",
        damage_dice_sides=4
    )
}