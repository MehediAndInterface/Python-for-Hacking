"""
Guess the Number: Generate a random number and have the user guess it, providing "too high" or "too low" hints.

# 1. Set up the game variables
# 2. Use a 'for' loop to limit the guesses
# 3. This 'else' block runs ONLY if the 'for' loop completes without a 'break'
"""
import random


secret_number = random.randint(1, 100)
max_guesses = 5
print(f"I'm thinking of a number between 1 and 100.")
print(f"You have {max_guesses} chances to guess it.")


for guess_count in range(1, max_guesses + 1):
    try:
        guess = int(input(f"Guess #{guess_count}: "))

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 You got it in {guess_count} guesses! The number was {secret_number}.")
            break

    except ValueError:
        print("Oops! Please enter a valid number.")

else:
    print("\nSorry, you've run out of guesses!")
    print(f"The number I was thinking of was {secret_number}.")

