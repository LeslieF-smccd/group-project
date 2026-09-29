# Lab 1
# Group 6
# Authors: Leslie Fong
# Date: September 28, 2026

# Implement a text input guessing game for finding a number randomly picked
# from an integer "number" range. Suggested defaults are 1-100 {range(1,101)}
# with 5 tries attempts suggested as allowed before a game loss.
# Each incorrect player guess provides feedback for it being either too high
# or too low. Overall game desires repeating it with Y/N prompt.
#
# 2 main functions are defined - 'play_once_guessing()' handles game's logic.
# and 'play_game1()' loop cycles over play_once_guessing() repeatedly
# until the player answers (unless Yes) a No for playing it again.
#
# This module provides a "__main__" test driver with using a range 1-100 with
# 7 guesses allowed. "driver" test mode also emits correct answer first!
#
# Note that (2 ** tries)-1 needs to be >= range size for
# allowing a guaranteed win when using optimum binary searching.
# This is shown by this table:
#    Max range size   Tries for guaranteed as winnable
#    1                1
#    3                2
#    7                3
#    15               4
#    31               5
#    63               6
#    127              7
#
# Only providing for 5 tries with a range of 100, player will probably
# lose unless having a lucky guess!
#
# For usability, we'll accept a negative number to gracefully exit the
# current game in the cycle. The player must still not type a Y to exit the
# looped games cycling, gracefully. The negative case facilitates larger range
# and tries can be usable to abandon games requiring large amounts of guesses.

import random

game_one_plays = 0

def play_once_guessing(start=1, end=100, tries=5):
    """
    Play 1 cycle of game to guess randomly selected positive in a range.

    Typical default case expected is to find a number between 1 - 100 inclusive.
    Player has a limited number of tries to guess the positive number, with
    the default number of attempts being 5 tries are allowed.

    A quit game early leading tip gets printed when called by play_game1().
    Quitting the game early is supported for any caller of this function
    when entering any negative number.

    Parameters:
        start : int
            Default is 1. The lowest number in the guessing range.

        end : int
            Default is 100. The highest number in the guessing range.

        tries: int
            Default is 5. The number of attempts for guessing correctly
            allowed before the game is lost.

    Return:
        bool
            True - the game was won, the number successfully guessed.
            False - the game was lost by failing to guess number correctly.

    Examples:
        This desired game session text includes a Y/N question loop,
        from play_game1() being the caller. The function here instead returns
        after proclaiming the win or loss, without providing a Y/N service.

    --- 2 examples play cycles, showing different loss/win outcomes ---
        I'm thinking of a number between 1 and 100.
        Guess what it is. You have 5 tries: 50
        Nope! Too low. Try again (4 tries left): 75
        Nope! Too high. Try again (3 tries left): 60
        Nope! Too low. Try again (2 tries left): 70
        Nope! Too high. Try again (1 try left): 65
        Nope! You lost. The number was 62
    --- ----------------------------------------- visual sep for example only
        Do you want to play again? (Y/N): Y
        I'm thinking of a number between 1 and 100.
        Guess what it is. You have 5 tries: 50
        Nope! Too low. Try again (4 tries left): 75
        You got it!
        Do you want to play again? (Y/N)
    --- done with the 2 play cycles examples  ---
    
    Author: Leslie Fong
    """
    global game_one_plays

    solution = random.randint(start, end) # start and end potentials included
    tries_left = tries
    bailed = False # allow for early bail of game, using -1 etc.
    relative = "tbd"

    # Helpful introduction message, only once per loop
    if game_one_plays == 1:
        print(f"[Game Tip: Guessing -1 will stop the game early.]", end='')
        if __name__ == "__main__":
            print(f" [solution: {solution}]", end='')
        print("\n")

    try_word = "tries"
    if tries_left == 1: # dynamically correct grammer
        try_word = "try"
    print(f"I'm thinking of a number between {start} and {end}.")

    guess_input = input(f"Guess what it is. You have {tries_left} tries: ").strip()
    if (len(guess_input) > 0) and (
        guess_input[0] in "-0123456789"):
        guess = int(guess_input)
    else:
        guess = -1
    if guess <= -1: # early bail out
        bailed = True

    # reusable code to format the incorrect guess messaging
    calc_relation = lambda x, match : "high" if x > solution else "low"

    if guess != solution: # start feedback message looping until success
        relative = calc_relation(guess, solution)
        while tries_left > 1 and not bailed:
            tries_left -= 1
            if tries_left <= 1: # dynamically correct grammer
                try_word = "try"

            question = f"Nope! Too {relative}. Try again ({tries_left} {try_word} left): "
            guess_input = input(question).strip()
            if (len(guess_input) > 0) and (
                guess_input[0] in "-0123456789"):
                guess = int(guess_input)
            else:
                guess = -1

            if guess == solution: # success, wrap up results
                break

            if guess <= -1: # early bail out
                bailed = True
                break

            relative = calc_relation(guess, solution)

    if guess == solution: # winner!
        print("You got it!")
        return True

    if bailed:
        print(f"Gave up early. The number was {solution}")
    else:
        print(f"Nope! You lost. The number was {solution}")
    return False

def play_game1(start = 1, end = 100, tries = 5):
    """
    Plays guessing Game-1 once, then asks whether to play it again, repeatedly.

    Typical case expected is to find a number between 1 and 100 inclusive.
    Player has a limited number of tries to guess the number, with
    the default number being 5 tries.

    Parameters:
        start : int
            Default is 1. The lowest number in the guessing range.

        end : int
            Default is 100. The highest number in the guessing range.

        tries: int
            Default is 5. The number of attempts for guessing correctly
            before each game's outcome is lost.

    Return:
        int
            The number of times the game was won in this calls loop.
    
    Author: Leslie Fong
    """
    global game_one_plays
    score = 0
    plays = 0
    game_one_plays = 1
    while True:
        won = play_once_guessing(start, end, tries)
        if won:
            score += 1
        plays += 1
        game_one_plays = plays + 1
        get_yes = input("Do you want to play again? (Y/[N]): ")
        if 'y' in get_yes.lower():
            continue
        break

    game_one_plays = 0
    time_s = 's'
    if score == 1:
        time_s = ''
    print(f"\nYou won the game {score} time{time_s} out of {plays}.")
    return score

# Testing of the game 1 export functions
if __name__ == "__main__":
    play_game1(end = 100, tries=7) # 6 tries is winnable to end 63

    print()
    help(play_once_guessing)
    print()
    help(play_game1)

