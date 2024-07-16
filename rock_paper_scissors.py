import random

items = ["rock", "paper", "scissors"]

print("Which item do you choose?")
print("Rock [0] Paper [1] Scissors [2]")

choice_int = int(input("Choose: "))
choice = items[choice_int]

computer_int = random.randint(0, 2)
computer = items[computer_int]

print("You chose " + choice + ". The computer chose " + computer + ".")

if choice == computer:
    print("It's a tie!")
elif (choice == "rock" and computer == "scissors") or \
     (choice == "paper" and computer == "rock") or \
     (choice == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")
