from dice import generate_attribute_score

def create_score_grid():
    """Create a 6x6 grid of attribute scores."""
    return [[generate_attribute_score() for _ in range(6)] for _ in range(6)]

def display_grid(grid):
    """Prints grid in readable format."""
    print("\n   c0  'c1  c2  c3  c4  c5")
    print("  " + "-" * 25)
    for i, row in enumerate(grid):
        print(f"r{i} | {' '.join(f'{score:2}' for score in row)}")
    print("\nChoose a set of scores by typing its identifier ")


def get_selection(grid):
    while True:
        choice = input("Your choice: ").lower().strip()

        # Rows
        if choice.startswith('r') and len(choice) == 2 and choice[1].isdigit():
            row_index = int(choice[1])
            if 0 <= row_index < 6:
                return grid[row_index]

        # Columns   
        if choice.startswith('c') and len(choice) == 2 and choice[1].isdigit():
            col_index = int(choice[1])
            if 0 <= col_index < 6:
                return [grid[i][col_index] for i in range(6)]

        # Diagonals
        if choice == 'd1': # Main diagonal (top-left to bottom-right)
            return [grid[i][i] for i in range(6)]
        if choice == 'd2': # Anti-diagonal (top-right to bottom-left)
            return [grid[i][5 - i] for i in range(6)]
      
        print("Invalid input. Please try again (e.g., 'r0', 'c3', 'd1').")

def run_generator():
  """Runs the full attribute generation process."""
  print("--- Generating Attribute Scores ---")
  score_grid = create_score_grid()
  display_grid(score_grid)
  selected_scores = get_selection(score_grid)
  print(f"\nYou selected: {selected_scores}")
  return selected_scores