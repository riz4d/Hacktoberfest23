from os import system
from art import art
from states import game_state
from process import welcome, process

moves = open('moves.txt').read().split('\n')[1:-2]

# Run welcome function to introduce the game.
welcome()

# Assign turn variable for first turn.
turn = 1

# Iterate through moves,
for move in moves:
    process(move, turn)
    turn += 1

# After final turn, assign final game state.
final_state = game_state()

# Announce game over and print final game state.
print('\nGAME OVER!\n')
print(final_state)

# Write final game state to JSON file, and open this file.
with open('final_state.json', 'w') as f:
    f.write(final_state)
system('open final_state.json')
