"""04_game_v1.
Includes lists that select for the game based on the users answer.
Also includes function for the game."""


import random


# Function for difficulty
def difficulty(question):
    while True:

        # Ask user what difficulty they want to play
        answer = input(question).lower()

        # If they say easy
        if answer == "easy":
            answer = easy
            break

        # If they say medium
        elif answer == "medium":
            answer = medium
            break

        # If they say hard
        elif answer == "hard":
            answer = hard
            break

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'.")

    # Print answer to user
    print(f"\nDifficulty: {answer}."
          f"\n\nPress <enter> to start!")


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


# Main routine for difficulty selection
difficulty("What difficulty would you like to play? "
           "\n(Please answer 'easy', 'medium', or 'hard'): ")


# Main routine for game
def game(game_answer):
    if difficulty is easy:
        for i in easy:
            game_answer = input(f"What is {i[0]} in Maori?: ")
            if game_answer == i[1]:
                print("Correct")

    if difficulty is medium:
        for i in easy:
            game_answer = input(f"What is {i[0]} in Maori?: ")
            if game_answer == i[1]:
                print("Correct")

    if difficulty is hard:
        for i in easy:
            game_answer = input(f"What is {i[0]} in Maori?: ")
            if game_answer == i[1]:
                print("Correct")
