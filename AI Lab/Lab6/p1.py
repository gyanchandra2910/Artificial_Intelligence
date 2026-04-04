def print_board(board):
    print("")
    for i in range(3):
        print(board[i][0], ":", board[i][1], ":", board[i][2])
        if i == 0 or i == 1:
            print("-- -- -- ")
    print("")

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
            
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
            
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
        
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

def min_max(board, depth, alpha, beta):
    winner = check_win(board)
    if winner == 'O': 
        return 10 - depth 
    if winner == 'X': 
        return depth - 10 
    if is_board_full(board) == True: 
        return 0         
    
    if depth % 2 == 0:
        best_score = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = min_max(board, depth + 1, alpha, beta)
                    board[i][j] = ' ' 
                    
                    if score > best_score:
                        best_score = score
                    if best_score > alpha:
                        alpha = best_score

                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = min_max(board, depth + 1, alpha, beta)
                    board[i][j] = ' '
                    
                    if score < best_score:
                        best_score = score
                    if best_score < beta:
                        beta = best_score
                        
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return best_score


user = 0
sys = 0
d = 0

while True:
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    print("User is X and system is O")
    print_board(board)

    while True:
        print("Player 1 turn 'X'")
        x = int(input("Enter row 0, 1, 2: "))
        y = int(input("Enter col 0, 1, 2: "))
        
        if x > 2 or y > 2 or x < 0 or y < 0:
            print("Out of bound value, please enter again")
            continue
            
        if board[x][y] != ' ':
            print("Place already filled")
            continue
        
        board[x][y] = 'X'
        print_board(board)
        
        if check_win(board) == 'X':
            print("You win!")
            user = user + 1
            break
        if is_board_full(board) == True:
            print("Draw!")
            d = d + 1
            break
            
        print("Computer running: ")
        best_val = -1000
        best_row = -1
        best_col = -1
        
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    move_val = min_max(board, 1, -1000, 1000)
                    board[i][j] = ' '
                    if move_val > best_val:
                        best_val = move_val
                        best_row = i
                        best_col = j

        board[best_row][best_col] = 'O'
        print_board(board)

        if check_win(board) == 'O':
            print("System win!")
            sys = sys + 1
            break
        if is_board_full(board) == True:
            print("Draw")
            d = d + 1
            break

    print("Scores : ")
    print("User:", user, " System:", sys, " Draws:", d)
    print("--------------")
    print("")
    
    choice = input("Input y to play again else n for not playing ")
    if choice != 'y':
        print("Game Over")
        break
    