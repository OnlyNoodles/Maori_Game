"""03_difficulty_v1.
Gives the user an option to choose the difficulty of the quiz.
Easy, medium, and hard are the options."""


# Function for 'yes' or 'no' checker
def difficulty(question):
    while True:

        # Ask user if they've played before
        answer = input(question).lower()

        # If they say easy,
        if answer == "easy":
            break

        # If they say medium,
        elif answer == "medium":
            break

        # if they say hard,
        elif answer == "hard":
            break

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'.")

    # Print answer to user
    print(f"\nDifficulty: {answer}."
          f"\n\nPress <enter> to start!")


# Main routine
difficulty("What difficulty would you like to play? "
           "\n(Please answer 'easy', 'medium', or 'hard'): ")
