"""04_game_v3.
Links 03_difficulty_v2 to the main game.
Also adds the lists so that the user's answer will link
and select their preferred list difficulty.
This is the version I will use in maori_game_base."""


import random


# Difficulty lists
easy = [["1", "tahi"], ["2", "rua"], ["3", "toru"], ["4", "wha"], ["5", "rima"],
        ["6", "ono"], ["7", "whetu"], ["8", "waru"], ["9", "iwa"], ["10", "tekau"]]
medium = [["11", "tekau ma tahi"], ["12", "tekau ma rua"],
          ["13", "tekau ma toru"], ["14", "tekau ma wha"],
          ["15", "tekau ma rima"], ["16", "tekau ma ono"],
          ["17", "tekau ma whetu"], ["18", "tekau ma waru"],
          ["19", "tekau ma iwa"], ["20", "rua tekau"]]
hard = [["21", "rua tekau ma tahi"], ["22", "rua tekau ma rua"],
        ["23", "rua tekau ma toru"], ["24", "rua tekau ma wha"],
        ["25", "rua tekau ma rima"], ["26", "rua tekau ma ono"],
        ["27", "rua tekau ma whetu"], ["28", "rua tekau ma waru"],
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


# Main routine for game
random.shuffle(difficulty_choice)

for i in difficulty_choice:
    game_answer = input(f"What is {i[0]} in Maori?: ").lower()
    if game_answer == i[1]:
        print("\nCorrect\n")
    else:
        print("\nIncorrect\n")
