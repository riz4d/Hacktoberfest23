from setup import knights, items

# Function to draw state of the board, based on knights and items.
def board_state():

    # Create an empty 8* board.
    board = [[' ']*8 for i in range(8)]

    # Place items in their correct board squares, if they have no holder.
    for item in items:
        if item.holder is None:
            board[item.position[0]][item.position[1]] = item.code

    # Place knights in their correct board squares, if they are alive.
    for knight in knights:
        if knight.status == 'ALIVE':
            board[knight.position[0]][knight.position[1]] = knight.code

    # Print the board, with separator pipes.
    for line in board:
        print('|'.join(line))

# Function to prepare a JSON file, showing the game state.
def game_state():

    # Create an empty dictionary to record the game state.
    game_state = {}

    # Iterate through knights to record their game states.
    for knight in knights:

        # If knight holds no item, this must be declared explicitly.
        # This avoids an error relating item of None type having no attributes.
        if knight.item is None:
            game_state[knight.name] = [knight.position,
                                    knight.status,
                                    None,
                                    knight.attack,
                                    knight.defence]

        # If knight holds and item, that item's name can be added.
        # The item's attack and defence can also be added to the knight's.
        else:
            game_state[knight.name] = [knight.position,
                                    knight.status,
                                    knight.item.name,
                                    knight.attack + knight.item.attack,
                                    knight.defence + knight.item.defence]

    # Iterate through items to record their game states.
    for item in items:

        # Replace item holder name with binary value, to fit game briefing.
        if item.holder is None:
            item.holder = 'No'
        else:
            item.holder = 'Yes'
        game_state[item.name] = [item.position,
                                item.holder]

    # Assign game state the output variable, with correct spacing and symbols.
    output = '' + '{\n'
    for key, value in game_state.items():
        output += f'    "{key}": {value},\n'
    output += '}'

    return output
