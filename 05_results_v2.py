"""05_results.
This component shows the results of the user gameplay.
It will tell the user how many questions they answered correctly out of 10,
which is how many questions are in each list."""


import random


# Difficulty lists
easy = [["1", "tahi"], ["2", "rua"], ["3", "toru"], ["4", "wha"], ["5", "rima"],
        ["6", "ono"], ["7", "whitu"], ["8", "waru"], ["9", "iwa"], ["10", "tekau"]]
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
difficulty = input("What difficulty would you like to play?"
                   "\n(Please answer 'easy', 'medium', or 'hard'): ").lower()

# If user answers easy
if difficulty == "easy":
    # Select the 'easy' list for the game
    difficulty_choice = easy
    # Print answer to user
    print("\nDifficulty: easy.\n")
# If user answers medium
elif difficulty == "medium":
    # Select the 'medium' list for the game
    difficulty_choice = medium
    # Print answer to user
    print("\nDifficulty: medium.\n")
# If user answers hard
elif difficulty == "hard":
    # Select the 'hard' list for the game
    difficulty_choice = hard
    # Print answer to user
    print("\nDifficulty: hard.\n")
# If user answers anything, difficulty will be automatically set to easy
else:
    difficulty_choice = easy
    print("\nDifficulty has been automatically been set to easy.\n")
input("Press <enter> to play!\n")


# Starts the user from 0 right questions
correct = 0


# Main routine for game
random.shuffle(difficulty_choice)

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
# Print results to user
print(f"--- Results ---"
      f"\n\nYou answered {correct} out of 10 questions correctly!\n")
