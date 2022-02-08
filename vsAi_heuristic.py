import math
from utility import *

lines = [[(i, j) for i in range(4)] for j in range(4)
] + [[(j, i) for i in range(4)] for j in range(4)
] + [[(i, i) for i in range(4)],
    [(3-i, i) for i in range(4)]]

def evaluate(board, player):
    score = 0
    for line in lines:
        discs = [board[i][j] for i, j in line]
        # The more discs in one line the better
        value = [100, 10, 6, 1, 0][sum(ch == "_" for ch in discs)]
        if "X" in discs:
            if not "O" in discs: # X could still win in this line
                score += value
        elif "O" in discs: # O could still win in this line
            score -= value
    # Change the sign depending on which player has just played
    return score if player == "X" else -score

def ai(board):
    spotsLeft = 16
    p1 = 'X'    # Computer
    p2 = 'O'    # Player
    turn = p1
    while True:
        res, stat = checkGameOver(board, spotsLeft)
        if res==False:
            if turn == p1:
                # AI -- a heuristic based approach
                print("\nComputer's Turn")
                bestScore = -math.inf
                bestMove = None
                for i in range(4):
                    for j in range(4):
                        if board[i][j] == '_':
                            board[i][j] = turn
                            score = evaluate(board, turn)
                            if score > bestScore:
                                bestScore = score
                                bestMove = (i, j)
                            board[i][j] = '_'
                i, j = bestMove
                board[i][j] = turn
                turn = p2
                spotsLeft-=1
            else:
                # Human
                inp = int(input(f"\nYour turn: "))
                i, j = spotToIdx(inp)
                if board[i][j]=='_':
                    board[i][j] = turn
                    turn = p1
                    spotsLeft-=1
        else: return stat
        printBoard(board)