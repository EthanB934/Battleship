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
        x_coordinate = y_row[x]
        return x_coordinate

    def update_x_coordinate(self, x, y):
        y_row = self.get_y_coordinate(y)
        y_row[x] = True
        
    def check_placement(self, y1, x1, y2, x2):

        try:
            y1_y2_difference = abs(y1 - y2)
            if(y1_y2_difference > 1):
                error_message = "The y-coordinates provided are two far from one another. Destroyers are two spaces in length"
                return error_message
        except: 
            
            is_y1_x1_available = self.get_x_coordinate(y1, x1)
            is_y2_x2_available = self.get_x_coordinate(y2, x2)

            if not is_y1_x1_available and not is_y2_x2_available:
                return True
  

        
    def place_destroyer_vertically(self, y1_x1, y2_x2):
            y1, x1 = y1_x1
            y2, x2 = y2_x2

            is_placement_valid = self.check_placement(y1, x1, y2, x2)

            if(is_placement_valid):
                self.update_x_coordinate(y1, x1)
                self.update_x_coordinate(y2, x2)

            print(self.grid)


testGrid = Grid()

testGrid.place_destroyer_vertically((2, 2), (0, 0))


