import math
from utility import *

def minimax(board, spotsLeft, maximizing):
    global count
    bestIdx = (0,0)
    p1 = 'X'
    p2 = 'O'
    res, stat = checkGameOver(board, spotsLeft)
    if res==True:
        if stat == 'X': return 17-spotsLeft, bestIdx
        elif stat == 'O': return -17+spotsLeft, bestIdx
        else: return 0, bestIdx
    
    if maximizing:
        # return max score
        bestMove = -math.inf
        for i in range(4):
            for j in range(4):
                if board[i][j] == '_':
                    board[i][j] = p1
                    score, idx = minimax(board, spotsLeft-1, False)
                    print(score, idx)
                    board[i][j] = '_'
                    if bestMove<score:
                        bestMove = score
                        bestIdx = (i,j)
        return bestMove, bestIdx
    else:
        # return min score
        bestMove = math.inf
        for i in range(4):
            for j in range(4):
                if board[i][j] == '_':
                    board[i][j] = p2
                    score, idx = minimax(board, spotsLeft-1, True)
                    print(score, idx)
                    board[i][j] = '_'
                    if bestMove>score:
                        bestMove = score
                        bestIdx = (i,j)
        return bestMove, bestIdx
    

def ai(board):
    spotsLeft = 16
    p1 = 'X'    # Computer
    p2 = 'O'    # Player
    turn = p1
    while True:
        res, stat = checkGameOver(board, spotsLeft)
        if res==False:
            if turn == p1:
                # AI
                boardCopy = board[:]
                score, idx = minimax(boardCopy, spotsLeft, True)
                board[idx[0]][idx[1]] = turn
                turn = p2
                spotsLeft-=1
            else:
                # Human
                inp = int(input(f"Your turn: "))
                i, j = spotToIdx(inp)
                if board[i][j]=='_':
                    board[i][j] = turn
                    turn = p1
                    spotsLeft-=1
        else: return stat
        printBoard(board)