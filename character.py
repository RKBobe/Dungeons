# character.py
from attributes import Attributes
from character_class import CharacterClass

class PlayerCharacter:
  """The player's character, composed of other objects."""
  def __init__(self, name, attributes, character_class):
    self.name = name
    self.attributes = attributes
    self.character_class = character_class

    # Calculate HP
    con_modifier = (self.attributes.constitution - 10) // 2
    self.max_hp = self.character_class.hit_die + con_modifier
    self.current_hp = self.max_hp

    # Copy proficiencies from the chosen class
    self.saving_throws = character_class.saving_throws
    self.armor_proficiencies = character_class.armor_proficiencies
    self.weapon_proficiencies = character_class.weapon_proficiencies

    # We will handle choosing skills in a later step
    self.skills = []


  def __str__(self):
    attrs = self.attributes
    return (
      f"Name: {self.name}\n"
      f"Class: {self.character_class.name}\n"
      f"HP: {self.current_hp}/{self.max_hp}\n"
      f"Saving Throws: {', '.join(self.saving_throws)}\n"
      f"--- Attributes ---\n"
      f"STR: {attrs.strength}, DEX: {attrs.dexterity}, CON: {attrs.constitution}\n"
      f"INT: {attrs.intelligence}, WIS: {attrs.wisdom}, CHA: {attrs.charisma}"
    )

  def is_alive(self):
    """Returns True if the character's HP is above 0."""
    return self.current_hp > 0