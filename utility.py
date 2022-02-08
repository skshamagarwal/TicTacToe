def instructions(mode):
    if mode == 1:
        print("Game Mode: HUMAN VS HUMAN")
    elif mode == 2:
        print("Game Mode: HUMAN VS RANDOM BOT")
    elif mode == 3:
        print("Game Mode: HUMAN VS SMART BOT")

    print("\nRefer to the table below to mark at your desired spot:")
    for i in range(1, 17):
        print(i,end=" ")
        if i%4==0:
            print()
        else:
            print("|", end=" ")


def printBoard(board):
    print("\nBOARD:")
    for i in board:
        print(' | '.join(i))


def checkWin(board):
    # Check Row
    for i in board:
        if len(set(i)) == 1 and i[0]!='_':
            return i[0]
        
    # Check Column
    for i in range(4):
        if (board[0][i] == board[1][i] == board[2][i] == board[3][i]) and board[0][i]!='_':
            return board[0][i]
    
    # Check Diagonals
    if (board[0][0]==board[1][1]==board[2][2]==board[3][3]) and board[0][0]!='_':
            return board[0][0]
    if (board[0][3]==board[1][2]==board[2][1]==board[3][0]) and board[0][3]!='_':
        return board[0][3]
    
    # No One Won Yet
    return -1
    
    
def checkGameOver(board, spotsLeft):
    # t -> Game Tied
    # x -> Player X won
    # o -> Player O won
    
    # if tied - all spots filled
    if spotsLeft == 0:
        return True, 'T'
    
    # if any player won the game
    result = checkWin(board)
    if result!=-1:
        return True, result
    
    return False, -1


def spotToIdx(ip):
    if ip == 1: return 0, 0
    elif ip == 2: return 0, 1
    elif ip == 3: return 0, 2
    elif ip == 4: return 0, 3
    elif ip == 5: return 1, 0
    elif ip == 6: return 1, 1
    elif ip == 7: return 1, 2
    elif ip == 8: return 1, 3
    elif ip == 9: return 2, 0
    elif ip == 10: return 2, 1
    elif ip == 11: return 2, 2
    elif ip == 12: return 2, 3
    elif ip == 13: return 3, 0
    elif ip == 14: return 3, 1
    elif ip == 15: return 3, 2
    elif ip == 16: return 3, 3
    
    
def gameResult(result):
    if result == "T": print("Game Tied!")
    if result == "X": print("Player X Won!")
    if result == "O": print("Player O Won!")