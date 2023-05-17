"""03_difficulty_v2.
Changed difficulty component to not be a function, so it can work with and link to the main game."""


# Main routine for difficulty
difficulty = input("What difficulty would you like to play?"
                   "\n(Please answer 'easy', 'medium', or 'hard'): ").lower()

# If user answers easy
if difficulty == "easy":
    print("\nDifficulty: easy.\n")
elif difficulty == "medium":
    print("\nDifficulty: medium.\n")
# If user answers hard
elif difficulty == "hard":
    print("\nDifficulty: hard.\n")
# If user answers anything, difficulty will be automatically set to easy
else:
    print("\nDifficulty has been automatically been set to easy.\n")
input("Press <enter> to play!\n")
