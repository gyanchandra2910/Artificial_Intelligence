import random

class Env:
  
  # FIX 1: _init__ se __init__ kar diya
  def __init__(self):
    self.start = (0, 0)
    self.state = (0, 0)
    self.goal = (3,3)
    self.obstacles = [(1,1), (2, 3)]
    self.no_of_action = 4
    self.size = 4

  def reset(self):
    self.state = self.start
    return self.state_to_index(self.state)
  
  def index_to_state(self, index):
    # FIX 2: index ka use karke row, col calculate kiya
    return (index // self.size, index % self.size)
  
  def state_to_index(self, state):
    return state[0] * self.size + state[1]
  
  def step(self, action):
    r, c = self.state
    if action == 0:
      r = max(r - 1, 0)
    elif action == 1:
      r = min(self.size - 1, r + 1)
    elif action == 2:
      c = max(0, c - 1)
    elif action == 3:
      c = min(c + 1, self.size - 1)

    next_state = (r, c)

    if next_state == self.goal:
      self.state = next_state # FIX 3: State update kiya
      # FIX 4: Hamesha index return karenge taaki Q-table read ho sake
      return True, 20, self.state_to_index(next_state) 
    
    if next_state in self.obstacles:
      # Obstacle mein gird gaya, wahi rahega
      return False, -5, self.state_to_index(self.state)
    
    self.state = next_state # FIX 3: State update kiya
    return False, -1, self.state_to_index(next_state)


def q_learning(env, episode = 500, alpha = 0.1, gamma = 0.9, epsilon = 0.1):
  Q = [[0.0 for _ in range(4)] for _ in range(16)]

  for i in range(episode):
    state = env.reset()
    done = False
    while not done:
      val = random.uniform(0, 1)
      if val < epsilon:
        action = random.randint(0, 3)
      else:
        action = 0
        maxi = Q[state][action]
        for a in range(4): # 'i' loop variable overlap se bachne ke liye 'a' use kiya
          if Q[state][a] > maxi:
            action = a
            maxi = Q[state][a]
        
      done, reward, next_state = env.step(action)

      best_next_state = max(Q[next_state])

      Q[state][action] = Q[state][action] + alpha * (reward + gamma*(best_next_state - Q[state][action]))

      state = next_state
  return Q


# FIX 5: sweeps aur gamma ko default value de di
def bellman(env, sweeps=50, gamma=0.9): 
  Q = [[0.0 for _ in range(4)] for _ in range(16)]
  for i in range(sweeps):
    for s in range(16):
      state_coordinate = env.index_to_state(s)

      if state_coordinate == env.goal:
        continue

      for a in range(4):
        env.state = state_coordinate
        # FIX 4 (update): Step return order match kiya (done, reward, next_state)
        done, reward, next_state = env.step(a) 

        best_next_val = max(Q[next_state])
        Q[s][a] = reward + gamma*best_next_val
        
  return Q # FIX 5: Function se Q table bahar bheji


# FIX 6: Function ka naam badal kar print_policy kiya
def print_policy(Q, env, title="Policy"):
  print(f"\n--- {title} ---")
  action = ["UP", "DOWN", "LEFT", "RIGHT"]
  for s in range(16):
    coords = env.index_to_state(s)

    if coords == env.goal:
      print("state", coords, "->", "GOAL")
    elif coords in env.obstacles: # FIX: self.obstacles ki jagah env.obstacles
      print("state", coords, "->", "OBSTACLE")
    else:
      best_action = Q[s].index(max(Q[s]))
      print("state", coords, "->", action[best_action])


# --- Main Execution ---
env = Env()

q = q_learning(env)
q_bell = bellman(env) # Default values set kar di hai sweeps aur gamma ki 

print_policy(q, env, "Q-Learning Output")
print_policy(q_bell, env, "Bellman Equation Output")