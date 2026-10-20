class Grid:
    def __init__(self):
        self.grid = [
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
        ]

    def get_y_coordinate(self, y):
        return self.grid[y]

    def get_x_coordinate(self, x, y):
        y_row = self.get_y_coordinate(y)
        print(y_row[x])
        x_coordinate = y_row[x]
        return x_coordinate



testGrid = Grid()

testGrid.get_x_coordinate(2, 2)


