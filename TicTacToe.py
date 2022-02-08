import numpy as np
from vsAi_heuristic import * 
from vsHuman import * 
from vsRandom import * 
from utility import * 

board = np.array([['_','_','_', '_'],['_','_','_', '_'],['_','_','_', '_'],['_','_','_', '_']])

print("1: Play vs Human\n2: Play vs Random Bot\n3: Play vs Smart Bot")
print()
mode = int(input("Select mode (1 or 2 or 3): "))
print()
instructions(mode)
printBoard(board)
if mode==1 or mode==2 or mode==3:
    if mode==1:
        result = human(board)
    elif mode==2:
        result = randomBot(board)
    elif mode==3:
        result = ai(board)

    print('Game Result: ', end="")
    gameResult(result)
else:
    print('\nInvalid Input')
