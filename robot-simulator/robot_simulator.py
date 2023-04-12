"""Robot closs for simulation"""
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"


directions_list = [WEST, NORTH, EAST, SOUTH]
# L -1, R + 1
co_ord_addition = [(-1,0), (0,1), (1,0), (0,-1)]
class Robot:
    """Robot closs for simulation"""
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (self.x_pos, self.y_pos)

    def move(self, directions):
        """Move robot according to the direction string"""
        for letter in directions:
            if letter == 'L':
                current_dir_index = directions_list.index(self.direction)
                current_dir_index -= 1
                if current_dir_index < 0:
                    current_dir_index = len(directions_list) - 1
                self.direction = directions_list[current_dir_index]

            if letter == 'R':
                current_dir_index = directions_list.index(self.direction)
                current_dir_index += 1
                if current_dir_index == len(directions_list):
                    current_dir_index = 0
                self.direction = directions_list[current_dir_index]

            if letter == 'A':
                current_dir_index = directions_list.index(self.direction)
                self.x_pos += co_ord_addition[current_dir_index][0]
                self.y_pos += co_ord_addition[current_dir_index][1]
                self.coordinates = (self.x_pos, self.y_pos)
