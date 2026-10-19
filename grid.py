class Grid:
    def __init__(self):
        self.grid = [
            [0, 1, 2, 3],
            [0, 1, 2, 3],
            [0, 1, 2, 3],
            [0, 1, 2, 3],
            [0, 1, 2, 3],
            [0, 1, 2, 3],
        ]

    def get_x_coordinate(self, x):
        return self.grid[x]

    def get_y_coordinate(self, x, y):
        x_row = self.get_x_coordinate(x)
        print(x_row[y])
        y_coordinate = x_row[y]
        return y_coordinate
    
testGrid = Grid()

testGrid.get_y_coordinate(2, 2)


