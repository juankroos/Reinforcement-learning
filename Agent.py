## we gona strain an aget to find the best way to get from the bottom left to the top right in a table whit variable size
import numpy as np
import matplotlib.pyplot as plt
from random import random
from position import Positions

class Agent(Positions):
    current_position = (0, 0)
    name = "Agent"
    rewards = []
    total_reward = 0

    def __init__(self, table, rewards,level, actions):
        self.table = table
        self.rewards = rewards
        self.level = level
        #self.actions = actions
        self.current_position = (0, 0)
        self.total_reward = 0
        self.x = 0
        self.y = 0
        self.q_table = {} # up, down , left, right
        for i in range(table.size[0]):
            for j in range(table.size[1]):
                self.q_table[(i,j)] = {0.0,0.0,0.0,0.0}
        
        self.actions = {
    "up": (0, 1),         # +y
    "down": (0, -1),      # -y
    "right": (1, 0),      # +x
    "left": (-1, 0),      # -x
    "up_right": (1, 1),   # +x, +y
    "up_left": (-1, 1),   # -x, +y
    "down_right": (1, -1),# +x, -y
    "down_left": (-1, -1),# -x, -y
    "stay": (0, 0)
}

    def fill_q_table(self, state, action, reward, next_state, alpha, gamma):
        """update the q_table using the Q-learning algorithm"""
        max_future_q = max(self.q_table[next_state])
        current_q = self.q_table[state][action]
        new_q = (1 - alpha) * current_q + alpha * (reward + gamma * max_future_q)
        self.q_table[state][action] = new_q


    def deplacement(self,x,y):
        """move the agent to a new location"""
        if (x < 0 or x >= self.table.size[0]) or (y < 0 or y >= self.table.size[1]):
            raise ValueError("new position is out of bounds")
        if self.table.arrr[x][y] == '*':
            raise ValueError("nw position is an obstacle")
        self.current_position = (x, y)
        self.x = x
        self.y = y

    def check():
        """check if the agent is at the goal position"""
        return self.current_position == (self.table.size[0] - 1, self.table.size[1] - 1)
    
    

# next steap make de decision process

# next steap make the choices process
# next steap make the learning process