import numpy as np
import random
import math
import matplotlib.pyplot as plt

class Map:
    _instance = map

    '''def __init__(self, level, size, name, difficulty):
        self.size = size
        self.name = name
        self.rewards = []
        if not (isinstance(size, tuple) and len(size) == 2 and size[0] > 0 and size[1] > 0):
            raise ValueError("Size must be a tuple of two positive integers")
        if difficulty not in [1, 2, 3]:
            raise ValueError("Difficulty must be 1, 2, or 3")
        self.difficulty = difficulty
        self.obstacle = "*"
        diagonal = math.sqrt(max(0, (self.size[0]**2 - self.size[1]**2) / 2))
        self.level = [int(diagonal) - 1, int(diagonal), int(diagonal) + 1]
        #self.random_array = np.zeros(size, dtype=str)
        #self.random_array.fill('0')
        self.arr = np.array = np.zeros(size, dtype=str)
        self.arr = np.zeros(size, dtype=str)
    '''
    def __init__(self, level, size, name, difficulty):
        self.size = size
        self.name = name
        self.rewards = []
        if not (isinstance(size, tuple) and len(size) == 2 and size[0] > 0 and size[1] > 0):
            raise ValueError("size must be a tuple of two positive integer blablabla...")
        if difficulty not in [1, 2, 3]:
            raise ValueError("difficulty must be 1, 2 or 3")
        self.difficulty = difficulty
        self.obstacle = "*"
        self.arrr = np.zeros(size, dtype=str)
        self.arrr.fill('0')

    def add_infos(self,n,m,obs_nub):
        """Initialize the map array with free cells."""
        if n != self.size[0] or m != self.size[1]:
            raise ValueError("Input dimensions must match map size")
        else:
            if self._instance == None:
                self._instance =self
                self.arrr = np.zeros((n, m), dtype=str)
                self.arrr.fill('0')
            else:
                for k in range(obs_nub):
                    x = random.randint(0, n - 1)
                    y = random.randint(0, m - 1)
                    self.arrr[x][y] = '*'

                    

        
        
    def add_obstacle(self, n, m):
        """Add obstacles randomly, stopping at difficulty-based threshold."""
        if n != self.size[0] or m != self.size[1]:
            raise ValueError("Input dimensions must match map size")
        
        target_obstacles = self.level[self.difficulty - 1] if self.difficulty in [1, 2, 3] else 0
        c = 0
        max_attempts = n * m * 2
        attempts = 0

        while c < target_obstacles and attempts < max_attempts:
            i = random.randint(0, n - 1)
            j = random.randint(0, m - 1)
            if self.random_array[i, j] == '0':
                self.random_array[i, j] = self.obstacle
                c += 1
            attempts += 1
    
    def add_obstacle(self,n,m):
        pass
    
    def visualize_map(self):
        """Visualize map with matplotlib."""
        display_array = np.zeros(self.size, dtype=float)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.random_array[i, j] == self.obstacle:
                    display_array[i, j] = 1
                elif self.random_array[i, j] == '0':
                    display_array[i, j] = 0
                else:
                    display_array[i, j] = 0.5
        plt.imshow(display_array, cmap='viridis', interpolation='nearest')
        plt.title(f"Map: {self.name} (Difficulty {self.difficulty})")
        plt.colorbar(label='0: Free, 0.5: Reward, 1: Obstacle')
        plt.savefig('map_visualization.png')
        plt.close()

    def visualize_map_new(self):
        """visualise map with matplotlib"""
        display_array = self.arrr
        c = 0
        print(display_array)

    # Unchanged methods
    def generate_obstacle(self, n, m):
        for i in range(n):
            for j in range(m):
                match self.difficulty:
                    case 1:
                        for i in range(self.level[0]):
                            self.add_obstacle(n, m)
                    case 2:
                        for i in range(self.level[1]):
                            self.add_obstacle(n, m)
                    case 3:
                        for i in range(self.level[2]):
                            self.add_obstacle(n, m)

    def generate_obstacle_new(self, n, m):
        match self.difficulty:
            case 1:
                for i in range(self.level[0]):
                    self.add_obstacle(n, m)
            case 2:
                for i in range(self.level[1]):
                    self.add_obstacle(n, m)
            case 3:
                for i in range(self.level[2]):
                    self.add_obstacle(n, m)

    def generate_table(self, n, m):
        """Generate a table of size n x m with random values."""
        self.random_array = np.zeros(n, m)

    def generate_rewards(self, n, m):
        """Generate a table of size n x m with random rewards for free cells."""
        for i in range(n):
            for j in range(m):
                rand_i = random.randint(0, n-1)
                rand_j = random.randint(0, m-1)
                if self.random_array[rand_i, rand_j] == 0:
                    self.rewards = np.random.rand(1, 3)

# Test script
if __name__ == "__main__":
    m = Map(level=3, size=(6, 6), name="test_map", difficulty=3)
    m.add_infos(6, 6, 6)
    #m.add_obstacle(6, 6) 
    print("Map array:")
    m.visualize_map_new()
    print("\n")
    m.visualize_map_new()
    print(m.random_array)
    m.visualize_map()
    #m.generate_obstacle_new(2,3)
    #m.visualize_map()