"""04_game_v3.
Trying another way to make the game work with difficulty options.
"""


import random


# Difficulty lists
easy = [["1", "tahi"], ["2", "rua"], ["3", "toru"], ["4", "wha"], ["5", "rima"],
        ["6", "ono"], ["7", "whetu"], ["8", "waru"], ["9", "iwa"], ["10", "tekau"]]
medium = [["11", "tekau ma ono"], ["12", "tekau ma rua"],
          ["13", "tekau ma toru"], ["14", "tekau ma wha"],
          ["15", "tekau ma rima"], ["16", "tekau ma ono"],
          ["17", "tekau ma whetu"], ["18", "tekau ma waru"],
          ["19", "tekau ma iwa"], ["20", "rua tekau"]]
hard = [["21", "rua tekau ma tahi"], ["22", "rua tekau ma rua"],
        ["23", "rua tekau ma toru"], ["24", "rua tekau ma wha"],
        ["25", "rua tekau ma rima"], ["26", "rua tekau ma ono"],
        ["27", "rua tekau ma whetu"], ["28", "rua tekau ma waru"],
        ["29", "rua tekau ma iwa"], ["30", "toru tekau"]]


# Function for difficulty question
difficulty = input("What difficulty would you like to play?"
                   "\n(Please answer 'easy', 'medium', or 'hard'): ")

# If user answers easy
if difficulty == "easy":
    # 
    difficulty_choice = easy
    print("\nDifficulty: easy.")
elif difficulty == "medium":
    difficulty_choice = medium
    print("\nDifficulty: medium.\n")
elif difficulty == "hard":
    difficulty_choice = hard
    print("\nDifficulty: hard.\n")
else:
    difficulty_choice = easy
    print("\nDifficulty has been automatically been set to easy.\n")
input("Press <enter> to play!\n")


# Main routine for game
random.shuffle(difficulty_choice)

for i in difficulty_choice:
    game_answer = input(f"What is {i[0]} in Maori?: ")
    if game_answer == i[1]:
        print("\nCorrect\n")
    else:
        print("\nIncorrect\n")
