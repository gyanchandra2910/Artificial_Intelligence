import random

def calc_cost(board):
    n = len(board)
    cost = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                cost += 1
    return cost

def solve(n):
    while True:
        board = [random.randint(0, n - 1) for _ in range(n)]
        
        while True:
            curr_cost = calc_cost(board)
            if curr_cost == 0:
                return board
            
            best_board = list(board)
            min_cost = curr_cost
            
            for col in range(n):
                orig_row = board[col]
                for row in range(n):
                    if row != orig_row:
                        board[col] = row
                        new_cost = calc_cost(board)
                        if new_cost < min_cost:
                            min_cost = new_cost
                            best_board = list(board)
                        board[col] = orig_row
            
            if min_cost >= curr_cost:
                break
            
            board = best_board

n = 8
res = solve(n)
print("The position of queen in each row is ", res)
