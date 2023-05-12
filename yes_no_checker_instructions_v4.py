"""yes_no_checker_instructions_v4.
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
            print("What difficulty would you like to play?: ")
            break

        # If they say no, output 'Display Instructions'
        elif answer == "no" or answer == "n":
            print("This Maori quiz will test your knowledge on numbers in Maori."
                  "\nFirst, choose a difficulty. Difficulties range from:\n")
            break
        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'.")
    return ()


# Main routine
show_instructions = yes_no("Have you played this game before?: ")
