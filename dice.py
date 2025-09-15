# dice.py

import random

def roll(sides):
  """
  Simulates rolling a single die with a given number of sides.
  Returns an integer representing the result.
  """
  if sides <= 0:
    raise ValueError("Number of sides must be a positive integer.")
  return random.randint(1, sides)

def roll_with_modifier(sides, modifier=0):
    """
    Simulates rolling a single die and adds a modifier.
    """
    return roll(sides) + modifier

# vv-- THIS IS THE FUNCTION TO CHECK --vv
def generate_attribute_score():
  """
  Rolls 4d6, rerolls any 1s once, and returns the sum of the highest 3 dice.
  """
  # All of these lines MUST be indented like this
  rolls = []
  for _ in range(4):
    roll = random.randint(1, 6)
    if roll == 1:
      roll = random.randint(1, 6)
    rolls.append(roll)
  
  rolls.sort()
  highest_three = rolls[1:]
  
  return sum(highest_three)