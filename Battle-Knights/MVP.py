from os import system

class Knight:
    # Define knight class, with all required attributes.
    def __init__(self, code, name, position, status, item, attack, defence):
        self.code = code
        self.name = name
        self.position = position
        self.status = status
        self.item = item
        self.attack = attack
        self.defence = defence

class Item:
    # Define item class, with all required attributes.
    def __init__(self, code, name, attack, defence, value, position, holder):
        self.code = code
        self.name = name
        self.attack = attack
        self.defence = defence
        self.value = value
        self.position = position
        self.holder = holder

# Define all knights, as instances of knight class.
R = Knight('R', 'Red', [0,0], 'ALIVE', None, 1, 1)
B = Knight('B', 'Blue', [7,0], 'ALIVE', None, 1, 1)
G = Knight('G', 'Green', [7,7], 'ALIVE', None, 1, 1)
Y = Knight('Y', 'Yellow', [0,7], 'ALIVE', None, 1, 1)

# Define all items, as instances of item class.
A = Item('A', 'Axe', 2, 0, 40, [2,2], None)
M = Item('M', 'Magic Staff', 1, 1, 30, [5,2], None)
D = Item('D', 'Dagger', 1, 0, 20, [2,5], None)
H = Item('H', 'Helmet', 0, 1, 10, [5,5], None)

# Create lists of knights and items, to iterate easily through their instances.
knights = [R, B, G, Y]
items = [A, M, D, H]

def move_details(move):
# Decision tree illustrating the outcomes of each move.
# Knight and item instances are adjusted accordingly.

    # Create empty list for outcomes, which will be carried into setup.py.
    outcomes = []

    # Assigning knight code from this move to mover.
    for knight in knights:
        if move[0] == knight.code:
            mover = knight

    # Assign the item held by the mover to holding.
    # This allows us to use attributes of this item below.
    holding = mover.item

    # Check if mover is alive - otherwise movement will be skipped.
    if mover.status == 'ALIVE':

        # Dictionary translating directional letter into instruction list.
        # First item of list is mover's position index to change.
        # Second item of list is direction in which to change position index.
        directions = {'N':[0,-1], 'S':[0,1], 'W':[1,-1], 'E':[1,1]}

        # Iterate through directions dictionary.
        for key, value in directions.items():
            if move[2] == key:
                position_shift = mover.position[value[0]] + value[1]

                # Check if new position is on the board, else knight will drown.
                if position_shift in range(8):
                    mover.position[value[0]] = position_shift

                    # Check if knight moves onto a square with item on it.
                    for item in items:
                        if item != holding:
                            if item.position == mover.position:

                                # If knight has not item, pickup is triggered.
                                if holding is None:
                                    item.holder = mover
                                    mover.item = item

                                # Check if new item more valuable than holding.
                                # If so, drop holding item, and pickup new item.
                                elif holding.value < item.value:
                                    item.holder = mover
                                    mover.item = item
                                    holding.holder = None
                                    holding.position = list(mover.position)

                                # Append pickup condition to outcomes.
                                outcomes.append('pickup')

                    # Attack triggered if knight moves to other knight's square.
                    for defender in knights:
                        if defender != mover:
                            if defender.status == 'ALIVE':
                                if defender.position == mover.position:

                                    # Total attack, with weapon and surprise.
                                    total_attack = mover.attack + 0.5
                                    for item in items:
                                        if mover.item == item:
                                            total_attack += item.attack

                                    # Total defence, with weapon.
                                    total_defence = defender.defence
                                    for item in items:
                                        if defender.item == item:
                                            total_defence += item.defence

                                    # Determine winner and loser of battle.
                                    # Append winner and loser names to outcomes.
                                    if total_attack > total_defence:
                                        defender.status = 'DEAD'
                                        defender.item = None
                                        outcomes.append([defender.name,
                                            mover.name])
                                    else:
                                        mover.status = 'DEAD'
                                        mover.item = None
                                        outcomes.append([mover.name,
                                            defender.name])

                # Drowning triggered if knight moves to position outside board.
                else:
                    if mover.item is not None:
                        drop = mover.item
                        drop.holder = None
                        drop.position = list(mover.position)
                    mover.status = 'DROWNED'
                    mover.position = None
                    mover.item = None

                    # Append drowning condition to outcomes.
                    outcomes.append('drown')

    # Outcome list returned, with items informing triggers in setup.py.
    return outcomes

moves = open('moves.txt').read().split('\n')[1:-2]

# Assign turn variable for first turn.
turn = 1

# Iterate through moves,
for move in moves:
    move_details(move)
    turn += 1

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

# After final turn, assign final game state.
final_state = game_state()

# Announce game over and print final game state.
print('\nGAME OVER!\n')
print(final_state)

# Write final game state to JSON file, and open this file.
with open('final_state.json', 'w') as f:
    f.write(final_state)
system('open final_state.json')
