def is_game_over(grid):
  # Check Rows and Columns
  for i in range(3):
    if grid[i][0] == grid[i][1] and grid[i][0] == grid[i][2] and grid[i][0] != ' ':
      return grid[i][0]
  
  for i in range(3):
    if grid[0][i] == grid[1][i] and grid[0][i] == grid[2][i] and grid[0][i] != ' ':
      return grid[0][i]
    
  # MISTAKE 1: Diagonal check mein tu `!= ' '` lagana bhool gaya tha. 
  # Aur second diagonal mein `grid[2][1]` likh diya tha jo ki `grid[2][0]` hona chahiye!
  # FIXED:
  if grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2] and grid[0][0] != ' ':
    return grid[0][0]

  if grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0] and grid[0][2] != ' ':
    return grid[0][2]
  
  return None # Agar koi na jeete toh kuch return nahi karna chahiye
  
def is_board_full(grid):
  for i in range(3):
    for j in range(3):
      if grid[i][j] == ' ':
        return False
  return True

def print_board(grid):
  # MISTAKE 2: Puraane print wale logic se matrix ajeeb print hoti.
  # FIXED: Acha format laga diya
  print("\n")
  for i in range(3):
    print(f" {grid[i][0]} | {grid[i][1]} | {grid[i][2]} ")
    if i < 2:
        print("---+---+---")
  print("\n")

def min_max(grid, depth, alpha , beta):
  check = is_game_over(grid)
  if check == 'X':
    return 1  # AI (Maximizer) jeeta
  if check == 'O':
    return -1 # User (Minimizer) jeeta
  if is_board_full(grid):
    return 0

  # Maximizer's block (AI 'X')
  if depth % 2 == 0:
    best_score = -1e9
    for i in range(3):
      for j in range(3):
        if grid[i][j] == ' ':
          grid[i][j] = 'X'
          score = min_max(grid, depth + 1, alpha, beta)
          grid[i][j] = ' '
          
          if score > best_score:
            best_score = score
            
          # MISTAKE 3: Alpha update aise karna better hota hai
          alpha = max(alpha, best_score)
          
          if alpha >= beta:
            break # return ki jagah break use karna standard approach hai
            
    # MISTAKE 4 (SABSE BADI GALTI): Tune loop khatam hone ke baad best_score return hi nahi kiya tha!
    # FIXED: Added return
    return best_score

  # Minimizer's block (User 'O')
  else :
    best_score = 1e9
    for i in range(3):
      for j in range(3):
        if grid[i][j] == ' ':
          grid[i][j] = 'O'
          score = min_max(grid, depth + 1, alpha, beta)
          grid[i][j] = ' '
          
          if score < best_score:
            best_score = score
            
          # FIXED: Beta update
          beta = min(beta, best_score)
          
          if alpha >= beta:
            break # FIXED
            
    # MISTAKE 5: Yahan bhi loop ke bahar return lagana zaroori hai!
    return best_score
        
# MISTAKE 6: Grid galat banayi thi -> `[[' ', ' ', ' '] , []]`
# FIXED: Sahi 3x3 array banaya
grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

print("User is 'O' and AI is 'X'")
print_board(grid)

while(True):
  print("Your turn 'O'")
  row = int(input("Row (0, 1, 2): "))
  col = int(input("Col (0, 1, 2): "))

  # Basic check agar spot already bhara ho
  if grid[row][col] != ' ':
      print("Invalid move, spot taken!")
      continue

  grid[row][col] = 'O'
  print_board(grid)

  # MISTAKE 7: User move ke baad win/draw check missing tha
  if is_game_over(grid) == 'O':
      print("You Win!")
      break
  if is_board_full(grid):
      print("Draw!")
      break

  print("AI is thinking...")
  r, c = None, None
  best_score = -1e9
  for i in range(3):
    for j in range(3):
      if grid[i][j] == ' ':
        grid[i][j] =  'X'
        score = min_max(grid, 1, -1e9, 1e9)
        grid[i][j] = ' '

        if score > best_score:
          # MISTAKE 8: Tune galti se `score = best_score` likh diya tha, ulta assign ho gaya tha!
          # FIXED:
          best_score = score
          
          # MISTAKE 9: `r = i, c = j` invalid Python syntax hai
          # FIXED: `r, c = i, j`
          r, c = i, j
      
  grid[r][c] = 'X'
  print_board(grid)

  # MISTAKE 10: AI move ke baad win/draw check missing tha
  if is_game_over(grid) == 'X':
      print("AI Wins!")
      break
  if is_board_full(grid):
      print("Draw!")
      break