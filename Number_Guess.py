import random
import time

def number_guess_game():
    print("Welcome to the Number Guessing Game!")
    print("You have a limited amount of time to guess a number between 1 and 10.")
    print("If you don't guess within the given time, you will be asked to play again.")

    while True:
        try:
            time_limit = int(input("Enter the time limit in seconds (e.g., 5): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        target_number = random.randint(1, 10)
        print("\nGuess the number between 1 and 10:")
        
        start_time = time.time()
        user_input = None

        while True:
            if time.time() - start_time >= time_limit:
                print("Time's up! You ran out of time.")
                break

            try:
                user_input = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            
            if user_input == target_number:
                print("Congratulations! You guessed the correct number.")
                break
            else:
                print("Incorrect guess. Try again!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    number_guess_game()
