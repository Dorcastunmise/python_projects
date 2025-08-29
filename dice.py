import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4: # e.g 1 <= 2 <= 4
            break
        else:
            print("Players have to be between 2 and 4.")
            continue
    else:
        print("Invalid input. Please enter a number between 2 and 4.")


max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for each_player in range(players):
        print(f"\nPlayer {each_player + 1}'s turn")
        print(f"Your current score is {player_scores[each_player]}\n")

        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y/n)? ").strip().lower()
            if should_roll != 'y':
                break

            value = roll()
            if value == 1:
                print("Rolled a 1! No points this round.")
                current_score = 0
                break
            else:
                current_score += value
                print("Yay! You rolled a", value)
            print(f"Your current score is {current_score}") 

        player_scores[each_player] += current_score   
        print(f"Your total score is {player_scores[each_player]}")

max_score = max(player_scores)
winner = player_scores.index(max_score) + 1
print(f"\nPlayer {winner} wins with a score of {max_score}!")