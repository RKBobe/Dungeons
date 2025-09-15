# character_class.py

class CharacterClass:
  """Defines the attributes of a character class."""
  def __init__(self, name, hit_die, primary_ability, saving_throws,
               armor_proficiencies, weapon_proficiencies, skill_choices, num_skill_choices):
    self.name = name
    self.hit_die = hit_die
    self.primary_ability = primary_ability
    self.saving_throws = saving_throws
    self.armor_proficiencies = armor_proficiencies
    self.weapon_proficiencies = weapon_proficiencies
    self.skill_choices = skill_choices
    self.num_skill_choices = num_skill_choices

# A dictionary to hold all the predefined classes for easy access
CLASSES = {
    "fighter": CharacterClass(
        name="Fighter", hit_die=10, primary_ability="Strength or Dexterity",
        saving_throws=["Strength", "Constitution"],
        armor_proficiencies=["All armor", "Shields"],
        weapon_proficiencies=["Simple weapons", "Martial weapons"],
        skill_choices=["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"],
        num_skill_choices=2
    ),
    "wizard": CharacterClass(
        name="Wizard", hit_die=6, primary_ability="Intelligence",
        saving_throws=["Intelligence", "Wisdom"],
        armor_proficiencies=[],
        weapon_proficiencies=["Daggers", "Darts", "Slings", "Quarterstaffs", "Light crossbows"],
        skill_choices=["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"],
        num_skill_choices=2
    ),
    "rogue": CharacterClass(
        name="Rogue", hit_die=8, primary_ability="Dexterity",
        saving_throws=["Dexterity", "Intelligence"],
        armor_proficiencies=["Light armor"],
        weapon_proficiencies=["Simple weapons", "Hand crossbows", "Longswords", "Rapiers", "Shortswords"],
        skill_choices=["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"],
        num_skill_choices=4 # Rogues get 4 skills
    ),
    "cleric": CharacterClass(
        name="Cleric", hit_die=8, primary_ability="Wisdom",
        saving_throws=["Wisdom", "Charisma"],
        armor_proficiencies=["Light armor", "Medium armor", "Shields"],
        weapon_proficiencies=["Simple weapons"],
        skill_choices=["History", "Insight", "Medicine", "Persuasion", "Religion"],
        num_skill_choices=2
    ),
    "barbarian": CharacterClass(
        name="Barbarian", hit_die=12, primary_ability="Strength",
        saving_throws=["Strength", "Constitution"],
        armor_proficiencies=["Light armor", "Medium armor", "Shields"],
        weapon_proficiencies=["Simple weapons", "Martial weapons"],
        skill_choices=["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"],
        num_skill_choices=2
    ),
    "bard": CharacterClass(
        name="Bard", hit_die=8, primary_ability="Charisma",
        saving_throws=["Dexterity", "Charisma"],
        armor_proficiencies=["Light armor"],
        weapon_proficiencies=["Simple weapons", "Hand crossbows", "Longswords", "Rapiers", "Shortswords"],
        skill_choices=["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth"],
        num_skill_choices=3 # Bards get any 3 skills
    ),
    "druid": CharacterClass(
        name="Druid", hit_die=8, primary_ability="Wisdom",
        saving_throws=["Intelligence", "Wisdom"],
        armor_proficiencies=["Light armor", "Medium armor", "Shields (non-metal)"],
        weapon_proficiencies=["Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"],
        skill_choices=["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"],
        num_skill_choices=2
    ),
    "monk": CharacterClass(
        name="Monk", hit_die=8, primary_ability="Dexterity and Wisdom",
        saving_throws=["Strength", "Dexterity"],
        armor_proficiencies=[],
        weapon_proficiencies=["Simple weapons", "Shortswords"],
        skill_choices=["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"],
        num_skill_choices=2
    ),
    "paladin": CharacterClass(
        name="Paladin", hit_die=10, primary_ability="Strength and Charisma",
        saving_throws=["Wisdom", "Charisma"],
        armor_proficiencies=["All armor", "Shields"],
        weapon_proficiencies=["Simple weapons", "Martial weapons"],
        skill_choices=["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"],
        num_skill_choices=2
    ),
    "ranger": CharacterClass(
        name="Ranger", hit_die=10, primary_ability="Dexterity and Wisdom",
        saving_throws=["Strength", "Dexterity"],
        armor_proficiencies=["Light armor", "Medium armor", "Shields"],
        weapon_proficiencies=["Simple weapons", "Martial weapons"],
        skill_choices=["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"],
        num_skill_choices=3 # Rangers get 3
    ),
    "sorcerer": CharacterClass(
        name="Sorcerer", hit_die=6, primary_ability="Charisma",
        saving_throws=["Constitution", "Charisma"],
        armor_proficiencies=[],
        weapon_proficiencies=["Daggers", "Darts", "Slings", "Quarterstaffs", "Light crossbows"],
        skill_choices=["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"],
        num_skill_choices=2
    ),
    "warlock": CharacterClass(
        name="Warlock", hit_die=8, primary_ability="Charisma",
        saving_throws=["Wisdom", "Charisma"],
        armor_proficiencies=["Light armor"],
        weapon_proficiencies=["Simple weapons"],
        skill_choices=["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"],
        num_skill_choices=2
    ),
    "artificer": CharacterClass(
        name="Artificer", hit_die=8, primary_ability="Intelligence",
        saving_throws=["Constitution", "Intelligence"],
        armor_proficiencies=["Light armor", "Medium armor", "Shields"],
        weapon_proficiencies=["Simple weapons"],
        skill_choices=["Arcana", "History", "Investigation", "Medicine", "Nature", "Perception", "Sleight of Hand"],
        num_skill_choices=2
    )
}