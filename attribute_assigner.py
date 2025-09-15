# attribute_assigner.py

def run_assignment(scores):
    """
    Allows the player to assign their rolled scores to attributes.
    """
    attributes_to_assign = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    assigned_scores = {}
    
    # Use a copy of the scores list so we can safely remove items
    available_scores = list(scores)
    
    print("\n--- Assign Your Attribute Scores ---")
    print(f"Your rolled scores are: {available_scores}")

    for attribute in attributes_to_assign:
        while True:
            # Display remaining scores and prompt for assignment
            print(f"\nAvailable scores: {available_scores}")
            prompt = f"Which score do you want to assign to {attribute.title()}? "
            
            try:
                selection = int(input(prompt))
                if selection in available_scores:
                    # Assign the score and remove it from the available list
                    assigned_scores[attribute] = selection
                    available_scores.remove(selection)
                    break # Exit the validation loop
                else:
                    print("That score is not available. Please pick from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                
    print("\nAttribute assignment complete!")
    return assigned_scores