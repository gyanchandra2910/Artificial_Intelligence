import copy

GOAL = [[1, 2, 3],[4, 5, 6], [7, 8, 0]]
START = [[3, 4, 8], [6, 0, 7], [5, 2, 1]]

def get_heuristic(board):
    err = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != GOAL[i][j]:
                err = err + 1
    return err
    
def move_gen(cur_row, cur_col, board):
    neighbours = []
    

    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    for move in moves:
        r = move[0]
        c = move[1]
        new_r = cur_row + r
        new_c = cur_col + c
        if new_r >= 0 and new_r < 3 and new_c >= 0 and new_c < 3:
            new_board = copy.deepcopy(board)
            val_at_zero = new_board[cur_row][cur_col]
            val_at_new = new_board[new_r][new_c]
            new_board[cur_row][cur_col] = val_at_new
            new_board[new_r][new_c] = val_at_zero
            
            neighbours.append(new_board)
            
    return neighbours

def get_zero_location(board):
        row_of_empty = -1
        col_of_empty = -1
        for i in range(3):
            for j in range(3):
                if(board[i][j] == 0):
                    row_of_empty = i
                    col_of_empty = j
                    break
            if row_of_empty != -1:
                break
        return row_of_empty, col_of_empty

def hill_climb():
    print("The hill climb is starting with initial board", START)
    print("\n")
    cur_best_board = START
    cur_best_val = get_heuristic(START)
    while True:
        row_of_zero, col_of_zero = get_zero_location(cur_best_board)
        if cur_best_val == 0:
            print("Goal reached")
        
        get_neighbours = move_gen(row_of_zero, col_of_zero, cur_best_board)
        best_neighbour_val =  get_heuristic(get_neighbours[0])
        best_neighbour_board = get_neighbours[0]
        
        for neighbour in get_neighbours:
            heuristic_val = get_heuristic(neighbour)
            if heuristic_val < best_neighbour_val:
                best_neighbour_val = heuristic_val
                best_neighbour_board = neighbour
        
        if(best_neighbour_val >= cur_best_val):
            print("The goal is not reachable")
            break
        
        cur_best_board = best_neighbour_board
        cur_best_val = best_neighbour_val
        print("next_board : ", cur_best_board)
        print("\n")
        
        
hill_climb()
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            