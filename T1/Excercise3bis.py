#Guess the number: Develop a game where the computer chooses a random number, and
#the player must guess it within a limited number of attempts
import random

def main():
    # Set the range of numbers and the number of attempts
    min_number = #TODO
    max_number = #TODO
    max_attempts = #TODO

    # Generate a random number for the player to guess
    secret_number = random.randint(min_number, max_number)

    print(f"Welcome to Guess the Number!")
    print(f"I'm thinking of a number between {min_number} and {max_number}.")

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}/{max_attempts}: Enter your guess: "))

        if #TODO
            print("Try a higher number.")
        elif #TODO
            print("Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    main()



