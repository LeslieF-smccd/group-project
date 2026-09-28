# Lab 1
# Group 6
# Authors: Leslie Fong
# Date: September 26, 2026

# Implement a text input rock-paper-scissors game,
# by player typing a number representing a weapon choice,
# while computer picks its own weapon as a random selection.
#
# The overall game desires repeating itself with a Y/N prompt.
#
# 2 game functions are defined - 'play_once_rps()' handles game's logic.
# and 'play_game2()' loop cycles over play_once_rps() repeatedly
# until the player answers a No for playing it again.
#
# This module provides a "__main__" test driver
#

import random

def play_once_rps():
    """
    Play 1 cycle of a user chosen weapon vs. randomly selected weapon.

    The mapping choice of weapons to numbers defined in task's example were:
        1. paper
        2. scissors
        3. rock

    Refresher on battle pairing off rules: rock > scissors > paper > rock.

    Outputs:
        It is a tie!
        You won! Your [rock, paper, scissors] defeats opponent's [rock, ...]!
        You lost. Opponent's [rock, paper, scissors] defeats your [rock, ...]!
        Do you want to play again? (Y/[N])

    Parameters: None

    Return:
        int
             1 - Game was won, user's weapon choice came out on top.
            -1 - Game was lost by failing to overpower/defend the attack.
             0 - Game resolved as a tie for the same attack weapons.

    Examples:
        This desired game session text includes a Y/N question loop,
        via play_game2() being its caller. This function here instead returns
        after proclaiming the win or loss, without providing a Y/N service.

    --- 2 example play cycles, showing different loss/win outcomes ---
            Do you want to play? yes
            Enter your choice: 1. paper, 2. scissors, 3. rock: 2
            It is a tie!

    --- ----------------------------------------- visual sep for example only
            Do you want to play again? (Y/[N]): y
            Enter your choice: 1. paper, 2. scissors, 3. rock: 2
            You won! Your scissors defeats opponent's paper.

            Do you want to play again? (Y/[N]): n
    --- done with the 2 play cycles examples  ---
    """

    # Define useful constant nums to enhance code readability.
    rock = 3
    scissors = 2
    paper = 1

    if False: # if wanting to use different number mappings instead:
        rock = 1
        paper = 2
        scissors = 3

    # generate preferred display of choice ordering
    weapons = [1,1,1]
    weapons[paper-1] = paper
    weapons[scissors-1] = scissors
    weapons[rock-1] = rock

    min_w = min(weapons) # 1
    max_w = max(weapons) # 3

    attack = random.randint(min_w, max_w) # start and end are included

    bailed = False

    rps_names = ["", "", ""]  # be more flexible on number to names
    # reusable code to map number to weapon's name
    name_weapon = lambda x : rps_names[x - 1]

    rps_names[rock-1] = "rock"
    rps_names[paper-1] = "paper"
    rps_names[scissors-1] = "scissors"

    # input(f"Enter...: {paper}. paper, {scissors}. scissors, {rock}. rock: ")
    # input(f"Enter...: {rock}. rock, {paper}. paper, {scissors}. scissors: ")
    rps_input = input(f"Enter your choice: "
                        f"{weapons[0]}. {name_weapon(weapons[0])}, "
                        f"{weapons[1]}. {name_weapon(weapons[1])}, "
                        f"{weapons[2]}. {name_weapon(weapons[2])}: ").strip()
    # feedback from Everett
    print(f"Computer chose: {attack} - {name_weapon(attack)}")
    if (len(rps_input) == 1) and (rps_input[0] in
                                f"{paper}" f"{scissors}" f"{rock}"): # "123"
        rps = int(rps_input)
    else:
        rps = -1
        bailed = True
        print(f"You lost. Opponent's {name_weapon(attack)} defeats a concession.")
        return -1

    won = 0

    if rps == attack:
        print("It is a tie!")
        return 0

    if rps == rock:
        if attack == scissors:
            won = 1
        else:
            won = -1
    elif rps == paper:
        if attack == rock:
            won = 1
        else:
            won = -1
    else: # rps == scissors
        if attack == paper:
            won = 1
        else:
            won = -1

    if won > 0:
        print(f"You won! Your {name_weapon(rps)} defeats opponent's {name_weapon(attack)}.")
    else:
        print(f"You lost. Opponent's {name_weapon(attack)} defeats your {name_weapon(rps)}.")
    return won

def play_game2():
    """
    Plays Rock-Paper-Scissors game via play_once_rps(), as directed.

    Before playing it the first time, a confirmation question to
    start is asked, needing a Y typed yes reply. If started, the game
    is played, and then asks user whether to play it again, repeatedly.

    Parameters:
        None

    Return:
        None
        int
            The number of times the RPS game was won in repeated calls.
            If player refused to start playing, None is returned.
    """
    score = 0
    plays = 0
    ties = 0
    losses = 0

    initial = input("Do you want to play? ").strip()
    if len(initial) < 1 or 'y' != initial[0].lower():
        return None

    while True:
        won = play_once_rps()
        if won > 0:
            score += 1
        elif won < 0:
            losses -= 1
        else:
            ties += 1
        plays += 1

        get_yes = input("\nDo you want to play again? (Y/[N]): ").strip()
        if 'y' in get_yes.lower():
            continue

        # Easier to rapid run or test, if we allow 1, 2, 3 to continue Y too.
        if len(get_yes) == 1 and get_yes[0] in "123":
            continue

        break

    print()
    print(f'{"Rock-Paper-Scissors Game Results Summary":^40}')
    print(f"    Wins:   {score:3d} {100 * score/plays:6.2f}%")
    print(f"    Losses: {-losses:3d} {-100 * losses/plays:6.2f}%")
    print(f"    Ties:   {ties:3d} {100 * ties/plays:6.2f}%")

    time_s = 's'
    play_s = 's'
    if score == 1:
        time_s = ''
    if plays == 1:
        play_s = ''
    print(f"\nYou won {score} time{time_s} out of {plays} play{play_s}.\n")
    return score

# Testing of the game 2 export functions
if __name__ == "__main__":
    play_game2()
    print()
    help(play_once_rps)
    print()
    help(play_game2)

