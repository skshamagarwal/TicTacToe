import random
from utility import * 

def randomBot(board):    
    p1 = 'X'
    p2 = 'O'
    
    spotsLeft = 16
    available = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    turn = p1
    while True:
        res, stat = checkGameOver(board, spotsLeft)
        print()
        if res==False:
            if turn == p1:
                inp = int(input(f"Your turn: "))
                i, j = spotToIdx(inp)
                if board[i][j]=='_':
                    board[i][j] = turn
                    turn = p2
                    spotsLeft-=1
                    available.remove(inp)
            else:
                inp = random.choice(available)
                print(f"Computers Turn: {inp}")
                available.remove(inp)
                i, j = spotToIdx(inp)
                board[i][j] = turn
                turn = p1
                spotsLeft-=1
        else: return stat
        printBoard(board)