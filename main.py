# main.py
from character import PlayerCharacter
from attributes import Attributes
from attribute_generator import run_generator

def main():
  """Main function to run the game."""
  print("Welcome to your D&D character creator!")
  
  # Run the interactive attribute generator
  scores = run_generator()
  
  # For now, we'll auto-assign them. We can let the player assign them later.
  # We'll also add the other 3 attributes to the class.
  player_attrs = Attributes(
    strength=scores[0],
    dexterity=scores[1],
    constitution=scores[2],
    intelligence=scores[3], # We'll uncomment these once we add them
    wisdom=scores[4],
    charisma=scores[5]
  )
  
  # NOTE: We need to update the Attributes and PlayerCharacter classes
  # to handle all 6 attributes to make this fully work.
  # For now, this demonstrates the system.
  
  player = PlayerCharacter(name="Valerius", hp=25, attributes=player_attrs)
  
  print("\n--- Your Character Has Been Created ---")
  print(player)


if __name__ == "__main__":
  main()