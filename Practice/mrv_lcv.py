import copy 

initial_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

def is_possible(grid, r, c, val):
    for i in range(9):
        if grid[r][i] == val:
            return False
        if grid[i][c] == val:
            return False
            
    # MISTAKE 1: Block ka starting index nikalne ke liye * 3 karna zaroori hai.
    row = (r // 3) * 3  # FIXED: added * 3
    col = (c // 3) * 3  # FIXED: added * 3
    
    for i in range(3):
        for j in range(3):
            new_r = row + i
            new_c = col + j
            # MISTAKE 2: Tune grid[new_c][new_r] likh diya tha, jabki [new_r][new_c] hota hai.
            if grid[new_r][new_c] == val: # FIXED: swapped row and col
                return False
                
    return True

def possible_val(grid, r, c):
    domain = []
    # MISTAKE 3: Sudoku me numbers 1 se 9 tak hote hain, range(9) matlab 0 se 8 ho jayega.
    for i in range(1, 10): # FIXED: Changed range(9) to range(1, 10)
        if is_possible(grid,r,c,i):
            domain.append(i)  
    return domain


def MRV(grid):
    best_domain_val = 1e9
    best_domain = []
    row, col = None, None
    domain = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                domain = possible_val(grid, i, j)
                if len(domain) < best_domain_val:
                    # MISTAKE 4: Tune best_domain_val ko update hi nahi kiya tha, isliye wo humesha 1e9 rehta.
                    best_domain_val = len(domain) # FIXED: Added this line to update minimum length
                    best_domain = domain
                    row, col = i, j
    
    if best_domain_val == 1e9:
        return None, None, []
    
    return row, col, best_domain

def LCV(grid, row, col, domain):
    if len(domain) == 0:
        return True

    best_count = 1e9
    best_val = None
    
    val_count = [] # MISTAKE 5: Ye list bahar banani thi. Tune isko 'for val in domain:' loop ke andar daal diya tha, jisse har baar ye list empty ho rahi thi.

    for val in domain:
        false_count = 0
        temp_grid = copy.deepcopy(grid)
        temp_grid[row][col] = val

        for i in range(9):
            if temp_grid[row][i] == 0 and not is_possible(temp_grid, row, i, val):
                false_count += 1
            if temp_grid[i][col] == 0 and not is_possible(temp_grid, i, col, val):
                false_count += 1
                
        # MISTAKE 6: Yahan bhi block logic me * 3 karna chhooth gaya tha.
        new_r = (row // 3) * 3 # FIXED: added * 3
        new_c = (col // 3) * 3 # FIXED: added * 3

        for i in range(3):
            for j in range(3):
                r = new_r + i
                c = new_c + j

                if temp_grid[r][c] == 0 and not is_possible(temp_grid, r, c, val):
                    false_count += 1
        
        # MISTAKE 7: .append() ek bar me sirf ek argument leta hai. Tujhe as a Tuple (bracket laga ke) pass karna tha.
        val_count.append((false_count, val)) # FIXED: added parenthesis () to make it a tuple
    
    val_count.sort()
    return val_count

def solve(grid):
    row, col, domain = MRV(grid)
    if row == None and col == None:
        return True
    
    values = LCV(grid, row, col, domain)

    for count, val in values:
        grid[row][col] = val
        if(solve(grid)):
            return True
        grid[row][col] = 0
    
    return False

# ----- TESTING THE CODE -----
grid_copy = copy.deepcopy(initial_grid)
solve(grid_copy)

print("SOLVED GRID:")
for r in grid_copy:
    print(r)