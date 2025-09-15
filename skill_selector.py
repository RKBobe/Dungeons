# skill_selector.py

def run_skill_selection(player):
    """
    Manages the skill selection process for the player.
    """
    chosen_skills = []
    available_skills = player.character_class.skill_choices
    num_to_choose = player.character_class.num_skill_choices
    
    print(f"\n--- Choose {num_to_choose} Skills ---")
    
    while len(chosen_skills) < num_to_choose:
        print("\nAvailable Skills:")
        for skill in available_skills:
            # Show an 'X' next to skills already chosen
            if skill in chosen_skills:
                print(f"- [X] {skill}")
            else:
                print(f"- [ ] {skill}")
        
        prompt = f"Select a skill ({len(chosen_skills) + 1} of {num_to_choose}): "
        selection = input(prompt).strip().title() # .title() capitalizes the word correctly

        if selection not in available_skills:
            print("Invalid skill. Please choose from the list.")
        elif selection in chosen_skills:
            print(f"You have already chosen {selection}. Pick another.")
        else:
            chosen_skills.append(selection)
            print(f"'{selection}' selected.")

    return chosen_skills