# combat_engine.py
import time

def run_combat_encounter(player, monster):
    """
    Manages a turn-based combat encounter between the player and a monster.
    """
    print(f"\nA wild {monster.name} appears! Combat begins!")
    turn_counter = 1

    # The main combat loop continues as long as both are alive
    while player.is_alive() and monster.is_alive():
        print(f"\n--- Round {turn_counter} ---")

        # Player's turn
        print(f"{player.name}'s turn.")
        player.attack(monster)
        if not monster.is_alive():
            break # End combat if monster is defeated
        
        time.sleep(1) # Pause for readability

        # Monster's turn
        print(f"\n{monster.name}'s turn.")
        monster.attack(player)
        if not player.is_alive():
            break # End combat if player is defeated

        time.sleep(1) # Pause for readability
        turn_counter += 1

    # --- End of Combat ---
    print("\n--- Combat Over ---")
    if player.is_alive():
        print(f"Congratulations! {player.name} defeated the {monster.name}!")
    else:
        print(f"{player.name} was defeated. Game Over.")