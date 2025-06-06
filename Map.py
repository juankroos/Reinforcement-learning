import numpy as np
class Map:
    def __init__(self,level,size,name,dificulty):
        self.size = size
        self.name = name
        self.random_array = []
        self.rewards = []
    
        self.level = [ math.sqrt((self.size[0]**2 - self.size[1]**2)/2) - 1 , math.sqrt((self.size[0]**2 - self.size[1]**2)/2) , math.sqrt((self.size[0]**2 - self.size[1]**2)/2) +1]
        self.dificulty = dificulty
        self.obstacle = "*"
    
    # Intialze when the map is full of 0 cells
    def add_obstacle(self, n,m):
        """Add an obstacle to the map."""
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.random_array[i][j] == 0:
                    i = random.randint(0, n-1)
                    j = random.randint(0, m-1)
                    self.random_array[i][j] = self.obstacle

                    #c += 1
                    # Level 1   c >=  math.sqrt((self.size[0]**2 - self.size[1]**2)/2) -1
                    # Level 2   c >=  math.sqrt((self.size[0]**2 - self.size[1]**2)/2) 
                    # Level 3   c >=  math.sqrt((self.size[0]**2 - self.size[1]**2)/2) +1


                    #if c >=  math.sqrt((self.size[0]**2 - self.size[1]**2)/2):
                    #   break
                else:
                    pass
    
    # generate some ramdom obstacle according to the level
    # the number of cell in diagonal is enought to make a reachable path in intervale {diagonal -1, diagonal, diagonal +1} 
    # formula used to find it  math.sqrt((self.size[0]**2 - self.size[1]**2)/2) 
    # level 1: obstacle  randomized of 0 to the diagonal -1
    # level 2: obstacle randomized of 0 to the diagonal 
    # level 3: obstacle randomized of 0 to the diagonal +1

#Fonction finish don't touch it
    def generate_obstacle(n,m):
        for i in range(n):
            for j in range(m):
                match self.dificulty:
                    case 1:
                        for i in range(self.level[0]):
                            add_obstacle(n,m)
                    case 2:
                        for i in range(self.level[1]):
                            add_obstacle(n,m)
                    case 3:
                        for i in range(self.level[2]):
                            add_obstacle(n,m)
                    
    # Same here don't touch it
    def generate_table(self, n,m):
        """Generate a table of size n x m with random values."""
        self.random_array = np.random.rand(n, m)

    # i don't know yet but... don't touch it        
    # Initialize after the initialization of the map
    def generate_rewards(self,n,m):
        """Generate a table of size n x m with random rewards. for free cell"""
        for i in range(n):
            for j in range(m):
                i = random.randint(0, n-1)
                j = random.randint(0, m-1)
                if self.random_array[n,m] == 0:
                    self.rewards = np.random.rand(1,3)



    # The next stpe is to generate random value and the table will be filled by rewards and obstacles ##finish
    # The next step is to make the agent capable of identify obstacle and reward and learn from it to chose the best direction
    # And save those data !!important so if the map is the same the agent will not learn again and just go straight to the goal 
    # The next step is to make the agent capable of identify obstacle and reward and learn from it to chose the best direction
