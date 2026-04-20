import random

def cost(grid):
  n = len(grid)
  cost_val = 0 # Variable ka naam 'cost_val' kar diya taaki function naam (cost) se clash na kare
  for i in range(n):
    for j in range(i + 1, n):
      # MISTAKE 1: Tune bracket galat jagah close kiya tha. 
      # Tune likha tha: abs(grid[i] - grid[j] == abs(i - j)) -> Ye andar condition check kar raha hai.
      # FIXED: Sahi syntax hoga dono ko alag abs() mein rakhna.
      if grid[i] == grid[j] or abs(grid[i] - grid[j]) == abs(i - j):
        cost_val += 1
  return cost_val

def solve(n):
  while True:
    board = [random.randint(0, n - 1) for _ in range(n)]
    while True:
      curr_cost = cost(board)
      if curr_cost == 0:
        return board
      
      # MISTAKE 2 (SABSE BADI GALTI): Tune sirf `best_board = board` likha tha.
      # Python mein isse nayi list nahi banti, bas ek naya naam mil jata hai usi list ko.
      # Jab tu neeche `board[row] = col` karega, toh `best_board` bhi apne aap change ho jayega!
      # FIXED: `list(board)` use karna padega taaki ek duplicate copy bane.
      best_board = list(board)
      min_cost = curr_cost
      
      for row in range(n):
        orig_col = board[row]
        for col in range(n):
          if col != orig_col:

            board[row] = col
            new_cost = cost(board)

            if new_cost < min_cost:
              min_cost = new_cost
              # MISTAKE 3: Yahan bhi naye board ki COPY save karni padegi.
              # FIXED: best_board = list(board)
              best_board = list(board)
            
            # Backtrack
            board[row] = orig_col

      if min_cost >= curr_cost:
        break

      board = best_board 

# MISTAKE 4: Tune code mein solve() function banaya, par usko call (run) hi nahi kiya!
# FIXED: Function call aur print statement add kiya.
res = solve(8)
print("Solution mil gaya:", res)