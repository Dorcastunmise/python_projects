with open("story.txt", "r") as f:   # Opening the file "story.txt" in read mode and storing it as f
    story = f.read()                # Reading the entire content of the file into the variable "story"

#words = []                          # Creating an empty list called "words" to store placeholders like <word> but there will be no unique placeholders
words = set()                       # Using a set to store unique placeholders like <word>
word_str = -1                       # Initializing a variable "word_str" with -1, marking no start index found yet

target_str = "<"                    # Setting the target start character as "<"
target_end = ">"                    # Setting the target end character as ">"

# enumerate is giving both the index (i) and the character (char) while looping through "story"
for i, char in enumerate(story):    
    if char == target_str:          # Checking if the current character is "<"
        word_str = i                # Storing the position of "<" in "word_str"
    
    if char == target_end and word_str != -1:  # Checking if the current character is ">" and if "<" has been found
        word = story[word_str: i + 1]          # Extracting the substring from "<" to ">" (inclusive)
        words.add(word)                         # Adding the extracted placeholder (like <name>) to the set "words"
        word_str = -1                          # Resetting "word_str" back to -1 to mark search as complete


answers = {}
for word in words:
     # Prompting the user to enter a word corresponding to the placeholder (removing "<" and ">")
    answer = input(f"Enter a word for " + word + ": ") 
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])  # Replacing each placeholder in the story with the user's input

print(story)  # Printing the final story with all placeholders replaced by user inputs
