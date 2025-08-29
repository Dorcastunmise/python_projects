name  = input("Type your name: ").strip().capitalize()
print(f"Welcome to the adventure, {name}!")

qstn = input("You find yourself at a crossroads. Do you want to go straight, left or right? (Straight/Left/Right): ").strip().lower()

if qstn == "left":
    river = input("You encounter a river. Do you want to swim across or build a raft? (Swim/Raft): ").strip().lower()
    if river == "swim":
        print("You chose to swim across the river. You are now safely on the other side.")
    elif river == "raft":
        print("You chose to build a raft. Raft is not strong enough, wood is too weak!")
    else:
        print("Invalid choice. Please choose Swim or Raft.")
elif qstn == "right":
    space = input("You find a spaceship. Do you want to enter or walk away? (Enter/Walk): ").strip().lower()
    if space == "enter":
        print("You entered the spaceship and blasted off into space!")
    elif space == "walk":
        print("You chose to walk away from the spaceship. You continue your adventure on foot.")
    else:
        print("Invalid choice. Please choose Enter or Walk.")
elif qstn == "straight":
    life = input("You see a mysterious cave. Do you want to enter or go back? (Enter/Back): ").strip().lower()
    if life == "enter":
        print("You entered the cave and found a treasure! Congratulations!")
    elif life == "back":
        print("You chose to go back. You ended your adventure.")
    else:
        print("Invalid choice. Please choose Enter or Back.")
else:
    print("Invalid choice. Please choose Straight, Left or Right.")