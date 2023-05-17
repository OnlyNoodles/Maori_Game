"""04_game_v4.
Tried making a loop when choosing the difficulty for the game
which would then link to the game component.
"""


import random


# Difficulty lists
# Easy list
easy = [["1", "tahi"], ["2", "rua"], ["3", "toru"], ["4", "wha"], ["5", "rima"],
        ["6", "ono"], ["7", "whetu"], ["8", "waru"], ["9", "iwa"], ["10", "tekau"]]
# Medium list
medium = [["11", "tekau ma ono"], ["12", "tekau ma rua"],
          ["13", "tekau ma toru"], ["14", "tekau ma wha"],
          ["15", "tekau ma rima"], ["16", "tekau ma ono"],
          ["17", "tekau ma whetu"], ["18", "tekau ma waru"],
          ["19", "tekau ma iwa"], ["20", "rua tekau"]]
# Hard list
hard = [["21", "rua tekau ma tahi"], ["22", "rua tekau ma rua"],
        ["23", "rua tekau ma toru"], ["24", "rua tekau ma wha"],
        ["25", "rua tekau ma rima"], ["26", "rua tekau ma ono"],
        ["27", "rua tekau ma whetu"], ["28", "rua tekau ma waru"],
        ["29", "rua tekau ma iwa"], ["30", "toru tekau"]]


difficulty = ""
while difficulty != "x":

    # Ask the user for difficulty
    difficulty = input("What difficulty would you like to play?"
                       "\n(Please answer 'easy', 'medium', or 'hard'): ").lower()

    # If they say easy
    if difficulty == "easy":
        difficulty_choice = easy
        break

    # If they say medium
    elif difficulty == "medium":
        difficulty_choice = medium
        break

    # If they say hard
    elif difficulty == "hard":
        difficulty_choice = hard
        break

    # Ask for either easy, medium, or hard
    else:
        print("Please answer easy, medium, or hard.")

# Print answer to user
print(f"\nDifficulty: {difficulty}.\n")
input("Press <enter> to play!\n")


# Function for difficulty
difficulty = input("What difficulty would you like to play?"
                   "\n(Please answer 'easy', 'medium', or 'hard'): ")


# Main routine for game
random.shuffle(difficulty_choice)

for i in difficulty_choice:
    game_answer = input(f"What is {i[0]} in Maori?: ")
    if game_answer == i[1]:
        print("Correct")
    else:
        print("Incorrect")
