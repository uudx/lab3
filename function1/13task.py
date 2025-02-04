from random import randint

rannumber = randint(1,20)
is_true = True
i = 0

name = input("Hello! What is your name?\n")
print("\nWell, KBTU, I am thinking of a number between 1 and 20.")

while is_true:
    print("Take a guess.")

    i += 1

    guess = int(input())
    print("\n")

    if guess == rannumber:
        print(f"Good job, KBTU! You guessed my number in {i} guesses!")
        break
    elif guess > rannumber:
        print("Your guess is too high.")
    elif guess < rannumber:
        print("Your guess is too low.")
