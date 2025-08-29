print("Welcome to the Quiz Game!")

playing = input("Do you want to play? (yes/no): ").strip().capitalize()
if playing != "Yes":
    print("Okay, maybe next time!")
    quit()
print("Great! Let's start the game.")

score = 0
capital = input("What is the capital of France? ").strip().capitalize()
if capital == "Paris":
    print("Correct!")
    score += 1
elif capital == "":
    print("No answer provided. The capital of France is Paris.")
    print("Game Over!")
    quit()
else:
    print("Wrong answer. The capital of France is Paris.")

technical_qstn = input("What does CPU stand for? ").strip().upper()
if technical_qstn == "CENTRAL PROCESSING UNIT":
    print("Correct!")
    score += 1
elif technical_qstn == "":
    print("No answer provided. CPU stands for Central Processing Unit.")
    print("Game Over!")
    quit()
else:
    print("Wrong answer. CPU stands for Central Processing Unit.")

python_qstn = input("What programming language is this game written in? ").strip().capitalize()
if python_qstn == "Python":
    print("Correct!")
    score += 1
elif python_qstn == "":
    print("No answer provided. This game is written in Python.")
    print("Game Over!")
    quit()
else:
    print("Wrong answer. This game is written in Python.")

nigeria_qstn = input("What is the capital of Nigeria? ").strip().capitalize()
if nigeria_qstn == "Abuja":
    print("Correct!")
    score += 1
elif nigeria_qstn == "":
    print("No answer provided. The capital of Nigeria is Abuja.")
    print("Game Over!")
    quit()
else:
    print("Wrong answer. The capital of Nigeria is Abuja.")


medical_qstn = input("What is the medical term for high blood pressure? ").strip().capitalize()
if medical_qstn == "Hypertension":
    print("Correct!")
    score += 1
elif medical_qstn == "":
    print("No answer provided. The medical term for high blood pressure is Hypertension.")
    print("Game Over!")
    quit()
else:
    print("Wrong answer. The medical term for high blood pressure is Hypertension.")

print("Congratulations! You've completed the quiz. Your score is: " + str((score/5) * 100) + "%")