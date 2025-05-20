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
    
    


    
            
