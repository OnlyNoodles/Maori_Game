"""02_yes_no_checker_instructions_v4.
Turned yes_no_checker_instructions_v3 into a function.
Also added a 'break' command to break the 'while' loop
when the user answers 'yes' or 'no'.
Also typed out instructions. """


# Function for 'yes' or 'no' checker
def yes_no(question):
    while True:

        # Ask user if they've played before
        answer = input(question).lower()

        # If they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            print("\nWhat difficulty would you like to play?: ")
            break

        # If they say no, show instructions
        elif answer == "no" or answer == "n":
            print("\n---Instructions---"
                  "\n\nThis Maori quiz will test your knowledge on numbers in Maori."
                  "\nFirst, choose a difficulty. Difficulties range from:"
                  "\n\n1. Beginner (Numbers 1 - 10)."
                  "\n2. Intermediate (Numbers 11 - 20)."
                  "\n3. Expert (Numbers 21 - 30)."
                  "\n\nSecondly, once you enter a number, the program will tell you what difficulty you have chosen."
                  "\nRemember this, you don't need macrons."
                  "\nThen, press 'enter' to start the game!")
            break
        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'.")
    return ()


# Main routine
show_instructions = yes_no("Have you played this game before? "
                           "\n(Please answer 'yes' or 'no'): ")
