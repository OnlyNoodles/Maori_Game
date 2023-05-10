"""yes_no_checker.
Asks if the user has played this quiz before."""


yes_no = input("Have you played this game before?: ")
if yes_no == "yes":
    print("What difficulty do you want to play?: ")
elif yes_no == "no" or yes_no == "n":

    print("Instructions go here")
else:
    print("Please answer 'yes' or 'no'.")
