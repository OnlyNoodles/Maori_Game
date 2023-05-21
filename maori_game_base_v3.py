"""maori_game_base_v3.
Updated my code so that users can use numbers to choose difficulties.
I made sure to keep the spelling fix in 'whitu'.
Also, I deleted the print question statement in the Yes/No checker component
after yes since the same question is asked afterwards.
This is the final version of my program."""


import random


# Welcome Message
print("--- Welcome to the Beginners Maori Number Quiz ---")
# Ask for name
name = input("\nPlease enter your name: ")
# Combine welcome message and name
print(f"\nWelcome to the Beginners Maori Number Quiz, {name}!")


# Function for 'yes' or 'no' checker
def yes_no(question):
    while True:

        # Ask user if they've played before
        answer = input(question).lower()

        # If they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            break

        # If they say no, show instructions
        elif answer == "no" or answer == "n":
            print("\n---Instructions---"
                  "\n\nThis Maori quiz will test your knowledge on numbers in Maori."
                  "\nFirst, choose a difficulty. Difficulties range from:"
                  "\n\n1. Easy (Numbers 1 - 10)."
                  "\n2. Medium (Numbers 11 - 20)."
                  "\n3. Hard (Numbers 21 - 30)."
                  "\n\nSecondly, once you enter a difficulty, "
                  "the program will tell you what difficulty you have chosen."
                  "Answering anything besides the answers in the "
                  "\napostrophes will automatically set the difficulty to 'easy'"
                  "\nRemember this, you don't need macrons when answering questions."
                  "\nThen, press 'enter' to start the game!")
            break
        # Otherwise - show error
        else:
            print("\nPlease answer 'yes' or 'no'.")
    return ()


# Main routine for Yes/No Checker
show_instructions = yes_no("\nHave you played this game before? "
                           "\n(Please answer 'yes' or 'no'): ")


# Difficulty lists
easy = [["1", "tahi"], ["2", "rua"],
        ["3", "toru"], ["4", "wha"],
        ["5", "rima"], ["6", "ono"],
        ["7", "whitu"], ["8", "waru"],
        ["9", "iwa"], ["10", "tekau"]]
medium = [["11", "tekau ma tahi"], ["12", "tekau ma rua"],
          ["13", "tekau ma toru"], ["14", "tekau ma wha"],
          ["15", "tekau ma rima"], ["16", "tekau ma ono"],
          ["17", "tekau ma whitu"], ["18", "tekau ma waru"],
          ["19", "tekau ma iwa"], ["20", "rua tekau"]]
hard = [["21", "rua tekau ma tahi"], ["22", "rua tekau ma rua"],
        ["23", "rua tekau ma toru"], ["24", "rua tekau ma wha"],
        ["25", "rua tekau ma rima"], ["26", "rua tekau ma ono"],
        ["27", "rua tekau ma whitu"], ["28", "rua tekau ma waru"],
        ["29", "rua tekau ma iwa"], ["30", "toru tekau"]]


# Main routine for difficulty
difficulty = input("\nWhat difficulty would you like to play?: ").lower()

# If user answers easy
if difficulty == "easy" or difficulty == "1":
    # Select the 'easy' list for the game
    difficulty_choice = easy
    # Print answer to user
    print("\nDifficulty: easy.\n")
# If user answers medium
elif difficulty == "medium" or difficulty == "2":
    # Select the 'medium' list for the game
    difficulty_choice = medium
    # Print answer to user
    print("\nDifficulty: medium.\n")
# If user answers hard
elif difficulty == "hard" or difficulty == "3":
    # Select the 'hard' list for the game
    difficulty_choice = hard
    # Print answer to user
    print("\nDifficulty: hard.\n")
# If user answers anything, difficulty will be automatically set to easy
else:
    difficulty_choice = easy
    print("\nDifficulty has been automatically been set to easy.\n")
input("Press <enter> to play!\n")


# Main routine for game
random.shuffle(difficulty_choice)


# Starts the user from 0 right questions
correct = 0


for i in difficulty_choice:
    # Ask the question
    game_answer = input(f"What is {i[0]} in Maori?: ").lower()
    if game_answer == i[1]:
        # Tell the user they answered correctly
        print("\nCorrect\n")
        # Add a value of 1 to 'correct' everytime the user answers correctly
        correct += 1
    else:
        # If user answers incorrectly, don't add any value to 'correct'
        # Tell the user they answered incorrectly
        print("\nIncorrect\n")
# Print results with finished 'correct' value to user
print(f"--- Results ---"
      f"\n\nYou answered {correct} out of 10 questions correctly!\n")
