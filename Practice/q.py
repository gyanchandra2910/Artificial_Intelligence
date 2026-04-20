import random
import matplotlib.pyplot as plt


# -------------------------------
# Environment class (Grid World)
# -------------------------------

class ENv:

    def __init__(self):

        # start position
        self.start = (0,0)

        # current state
        self.state = (0,0)

        # goal position
        self.goal = (3,3)

        # obstacles jaha agent nahi ja sakta
        self.obstacles = [(1,1),(2,3)]

        # 4 actions -> up down left right
        self.no_of_action = 4

        # grid size
        self.size = 4


    # state (row,col) ko index me convert karega
    def state_to_index(self,state):
        return state[0]*self.size + state[1]


    # index ko wapas state me convert karega
    def index_to_state(self,index):
        return index//self.size , index%self.size


    # environment reset karega
    def reset(self):
        self.state = self.start
        return self.state_to_index(self.state)


    # action perform karega
    def step(self,action):

        r,c = self.state

        # action define kar rahe hai
        if action == 0:      # up
            r -= 1

        elif action == 1:    # down
            r += 1

        elif action == 2:    # left
            c -= 1

        elif action == 3:    # right
            c += 1


        # boundary check (grid se bahar nahi jana)
        r = max(0,min(self.size-1,r))
        c = max(0,min(self.size-1,c))


        next_state = (r,c)


        # agar goal mil gaya
        if next_state == self.goal:
            self.state = next_state
            return True , 60 , self.state_to_index(self.state)


        # agar obstacle hit hua
        elif next_state in self.obstacles:
            return False , -50 , self.state_to_index(self.state)


        # normal step penalty
        else:
            self.state = next_state
            return False , -1 , self.state_to_index(self.state)



# ---------------------------------
# Q LEARNING
# ---------------------------------

def q_learning(env,episodes=500,alpha=0.1,gamma=0.9,epsilon=0.1):

    # Q table initialize
    Q = [[0.0 for _ in range(4)] for _ in range(16)]

    rewards = []

    for ep in range(episodes):

        state = env.reset()

        done = False
        total_reward = 0

        while not done:

            # epsilon greedy policy
            val = random.uniform(0,1)

            if val < epsilon:
                action = random.randint(0,3)

            else:

                # best action choose
                action = 0
                maxi = Q[state][0]

                for i in range(4):
                    if Q[state][i] > maxi:
                        maxi = Q[state][i]
                        action = i


            done , reward , next_state = env.step(action)

            total_reward += reward


            # next state ka best Q
            max_val_next = max(Q[next_state])


            # Q learning update formula
            Q[state][action] = Q[state][action] + alpha*(reward + gamma*max_val_next - Q[state][action])


            state = next_state


        rewards.append(total_reward)

    return Q , rewards



# ---------------------------------
# Bellman Update
# ---------------------------------

def bellman(env,sweeps=50,gamma=0.9):

    Q = [[0.0 for _ in range(4)] for _ in range(16)]

    rewards = []

    for k in range(sweeps):

        total_reward = 0

        for s in range(16):

            cur_state = env.index_to_state(s)

            # goal state skip
            if cur_state == env.goal:
                continue


            for a in range(4):

                env.state = cur_state

                done , reward , next_state = env.step(a)

                best_next = max(Q[next_state])

                # bellman update
                Q[s][a] = reward + gamma*best_next

                total_reward += reward

        rewards.append(total_reward)

    return Q , rewards



# ---------------------------------
# MAIN PROGRAM
# ---------------------------------

env = ENv()


Q1 , q_rewards = q_learning(env)

Q2 , bellman_rewards = bellman(env)



# ---------------------------------
# GRAPH PLOT
# ---------------------------------

plt.figure(figsize=(8,5))

plt.plot(q_rewards,label="Q Learning")

plt.plot(bellman_rewards,label="Bellman Update")

plt.xlabel("Episodes / Sweeps")

plt.ylabel("Total Reward")

plt.title("Q Learning vs Bellman")

plt.legend()

plt.show()