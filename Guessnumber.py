"""
Number Guessing Game
-----------------------
Demonstrates:
- a class holding game state (secret number, attempts) instead of globals
- separating game logic (Game.guess) from display/I/O (the main loop)
- try/except ValueError for non-numeric input, using continue to re-prompt
  without costing the player an attempt
- while/else: the else runs only if the loop was never broken out of
- dict dispatch for a difficulty menu
"""

import random


class Game:
    def __init__(self, low=1, high=100, max_attempts=7):
        self.low = low
        self.high = high
        self.secret = random.randint(low, high)
        self.max_attempts = max_attempts
        self.attempts_used = 0

    def guess(self, value):
        """Register a guess, return 'low', 'high', or 'correct'."""
        self.attempts_used += 1
        if value < self.secret:
            return "low"
        elif value > self.secret:
            return "high"
        else:
            return "correct"

    def attempts_left(self):
        return self.max_attempts - self.attempts_used

    def is_over(self):
        return self.attempts_used >= self.max_attempts


def choose_difficulty():
    print("\n1. Easy   (1-50,  10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-200, 5 attempts)")
    choice = input("Choose difficulty (1-3): ").strip()
    settings = {
        "1": (1, 50, 10),
        "2": (1, 100, 7),
        "3": (1, 200, 5),
    }
    return settings.get(choice, (1, 100, 7))  # default to Medium on invalid input


def play_round(game):
    print(f"\nI'm thinking of a number between {game.low} and {game.high}.")

    while not game.is_over():
        raw = input(f"Guess a number ({game.attempts_left()} attempts left): ").strip()

        try:
            value = int(raw)
        except ValueError:
            print("That's not a valid number — try again.")
            continue  # doesn't count as an attempt

        result = game.guess(value)
        if result == "correct":
            print(f"Correct! You got it in {game.attempts_used} attempt(s).")
            break
        elif result == "low":
            print("Too low.")
        else:
            print("Too high.")
    else:
        # only runs if the while loop ended by running out of attempts,
        # not if it ended via 'break' on a correct guess
        print(f"Out of attempts! The number was {game.secret}.")


def main():
    while True:
        low, high, max_attempts = choose_difficulty()
        game = Game(low, high, max_attempts)
        play_round(game)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()