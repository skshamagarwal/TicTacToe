from utility import * 

def human(board):
    p1 = 'X'
    p2 = 'O'
    spotsLeft = 16
    turn = p1
    while True:
        print()
        res, stat = checkGameOver(board, spotsLeft)
        if res==False:
            inp = int(input(f"{turn}'s turn: "))
            i, j = spotToIdx(inp)
            if board[i][j]=='_':
                board[i][j] = turn
                if turn == p1: turn = p2
                else: turn = p1
                spotsLeft-=1
        else: return stat
        printBoard(board)