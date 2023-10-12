from setup import knights, items
from art import art

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
