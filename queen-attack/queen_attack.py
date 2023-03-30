"""Queen has co-ordinates and function to see if can attack other queen object"""

def pos_diagonal_positions(row,column):
    """diagonal_positions """
    x_grid = row
    y_grid = column
    end_reached = True
    attack_pos = []
    while end_reached:
        x_grid += 1
        y_grid += 1
        if x_grid == 8 or y_grid == 8:
            end_reached = False
            break
        attack_pos.append((x_grid,y_grid))

    x_grid = row
    y_grid = column
    end_reached = True
    while end_reached:
        x_grid -= 1
        y_grid -= 1
        if x_grid == -1 or y_grid == -1:
            end_reached = False
            break
        attack_pos.append((x_grid,y_grid))

    return attack_pos


def neg_diagonal_positions(row,column):
    """diagonal_positions """
    x_grid = row
    y_grid = column
    end_reached = True
    attack_pos = []
    while end_reached:
        x_grid += 1
        y_grid -= 1
        if x_grid == 8 or y_grid == -1:
            end_reached = False
            break
        attack_pos.append((x_grid,y_grid))

    x_grid = row
    y_grid = column
    end_reached = True
    while end_reached:
        x_grid -= 1
        y_grid += 1
        if x_grid == -1 or y_grid == 8:
            end_reached = False
            break
        attack_pos.append((x_grid,y_grid))

    return attack_pos

class Queen:
    """Queen has co-ordinates and function to see if can attack other queen object"""
    def __init__(self, row, column):

        # if the row parameter is negative
        if row < 0:
            raise ValueError("row not positive")

        # if the row parameter is not on the defined board
        if row > 7:
            raise ValueError("row not on board")

        # if the column parameter is negative
        if column < 0:
            raise ValueError("column not positive")

        # if the column parameter is not on the defined board
        if column > 7:
            raise ValueError("column not on board")

        self.row = row
        self.column = column
        self.attack_positions = []
        # Horizontal and vertical attack positions
        for grid in range(8):
            self.attack_positions.append((self.row, grid))
            self.attack_positions.append((grid, self.column))

        # \ attack position
        self.attack_positions += pos_diagonal_positions(row, column)
        # / attack position
        self.attack_positions += neg_diagonal_positions(row, column)

        # Unique positions
        self.attack_positions = list(set(self.attack_positions))
        self.attack_positions.remove((self.row, self.column))

    def can_attack(self, another_queen):
        """If both the queens are on the same location"""
        if another_queen.row == self.row and another_queen.column == self.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        if (another_queen.row, another_queen.column) in self.attack_positions:
            return True

        return False
