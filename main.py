# main.py
from character import PlayerCharacter
from attributes import Attributes
from race import Race, RACES
from character_class import CharacterClass, CLASSES
from weapon import WEAPONS
from attribute_generator import run_generator
from attribute_assigner import run_assignment
from skill_selector import run_skill_selection
from combat_engine import run_combat_encounter # Import combat engine

def main():
  """Main function to run the game."""
  # --- Character Creation ---
  print("--- D&D Character Creator ---")
  scores = run_generator()
  final_attributes = run_assignment(scores)
  
  print("\n--- Choose your Race ---")
  for key in RACES: print(f"- {RACES[key].name}")
  chosen_race = None
  while not chosen_race:
      selection = input("Enter race name: ").lower().strip()
      if selection in RACES: chosen_race = RACES[selection]
      else: print("Invalid race.")
  
  for attr, mod in chosen_race.attribute_modifiers.items():
      final_attributes[attr] += mod
  
  player_attrs = Attributes(**final_attributes)
  
  print("\n--- Choose your Class ---")
  for key in CLASSES: print(f"- {CLASSES[key].name}")
  chosen_class = None
  while not chosen_class:
      selection = input("Enter class name: ").lower().strip()
      if selection in CLASSES: chosen_class = CLASSES[selection]
      else: print("Invalid class.")
  
  player = PlayerCharacter(name="Valerius", race=chosen_race, attributes=player_attrs, character_class=chosen_class)
  player.skills = run_skill_selection(player)
  
  print("\n--- Character Has Been Created ---")
  print(player)

  # --- Staging a Test Combat ---
  # 1. Equip the player
  player.equipped_weapon = WEAPONS["longsword"]
  print(f"\n{player.name} equips a {player.equipped_weapon.name}.")

  # 2. Create a monster (we can use our classes for this!)
  goblin_attrs = Attributes(strength=8, dexterity=14, constitution=10, intelligence=10, wisdom=8, charisma=8)
  goblin = PlayerCharacter(name="Goblin", race=RACES["elf"], attributes=goblin_attrs, character_class=CLASSES["rogue"])
  goblin.max_hp = 7 # Let's override some stats for a classic goblin feel
  goblin.current_hp = 7
  goblin.equipped_weapon = WEAPONS["dagger"]
  print(f"A {goblin.name} with a {goblin.equipped_weapon.name} steps out of the shadows!")

  # 3. Run the combat encounter
  run_combat_encounter(player, goblin)


if __name__ == "__main__":
  main()