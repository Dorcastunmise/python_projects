import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "cyan", "magenta"]


def get_number_of_turtles():
    racers = 0
    while True:
        racers = input("Enter the number of races (between 2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid input. Please enter a number between 2 and 10.")
            continue # Continue to the next iteration of the loop i.e the beginning of the while loop

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number out of range. Please enter a number between 2 and 10.")
        # Loop continues until a valid number is entered

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randint(1, 20) # Move each turtle a random distance between 1 and 20
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)] # Return the color of the winning turtle


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle(shape="turtle")
        racer.color(color)
        racer.left(90)
        racer.penup()        
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing Game")
    screen.bgcolor("black")

racers = get_number_of_turtles()
init_turtle()

random.shuffle(COLORS)
# Select the first 'racers' colors from the shuffled list e.g if racers = 3, colors = ["blue", "red", "green"]
colors = COLORS[:racers] 
winner = race(colors)
print(f"The winner is the {winner} turtle!")
time.sleep(5) # Pause for 5 seconds before closing the window