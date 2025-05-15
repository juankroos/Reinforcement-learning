class Positions:
    ACTION_UP = "up"
    ACTION_DOWN = "down"
    ACTION_LEFT = "left"
    ACTION_RIGHT = "right"
    ACTION_DIAGONAL_UP = "diagonal_up"
    ACTION_DIAGONAL_DOWN = "diagonal_down"
    ACTION_DIAGONAL_LEFT = "diagonal_left"
    ACTION_DIAGONAL_RIGHT = "diagonal_right"


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

'''
def move(self, action):
        actions = {
            self.ACTION_UP: self.x_pos,
            self.ACTION_DOWN: self.x_neg,
            self.ACTION_LEFT: self.y_neg,
            self.ACTION_RIGHT: self.y_pos,
            self.ACTION_DIAGONAL_UP: lambda: (self.x_pos(), self.y_pos()),
            self.ACTION_DIAGONAL_DOWN: lambda: (self.x_neg(), self.y_neg())
        }
        actions.get(action, lambda: None)()
'''

# Move function
def Move(self, action):
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
