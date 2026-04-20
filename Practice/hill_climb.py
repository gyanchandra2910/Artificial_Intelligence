import copy 
import random

GOAL = [[1, 2, 3],
        [4, 5, 6], 
        [7, 8, 0]]
        
START = [[3, 4, 8], 
         [6, 0, 7], 
         [5, 2, 1]]

def get_zero_pos(grid):
  for i in range(3):
    for j in range(3):
      if grid[i][j] == 0:
        return i, j
    
  return None, None

def heuristic(grid, goal):
  score = 0
  for i in range(3):
    for j in range(3):
      # Minor correction: Waise toh 0 ko ginne se bhi code chalega, 
      # par standard rule ye hai ki empty space (0) ko error mein nahi ginte.
      if grid[i][j] != 0 and grid[i][j] != goal[i][j]:
        score += 1
  return score

def moves(grid):
  # MISTAKE 1: Python lists mein .size() method nahi hota, len() function hota hai.
  n = len(grid)      # FIXED: grid.size() -> len(grid)
  m = len(grid[0])   # FIXED: grid[0].size() -> len(grid[0])
  
  x, y = get_zero_pos(grid)
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]
  grids = []
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      temp = copy.deepcopy(grid)
      val = temp[nx][ny]
      temp[x][y] = val
      temp[nx][ny] = 0

      grids.append(temp)
  return grids

def solve(start, goal):
  cur_score = heuristic(start, goal)
  
  # PRINTING: Ye step add kiya hai taaki path dikhe
  print("Current Grid:")
  for row in start:
      print(row)
  print("Heuristic Score:", cur_score, "\n")

  if cur_score == 0:
    print("🎉 Goal Reached!")
    return True

  neighbour = moves(start)
  change = False
  best_neighbour = []
  
  for grid in neighbour:
    score = heuristic(grid, goal)
    if score < cur_score:
      best_neighbour = grid
      cur_score = score
      change = True
  
  if change == False:
    print("❌ Cant solve (Stuck at local minima)")
    return False # FIXED: Khali return ki jagah return False dena zyada theek hai.

  # MISTAKE 2: Recursion call ke aage return lagana zaroori hai.
  return solve(best_neighbour, goal) # FIXED: Added 'return' before solve()


# ==========================================
# NEW FIXES IN RANDOM BOARD & EXECUTION
# ==========================================

def get_random_board(grid):
    # FIXED: Original grid ko change na kare, isliye deepcopy banaya
    nums = copy.deepcopy(grid) 
    
    # FIXED: 'i' ko '_' kar diya taaki get_zero_pos wale (i, j) se clash na kare
    for _ in range(50):
        # FIXED: Function ka sahi naam 'get_zero_pos' hai, 'get_zero_location' nahi
        i, j = get_zero_pos(nums) 
        
        # FIXED: moves() function ke andar loop wala 'nums' pass karna hai, original 'grid' nahi
        neighbour = moves(nums)
        
        # FIXED: Tera code random.ch par kat gaya tha, usko poora kiya
        nums = random.choice(neighbour) 
        
    return nums

# FIXED: Ab isko multiple times (Iterative) chalane ke liye ek loop me daal diya
def run_iterative_hill_climbing():
    for iteration in range(1, 16):
        print("====================================")
        print(f"🔄 Iteration : {iteration}")
        
        # GOAL board se 50 ulte moves chalkar naya board mangwaya
        random_start = get_random_board(GOAL)
        
        # Apne recursive function ko call kiya
        success = solve(random_start, GOAL)
        
        if success:
            print(f"🏆 Algorithm won in Iteration {iteration}!")
            break
        else:
            print(f"Retrying...\n")

# Program yahan se start hoga
run_iterative_hill_climbing()