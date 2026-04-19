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

def is_valid(grid, r, c, no):
    for i in range(9):
        if grid[r][i] == no or grid[i][c] == no:
            return False
    
    row = (r // 3)*3
    col = (c // 3)*3
    for i in range(3):
        for j in range(3):
            if grid[row + i][col + j] == no:
                return False
        
    return True

def possible_val(grid, r, c):
    domain = []
    if grid[r][c] != 0:
        return domain
    for no in range(1,10):
        if is_valid(grid, r, c, no):
            domain.append(no)
    return domain
    
def MRV(grid):
    mini = 1e9
    best_cell = None
    best_domain = [] 
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                domain = possible_val(grid, i, j)
                if len(domain) < mini:
                    mini = len(domain)
                    best_cell = (i, j)
                    best_domain = domain 
                
    return best_cell, best_domain 
    
def LCV(grid, r, c , domain):
    val_count = []
    for val in domain:
        
        temp_grid = copy.deepcopy(grid)
        temp_grid[r][c] = val
        
        false_count = 0
        
        for i in range(9):
            if temp_grid[r][i] == 0 and not is_valid(temp_grid, r, i, val):
                false_count += 1
        
        for i in range(9):
            if temp_grid[i][c] == 0 and not is_valid(temp_grid, i, c, val):
                false_count += 1
                
        row = (r//3)*3
        col = (c//3)*3
        
        for i in range(3):
            for j in range(3):
                new_r = row + i
                new_c = col + j
                
                if temp_grid[new_r][new_c] == 0 and not is_valid(temp_grid, new_r, new_c, val):
                    false_count += 1
                
        val_count.append((val,false_count))
    val_count.sort(key = lambda x : x[1])
    
    return [i[0] for i in val_count]
        
def solve(grid):
    
    cell, domain = MRV(grid) 
    
    if cell is None:
        return True
    row, col = cell
    
    poss_values = LCV(grid, row, col, domain) 
    
    for value in poss_values:
        print("MRV Cell:", row, col, "| LCV Order:", poss_values, "| Assigned:", value)
        
        grid[row][col] = value
        if(solve(grid)):
            return True
            
        grid[row][col] = 0
    
    return False
    
grid = copy.deepcopy(initial_grid)
print("INITIAL GRID:")
for r in grid:
    print(r)

print("\n")
solve(grid)

print("\nFINAL SOLVED GRID:")
for r in grid:
    print(r)
    