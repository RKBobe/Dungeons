# main.py
from character import PlayerCharacter
from attributes import Attributes
from attribute_generator import run_generator
from attribute_assigner import run_assignment # Import the new function
from character_class import CLASSES
from skill_selector import run_skill_selection

def main():
  """Main function to run the game."""
  print("Welcome to your D&D character creator!")

  # 1. Generate Attributes from the grid
  scores = run_generator()

  # 2. Assign the chosen scores -- NEW STEP
  final_attributes = run_assignment(scores)
  
  # Create the Attributes object using the assigned scores
  # The ** operator unpacks the dictionary into keyword arguments
  # e.g., Attributes(strength=18, dexterity=15, ...)
  player_attrs = Attributes(**final_attributes)

  # 3. Choose a Class
  print("\n--- Choose your Class ---")
  for key in CLASSES:
      print(f"- {CLASSES[key].name}")

  chosen_class = None
  while not chosen_class:
      selection = input("Enter class name: ").lower().strip()
      if selection in CLASSES:
          chosen_class = CLASSES[selection]
      else:
          print("Invalid class. Please choose from the list.")

  # 4. Create the Player Character
  player = PlayerCharacter(
      name="Valerius",
      attributes=player_attrs,
      character_class=chosen_class
  )

  # 5. Choose Skills
  player.skills = run_skill_selection(player)

  # 6. Display Final Character
  print("\n--- Your Character Has Been Created ---")
  print(player)


if __name__ == "__main__":
  main()