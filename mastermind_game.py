import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_code():
    while True:
        print(f" R : Red\n G : Green\n B : Blue\n Y : Yellow\n W : White\n O : Orange\n")
        guess = input("Guess a color between R, G, B, Y, W, O: ").upper().split(" ") #this returns a list

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            break #breaks entirely out of the while loop

    return guess
            

def check_code(guess, real_code):
    color_counts = {}   # Creating a dictionary to count occurrences of each color in the real code
    correct_pos = 0   # Initializing the number of correct positions
    incorrect_pos = 0   # Initializing the number of incorrect positions

    for color in real_code:   # Iterating through each color in the real code
        if color not in color_counts:   # Checking if the color is not yet in the dictionary
            color_counts[color] = 0   # Initializing its count
        color_counts[color] += 1   # Increasing the count for the color

    for guess_color, real_color in zip(guess, real_code):   
        # Iterating through pairs of guessed and real colors
        if guess_color == real_color:   # Checking if the guess is in the correct position
            correct_pos += 1   # Increasing correct position count
            color_counts[guess_color] -= 1   # Reducing the available count of that color

    for guess_color, real_color in zip(guess, real_code):   
        # Iterating again through pairs of guessed and real colors
        if guess_color in color_counts and color_counts[guess_color] > 0:   
            # Checking if the guess color is still available in the dictionary
            incorrect_pos += 1   # Increasing incorrect position count
            color_counts[guess_color] -= 1   # Reducing the count for that color

    return correct_pos, incorrect_pos   # Returning the counts of correct and incorrect positions

def game():
    print(f"Welcome to Mastermind, you have {TRIES} tries to guess the code...")
    print(f"The valid colors are", *COLORS)
    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")

    else:
        print(f"You ran out of tries. The code was: {code}")

if __name__ == "__main__":
    game()
    






