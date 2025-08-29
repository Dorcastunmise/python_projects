import random  # importing the random module for generating random numbers
import time    # importing the time module for tracking time


OPERATORS = ['+', '-', '*']  # defining a list of possible operators for math problems
MIN_OPERAND = 3  # setting the minimum value an operand can take
MAX_OPERAND = 12  # setting the maximum value an operand can take
TOTAL_PROBLEMS = 5  # setting the total number of problems to generate

def generate_problem():  
    left = random.randint(MIN_OPERAND, MAX_OPERAND)  # picking a random number between MIN_OPERAND and MAX_OPERAND for the left operand
    right = random.randint(MIN_OPERAND, MAX_OPERAND)  # picking a random number between MIN_OPERAND and MAX_OPERAND for the right operand
    operator = random.choice(OPERATORS)  # selecting a random operator from the OPERATORS list

    expr = str(left) + ' ' + operator + ' ' + str(right)  # creating a string representation of the math expression
    answer = eval(expr)    # eval() can evaluate string expressions
    return expr + " = " + str(answer)

wrong = 0
input("Press Enter to start...")  # waiting for user input to start the quiz
print("You will be given " + str(TOTAL_PROBLEMS) + " problems to solve.")

# time.time() gets the current time in seconds since January 1, 1970 (called the "epoch").
# It gives you a floating-point number like 1724935206.4532 (seconds + fractions of a second).
time_str = time.time()

# int(time_str) turns that floating-point into an integer (drops the decimal part).
# Then we add 60, which means "60 seconds after the time we started".
# str(...) turns that number into text so it can be joined with the rest of the message.
print("You have " + str(int(time_str) + 60) + " seconds to complete the quiz.")

# for i in range(TOTAL_PROBLEMS) creates a loop that runs once for each problem.
# Example: if TOTAL_PROBLEMS = 5, then i will take values 0,1,2,3,4 (5 times).
for i in range(TOTAL_PROBLEMS): 

    # generate_problem() makes a math question and answer, like "5+3 = 8".
    # .split(' = ') cuts the string into two parts: 
    #   expr = "5+3"
    #   answer = "8"
    expr, answer = generate_problem().split(' = ')

    # while True means "repeat forever until we break out".
    # We use this so the player can retry the same question until they get it right.
    while True:  

        # input(...) shows the problem and waits for the user to type an answer.
        # str(i + 1) changes the problem number into text (since i starts at 0, we add 1).
        guess = input("\nProblem #" + str(i + 1) + ": " + expr + " = ")

        # if the guess (what the user typed) is the same as the correct answer...
        if guess == str(answer):   
            print("Correct!")   
            # break exits the while loop, moving on to the next problem
            break   

        else:
            print("Incorrect. Try again.")   
            wrong += 1   
            continue  

# after all problems, record the finishing time (same format as start time).
end_time = time.time()   

# subtract start time from end time to see how long the player took in seconds.
time_taken = round(end_time - time_str,2)   

# TOTAL_PROBLEMS - wrong gives number of correct answers.
# Put it inside str() so it prints nicely as text.
print("\nYou got " + str(TOTAL_PROBLEMS - wrong) + " out of " + str(TOTAL_PROBLEMS) + " correct.")   

# show how many seconds the player used (int() removes decimals for neatness).
print("Time taken: " + str(int(time_taken)) + " seconds.")  
