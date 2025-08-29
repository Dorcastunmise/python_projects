import random

user_wins = 0
computer_wins = 0

options = ['Rock', 'Paper', 'Scissors']

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").strip().capitalize()
    if user_input == 'Q':
        break
    elif user_input not in ['Rock', 'Paper', 'Scissors']:
        print("Invalid input. Please try again.")
        continue
    else:
        # Rock: 0, Paper: 1, Scissors: 2
        random_number = random.randint(0, 2)
        computer_pick = options[random_number]
        print("Computer chose:", computer_pick, ".")

        if user_input == computer_pick:
            print("It's a tie!")
        elif (user_input == 'Rock' and computer_pick == 'Scissors') or \
             (user_input == 'Paper' and computer_pick == 'Rock') or \
             (user_input == 'Scissors' and computer_pick == 'Paper'):
            print("You win!")
            user_wins += 1
        else:
            print("You lose!")
            computer_wins += 1

        print("Score - You:", user_wins, "Computer:", computer_wins)

