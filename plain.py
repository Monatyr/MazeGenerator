import random
from cell import Cell
import numpy as np

class Plain:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[Cell(None) for _ in range(width)] for _ in range(height)]
        self.start_cell = self.grid[self.height//2][0]
        self.end_cell = self.grid[self.height//2][self.width-1]

        for i, row in enumerate(self.grid):
            for j, el in enumerate(row):
                new_neighbours = []
                if j != 0:
                    new_neighbours.append(self.grid[i][j-1])
                else:
                    new_neighbours.append(None)
                if i != 0:
                    new_neighbours.append(self.grid[i-1][j])
                else:
                    new_neighbours.append(None)
                if j != self.width-1:
                    new_neighbours.append(self.grid[i][j+1])
                else:
                    new_neighbours.append(None)
                if i != self.height-1:
                    new_neighbours.append(self.grid[i+1][j])
                else:
                    new_neighbours.append(None)
                
                el.add_neighbours(new_neighbours)

                
    def draw(self):
        for i, row in enumerate(self.grid):
            for j, el in enumerate(row):
                print(len(list(filter(lambda x : x is not None and x.visited == False, el.neighbours))), end="")
            print()


    def create_dfs_maze(self, starting_cell: Cell):
        starting_cell.visited = True
        indices = list(range(4))
        random.shuffle(indices)
        for index in indices:
            el = starting_cell.neighbours[index]
            if el and not el.visited:
                starting_cell.walls[index] = False
                el.walls[(index-2)%4] = False
                self.create_dfs_maze(el)

    
    def create_kruskal_maze(self):
        #komórki indeksowane od 0; index*2 == prawa pionowa ściana; index*2 + 1 == dolna pozioma ściana
        #pionowe ściany - parzysty y
        #poziome ścainy - 
        walls = np.zeros((2*self.height, 2*self.width), dtype=object)
        for i in range(2*self.height):
            for j in range(2*self.width):
                walls[i][j] = (i,j)
        walls = walls.flatten()
        np.random.shuffle(walls)
        cells = [[set([el]) for j, el in enumerate(row)] for i, row in enumerate(self.grid)]
        
        for wall in walls:
            if 0: #pozioma ściana:
                pass
            else: #pionowa ściana:
                pass



    def solve(self, current_pos):
        for i, row in enumerate(self.grid):
            for j, el in enumerate(row):
                el.visited = False

        return self.solve_step(current_pos)

    def solve_step(self, current_pos):
        current_cell = self.grid[current_pos[0]][current_pos[1]]
        current_cell.visited = True
        if current_cell == self.end_cell:
            return [(current_pos)]
        indices = list(range(4))
        random.shuffle(indices)
        for index in indices:
            neighbour = current_cell.neighbours[index]
            if index == 0: neighbour_pos = (current_pos[0], current_pos[1]-1)
            elif index == 1: neighbour_pos = (current_pos[0]-1, current_pos[1])
            elif index == 2: neighbour_pos = (current_pos[0], current_pos[1]+1)
            elif index == 3: neighbour_pos = (current_pos[0]+1, current_pos[1])
            if not current_cell.walls[index] and not neighbour.visited:
                res = self.solve_step(neighbour_pos)
                if res:
                    res.append(current_pos)
                    return res
        return None



if __name__ == "__main__":
    plain = Plain(3,3)
    # plain.draw()
    # plain.create_dfs_maze(plain.grid[0][0])
    # plain.show_walls()
    plain.create_kruskal_maze()