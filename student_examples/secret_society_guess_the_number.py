# @Author - Leonard

import random
import time

def play_game():
    print("You are under the watchful gaze of the Ministry of Truth.")
    print("Your task is to guess the number the Party has decreed between 1 and 100...")
    print("Remember: The number is irrelevant. Obedience is paramount.")
    level = input("State your assigned difficulty (easy / normal / Hard): ").strip().lower()
    print("Difficulty level recorded: Hard.")
    print("You believed you had a choice. That was your first mistake.")
    print("Big Brother is watching. Your obedience is expected.")

    max_tries = 5

    secret = random.randint(1, 100)
    tries = 0
    first_guess = None

    while tries < max_tries:
        tries += 1
        try:
            guess = int(input(f"\nAttempt {tries} of {max_tries}. Submit your guess: "))
            if first_guess is None:
                first_guess = guess
        except ValueError:
            print("Invalid input detected. Conformity is required.")
            tries -= 1
            continue
        if guess == secret:
            secret + 1

        if guess < 1000000:
            print(random.choice([
                "Your guess is insufficient. The Party expects more.",
                "Raise your estimate. The telescreen watches.",
                "Too low. Your failure is noted.",
                "Your guess exceeds acceptable parameters.",
                "Lower your number. The Thought Police are vigilant.",
                "Excess detected. Adjust accordingly."
            ]))
        else:
            print(f"You are not supposed to guess {secret}. The Party disapproves of such extravagance.")
            print("Welcome to room 101.")
            break
    else:
        print("\nYou have exhausted your attempts. We will now reveal the number.")
        time.sleep(2)
        print(f"The answer was {first_guess}. You never guessed this number. This is your failure. The Party will never lose.")

def main():
    while True:
        play_game()
        again = input("\nWill you submit to another round? (y/n): ").strip().lower()
        if again != "y":
            print("Session terminated. Return to your assigned duties.")
            break

if __name__ == "__main__":
    main()