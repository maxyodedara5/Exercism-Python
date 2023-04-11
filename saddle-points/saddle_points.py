"""Gives saddle points"""

def saddle_points(matrix):
    """Gives saddle points"""

    saddle_pts = []
    rows = len(matrix)
    if rows == 0:
        return []
    cols = len(matrix[0])
    for row in matrix:
        if len(row) != cols:
            raise ValueError("irregular matrix")

    for row_co in range(rows):
        for col_co in range(cols):
            check_x = row_co
            check_y = col_co
            row_items = []
            col_items = []
            #TODO: Can use better logic for this instead of iterating each element
            for row in range(rows):
                for col in range(cols):
                    if row == check_x:
                        row_items.append(matrix[row][col])
                    if col == check_y:
                        col_items.append(matrix[row][col])

            value = matrix[check_x][check_y]
            row_flag = True
            for item in row_items:
                if value < item:
                    row_flag = False

            col_flag = True
            for item in col_items:
                if value > item:
                    col_flag = False

            if row_flag and col_flag:
                saddle_pts.append({"row": row_co + 1, "column": col_co + 1})

    return saddle_pts
