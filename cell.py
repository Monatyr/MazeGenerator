class Cell:

    def __init__(self, neighbours):
        self.visited = False
        self.neighbours = neighbours #left, upper, right, bottom
        self.walls = [True for _ in range(4)] #left, upper, right, bottom


    def add_neighbours(self, new_neighbours):
        self.neighbours = new_neighbours

