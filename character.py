# character.py
from attributes import Attributes
from character_class import CharacterClass
from race import Race
from dice import roll # Import the roll function
from weapon import Weapon # Import the new Weapon class

class PlayerCharacter:
  """The player's character, composed of other objects."""
  def __init__(self, name, race, attributes, character_class):
    self.name = name
    self.race = race
    self.attributes = attributes
    self.character_class = character_class

    # -- HP Calculation --
    con_modifier = (self.attributes.constitution - 10) // 2
    self.max_hp = self.character_class.hit_die + con_modifier
    self.current_hp = self.max_hp

    # -- Proficiencies & Abilities --
    self.saving_throws = character_class.saving_throws
    self.armor_proficiencies = character_class.armor_proficiencies
    self.weapon_proficiencies = character_class.weapon_proficiencies
    self.special_abilities = race.special_abilities
    self.skills = []

    # -- Equipment -- (NEW)
    self.inventory = []
    self.equipped_weapon = None


  def take_damage(self, amount):
    """Reduces the character's HP by a given amount."""
    self.current_hp -= amount
    if self.current_hp < 0:
        self.current_hp = 0
    print(f"{self.name} takes {amount} damage! Current HP: {self.current_hp}/{self.max_hp}")


  def attack(self, target):
    """Performs an attack against a target."""
    if not self.equipped_weapon:
        print(f"{self.name} has no weapon equipped and cannot attack!")
        return

    print(f"{self.name} attacks {target.name} with a {self.equipped_weapon.name}!")
    
    # --- Attack Roll (To-Hit) ---
    # For now, we assume all melee attacks use Strength.
    str_modifier = (self.attributes.strength - 10) // 2
    attack_roll = roll(20)

    # Simplified "To-Hit" logic: We'll add Armor Class (AC) later.
    # For now, a roll of 10+ hits.
    if attack_roll + str_modifier >= 10:
        print(f"Attack roll: {attack_roll} + {str_modifier} (STR mod) = {attack_roll + str_modifier}. It's a hit!")
        
        # --- Damage Roll ---
        damage_roll = roll(self.equipped_weapon.damage_dice_sides)
        total_damage = damage_roll + str_modifier
        
        # Ensure damage is at least 1
        if total_damage < 1:
            total_damage = 1

        target.take_damage(total_damage)

    else:
        print(f"Attack roll: {attack_roll} + {str_modifier} (STR mod) = {attack_roll + str_modifier}. A miss!")


  def __str__(self):
    attrs = self.attributes
    weapon_name = self.equipped_weapon.name if self.equipped_weapon else "None"
    return (
      f"Name: {self.name}\n"
      f"Race: {self.race.name}, Class: {self.character_class.name}\n"
      f"HP: {self.current_hp}/{self.max_hp}\n"
      f"Weapon: {weapon_name}\n" # Added this line
      f"Saving Throws: {', '.join(self.saving_throws)}\n"
      f"Skills: {', '.join(self.skills)}\n"
      f"Abilities: {', '.join(self.special_abilities)}\n"
      f"--- Attributes ---\n"
      f"STR: {attrs.strength}, DEX: {attrs.dexterity}, CON: {attrs.constitution}\n"
      f"INT: {attrs.intelligence}, WIS: {attrs.wisdom}, CHA: {attrs.charisma}"
    )

  def is_alive(self):
    """Returns True if the character's HP is above 0."""
    return self.current_hp > 0