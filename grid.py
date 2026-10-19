class Grid:
    def __init__(self):
        self.grid = [
            [[0], [1], [2], [3]],
            [[0], [1], [2], [3]],
            [[0], [1], [2], [3]],
            [[0], [1], [2], [3]],
            [[0], [1], [2], [3]],
        ]

    def get_x_coordinate(self, x):
        print(self.grid[x])
        return self.grid[x]


testGrid = Grid()

testGrid.get_x_coordinate(2)


