## we gona strain an aget to find the best way to get from the bottom left to the top right in a table whit variable size
import numpy as np
import matplotlib.pyplot as plt
from random import random

class Agent:
    current_position = (0, 0)
    name = "Agent"
    rewards = []
    total_reward = 0
    def __init__(self, table, rewards, actions):
        self.table = table
        self.rewards = rewards
        #self.actions = actions
        self.current_position = (0, 0)
        self.total_reward = 0

class Positions:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Base move function
    def x_pos():
        self.x += 1

    def y_pos():
        self.y +=  1

    def x_neg():
        if self.x > 0:
            self.x -= 1

    def y_neg():
        if self.y > 0:
            self.y -=  1
        

    def move(self, action):
        match action:
            case "up":
                self.x_pos()
            case "down":
                self.x_neg()
            case "left":
                self.y_neg()    
            case "right":
                self.y_pos()
            case "diagonal_up":
                self.x_pos()
                self.y_pos()
            case "diagonal_down":
                self.x_neg()
                self.y_neg()
            case "diagonal_left":
                self.x_neg()
                self.y_pos()
            case "diagonal_right": 
                self.x_pos()
                self.y_neg()
                
        


class move:
    actions = {"up": (1,0), "down": (-1,0), "left": (0,-1), "right": (0,1), "stay": (0,0),"diagonal": (1,1)}
    up = (1,0)
    down = (-1,0)
    left = (0,-1)
    right = (0,1)
    diagonal = (1,1)
    stay = (0,0)



def generate_table(n, m):
    """Generate a table of size n x m with random values."""
    return np.random.rand(n, m)

def generate_rewards(n, m):
    """Generate a table of rewards for each cell."""
    return np.random.rand(n, m)



    
    
            
