import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("")
    print("*** Number Guessing Game ***")
    print("I picked a number between 1 and 100!")
    print("")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again!")
        elif guess > number:
            print("Too high! Try again!")
        else:
            print("")
            print("Correct! You got it in", attempts, "attempts!")
            break

while True:
    play_game()
    print("")
    again = input("Play again? (yes/no): ")
    if again.lower() == "no":
        print("Thanks for playing! Goodbye!")
        break	
0

