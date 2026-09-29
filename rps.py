# Lab 1 
# Group #7
# Author: Everett Carvalho
# Date: 09/28/2026

import random

weapons = ["", "paper", "scissors", "rock"] # 0, 1, 2, 3

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


        if user == computer:
            print(f"It's a tie! You both picked {weapons[user]}.")
        elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
            print(f"You win! You picked {weapons[user]} and the computer picked {weapons[computer]}.")
        else:
            if user in [1, 2, 3]:
                print(f"You lose! You picked {weapons[user]} and the computer picked {weapons[computer]}.")
            else:
                print(f"You lost. Computer's {weapons[computer]} defeats an unarmed you.")

        answer = input("Do you want to play again? (Y/N): ")    

if __name__ == "__main__":
    rps()