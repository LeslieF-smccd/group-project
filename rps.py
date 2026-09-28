# Lab 1 
# Group #7
# Author: Everett Carvalho
# Date: 09/28/2026

import random

def rps():
    """Play Rock-Paper-Scissors game against the computer.

    The computer picks a random number 1-3 and the user picks a 
    number (1 = paper, 2 = scissors, 3 = rock). Paper beats rock,
    rock beats scissors, and scissors beats paper. Same number is a tie.

    Author: Everett Carvalho
    """
    answer = input("Do you want to play? ")
    while answer.lower() in ("yes", "y"):
        computer = random.randint(1, 3)
        user = int(input("Enter your choice: 1. paper, 2. scissors, 3. rock: "))
        print("Computer chose: ", computer)

        if user == computer:
            print("It's a tie!")
        elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
            print("You win!")
        else:
            print("Computer wins!")

        answer = input("Do you want to play again? (Y/N): ")    

if __name__ == "__main__":
    rps()