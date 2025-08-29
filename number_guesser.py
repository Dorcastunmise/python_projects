import random

# number_to_guess = random.randrange(1, 11) this will not include 11
# number_to_guess = random.randint(1, 11) this will include 11


top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

number_to_guess = random.randint(0,top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == number_to_guess:
        print("You got it!")
        break
    elif user_guess < number_to_guess:
        print("Too low.")
    else:
        print("Too high.")
    
    
print("You got it in", guesses, "guesses.")