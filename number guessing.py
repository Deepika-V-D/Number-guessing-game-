import random

numbers = [ ]

secret_number = random.randint(1, 10)
attempts = 0

print("===== NUMBER GUESSING GAME =====")
print("Guess a number between 1 and 10")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    numbers.append(guess)

    if guess == secret_number:
        print("Correct! You Won!")
        print("Number of attempts:", attempts)
        print("Your guesses:", numbers)
        break

    elif guess < secret_number:
        print("Too Low! Try again.")

    else:
        print("Too High! Try again.")