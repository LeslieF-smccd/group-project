# Lab 1
# Group 6
# Authors: Leslie Fong, Everett Carvalho
# Date: September 26, 2026

# Main program for implementing a set of text input games.
# Game 1 is guessing to find a number randomly picked in a range
# Game 2 is Rock-Paper-Scissors game
#
# This main program invokes the individual games' module functions,
# and repeats playing the user's choices for which game to run,
# if desired. After running a game, a Y/N choice is offered to rerun it.
# If not rerun, the main choices of either games or to exit is offered again.

import guessing
import rps

print("*******************************************************************")
print("*   Welcome to CIS-117 Assignment 6, Group Lab 1 - Games!         *")
print("*   Code Developed by Group 6                                     *")
print("*   Authors: Leslie Fong, Everett Carvalho                        *")
print("*******************************************************************")

print()
print("There are 2 games to choose from to play.")
print("")
print("The first game is a Guessing Game, which challenges you to guess the")
print("number the program selected within the range of 1 to 100.")
print("Every time you make an incorrect guess, the program indicates whether")
print("it was too low, or too high. The challenge is having a limited number")
print("of only 5 tries to win!")
print()
print("The next choice is the Rock-Paper-Scissors Game, from ancient times.")
print("You will be asked to choose a weapon to duel against the program's")
print("choice of a weapon. The available weapons are Rock, Paper, or Scissors.")
print("The competition's win rules are:")
print("Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.")
print()
print("Both of these games will involve luck as an element for winning.")
print()

# Optional to offer the extra bonus picks version
print("The first Guessing Game also offers an easier to win variation, which")
print("can reward dedicated strategies for winning, without requiring luck.")
print()

all_done = False
while not all_done:
    print("\nWhich game do you want to play?\n    Letter choices are:")
    print("        1. Guessing Game")
    print("        2. Rock-Paper-Scissors")
    print("        3. Guessing Game, with 2 bonus tries")
    print("        X. Exit")
    choice = input("    Which game do you want to play: ").strip().lower()

    game_name = ""

    while True:
        if choice == '1':
            game_name = "Guessing Game"
            print("\nPlaying Guessing Game!\n")
            guessing.play_game1(end = 100, tries = 5) # 7 enables guarantee winnable
        elif choice == '2':
            game_name = "Rock-Paper-Scissors"
            print("\nPlaying Rock-Paper-Scissors!\n")
            rps.rps()
        elif choice == '3':
            game_name = "Guessing Game"
            print("\nPlaying Guessing Game, with 2 bonus tries\n")
            guessing.play_game1(end = 100, tries = 7) # 7 enables guarantee winnable
        else:
            all_done = True
            break

        print(f"\nHope you enjoyed {game_name}!\n")

        # Requirement to offer rerunning the same game again.
        repeat = input("Do you want to play that game again? " ).strip().lower()
        if len(repeat) < 1 or 'y' != repeat[0]:
            break

print("\nAll done with games. Thank you for playing.\n"
      "Come back and play again!\n"
       "Bye!\n")

