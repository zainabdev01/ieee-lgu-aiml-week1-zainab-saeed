"""
Number Guessing Game
IEEE LGU AI/ML Cohort One - Week 1 Assignment (Option 1)
Author: Zainab Saeed

The computer picks a secret random number and the player tries to
guess it within a limited number of tries. Includes difficulty levels
and a simple score counter (bonus features).
"""

import random


def choose_difficulty():
    """Ask the player to pick a difficulty level and return (low, high, max_tries)."""
    print("\nChoose a difficulty level:")
    print("  1. Easy   (1-50,  10 tries)")
    print("  2. Medium (1-100, 7 tries)")
    print("  3. Hard   (1-200, 5 tries)")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return 1, 50, 10
        elif choice == "2":
            return 1, 100, 7
        elif choice == "3":
            return 1, 200, 5
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def get_valid_guess(low, high):
    """Keep asking until the player enters a valid integer in range."""
    while True:
        raw_guess = input(f"Enter your guess ({low}-{high}): ").strip()
        try:
            guess = int(raw_guess)
        except ValueError:
            print("That's not a valid number. Please try again.")
            continue

        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}.")
            continue

        return guess


def play_round():
    """Play a single round of the guessing game."""
    low, high, max_tries = choose_difficulty()
    secret_number = random.randint(low, high)
    tries_used = 0

    print(f"\nI'm thinking of a number between {low} and {high}. "
          f"You have {max_tries} tries. Good luck!")

    while tries_used < max_tries:
        guess = get_valid_guess(low, high)
        tries_used += 1
        tries_left = max_tries - tries_used

        if guess == secret_number:
            score = max(0, (max_tries - tries_used + 1) * 10)
            print(f"\nCongratulations! You guessed it in {tries_used} "
                  f"tr{'y' if tries_used == 1 else 'ies'}!")
            print(f"Your score: {score} points")
            return

        if guess > secret_number:
            print("Too High! Try a smaller number.")
        else:
            print("Too Low! Try a bigger number.")

        if tries_left > 0:
            print(f"Attempts left: {tries_left}")

    print(f"\nOut of tries! The secret number was {secret_number}. Better luck next time!")


def main():
    print("=" * 50)
    print("   WELCOME TO THE NUMBER GUESSING GAME")
    print("=" * 50)

    while True:
        play_round()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
