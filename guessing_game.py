import random

number = random.randint(0, 10)
guess = 0
count = 0

while guess != number: 
    guess = int(input("Please enter a number between 0 to 10: "))
    count += 1
    
    if guess == number:
        print("You guessed the correct number in " + str(count) + " tries! Woo-hoo!")
    elif guess > number:
        print("You guessed too high, try going lower.")
    elif guess < number:
        print("You guessed too low, try going higher.")