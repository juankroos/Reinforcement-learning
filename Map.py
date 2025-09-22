import numpy as np
import random
import math
import matplotlib.pyplot as plt


class Map:
    def __init__(self,level,size,name,difficulty):
        self.size = size
        self.name = name
        self.random_array = []
        self.rewards = []
        diagonal = math.sqrt(max(0, (self.size[0]**2 - self.size[1]**2) / 2))
        self.level = [int(diagonal) - 1, int(diagonal), int(diagonal) + 1]
        self.difficulty = difficulty
        self.obstacle = "*"
        self.random_array = np.zeros(size, dtype=str)  # Initialize with zeros
    
    # Intialze when the map is full of 0 cells
    def add_obstacle(self, n, m):
        """Add obstacles to the map based on difficulty level, stopping at the level-specific threshold."""
        # Determine the number of obstacles based on difficulty
        if self.difficulty == 1:
            target_obstacles = self.level[0]
        elif self.difficulty == 2:
            target_obstacles = self.level[1]
        elif self.difficulty == 3:
            target_obstacles = self.level[2]
        else:
            target_obstacles = 0  # Default to no obstacles for invalid difficulty

        # Counter for placed obstacles
        c = 0
        max_attempts = n * m * 2  # Avoid infinite loops
        attempts = 0

        while c < target_obstacles and attempts < max_attempts:
            # Randomly select a cell
            i = random.randint(0, n - 1)
            j = random.randint(0, m - 1)
            # Place obstacle only if cell is free (0)
            if self.random_array[i, j] == 0:
                self.random_array[i, j] = self.obstacle
                c += 1
            attempts += 1
    
    # generate some ramdom obstacle according to the level
    # the number of cell in diagonal is enought to make a reachable path in intervale {diagonal -1, diagonal, diagonal +1} 
    # formula used to find it  math.sqrt((self.size[0]**2 - self.size[1]**2)/2) 
    # level 1: obstacle  randomized of 0 to the diagonal -1
    # level 2: obstacle randomized of 0 to the diagonal 
    # level 3: obstacle randomized of 0 to the diagonal +1

#Fonction finish don't touch it
    def generate_obstacle(self,n,m):
        for i in range(n):
            for j in range(m):
                match self.difficulty:
                    case 1:
                        for i in range(self.level[0]):
                            self.add_obstacle(n,m)
                    case 2:
                        for i in range(self.level[1]):
                            self.add_obstacle(n,m)
                    case 3:
                        for i in range(self.level[2]):
                            self.add_obstacle(n,m)
                    
    # Same here don't touch it
    def generate_table(self, n,m):
        """Generate a table of size n x m with random values."""
        self.random_array = np.zeros(n, m)

    # i don't know yet but... don't touch it        
    # Initialize after the initialization of the map
    def generate_rewards(self,n,m):
        """Generate a table of size n x m with random rewards. for free cell"""
        for i in range(n):
            for j in range(m):
                rand_i = random.randint(0, n-1)
                rand_j = random.randint(0, m-1)
                if self.random_array[rand_i,rand_j] == 0:
                    self.rewards = np.random.rand(1,3)



    # The next stpe is to generate random value and the table will be filled by rewards and obstacles ##finish
    # The next step is to make the agent capable of identify obstacle and reward and learn from it to chose the best direction
    # And save those data !!important so if the map is the same the agent will not learn again and just go straight to the goal 
    # The next step is to make the agent capable of identify obstacle and reward and learn from it to chose the best direction
if __name__ == "__main__":
    map1 = Map(1,(10,10),"map1",2)
    a = map1.generate_obstacle(10,10)
    print(map1.random_array)
    print(map1.rewards)