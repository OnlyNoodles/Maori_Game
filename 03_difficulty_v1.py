"""03_difficulty_v1.
Gives the user an option to choose the difficulty of the quiz.
Easy, medium, and hard are the options."""


# Function for 'yes' or 'no' checker
def difficulty(question):
    while True:

        # Ask user if they've played before
        answer = input(question).lower()

        # If they say yes, output 'Program Continues'
        if answer == "easy":
            break

        # If they say no, show instructions
        elif answer == "medium":
            break

        elif answer == "hard":
            break

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'.")
    print(f"\nYou answered {answer}.")


# Main routine
difficulty("What difficulty would you like to play? "
           "\n(Please answer 'easy', 'medium', or 'hard'): ")

# Kavin, remember to change ur code to one difficulty.
# Also, wrong = 0
# If input is wrong, +1
