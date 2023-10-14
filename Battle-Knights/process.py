from os import system
from time import sleep
from setup import knights, items
from move_details import move_details
from states import board_state
from art import art

# Welcome function to introduce the game.
# This includes heading, starting board, and ASCII art illustration of items.
def welcome():
    for item in items:
        system('clear')
        print('\nWELCOME TO BATTLE KNIGHTS!\n')
        board_state()
        print('\n')
        for line in art()[item.code]:
            print(line)
            sleep(0.01)
        sleep(1)

# Process to print turn outcomes, derived from move details.
def process(move, turn):

    # Assign knight taking the turn to mover.
    for knight in knights:
        if knight.code == move[0]:
            mover = knight

    # Assign outcomes of move details to outcomes variable.
    outcomes = move_details(move)

    # Print knight and direction of mover, with board and relevant ASCII art.
    system('clear')
    print(f'\nTURN {str(turn)}:\n')
    board_state()
    for key,value in {'N':'North','S':'South','E':'East','W':'West'}.items():
        if key == move[2]:
            bearing = value
    for key, value in art().items():
        if key == move[0] + move[2]:
            print(f'\n{mover.name} knight moves {bearing}.\n')
            for letter in value:
                sleep(0.01)
                print(letter)
            sleep(1)

    # If outcomes include drown, print ASCII art and text for drowning.
    if 'drown' in outcomes:
        system('clear')
        print(f'\nTURN {str(turn)}:\n')
        board_state()
        print(f'\n{mover.name} knight drowns!\n')
        for letter in art()['DROWNED']:
            sleep(0.01)
            print(letter)
        sleep(1)

    # If outcomes include drown, print ASCII art for itmem and text for pickup.
    if 'pickup' in outcomes:
        item = mover.item
        system('clear')
        print(f'\nTURN {str(turn)}:\n')
        board_state()
        print(f'\n{mover.name} knight picks up {item.name}!\n')
        for letter in art()[item.code]:
            sleep(0.01)
            print(letter)
        sleep(1)

    # If outcomes include attack, print ASCII art and fighters for battle.
    for outcome in outcomes:
        if mover.name in outcome:
            system('clear')
            print(f'\nTURN {str(turn)}:\n')
            board_state()
            print(f'\n{outcome[1]} knight kills {outcome[0]} knight!\n')
            for letter in art()['DEAD']:
                sleep(0.01)
                print(letter)
            sleep(1)
        break
