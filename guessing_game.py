import random

number = random.randint(0, 10)
guess = 0

while guess != number: 
    guess = int(input("Please enter a number between 0 to 10: "))
    
    if guess == number:
        print("You guessed the correct number! Woo-hoo!")
    else: 
        print("Womp-womp, you got it wrong!")